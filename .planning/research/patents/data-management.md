# Patent: Data Management for Adaptive Power Grid Management

## Bibliographic Data

| Field | Value |
|-------|-------|
| Title | Data Management for Adaptive Power Grid Management |
| Publication Number | WO 2024/211800 A1 |
| PCT Application | PCT/US2024/023395, filed 2024-04-05 |
| US Priority Application | 18/131,790, filed 2023-04-06 |
| Publication Date | 2024-10-10 |
| Inventor | SHARIF-ASKARY, Jamshid |
| Assignee | GE Infrastructure Technology LLC, 300 Garlington Road, Greenville, SC 29615 |
| IPC Classes | G05B 15/02, G06F 9/50, G05F 1/66, G05B 13/00, G06F 1/3203 |
| Pages | 111 (image-only PDF; also available as `patent_ocr.pdf` with full OCR text layer) |
| Family Relationship | Continuation of US 18/131,790; continuation-in-part of AGMS parent (WO 2023/064623) |
| ISR Cited Prior Art | US 2013/0085614 A1 (Wenzel) — cited as X (category: claimed invention cannot be considered novel when taken alone) against all claims 1–16 |

---

## Problem Addressed

The AGMS architecture (parent patent) involves numerous concurrent modules — GWM alert correlation, GA artificer, grid-wide foresight manager, grid scouts command, operating cells, federated transaction manager — all of which need access to asset data, contextual data, and operational state. A naive shared-database approach creates contention, role-inappropriate data exposure, and coupling between modules that must operate independently (including during WAN outages). The patent addresses this by introducing a **data management module** that serves each requesting module a customized "point of view" (POV) file: a role-filtered, context-appropriate slice of the aggregated asset data, assembled on demand using a patterns database that encodes what each module role should see. This decouples the data plane from each module's logic and ensures that no module receives data outside its operational context — a form of attribute-based access control expressed as view patterns.

---

## Core Technical Method

### Central Abstraction: Point of View (POV) Files

A POV file is not a raw data dump. It is a **structured, role-filtered view** of grid asset data assembled by the data management module specifically for the requesting module's role and operational context. The patterns database stores view patterns — essentially schema templates that specify which data fields, at what granularity, with what relevancy ranking, to include for a given module role. The data management module acts as the sole interface to the underlying asset database; no other module queries the asset DB directly.

### Data Management Module Workflow (Fig. 24 / claim method)

1. **Aggregate device data**: Communicates with devices on the network to aggregate device data into the asset database. In the AGMS architecture, this means collecting telemetry from all field agent devices (FADs) across operating cells — sensor readings, device status, operational indexes, alert flags, DNA map updates.

2. **Receive a PoV file request**: One of the AGMS modules (e.g., Grid Wide Formation Manager, GridwideEye, CSM Operator, ORACS correlation engine) sends a POV file request to the data management module specifying its role/context identifier.

3. **Retrieve asset data**: Queries the asset database based on the PoV file request parameters — the requesting module's role, the formation ID, the ORACS context.

4. **Select a view pattern**: Looks up the patterns database to retrieve the appropriate view pattern for the requesting module's role. The Learning Engine assists in selecting the most relevant pattern (Fig. 19/32 — Learning Engine retrieving the most relevant pattern associated with the PoVf.id).

5. **Form the PoV file**: Applies the view pattern to the retrieved asset data, composing the role-appropriate view. The `gWE contents composer` composes relevant point of view per PoVf.id. The `gPoView Meta-Object Builder` assembles the final PoV object.

6. **Send the PoV file**: Returns the PoV file to the requesting module. The requesting module never touches the raw asset database.

### View Pattern Types (from OCR text and Figs. 19, 31–32)

Three specialized construct modules produce different PoV types:

- **viewConstructModule** (ref 1115A): Parses PoVf.id contents and patterns; retrieves ORACS(id), lf(cT); creates observability and situational awareness with extended line of sight; constructs a condition-based point of view for ORACS(id) in relation to lf(cT). This is the "eyes on the field" view for operational monitoring.

- **controlConstructModule** (ref 1116A): Parses PoVf.id contents and patterns; retrieves ORACS(id), action list within ORACS(id), action function (aft); constructs action list within ORACS(id).aft, construct controlPoVf.id (oracs.id, aft). This is the actuation/control command view.

- **adminConstructModule** (ref 1117A): Parses PoVf.id contents; identifies participating apps within PoVf; creates contextual collaboration links among apps (collab.l(id)(Apps_{1,n})). This is the inter-application coordination view.

### Contextual Abstraction Panels and Relevancy Indexing (from OCR text)

The OCR-extracted text confirms that the contextual abstraction panels (CAPs) within this data management context use a three-tier relevancy index system: **high, medium, low** relevancy. The `gWE meta-object Historical Archive` and `UI/UX Patterns archive` back the learning engine's pattern selection. The `gw asset portfolio DB (gwapd)` provides the asset attribute data layer.

### Security: ga-authenticationkey in Data Flow (Fig. 19)

`gridwideEye` authenticates via ga-authenticationkey before any PoV frame is released. The `gWE-gatekeeper` checks the token; on failure, the request is rejected and no data is released. On success, the `gridwideEye PoV builder` assembles and returns the frame. The `gridwideEye Agent` then extracts the frame ID and contents associated with the PoVf.id.

### Relationship to Asset Portfolio Patent (WO 2024/211758)

The data-management and asset-portfolio patents are siblings filed on the same date (PCT filed 2024-04-05) from the same priority application base (both from 2023-04-06). They share nearly identical diagrams for Figs. 15–19 and 20–23 — the ORACS formation workflow, scout launch, and GridwideEye PoV flow are common to both. The primary distinction is:
- Asset Portfolio patent: focuses on the **selection and verification** of assets (who gets into the formation plan, and are they operationally fit).
- Data Management patent: focuses on **what data each participant sees** during and after formation (the POV file serving layer).

Together they implement a complete "plan → verify → execute → observe" loop for AGMS formations.

### ORACS Data Flow in Context (Figs. 15–18 are shared with asset-portfolio)

The same ORACS operation loop formation construct, ORACS resource interdependency analyzer, ORACS DNA analyzer, inter-oracs operation formation, scouts command, and scouts launch manager appear identically in both patents. In the data management patent, the emphasis is on how each of these modules receives its contextual data via PoV files rather than raw database queries.

---

## Key Independent Claims (Paraphrased)

**Primary system claim:** A power grid management system comprising a data management module that: (a) communicates with devices on the network to aggregate device data in the asset database; (b) receives a point of view (POV) file request from one of the modules in the power grid management system; (c) retrieves asset data from the asset database based on the POV file request; (d) selects a view pattern from a patterns database based on the POV file request; (e) forms a POV file based on the asset data and the view pattern; and (f) sends the POV file to the module.

**Secondary claims (from OCR):** Also claim the formation loop method (Fig. 20), the asset verification method with operational indexes (Fig. 21), the historical meta-object matching method (Fig. 22), and the scout command method (Fig. 23) — same as in the asset-portfolio patent, reflecting the shared architecture.

---

## Key Technical Details from OCR (patent_ocr.pdf)

The OCR text layer (extracted from `patent_ocr.pdf`) yields the following additional specifics not easily readable from the image PDF:

- **gAVA (grid artificer virtual agent)**: standardizes communication messaging formats between modules. The gAVA is the inter-module message broker that enforces schema consistency — every module speaks to every other via gAVA-formatted messages.
- **Contextual abstraction panels with high/medium/low relevancy indexing**: CAPs are ranked by the Learning Engine's probability output; the CSM Builder selects the highest-relevancy CAP and the Simulation Engine validates the resulting state machine.
- **CSM builder validation via simulation engine before production promotion**: The patent explicitly states that draft CSM entries are validated via the simulation engine before being promoted to production status. This is the "provisional → calibrated → production" three-stage pipeline.
- **ga-authenticationkey security token system**: every inter-module communication passes a ga-authenticationkey; the GateKeeper component validates it before processing. This is analogous to OAuth2 bearer tokens but is architecturally embedded in the module orchestration protocol.

---

## Connection to Juan's Work

| Patent Concept | Juan's Analogous Work | Bridge Narrative |
|---|---|---|
| POV file: role-filtered view of asset data assembled on demand from a patterns DB | Grafana dashboards in OSED: each stakeholder role (grid operator, building manager, engineer) sees a different Grafana dashboard over the same InfluxDB/TimescaleDB data | Juan's OSED multi-dashboard architecture is a direct analog — same backend data, role-appropriate views |
| Patterns database: schema templates specifying what each module role should see | SI-MAPPER: ASHRAE 223P ontology defines what data properties are relevant for each equipment class and system relationship | The SI-MAPPER ontology is a semantic "patterns database" — it encodes which data fields are meaningful for a given system type |
| Data management module as the sole interface to the asset DB — no direct DB access by other modules | FastAPI service layer in OSED: all sensor data access goes through a FastAPI service; edge nodes never query InfluxDB directly | Juan's API-mediated data access pattern is architecturally identical to the data management module's role |
| ga-authenticationkey + GateKeeper: authenticated inter-module messaging | gRPC with service-to-service auth tokens in OSED; MCP server tool-call authentication in SI-MAPPER | Juan has implemented authenticated structured messaging at both the gRPC (OSED) and MCP (SI-MAPPER) layers |
| gAVA: standardized message format enforced across all modules | MQTT topic schema + payload schema in OSED: standardized message structure across all edge nodes and services | Juan designed and enforced the MQTT schema that all OSED components use — the same role as gAVA |
| Learning Engine selecting the most relevant view pattern | HEMS: the ML model selects which thermal model to apply based on building context — analogous pattern selection from historical data | Juan's model-selection logic is conceptually the same as the Learning Engine's pattern-selection step |
| Three-tier relevancy indexing (high/medium/low) | CVXPY MPC priority weights: Juan's optimization uses weighted objectives to prioritize control actions — the same relevancy ordering concept applied to optimization | Juan's optimization framework already implements the "weighted priority among competing objectives" that relevancy indexing formalizes |

**Sharpest bridge story:** "The POV file concept in this patent solves the same problem I solved in OSED's API layer: when you have many concurrent services all needing different slices of the same telemetry data, you need a mediation layer that assembles role-appropriate views rather than giving everyone raw DB access. In OSED, that's the FastAPI service layer with role-based endpoint filtering. In this patent, it's the data management module with a patterns database. The architecture is the same; the scale is different."

---

## Question to Ask the Director

> "The POV file patterns database is central to the whole data management design — it encodes what each module role should see. How is that patterns database populated and evolved? Is it hand-authored by domain engineers at design time, or does the Learning Engine update it based on observing which patterns actually resulted in effective formation outcomes? And is there a mechanism to detect when the existing patterns are insufficient for a novel grid condition — and trigger human-in-the-loop review?"
