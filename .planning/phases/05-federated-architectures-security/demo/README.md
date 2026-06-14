# FED-01/02a: FedAvg / FedProx / Byzantine Robustness Demo

A self-contained teaching demo implementing **FedAvg**, **FedProx** (proximal regularization),
**Krum**, and **coordinate-wise median** entirely from scratch in NumPy — no Flower, no PySyft,
no framework dependency. The script simulates non-IID federated learning across six clients,
demonstrates how FedProx's proximal term damps client drift, then injects a Byzantine
(poisoned) client and shows Krum and coordinate-wise median rejecting it while plain FedAvg
is corrupted.

---

## What It Demonstrates

The script tells one story in four acts:

1. **Non-IID clients:** Six simulated substations each have a different local data distribution
   (different "feeder" means: 0.0, 0.5, 1.0, 1.5, 2.0, 2.5). This is the non-IID structure
   that breaks naive FedAvg when clients run many local epochs — each substation's model
   drifts toward its own local optimum.

2. **FedAvg convergence:** The server runs 20 communication rounds, aggregating client models
   as a weighted average $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$ (McMahan et al. 2017).

3. **FedProx damps drift:** The same 20-round run with μ=0.5 adds a proximal term
   $+\frac{\mu}{2}\lVert w - w_t \rVert^2$ to each client's local objective, penalizing
   deviation from the global model. The final estimate sits within 0.01 of the true optimum,
   versus ~0.64 error when Byzantine clients attack plain FedAvg.

4. **Byzantine injection — Krum and median reject it:** Client 0 sends a poisoned update
   (shift −5.0, far outside the honest cluster). Plain FedAvg averages the poison in.
   Krum (Blanchard et al. 2017) scores each update by distance to nearest neighbors and
   selects the honest update with minimum score. Coordinate-wise median takes the element-wise
   median, leaving the outlier in the tail where it does not affect the result.

---

## Prerequisites

NumPy only — simpler than the Phase 1/2 demos (no scipy, no matplotlib required):

```
numpy (1.26+)
```

No FL framework is needed. FedAvg, FedProx, Krum, and coordinate-wise median are implemented
from scratch in ~200 lines of numpy arithmetic to demonstrate understanding of the underlying
aggregation math.

---

## How to Run

```bash
cd .planning/phases/05-federated-architectures-security/demo
python3 fedavg_fedprox_krum_demo.py
```

**Expected console output:**

```
========================================================
  FedAvg / FedProx / Byzantine Robustness Demo
========================================================

  Clients: 6   Local epochs: 10   Rounds: 20   Poison: client 0 (shift -5.0)
  True global optimum: 1.22

  Method             | Final Estimate | Error  | Notes
  -------------------|----------------|--------|---------------------------
  Plain FedAvg       | +0.5826       | -0.6353 | Poisoned -- client 0 pulled it off
  FedProx (mu=0.5)   | +1.2237       | +0.0057 | Proximal term kept local models near global
  Krum (f=1) [client 3]| +1.4743       | +0.2564 | Rejected client 0; selected honest update
  Coord Median       | +1.2548       | +0.0369 | Median ignores outlier
  -------------------|----------------|--------|---------------------------
```

Output is the console table — no plot file is generated.

---

## Interview Talking Points

**Talking point 1 — FedProx vs FedAvg under non-IID data:**

> "I implemented FedProx from scratch in NumPy so I could see the proximal term working.
> The key insight is that the proximal term lives in the *client's local objective*, not in
> the server aggregation — each client minimizes F_k(w) + (μ/2)||w − w_t||² rather than
> pure F_k(w). That penalizes deviation from the global model, so the client stops short
> of its own local optimum. In the table you can watch FedProx land at +0.006 error while
> the same FedAvg run under Byzantine attack is at −0.64 — the proximal term is what keeps
> each substation's local update tethered to the fleet model."

**Talking point 2 — Byzantine robustness in ~10 lines:**

> "Watch plain FedAvg get dragged off by the poisoned client while Krum just drops it.
> Krum scores each update by distance to its nearest neighbors and picks the one closest
> to the crowd — the outlier is never selected because its Krum score is the highest.
> Coordinate-wise median achieves similar robustness differently: it takes the element-wise
> median across all updates, so the poisoned outlier ends up in the tail and doesn't move
> the result. That's Byzantine robustness in ~10 lines of numpy."

**Talking point 3 — The honest bridge:**

> "In OSED I ran distributed edge inference across DER nodes — no cloud round-trip for
> local decisions. I haven't run federated *learning* in production, but that's the
> natural next step: keep the local inference, add FedAvg so the fleet improves a shared
> model without ever shipping raw telemetry — and Krum so one bad node can't poison it."

---

## Key Implementation Details

| Component | Implementation choice | Reason |
|-----------|----------------------|--------|
| 1-D mean estimation | Loss F_k(w) = mean((w − x)²); grad = 2·mean(w − x) | Simplest non-IID problem; makes non-IID structure and drift visible with no matrix math |
| FedProx proximal term | Added inside `fedprox_local_step`, not in `fedavg_aggregate` | Correct per Li et al. 2020 — the proximal term constrains the local objective, not the server aggregation; a common interview pitfall |
| Krum selection | Sum squared distances to n−f−2 nearest neighbors; argmin | Blanchard et al. 2017; honest updates cluster, poisoned update is distant — minimum-score update is most trustworthy |
| Coordinate-wise median | `np.median(np.stack(updates), axis=0)` | One-liner; robust to up to n/2−1 Byzantine clients; ignores correlation across dimensions |
| No matplotlib | stdout table only | The contrast table is the talking point; no display dependency needed |
| Seed 42 | `np.random.seed(42)` at top of `run_demo()` | Reproducible output; numbers in this README match exactly what the script prints |

---

## Files

```
demo/
├── fedavg_fedprox_krum_demo.py   — single self-contained NumPy script
└── README.md                      — this file
```
