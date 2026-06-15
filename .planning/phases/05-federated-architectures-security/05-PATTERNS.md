# Phase 5: Federated Architectures & Security — Pattern Map

**Mapped:** 2026-06-14
**Files analyzed:** 5 (3 note files + 1 demo script + 1 demo README)
**Analogs found:** 5 / 5

---

## File Classification

| New File | Role | Data Flow | Closest Analog | Match Quality |
|----------|------|-----------|----------------|---------------|
| `notes/FED-01-federated-vs-distributed.md` | study-note (explain-why depth) | concept + LaTeX formulas | `notes/TVS-04-asset-health.md` (Phase 2) | exact — same For:/Purpose: header, numbered sections, say-aloud track, bridge callout, mixed LaTeX |
| `notes/FED-02-byzantine-robustness.md` | study-note (explain-why depth) | concept + LaTeX + comparison table | `notes/KAL-02-kalman-family-kf-ekf-ukf.md` (Phase 1) | exact — algorithm-depth note with decision table, pitfall callouts, quick-recall card |
| `notes/FED-03-edge-security.md` | study-note (awareness depth) | prose paragraphs + grid-threat pairings | `notes/TVS-04-asset-health.md` sections 4–6 (Phase 2) | role-match — awareness-only sections follow same pattern (mental model, DGA, RUL) |
| `demo/fedavg_fedprox_krum_demo.py` | teaching-demo (NumPy from-scratch) | numerical simulation → printed contrast table | `demo/dc_powerflow_baddata_demo.py` (Phase 2) | exact — same module-docstring header, physical-constants block, named helper functions, `run_demo()` entry point, `np.random.seed(42)`, printed banner with `=` dividers, `if __name__ == '__main__'` |
| `demo/README.md` | demo-readme | interview talking points + how-to-run | `demo/README.md` (Phase 1 EKF) and `demo/README.md` (Phase 2 DC power-flow) | exact — same section order: What It Demonstrates / Prerequisites / How to Run / Interview Talking Points / Key Implementation Details / Files |

---

## Pattern Assignments

### `notes/FED-01-federated-vs-distributed.md` (study-note, explain-why depth)

**Primary analog:** `.planning/phases/02-transmission-virtual-sensing/notes/TVS-04-asset-health.md`
**Secondary analog:** `.planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md`

**Header block pattern** (TVS-04-asset-health.md lines 1–8):
```markdown
# TVS-04: Asset-Health Estimation

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Cover transformer/asset-health virtual sensing — the IEEE C57.91 hot-spot thermal
ODE (deep), Arrhenius loss-of-life, and DGA / Dynamic Line Rating / RUL (awareness) — so you can
explain how an unmeasured internal condition is *inferred* from telemetry and turned into a
maintenance decision, and tie each to work you have already built.

---

> **Depth strategy:** FULL/worked depth for the **IEEE C57.91 hot-spot ODE** and the **Arrhenius
> aging law** (criteria-named). **Awareness only** — crisp, no derivation — for **DGA**...
```

Apply to FED-01: replace title/purpose text; retain the `> **Depth strategy:**` blockquote immediately after the `---` separator naming which subsections are explain-why vs. awareness-only.

**Numbered section with "mental model first" opener pattern** (TVS-04-asset-health.md lines 17–27):
```markdown
## 1. IEEE C57.91 Transformer Thermal Model — The Physics (Deep)

**Mental model first.** You almost never measure the winding **hot-spot** temperature directly —
it is buried inside the windings under oil. But hot-spot temperature is what ages the insulation,
so it is the quantity that matters.
```

Apply to FED-01: each numbered section opens with a **Mental model first.** or **The one-liner:** sentence before diving into formulas.

**LaTeX formula with term-by-term table pattern** (TVS-04-asset-health.md lines 28–50):
```markdown
$$\tau_{TO}\,\frac{d\,\Delta\theta_{TO}}{dt} = \Delta\theta_{TO,\,U}\left(\frac{K^2 R + 1}{R+1}\right)^{n} - \Delta\theta_{TO}$$

### Term-by-term (à la KAL-03)

| Term | Name | Expression / role | Physical meaning |
|------|------|-------------------|------------------|
| $\theta_{HS}$ | Hot-spot temperature | ... | The **hidden state** — ... |
```

Apply to FED-01: use the same inline `$$...$$` display-math blocks for the FedAvg update rule $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$ and the FedProx proximal term $+\frac{\mu}{2}\lVert w - w_t\rVert^2$, each followed by a term-by-term table.

**"<3-min say-aloud version" section pattern** (TVS-04-asset-health.md lines 152–167):
```markdown
## <3-min say-aloud version

> "Asset health is virtual sensing on infrastructure. Take a transformer: the thing that ages it is
> the **winding hot-spot temperature**, which you can't measure — it's buried under oil. So
> **IEEE C57.91** gives you two cascaded first-order ODEs ... All of it is: infer the quantity
> that matters from the telemetry you have, then act on it."
```

Apply to FED-01: place `## <3-min say-aloud version` at the bottom (before the Bridge callout), using a single block-quoted paragraph that hits the criterion's named points in spoken order.

**"Bridge to your work" callout pattern** (TVS-04-asset-health.md lines 170–194):
```markdown
## → Bridge to your work

> **"Transformer hot-spot and DLR are the same virtual-sensing pattern as my OSED building thermal
> estimator — you can't measure the quantity that matters directly, so you infer it from a physics
> model plus available telemetry and act on the estimate."**

| Grid asset-health virtual sensing | My OSED / Building Intelligence work (CV) |
|-----------------------------------|--------------------------------------------|
| Hidden state: winding hot-spot / conductor temp | Hidden state: zone thermal state |
```

Apply to FED-01: use `## → Bridge to your work` as the final H2 section. Open with a bold block-quoted one-liner pivot sentence (the "honest delta" framing from D-07). Optionally follow with a two-column comparison table mapping the grid federated-learning concept to Juan's closest CV analog.

**Quick-Recall Card pattern** (TVS-04-asset-health.md lines 199–208, also KAL-02 lines 330–354):
```markdown
## Quick-Recall Card (Recite Before the Interview)

1. **C57.91 thermal model:** two cascaded first-order rises — ...
2. **Drivers:** ...
```

Apply to FED-01: numbered bullet list of the 4–6 most compressed facts, labelled **bold**, recitable in under 60 seconds.

**Sources footer pattern** (TVS-04-asset-health.md line 211):
```markdown
*Sources: IEEE Std C57.91-2011 ...; CV (OSED building thermal estimator ...)*
```

Apply to all FED notes: single italic line at the very bottom listing primary citations.

---

### `notes/FED-02-byzantine-robustness.md` (study-note, explain-why + algorithm depth)

**Primary analog:** `.planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md`

**Algorithm-depth section with "When X fails" probe pattern** (KAL-02 lines 110–129):
```markdown
### When EKF Fails

This is a common interview probe — know these failure modes:

1. **Highly nonlinear model:** If $f$ or $h$ has strong curvature, ...
2. **Ill-conditioned Jacobian near voltage collapse:** ...
3. **Positive-feedback divergence:** As $P$ grows ...

**Interview sentence:** "EKF linearizes via Jacobian. When the system is strongly nonlinear,
the Jacobian is a poor local approximation, and the error compounds step-by-step until the
filter diverges. That is when you reach for the UKF."
```

Apply to FED-02: after explaining each technique (Krum, coordinate-wise median), add a `### When X Fails` or `### Limitation` subsection naming the known failure mode and the interview-defensible sentence. Mirror the `**Interview sentence:**` convention exactly.

**Decision table pattern** (KAL-02 lines 200–210):
```markdown
## 4. EKF vs UKF Decision Table

<!-- greppable tag: EKF UKF decision -->

| Property | EKF | UKF |
|----------|-----|-----|
| Approach | Jacobian linearization (1st-order Taylor) | Sigma-point propagation (3rd-order accurate) |
| Accuracy | Good for mildly nonlinear | Better for moderately-to-highly nonlinear |
```

Apply to FED-02: use the same two-column (or three-column) markdown table for the gossip-vs-central aggregation tradeoff section. The table is the primary vehicle; prose before/after it gives the framing.

**Quick-Recall Card with bold labels pattern** (KAL-02 lines 330–354):
```markdown
## Quick-Recall Card (Recite Before the Interview)

**Linear KF:**
- Predict: $\hat{x}_{k|k-1} = F\hat{x} + Bu$; $P_{k|k-1} = FPF^\top + Q$
- Update: ...

**EKF:**
- Same as KF but replace $F$ with $A = \partial f/\partial x$ ...
```

Apply to FED-02: group by concept (FedAvg, Krum, Coord Median, Gossip-vs-Central), each with a **Bold label:** line. Use inline `$...$` for formulas inside the card.

---

### `notes/FED-03-edge-security.md` (study-note, awareness depth)

**Primary analog:** `.planning/phases/02-transmission-virtual-sensing/notes/TVS-04-asset-health.md` — sections 4, 5, 6 (DGA, DLR, RUL at awareness depth)

**Awareness section pattern** (TVS-04-asset-health.md lines 108–126):
```markdown
## 4. DGA — Dissolved Gas Analysis (Awareness)

Under thermal/electrical stress, transformer oil decomposes and releases **key gases**; ...
**No derivation — recognize the associations:**

| Gas | Association |
|-----|-------------|
| H₂ | Partial discharge |
...

**One line:** *"DGA is a virtual sensor for internal fault type — you infer what's failing inside a
sealed tank from the gas signature in the oil."*
```

Apply to FED-03: each security concept (OTA, TPM, SPIFFE/SPIRE) gets one H2 section labeled `(Awareness)`. Follows the same pattern: **What it is** (one crisp paragraph), **The concrete grid threat it counters** (one paragraph), **One line / Interview sentence** (italicized summary), and optionally **Bridge** (Juan's closest analog + the upgrade). No sub-sub-sections, no config detail.

The three-section structure for FED-03 should follow this shape exactly:

```markdown
## 2. OTA Update Integrity (Awareness)

**What it is:** ...signed artifact...HSM...signature verification before install.

**The concrete grid threat it counters:** ...malicious firmware push to K3s substation fleet...

**Interview sentence:** *"OTA signing means an attacker must compromise the signing key, not
just the update channel — the edge node rejects any image that doesn't pass signature
verification before execution."*

**→ Bridge to your work:** Juan has shipped OTA updates. The upgrade is to add a signing step
and a signature-check at the node — same mechanism, grid-safety guarantee.
```

---

### `demo/fedavg_fedprox_krum_demo.py` (teaching-demo, NumPy from-scratch)

**Primary analog:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py`
**Secondary analog:** `.planning/phases/01-kalman-state-estimation/demo/ekf_line_temp_demo.py`

**Module docstring header pattern** (dc_powerflow_baddata_demo.py lines 1–24):
```python
"""
dc_powerflow_baddata_demo.py
----------------------------
From-scratch 3-bus DC power-flow weighted-least-squares (WLS) state estimator
that infers bus voltage angles from a redundant measurement set, then detects
and removes a single corrupted measurement via the chi-squared test ...

This is the TVS-02 + TVS-03 hands-on demo for interview preparation ...

Dependencies: numpy, scipy, matplotlib  (from-scratch; no SE / power-flow library needed)
Run:          python3 dc_powerflow_baddata_demo.py
Output:       dc_powerflow_baddata.png (saved beside this script)
              Console: chi-squared / flagged-measurement / re-solved-angles readout

3-bus network constants used throughout:
  ...
"""
```

Apply to FED-05 demo: use an identical docstring block with:
- filename + dashed underline
- one-sentence description of all three techniques
- `This is the FED-01 + FED-02a hands-on demo for interview preparation.`
- `Dependencies: numpy  (from-scratch; no Flower/PySyft dependency)`
- `Run: python3 fedavg_fedprox_krum_demo.py`
- `Output: Console: before/after contrast table`
- Dataset constants listed (n_clients=6, means, sigma, n_samples)

**Physical/scenario constants block pattern** (dc_powerflow_baddata_demo.py lines 37–43, ekf_line_temp_demo.py lines 39–47):
```python
# ---------------------------------------------------------------------------
# Drake ACSR physical constants
# ---------------------------------------------------------------------------
MCP = 534.0        # J/(m·°C)  heat capacity per unit length
R25 = 7.28e-5      # Ω/m       DC resistance at 25°C
```

Apply to FED-05 demo: use the same `# ---\n# [Name] constants\n# ---` block for the non-IID client scenario constants (TRUE_MEANS, N_SAMPLES, SIGMA, MU_FEDPROX, POISON_MAGNITUDE, POISON_CLIENT, N_ROUNDS, LOCAL_EPOCHS). All on module-level, upper-case names, inline comments.

**Named helper functions + horizontal separator pattern** (dc_powerflow_baddata_demo.py lines 46–99):
```python
# ---------------------------------------------------------------------------
# 3-bus DC power-flow constants
# ---------------------------------------------------------------------------

def build_B_matrix():
    """Reduced bus susceptance matrix ..."""
    ...

def wls_solve(H, W, z):
    """One-shot linear WLS ..."""
    ...
```

Apply to FED-05 demo: decompose into clearly named helpers with one-line docstrings, each preceded by the `# ---\n# Section title\n# ---` separator:
- `generate_clients(n_clients, true_means, n_samples, sigma, seed)` — returns list of (data, n_k) tuples
- `local_sgd(w, data, lr, epochs)` — gradient steps on 1-D mean estimation
- `fedprox_local_step(w_local, w_global, data, lr, epochs, mu)` — same but with proximal term
- `fedavg_aggregate(local_models, n_samples)` — weighted average
- `krum_select(updates, f)` — Krum score + argmin
- `coord_median(updates)` — np.median one-liner
- `inject_poison(updates, client_idx, magnitude)` — replaces one update

**`run_demo()` function with `np.random.seed(42)` + printed banner pattern** (dc_powerflow_baddata_demo.py lines 102–168):
```python
def run_demo():
    """Solve the 3-bus DC WLS, inject + detect + remove a gross error, plot and save PNG."""
    np.random.seed(42)
    ...
    print("=" * 62)
    print("  3-Bus DC State Estimation — Bad-Data Detection (chi2 + rN)")
    print("=" * 62)
    ...
    print(f"  --- Solve #1 (with bad data) ---")
    print(f"  chi2 threshold (95%, df={df1}) : {thr1:.3f}")
```

Apply to FED-05 demo: single `run_demo()` function containing all execution logic. Opens with `np.random.seed(42)`. Printed banner uses `"=" * 54` (or similar width). Banner structure:
```
======================================================
  FedAvg / FedProx / Byzantine Robustness Demo
======================================================

  Clients: 6   Local epochs: 10   Rounds: 20   Poison: client 0 (shift -5.0)
  True global optimum: ~1.22

  Method             | Final Estimate | Error  | Notes
  -------------------|---------------|--------|---------------------------
  Plain FedAvg       |  ...          | ...    | Poisoned — client 0 pulled it off
  FedProx (mu=0.5)   |  ...          | ...    | Proximal term kept local models near global
  Krum (f=1)         |  ...          | ...    | Rejected client 0; selected honest update
  Coord Median       |  ...          | ...    | Median ignores outlier
  -------------------|---------------|--------|---------------------------
```

**`if __name__ == '__main__'` guard pattern** (both Phase 1/2 demos, final line):
```python
if __name__ == '__main__':
    run_demo()
```

Apply to FED-05 demo: always the final two lines.

**No matplotlib in FED-05 demo** (decision from 05-RESEARCH.md environment section): unlike Phase 1/2 demos which save a PNG, the FED-05 demo prints the contrast table to stdout only. No `import matplotlib`, no `plt.savefig`. The README should note this explicitly: "output is the console table — no plot file generated."

---

### `demo/README.md` (demo-readme)

**Primary analog:** `.planning/phases/01-kalman-state-estimation/demo/README.md`
**Secondary analog:** `.planning/phases/02-transmission-virtual-sensing/demo/README.md`

**README section order pattern** (Phase 1 README.md lines 1–139):
```markdown
# KAL-04: IEEE 738 EKF Line-Temperature Demo

A self-contained Extended Kalman Filter (EKF) that estimates overhead conductor
temperature from simulated current telemetry ...

---

## What It Demonstrates

The script builds a **from-scratch EKF** (numpy/scipy only — no external KF library) that:

1. Simulates ...
2. Generates ...
3. Runs ...

---

## Prerequisites

Only standard scientific Python packages required — all already installed:

```
numpy   (1.26.4+)
```

No external Kalman filter library is needed. The EKF is implemented from scratch ...

---

## How to Run

```bash
cd .planning/phases/01-kalman-state-estimation/demo
python3 ekf_line_temp_demo.py
```

**Expected console output:**
```
==============================================================
...
```

---

## Interview Talking Points

**Talking point 1 — ...**

> "I implemented this EKF from scratch in numpy rather than calling a library. ..."

**Talking point 2 — ...**

---

## Key Implementation Details

| Component | Implementation choice | Reason |
|-----------|----------------------|--------|
| ... | ... | ... |

---

## Files

```
demo/
├── fedavg_fedprox_krum_demo.py   — ...
└── README.md                      — this file
```
```

Apply to FED-05 demo README:
- H1 title: `# FED-01/02a: FedAvg / FedProx / Byzantine Robustness Demo`
- Lead paragraph names all three techniques + "from scratch in NumPy"
- `## What It Demonstrates` — numbered list of the four narrative steps (non-IID clients, FedAvg rounds, FedProx contrast, poison injection + Krum/median rejection)
- `## Prerequisites` — numpy only (no scipy, no matplotlib — simpler than Phase 1/2)
- `## How to Run` — cd path + python3 command + **Expected console output** block showing the full before/after table
- `## Interview Talking Points` — 3 talking points matching the demo's three narrative acts (FedAvg/FedProx contrast, Krum rejection, median vs. Krum tradeoff)
- `## Key Implementation Details` — table with Component / Implementation choice / Reason rows for each helper function
- `## Files` — code block listing demo/ directory contents

**Talking-point voice pattern** (Phase 1 README.md lines 85–104):
```markdown
**Talking point 1 — "From scratch" signals depth, not just library knowledge:**

> "I implemented this EKF from scratch in numpy rather than calling a library.  That forced
> me to derive the process Jacobian `A = df/dTc` analytically for the IEEE 738 ODE ..."
```

Apply to FED-05 README: each talking point has a bold descriptive label followed by a block-quoted first-person statement. Talking point 3 should include the honest bridge pivot (D-07 language): "In OSED I ran distributed edge inference across DER nodes — no cloud round-trip. I haven't run federated learning in production, but that's the natural next step..."

---

## Shared Patterns

### For: / Purpose: Header
**Source:** All Phase 1–4 notes (canonical in `KAL-02-kalman-family-kf-ekf-ukf.md` lines 1–8, `TVS-04-asset-health.md` lines 1–8, `STK-03-messaging-orchestration.md` lines 1–8)
**Apply to:** FED-01, FED-02, FED-03

```markdown
**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** [One sentence stating exactly what the note covers and what the reader will be able to do.]

---

> **Depth strategy:** [Which subsections are explain-why depth and which are awareness-only.]
```

The `---` + `> **Depth strategy:**` blockquote is mandatory in this project's note convention. It appears in both TVS-04 and STK-05, confirming it as a Phase 4-era addition to the pattern.

### Say-Aloud Track
**Source:** `TVS-04-asset-health.md` lines 152–167
**Apply to:** FED-01, FED-02, FED-03

Section heading is exactly `## <3-min say-aloud version` (no period). Content is a single block-quoted paragraph in first-person spoken voice. Positioned near the bottom of the note — after all technical sections and before the Bridge callout. The track must hit every criterion-named point for the note's requirement.

### Bridge Callout
**Source:** `TVS-04-asset-health.md` lines 170–194; `STK-03-messaging-orchestration.md` (Phase 4 pattern)
**Apply to:** FED-01, FED-02, FED-03

Section heading is exactly `## → Bridge to your work`. Opens with a bold block-quoted one-liner. Followed by either a two-column table or a prose paragraph with the "honest delta" framing. For FED notes, the bridge callouts must use the exact D-07 framing (OSED edge inference → FedAvg upgrade; MQTT fleet → SPIFFE upgrade; OTA shipped → add signing + TPM).

### Quick-Recall Card
**Source:** `TVS-04-asset-health.md` lines 199–208; `KAL-02-kalman-family-kf-ekf-ukf.md` lines 330–354
**Apply to:** FED-01, FED-02, FED-03

Section heading is exactly `## Quick-Recall Card (Recite Before the Interview)`. Numbered or bold-labelled compressed facts. Inline LaTeX for formulas. Target: recitable in under 60 seconds. This section must appear in every note, positioned after the Bridge callout and before the Sources footer.

### Sources Footer
**Source:** `TVS-04-asset-health.md` line 211; `KAL-02-kalman-family-kf-ekf-ukf.md` line 358
**Apply to:** FED-01, FED-02, FED-03

```markdown
*Sources: [citation list, comma-separated, italicized, single line]*
```

### `np.random.seed(42)` + `run_demo()` + `if __name__ == '__main__'`
**Source:** `dc_powerflow_baddata_demo.py` lines 102, 210–213; `ekf_line_temp_demo.py` lines 208, 330–331
**Apply to:** `demo/fedavg_fedprox_krum_demo.py`

All three are non-negotiable in every Phase demo: seed for reproducibility, `run_demo()` function containing all simulation/print logic, guard at the final two lines.

### `# ---\n# [Name]\n# ---` Section Separators in Demo Scripts
**Source:** `dc_powerflow_baddata_demo.py` lines 36, 45, 76, 101; `ekf_line_temp_demo.py` lines 38, 51, 95, 118, 167, 185, 207
**Apply to:** `demo/fedavg_fedprox_krum_demo.py`

```python
# ---------------------------------------------------------------------------
# [Section name]
# ---------------------------------------------------------------------------
```

Used to visually delimit: scenario constants, each helper function group, and the main demo function.

---

## No Analog Found

All five Phase 5 files have close analogs. No files require falling back to RESEARCH.md patterns only.

| File | Analog Quality | Note |
|------|---------------|------|
| `notes/FED-01-federated-vs-distributed.md` | exact | TVS-04 is the direct style template |
| `notes/FED-02-byzantine-robustness.md` | exact | KAL-02 algorithm-depth + decision-table pattern is exact |
| `notes/FED-03-edge-security.md` | role-match | TVS-04 awareness sections (DGA, DLR, RUL) are the structural template |
| `demo/fedavg_fedprox_krum_demo.py` | exact | dc_powerflow_baddata_demo.py is the direct structural template; key difference is no matplotlib (stdout table only) |
| `demo/README.md` | exact | Phase 1 EKF README is the canonical structure; Phase 2 confirms the pattern |

---

## Metadata

**Analog search scope:** `.planning/phases/01-kalman-state-estimation/`, `.planning/phases/02-transmission-virtual-sensing/`, `.planning/phases/04-protocols-stack-architecture/`
**Files scanned:** 9 (2 demo .py, 2 demo README.md, 5 note .md files across phases 1/2/4)
**Pattern extraction date:** 2026-06-14
