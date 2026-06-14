"""
fedavg_fedprox_krum_demo.py
---------------------------
From-scratch federated-learning teaching demo: ~6 non-IID clients do local
training, the server aggregates with FedAvg, FedProx's proximal term damps
client drift, then one poisoned client is injected and Krum + coordinate-wise
median reject it while plain FedAvg is corrupted.

This is the FED-01 + FED-02a hands-on demo for interview preparation.

Dependencies: numpy  (from-scratch; no Flower/PySyft dependency)
Run:          python3 fedavg_fedprox_krum_demo.py
Output:       Console: before/after contrast table (no plot file generated)

Non-IID client scenario:
  N_CLIENTS=6, TRUE_MEANS=[0.0,0.5,1.0,1.5,2.0,2.5], N_SAMPLES=[50,80,60,90,70,40],
  SIGMA=0.3, LOCAL_EPOCHS=10, N_ROUNDS=20, MU_FEDPROX=0.5,
  POISON_CLIENT=0, POISON_MAGNITUDE=5.0
"""
import numpy as np


# ---------------------------------------------------------------------------
# Non-IID client scenario constants
# ---------------------------------------------------------------------------
N_CLIENTS        = 6
TRUE_MEANS       = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]   # each client's local optimum (different feeders)
N_SAMPLES        = [50, 80, 60, 90, 70, 40]           # heterogeneous client sizes
SIGMA            = 0.3                                 # within-client noise
LOCAL_EPOCHS     = 10
N_ROUNDS         = 20
LR               = 0.1                                 # local SGD learning rate
MU_FEDPROX       = 0.5                                 # proximal coefficient
POISON_CLIENT    = 0
POISON_MAGNITUDE = 5.0                                 # client 0 sends global - 5.0


# ---------------------------------------------------------------------------
# Client data generation
# ---------------------------------------------------------------------------

def generate_clients(n_clients, true_means, n_samples, sigma):
    """Generate n_clients non-IID datasets; each sampled from N(mu_k, sigma^2)."""
    clients = []
    for k in range(n_clients):
        data = np.random.normal(true_means[k], sigma, n_samples[k])
        clients.append((data, n_samples[k]))
    return clients


# ---------------------------------------------------------------------------
# Local training helpers
# ---------------------------------------------------------------------------

def local_sgd(w, data, lr, epochs):
    """FedAvg local training: plain gradient steps on 1-D mean estimation.

    Loss: F_k(w) = mean((w - x)^2)   grad = 2 * mean(w - x)
    """
    w = float(w)
    for _ in range(epochs):
        grad = 2.0 * np.mean(w - data)
        w -= lr * grad
    return w


def fedprox_local_step(w_local, w_global, data, lr, epochs, mu):
    """FedProx local training: gradient steps + proximal term mu*(w_local - w_global).

    Minimizes F_k(w) + (mu/2)||w - w_global||^2 — the proximal term penalizes
    deviation from the global model, damping client drift under non-IID data.
    """
    w = float(w_local)
    w_g = float(w_global)
    for _ in range(epochs):
        grad = 2.0 * np.mean(w - data)
        proximal_grad = mu * (w - w_g)      # gradient of (mu/2)||w - w_t||^2
        w -= lr * (grad + proximal_grad)
    return w


# ---------------------------------------------------------------------------
# Aggregation helpers
# ---------------------------------------------------------------------------

def fedavg_aggregate(local_models, n_samples):
    """Server aggregation: weighted average sum((n_k / n) * w_k)."""
    n_total = sum(n_samples)
    return sum((n / n_total) * w for n, w in zip(n_samples, local_models))


def krum_select(updates, f):
    """Krum: pick the update with minimum sum-of-distances to its n-f-2 nearest neighbors.

    Blanchard et al. NIPS 2017 — honest updates cluster together; the poisoned
    update is far from the cluster so its Krum score is high (never selected).
    Returns the index of the selected (most trustworthy) update.
    """
    n = len(updates)
    n_neighbors = n - f - 2
    scores = []
    for i, u_i in enumerate(updates):
        dists = sorted(
            [(u_i - u_j) ** 2 for j, u_j in enumerate(updates) if j != i]
        )
        scores.append(sum(dists[:n_neighbors]))
    return int(np.argmin(scores))


def coord_median(updates):
    """Coordinate-wise median — robust to up to n/2-1 Byzantine clients."""
    return float(np.median(np.stack(updates), axis=0))


def inject_poison(updates, client_idx, magnitude):
    """Replace updates[client_idx] with a poisoned value (large negative shift)."""
    poisoned = list(updates)
    # Poison: shift to pull the global model far from the honest cluster
    poisoned[client_idx] = updates[client_idx] - magnitude
    return poisoned


# ---------------------------------------------------------------------------
# Main demo
# ---------------------------------------------------------------------------

def run_demo():
    """Run the full FedAvg / FedProx / Krum / coord-median teaching demo."""
    np.random.seed(42)

    # ---- True global optimum = weighted mean of client local optima ----
    n_total = sum(N_SAMPLES)
    true_global = sum(
        (n / n_total) * mu for n, mu in zip(N_SAMPLES, TRUE_MEANS)
    )   # ~1.22

    # ---- Generate non-IID client datasets ----
    clients = generate_clients(N_CLIENTS, TRUE_MEANS, N_SAMPLES, SIGMA)
    datasets   = [c[0] for c in clients]
    n_samples  = [c[1] for c in clients]

    # ---- Run 1: Plain FedAvg (N_ROUNDS rounds, LOCAL_EPOCHS local steps) ----
    w_fedavg = 0.0
    for _ in range(N_ROUNDS):
        local_models = [
            local_sgd(w_fedavg, data, LR, LOCAL_EPOCHS)
            for data in datasets
        ]
        w_fedavg = fedavg_aggregate(local_models, n_samples)

    # ---- Run 2: FedProx (same rounds; clients add proximal term) ----
    w_fedprox = 0.0
    for _ in range(N_ROUNDS):
        local_models_prox = [
            fedprox_local_step(w_fedprox, w_fedprox, data, LR, LOCAL_EPOCHS, MU_FEDPROX)
            for data in datasets
        ]
        w_fedprox = fedavg_aggregate(local_models_prox, n_samples)

    # ---- Byzantine demo: one poisoned round, three aggregation strategies ----
    # Take honest local updates from a single round starting at the FedProx estimate
    # (a reasonable converged global model) — then inject poison on client 0
    w_ref = w_fedprox
    honest_updates = [
        local_sgd(w_ref, data, LR, LOCAL_EPOCHS) for data in datasets
    ]
    poisoned_updates = inject_poison(honest_updates, POISON_CLIENT, POISON_MAGNITUDE)

    # (a) Plain FedAvg on the poisoned set
    w_plain_poisoned = fedavg_aggregate(poisoned_updates, n_samples)

    # (b) Krum: select the honest update (poisoned client has highest Krum score)
    selected_idx = krum_select(poisoned_updates, f=1)
    w_krum = poisoned_updates[selected_idx]

    # (c) Coordinate-wise median: ignores the outlier
    w_median = coord_median(poisoned_updates)

    # ---- Console output ----
    print("=" * 56)
    print("  FedAvg / FedProx / Byzantine Robustness Demo")
    print("=" * 56)
    print()
    print(f"  Clients: {N_CLIENTS}   Local epochs: {LOCAL_EPOCHS}   "
          f"Rounds: {N_ROUNDS}   Poison: client {POISON_CLIENT} (shift -{POISON_MAGNITUDE:.1f})")
    print(f"  True global optimum: {true_global:.2f}")
    print()
    print("  Method             | Final Estimate | Error  | Notes")
    print("  -------------------|----------------|--------|---------------------------")

    rows = [
        ("Plain FedAvg",
         w_plain_poisoned,
         "Poisoned -- client 0 pulled it off"),
        (f"FedProx (mu={MU_FEDPROX})",
         w_fedprox,
         "Proximal term kept local models near global"),
        (f"Krum (f=1) [client {selected_idx}]",
         w_krum,
         f"Rejected client {POISON_CLIENT}; selected honest update"),
        ("Coord Median",
         w_median,
         "Median ignores outlier"),
    ]

    for label, est, note in rows:
        err = est - true_global
        print(f"  {label:<19}| {est:>+.4f}       | {err:>+.4f} | {note}")

    print("  -------------------|----------------|--------|---------------------------")
    print()


if __name__ == '__main__':
    run_demo()
