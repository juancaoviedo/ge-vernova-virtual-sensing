# Phase 5: Federated Architectures & Security - Context

**Gathered:** 2026-06-14
**Status:** Ready for planning

<domain>
## Phase Boundary

Produce study material that closes **Gap 5 (federated)** — the highest-differentiation
*technical* gap — so Juan can, in conversation:

- **FED-01** — Precisely **distinguish federated from distributed** (the "no central
  coordinator" constraint), explain **FedAvg** weight aggregation, articulate why
  **FedProx** proximal regularization is needed when substations have **non-IID** load
  profiles (client drift).
- **FED-02 (a) — Byzantine robustness:** explain **coordinate-wise median / Krum**,
  describe how **gradient poisoning** is detected, name the **gossip-vs-central-aggregation**
  tradeoff.
- **FED-02 (b) — Edge security:** describe **OTA update integrity**, **TPM attestation**,
  and **SPIFFE/SPIRE PKI** for edge identity — each tied to a **concrete grid threat**.

This phase also closes the **STK-05 "fog/federated" tier** that Phase 4 deliberately left
at awareness level (Phase 4 named the concept; Phase 5 owns its depth).

**Out of scope (belongs to other phases):**
- The aggregate **vocabulary-bridge table**, the **OSED pitch**, **STAR stories**, and the
  **timed Q&A / mock-interview** rehearsal loop — all **Phase 6** (BRG-01..03, QNA-01..03).
  Per-note bridge callouts + say-aloud tracks here *feed* Phase 6 without duplicating it.
- **Deep federated-learning math** (FedProx/SCAFFOLD convergence proofs), **SPIRE config /
  TPM internals**, framework-specific Flower/PySyft API depth — awareness only (see CLAUDE.md
  "What NOT to Over-Invest In": "Federated learning math … Flower/FedAvg is enough").
- Re-deriving the Phase 3 patent depth or the Phase 4 STK-05 architecture — **cross-reference,
  don't reproduce**.

This phase produces **3 notes + 1 small Python demo** (the first demo since Phase 2).

</domain>

<decisions>
## Implementation Decisions

### Deliverable shape
- **D-01:** **3 notes (topic-coherent, NOT strictly per-requirement).** FED-02 bundles two
  unrelated clusters, so split it:
  - `notes/FED-01-federated-vs-distributed.md` — federated vs distributed ("no central
    coordinator"), FedAvg aggregation, FedProx proximal term, non-IID / client drift.
  - `notes/FED-02-byzantine-robustness.md` — Krum, coordinate-wise median, gradient-poisoning
    detection, gossip-vs-central aggregation tradeoff.
  - `notes/FED-03-edge-security.md` — OTA update integrity, TPM attestation, SPIFFE/SPIRE PKI,
    each mapped to a concrete grid threat.
  - Note count (3) > requirement count (2) is fine — coherence beats ID-matching. Departs from
    the Phases 1–2 strict per-requirement convention by design.

### Hands-on demo (reintroduced — first since Phase 2)
- **D-02:** **One small self-contained Python/NumPy demo covering all three concepts in a single
  runnable script.** Unlike Phase 4's conversational protocols, FedAvg/FedProx/Krum are
  genuinely numerical/algorithmic (like the Phase 1 EKF and Phase 2 power-flow demos), so a demo
  earns real "I've actually run this" credibility on the differentiator gap.
- **D-03:** **Demo storyline (single script):** a few clients with **non-IID** data → **FedAvg**
  converges (averaging) → **FedProx** proximal term **damps client drift** → inject one
  **poisoned** client and show **Krum / coordinate-wise median rejecting it** while plain FedAvg
  gets corrupted. Print a small **before/after table** of the contrast. This single artifact
  exercises FED-01 (FedAvg/FedProx/non-IID) **and** FED-02a (Byzantine robustness) — FED-03 edge
  security stays notes-only (not demo-able in NumPy).
- **D-04:** **A `demo/` directory returns this phase** (departs from Phase 4's notes-only,
  mirrors Phases 1–2). NumPy-only, from-scratch (no Flower/PySyft dependency) — the point is to
  *show the aggregation math*, not exercise a framework. Include a short README in the
  Phase 1/2 demo style.

### Depth calibration
- **D-05:** **Tiered depth — deep on federated learning, awareness on edge security.**
  - **Explain-WHY depth:** FedAvg/FedProx/non-IID (FED-01) and Byzantine robustness — Krum &
    coordinate-wise median mechanics, poisoning detection, gossip-vs-central (FED-02a). These are
    the parts an interviewer probes.
  - **Awareness depth only:** edge security (FED-03) — one crisp paragraph each on OTA integrity,
    TPM attestation, SPIFFE/SPIRE, **each paired with a concrete grid threat**. The criterion only
    asks to "describe + connect," so **no SPIRE config, no TPM register internals.**

### Grid grounding & AGMS connection
- **D-06:** **Close the STK-05 loop, lightly.** Anchor **non-IID concretely to substation load
  profiles** (the FED-01 criterion's own framing — different feeders/climates/DER mixes →
  non-IID). Add a short callout in the FED notes that **this is the depth behind the STK-05
  "fog/federated" tier**. Add a brief **AGMS tie** (Operation Loop *simulate-before-commit* and
  Scout Command *federated decisioning* as patent analogs of federated/edge-autonomous control).
  **Cross-reference Phase 3/4 — do not re-derive.** Keep the AGMS overlay short.

### Bridge to Juan's work (federated learning is a GENUINE gap)
- **D-07:** **Honest "closest thing I've built + the upgrade I'd make" framing** — do NOT claim
  Juan has run production federated learning. Each "→ Bridge to your work" callout names the real
  adjacent experience and the concrete delta:
  - **OSED edge inference / DER control** = distributed-without-central-coordinator instinct →
    **FedAvg is the federated upgrade** (share weights, never move raw sensor data).
  - **MQTT device fleet / K8s identity** → **SPIFFE/SPIRE** workload identity is the upgrade path.
  - **OTA updates Juan has shipped** → add **signing + TPM-attested integrity** for grid trust.
  - Honest about the gap, but demonstrates he grasps the delta and could implement it. (Rejected
    "claim adjacency" — risky if probed on the differentiator topic.)

### Conventions carried forward (from Phases 1–4 — non-negotiable, not re-discussed)
- **D-08:** **Oral-rehearsal note style.** Each note opens with **For: / Purpose:** header, uses
  numbered sections, and is written for speak-aloud recall, ending with a tight **"<3-min
  say-aloud" talk-track** hitting its criterion's named points (Phase 2 D-06, Phase 4 D-07).
- **D-09:** **Per-note "→ Bridge to your work" callout** (boxed, 1–2 sentences) per D-07 framing
  above (Phase 4 D-08).
- **D-10:** **Markdown + selective LaTeX.** Prose/tables carry most of it; use LaTeX-in-markdown
  only where a formula genuinely helps — e.g. the FedAvg weighted-average update
  $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$, the FedProx proximal term
  $+ \frac{\mu}{2}\lVert w - w_t \rVert^2$, and the Krum score (sum of distances to nearest
  neighbors). Mirror the Phase 1–2 note structure (Phase 4 D-10).
- **D-11 [informational]:** **No aggregate vocabulary-bridge table and no timed-drill / Q&A loop
  here** — Phase 6 (BRG-01..03, QNA-01..03). Scope-exclusion guardrail; plans must NOT create
  those artifacts.

### Claude's Discretion
Exact filenames/slugs within `notes/` and `demo/`; precise section ordering within each note and
whether the "<3-min say-aloud" track sits at top or bottom; the exact non-IID toy dataset and
client count in the demo; how the FedProx $\mu$ and poison magnitude are chosen for a legible
before/after contrast; whether coordinate-wise median, Krum, or both are shown in the demo (at
least one, ideally both named); exactly which concrete grid threats pair with OTA/TPM/SPIFFE;
how richly the AGMS overlay cross-links back to the Phase 3 deck (kept short either way).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

ROADMAP.md declares no explicit "Canonical refs" line for Phase 5. The references below were
accumulated from CLAUDE.md (the primary content base), REQUIREMENTS.md, the `docs/` source
material, and the Phase 1–4 artifacts whose conventions this phase follows.

### Primary content base (lift & refine from THESE first)
- `CLAUDE.md` — **the authoritative content base.** "Category 5: Federated Architectures &
  Federated Learning" (Federated Data Pipelines, Flower/PySyft/FedML/OpenFL table → FED-01/02),
  the "Summary Reference Table" rows for Federated ML (the bridge raw material → D-09), and
  **"What NOT to Over-Invest In"** ("Federated learning math (FedProx, SCAFFOLD) … Flower/FedAvg
  is enough" — the explicit depth ceiling enforcing D-05) and "Recommended Python Libraries to
  Recognize" (flwr — recognize, not build; D-04 is NumPy-only).

### Source material in `docs/`
- `docs/job-requirements.md` — the JD; source of the "federated control frameworks" language and
  the named tools/concepts Juan must speak to. The vocabulary target.
- `docs/Juan Carlos Oviedo Cepeda - 2026.pdf` — Juan's CV; source of the OSED / HEMS / edge / K8s
  / MQTT / OTA experience anchoring every "→ Bridge to your work" callout (D-07). **Federated
  learning is NOT in the CV — this is the gap the honest-bridge framing addresses.**
- `docs/intelligrid.pdf` — IntelliGrid distributed/decentralized grid-control architecture;
  grounding for the substation-federated framing (D-06).
- `docs/mapek.pdf`, `docs/orbit.pdf`, `docs/flisr.pdf` — additional decentralized grid-control
  source material (consult if relevant to the federated/edge-autonomy framing).

### Phase 4 artifacts this phase closes the loop on (D-06)
- `.planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md` — the
  four-tier reference architecture whose **"fog/federated" tier** Phase 5 supplies the depth for.
  The FED notes should explicitly point back here.
- `.planning/phases/04-protocols-stack-architecture/04-CONTEXT.md` — the D-07/D-08/D-10 note-style
  conventions carried forward (renumbered D-08/D-09/D-10 here).

### Phase 3 patent material (for the short AGMS tie — D-06)
- `.planning/research/patents/INDEX.md` — AGMS component map; source for the brief Operation Loop
  (simulate-before-commit) / Scout Command (federated decisioning) federated analogs. **Keep the
  overlay short — reference, don't re-derive.**

### Phase convention references (note + demo style — D-08/D-09/D-10, D-04)
- `.planning/phases/02-transmission-virtual-sensing/notes/TVS-04-asset-health.md` (and siblings)
  — established note style: For:/Purpose: header, numbered sections, "<3-min say-aloud" track,
  boxed "→ Bridge to your work" callout.
- `.planning/phases/02-transmission-virtual-sensing/` demo + README — the small-from-scratch
  Python demo + README pattern D-04 revives (also Phase 1 EKF demo).
- `.planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md` —
  canonical note-style reference.

### Standards / concepts referenced by requirements (cite, don't reproduce)
- **FedAvg** (McMahan et al., 2017) — communication-efficient federated averaging.
- **FedProx** (Li et al., 2020) — proximal term for heterogeneous/non-IID federated optimization.
- **Krum / Multi-Krum** (Blanchard et al., 2017) — Byzantine-robust aggregation.
- **SPIFFE/SPIRE** — workload identity / PKI standard for edge.
- **TPM 2.0 attestation** — hardware root-of-trust for edge integrity.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **CLAUDE.md "Category 5" + Summary Reference Table** — the federated-ML comparison content and
  the "Federated ML → Flower (flwr) → Azure ML centralized → train at edge, share weights, never
  move raw data" bridge one-liner already exist; notes lift and tighten rather than author from
  scratch.
- **Phase 1–2 demo + README scaffold** — the small NumPy from-scratch demo pattern (sim → run →
  print contrast → README) is directly reusable for the FedAvg/FedProx/Krum demo (D-02/D-04).
- **Phase 1–4 `notes/` header style** — For:/Purpose:, numbered sections, say-aloud track, bridge
  callout — established and reused (D-08/D-09).

### Established Patterns
- **`notes/` topic-file split** (Phases 1–2) — followed but loosened: 3 topic-coherent notes, not
  strictly per-requirement (D-01).
- **`demo/` returns** (D-04) — departs from Phase 4 (notes-only), re-aligns with Phases 1–2.
- **Markdown + selective LaTeX** — equations only where they help; the few that do are the FedAvg
  update, the FedProx proximal term, and the Krum score (D-10).

### Integration Points
- Phase 5 notes feed **Phase 6**: per-note "→ Bridge to your work" callouts and "<3-min say-aloud"
  tracks become raw material for the aggregate vocabulary-bridge table (BRG-01..03); the federated
  architecture + demo feed the "500-node virtual sensing pipeline" and federated-aggregator
  system-design drills (QNA). Keep them in a form Phase 6 can lift directly.
- The FED notes **close the STK-05 "fog/federated" tier** (Phase 4) and **tie to AGMS** (Phase 3)
  — keep cross-links so the phases reinforce rather than duplicate.

</code_context>

<specifics>
## Specific Ideas

- **The differentiator one-liners to nail** (highest-yield, most-likely-probed):
  - "**Federated ≠ distributed**: distributed has a coordinator splitting work across workers;
    federated has **no central coordinator owning the data** — each substation trains locally and
    only **weights/gradients leave**, never raw sensor streams."
  - "**FedProx over FedAvg** because substations are **non-IID** — different feeders, climates, DER
    mixes — so naive averaging drifts; the **proximal term** keeps each local update near the
    global model."
  - "**Krum/median** because one **compromised or faulty substation** can poison the global model
    with a malicious gradient; robust aggregation **rejects the outlier** instead of averaging it
    in."
- **Edge-security-to-grid-threat pairings** (FED-03 — name + connect, awareness depth):
  OTA integrity → *prevents a malicious firmware push bricking/weaponizing a substation fleet*;
  TPM attestation → *proves a relay is running unmodified trusted code before it joins control*;
  SPIFFE/SPIRE → *cryptographic workload identity so a spoofed node can't impersonate a real IED*.
- **Bridge callouts read as honest interview pivots**, e.g. "In OSED I ran distributed edge
  inference across DER nodes — no cloud round-trip for local decisions. I haven't run federated
  *learning* in production, but that's the natural next step: keep the local inference, add FedAvg
  so the fleet improves a shared model without ever shipping raw telemetry — and Krum so one bad
  node can't poison it."
- **Demo punchline to rehearse:** "Watch plain FedAvg get dragged off by the poisoned client while
  Krum just drops it — that's Byzantine robustness in ~10 lines."

</specifics>

<deferred>
## Deferred Ideas

- **Aggregate vocabulary-bridge table** (federated/security terms → Juan's-tool analog → pivot
  sentence) — **Phase 6** (BRG-01..03). Per-note callouts here feed it.
- **System-design drills** (e.g. "500-node virtual sensing pipeline" with a federated aggregator)
  and **timed Q&A / mock-interview rehearsal** — **Phase 6** (QNA-01..03). This phase's demo +
  federated framing are the canvas those drills draw on.
- **Framework-level FL depth** (Flower/PySyft API, SCAFFOLD/FedNova, secure aggregation / HE/SMPC
  math, full SPIRE config, TPM register internals) — explicitly **declined** for this phase per the
  D-05 depth ceiling and CLAUDE.md "What NOT to Over-Invest In." Awareness only.
- **A demo using a real FL framework (Flower)** — considered and declined; D-04 keeps it NumPy
  from-scratch to show the aggregation math, not exercise a dependency. Could be optional Phase 6
  reinforcement if time allows, but not planned.

None beyond the above — discussion stayed within phase scope.

</deferred>

---

*Phase: 5-Federated Architectures & Security*
*Context gathered: 2026-06-14*
