# Phase 8: IEEE 33-Bus DER Measurement Source — Pattern Map

**Mapped:** 2026-06-22
**Files analyzed:** 11 (new files this phase creates)
**Analogs found:** 2 / 11 (all from `docs/build_site.py` and `docs/demos/*.py`; the
rest are greenfield — no pandapower, Docker, InfluxDB, Grafana, or uv code exists
anywhere in the repo)

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|---|---|---|---|---|
| `system1-measurement-source/pyproject.toml` | config | — | none | greenfield |
| `system1-measurement-source/Makefile` | config | — | none | greenfield |
| `system1-measurement-source/.env.example` | config | — | none | greenfield |
| `system1-measurement-source/docker-compose.yml` | config | — | none | greenfield |
| `system1-measurement-source/src/ieee33/config.py` | config | — | none | greenfield |
| `system1-measurement-source/src/ieee33/network.py` | utility | transform | `docs/demos/dc_powerflow_baddata_demo.py` | partial-match (same "constants + pure function" layout; different domain) |
| `system1-measurement-source/src/ieee33/ingest.py` | utility | file-I/O + request-response | `docs/build_site.py` | partial-match ("one command + validation gate + halt-loud-on-failure" ethos) |
| `system1-measurement-source/src/ieee33/sim.py` | utility | batch + CRUD | `docs/demos/dc_powerflow_baddata_demo.py` | partial-match ("run_demo() → numeric loop → artifact output" structure) |
| `system1-measurement-source/src/ieee33/validate.py` | utility | transform | `docs/build_site.py` (validate_links) | partial-match ("assert correctness, fail loud") |
| `system1-measurement-source/grafana/provisioning/**` | config | — | none | greenfield |
| `system1-measurement-source/README.md` | config | — | none | greenfield |

---

## Pattern Assignments

### `src/ieee33/network.py` (utility, transform)

**Closest analog:** `docs/demos/dc_powerflow_baddata_demo.py`

**Why it matches:** `network.py` is a module of pure functions (no side effects, no I/O)
that build and return a data structure — exactly how `dc_powerflow_baddata_demo.py` builds
its B-matrix and H-matrix constants via module-level constants + plain functions.

**Imports pattern** (`dc_powerflow_baddata_demo.py` lines 27–32):
```python
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import chi2
```
For `network.py`, mirror the stdlib-first, then third-party order:
```python
import pandapower as pp
import pandapower.networks as pn
import pandapower.control as ctrl
```

**Constants-block pattern** (`dc_powerflow_baddata_demo.py` lines 37–43):
```python
B12 = 10.0    # p.u.   susceptance of line 1-2  (x = 0.1 p.u.)
B13 = 10.0    # p.u.
B23 = 10.0    # p.u.
P2 = -1.0     # p.u.   true power injection (load) at bus 2
P3 = -0.5     # p.u.
SIGMA = 0.01  # p.u.   measurement noise standard deviation
SLACK_BUS = 1 # reference bus, theta_1 = 0
```
For `network.py`, put all bus-index mapping, nameplate, and physical constants in a
module-level block with inline units comments before any function.

**Pure-function pattern** (`dc_powerflow_baddata_demo.py` lines 46–53 `build_B_matrix`):
```python
def build_B_matrix():
    """Reduced bus susceptance matrix (slack row/col deleted) -> [[20,-10],[-10,20]].

    Full DC B-bus is the susceptance Laplacian; deleting the slack (bus 1)
    row and column leaves the reduced 2x2 system B_red @ [theta_2, theta_3] = [P2, P3].
    """
    B_red = np.array([[B12 + B23, -B23],
                      [-B23,       B13 + B23]])
    return B_red
```
`build_enhanced_33bus()` follows the same shape: one public function with a docstring
explaining what it builds and returns; inline assertion comments for landmines (tie-line
`in_service`, bus index offset).

**No `if __name__ == "__main__"` block** — `network.py` is a library module imported by
`ingest.py`, `sim.py`, and `validate.py`. Do not add a standalone runner here.

---

### `src/ieee33/ingest.py` (utility, file-I/O + request-response)

**Closest analog:** `docs/build_site.py` — for the "single entry-point, halt-loud-on-failure,
validation gate" pattern.

**Entry-point + fail-loud pattern** (`docs/build_site.py` lines 1016–1076):
```python
def main() -> None:
    NOTES_OUT.mkdir(parents=True, exist_ok=True)

    note_paths = discover_notes()
    if not note_paths:
        raise RuntimeError("could not convert: no note files found — check REPO_ROOT")
    # ... body ...

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
```
`ingest.py`'s `main()` mirrors this: check InfluxDB reachability, check OPSD endpoint
reachability, fetch data, write, assert 96 rows written — halt with `sys.exit(1)` on
any failure. No synthetic fallback; the halt IS the fallback (SPEC req 3).

**Validation gate pattern** (`docs/build_site.py` lines 945–1009 `validate_links`):
```python
def validate_links() -> None:
    """..."""
    broken: list[str] = []
    noindex_missing: list[str] = []

    for page in all_pages:
        # ... accumulate issues ...

    issues = noindex_missing + broken
    if issues:
        print("\n--- LINK VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        sys.exit(1)

    print(f"  validate_links: OK — {len(all_pages)} pages, 0 broken links, ...")
```
Mirror this "accumulate issues → fail loud with detail → print OK on success" shape for
post-ingest assertion: assert exactly 96 profile points in bucket, print count on success.

**Module docstring + `Run:` convention** (`dc_powerflow_baddata_demo.py` lines 1–24):
```python
"""
dc_powerflow_baddata_demo.py
----------------------------
From-scratch 3-bus DC power-flow weighted-least-squares (WLS) state estimator
...

Dependencies: numpy, scipy, matplotlib
Run:          python3 dc_powerflow_baddata_demo.py
Output:       dc_powerflow_baddata.png
"""
```
`ingest.py` should open with the same style: one-paragraph description, `Dependencies:`,
`Run:` (via `uv run ingest`), `Effect:` (writes 96 profile rows to InfluxDB).

---

### `src/ieee33/sim.py` (utility, batch + CRUD)

**Closest analog:** `docs/demos/dc_powerflow_baddata_demo.py` — for the "numeric loop with
constants → loop → output artifact" structure. Also draws from `docs/build_site.py` for the
re-runnable, deterministic, one-command ethos.

**`run_demo()` loop structure** (`dc_powerflow_baddata_demo.py` lines 102–169):
```python
def run_demo():
    """Solve the 3-bus DC WLS, inject + detect + remove a gross error, plot and save PNG."""
    np.random.seed(42)

    # ---- Ground truth: solve reduced DC power flow B_red @ theta = P ----
    B_red = build_B_matrix()
    theta_true = np.linalg.solve(B_red, np.array([P2, P3]))

    # ---- Build measurements ----
    H = build_H()
    # ... loop over steps ...
    # ---- Console readout ----
    print("=" * 62)
    print("  3-Bus DC State Estimation — Bad-Data Detection")
    print("=" * 62)
```
`sim.py`'s `main()` follows the same shape:
1. Build `net, trafo_idx = build_enhanced_33bus()` (analogous to `build_B_matrix()`)
2. Query 96-row profiles DataFrame from InfluxDB (analogous to `build_H()` / setup)
3. Loop over 96 steps with section-header comments
4. Console readout per step + final summary (step count, Vmin, Vmax, total losses)

**Determinism pattern** (`dc_powerflow_baddata_demo.py` line 104 and `ekf_line_temp_demo.py`
line 213):
```python
np.random.seed(42)
```
`sim.py` has no stochastic elements (D-16), but the determinism guarantee is documented
in the module docstring: "Fixed day + fixed profiles + deterministic Newton-Raphson →
identical 96 snapshots on every run."

**Output artifact convention** (`dc_powerflow_baddata_demo.py` lines 205–209):
```python
script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir, 'dc_powerflow_baddata.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight')
print(f"Saved {out_path}")
```
`sim.py`'s "output artifact" is the 96 snapshots in InfluxDB. Print confirmation of each
write batch and a final "96 snapshots written to bucket 'state'" line — same convention of
confirming the output at the end.

---

### `src/ieee33/validate.py` (utility, transform)

**Closest analog:** `docs/build_site.py` `validate_links()` function — for the "assert
correctness, accumulate failures, fail loud with detail, print OK on success" pattern.

**Fail-loud pattern** (`docs/build_site.py` lines 999–1009):
```python
    issues = noindex_missing + broken
    if issues:
        print("\n--- LINK VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        print(f"\n  {len(broken)} broken link(s), ...", file=sys.stderr)
        sys.exit(1)

    print(f"  validate_links: OK — {len(all_pages)} pages, 0 broken links, ...")
```
`validate.py` runs `case33bw()` → `pp.runpp()` → asserts `vm_min ≈ 0.913 pu` within
tolerance. On failure: print the actual value and the expected range, `sys.exit(1)`.
On success: print "Base case OK: vm_min=0.9130 pu at pp_bus=17".

**Entry-point pattern** (same `if __name__ == "__main__"` wrapper as `build_site.py`
lines 1072–1076 and both demo scripts): wrap `main()` in try/except, print FATAL to
stderr, `sys.exit(1)`.

---

### `src/ieee33/config.py` (config)

**Closest analog:** Module-level constants blocks in `dc_powerflow_baddata_demo.py`
(lines 37–43) and `ekf_line_temp_demo.py` (lines 40–48).

**Constants-block pattern** (`ekf_line_temp_demo.py` lines 40–48):
```python
MCP = 534.0        # J/(m·°C)  heat capacity per unit length
R25 = 7.28e-5      # Ω/m       DC resistance at 25°C
ALPHA_R = 0.00403  # /°C       temperature coefficient of resistance
D = 0.0281         # m         conductor outer diameter
EPS = 0.5          # —         emissivity
```
`config.py` is a pure-constants file (no functions, no I/O): OPSD_URL, TARGET_DATE,
DG_NAMEPLATE_MW, DG_SCALE_FACTOR, BUS mapping dict, INFLUXDB_URL / INFLUXDB_TOKEN /
INFLUXDB_ORG loaded from `python-dotenv`. Inline units comments on every constant.

---

### `pyproject.toml` (config, greenfield)

**Greenfield — no in-repo analog.** No `pyproject.toml` or `uv.lock` exists anywhere in
the repo. The repo previously used a `.build-venv/` directory (gitignored); this phase
replaces that convention with `uv`. Use RESEARCH.md Pattern 7 (lines 536–567) as the
external pattern. Key structure: `[project]`, `[project.scripts]` with three entry points
(`ingest`, `sim`, `validate`), `requires-python = ">=3.12"`, pinned `dependencies`.

---

### `Makefile` (config, greenfield)

**Greenfield — no Makefile anywhere in the repo.** Use RESEARCH.md Pattern 7 (lines
543–567) as the external pattern. Targets: `up`, `ingest`, `sim`, `validate`, `all`,
`down`, `clean`. The `ingest` and `sim` targets depend on `up` (infra must be running).

---

### `docker-compose.yml` (config, greenfield)

**Greenfield — no Docker Compose file anywhere in the repo.** Use RESEARCH.md Pattern 5
(lines 454–489) as the external pattern. Two services: `influxdb:2.9.1` and
`grafana/grafana:11.6.15`. Key landmine: `DOCKER_INFLUXDB_INIT_BUCKET` creates only the
`profiles` bucket; `state` bucket is created programmatically.

---

### `grafana/provisioning/**` (config, greenfield)

**Greenfield — no Grafana provisioning YAML anywhere in the repo.** Use RESEARCH.md
Pattern 6 (lines 496–531) as the external pattern. Three files:
`datasources/influxdb.yml`, `dashboards/default.yml`, `dashboards/ieee33-state.json`.
Key landmine: hard-code `ieee33-dev-token` literal in `secureJsonData.token` — do not
use `${VAR}` substitution (known Grafana issue #89519).

---

### `.env.example` (config, greenfield)

**Greenfield.** No `.env` pattern exists in the repo. Standard pattern: list
`INFLUXDB_URL`, `INFLUXDB_TOKEN`, `INFLUXDB_ORG` with placeholder values; never commit
the actual `.env` (gitignore it).

---

### `README.md` (greenfield)

**Greenfield — no runbook-style README exists in the repo.** The closest spirit is the
`docs/build_site.py` docstring at lines 1–14 (which describes usage with `Run:` and
scope per plan). The README is the human-readable version of that pattern, expanded to
the full "rhythm": `uv sync` → `docker compose up` → `uv run ingest` → `uv run sim`
→ open Grafana at http://localhost:3000 → open InfluxDB at http://localhost:8086.

---

## Shared Patterns

### Module docstring convention
**Source:** `docs/demos/dc_powerflow_baddata_demo.py` lines 1–24;
`docs/demos/ekf_line_temp_demo.py` lines 1–27

**Apply to:** All `.py` files in `src/ieee33/`

Pattern: opening docstring names the file, draws a separator line, gives a one-paragraph
description, then `Dependencies:`, `Run:` (command to execute), `Output:` or `Effect:`.

```python
"""
<filename>
----------
<one-paragraph description of what the module does and why>

Dependencies: pandapower, influxdb-client, pandas, numpy, python-dotenv
Run:          uv run <entrypoint>
Effect:       <what it writes / asserts / returns>
"""
```

### Fail-loud error handling
**Source:** `docs/build_site.py` lines 1072–1076 (outer try/except) and
`validate_links()` lines 999–1009 (inner issue accumulation)

**Apply to:** `ingest.py`, `sim.py`, `validate.py`

```python
if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
```
Never swallow exceptions silently. Print the full error to stderr. Exit non-zero so Make
targets propagate failure.

### Constants with inline unit comments
**Source:** `docs/demos/ekf_line_temp_demo.py` lines 40–48;
`docs/demos/dc_powerflow_baddata_demo.py` lines 37–43

**Apply to:** `config.py`, `network.py`, `validate.py`

Every physical constant gets a comment with value, unit, and source reference in the
same column-aligned block. No "magic numbers" buried in functions.

### Section-header comments in long functions
**Source:** `docs/demos/dc_powerflow_baddata_demo.py` `run_demo()` lines 109–168

```python
    # ---- Ground truth: solve reduced DC power flow ----
    # ---- Build measurements ----
    # ---- WLS solve #1 (with bad data) ----
    # ---- Identify the suspect ----
    # ---- Remove and re-solve ----
    # ---- Console readout ----
```
**Apply to:** `sim.py` `main()` loop body. Each logical phase of the 96-step loop gets a
`# ---- <phase name> ----` separator comment.

### Non-interactive matplotlib backend
**Source:** `docs/demos/dc_powerflow_baddata_demo.py` lines 29–30;
`docs/demos/ekf_line_temp_demo.py` lines 32–33

```python
import matplotlib
matplotlib.use('Agg')   # non-interactive backend — works without a display
```
**Apply to:** Not applicable to System 1 (`network.py`, `sim.py`, etc. do not generate
plots). Note for future phases that add visualization scripts.

---

## No Analog Found

Files with no close match in the codebase. Planner MUST use RESEARCH.md sections instead:

| File | Role | Data Flow | RESEARCH.md Section to Use |
|---|---|---|---|
| `pyproject.toml` | config | — | Pattern 7 (lines 536–542) |
| `Makefile` | config | — | Pattern 7 (lines 543–567) |
| `docker-compose.yml` | config | — | Pattern 5 (lines 454–489) |
| `grafana/provisioning/datasources/influxdb.yml` | config | — | Pattern 6 (lines 497–515) |
| `grafana/provisioning/dashboards/default.yml` | config | — | Pattern 6 (lines 519–531) |
| `grafana/provisioning/dashboards/ieee33-state.json` | config | — | RESEARCH.md §Architecture + D-13 panel list |
| `.env.example` | config | — | RESEARCH.md §Standard Stack + D-06/D-07/D-10 |
| `src/ieee33/__init__.py` | config | — | Empty or minimal package marker; no analog needed |
| Whole pandapower network-builder pattern | — | — | RESEARCH.md Patterns 1–2 (lines 218–332) |
| InfluxDB write/query pattern | — | CRUD | RESEARCH.md Patterns 3–4 (lines 338–449) |
| OPSD chunked CSV ingestion | — | file-I/O | RESEARCH.md Pattern 3 (lines 348–391) |

---

## Greenfield Rationale

This is the first code-build phase in a study-notes repository. The repo contains:
- `docs/build_site.py` — a 1,077-line HTML build script (no power-systems code)
- `docs/demos/*.py` — three self-contained NumPy teaching demos (no pandapower, no DB)
- No Docker, no Compose, no pyproject.toml, no Makefile, no InfluxDB client code

The two genuine analogs extracted above (build_site.py's "fail-loud entry-point" ethos
and the demo scripts' "constants → functions → `run_demo()` → output" structure) are
style guides, not API guides. All pandapower, InfluxDB, Docker Compose, and Grafana
patterns come from the external sources documented in RESEARCH.md.

---

## Metadata

**Analog search scope:** `docs/`, `patents-site/`, repo root (`/home/juan/codes/ge-vernova-virtual-sensing`)
**Files scanned:** 6 Python files, 0 TOML/YAML/Makefile (none found outside `.planning/`)
**Pattern extraction date:** 2026-06-22
