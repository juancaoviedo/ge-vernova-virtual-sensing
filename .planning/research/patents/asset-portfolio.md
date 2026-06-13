# Patent: Asset Portfolio Manager for Adaptive Power Grid Management

## Bibliographic Data

| Field | Value |
|-------|-------|
| Title | Asset Portfolio Manager for Adaptive Power Grid Management |
| Publication Number | WO 2024/211758 A1 |
| PCT Application | PCT/US2024/023336, filed 2024-04-05 |
| US Priority Application | 18/131,758, filed 2023-04-06 |
| Publication Date | 2024-10-10 |
| Inventor | SHARIF-ASKARY, Jamshid |
| Assignee | GE Infrastructure Technology LLC, 300 Garlington Road, Greenville, SC 29615 |
| IPC Classes | G06Q 10/06, G06Q 10/0635, G06Q 10/00, G06Q 50/06, G06Q 10/0631 |
| Pages | 115 (image-only PDF) |
| Family Relationship | Continuation of US 18/131,758; continuation-in-part of AGMS parent (WO 2023/064623) |

---

## Problem Addressed

When the AGMS parent patent determines a formation plan, it identifies which assets (field devices, sensors, controllers, PMUs, microgrids) need to participate in an operation loop (ORACS — **Observability, Reachability, Adaptability, Controllability, Security**; the index set the patents define in their abbreviation key, extended to seven for verification with *sustainability* + *stability*). The parent patent's formation logic assumes asset availability and operational readiness, but does not specify how to verify that each candidate asset actually meets the operational requirements for that specific formation task. In degraded grid scenarios — post-disturbance, post-storm, during maintenance windows — a significant fraction of assets will be offline, degraded, or operationally mismatched for a given task. Deploying formation plans to unverified assets wastes scout resources, creates failed coordination loops, and risks incomplete formation execution. This patent fills that gap with a dedicated **Asset Portfolio Manager** that acts as a gating layer between the provisional logistics list (raw asset candidates) and the verified logistics list (assets cleared for inclusion in the formation plan).

---

## Core Technical Method

### Key New Concept: ORACS Operation Loop

The patent centers on the **ORACS** construct. The patents' own abbreviation key (para [0209]) defines ORACS as the five **operational-index dimensions** every operation loop must satisfy — *not* an Operation/Role/Asset/Context/Scouts backronym (that earlier gloss was an error and has been corrected):
- **O** — Observability (can the asset's state be seen / measured?)
- **R** — Reachability (can it be communicated with / commanded?)
- **A** — Adaptability (can it reconfigure to the task?)
- **C** — Controllability (can its behavior be driven?)
- **S** — Security (is it trustworthy / defensible?)

For asset *verification*, the Portfolio Manager extends these five to **seven** by adding **sustainability** and **stability**. ("Adaptability" sometimes appears as "adoptability" in the WO continuation's OCR — same index.)

An "ORACS operation loop formation construct" (Fig. 16) is the unit of work that the Asset Portfolio Manager validates. Each ORACS has a host ORACS (the lead asset) and participating ORACS (supporting assets). The formation plan may consist of multiple ORACS loops, each corresponding to a different geographic cluster or operational domain.

### Asset Portfolio Manager Workflow

**Inputs:**
- Formation plan from the Grid Wide Formation Manager (via Grid Wide Federation Command)
- Provisional logistics list: a set of candidate assets identified from a historical meta-object database, with tentative role assignments and DNA maps
- Asset database (gridWid asset portfolio DB, `gwapd`): stores asset attributes including operational indexes for observability, reachability, adoptability, controllability, sustainability, stability (the "O, R, A, C, S" operational dimensions)

**Step 1 — Asset Formation Processor** (Fig. 15, ref 1000):
Receives the formation file identifier (gWFCf(id)) and ORACS identifier. Parses the grid-wide formation context file, extracts asset function types, critical assets, and associated asset type attributes in relation to the ORACS operation. Generates a `corTemp(id)` correlation template.

**Step 2 — ORACS Resource Interdependency Analyzer** (Fig. 15, ref 1002B/1214):
Maps each asset's critical resources; determines the operational context; evaluates interdependency type (1-to-n, n-to-1, or n-to-n) for resources with complex dependency; defines cascading operational requirements; identifies the critical asset in the cascade. This is the dependency-graph analysis step.

**Step 3 — Operational Index Verification** (Fig. 15, ref 997–998):
Verifies that assets critical to the ORACS formation have acceptable operational indexes across all six dimensions: **observability, reachability, adoptability, controllability, sustainability, stability**. Assets failing any threshold are excluded. The `grid.wide.federation.mgr` executes this check against the `gwapd` asset portfolio database.

**Step 4 — ORACS Operation Loop Formation Construct** (Fig. 16):
Once assets pass the index check, the ORACS Operation Loop Formation Construct is instantiated:
- *ORACS-ol Correlation Engine* (ref 1015E): parses assigned resources in the logistic files; determines operation correlation using the Learning Engine and f(asset(id)); validates results in the Simulation Engine.
- *ORACS-ol DNA Analyzer* (ref 1421): performs DNA matching to identify ORACS and map to the best-matched DNA for interdependency level.
- *ORACS-ol DNA Matching Processor* (ref 1422): matches DNA patterns; determines coloration percentage; creates o, r, a, c, s analysis for each participating ORACS; produces a logistic gap file for participants with high interdependency correlation.
- *ORACS-ol Ownership ID Assignment* (ref 1423/1019C): creates a unique asset ID (`oracs.lf-tag`) in relation to host ORACS plus all interacting ORACS participating in the assigned operation loop.
- *ORACS-ol Tag-mgr* (ref 1024C): manages the tagging/labeling of all ORACS in the operation loop.

**Step 5 — Inter-ORACS Operation Formation** (Fig. 17):
For ORACS that span multiple operating cells (inter-operation formation), the inter-oracs context builder parses the meta-object, extracts the ORACS-id, associated context logistic file, correlation map, DNA-id, and determines neighboring ORACS-id. The `gWidLogistician` identifies logistic gaps and high-interdependency correlations between operating cells.

**Step 6 — Scout Formation and Launch** (Figs. 18–19):
`grid.scouts.command` receives the ORACS formation-ready signal, retrieves OC-meta-objects, extracts ORACS(id) and DNA.map(id) for host and participating ORACS. The `Scouts.launch.mgr` prepares a launch plan (time, load, origin, destination, asset(id)). The `Scouts.incubator.mgr` checks scout availability, assigns roles (coordinator, messenger, inspector, guard), coordinates with the participating ORACS coordinator, and re-supplies scouts if gaps are detected. The `gwPortfolio Custodian` interfaces with the `gridWid asset portfolio DB (gwapd)` throughout.

**Step 7 — GridwideEye PoV Frame** (Figs. 19, 30–32):
The `gridwideEye Liaison` creates a Point of View frame (PoVf.id) and contents. `gridwideEye` authenticates via ga-authenticationkey, passes the gWE-gatekeeper check, and the `gridwideEye PoV builder` (gridwideEye PoVbuilder) composes the point of view per PoVf.id. Different construct modules produce:
- `viewConstructModule`: observability & situational awareness with extended line of sight; condition-based PoV
- `controlConstructModule`: action list within ORACS operation; control PoV
- `adminConstructModule`: app collaboration links among participating apps; admin PoV

### Method Claims Summary (Figs. 20–24)

**Fig. 20 — Primary claim method** (6 steps):
1. Determine federation command template for formation plan based on context meta-object
2. Select at least one asset class from the asset database for each task of the plurality of tasks, based on comparing asset class attributes with class requirements
3. For each selected asset class, select at least one asset based on asset statuses associated with the tasks
4. Assign a task of the formation plan to the at least one asset
5. Generate a provisional logistics list comprising selected assets for the plurality of tasks
6. Cause the selected assets of the plurality of network devices to execute the formation plan

**Fig. 21 — Asset verification method** (6 steps):
1. Store asset attributes of assets on a network of devices in an asset database
2. Identify plurality of assets from a provisional logistics list assigned to one or more tasks of a formation plan having a plurality of states
3. Determine operation objectives for the formation plan
4. Determine operational index requirements for each asset based on the formation plan; verify the plurality of assets have acceptable operational indexes based on the operational index requirements and asset data in the asset database
5. Generate a logistics list comprising verified assets for the plurality of tasks for the formation plan
6. Cause the formation plan to be executed on the network of devices

**Fig. 22 — Historical meta-object matching method:**
Retrieve historical meta-objects; match schema based on comparing tasks of the operation loop and the logistics list with historical meta-objects; construct meta-objects for assets based on the matching schema and the formation plan.

**Fig. 23 — Scout command method** (7 steps):
1. Store asset data associated with devices in asset database
2. Receive scout command module: formation plan + logistics list with host asset and participant assets
3. Identify host asset and participant assets in the operation loop
4. Determine assigned roles for each of the plurality of participant assets
5. Verify availabilities of participant assets based on assigned roles and asset data
6. Determine a launch plan for the host asset and the plurality of participant assets
7. Cause the plurality of network devices to execute the formation plan based on the launch plan

**Fig. 24 — Data management (PoV) method:**
Communicate with devices to aggregate device data; receive a PoV file request; retrieve asset data from the asset database; select a view pattern from the patterns database; form a PoV file; send the PoV file to the requesting module.

---

## Connection to Juan's Work

| Patent Concept | Juan's Analogous Work | Bridge Narrative |
|---|---|---|
| ORACS operational index verification: checking observability, reachability, controllability before asset inclusion | OSED device health monitoring: verifying edge node connectivity, MQTT broker reachability, and inference pipeline health before dispatching control commands | Juan's OSED platform enforces a similar "is this node ready to receive a command?" gate before any actuator dispatch |
| Asset portfolio DB (gwapd): stores multi-dimensional operational attributes per device | Databricks/PySpark substation analytics: billions of sensor data points per device, tagged with device metadata, maintenance state, and operational class | Juan built and operated the large-scale asset data layer that would back the gwapd |
| DNA map: unique asset fingerprint encoding role, function, observability, DNA matching for interdependency | SI-MAPPER: computer-vision-to-ontology pipeline that creates a knowledge graph with typed entity nodes and relationship edges for each asset in a building system | SI-MAPPER is exactly the "DNA map" concept applied to building assets — typed identifiers + relationship graph |
| Scout launch plan: time, load, origin, destination, asset(id) — logistics scheduling | K8s pod scheduling in OSED: DaemonSets and Jobs scheduled to specific edge nodes with resource constraints | Juan has implemented software logistics at the K8s level that parallels the scout launch plan |
| Operational index dimensions: sustainability, stability | CVXPY MPC optimization: explicitly models energy sustainability constraints and stability bounds on controllable loads | Juan's optimization stack enforces the same constraint categories the patent measures as operational indexes |
| GridwideEye PoV frames: role-differentiated views of the same data (control PoV vs. admin PoV vs. observability PoV) | Grafana dashboards in OSED: different dashboards for grid operators vs. engineers vs. building managers, all pulling from the same InfluxDB/TimescaleDB backend | Juan has implemented the same multi-view-on-shared-data pattern |
| Learning Engine + Simulation Engine feedback loop for ORACS calibration | HEMS: the building thermal model is calibrated against actual thermal response and retrained; similar feedback between prediction and actuation | Juan's ML pipeline has the predict-observe-calibrate loop the patent's learning engine implements |

**Sharpest bridge story:** "When I built SI-MAPPER, I was solving a problem almost identical to the DNA map concept in this patent: I needed a typed, relationship-aware fingerprint for every asset in a building system so that automated agents could reason about inter-asset dependencies without human configuration. The SI-MAPPER ontology (based on ASHRAE 223P) maps to what the patent calls the DNA map. The Asset Portfolio Manager's dependency-graph analysis using DNA matching is exactly what SI-MAPPER's knowledge graph traversal does for building systems."

---

## Question to Ask the Director

> "The ORACS operational index has six dimensions — observability, reachability, adoptability, controllability, sustainability, stability. How are these indexes derived in practice: are they continuously updated from telemetry in real-time, or are they pre-computed from historical operational data and refreshed on a schedule? And when a formation plan needs to execute under a tight time constraint, is there a mechanism to accept an asset with a marginal index on one dimension if all other dimensions are strong?"
