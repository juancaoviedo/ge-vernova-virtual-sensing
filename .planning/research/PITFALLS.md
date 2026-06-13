# Pitfalls Research — Interview Prep

**Domain:** Grid virtual sensing / decentralized edge systems (GE Vernova Senior SE&S role)
**Researched:** 2026-06-13
**Confidence:** HIGH (technical content verified via multiple academic/official sources)

---

This document serves as both a pitfall guide and a mock-interview study sheet. The audience is
Juan Carlos Oviedo Cepeda preparing for a 1-week crash prep before a GE Vernova interview.
Each pitfall entry is structured as: the trap, why interviewers surface it, and the strong answer.

---

## Critical Pitfalls

### Pitfall 1: Claiming "Kalman Filter Experience" Without Depth

**What goes wrong:**
Candidate says "I understand state estimation and use Kalman-style approaches" without being
able to explain EKF vs. UKF, when linearization breaks down, how to tune Q and R, or what
filter divergence looks like and how to detect it.

**Why it's tricky / how interviewers probe it:**
Kalman filters are explicitly named in the JD. An interviewer will likely ask "walk me through
how you'd apply a Kalman filter to estimate line temperature from limited sensors." The trap
is giving a textbook-level answer (predict-update cycle) without demonstrating awareness of
failure modes:
- EKF requires Jacobian computation; if the process or measurement model is highly nonlinear
  (e.g., nonlinear power-flow equations), Jacobian approximation fails and the filter diverges.
- Q (process noise covariance) and R (measurement noise covariance) are tuning parameters;
  over-weighting R produces sluggish estimates that trail reality; over-weighting Q produces
  noisy, erratic output. Interviewers who have built these systems will notice if you treat
  these as set-and-forget constants.
- UKF sigma-point approach is more accurate for nonlinear systems but its sigma-point
  parameters (alpha, beta, kappa) also need tuning and its advantage assumes roughly
  Gaussian noise — which grid measurements often violate.
- Filter divergence: innovation sequence (z - H*x_hat) grows unboundedly; a chi-squared
  test on the innovations sequence is the standard early-warning.

**Strong answer / mental model:**
"EKF linearizes at each step — fine for mildly nonlinear systems like voltage magnitude
estimation, but risky where power-flow Jacobians become ill-conditioned near voltage
collapse. For those cases I'd move to UKF, which propagates sigma points through the
nonlinear function without Jacobian approximation. Grid measurements also have outliers
from bad data and GPS-spoofed PMU samples, so I'd pair the filter with a residual chi-
squared test gating the measurement update: if the normalized innovation exceeds a
threshold, I reject the sample rather than corrupt the state estimate. Q and R are
initialized from physics priors but must be adaptive — I'd look at approaches like the
Sage-Husa adaptive algorithm or covariance matching."

**Study phase:** Kalman/state estimation primer (Priority 1 gap).

---

### Pitfall 2: Conflating Distribution-Side Sensing with Transmission-Side Work

**What goes wrong:**
Juan's entire edge/sensing background is buildings, microgrids, and DER (distribution and
behind-the-meter). Without explicit translation, interviewers hear "HEMS and Modbus on
building HVAC" when the JD asks for "voltage stability, phase angles, line temperature, asset
health" on the bulk transmission system.

**Why it's tricky / how interviewers probe it:**
The interviewer knows the difference:
- Transmission: 3-phase balanced, high voltage (115–765 kV), PMU-rich, millisecond-class
  latency requirements for protection, SCADA polling 2–6 s, state estimation feeds EMS/AGC.
- Distribution: Three-phase unbalanced, low voltage, historically sensor-sparse, DER-driven
  bi-directional flow, ADMS rather than EMS.
If you speak only distribution vocabulary (load profiles, DR, HEMS) when asked about
transmission state estimation, you signal a domain gap that is exactly what the role is
trying to fill.

**Strong answer / mental model:**
Explicitly bridge the vocabularies: "My OSED work at Hydro-Québec operated at the
distribution/DER layer, but the architectural challenges are parallel and I've worked with
Hydro-Québec's EMS data from substation historians. At the transmission layer, the physics
are more tractable — balanced three-phase, well-observed with PMUs — but the consequences
of estimation error are much higher: wrong voltage-stability margin means load shedding or
cascading failure. The virtual sensing algorithms I'd bring to transmission would still use
the same filter/observer structure, but grounded in AC power-flow equations rather than
thermal or demand models." Then name specific transmission quantities (voltage phasors,
line impedance, thermal rating) and show you understand how they're measured vs. inferred.

**Study phase:** Transmission virtual sensing deep-dive (Priority 2 gap).

---

### Pitfall 3: Treating "Federated" as Synonymous with "Distributed"

**What goes wrong:**
Candidate uses "federated" loosely to mean "runs on multiple nodes" — which is just
distributed computing. GE Vernova's JD specifically calls for "federated architectures that
allow distributed nodes to collaborate securely without central coordination." That is a
precise technical constraint: no shared parameter server, no central aggregator, no single
point of failure or trust.

**Why it's tricky / how interviewers probe it:**
The interviewer will ask "how do nodes in your federated setup agree on a global model update
without sending raw data to a central server?" and probe for:
- FedAvg vs gossip-based aggregation vs decentralized SGD.
- Non-IID data problem: substation A has full PMU coverage; substation B has only SCADA
  RTU data every 6 s. Naive averaging of local gradients produces a globally biased model.
  This is the "client drift" failure mode.
- Partial failure: if 30% of edge nodes go offline mid-round, what happens to model
  convergence? Byzantine-fault tolerance?
- Security: without a trusted aggregator, how do you defend against a poisoned gradient
  injection from a compromised node?

**Strong answer / mental model:**
"True decentralized federated learning uses gossip or ring-reduce topologies — each node
exchanges model updates only with its neighbors, no central aggregator required. The non-
IID challenge in grid contexts is severe: feeder topology, DER mix, and load profiles
differ radically between substations. I'd use FedProx-style proximal regularization to
anchor local updates near the global model, limiting client drift. For Byzantine robustness
without a trusted server, coordinate-wise median aggregation (e.g., the Krum or GeoMed
approach) filters out outlier gradients. The trade-off is convergence speed: gossip
converges more slowly than centralized FedAvg, so I'd tune the communication rounds based
on the criticality of the update."

**Study phase:** Federated architectures primer (Priority 5 gap).

---

### Pitfall 4: Ignoring Time Synchronization as a Root Cause

**What goes wrong:**
Candidate designs a virtual sensing pipeline that aggregates PMU data (30–120 samples/s) with
SCADA RTU data (1 sample per 2–6 s) without accounting for clock alignment, GPS spoofing
vulnerability, and the effect of a 1 ms timestamp error on phase angle calculations.

**Why it's tricky / how interviewers probe it:**
A 1 µs GPS timestamp error corresponds to a ~0.02° phase angle error at 60 Hz — below
typical noise. But a 1 ms error (common with IEEE 1588 PTP jitter in congested networks)
is ~21° — which completely invalidates voltage stability indices. Interviewers will ask
"how do you handle heterogeneous sampling rates and clock drift?" Candidates who answer
"just resample everything to a common interval" miss the point: resampling without clock
alignment compounds error, and GPS spoofing attacks on PMUs have been demonstrated in
production grids.

**Strong answer / mental model:**
"I'd use GPS-synchronized IEEE C37.118 data from PMUs as the timing backbone and treat
SCADA data as low-frequency measurements in a mixed measurement state estimator — not try
to resample PMU data down to SCADA rates, which would throw away fast dynamics. For clock
drift between substations without GPS fallback, I'd implement cross-correlation between
overlapping sensor zones to detect anomalous phase offsets. GPS spoofing is a live threat:
the detection signature is a sudden correlated shift in phase angles across all PMUs at a
substation that isn't explained by load change — I'd monitor the innovation sequence for
that pattern and cross-validate against SCADA frequency readings, which are GPS-independent."

**Study phase:** Grid protocols and PMU/SCADA notes (Priority 4 gap).

---

### Pitfall 5: Virtual Sensor Overfitting to Training Topology

**What goes wrong:**
A virtual sensor trained on historical data from substation A works well during testing but
degrades silently after a network reconfiguration (switched feeder, added transformer,
topology change after a fault) because the ML model encoded topology-specific correlations
as if they were physical laws.

**Why it's tricky / how interviewers probe it:**
This is the "looks done but isn't" failure mode for production ML in grids. An interviewer
will ask "how do you validate a virtual sensor after you've deployed it?" The trap is saying
"I check RMSE on held-out test data" — which only validates the trained topology, not the
deployed one. The stronger answer distinguishes between:
- Model validation (does it generalize to unseen historical data?)
- Physical consistency checks (does the inferred value satisfy Kirchhoff's laws / power
  balance?)
- Operational monitoring (is the innovation sequence growing? Has the topology changed?)
No ground-truth sensor means you must triangulate.

**Strong answer / mental model:**
"Ground truth is often unavailable in production, so validation is multi-layered. First,
physics consistency: any inferred voltage must satisfy power-flow equations given neighboring
measurements — I'd run a lightweight power-flow check on inferred values and flag divergence.
Second, cross-sensor redundancy: where two sensing paths exist, I track the difference; a
growing discrepancy is a sensor or model drift signal. Third, after any topology change
(confirmed by SCADA switching events), I trigger a re-calibration window — the model must
be retrained or at least fine-tuned against the new topology before being trusted. The
Hydro-Québec AMI cross-validation pattern — using AMI data to expose feeder model drift
against apparently stable dashboards — is exactly this: the dashboard metric masks drift
that the twin's power-balance residual reveals."

**Study phase:** Virtual sensing & validation study notes.

---

### Pitfall 6: IEC 61850 GOOSE Used for Supervisory, Not Just Protection

**What goes wrong:**
Candidate says "IEC 61850 handles all real-time substation communication" without
distinguishing GOOSE from SAMPLED VALUES from MMS. Specifically, routing slow poll-and-
response traffic (meter reads, setpoints) over GOOSE instead of MMS/DNP3 wastes the
real-time channel and creates unpredictable latency for time-critical protection messages.

**Why it's tricky / how interviewers probe it:**
The JD lists IEC 61850 and DNP3 side by side. An interviewer knowledgeable in substation
automation will ask "how would you decide whether to use GOOSE or DNP3 for a given message?"
Candidates who describe GOOSE as "the fast protocol" without explaining the publisher-
subscriber (multicast, no acknowledgment) nature and the performance Class A (<4 ms) vs
Class B (<8 ms) requirements will sound like they memorized a glossary.

**Strong answer / mental model:**
"GOOSE is for protection-class events: breaker status changes, permissive transfer-trip,
bus differential signals. It's Ethernet multicast with no TCP/IP overhead, retransmitted
with decreasing intervals on change — designed to survive a single packet drop without
retransmit delay. DNP3 serves SCADA/DMS: polling, setpoints, operator commands, alarms.
Mixing them causes trouble: if I route DNP3 polling over the GOOSE VLAN, network congestion
degrades GOOSE retransmit timing and you lose the <4 ms guarantee. Sampled Values is a
third distinct channel — streaming current/voltage waveforms at 80 or 256 samples/cycle
for protection relays and digital fault recorders, not appropriate for state estimation
pipelines. For virtual sensing, I'd consume GOOSE events for topology change detection and
use the SV stream as the high-fidelity waveform source, with DNP3 or ICCP for the control-
center exchange."

**Study phase:** Grid protocols notes (Priority 7 gap — awareness level).

---

### Pitfall 7: MQTT as the Answer for All Edge Messaging in a Grid Context

**What goes wrong:**
Candidate defaults to MQTT for all edge messaging because it is the protocol they know from
IoT/building systems. For a decentralized grid deployment where messages must be persistent,
replayable, and deliverable across disconnected nodes, MQTT's hub-and-spoke broker model
is a single point of failure and cannot deliver local mesh communication.

**Why it's tricky / how interviewers probe it:**
The JD names Kafka/NATS, MQTT, and Pulsar together. The interviewer will ask "why would you
choose NATS over MQTT for edge nodes that may be intermittently connected?" Answering
"MQTT is what I know from my IoT work" concedes that you haven't thought about this
architectural choice.

**Strong answer / mental model:**
"MQTT works well for constrained devices reporting to a cloud broker but has two weaknesses
for decentralized grid edges: the broker is a single point of failure, and every message
must traverse the broker even if publisher and subscriber are on the same local network.
NATS with leaf nodes solves both: each edge site runs a local NATS server that handles
intra-site traffic with sub-millisecond latency without WAN dependency; when connectivity
is restored, it synchronizes with the cluster. For durable replay — important for event
sourcing and post-mortem analysis after a grid event — I'd add JetStream persistence to
NATS rather than adding Kafka, which is too resource-heavy for an edge node. Kafka lives
at the aggregation tier: high-throughput stream replay for historians, analytics, and
training data pipelines. Pulsar is worth knowing because GE Vernova's JD calls it out,
but its multi-layer architecture (bookie/broker split) adds operational complexity that
I'd only accept if multi-tenancy and geo-replication were requirements."

**Study phase:** Streaming stack notes (Priority 6 gap).

---

### Pitfall 8: Treating Edge Security as "Just TLS + Auth"

**What goes wrong:**
Candidate reduces edge security to "encrypt in transit, authenticate devices with certs"
without discussing supply-chain compromise, OTA update integrity, side-channel attacks on
constrained hardware, and the expanded physical attack surface of thousands of field devices.

**Why it's tricky / how interviewers probe it:**
The JD says "federated data pipelines that allow distributed nodes to collaborate securely
without central coordination." Without central coordination, revocation and key rotation
become hard. An interviewer will probe: "If one edge node is compromised, how does that
affect the rest of the federated system?" The trap: answering only about data-in-transit
encryption and ignoring gradient poisoning, replay attacks on OTA updates, and the cost of
heavyweight cryptography on constrained hardware.

**Strong answer / mental model:**
"Edge security has three layers the JD context makes critical. First, OTA update integrity:
firmware must be cryptographically signed with a hardware root of trust, and each device
should verify the signature before applying — unsigned or replayed updates are the most
common firmware attack vector. Second, federated model integrity: in a gossip-based model
update round, a compromised node can inject poisoned gradients. Coordinate-wise median
aggregation (Krum) provides Byzantine tolerance without a trusted server, but it adds
computational cost. Third, key management without a central authority: I'd use a device
certificate hierarchy (PKI embedded in silicon at manufacture) rather than runtime key
exchange, so revocation is offline-capable. The physical attack surface is real —
thousands of devices in accessible substations — so tamper-evident enclosures and TPM
attestation matter too."

**Study phase:** Federated architecture security notes.

---

### Pitfall 9: Dismissing Physics-Based Models in Favor of Pure Data-Driven Approaches

**What goes wrong:**
Candidate describes virtual sensing as "train an ML model to predict the unmeasured
quantity" without anchoring the model to physical constraints, making it brittle in
out-of-distribution scenarios (faults, load pockets, topology changes) and unacceptable
for grid operators who must understand why a value was estimated.

**Why it's tricky / how interviewers probe it:**
GE Vernova's research culture is explicitly physics-AI hybrid (patents reference adaptive
power, digital twins, OCR of physical data). An interviewer will ask "how do you handle a
scenario your training data never saw — say, a novel fault type?" Pure ML will hallucinate
a plausible but physically invalid estimate. The strong answer integrates physics.

**Strong answer / mental model:**
"Physics-informed neural networks (PINNs) or physics-constrained observers impose power-
flow equation residuals as soft constraints in the loss function — the model learns to
interpolate between measurements while respecting Kirchhoff's laws. For less expressive
edge nodes, a simpler approach is to use the physics model as the predict step in a Kalman
or particle filter and reserve ML for the measurement-update step (learning the nonlinear
measurement model). This hybrid gives you three things: physical interpretability (operators
can audit the estimate against a known model), graceful degradation under distribution shift
(the physics model still produces a bounded estimate even when ML component fails), and a
natural anomaly detector (large innovation = measurement is inconsistent with physics model)."

**Study phase:** Virtual sensing deep-dive + Kalman primer.

---

### Pitfall 10: Underestimating Observability as a Hard Mathematical Constraint

**What goes wrong:**
Candidate says "we'll infer missing sensor values" without first establishing whether the
system is observable — i.e., whether the available measurements are structurally sufficient
to uniquely determine all unknown states. In an under-observed grid segment, no algorithm
can uniquely estimate the voltage phasor; the problem is ill-posed, not just noisy.

**Why it's tricky / how interviewers probe it:**
Observability analysis precedes state estimation in every proper power-systems implementation.
An interviewer might ask: "You have a feeder with 10 buses and only 4 current magnitude
sensors. Can you estimate all bus voltages?" The correct answer involves the rank of the
measurement Jacobian, topological observability, and observable islands — not "we'll use
more data or a bigger model."

**Strong answer / mental model:**
"Observability analysis in power systems means checking whether the measurement Jacobian H
has full column rank relative to the number of state variables (typically 2n-1 for n buses
in DC approximation). Under-observed systems have observable islands separated by
unobservable boundaries — you can estimate states within an island but not their relative
phase offset. Virtual sensing's role is to extend observability: a virtual voltage sensor
at an unobserved bus must be tied to a physical anchor (measured bus) through the network
model, or you add a pseudo-measurement (load forecast with high uncertainty). The key
engineering decision is: is the virtual sensor providing information that makes an
unobservable island observable, or is it providing redundancy to an already-observed state?
The former is critical; the latter is just accuracy improvement."

**Study phase:** State estimation / Kalman primer (Priority 1 gap).

---

### Pitfall 11: Conflating Real-Time Control Safety with Best-Effort Software Engineering

**What goes wrong:**
Candidate describes a control loop in terms of uptime SLAs and retry logic — cloud-
infrastructure thinking — without discussing deterministic latency, watchdog timers, fail-
safe states, and the distinction between advisory outputs (dashboard) and actuation outputs
(breaker control) that have hard latency and reliability requirements.

**Why it's tricky / how interviewers probe it:**
The JD asks for "adaptive edge intelligence and control logic to enable real-time grid
insights with minimal latency" and references IEC 61850 Class A (4 ms) protection-class
timing. An interviewer will ask "what happens if your edge inference takes 50 ms instead
of 5 ms?" In cloud software, 50 ms is fine. In protection relay logic, it causes a breaker
to not trip on a fault and allows fault current to flow, potentially causing cascading
outages.

**Strong answer / mental model:**
"I distinguish three tiers: (1) protection-class actuation — hard real-time, typically
<4 ms, must be implemented in dedicated IEDs with deterministic RTOSes, not general-purpose
Linux/K3s stacks; (2) control-class response — soft real-time, 100 ms to 1 s range, can
run on edge computing nodes with careful scheduling priority and process isolation from
non-deterministic workloads; (3) advisory/optimization — seconds to minutes, standard
cloud-edge software stack. My edge software work targets tier 2 and 3. I would never route
protection trip logic through a Kubernetes pod. For the tier-2 control layer, I'd design
the edge application with a deterministic execution budget, use preemptive kernel
scheduling (PREEMPT_RT patch), and implement a watchdog that forces a safe fail state if
the control loop misses its deadline."

**Study phase:** System design drills.

---

## Candidate-Specific Traps (Juan's Background)

### Trap A: Speaking Only Building/DER Vocabulary

**Risk:** Interviewer asks "describe your experience with transmission-side sensing" and
candidate launches into HEMS, building thermal models, and Modbus/BACnet — all distribution
or behind-the-meter. The interviewer hears: "I have no T&D experience."

**Mitigation:** Prepare explicit vocabulary bridges in advance. Map each OSED/HEMS concept
to its transmission analog:
- Edge thermal state (building) → Line thermal rating (conductor ampacity, Dynamic Line Rating)
- DER dispatch control → AGC (Automatic Generation Control) / Volt-VAR Optimization
- MQTT from sensors → PMU / C37.118 synchrophasors
- InfluxDB time-series for demand → SCADA historian for voltage/frequency telemetry
- MPC on HVAC → MPC for reactive power scheduling at substation
Always anchor with: "My experience is distribution/DER side; the algorithmic patterns
are the same — the quantities and consequences differ."

---

### Trap B: Kalman Claim Without Depth

**Risk:** Candidate studied Kalman filter for 2 hours and says "yes, I'm familiar with
Kalman filters." Interviewer (who has implemented EKF for PMU-based state estimation) asks
two follow-up questions and the shallow knowledge is exposed.

**Mitigation:** Depth over breadth. Know one worked example cold:
"Estimate real-time line current from noisy CT readings and PMU voltage phasors using an
EKF with a linear network model as the prediction step and a nonlinear measurement model."
Be able to name Q and R concretely, describe what happens when the filter diverges, and
explain what the innovation sequence looks like.

---

### Trap C: Over-Emphasizing Academic Background at the Expense of Production Evidence

**Risk:** Candidate leads with PhD research and 30 papers when the JD is explicitly "hands-
on, startup-style." The interviewer wants to hear about shipping software that worked in
production under real grid conditions, not publications.

**Mitigation:** Lead with OSED: "architected and deployed a cloud-edge platform managing
real distributed assets at Hydro-Québec — real latency constraints, real grid events,
Kubernetes in production, real-time ML inference." Use research publications as supporting
evidence of depth, not as the headline. Map each story to a specific JD line.

---

### Trap D: Not Speaking GE Vernova's Own Language (Director's Patents)

**Risk:** Candidate is unfamiliar with the Electrification Chief Architect's published work
(adaptive power allocation, asset portfolio optimization, OCR of physical data) and cannot
connect the interview conversation to the lab's specific technical agenda.

**Mitigation:** Deep-read the four patents before the interview. Identify one concrete
connection per patent to Juan's own work. Prepare one question per patent that shows you
understood it: "In patent X, you use Y approach — I faced a related challenge in OSED
where I did Z; how does your approach handle [specific edge case]?"

---

## Likely Tough Interview Questions with Answer Keys

These are questions a senior engineer at GE Vernova with grid/state-estimation background
would realistically ask. For each, the key points of a strong answer are listed.

---

**Q1. Walk me through how you would design a virtual sensor to estimate real-time line
temperature on a 230 kV transmission line with only PMU current magnitude data and
weather telemetry.**

Key points:
- Use IEEE 738 conductor thermal model (ACSR ampacity model) as the physics predict step.
- Inputs: current magnitude (from PMU), ambient temperature, wind speed.
- State variable: conductor temperature (single scalar, or distributed along line).
- Use EKF or UKF: predict step = IEEE 738 heat balance ODE; update step = fuse in actual
  current measurement, update conductor temp estimate.
- Handle missing weather data: degrade gracefully using historical wind/temp climatology as
  a prior; flag elevated uncertainty to the operator.
- Validation without ground truth: cross-validate against a nearby reference line where
  temperature IS measured; monitor innovation sequence for drift.
- Output feeds Dynamic Line Rating (DLR): real-time ampacity rather than static nameplate.

---

**Q2. Your federated edge nodes are updating a shared model for voltage stability
prediction. One node starts injecting adversarial gradient updates. How do you detect
and mitigate this without a central coordinator?**

Key points:
- Detection: coordinate-wise anomaly — the update from the compromised node will have
  significantly higher norm or diverge directionally from its neighbors' updates.
- Mitigation: Byzantine-robust aggregation — coordinate-wise median (Krum) rather than
  mean. Gossip ring: each node aggregates only from k neighbors, limiting blast radius.
- Attestation: use TPM / secure boot attestation; if node fails hardware attestation, drop
  its update from the aggregation ring.
- Monitoring: track per-node contribution to global model loss over time; a sudden
  improvement in loss from one node after a period of stagnation is a red flag.
- Recovery: exclude the node from the gossip ring until manually re-certified; roll back
  the global model to the last known-good checkpoint.

---

**Q3. Explain the chi-squared test for bad data detection in power system state
estimation. What are its limitations?**

Key points:
- After weighted least squares (WLS) state estimation, compute the weighted residual sum
  J(x) = (z - h(x))^T * R^{-1} * (z - h(x)); this follows a chi-squared distribution
  with (m - n) degrees of freedom where m = measurements, n = states.
- If J(x) exceeds the chi-squared threshold at chosen confidence level, bad data is present.
- Limitation 1: identifies THAT bad data exists, not WHICH measurement. Identification
  requires normalized residual analysis (largest residual = suspect).
- Limitation 2: leverage measurements — measurements that, if removed, make a bus
  unobservable — have zero residual even if corrupted. The chi-squared test is blind to
  these.
- Limitation 3: interacting bad data (multiple bad measurements) can cancel each other's
  residuals, passing the chi-squared test while still corrupting the state estimate.
- Modern extension: False Data Injection Attack detection requires additional structure
  detection (the attack vector lies in the null space of H).

---

**Q4. How would you architect a decentralized data pipeline for 500 edge substation nodes
that must continue operating during WAN outages and synchronize reliably when connectivity
is restored?**

Key points:
- Each substation runs a local NATS leaf node (lightweight, <100 MB RAM) handling all
  intra-site messaging: PMU data, sensor readings, local control loops.
- JetStream persistence: all critical messages are durably stored locally; replay on
  reconnect ensures no data loss.
- WAN tier: NATS hub cluster in cloud / data center; leaf nodes auto-reconnect and replay
  persisted messages in order, de-duplicated by sequence ID.
- Avoid Kafka at the edge: Kafka's minimum JVM footprint (~1 GB) is too heavy for
  substation edge hardware. Kafka lives at the aggregation tier.
- Conflict resolution: CRDT (Conflict-free Replicated Data Type) for config state; for
  time-series measurement data, no conflict — timestamps are authoritative.
- Security: mTLS between leaf and hub; hardware-attested node certificates; message signing
  at source to prevent injection.

---

**Q5. IEC 61850 GOOSE vs. DNP3 — when do you use each, and what breaks if you get it
wrong?**

Key points:
- GOOSE: Ethernet multicast (Layer 2), no IP, <4 ms Class A latency, event-driven, no ACK.
  For: breaker trip permissive, bus differential initiation, status-change events.
- DNP3: TCP/IP or serial, polling-based, 100 ms to seconds. For: SCADA telemetry, operator
  setpoints, alarms, control-centre exchange.
- Getting it wrong: routing DNP3 polling traffic on the GOOSE VLAN creates network
  congestion; GOOSE retransmit intervals are timing-sensitive and will not meet Class A
  guarantee. Conversely, using GOOSE for setpoints loses ACK confirmation — you don't
  know if the control reached the device.
- Sampled Values (SV): waveform streaming at 80 or 256 samples/cycle; for protection relays
  and digital fault recorders, NOT for state estimation pipelines (too much data, too
  specialized).
- MMS/ACSI over TCP: configuration, file transfer, reporting — the "northbound" interface
  to EMS/SCADA.

---

**Q6. How does non-IID data distribution across grid edge nodes affect federated learning
convergence, and what does that look like specifically in a substation context?**

Key points:
- Non-IID means each substation's local dataset has a different statistical distribution:
  feeder A has industrial loads with flat demand profiles; feeder B has residential loads
  with morning/evening peaks; feeder C has high solar PV.
- Effect: local SGD updates pull the model toward the local optimum. When averaged (FedAvg),
  the result is a global model that fits no substation well — especially ones with unusual
  load profiles.
- Manifestation: accuracy on feeder C (high solar) is systematically worse than feeders A
  and B; the global model has never seen feeder C's distribution well-represented.
- Mitigation: FedProx proximal term (penalizes deviation from global model during local
  training); clustered FL (group substations by load type and train separate models);
  personalization layer on top of a shared base model.
- Concept drift in grids: seasonal load shifts, new DER installations, topology changes.
  Requires periodic full retraining or incremental fine-tuning triggered by drift detectors
  (e.g., ADWIN on prediction error).

---

**Q7. You have 10 minutes to explain your most relevant project to the Electrification
Chief Architect. Go.**

Key points (STAR structure with GE Vernova vocabulary):
- Situation: Hydro-Québec needed to coordinate distributed controllable loads (building
  HVAC, EV chargers, water heaters) across 10,000+ sites to provide real-time grid
  services (frequency response, voltage support at the feeder level).
- Task: Architect a cloud-edge platform that pushed control decisions to the edge of
  the distribution network with sub-second latency while maintaining Hydro-Québec's
  privacy and security requirements.
- Action: Built OSED — a Kubernetes-orchestrated edge platform with local ML inference
  for thermal state estimation (virtual sensor for building temperature trajectory),
  MQTT-based secure data pipelines, InfluxDB time-series at edge and cloud, and a
  convex optimization dispatch layer. Used Modbus/BACnet for legacy device interop.
  Embedded adaptive control logic at the edge so nodes continued operating during
  cloud connectivity loss.
- Result: 21% cost reduction via dynamic tariff response; demonstrated sub-second
  control latency; led Hydro-Québec into Linux Foundation Energy open-source community.
- Vocabulary bridge: frame HEMS thermal model as "virtual sensing for building thermal
  state"; frame OSED as "federated edge control without central coordination"; frame
  DER dispatch as "decentralized grid services at the distribution edge."

---

**Q8. GPS spoofing of PMU timestamps: how do you detect it and what's the state
estimation impact?**

Key points:
- PMUs use unencrypted GPS civil signals for 1 PPS time synchronization; a spoofing
  transmitter can shift the phase reference by inducing a false time offset.
- Impact: a 1 ms time offset at 60 Hz = 21.6° phase angle error. This shifts the voltage
  phasor reading by that angle, corrupting voltage stability indices and inter-area
  oscillation monitoring that rely on relative phase angles between PMUs.
- Detection signatures:
  (a) Sudden correlated jump in phase angles across ALL PMUs at one substation but not
      neighboring ones — GPS spoof is substation-local.
  (b) Phase angle change inconsistent with any load change visible in SCADA MW/MVAR.
  (c) Cross-validation: compute line flow implied by phase angle difference and compare
      to flow meter on same line — discrepancy exceeds noise threshold.
- Mitigation: IEEE 1588 PTP over fiber as a GPS-independent backup timing source;
  chi-squared test on the innovation sequence gated by a physical plausibility check
  (angle change rate bounded by system inertia).

---

**Q9. What is Dynamic Line Rating and how would you implement it as a virtual sensing
product?**

Key points:
- Static thermal rating assumes worst-case (low wind, high ambient). DLR computes real-time
  ampacity from actual weather and conductor state.
- Virtual sensing angle: we don't have a conductor temperature sensor on most lines, so we
  infer it from available current, voltage, and weather telemetry.
- Implementation: IEEE 738 heat balance ODE as the physical model; EKF wrapping it uses
  current magnitude (PMU) as the measurement; conductor temp is the latent state.
- DLR can unlock 10–40% additional capacity on existing lines — the most cost-effective
  grid upgrade possible.
- Failure modes to address: wind speed data sparsity (substation anemometers are not
  representative of the entire line span); conductor aging changes thermal constants;
  model must be re-calibrated periodically.
- Connection to JD: line temperature is explicitly named as a target virtual sensing
  quantity. This is a worked example ready to deploy.

---

**Q10. Why would you choose a physics-informed ML approach over pure data-driven ML for
voltage stability margin estimation, and what are the tradeoffs?**

Key points:
- Data-driven only: fast to train, good interpolation within training distribution, but
  fails silently on out-of-distribution operating conditions (stressed system near voltage
  collapse is by definition rare in training data).
- Physics-informed (PINN or hybrid observer): loss function includes power-flow equation
  residuals as soft constraints. Model cannot output a voltage that violates Kirchhoff's
  laws.
- Tradeoffs: PINNs are harder to train (competing loss terms, need proper weighting);
  require an accurate physics model (if the model is wrong, the constraint is wrong);
  inference is slower.
- Grid-specific reason to prefer physics-informed: operators and NERC reliability
  standards require explainable estimates. "The ML model said voltage stability margin
  is 15%" is not acceptable without a physical grounding. "The model's estimate is
  consistent with the linearized power-flow solution given observed measurements" is.
- Practical hybrid: use physics model as predict step (Kalman-style), use ML for the
  nonlinear measurement model correction. Best of both.

---

**Q11. Your edge node has 4 GB RAM and 2 CPU cores. You need to run: local NATS broker,
Kalman filter state estimator (updating at 30 Hz), a federated learning local training
job, and a local K3s agent. How do you resource-partition this?**

Key points:
- K3s agent itself needs ~300 MB RAM and minimal CPU when idle — allocate 512 MB with
  a hard limit to prevent it starving control software.
- NATS server: <50 MB RAM, negligible CPU for 30 Hz message rate at one substation.
- Kalman estimator at 30 Hz: compute budget depends on state size. A 20-bus EKF
  costs O(n^3) per step; for 20 states: microseconds on a modern ARMv8. Allocate
  dedicated CPU core with SCHED_FIFO priority to guarantee deterministic latency.
- Federated training: the biggest consumer and the most flexible. Run as a background
  batch job using remaining RAM (~2 GB) and the second CPU core, with SCHED_BATCH
  priority — preempted whenever the estimator needs CPU. Schedule training rounds
  during low-traffic periods (off-peak); do not run during grid stress events.
- Practical constraint: ML model size must fit in the 2 GB budget; use quantization
  (INT8) or pruning to keep the local model small enough for edge inference.

---

**Q12. How do you "close the loop" between a simulation environment (RTDS/PSCAD) and a
live grid deployment of a virtual sensing algorithm?**

Key points:
- Step 1 — Hardware-in-the-loop (HIL): simulate the grid in RTDS; feed real PMU-format
  data to the virtual sensing algorithm running on actual edge hardware. Validate timing,
  latency, and accuracy against known simulation ground truth.
- Step 2 — Software-in-the-loop (SIL): run the full software stack (K3s, NATS, estimator)
  in a containerized RTDS interface. Stress-test with fault scenarios the real grid rarely
  produces.
- Step 3 — Pilot deployment with parallel run: deploy virtual sensor on a real substation
  while keeping the existing SCADA estimator running. Compare outputs for 30–90 days;
  calculate RMSE against any available physical sensors.
- Step 4 — Gradual cutover: promote virtual sensor output as advisory, then as a soft
  input to control loops, then as primary signal only after sustained performance.
- The "reality gap" failure: simulation model does not include transformer tap position
  uncertainty, line parameter aging, or telemetry delay. Virtual sensors trained on RTDS
  data will have systematic bias on the real system. Mitigation: online fine-tuning with
  real data during the pilot phase.

---

## Phase-Specific Warnings

| Study Phase | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Kalman/State Estimation primer | Memorizing predict-update without EKF/UKF tradeoffs | Work through the grid line-temp EKF example numerically |
| Transmission virtual sensing | Using distribution vocabulary when asked T&D questions | Build explicit vocabulary bridge table; practice translating each story |
| Director's patents deep-read | Treating patents as background reading, not interview material | Prepare one concrete connection per patent to your own work |
| PMU/SCADA/DNP3 protocols | Knowing what protocols exist but not when to use each | Study the GOOSE vs DNP3 decision table; memorize Class A/B timing |
| Federated architectures | Confusing distributed with federated; missing non-IID problem | Work through FedAvg vs FedProx math; explain client drift in your own words |
| Streaming stack | Defaulting to MQTT without justification | Practice the MQTT vs NATS vs Kafka decision framework aloud |
| System-design drills | Giving cloud-software answers to hard-real-time control questions | Practice the three-tier control latency framing before every drill |
| Behavioral/STAR stories | Leading with papers/PhD rather than production impact | Rewrite every story to open with the deployed outcome |

---

## Sources

- [Power System Dynamic State Estimation Using Extended and Unscented Kalman Filters (arXiv 2012.06069)](https://arxiv.org/pdf/2012.06069)
- [State estimation of voltage and frequency stability using multiple filtering techniques (Nature Scientific Reports 2025)](https://www.nature.com/articles/s41598-025-10171-2)
- [Adaptive Extended Kalman Filter with Correntropy Loss (PMC 2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7514774/)
- [Decentralized UKF based on consensus for multi-area dynamic state estimation (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0142061514005754)
- [Undetectable GPS-Spoofing Attack on PMU Time Series Data (arXiv 2206.12440)](https://arxiv.org/pdf/2206.12440)
- [Dynamic GPS Spoofing Attack Detection using PMU and SCADA (IEEE Xplore)](https://ieeexplore.ieee.org/document/9127471/)
- [Vulnerability and Impact Analysis of IEC 61850 GOOSE Protocol (MDPI Sensors 2021)](https://www.mdpi.com/1424-8220/21/4/1554)
- [IEC 61850 GOOSE testing guide (OPAL-RT blog)](https://www.opal-rt.com/blog/iec-61850-goose-messaging-and-how-to-test-it-for-substation-automation-projects/)
- [Federated learning for critical electrical infrastructure — data heterogeneity (Frontiers AI 2025)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1697175/full)
- [Trustless Federated Learning at Edge-Scale (arXiv 2511.21118)](https://arxiv.org/html/2511.21118v1)
- [NATS vs MQTT for IoT Fleet Management (Synadia)](https://www.synadia.com/blog/nats-vs-mqtt-technical-comparison-iot-fleet-management)
- [Kafka, Pulsar, and NATS comparison (RisingWave)](https://risingwave.com/blog/kafka-pulsar-and-nats-a-comprehensive-comparison-of-messaging-systems/)
- [Virtual sensing in intelligent buildings — validation and drift (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0926580522004484)
- [Power System Digital Twins: Lessons Learned (IET Digital Twins 2025)](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/dgt2.70015)
- [Grid Edge Sensor Networks for ADMS Control (Electricity Forum)](https://electricityforum.com/iep/asset-intelligence/grid-edge-sensor-networks)
- [Distribution vs Transmission grid sensing (PNNL sensor network report)](https://gridarchitecture.pnnl.gov/media/advanced/Sensing_for_Advanced_Grids_v1_7_GMLC.pdf)
- [Linear State Estimation and Bad Data Detection for Power Systems (arXiv 2001.10764)](https://arxiv.org/pdf/2001.10764)
- [Quantum Technologies and Edge Devices in Electrical Grids (arXiv 2603.06783)](https://arxiv.org/pdf/2603.06783)

---
*Pitfalls research for: GE Vernova Virtual Sensing & Decentralized Grid Operations interview prep*
*Researched: 2026-06-13*
