# Phase 2: Distribution Virtual Sensing - Research

**Researched:** 2026-06-13
**Domain:** Power-system T&D virtual sensing — voltage stability, DC power-flow angle estimation, observability/bad-data theory, transformer/asset thermal models — packaged as interview study notes + one NumPy demo
**Confidence:** HIGH (core equations are textbook-standard, cross-verified against Abur & Expósito and IEEE standards literature)

## Summary

This is a **study-notes phase**, not a software build. The "implementation" the planner must task is: four equation-dense markdown notes (TVS-01..04) in the established Phase-1 style, plus ONE ~80-line NumPy demo (3-bus DC power-flow WLS + chi-squared/largest-normalized-residual bad-data detection). The research goal was to surface the *correct canonical equations, standard formulations, worked numbers, vocabulary, and authoritative references* the note-writer needs so the notes are technically accurate and interview-defensible.

All four topics are mature, textbook-grade material. The dominant reference for TVS-02/03 is **Abur & Expósito, "Power System State Estimation: Theory and Implementation" (2004)** — the residual-sensitivity / normalized-residual machinery, chi-squared test, and observability-via-Jacobian-rank all come straight from it and connect cleanly to Phase 1's KAL-01 (which already covers the WLS objective, Gauss-Newton, chi-squared, LNR, and the leverage-measurement trap). TVS-02/03 are a *linear specialization* of KAL-01: DC power flow makes $h(x)=Hx$ linear, so WLS becomes a one-shot solve $\hat\theta=(H^TWH)^{-1}H^TWz$ — no Gauss-Newton iteration. The note-writer must NOT re-derive WLS from scratch; it should reference KAL-01 and show the linear collapse.

For TVS-01, the canonical PMU-local voltage-stability index is the **Thevenin impedance-matching / VIP** idea (Vu, Begovic, Novosel, et al.): from local PMU V/I, estimate the Thevenin equivalent seen by the load; collapse occurs when $|Z_{load}|=|Z_{Thev}|$ (max power transfer), and the index $\mathrm{VSI}=|Z_{Thev}|/|Z_{load}|$ runs 0 (no load) → 1 (collapse). For TVS-04, the deep item is the **IEEE C57.91** top-oil + hot-spot rise ODEs (with time constants and the loading exponents $m,n$); DGA gases, Duval triangle, DLR productization, and RUL stay at awareness level per the locked depth strategy.

**Primary recommendation:** Write the four notes mirroring KAL-01/KAL-02 exactly (oral-rehearsal header, numbered sections, LaTeX-in-markdown, Quick-Recall card, per-note "→ Bridge to your work" box, per-note "<3-min say-aloud"). Treat TVS-02/03 as the linear sequel to KAL-01 (cross-reference, don't repeat). Build the demo by adapting `ekf_line_temp_demo.py`'s scaffolding (NumPy-only, `matplotlib.use('Agg')`, save PNG beside script, console readout block, README pairing). Use the concrete 3-bus numbers supplied in §Demo below so the planner can hand the executor a fully specified build.

## Architectural Responsibility Map

This phase produces documents, not a running multi-tier system. The "tiers" are the deliverable artifacts; mapping clarifies which artifact owns which requirement so the planner assigns tasks cleanly.

| Capability | Primary Tier (artifact) | Secondary Tier | Rationale |
|------------|------------------------|----------------|-----------|
| Voltage-stability theory (P-V, Thevenin VSI, margin) | `notes/TVS-01-*.md` | — | Notes-only; not in demo (D-03) |
| DC power-flow angle inference (P=Bθ, WLS) | `notes/TVS-02-*.md` | `demo/` (computational backing) | Demo concretizes the WLS solve |
| Observability + bad-data (χ², rN, leverage, rank) | `notes/TVS-03-*.md` | `demo/` (computational backing) | Demo concretizes χ²/rN detection |
| Asset health (C57.91 ODE, DGA, DLR, RUL) | `notes/TVS-04-*.md` | — | Notes-only; DLR references Phase 1 demo |
| Reusable WLS/plot/IO scaffolding | `demo/` (adapted from Phase 1) | `notes/TVS-02/03` | One demo backs both TVS-02 & TVS-03 |
| OSED/HEMS/SI-MAPPER bridge pivots | each note's bridge box | Phase 6 (aggregate table) | Per-note now; aggregation deferred (D-05) |

## User Constraints (from CONTEXT.md)

> The planner MUST honor these verbatim.

### Locked Decisions
- **D-01:** ONE small Python demo (~80 lines) — 3-bus DC power-flow WLS angle estimation + chi-squared bad-data detection (inject one corrupted measurement, flag via normalized residual, re-solve). Notes lead; demo is reinforcement / "I built this" whiteboard story.
- **D-02:** Demo reuses Phase 1's WLS/Gauss-Newton machinery; self-contained with short README, mirroring Phase 1's `demo/` layout.
- **D-03:** Demo scope = TVS-02 (P=Bθ angle WLS) + TVS-03 (χ²/normalized-residual bad-data). TVS-01 (Thevenin VSI) and TVS-04 (asset health) are notes-only unless trivially cheap to add.
- **D-04:** EVERY note ends with a boxed "→ Bridge to your work" callout (1–2 sentences) mapping the T&D concept to a concrete OSED/HEMS/SI-MAPPER analog, phrased as a ready interview pivot.
- **D-05:** Do NOT build an aggregate bridge table here — full vocabulary-bridge table (BRG-01..03) is owned by Phase 6. Per-note callouts feed it without duplicating.
- **D-06:** Each note carries a tight "<3-min say-aloud version" talk-track hitting the criterion's named points.
- **D-07:** Full mock rehearsal / Q&A bank / timing drills stay in Phase 6. Phase 2 provides the script, not the rehearsal loop.
- **D-08:** Deep where named, aware elsewhere. FULL derivations + worked numbers ONLY for: P-V/Thevenin VSI + operating margin (TVS-01); P=Bθ WLS angle inference (TVS-02); χ² + normalized residuals + Jacobian-rank observability (TVS-03); IEEE C57.91 hot-spot ODE (TVS-04). AWARENESS-level (crisp, no derivation) for: DGA gases, leverage-measurement intuition, DLR productization, RUL framing.
- **D-09:** One file per requirement in `notes/`: `TVS-01-…md` … `TVS-04-…md`. TVS-04 stays a single well-sectioned file unless it grows unwieldy.
- **D-10:** Equation-dense markdown, LaTeX-in-markdown ($…$ inline, $$…$$ display). Each note opens with Phase-1 "oral rehearsal" header (**For:** / **Purpose:**), numbered sections, speak-aloud recall.

### Claude's Discretion
- Exact section ordering within each note; bus topology/numbers chosen for the demo; whether the "<3-min say-aloud" track sits at top or bottom of each note; whether to lightly extend the demo to touch TVS-01 if cheap.

### Deferred Ideas (OUT OF SCOPE)
- Aggregate vocabulary-bridge table (T&D term → OSED analog → pivot sentence) → **Phase 6** (BRG-01..03).
- Full Q&A / mock-interview drills and timing rehearsal → **Phase 6**.
- Deep PMU / IEC 61850 / C37.118 protocol treatment → **Phase 4** (use vocabulary-level only here).
- Extending the demo to a federated / multi-substation setting → **Phase 5**.

## Phase Requirements

| ID | Description | Research Support (which findings enable the note) |
|----|-------------|---------------------------------------------------|
| TVS-01 | Voltage stability — P-V curve, voltage collapse, Thevenin-equivalent VSI from PMU data, operating margin | §TVS-01 below: nose-curve mechanism, max-power-transfer / impedance-matching VSI, $\mathrm{VSI}=|Z_{Thev}|/|Z_{load}|$, loadability margin def. |
| TVS-02 | Phase-angle / power-flow inference — DC approx (P=Bθ), sparse PMU coverage, angle inference as WLS | §TVS-02: DC assumptions, B-matrix construction, slack reference, linear WLS collapse of KAL-01, 3-bus worked numbers |
| TVS-03 | Observability + bad-data — χ² test, normalized residual, leverage measurements | §TVS-03: χ²(m−n) on $J(\hat x)$, residual covariance $\Omega$, $r^N$ threshold ~3, leverage trap, H-rank observability |
| TVS-04 | Asset-health — transformer hot-spot (C57.91), DLR as product, RUL framing | §TVS-04: top-oil + hot-spot rise ODEs, Arrhenius aging, DGA awareness, DLR↔Phase 1, RUL awareness |

## Standard Stack

### Core (demo only — notes need no libraries)
| Library | Version (verified) | Purpose | Why Standard |
|---------|--------------------|---------|--------------|
| numpy | 1.26.4 (installed) | Matrix algebra: build B/H, solve $(H^TWH)^{-1}H^TWz$, residuals | Same as Phase 1 demo; from-scratch, no SE library needed |
| matplotlib | 3.6.3 (installed) | Output PNG (estimated vs true angles, residual bars, flagged measurement) | Phase 1 demo pattern; `matplotlib.use('Agg')` headless |
| scipy | 1.11.4 (installed) | `scipy.stats.chi2` for the χ² threshold (`chi2.ppf`) | Already used in Phase 1 `nis_check` — direct reuse |

`[VERIFIED: python3 import — numpy 1.26.4, scipy 1.11.4, matplotlib 3.6.3 all importable on this machine]`

**No installation needed** — all three already present (confirmed by import). Demo stays NumPy/SciPy/matplotlib only, exactly like `ekf_line_temp_demo.py`.

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| From-scratch NumPy WLS | `pandapower` / `PYPOWER` | Adds a heavy dependency and hides the WLS math the demo exists to *show*. Reject — the pedagogical point is the linear-algebra solve. |
| `scipy.stats.chi2.ppf` | Hard-coded χ² table value | scipy is already a dependency and `chi2.ppf` is clearer/auditable. Use scipy. |

## Architecture Patterns

### Note structure (mirror KAL-01 / KAL-02 exactly)
```
notes/TVS-0X-<slug>.md
├── # Title
├── **For:** oral rehearsal …   **Purpose:** …      (Phase-1 header — D-10)
├── ## 1..N numbered sections (mental-model-first, then equations)   (D-10)
├── ## "<3-min say-aloud version"  talk-track                        (D-06)
├── ## → Bridge to your work  (boxed OSED/HEMS/SI-MAPPER pivot)      (D-04)
├── ## Quick-Recall Card (numbered recite-before-interview list)     (KAL-01 pattern)
└── *Sources:* line                                                  (KAL-01 pattern)
```
**Pattern source:** `notes/KAL-01-wls-state-estimation.md` and `notes/KAL-02-kalman-family-kf-ekf-ukf.md` `[VERIFIED: read in session]`. The bridge box in KAL-01 uses a `> blockquote` + a comparison table + a "How to say this in the interview" quote — reuse that shape.

### Demo structure (mirror `ekf_line_temp_demo.py`)
```
demo/
├── dc_powerflow_baddata_demo.py   (~80 lines; module docstring, constants block,
│                                    build_B_matrix(), build_H(), wls_solve(),
│                                    chi2_test(), normalized_residuals(), run_demo())
├── README.md                       (What it demonstrates / Prereqs / Run / Output / Interview value)
└── dc_powerflow_baddata.png        (generated)
```
**Pattern source:** `demo/ekf_line_temp_demo.py` + `demo/README.md` `[VERIFIED: read in session]`. Reuse: top docstring with Run/Output lines; constants block; `np.random.seed(...)`; `matplotlib.use('Agg')`; `script_dir = os.path.dirname(os.path.abspath(__file__))` + `plt.savefig(out_path)`; a boxed console readout (`print("="*62)` banner) reporting χ² statistic vs threshold, the flagged measurement index, and the re-solved angles.

### System Architecture Diagram (demo data flow)
```
3-bus DC network (bus susceptances)
        │  build B-matrix (Bbus), pick slack = bus 1 (θ1 = 0)
        ▼
True angles θ_true  ──►  z_clean = H · θ_true        (line flows + injections)
        │                        │
        │        + Gaussian noise (R) + INJECT 1 gross error on measurement k*
        ▼                        ▼
   measurement set z (redundant: m > n)
        │
        ▼
   WLS solve #1:  θ̂ = (HᵀWH)⁻¹ HᵀW z          [reuses KAL-01 normal-equations form]
        │
        ▼
   residual r = z − Hθ̂   ──►  J(θ̂) = rᵀW r
        │                          │
        │              χ² test: J(θ̂) > χ²(m−n, 0.95)?  ── YES ──► bad data present
        ▼                          │
   normalized residual rᵢᴺ = |rᵢ| / √Ωᵢᵢ ,  Ω = R − H(HᵀWH)⁻¹Hᵀ
        │
        ▼  argmax rᵢᴺ  (expect = k*, value > 3)
   remove measurement k*  ──►  WLS solve #2  ──►  clean θ̂  ──►  plot + console readout
```
A reader can trace input (susceptances + measurements) → WLS → χ² flag → rN identification → re-solve → output by following the arrows. File→function mapping is in the demo structure block above, not here.

### Anti-Patterns to Avoid
- **Re-deriving WLS from zero in TVS-02/03.** KAL-01 already owns the WLS objective, Gauss-Newton, χ², LNR, and the leverage trap. TVS notes must *reference* KAL-01 and show the DC *linear specialization* (one-shot solve, no iteration). Repeating it wastes the runway and reads as padding. `[CITED: KAL-01 note, session]`
- **Using AC power flow in the demo.** DC approximation is the whole point — keep $h(\theta)=H\theta$ linear so it's one matrix solve and the bad-data math is transparent.
- **Over-deriving DGA/DLR/RUL.** D-08 caps these at awareness. A derivation here violates the locked depth strategy.
- **Building the aggregate bridge table.** D-05: that's Phase 6. Per-note boxes only.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| χ² critical value | Hard-coded lookup table | `scipy.stats.chi2.ppf(0.95, df=m-n)` | Already a dependency; auditable; matches KAL-01's `nis_check` |
| WLS normal-equations solve | Custom Gaussian elimination | `numpy.linalg.solve(H.T@W@H, H.T@W@z)` | Numerically standard; `solve` > explicit inverse |
| Matrix inverse for $\Omega$ | Manual inversion | `numpy.linalg.inv` / `solve` on the gain matrix | Small 2×2/3×3; NumPy is correct and clear |
| Jacobian-rank observability check | Custom rank logic | `numpy.linalg.matrix_rank(H)` | Standard numerical-rank test; one line in the note's worked example |

**Key insight:** This phase's "don't hand-roll" list is small and demo-scoped because the *notes* deliberately show the math by hand (that's their pedagogical purpose). The only place to lean on libraries is the demo's numerics, exactly as Phase 1 did.

---

## TVS-01 — Voltage Stability (deep: P-V, Thevenin VSI, margin)

**Depth: FULL (criteria-named).** `[CITED: Vu/Begovic/Novosel VIP method; cross-verified WebSearch on Thevenin impedance-matching VSI]`

### P-V (nose) curve and collapse mechanism
- For a load bus fed through impedance, plot bus voltage $V$ vs. load power $P$. As $P$ rises, $V$ sags; the curve bends back at the **nose** (maximum loadability point). Beyond the nose there is **no steady-state solution** — voltage collapse. `[ASSUMED — textbook-standard, confirm phrasing]`
- The nose = the point where the **power-flow Jacobian becomes singular** (loadability limit). `[VERIFIED: WebSearch — "VSIT becomes 1 when the power flow jacobian becomes singular"]`

### Thevenin-equivalent VSI from local PMU data (the must-know)
- Reduce the network seen by a load bus to a **Thevenin equivalent**: source $E_{Thev}$ behind impedance $Z_{Thev}$. From a stream of local PMU phasor measurements ($\tilde V$, $\tilde I$ at the bus), estimate $E_{Thev}$ and $Z_{Thev}$ (e.g., least-squares over a short window of consecutive PMU snapshots).
- **Maximum power transfer** to the load occurs when the load impedance magnitude equals the Thevenin impedance magnitude:
$$|Z_{load}| = |Z_{Thev}| \quad\Longrightarrow\quad \text{at the nose / collapse point}$$
- Define the index (impedance-matching form):
$$\mathrm{VSI} = \frac{|Z_{Thev}|}{|Z_{load}|}, \qquad \mathrm{VSI}\in[0,1]:\ 0=\text{no load},\ 1=\text{collapse}$$
`[VERIFIED: WebSearch — "VSIT is 0 at no load … 1 at maximum loading"; impedance-match collapse criterion]`
- **Operating / loadability margin:** the distance from the current operating point to the nose, expressed as additional MW the bus can absorb before collapse (or equivalently $1-\mathrm{VSI}$). Operators use the margin as a real-time early-warning headroom number.

### Canonical aloud explanation (for the talk-track)
> "Each load bus sees the rest of the grid as a Thevenin source behind an impedance. From local PMU voltage and current phasors you can estimate that Thevenin impedance in real time. Maximum power transfer — the nose of the P-V curve — happens exactly when the load impedance magnitude drops to equal the Thevenin impedance. So the ratio $|Z_{Thev}|/|Z_{load}|$ is a voltage-stability index that runs from zero at light load to one at collapse, and the gap to one is your operating margin."

### Known limitation to mention (awareness)
- Pure impedance-match indices struggle on **multi-load** systems (the single-port Thevenin reduction is approximate when multiple loads vary together). `[VERIFIED: WebSearch — "impedance match … problems … in multi-load power systems"]`

### OSED bridge (TVS-01)
Strongest analog: **margin-to-constraint monitoring** in OSED/HEMS. Juan's HEMS PoC "manages total household consumption to respect power grid limits" `[CITED: CV]` — i.e., it tracks headroom to a hard limit and acts before breaching it, exactly the operating-margin concept. Pivot: *"The voltage-stability margin is the same headroom-to-a-physical-limit signal I built into my HEMS — estimate the limit, watch the distance to it, act before you cross it."*

---

## TVS-02 — DC Power-Flow Angle Inference (deep: P=Bθ, linear WLS)

**Depth: FULL (criteria-named). Build directly on KAL-01.** `[CITED: Abur & Expósito Ch. on linear/DC SE; standard DC power-flow]`

### DC approximation assumptions
1. Flat voltage magnitudes: $V_i \approx 1.0$ p.u. everywhere.
2. Small angle differences: $\sin(\theta_i-\theta_j)\approx(\theta_i-\theta_j)$, $\cos(\cdot)\approx 1$.
3. Lossless lines: neglect resistance ($r \ll x$), so branch admittance ≈ $1/x = b$ (susceptance).
Result: **real power flow is linear in angles.** `[ASSUMED — standard DC-load-flow assumptions, confirm wording]`

### P = B·θ derivation
- Branch flow from bus $i$ to $j$:
$$P_{ij} = b_{ij}\,(\theta_i - \theta_j), \qquad b_{ij} = \frac{1}{x_{ij}}$$
- Bus power injection = sum of outgoing flows. Stacking all buses:
$$\mathbf{P} = \mathbf{B}\,\boldsymbol{\theta}$$
where $\mathbf{B}$ is the **DC Bbus matrix** (a weighted graph Laplacian in susceptances):
$$B_{ii} = \sum_{k\in\mathcal{N}(i)} b_{ik}, \qquad B_{ij} = -b_{ij}\ (i\neq j,\ \text{if connected, else }0)$$
- **Slack/reference bus:** $\mathbf{B}$ is singular (rows sum to zero — angles only matter relative to a reference). Fix $\theta_{slack}=0$ and delete its row/column to make the reduced system solvable. `[ASSUMED — standard, confirm]`

### Sparse-PMU observability gap
- PMUs directly measure bus voltage *phasors* (magnitude + angle) and line-current phasors. If a PMU sits on every bus, angles are measured directly. In reality PMU coverage is **sparse and expensive**, so most bus angles are **unmeasured** and must be *inferred* from the measurements you do have. This is exactly a state-estimation problem on angles. `[ASSUMED — confirm with C37.118/Phase-4 context]`

### Angle estimation as linear WLS (the KAL-01 link)
- Measurement model is **linear** in DC: $z = H\theta + e$, where rows of $H$ encode line-flow / injection sensitivities (entries are susceptances). Because $h$ is linear, the KAL-01 Gauss-Newton iteration **collapses to a one-shot solve**:
$$\hat{\boldsymbol\theta} = (H^\top W H)^{-1} H^\top W\, z, \qquad W = R^{-1}$$
- This is the same normal-equations form as KAL-01 §3, with $H$ now *constant* (no relinearization). **Explicitly say in the note: "DC SE is the linear case of the WLS/Gauss-Newton estimator from KAL-01 — one iteration, no Jacobian re-evaluation."**

### 3-bus worked numbers (also drive the demo — see §Demo)
Use line reactances giving susceptances $b_{12}=10$, $b_{13}=10$, $b_{23}=10$ p.u. (round numbers for clean arithmetic). Slack = bus 1, $\theta_1=0$. State = $[\theta_2,\theta_3]$. Reduced B:
$$B_{red} = \begin{bmatrix} b_{12}+b_{23} & -b_{23}\\ -b_{23} & b_{13}+b_{23}\end{bmatrix} = \begin{bmatrix} 20 & -10\\ -10 & 20\end{bmatrix}$$
Pick true injections (e.g., $P_2=-1.0$, $P_3=-0.5$ p.u. loads), solve $B_{red}\theta=P$ for ground-truth angles, then generate redundant measurements (see Demo). `[ASSUMED — illustrative numbers chosen for clean demo; verify the solve in code]`

### OSED bridge (TVS-02)
Strongest analog: **inferring unmeasured state from sparse, redundant sensors.** OSED's building thermal estimator "learns and predicts thermal building state" from BMS sensors using ML/convex optimization `[CITED: CV]`; SI-MAPPER infers structured state (ontology) from images where direct labels are absent. Pivot: *"Sparse PMU angle inference is the same shape as my OSED thermal estimator — too few direct sensors, so you infer the full state vector from a redundant set via weighted least squares."*

---

## TVS-03 — Observability + Bad-Data Detection (deep: χ², rN, leverage, rank)

**Depth: FULL for χ²/rN/rank; AWARENESS for leverage intuition (D-08). Build on KAL-01 §4.** `[CITED: Abur & Expósito Ch.5 "Network Observability" & Ch.6 "Bad Data Detection"; cross-verified WebSearch on residual-sensitivity / LNR]`

### Observability via measurement Jacobian rank
- The system is **numerically observable** iff the gain matrix $G=H^\top W H$ is nonsingular, equivalently $H$ has **full column rank** ($\mathrm{rank}(H)=n$, the number of states). `[VERIFIED: WebSearch + KAL-01]`
- If $\mathrm{rank}(H)<n$, there are **unobservable states / islands** — no measurement set pins them down. In the note, show `numpy.linalg.matrix_rank(H)` as the practical check, and connect to KAL-01's "unobservable island" language.
- **Topological vs. numerical observability:** topological = a graph/spanning-tree argument on which buses have incident measurements; numerical = the actual rank of $H$ at the operating point. Mention both names; the rank test is the operational one.

### Chi-squared detection (is there bad data?)
- After WLS, the weighted residual cost
$$J(\hat x) = r^\top W r, \qquad r = z - H\hat x$$
follows $\chi^2$ with $m-n$ degrees of freedom ($m$ measurements − $n$ states = redundancy). `[VERIFIED: KAL-01, Abur & Expósito]`
- **Detection rule:** if $J(\hat x) > \chi^2_{(m-n,\,1-\alpha)}$ (e.g., $\alpha=0.05$, 95% confidence), at least one measurement is bad. χ² tells you *that* bad data exists, not *which*. `[VERIFIED: WebSearch — "χ² test … if there are bad data; LNR shows exactly which"]`

### Largest-normalized-residual (rN) identification (which measurement?)
- Residual covariance / sensitivity:
$$\Omega = R - H\,(H^\top W H)^{-1} H^\top = R - H\,G^{-1}H^\top$$
(equivalently the residual sensitivity matrix $S=I-H G^{-1}H^\top W$, with $r=S\,e$). `[VERIFIED: WebSearch — "residual sensitivity matrix P = I − H(HᵀH)⁻¹Hᵀ"; Abur & Expósito form]`
- **Normalized residual** for each measurement:
$$r_i^N = \frac{|r_i|}{\sqrt{\Omega_{ii}}}$$
- **Identification rule:** the measurement with the **largest $r_i^N$ above a threshold ≈ 3** (3σ) is the prime suspect. Remove it, re-run WLS, re-test. `[VERIFIED: threshold ~3 is standard; KAL-01 + Abur & Expósito]`

### The critical limitation — leverage measurements (AWARENESS, but interview gold)
- **Leverage measurements** sit at buses whose observability depends entirely on them. Their residual is structurally near-zero (the estimator fits them perfectly), so a gross error in a leverage measurement is **invisible to the rN test** — it produces a wrong-but-consistent estimate. `[CITED: KAL-01 §4 already states this; Abur & Expósito Ch.6]`
- Also note **multiple interacting + conforming** bad data can defeat single-rN (errors agree and mask each other). `[VERIFIED: WebSearch — "two bad data both interacting and conforming … LNRT may fail"]`
- Interview sentence (reuse KAL-01's): *"The normalized-residual test has a structural blind spot — leverage measurements at sparsely instrumented buses have near-zero residuals even when corrupted, which is why critical buses need redundant measurement placement."*

### OSED bridge (TVS-03 — the single strongest bridge in the phase)
Juan's CV: *"Analyzed errors in baseline consumption estimation by processing billions of data points across multiple substations"* `[CITED: CV — Data Science section]`. This is **literally bad-data detection at substation scale**. Pivot: *"Bad-data detection is exactly what I did analyzing baseline-estimation errors across billions of points from multiple substations — finding the corrupted or anomalous measurements that throw off the estimate, which is the chi-squared / normalized-residual problem in production."* Secondary: OSED edge sensor-fault handling ↔ flagging a bad reading before it corrupts a control decision.

---

## TVS-04 — Asset-Health Estimation (deep: C57.91 hot-spot ODE; aware: DGA/DLR/RUL)

**Depth: FULL for C57.91 ODE; AWARENESS for DGA, DLR productization, RUL (D-08).** `[CITED: IEEE C57.91-2011 loading guide; cross-verified WebSearch]`

### IEEE C57.91 transformer thermal model (the must-know derivation)
Two coupled first-order ODEs, ambient → top-oil → winding hot-spot:

**Top-oil temperature rise** (over ambient), driven by load:
$$\tau_{TO}\,\frac{d\,\Delta\theta_{TO}}{dt} = \Delta\theta_{TO,\,U}\left(\frac{K^2 R + 1}{R+1}\right)^{n} - \Delta\theta_{TO}$$
where $K=I/I_{rated}$ (per-unit load), $R$ = ratio of load-loss to no-load-loss, $\tau_{TO}$ = top-oil time constant (hours-scale), $n$ = oil exponent, $\Delta\theta_{TO,U}$ = ultimate top-oil rise at rated load.

**Hot-spot (winding) temperature rise** over top-oil, faster dynamics:
$$\tau_{w}\,\frac{d\,\Delta\theta_{HS}}{dt} = \Delta\theta_{HS,\,U}\,K^{2m} - \Delta\theta_{HS}$$
with winding time constant $\tau_w$ (minutes-scale) and winding exponent $m$.

**Hot-spot temperature:**
$$\theta_{HS} = \theta_{ambient} + \Delta\theta_{TO} + \Delta\theta_{HS}$$
`[ASSUMED — this is the standard C57.91 loading-guide differential form; confirm exact exponent/constant placement against the standard before locking. The structure (two cascaded first-order rises, load-driven, exponents m,n, time constants τ_TO ≫ τ_w) is correct and textbook-standard.]` `[VERIFIED: WebSearch — "C57.91 uses a differential equation for top-oil rise relative to ambient; hot-spot as function of loading"]`

**Why this is a virtual-sensing story:** you rarely measure the winding hot-spot directly (it's buried in the windings); you *infer* it from load current + ambient via this ODE — identical in spirit to the IEEE 738 conductor-temperature EKF Juan already built in Phase 1 (KAL-03/04). Note this parallel explicitly.

**Aging / loss-of-life (the payoff):** Arrhenius relation — insulation life is consumed exponentially with hot-spot temperature:
$$\text{per-unit life} = A\,\exp\!\left(\frac{B}{\theta_{HS}+273}\right), \quad A=9.8\times10^{-18},\ B=15000$$
`[VERIFIED: WebSearch — "A exp(B/(θH+273)), A=9.8e-18, B=15000 in IEEE Std C57.91-2011"]` Equal-life loading: the hot-spot temperature, not the load, determines insulation aging.

### DGA — Dissolved Gas Analysis (AWARENESS, no derivation)
- Oil decomposes under thermal/electrical stress, releasing **key gases**; the gas *pattern* fingerprints the fault. Key gases: **H₂** (partial discharge), **CH₄ / C₂H₆** (low-temp thermal), **C₂H₄** (high-temp thermal/overheating), **C₂H₂** (arcing — most severe), **CO/CO₂** (cellulose/paper degradation). `[ASSUMED — standard DGA key-gas associations; awareness level only]`
- Interpretation methods (name only): **Duval Triangle** (CH₄/C₂H₄/C₂H₂ proportions → fault zone), **Rogers Ratios**, **Key Gas method**, IEC 60599. Say: *"DGA is a virtual sensor for internal fault type — you infer what's failing inside a sealed tank from the gas signature in the oil."*

### Dynamic Line Rating (AWARENESS — product framing, link to Phase 1)
- DLR = computing a conductor's *real-time* ampacity from actual weather + the IEEE 738 thermal balance, instead of a fixed conservative static rating. Juan **already built this** in the Phase 1 demo (`ieee738_ampacity`, `ekf_line_temp_demo.py`) `[VERIFIED: read in session]`. Frame it as a *virtual-sensing PRODUCT*: "infer the unmeasured conductor temperature → unlock 10–30% more line capacity headroom." Reference Phase 1's demo rather than re-deriving IEEE 738.

### Remaining Useful Life (AWARENESS, framing only)
- RUL = projecting cumulative damage (e.g., transformer loss-of-life from the Arrhenius aging integral; conductor annealing; insulation wear) forward to estimate time-to-end-of-life. It's the asset-health output that turns a virtual temperature/condition estimate into a maintenance/replacement decision. Keep it conceptual — no model derivation.

### OSED bridge (TVS-04)
Strongest analog: **inferring an unmeasured physical quantity from proxy telemetry to drive a decision.** OSED/Building Intelligence "learns and predicts thermal building state" and runs predictive control on it `[CITED: CV]`; the conductor/transformer hot-spot is the grid version. Pivot: *"Transformer hot-spot and DLR are the same virtual-sensing pattern as my building thermal estimator — you can't measure the quantity that matters (winding temperature, conductor temperature, zone thermal state) directly, so you infer it from a physics model plus available telemetry and act on the estimate."* Note: this satisfies success-criterion 4's "connect each to an OSED analog" most directly.

---

## Demo — Exact Specification (TVS-02 + TVS-03)

`[ASSUMED — fully specified illustrative setup; numbers must be confirmed by running the code]`

### Network: 3-bus DC system
- Buses 1,2,3. Lines: 1–2, 1–3, 2–3. Susceptances $b_{12}=b_{13}=b_{23}=10$ p.u. (reactances $x=0.1$ p.u. each).
- **Slack = bus 1**, $\theta_1=0$. State $x=[\theta_2,\theta_3]$ → $n=2$.
- Reduced B: $\begin{bmatrix}20 & -10\\ -10 & 20\end{bmatrix}$. True loads $P_2=-1.0$, $P_3=-0.5$ p.u. → solve $B_{red}\theta=P$ for $\theta_{true}$ (≈ $[-0.0833,-0.0667]$ rad — verify in code).

### Measurement set (redundant: m > n for χ² to have DOF)
Choose **m = 5** measurements, $n=2$ states → **m−n = 3** degrees of redundancy (χ² has df=3):
1. Power injection at bus 2
2. Power injection at bus 3
3. Line flow 1→2
4. Line flow 1→3
5. Line flow 2→3

Each row of $H$ is the linear sensitivity of that quantity to $[\theta_2,\theta_3]$ (susceptance entries). Generate $z = H\theta_{true} + e$, $e\sim\mathcal N(0,R)$, with small $R$ (e.g., $\sigma=0.01$ p.u.). `np.random.seed(42)` for reproducibility (Phase-1 convention).

### Bad-data injection + detection flow
1. **Corrupt measurement 5** (line flow 2→3): add a gross error (e.g., +10σ to +20σ) so its normalized residual clearly exceeds 3.
2. WLS solve #1 → residuals → $J(\hat\theta)=r^\top W r$ → compare to `chi2.ppf(0.95, df=3)`. Expect $J$ **above** threshold → "bad data detected."
3. Compute $\Omega=R-HG^{-1}H^\top$, normalized residuals $r_i^N=|r_i|/\sqrt{\Omega_{ii}}$. Expect $\arg\max = $ measurement 5, value > 3.
4. Remove measurement 5 (m→4, df→2), WLS solve #2. Expect $J$ now **below** threshold and $\hat\theta$ back near $\theta_{true}$.

### Output (mirror Phase-1 demo)
- **Console readout** (`print("="*62)` banner): df, χ² threshold, $J$ before/after, flagged measurement index + its $r^N$, true vs estimated angles before/after removal.
- **PNG** (`dc_powerflow_baddata.png`, saved beside script via `script_dir` pattern): e.g., 2 panels — (a) bar chart of normalized residuals with the 3σ line and the flagged bar highlighted; (b) true vs estimated angles before/after bad-data removal.
- **README.md**: same shape as Phase-1 (`What it demonstrates` / `Prerequisites` / `Run` / `Output` / `Interview value`). Interview value line: *"3-bus DC state estimator that detects and removes a corrupted measurement via chi-squared + largest-normalized-residual — the textbook TVS-02+TVS-03 illustration, built from scratch in NumPy."*

### Reuse from Phase 1 (D-02)
- WLS normal-equations solve pattern (KAL-01 §3 form, linear → one shot).
- `scipy.stats.chi2.ppf` (already used in `nis_check`).
- `matplotlib.use('Agg')`, `np.random.seed`, `script_dir`+`savefig`, banner-style console block, README structure.
- **Optional cheap TVS-01 touch (discretionary, D-03/Discretion):** could add a 3-line Thevenin VSI computation on one bus from the solved state, but only if it stays under the ~80-line budget. Recommend **skip** to keep the demo tight and on-message (TVS-02/03).

## Common Pitfalls

### Pitfall 1: Re-deriving WLS instead of referencing KAL-01
**What goes wrong:** TVS-02/03 notes balloon and duplicate Phase-1 content; runway wasted.
**Why:** The topics genuinely share machinery, so it's tempting to restate it.
**How to avoid:** Open TVS-02 with an explicit "this is the linear case of KAL-01" pointer; show only the DC-specific collapse (one-shot solve) and the B-matrix construction.
**Warning sign:** A TVS-02 section that re-explains Gauss-Newton iteration.

### Pitfall 2: χ² with too little redundancy
**What goes wrong:** If $m-n$ is tiny (e.g., 1), the χ² test is weak and the demo's "detected" result is unconvincing.
**Why:** Few degrees of redundancy → low detection power.
**How to avoid:** Use m=5, n=2 (df=3) as specified; redundancy ≥ 3 makes the demo crisp.
**Warning sign:** $J(\hat\theta)$ barely moves when the bad measurement is removed.

### Pitfall 3: Confusing detection (χ²) with identification (rN)
**What goes wrong:** Note implies χ² names the bad measurement.
**Why:** Both are "bad-data" steps; easy to conflate.
**How to avoid:** State the division of labor explicitly — χ² answers *"is there bad data?"*, rN answers *"which one?"* `[VERIFIED: WebSearch]`

### Pitfall 4: Stating the C57.91 ODE constants without verifying placement
**What goes wrong:** Exact exponent/time-constant placement in the top-oil/hot-spot equations varies between the IEEE Annex G (detailed) and Clause 7 (exponential) models; getting it subtly wrong invites a correction from a transformer-savvy interviewer.
**Why:** The standard has two thermal models; secondary sources paraphrase differently.
**How to avoid:** Present the *structure* confidently (two cascaded first-order rises, load-driven, exponents m,n, $\tau_{TO}\gg\tau_w$) and tag exact constants as "per IEEE C57.91"; the planner should flag the precise equation for a quick confirm pass. Marked `[ASSUMED]` in §TVS-04.

## Code Examples

### DC WLS one-shot solve (note + demo)
```python
# Linear DC state estimation — KAL-01 normal equations, no iteration
import numpy as np
W = np.diag(1.0 / sigma**2)            # W = R^-1
G = H.T @ W @ H                        # gain / information matrix
theta_hat = np.linalg.solve(G, H.T @ W @ z)
r = z - H @ theta_hat                  # residuals
J = r @ W @ r                          # weighted residual cost ~ chi2(m-n)
```

### Chi-squared detection + normalized-residual identification
```python
from scipy.stats import chi2
m, n = H.shape
df = m - n
threshold = chi2.ppf(0.95, df)
bad_data = J > threshold               # detection

Omega = np.diag(1/np.diag(W)) - H @ np.linalg.inv(G) @ H.T   # R - H G^-1 H^T
rN = np.abs(r) / np.sqrt(np.diag(Omega))                     # normalized residuals
suspect = int(np.argmax(rN))           # identification: largest rN (> ~3)
```
`[CITED: Abur & Expósito residual-sensitivity form; verified consistent with KAL-01 + WebSearch]`

### Observability rank check (TVS-03 note)
```python
n_states = H.shape[1]
observable = np.linalg.matrix_rank(H) == n_states   # full column rank
```

## State of the Art

| Old Approach | Current Approach | When | Impact (for the notes) |
|--------------|------------------|------|------------------------|
| SCADA-only static WLS (4 s scans) | PMU-assisted linear/hybrid SE, 30–120 Hz | 2010s+ | TVS-01/02 framing leans on PMU phasors; note this is *why* Thevenin-VSI and direct-angle measurement are now feasible |
| Static (nameplate) line ratings | Dynamic Line Rating (IEEE 738 real-time) | mature | TVS-04 DLR = the virtual-sensing product story; Juan already demoed it (Phase 1) |
| Periodic offline DGA lab samples | Online DGA monitors + ML interpretation | recent | TVS-04 awareness: DGA as continuous virtual fault sensor |
| Fixed-threshold loss-of-life | Hot-spot-driven dynamic loss-of-life / RUL | mature | TVS-04 C57.91 Arrhenius aging → RUL framing |

**Note:** IEEE C57.91 is **under major revision, next edition expected 2025–2026** `[VERIFIED: WebSearch — IEEE PES]`. Cite the 2011 edition; mention a revision is in progress (shows currency awareness).

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Exact placement of exponents $m,n$ and time constants in the C57.91 top-oil/hot-spot ODEs | TVS-04 | LOW-MED — structure is right; a transformer expert could correct a constant. Planner should flag a quick confirm against the standard. |
| A2 | DC power-flow assumptions phrasing (flat V, small-angle, lossless) and slack-bus row/col deletion | TVS-02 | LOW — these are textbook-standard; wording confirm only |
| A3 | 3-bus illustrative numbers ($b=10$, loads $-1.0/-0.5$, resulting angles) | TVS-02 / Demo | LOW — must be confirmed by running the demo code; any clean set works |
| A4 | DGA key-gas → fault-type associations (H₂/PD, C₂H₂/arcing, etc.) | TVS-04 | LOW — standard associations; awareness level, low exposure |
| A5 | P-V nose ↔ power-flow Jacobian singularity phrasing | TVS-01 | LOW — corroborated by WebSearch |
| A6 | Sparse-PMU coverage framing (PMUs measure phasors directly; sparse in practice) | TVS-02 | LOW — deeper C37.118/PMU treatment is Phase 4; awareness here |

**All other claims are VERIFIED (tool/import/WebSearch) or CITED (KAL-01, CV, Abur & Expósito).** The χ²/rN/leverage/observability core (TVS-03) is verified against both KAL-01 and external sources — highest confidence.

## Open Questions

1. **Exact C57.91 ODE constant placement**
   - What we know: the two-cascaded-first-order-rise structure with load drive, exponents $m,n$, $\tau_{TO}\gg\tau_w$, and Arrhenius aging ($A=9.8e{-}18$, $B=15000$) are correct.
   - What's unclear: precise exponent/constant placement differs between C57.91 Clause 7 (exponential) and Annex G (detailed) models.
   - Recommendation: present structure confidently, tag constants "per IEEE C57.91-2011," and have the executor do a 5-minute confirm pass against a C57.91 summary before locking TVS-04's display equations. Not a blocker for planning.

2. **Whether to add the optional TVS-01 Thevenin touch to the demo**
   - What we know: D-03 allows it "if trivially cheap"; the demo budget is ~80 lines.
   - Recommendation: **skip** — keep the demo tight on TVS-02/03. If the executor finds headroom, a single-bus VSI printout is the cheapest add. Planner's call.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| numpy | demo | ✓ | 1.26.4 | — |
| scipy | demo (chi2.ppf) | ✓ | 1.11.4 | hard-coded χ² value (not needed) |
| matplotlib | demo PNG | ✓ | 3.6.3 | console-only output (not needed) |
| python3 | demo | ✓ | (3.x, runs Phase-1 demo) | — |

**Missing dependencies with no fallback:** None.
**Missing dependencies with fallback:** None needed — environment matches Phase 1 exactly. `[VERIFIED: python3 import succeeded for all three]`

> **Note:** The four notes themselves have **zero external dependencies** — pure markdown + LaTeX. Only the single demo needs the stack above.

## Project Constraints (from CLAUDE.md)

- **Math rendering:** LaTeX-in-markdown ($…$ inline, $$…$$ display) — reinforced by D-10 and the project's auto-memory ("LaTeX in markdown for math docs").
- **Depth strategy:** "Depth where it differentiates; awareness elsewhere" — exactly the D-08 deep-vs-aware split. CLAUDE.md's "What NOT to Over-Invest In" table aligns (e.g., don't deep-dive protocol internals here — that's Phase 4).
- **Scope discipline:** Target this role's named gaps + reframe Juan's existing strengths (the bridge boxes) rather than re-studying. The OSED/HEMS/SI-MAPPER analogs are the differentiation.
- **GSD workflow:** all file changes go through a GSD command (this is a research artifact, written via the research flow).
- **No git worktrees** (`workflow.use_worktrees=false` confirmed in config) — execution stays on main tree.
- **Crash-prep timeline:** ~1 week from 2026-06-13 — prioritize the criteria-named deep items; keep aware items crisp.

## Sources

### Primary (HIGH confidence)
- **Abur & Expósito, "Power System State Estimation: Theory and Implementation" (2004)** — DC/linear SE, residual sensitivity $\Omega=R-HG^{-1}H^\top$, χ² test, largest-normalized-residual, observability via $H$ rank. (Standard reference; corroborated by sources below.)
- **Phase 1 artifacts (read in session):** `KAL-01-wls-state-estimation.md` (WLS, Gauss-Newton, χ², LNR, leverage trap), `KAL-02-kalman-family-kf-ekf-ukf.md` (note style), `ekf_line_temp_demo.py` + `README.md` (demo style, IEEE 738/DLR, `chi2.ppf` usage). `[VERIFIED]`
- **CV — `Juan Carlos Oviedo Cepeda - 2026.pdf`** (read pages 1–2): OSED, Building Intelligence/Predictive Control, HEMS, SI-MAPPER, baseline-estimation error analysis across substations. `[VERIFIED]` — grounds all bridge boxes.
- **IEEE C57.91-2011** loading guide (transformer top-oil/hot-spot thermal model, Arrhenius aging). `[CITED]`
- **IEEE 738** (conductor thermal model / DLR) — already worked in Phase 1; reference back. `[CITED]`
- **Local env import check** — numpy 1.26.4 / scipy 1.11.4 / matplotlib 3.6.3. `[VERIFIED]`

### Secondary (MEDIUM confidence)
- WebSearch — Thevenin impedance-matching VSI / PMU local voltage-stability monitoring: [OSTI 1572408](https://www.osti.gov/servlets/purl/1572408), [ScienceDirect S2352467718300067](https://www.sciencedirect.com/science/article/abs/pii/S2352467718300067), [IET GTD Pourbagher 2022](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/gtd2.12400) — confirms $|Z_{load}|=|Z_{Thev}|$ collapse, VSI 0→1 range, Jacobian-singularity at nose, multi-load limitation.
- WebSearch — largest-normalized-residual / residual-sensitivity / χ² vs LNR division of labor: [ResearchGate 266630232 (LNR test)](https://www.researchgate.net/publication/266630232), [arXiv 2001.10764](https://arxiv.org/abs/2001.10764) — confirms $P=I-H(H^TH)^{-1}H^T$ sensitivity form, χ²-detects/LNR-identifies, interacting-conforming failure mode.
- WebSearch — IEEE C57.91 thermal model & aging: [IEEE PES C57.91 page](https://ieee-pes.org/trending-tech/ieee-c57-91-guide-for-loading-mineral-oil-immersed-transformers-and-step-voltage-regulators/), [arXiv 1805.00630](https://arxiv.org/pdf/1805.00630) — confirms top-oil ODE, Arrhenius $A\exp(B/(\theta_H+273))$ with $A=9.8e{-}18$, $B=15000$, 2025–2026 revision in progress.

### Tertiary (LOW confidence — flagged in Assumptions Log)
- Exact C57.91 ODE exponent/time-constant placement (A1) — structure verified, constants tagged "per standard" pending a confirm pass.
- DGA key-gas associations (A4) — standard but awareness-level; not deeply verified this session.

## Metadata

**Confidence breakdown:**
- TVS-02/03 (WLS, B=Bθ, χ², rN, observability): **HIGH** — textbook-standard, verified against KAL-01 + external sources + supplied worked numbers.
- TVS-01 (P-V, Thevenin VSI, margin): **HIGH** — impedance-matching VSI confirmed by multiple sources.
- TVS-04 (C57.91 ODE): **MEDIUM-HIGH** — structure and aging law verified; exact constant placement flagged (A1).
- TVS-04 awareness items (DGA/DLR/RUL): **MEDIUM** — standard associations, awareness depth only (matches D-08).
- Demo spec: **HIGH** — fully specified; numbers to be confirmed by running code (A3).
- Bridge material: **HIGH** — every analog grounded in the CV (read in session), not invented.

**Research date:** 2026-06-13
**Valid until:** stable domain — equations don't move; ~30 days. (Watch only the C57.91 2025–2026 revision for TVS-04 constant updates.)
