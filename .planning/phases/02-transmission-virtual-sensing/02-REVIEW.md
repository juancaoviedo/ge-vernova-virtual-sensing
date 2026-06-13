---
phase: 02-transmission-virtual-sensing
reviewed: 2026-06-13T00:00:00Z
depth: standard
files_reviewed: 6
files_reviewed_list:
  - .planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py
  - .planning/phases/02-transmission-virtual-sensing/demo/README.md
  - .planning/phases/02-transmission-virtual-sensing/notes/TVS-01-voltage-stability.md
  - .planning/phases/02-transmission-virtual-sensing/notes/TVS-02-dc-powerflow-angle-wls.md
  - .planning/phases/02-transmission-virtual-sensing/notes/TVS-03-observability-bad-data.md
  - .planning/phases/02-transmission-virtual-sensing/notes/TVS-04-asset-health.md
findings:
  critical: 0
  warning: 3
  info: 3
  total: 6
status: issues_found
---

# Phase 2: Code Review Report

**Reviewed:** 2026-06-13
**Depth:** standard
**Files Reviewed:** 6
**Status:** issues_found

## Summary

Reviewed one ~80-line NumPy/SciPy demo (`dc_powerflow_baddata_demo.py`) and five
equation-dense study documents (one README, four TVS notes) for an interview-prep
study phase.

The demo's linear algebra is **correct**. I hand-traced every row of the `H`
measurement matrix and the reduced `B` matrix against the DC power-flow definitions
and they are self-consistent and right:

- Injection @2: `(b12+b23)θ2 − b23·θ3 = 20θ2 − 10θ3` → `[20, −10]` ✓
- Injection @3: `−b23·θ2 + (b13+b23)θ3 = −10θ2 + 20θ3` → `[−10, 20]` ✓
- Flow 1→2: `b12(θ1−θ2) = −10θ2` → `[−10, 0]` ✓
- Flow 1→3: `b13(θ1−θ3) = −10θ3` → `[0, −10]` ✓
- Flow 2→3: `b23(θ2−θ3) = 10θ2 − 10θ3` → `[10, −10]` ✓

The WLS normal-equations solve, the chi-squared degrees of freedom (`df = m−n = 3`
pre-removal, `2` post-removal), the residual-covariance form `Ω = R − H G⁻¹ Hᵀ`, and
the normalized-residual `|r|/√Ω_ii` are all textbook-correct (Abur & Expósito). The
script runs cleanly and reproduces the README's documented console output exactly,
including the seeded numbers (`J = 176.711`, `rN = 13.23`, recovery to within `7e-4`
rad). The four study notes' stated equations were given a light correctness pass and
are sound.

No correctness bugs, no security issues. The findings below are **runtime-robustness
hardening** on the demo (the suspect-removal and normalized-residual paths have a few
silent-failure edges that the fixed seed happens to dodge) plus minor clarity items.
None block this study artifact from serving its purpose.

## Warnings

### WR-01: Suspect removal can leave the re-solve unobservable, with no guard

**File:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py:134-136`
**Issue:** After picking `suspect = argmax(rN)`, the code drops that row and re-solves
without re-checking that `H2` still has full column rank. The pre-removal assert
(`matrix_rank(H) == n`, line 116) only validates the *original* `H`. For the shipped
seed and the deliberately-corrupted flow-2→3 row this is fine (4 rows, rank 2), but the
code path is one bad `argmax` away from feeding a rank-deficient `H2` into
`np.linalg.solve(G2, ...)` (line 80), which raises `LinAlgError` or returns garbage. A
demo whose entire point is "observability via rank" should re-assert observability after
removal.
**Fix:**
```python
keep = [i for i in range(m) if i != suspect]
H2, z2, W2 = H[keep], z[keep], np.diag(np.diagonal(W)[keep])
assert np.linalg.matrix_rank(H2) == n, \
    "Removing the suspect made the system unobservable — cannot re-solve"
theta2, r2, J2, _ = wls_solve(H2, W2, z2)
```

### WR-02: `np.sqrt(np.diag(Omega))` can produce NaN with no guard

**File:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py:97-98`
**Issue:** `Omega_ii` is the residual variance and is non-negative *in exact arithmetic*,
but for a leverage measurement it is structurally near-zero and floating-point round-off
can push it slightly negative. `np.sqrt` of a negative then yields `nan`, and
`argmax(rN)` silently returns an arbitrary index — the identification step fails without
an error. This is precisely the "leverage measurement" blind spot the companion note
TVS-03 §4 describes, so it is worth handling defensively even in a demo. It does not
trigger on the shipped seed (no leverage measurement is corrupted), but it is latent.
**Fix:**
```python
Omega = np.diag(1.0 / np.diag(W)) - H @ np.linalg.inv(G) @ H.T
omega_diag = np.clip(np.diag(Omega), 1e-12, None)   # guard leverage/round-off
rN = np.abs(r) / np.sqrt(omega_diag)
```

### WR-03: `chi2_test` `confidence` parameter is dead — both call sites use the default

**File:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py:86-89, 127, 138`
**Issue:** `chi2_test(J, df, confidence=0.95)` exposes a `confidence` knob, but both
callers (lines 127 and 138) rely on the default and the console labels hard-code
`"95%"` (lines 149, 158). If a reader changes the default to demonstrate a different
confidence level, the printed labels will silently lie ("95%" while testing at, say,
90%). For a teaching demo where the threshold *is* the lesson, the printed confidence
should track the value actually used rather than being a separate string literal.
**Fix:** Either drop the unused parameter, or derive the label from it, e.g. pass a
`CONFIDENCE = 0.95` module constant into both `chi2_test(...)` and the f-strings:
```python
print(f"  chi2 threshold ({CONFIDENCE:.0%}, df={df1}) : {thr1:.3f}")
```

## Info

### IN-01: Residual covariance recomputes `G⁻¹` via explicit `inv` instead of reusing the solve

**File:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py:97`
**Issue:** `normalized_residuals` calls `np.linalg.inv(G)` to form `Ω = R − H G⁻¹ Hᵀ`.
Forming an explicit inverse is the numerically less-preferred route; the textbook /
production idiom is to solve `G X = Hᵀ` and use `H @ X`. For a 2×2 `G` this is harmless,
but a study demo positioned as "the production machinery" would be more exemplary using
the solve form.
**Fix:**
```python
HGinvHt = H @ np.linalg.solve(G, H.T)
Omega = np.diag(1.0 / np.diag(W)) - HGinvHt
```

### IN-02: `r2` is unpacked but never used

**File:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py:136`
**Issue:** `theta2, r2, J2, _ = wls_solve(...)` binds `r2`, which is never referenced
again (only `theta2` and `J2` are used downstream). Minor dead binding; prefer `_` for
consistency with the discarded gain matrix on the same line.
**Fix:** `theta2, _, J2, _ = wls_solve(H2, W2, z2)`

### IN-03: "others < {...}" label assumes the second-largest rN is below the suspect

**File:** `.planning/phases/02-transmission-virtual-sensing/demo/dc_powerflow_baddata_demo.py:152-153`
**Issue:** The console prints `rN = {suspect}  (others < {np.partition(rN, -2)[-2]})`.
`np.partition(rN, -2)[-2]` is the second-largest value, which is correct *only* when the
suspect is the single largest (true here). It is a reasonable shorthand, but the phrasing
"others <" is slightly loose: the printed bound is itself one of the "others," so it is an
inclusive upper bound, not a strict one. Harmless for the demo; noting for precision since
the numbers are the teaching content.
**Fix (optional):** Reword to `(2nd-largest rN = {...})` to state exactly what the number is.

---

_Reviewed: 2026-06-13_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
