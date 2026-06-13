# Phase 2: Transmission Virtual Sensing - Pattern Map

**Mapped:** 2026-06-13
**Files analyzed:** 7 to-be-created (4 notes + demo script + demo README + demo PNG)
**Analogs found:** 7 / 7 (every new file maps directly to a Phase 1 artifact)

> This is a study-notes phase. "Role" is the artifact type (study-note / demo-script /
> demo-readme / generated-figure) and "data flow" is the document's pedagogical shape
> (equation-derivation, worked-example, or numeric WLS pipeline). The Phase 1 artifacts in
> `01-kalman-state-estimation/` are the literal templates — the executor mirrors their
> structure, not just their spirit.

## File Classification

| New File | Role | Data Flow | Closest Analog | Match Quality |
|----------|------|-----------|----------------|---------------|
| `notes/TVS-01-voltage-stability.md` | study-note | equation-derivation (deep) | `notes/KAL-01-wls-state-estimation.md` | exact (style) |
| `notes/TVS-02-dc-powerflow-angle-wls.md` | study-note | equation-derivation (deep, linear-WLS) | `notes/KAL-01-wls-state-estimation.md` | exact (style + WLS content extends KAL-01) |
| `notes/TVS-03-observability-bad-data.md` | study-note | equation-derivation (deep, χ²/rN) | `notes/KAL-01-wls-state-estimation.md` §4 | exact (style + content is KAL-01 §4 specialized) |
| `notes/TVS-04-asset-health.md` | study-note | worked-example + awareness mix | `notes/KAL-03-ieee738-ekf-worked-example.md` (depth) + `KAL-01`/`KAL-02` (header/section style) | exact (style) / role-match (ODE worked-example) |
| `demo/dc_powerflow_baddata_demo.py` | demo-script | numeric WLS pipeline (linear, one-shot) | `demo/ekf_line_temp_demo.py` | exact (skeleton) / role-match (linear WLS vs EKF) |
| `demo/README.md` | demo-readme | doc | `demo/README.md` (KAL-04) | exact |
| `demo/dc_powerflow_baddata.png` | generated-figure | matplotlib output | `demo/ekf_line_temp.png` | exact (generation pattern) |

**Note slug names above are illustrative** — exact slugs are Claude's discretion (D-09 only
fixes the `TVS-0X` prefix and `notes/` location).

## Shared Patterns

These cross-cutting patterns apply to **all four notes** and are extracted once here. Per-file
sections below reference them rather than repeating.

### SP-1 — Note header block (apply to ALL four notes)
**Source:** `notes/KAL-01-wls-state-estimation.md` lines 1-7 (and KAL-02 lines 1-8). D-10 locks this exact `For:`/`Purpose:` form.

```markdown
# KAL-01: WLS / Gauss-Newton Power-System State Estimation

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Close the vocabulary gap on state estimation so you can engage the interviewer's
questions on Kalman, WLS, and observability with specifics, not generalities.

---
```
Mirror exactly: `# TVS-0X: <Title>`, then `**For:** Oral rehearsal — …`, `**Purpose:** …`,
then `---`. Do NOT use the KAL-03 `**Phase:**/**Deliverable:**` variant — D-10 names the
KAL-01/02 `For:`/`Purpose:` header.

### SP-2 — Numbered mental-model-first sections (apply to ALL four notes)
**Source:** KAL-01 section pattern — `## 1. What WLS State Estimation Is (Mental Model First)` (line 9), `## 2. The WLS Objective Function` (line 41), `## 3. The Gauss-Newton Iteration (How You Actually Solve It)` (line 59), `## 4. Interview Vocabulary (The Terms You Must Own)` (line 98).

Pattern: each `## N.` section opens with a plain-language mental model, THEN the equations.
Inside sections, KAL-01 embeds bolded cue phrases and a `**One-liner for the interview:**` /
`**Interview sentence:**` quote (KAL-01 lines 36, 110, 147). Reuse these inline-cue conventions —
they are the "speak-aloud recall" device D-10 requires.

### SP-3 — LaTeX-in-markdown math (apply to ALL four notes)
**Source:** KAL-01 lines 19, 27, 45 (`$$ … $$` display) and inline `$x$`, `$W = R^{-1}$`. Also a project auto-memory convention ("LaTeX in markdown for math docs").
- Display equations: `$$ … $$` on their own lines.
- Inline math: `$…$`.
- Matrix/aligned blocks use `\begin{aligned} … \end{aligned}` (see KAL-02 lines 20-23, 34-37) for the C57.91 coupled ODEs in TVS-04 and the reduced-B matrix in TVS-02.

### SP-4 — "→ Bridge to your work" box (apply to ALL four notes — D-04)
**Source:** KAL-01 §6 "OSED Bridge" lines 177-213. The exact shape to reuse:
1. A `> blockquote` stating the analog crisply (KAL-01 lines 184-186).
2. A comparison **table** mapping grid concept ↔ Juan's-work concept (KAL-01 lines 190-197).
3. A `**How to say this in the interview:**` followed by a `> blockquote` pivot sentence (KAL-01 lines 204-212).

```markdown
> **"OSED's convex optimization formulates a quadratic objective over building state variables
> from sensor measurements — same minimize-weighted-squared-residuals logic, just swapping
> AC power-flow for an RC thermal model."**

| Power-System WLS | OSED Convex Optimization |
|-----------------|--------------------------|
| State vector $x = [V,\, \theta]$ per bus | State vector $= [T_\text{zone}, P_\text{HVAC}, …]$ per building |
| …               | …                        |

**How to say this in the interview:**
> "I have implemented the WLS objective in a different physical domain: …"
```
Per-note bridge **content** (which OSED/HEMS/SI-MAPPER analog) is supplied in RESEARCH.md
(§TVS-01..04 "OSED bridge" paragraphs) — TVS-03's "billions of points across substations"
bridge is the strongest. Do NOT build an aggregate table (D-05; that is Phase 6).

### SP-5 — "<3-min say-aloud version" talk-track (apply to ALL four notes — D-06)
**Source:** No literal Phase-1 heading, but KAL-01's `**One-liner for the interview:**` (line 36) and the RESEARCH.md "Canonical aloud explanation" blocks (e.g., RESEARCH §TVS-01 lines 171-172) are the raw material. Render as a `## <3-min say-aloud version` section containing a compressed spoken script (`> blockquote`) that hits the criterion's named points. Placement (top or bottom of note) is Claude's discretion.

### SP-6 — "Quick-Recall Card" + Sources line (apply to ALL four notes)
**Source:** KAL-01 lines 216-230 and KAL-02 lines 330-358.
- `## Quick-Recall Card (Recite Before the Interview)` — a numbered list (KAL-01 lines 218-226) of the must-recite facts/equations, ending with `**My bridge:**` (KAL-01 line 226).
- Closing italic `*Sources: …*` line (KAL-01 line 230). Cite Abur & Expósito, the relevant KAL note, and CV — per RESEARCH.md Sources.

---

## Pattern Assignments

### `notes/TVS-01-voltage-stability.md` (study-note, equation-derivation deep)

**Analog:** `notes/KAL-01-wls-state-estimation.md` (style) — content is NEW (Thevenin VSI, no Phase-1 equivalent).

**Apply:** SP-1, SP-2, SP-3, SP-4, SP-5, SP-6.

**Section skeleton** (mirrors KAL-01's mental-model-first numbering; content from RESEARCH §TVS-01):
1. P-V (nose) curve and collapse mechanism — nose = power-flow Jacobian singular.
2. Thevenin-equivalent VSI from local PMU data — $|Z_{load}|=|Z_{Thev}|$ at collapse; $\mathrm{VSI}=|Z_{Thev}|/|Z_{load}|\in[0,1]$.
3. Operating / loadability margin = distance to nose ($1-\mathrm{VSI}$).
4. Known limitation (awareness): single-port Thevenin breaks down for multi-load systems.

**Bridge content (SP-4):** margin-to-constraint monitoring in HEMS (RESEARCH §TVS-01 line 178). Depth: FULL for P-V/VSI/margin (D-08); awareness for the multi-load limitation.

---

### `notes/TVS-02-dc-powerflow-angle-wls.md` (study-note, deep — linear WLS)

**Analog:** `notes/KAL-01-wls-state-estimation.md` — both for STYLE (SP-1..6) and for direct CONTENT REUSE: TVS-02 is the linear specialization of KAL-01.

**WLS normal-equations pattern to reuse** — `notes/KAL-01-wls-state-estimation.md` lines 73-86:
```markdown
**Step 2 — Form the gain matrix (information matrix):**
$$G = H^\top W H$$
**Step 3 — Compute the state correction:**
$$\Delta x = G^{-1} H^\top W\, [z - h(\hat{x})]$$
```
TVS-02 must show the **DC collapse** of this: because $h(\theta)=H\theta$ is linear, Gauss-Newton
becomes a one-shot solve $\hat\theta=(H^\top W H)^{-1}H^\top W z$ (RESEARCH §TVS-02 lines 204-207).
**Explicitly cross-reference KAL-01 §3** and do NOT re-derive Gauss-Newton (anti-pattern, RESEARCH lines 136, 330-334).

**Section skeleton** (content from RESEARCH §TVS-02):
1. DC approximation assumptions (flat V, small-angle, lossless).
2. $P = B\theta$ derivation; $\mathbf B$ = susceptance-weighted graph Laplacian; slack-bus row/col deletion.
3. Sparse-PMU observability gap (awareness — deeper C37.118 is Phase 4).
4. Angle estimation as linear WLS — the KAL-01 link (one-shot solve).
5. 3-bus worked numbers ($b=10$, $B_{red}=[[20,-10],[-10,20]]$, loads $-1.0/-0.5$) — these also drive the demo.

**Use the `\begin{aligned}`/matrix LaTeX from SP-3** for $B_{red}$. **Bridge content (SP-4):** OSED thermal estimator infers full state from sparse redundant sensors (RESEARCH §TVS-02 line 215).

---

### `notes/TVS-03-observability-bad-data.md` (study-note, deep — χ²/rN/rank)

**Analog:** `notes/KAL-01-wls-state-estimation.md` §4 — TVS-03 IS KAL-01 §4 ("Bad-Data Detection: Chi-Squared Test", "Leverage Measurements") specialized to the linear DC case.

**χ² + LNR + leverage-trap content to reuse/extend** — `notes/KAL-01-wls-state-estimation.md` lines 122-151:
```markdown
After convergence, the weighted residual sum $J(\hat{x}) = r^\top W r$ follows a **chi-squared
distribution** with $m - n$ degrees of freedom … If $J(\hat{x}) > \chi^2_{\text{threshold}}(m-n, 0.95)$
… at least one measurement is bad. The **Largest Normalized Residual (LNR) test** then
identifies the culprit: compute $r_i / \sqrt{\Omega_{ii}}$ …
```
Leverage-measurement interview sentence to lift — KAL-01 lines 147-151 ("The LNR test has a
structural blind spot…"). RESEARCH §TVS-03 line 245 gives the same sentence reworded.

**Section skeleton** (content from RESEARCH §TVS-03):
1. Observability via Jacobian rank — $G=H^\top W H$ nonsingular ⟺ $\mathrm{rank}(H)=n$; show `numpy.linalg.matrix_rank(H)` (RESEARCH lines 379-383); topological vs numerical.
2. Chi-squared detection — "is there bad data?" ($J(\hat x)>\chi^2_{(m-n,0.95)}$).
3. Largest-normalized-residual identification — "which one?" $r_i^N=|r_i|/\sqrt{\Omega_{ii}}$, $\Omega=R-HG^{-1}H^\top$, threshold ≈3.
4. Critical limitation — leverage measurements (AWARENESS but "interview gold", D-08).

**Pitfall to encode (RESEARCH lines 342-345):** χ² detects, rN identifies — state the division of labor explicitly. **Bridge content (SP-4):** "billions of data points across multiple substations" baseline-error analysis = bad-data detection at scale (RESEARCH §TVS-03 line 248) — strongest bridge in the phase.

---

### `notes/TVS-04-asset-health.md` (study-note, worked-example + awareness mix)

**Analog (style):** `notes/KAL-01`/`KAL-02` header + section conventions (SP-1..6).
**Analog (worked-example depth):** `notes/KAL-03-ieee738-ekf-worked-example.md` — the depth bar for a "deep where named" ODE topic. KAL-03 lines 12-53 show the pattern: state the ODE in `$$…$$`, then a **term-by-term table** (`| Term | Name | Expression | Physical Meaning |`, KAL-03 lines 21-28) and a **parameter table** (KAL-03 lines 39-49). Mirror this for the C57.91 top-oil/hot-spot ODEs.

**C57.91 ODE rendering (use SP-3 `\begin{aligned}`/`$$`):** two cascaded first-order rises from RESEARCH §TVS-04 lines 259-268 — top-oil rise, hot-spot rise, $\theta_{HS}=\theta_{ambient}+\Delta\theta_{TO}+\Delta\theta_{HS}$, plus Arrhenius aging $A\exp(B/(\theta_{HS}+273))$, $A=9.8\times10^{-18}$, $B=15000$.

**Section skeleton (single well-sectioned file, D-09):**
1. IEEE C57.91 hot-spot ODE — **FULL/worked depth** (term tables à la KAL-03). Tag exact constants "per IEEE C57.91-2011"; executor does a 5-min confirm pass (RESEARCH Open Question 1, A1).
2. Aging / loss-of-life (Arrhenius) — FULL.
3. "Why this is virtual sensing" — parallel to the IEEE 738 conductor EKF Juan built in Phase 1 (KAL-03), state explicitly (RESEARCH line 271).
4. DGA dissolved-gas analysis — **AWARENESS only** (key-gas list, Duval/Rogers named, no derivation; D-08).
5. Dynamic Line Rating — **AWARENESS**, product framing; reference the Phase-1 `ieee738_ampacity` demo rather than re-deriving IEEE 738 (RESEARCH line 282).
6. Remaining Useful Life — **AWARENESS**, framing only.

**Bridge content (SP-4):** infer an unmeasured physical quantity (winding temp) from proxy telemetry to drive a decision = OSED building thermal estimator (RESEARCH §TVS-04 line 288). **Anti-pattern:** do NOT over-derive DGA/DLR/RUL (D-08; RESEARCH line 138).

---

### `demo/dc_powerflow_baddata_demo.py` (demo-script, linear WLS pipeline)

**Analog:** `demo/ekf_line_temp_demo.py` — reuse its skeleton; swap EKF numerics for linear DC WLS + bad-data. Target ~80 lines (D-01).

**Module docstring + Run/Output header** — `demo/ekf_line_temp_demo.py` lines 1-27:
```python
"""
dc_powerflow_baddata_demo.py
----------------------------
<one-paragraph description: 3-bus DC power-flow WLS angle estimation with
chi-squared + largest-normalized-residual bad-data detection>

Dependencies: numpy, scipy, matplotlib  (from-scratch; no SE library needed)
Run:          python3 dc_powerflow_baddata_demo.py
Output:       dc_powerflow_baddata.png (saved beside this script)
              Console: chi-squared / flagged-measurement / re-solved-angles readout

<constants block: susceptances b12=b13=b23=10, slack=bus1, loads P2=-1.0 P3=-0.5>
"""
```

**Headless-imports + seed block** — `demo/ekf_line_temp_demo.py` lines 29-34 and 210:
```python
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive backend — works without a display
import matplotlib.pyplot as plt
from scipy.stats import chi2
# … inside run_demo():
np.random.seed(42)
```

**Constants block convention** — `demo/ekf_line_temp_demo.py` lines 37-47 (UPPER_CASE module constants with unit comments). Use for the 3-bus susceptances / slack / load injections.

**WLS one-shot solve** (NEW numerics — from RESEARCH Code Examples lines 355-363, the linear collapse of KAL-01's normal equations):
```python
W = np.diag(1.0 / sigma**2)            # W = R^-1
G = H.T @ W @ H                        # gain / information matrix
theta_hat = np.linalg.solve(G, H.T @ W @ z)
r = z - H @ theta_hat                  # residuals
J = r @ W @ r                          # weighted residual cost ~ chi2(m-n)
```

**χ² detection + normalized-residual identification** (RESEARCH lines 366-376; reuses `chi2.ppf` exactly as the Phase-1 `nis_check` did at `ekf_line_temp_demo.py` lines 172-180):
```python
from scipy.stats import chi2
df = m - n
threshold = chi2.ppf(0.95, df)
bad_data = J > threshold                                       # detection
Omega = np.diag(1/np.diag(W)) - H @ np.linalg.inv(G) @ H.T     # R - H G^-1 H^T
rN = np.abs(r) / np.sqrt(np.diag(Omega))                       # normalized residuals
suspect = int(np.argmax(rN))                                   # identification (largest rN > ~3)
```

**Function decomposition** (mirror Phase-1's named-function style — `ieee738_rhs`, `ekf_step`, `nis_check`, `run_demo` at lines 54, 120, 172, 208): suggest `build_B_matrix()`, `build_H()`, `wls_solve()`, `chi2_test()`, `normalized_residuals()`, `run_demo()` (RESEARCH lines 101-103).

**Console banner readout** — `demo/ekf_line_temp_demo.py` lines 263-284 (`print("="*62)` banner; here ~62 wide):
```python
print("=" * 62)
print("  3-Bus DC State Estimation — Bad-Data Detection (χ² + rN)")
print("=" * 62)
# report: df, χ² threshold, J before/after, flagged measurement index + its rN,
#         true vs estimated angles before/after removal
print("=" * 62)
```

**PNG save pattern** — `demo/ekf_line_temp_demo.py` lines 287-327 (multi-panel `plt.subplots`, `script_dir` + `savefig`):
```python
script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir, 'dc_powerflow_baddata.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight')
print(f"Saved {out_path}")
```
Suggested panels (RESEARCH line 319): (a) bar chart of normalized residuals with the 3σ line and flagged bar highlighted; (b) true vs estimated angles before/after bad-data removal.

**Bad-data flow to implement** (RESEARCH Demo spec lines 311-315): solve #1 → χ² flag → rN argmax (= corrupted measurement 5) → remove → solve #2 → angles back near truth, J below threshold.

**Anti-pattern:** keep it linear DC ($h(\theta)=H\theta$) — do NOT use AC power flow (RESEARCH line 137); do NOT add `pandapower`/`PYPOWER` (RESEARCH line 80).

---

### `demo/README.md` (demo-readme)

**Analog:** `demo/README.md` (KAL-04) — mirror its section order exactly.

**Section order to reuse** — `demo/README.md` lines 1-139:
1. `# TVS-…: <title>` + one-paragraph summary (KAL-04 README lines 1-7).
2. `## What It Demonstrates` — numbered list of what the script does (lines 9-31).
3. `## Prerequisites` — numpy/scipy/matplotlib, "all already installed" (lines 34-47).
4. `## How to Run` — `cd … && python3 …` + an **Expected console output** fenced block + expected PNG filename (lines 50-79).
5. `## Interview Talking Points` — `> blockquote` talking points (lines 83-117). Use RESEARCH line 320's "Interview value" line: *"3-bus DC state estimator that detects and removes a corrupted measurement via chi-squared + largest-normalized-residual — the textbook TVS-02+TVS-03 illustration, built from scratch in NumPy."*
6. `## Key Implementation Details` — table (lines 120-129).
7. `## Files` — directory tree (lines 132-139).

---

### `demo/dc_powerflow_baddata.png` (generated-figure)

**Analog:** `demo/ekf_line_temp.png` — generated by running the script (the `script_dir`+`savefig` pattern above). Not authored by hand; produced as the demo's output, committed beside the script exactly as `ekf_line_temp.png` is.

---

## No Analog Found

None. Every Phase 2 file maps to a concrete Phase 1 artifact. The only genuinely NEW *content*
(no Phase-1 equation equivalent) is TVS-01's Thevenin VSI and TVS-04's C57.91 ODE — but both
reuse the Phase-1 *note structure* (SP-1..6) and TVS-04 borrows KAL-03's worked-example layout.

## Metadata

**Analog search scope:** `.planning/phases/01-kalman-state-estimation/notes/` and `/demo/` (the
CONTEXT/RESEARCH-designated templates). No broader codebase search needed — this repo is an
interview-prep document set, not a software project; Phase 1 is the sole and exact analog source.

**Files scanned:** 5 (KAL-01, KAL-02, KAL-03 notes; `ekf_line_temp_demo.py`; demo `README.md`).
**Pattern extraction date:** 2026-06-13
