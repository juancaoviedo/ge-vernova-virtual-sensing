# Knowledge Domain Map: Grid Virtual Sensing & Decentralized Operations

**Domain:** Senior interview prep — edge virtual sensing in power grids
**Researched:** 2026-06-13
**Confidence:** HIGH (core concepts verified against academic literature and official standards)

---

## Purpose of This File

This is not a software feature list. It is a **body-of-knowledge map** for Juan Carlos's
interview preparation. Each entry is a technical topic the role explicitly requires or
implies. The three tiers answer: *what do I need to be able to say in the room?*

- **Table Stakes** — You must be able to discuss these fluently. Gaps here are disqualifying.
- **Differentiators** — Depth here sets you apart from other senior candidates.
- **Awareness-Only** — Know the name, one-sentence definition, and that you can learn it fast.

For each topic: what it is, why it matters for THIS role, and how Juan's existing work bridges to it.

---

## Table Stakes (Must Command — Disqualifying If Missing)

### 1. Power System State Estimation (Static / WLS)

**What it is:**
State estimation determines the "best guess" of the grid's operating state — bus voltages
(magnitude and phase angle) and power flows — from a redundant, noisy set of measurements
(meters, PMUs, SCADA readings). The classical algorithm is Weighted Least Squares (WLS):
minimize `(z - h(x))^T W (z - h(x))` where `z` are measurements, `h(x)` is the
measurement model, `x` is the state vector (voltage magnitudes + angles), and `W` is the
measurement covariance inverse. Solved iteratively via Gauss-Newton.

**Why it matters for this role:**
Every "virtual sensing" algorithm is ultimately a state estimator inferring unobserved
quantities from observed ones. The JD explicitly lists "state estimation" as a required
technique. This is the conceptual parent of everything else on this list.

**Bridge from Juan's work:**
Juan already does this. In building thermal control (OSED), he estimates the thermal state
of a building from temperature sensors plus a physics model (RC network) to drive MPC.
That IS state estimation. The grid version uses a power flow model (`h(x)` = nonlinear
AC power flow equations) instead of a thermal RC model — same mathematical structure,
different physics. Key vocabulary: "measurement model," "state vector," "residuals,"
"observability," "bad data detection," "chi-squared test."

**What to be able to say:**
- Define the WLS objective and explain why Gauss-Newton is used (nonlinear `h(x)`)
- Explain "observability" — a grid is observable if you have enough measurements to
  uniquely determine all state variables
- Explain "bad data detection" via normalized residuals (chi-squared hypothesis test)
- Contrast static SE (snapshot, SCADA ~4-second scans) vs. dynamic SE (time-recursive)

**Complexity:** HIGH | **Interview weight:** CRITICAL

---

### 2. Kalman Filters — Linear KF, EKF, UKF

**What it is:**
The Kalman Filter is a recursive Bayesian estimator for linear dynamical systems. It has
two stages: **Predict** (use a system model to extrapolate state forward in time) and
**Update** (correct the prediction with a new measurement, weighting by relative
uncertainty). For nonlinear systems: Extended Kalman Filter (EKF) linearizes the model at
the current estimate via Jacobian; Unscented Kalman Filter (UKF) propagates a set of
"sigma points" through the true nonlinear function — more accurate, no Jacobian needed,
easier to implement.

In power grids, Dynamic State Estimation (DSE) uses EKF/UKF on a machine or generator
model to track rotor angle (δ), rotor speed (ω), and internal EMF — the quantities
SCADA is too slow to observe but PMUs can support.

**Why it matters for this role:**
The JD literally names "Kalman filters, state estimation" in the required qualifications.
This is Gap #1 in the project brief. A candidate who can't articulate KF predict-update
and the EKF/UKF distinction will fail the technical screen.

**Bridge from Juan's work:**
Building thermal estimation with MPC is close. The canonical approach for online building
thermal parameter estimation (published work: ScienceDirect 2019, ResearchGate 2014) uses
UKF to jointly estimate temperature states and RC parameters. Juan's RC-thermal estimator
is structurally the same as UKF-based DSE: both track a hidden state using a physics model
plus noisy observations. The key bridge sentence: "In OSED I used a physics-based model
and measurement residuals to update my state estimate at each control cycle — the same
predict-update structure as a Kalman filter; I'm formalizing that into KF vocabulary now."

**What to be able to say:**
- Predict step: `x_k|k-1 = F * x_k-1 + B * u`, `P_k|k-1 = F P F^T + Q`
- Update step: Kalman gain K, state update, covariance update
- EKF: Jacobian linearization; UKF: sigma points avoid Jacobian, better for highly
  nonlinear systems
- Grid application: DSE tracks generator rotor angle δ and speed ω at PMU rate (30-60 Hz)
- Process noise Q = model uncertainty; Measurement noise R = sensor uncertainty
- Tuning Q and R is the practical challenge (and where physics knowledge matters)

**Complexity:** HIGH | **Interview weight:** CRITICAL

---

### 3. Phasor Measurement Units (PMUs) and Synchrophasors

**What it is:**
A PMU samples voltage/current waveforms at high rate (typically 30-240 samples/sec),
computes magnitude and phase angle of the fundamental frequency component via DFT, and
time-stamps each sample using GPS (or IEEE 1588 PTP) to microsecond accuracy. The result
is a "synchrophasor" — a phasor synchronized across all PMUs in the network. This enables
WAMS: Wide-Area Measurement System. PMU data is aggregated by a Phasor Data Concentrator
(PDC) and transmitted via C37.118 protocol.

Static SCADA updates every ~4 seconds; PMUs report at 30-60 Hz. That 100x speed-up is
what makes Dynamic State Estimation and real-time virtual sensing tractable.

**Why it matters for this role:**
PMUs are the primary measurement source for transmission-level virtual sensing. Phase
angles directly indicate power flow direction and magnitude; phase angle differences signal
congestion and proximity to stability limits. Voltage magnitude + angle together = the
grid's state vector.

**Bridge from Juan's work:**
Juan processes substation timeseries data (Databricks/PySpark, billions of measurement
points). PMU data is the same telemetry at higher resolution. His InfluxDB/TimescaleDB
stack is exactly where PDC-aggregated synchrophasor streams land. Bridge vocabulary:
"PMU is the grid's IoT sensor; PDC is my MQTT broker aggregation layer."

**What to be able to say:**
- PMU measures: voltage phasor (V∠θ), current phasor, frequency, ROCOF
- GPS synchronization: all PMUs share the same time reference → phase angle differences
  are meaningful across substations hundreds of km apart
- C37.118.1: the IEEE standard for synchrophasor data format and transmission
- PDC: aggregates streams from multiple PMUs into a coherent dataset
- WAMS vs. SCADA: speed (30-60 Hz vs. 0.25 Hz), coverage (wide-area vs. local)

**Complexity:** MEDIUM | **Interview weight:** HIGH

---

### 4. Voltage Stability Monitoring and Voltage Stability Index (VSI)

**What it is:**
Voltage stability is the grid's ability to maintain acceptable voltages at all buses after
a disturbance. As load increases or generation trips, reactive power demand strains
transmission lines; at the "nose point" of the P-V curve, voltage collapses. Online VSIs
quantify proximity to that collapse. Common approaches:
- Thevenin equivalent: from PMU measurements, estimate the equivalent source impedance
  behind each bus; as load increases, source impedance approaches load impedance → VSI → 1
- L-index: compares load bus voltage to generator bus voltages via a linear algebra
  formulation; values 0–1 (1 = collapse)
- V-Q sensitivity: sensitivity of bus voltage to reactive power injection

**Why it matters for this role:**
Voltage stability is the first target parameter listed in the JD: "infer critical power
grid parameters (e.g., voltage stability, phase angles, line temperature, asset health)."
This is a core "what does the virtual sensor actually sense?" topic.

**Bridge from Juan's work:**
Voltage stability monitoring is structurally similar to Juan's building demand-response
work: both assess "proximity to constraint violation" in real time to trigger control
action. His OSED work already tracks grid-signal thresholds (dynamic tariffs responding to
grid stress). The T&D extension adds physics: reactive power, bus voltages, P-V curves.

**What to be able to say:**
- P-V curve and the "nose point" — where collapse occurs
- Why reactive power (Q) is critical for local voltage support
- Thevenin equivalent approach: estimate Z_th from PMU data, compute VSI = |Z_load|/|Z_th|
- Limitations: PMU coverage is sparse → virtual sensing fills the gap at unmonitored buses
- Connection to DERs: inverter-based resources can provide reactive support; this is where
  DER control (Juan's HEMS/OSED) plugs into T&D voltage stability

**Complexity:** HIGH | **Interview weight:** HIGH

---

### 5. Phase Angle and Power Flow Inference

**What it is:**
In AC power systems, the active power flow on a transmission line is approximately:
`P ≈ (V_i * V_j / X_ij) * sin(δ_i - δ_j)` where δ is the voltage phase angle and X_ij
is line reactance. Phase angle differences thus directly indicate power flow. Large
differences → high loading → congestion risk. If PMUs are not at every bus, phase angles
at unmonitored buses must be inferred from adjacent PMU readings and the network topology
model — this is the virtual sensing problem.

**Why it matters for this role:**
Phase angle is the second explicit parameter in the JD. The virtual sensing algorithm to
infer phase angles from sparse PMU measurements is a direct application of state
estimation (Topic 1) using the power flow model as `h(x)`.

**Bridge from Juan's work:**
Juan's convex optimization background (Stanford course) is directly applicable. The DC
power flow approximation (`P = B * θ` where B is the susceptance matrix, θ are angles)
reduces to a linear system. Solving it with measurement uncertainty → Juan's WLS toolbox.
His DLMP pricing research also uses locational marginal prices that embed congestion
signals correlated with phase angle differences.

**What to be able to say:**
- Phasor: V∠θ — magnitude and angle of AC voltage at a given frequency
- Phase angle difference δ_i - δ_j is the primary congestion signal
- DC power flow approximation: linearization valid for high-voltage (small angles, flat
  voltages) — makes optimization tractable
- AC power flow: full nonlinear model needed for precise estimation
- PMU coverage gap: transmission has ~20-40% PMU coverage today; virtual sensing
  estimates angles at unmonitored buses

**Complexity:** MEDIUM | **Interview weight:** HIGH

---

### 6. Dynamic Line Rating (DLR) and Conductor Temperature Estimation

**What it is:**
Overhead transmission lines have a static thermal rating (worst-case current capacity =
ampacity) based on conservative weather assumptions. Dynamic Line Rating (DLR) replaces
the static limit with a real-time estimate based on actual ambient temperature, wind speed,
solar radiation, and line current. The thermal model (IEEE 738 standard) relates conductor
temperature to these inputs:
`m*c * dT_c/dt = I²*R(T_c) - q_convective(T_c, wind) - q_radiative + q_solar`
This is an ODE for conductor temperature `T_c`. In DLR, conductor temperature is often
not directly measured — it is estimated from current, ambient sensors, and the IEEE 738
model. That estimation is virtual sensing.

**Why it matters for this role:**
"Line temperature" is explicitly named in the JD as a virtual sensing target. DLR is a
live GE Vernova product area. The physics model (thermal ODE) + measurement integration
is exactly the pattern of virtual sensing the role is building.

**Bridge from Juan's work:**
Juan's building thermal model is an RC network — `C * dT/dt = Q_load - UA*(T - T_amb)`.
The IEEE 738 conductor temperature ODE has IDENTICAL structure. Both are first-order
thermal systems with a time constant. His MPC/state-estimation experience on buildings
transfers directly: swap the building RC parameters for IEEE 738 parameters, swap indoor
temperature for conductor temperature, swap HVAC load for I²R heating. This is the
strongest and most concrete bridge to articulate.

**What to be able to say:**
- Static vs. dynamic thermal rating: static is conservative, DLR unlocks 10-40% more
  capacity in real conditions
- IEEE 738 standard: the thermal balance ODE for overhead conductors
- Virtual sensing angle: temperature is rarely directly measured; inferred from current
  and weather via the thermal model, with Kalman filter for online estimation
- Ampacity: maximum current given a maximum safe conductor temperature (typically 75–100°C
  for steel-core aluminum conductors)
- Operational value: DLR can defer expensive line upgrades while renewable integration
  increases peak flows

**Complexity:** MEDIUM | **Interview weight:** HIGH

---

### 7. Asset Health Estimation (Transformers, Lines, Breakers)

**What it is:**
Power transformer insulation degrades with thermal stress (Arrhenius aging law). Health
indices combine dissolved gas analysis (DGA), oil quality tests, load history (hot-spot
temperature estimation per IEEE C57.91), and electrical test data into a Remaining Useful
Life (RUL) estimate. Machine learning on these multivariate timeseries improves on
physics-only models. Edge inference means running the health model locally at the
substation rather than waiting for centralized analytics.

**Why it matters for this role:**
"Asset health" is the fourth named parameter in the JD. The edge deployment angle
(running health models on field devices) is a key differentiator for decentralized
operations.

**Bridge from Juan's work:**
Juan's edge ML (thermal load forecasting on edge devices in OSED) is the infrastructure
pattern. Replace building thermal state with transformer hot-spot temperature; replace
HVAC controllable load with maintenance alert/dispatch signal. The ML pipeline
(timeseries features → model inference → alert) is identical. The physics differs:
IEEE C57.91 thermal model for transformers instead of RC building model.

**What to be able to say:**
- IEEE C57.91: hot-spot temperature model for power transformers (fundamental aging driver)
- DGA: dissolved gases (H2, C2H2, CH4, etc.) are leading indicators of fault type and
  severity — this is the primary "sensor" for transformer health monitoring
- Remaining Useful Life (RUL) estimation: regression/LSTM on historical load + DGA data
- Edge vs. centralized: edge inference enables faster response, offline operation, and
  avoids privacy/data-sovereignty issues for utility data
- Connection to federated learning (Topic 10): each substation trains locally, aggregates
  anonymized model updates

**Complexity:** MEDIUM | **Interview weight:** HIGH

---

### 8. SCADA and Industrial IoT Protocols: DNP3, LoRa, MQTT, Modbus

**What it is:**
- **SCADA (Supervisory Control and Data Acquisition):** The traditional control-center
  system polling field RTUs every 4+ seconds via DNP3 or IEC 60870-5-101/104.
- **DNP3 (Distributed Network Protocol 3):** The dominant North American utility protocol
  for SCADA. Supports unsolicited reporting, time-stamped events, integrity polls. Not
  IP-native (predates TCP/IP) but runs over TCP/IP today. Contrast to MQTT: DNP3 is
  master-slave with defined utility data objects; MQTT is broker-based with arbitrary
  topics.
- **LoRaWAN:** Low-power wide-area network for IoT. Enables battery-powered sensors
  (line temperature probes, vibration, sag detection) across km-scale areas without
  cellular or fiber. Used for DLR sensors on transmission towers.
- **MQTT:** Juan already knows this. In the grid context it bridges from field devices to
  edge brokers; OpenFMB runs over MQTT/NATS/DDS.

**Why it matters for this role:**
The JD explicitly lists SCADA, PMUs, DER controllers, LoRa, MQTT, DNP3, Modbus as field
data sources. Understanding the protocol stack is table stakes for the "integrate field
data sources" responsibility.

**Bridge from Juan's work:**
Juan uses MQTT, Modbus, BACnet, OpenADR in OSED. DNP3 is the utility-substation
equivalent of Modbus: a fieldbus with defined data models for grid-specific objects
(analog inputs = meter readings, binary inputs = breaker status, analog outputs = setpoints).
Bridge: "I use Modbus for building equipment; DNP3 is Modbus's utility-substation cousin
with added features for SCADA reliability (unsolicited reporting, event buffering)."

**What to be able to say:**
- DNP3 key features: unsolicited reporting (device pushes data without polling), event
  buffering (stores readings if comms fail), defined data types for grid objects
- LoRa/LoRaWAN: star topology, 1-10 km range, battery life years, 0.3-50 kbps — perfect
  for infrequent DLR sensor readings or line sag monitors that can't have wired connections
- SCADA vs. WAMS: 4-second scan rate (SCADA) vs. 30 Hz (PMU/WAMS) — this speed gap is
  exactly why dynamic virtual sensing matters
- OpenFMB: runs over MQTT/NATS/DDS, bridges SCADA-world IEC 61850 models to IP-native
  publish-subscribe — Juan's most natural entry point to utility-specific protocols

**Complexity:** MEDIUM | **Interview weight:** HIGH

---

### 9. Edge-Native Architecture for Decentralized Grid Operations

**What it is:**
"Decentralized" means intelligence is pushed to field devices — substations, feeder
automation controllers, DER edge nodes — rather than relying on a central EMS/SCADA.
The architecture has three tiers:
1. **Edge device** (RTU, IED, small compute): runs local state estimation, protection
   logic, primary control loop. K3s (lightweight Kubernetes) or bare-metal.
2. **Edge aggregator** (substation compute, ~Raspberry Pi class): runs virtual sensing
   algorithms, local SCADA bridge, federated model aggregation.
3. **Cloud/regional control center** (optional, async): fleet management, model updates,
   planning optimization.

Federated data pipelines: each node processes its own data, shares only model parameters
or aggregated summaries — not raw measurements — to the regional tier.

**Why it matters for this role:**
The entire role is about building this architecture. "Distributing intelligence to the
resilient edge" is the job's core mission statement.

**Bridge from Juan's work:**
OSED is this architecture applied to buildings: building edge node (Raspberry Pi,
sensors) → edge aggregator (FastAPI/InfluxDB on-premise) → cloud (Kubernetes, GCP).
The components differ (IEDs instead of building controllers) but the pattern is identical.
Juan's Kubernetes/K3s, gRPC, MQTT, InfluxDB/TimescaleDB skills are exactly the edge
stack the JD requires.

**What to be able to say:**
- K3s vs. K8s: K3s is the lightweight Kubernetes distribution for edge (< 512 MB RAM),
  same API surface as K8s — Juan's K8s skills transfer directly
- The "autonomous" requirement: edge nodes must operate correctly during WAN outages
  (self-healing), which requires local state estimation + local control (Juan's MPC
  analogy: MPC runs on the edge and doesn't need cloud connection to actuate)
- NATS vs. Kafka for edge: NATS offers sub-millisecond latency and runs in ~20 MB RAM —
  better for edge; Kafka is the backend aggregation layer

**Complexity:** HIGH | **Interview weight:** CRITICAL

---

## Differentiators (Depth Here Sets You Apart)

### 10. Federated Learning and Federated Data Pipelines

**What it is:**
Federated Learning (FL): model training without sharing raw data. Each node trains on
local data, sends only model weight updates (gradients) to an aggregator, which averages
them (FedAvg algorithm) and redistributes the improved global model. No raw grid
measurements leave the utility's fence. Privacy-preserving and latency-reducing.

Federated data pipelines (as in the JD) is a broader concept: any architecture where
distributed nodes collaborate on inference/control without a central coordinator. This
includes FL but also Byzantine-fault-tolerant consensus, gossip protocols, and
peer-to-peer state estimation.

**Why it matters for this role:**
JD explicitly requires "federated data pipelines that allow distributed nodes to
collaborate securely without central coordination." FL for energy forecasting, fault
detection, and state estimation is an active research area (2024-2026 publications).

**Bridge from Juan's work:**
Juan's OSED architecture already isolates data at the building level (GDPR-compliant edge
inference). The federated extension: instead of centralizing building data, each building
trains a local forecast model and shares only gradient updates. His Hydro-Québec Linux
Foundation Energy leadership also maps here — LF Energy's OpenSTEF (probabilistic
forecasting) and related projects use federated patterns.

**Differentiating depth:**
- FedAvg vs. FedProx: FedProx adds a proximal term to handle heterogeneous (non-IID) data
  across substations — critical for grids where each substation has very different load profiles
- Differential privacy: add calibrated noise to gradients before sharing, preventing
  inference attacks — important for utilities with competitive/sensitive data
- Communication efficiency: gradient compression, quantization, sparse updates — needed
  because edge nodes may have narrow-band LoRa or cellular uplinks
- Byzantine resilience: a compromised substation node could send malicious gradient
  updates; robust aggregation (coordinate-wise median, Krum algorithm) mitigates this

**Complexity:** HIGH | **Interview weight:** HIGH

---

### 11. Signal Processing for Grid Applications

**What it is:**
Key signal processing techniques applied to grid sensing:
- **Fourier / DFT:** PMUs use DFT to extract phasor from sampled waveform. Windowing
  matters (Hann window reduces spectral leakage for off-nominal frequency).
- **ROCOF (Rate of Change of Frequency):** dF/dt detection for islanding, generator
  trip events. Computed from PMU frequency measurements; sensitive to noise — requires
  filtering.
- **Harmonic analysis:** Inverter-based DERs inject harmonics. DFT up to order 50+
  characterizes Power Quality.
- **Kalman-based frequency estimation:** Track fundamental frequency + harmonics
  jointly as state variables — more robust than straight DFT in noisy conditions.
- **Wavelet transform:** Better for transient detection (fault onset) than DFT — localizes
  in both time and frequency.

**Why it matters for this role:**
JD requires "signal processing techniques (e.g., Kalman filters, state estimation)."
Understanding the signal chain from raw waveform to synchrophasor is essential for
debugging virtual sensors in the field.

**Bridge from Juan's work:**
Juan's OSED ingests timeseries data and applies ML models. The signal processing layer
(before ML) is analogous: in buildings, sensors produce noisy temperature/power readings
that need smoothing and anomaly rejection before the model sees them. The grid equivalent
is: raw ADC samples → anti-aliasing filter → DFT → phasor → state estimator.

**Differentiating depth:**
- IEEE C37.118.1 accuracy classes (P class for protection, M class for measurement)
  and what compliance means for algorithm design
- Event-based PMU: how to handle subsynchronous oscillations (0.1-2 Hz), a growing
  concern with high-inverter-penetration grids
- Interarea oscillations: low-frequency oscillations (~0.1-0.8 Hz) visible in phase
  angle timeseries — detected by Prony analysis or FFT of angle difference

**Complexity:** HIGH | **Interview weight:** MEDIUM-HIGH

---

### 12. Digital Twins for Grid — OpenFMB, Modelica, Graph-Based Modeling

**What it is:**
A grid digital twin is a synchronized virtual model of a physical grid asset or network,
updated in real time from sensor feeds, used for state estimation, what-if simulation, and
control validation.

- **OpenFMB (Open Field Message Bus):** NAESB standard (2016). Defines common data models
  derived from IEC 61850 and CIM (IEC 61968/61970) published over MQTT/NATS/DDS. The
  "language" for field devices to talk to each other in a decentralized architecture.
  Juan's most natural entry point: OpenFMB uses MQTT publish-subscribe — identical to
  his OSED broker pattern.
- **Modelica / OpenModelica:** Equation-based, acausal modeling language. Define
  differential-algebraic equations (DAEs) for physical systems; simulate automatically.
  Used for grid component models (transformer, line, generator) that feed the digital twin.
- **CIM (Common Information Model, IEC 61968/61970):** The industry-standard ontology for
  power system data. Graph-based (nodes = buses, edges = lines/transformers). Used in
  EMS/DMS for grid topology management.
- **Graph-based modeling:** Grid topology as a graph enables graph neural networks (GNNs)
  for state estimation and fault location — active research (2023-2026).

**Why it matters for this role:**
JD preferred qualifications list "OpenFMB, Modelica, or graph-based modeling." More
importantly, the "close the loop between simulation and live operations" responsibility
is exactly what digital twins enable.

**Bridge from Juan's work:**
Juan built SI-MAPPER (CV → ontology, ASHRAE 223P) and IoT knowledge graphs — this is
graph-based data modeling applied to buildings. CIM for power systems is the same
conceptual pattern: a graph ontology for grid assets. His MCP server work (IoT-as-context
for GenAI) maps to the "GenAI querying a grid CIM graph" use case that is emerging.

**Differentiating depth:**
- OpenFMB profiles: SwitchReadingProfile, BreakerReadingProfile, SolarInverterProfile —
  know the vocabulary well enough to discuss integration design
- FMI (Functional Mock-up Interface): standard for co-simulation between Modelica models
  and real-time control systems — enables "hardware in the loop" testing
- Graph neural networks for topology estimation: when grid topology changes (switching),
  GNN re-estimates state without re-running full state estimation from scratch

**Complexity:** HIGH | **Interview weight:** MEDIUM (preferred, not required)

---

### 13. IEC 61850 — Substation Communication Standard

**What it is:**
IEC 61850 is the international standard for substation automation and protection
communication. Three key services:
- **MMS (Manufacturing Message Specification):** TCP/IP-based, for SCADA client-server
  communication (reading/writing data from IEDs).
- **GOOSE (Generic Object Oriented Substation Events):** Ethernet multicast, < 3ms
  latency, for protection events (breaker trip, fault signal). Bypasses TCP/IP stack.
- **Sampled Values (SV/9-2):** High-speed streaming of current/voltage samples from
  merging units to protection IEDs. Replaces copper wiring with fiber Ethernet.

Data model: Logical Nodes (LN) represent functions (XCBR = circuit breaker,
MMXU = measurement unit). Devices are described in SCL (Substation Configuration
Language, XML).

**Why it matters for this role:**
The JD lists IEC 61850 as preferred knowledge. It is THE protocol for modern substation
IED integration. Any virtual sensing algorithm deployed at the substation level will
read from IEC 61850 data models and publish results via IEC 61850 or OpenFMB.

**Bridge from Juan's work:**
Juan has the IEC 61850-3 document in his project docs. His MQTT pub-sub expertise
transfers: GOOSE is essentially a low-latency multicast pub-sub optimized for protection
relay speeds. The data model hierarchy (Logical Device → Logical Node → Data Object →
Data Attribute) is analogous to the IoT device ontologies he works with.

**What to be able to say:**
- GOOSE vs. MMS: GOOSE for < 3ms protection events, MMS for SCADA-speed configuration
  and monitoring
- Why IEC 61850 matters for virtual sensing: the virtual sensor output must be published
  as a Logical Node (e.g., MMXU for measured quantities) so protection and SCADA systems
  can consume it without knowing it's virtual
- SCL files: CID/SCD/ICD files define IED capability and substation configuration —
  the "schema" for the substation digital twin

**Complexity:** MEDIUM | **Interview weight:** MEDIUM (preferred, not required)

---

### 14. Observability, Bad Data Detection, and Robust Estimation

**What it is:**
A grid is "observable" if the measurement set uniquely determines all state variables.
Observability analysis (via graph theory: network tree + measurement spanning) identifies
unobservable islands. Bad data detection uses the normalized residual test after WLS
convergence: `r_i = (z_i - h_i(x̂)) / sqrt(Ω_ii)`. If |r_i| > threshold (e.g., 3σ),
measurement i is flagged. Largest Normalized Residual (LNR) test identifies which
measurement to remove.

Robust estimation alternatives (LAV — Least Absolute Value, or M-estimators) are
inherently less sensitive to outliers than WLS.

**Why it matters for this role:**
Sparse edge sensor coverage means observability is always a design constraint. A virtual
sensing system must know where it is unobservable and flag low-confidence estimates.

**Bridge from Juan's work:**
Juan's building ML pipeline includes data quality checks (sensor drift detection,
outlier removal before model inference). Bad data detection in grid SE is the same
problem formalized: instead of ad-hoc outlier removal, it uses residual statistics.

**Complexity:** MEDIUM | **Interview weight:** MEDIUM-HIGH

---

## Awareness-Only (Know the Name + One Sentence)

### 15. IEEE 2030.5 (SEP 2.0)

Smart Energy Profile 2.0 — the protocol for utility-to-DER communication over
IP networks (used in California for residential DERMS). The counterpart to OpenADR for
two-way DER control. Juan's HEMS/DER work connects; he can say he knows OpenADR and that
IEEE 2030.5 is the complementary protocol for direct grid-to-DER control.

**Interview use:** "My HEMS work used OpenADR for demand response; IEEE 2030.5 extends
that to direct inverter control, which I understand conceptually and can dive into quickly."

---

### 16. EMT Simulation Tools (PSCAD, RTDS, Opal-RT)

Electromagnetic Transient (EMT) tools simulate power systems at microsecond timesteps to
study fast transients (switching, faults, inverter dynamics). PSCAD (Manitoba Hydro
Research), RTDS (Real-Time Digital Simulator), Opal-RT — hardware-in-the-loop platforms.
The JD lists these as preferred. They are for power systems engineers; Juan's role is
software/algorithms. Acknowledge familiarity, do not over-claim.

**Interview use:** "I know these are the simulation environments where virtual sensor
algorithms are validated before field deployment — my role would be to interface the
algorithm outputs, not necessarily to build the EMT models themselves."

---

### 17. Transmission System Operator (TSO) vs. Distribution System Operator (DSO)

TSOs operate the high-voltage (>100 kV) transmission backbone (e.g., Hydro-Québec
TransÉnergie). DSOs operate medium/low-voltage distribution (local utilities). FERC,
NERC CIP, and WECC reliability standards govern TSO operations. Juan's OSED work is DSO
side; this role spans both (line temperature → transmission, DER → distribution).

**Interview use:** One sentence acknowledging the distinction and that he's bridging from
DSO/DER (his background) to TSO virtual sensing (the role's scope).

---

### 18. Wide-Area Protection and Control (WAPC) / UVLS / UFLS

Under-Voltage Load Shedding (UVLS) and Under-Frequency Load Shedding (UFLS) are
last-resort protection schemes that automatically disconnect load to prevent cascade
collapse. Wide-area protection uses PMU data to make coordinated tripping decisions in
< 100ms. Virtual sensing of voltage stability directly feeds UVLS arming logic.

**Interview use:** One sentence: "A voltage stability virtual sensor directly feeds the
arming threshold for UVLS schemes — it's not just monitoring, it's in the protection
critical path."

---

### 19. Particle Filters and Ensemble Methods

For highly non-Gaussian or nonlinear systems, particle filters (Sequential Monte Carlo)
approximate the posterior distribution with a set of weighted particles. More
computationally expensive than UKF but handles multi-modal distributions. Used in
fault location problems where the fault could be at discrete locations.

**Interview use:** "I know the family: KF for linear-Gaussian, EKF/UKF for nonlinear,
particle filters for strongly non-Gaussian — and I'd choose UKF for most grid DSE
problems for the right balance of accuracy and computational cost."

---

### 20. Graph Neural Networks (GNNs) for Grid State Estimation

Emerging research area (2022-2026): model the grid as a graph, train a GNN on historical
PMU + SCADA data, use it for fast approximate state estimation. Faster than iterative
WLS, handles topology changes naturally. Not yet in production at scale.

**Interview use:** "I see GNNs as the next frontier for grid SE, especially with variable
topologies from switching operations — and my knowledge graph work gives me a natural
bridge to graph-structured models."

---

## Feature / Topic Dependencies

```
Power System State Estimation (WLS)
    ├──extends──> Kalman Filter (Dynamic SE, KF adds time dimension to WLS)
    │                ├──extends──> EKF (linearize nonlinear grid model)
    │                └──extends──> UKF (sigma points, no Jacobian)
    │                                  └──enables──> Particle Filter (non-Gaussian)
    ├──requires──> PMUs & Synchrophasors (the measurement source)
    │                └──requires──> Signal Processing (DFT → phasor extraction)
    ├──requires──> Observability Analysis (know where estimation is valid)
    │                └──requires──> Bad Data Detection (residual testing)
    └──produces──> Virtual Sensing Outputs:
                      ├── Voltage Stability Index (VSI)
                      ├── Phase Angle Inference
                      ├── Dynamic Line Rating (conductor temperature)
                      └── Asset Health Estimation

Edge Architecture
    ├──requires──> Grid Protocols (DNP3, LoRa, MQTT, IEC 61850, OpenFMB)
    ├──extends──> Federated Data Pipelines (decentralized without central coord)
    │                └──enhances──> Federated Learning (FL for model training)
    └──integrates──> Digital Twins (OpenFMB + Modelica + CIM graph)

[Juan's Existing Work] ──bridges──> [Grid Virtual Sensing]
    Building RC Thermal Model        ──> IEEE 738 Conductor Thermal Model (DLR)
    Building State Estimation (MPC)  ──> Grid DSE (EKF/UKF on PMU data)
    MQTT Pub-Sub (OSED)             ──> OpenFMB over MQTT (grid edge bus)
    HEMS / DER Control              ──> DER-Grid Interface (IEEE 2030.5, voltage support)
    Knowledge Graph (ASHRAE 223P)   ──> CIM Graph (IEC 61968/61970)
    Edge ML Inference               ──> Edge Asset Health Estimation
    DLMP / Flexibility Markets      ──> Congestion signals (phase angle differences)
    Convex Optimization             ──> DC OPF, voltage stability margin optimization
```

---

## Study Priority Matrix

| Topic | Interview Weight | Juan's Current Gap | Study Priority |
|-------|----------------|--------------------|----------------|
| State Estimation (WLS) | CRITICAL | Low (has LS) | P1 — 2 hrs to connect dots |
| Kalman Filter / EKF / UKF | CRITICAL | HIGH (named gap) | P1 — needs hands-on |
| PMUs & Synchrophasors | HIGH | MEDIUM | P1 — 1 hr reading |
| Voltage Stability / VSI | HIGH | HIGH (T&D gap) | P1 — needs grid context |
| Phase Angle Inference | HIGH | MEDIUM | P1 — leverages WLS |
| Dynamic Line Rating | HIGH | HIGH (T&D gap) | P1 — great bridge story |
| Asset Health Estimation | HIGH | LOW (has edge ML) | P2 — quick apply |
| SCADA / DNP3 / LoRa | HIGH | MEDIUM (has Modbus/MQTT) | P2 — 1 hr protocol reading |
| Edge Architecture | CRITICAL | LOW (has K8s/OSED) | P1 — reframe existing |
| Federated Learning | HIGH | MEDIUM | P2 — conceptual + FedAvg |
| Signal Processing (grid) | MEDIUM-HIGH | MEDIUM | P2 — connect to PMU |
| Digital Twins / OpenFMB | MEDIUM | LOW (has knowledge graphs) | P2 — reframe |
| IEC 61850 | MEDIUM | LOW (has docs) | P2 — read the doc |
| Observability / Bad Data | MEDIUM-HIGH | LOW | P2 — 1 hr reading |
| IEEE 2030.5 | LOW | LOW | P3 — one sentence |
| EMT Tools | LOW | HIGH | P3 — awareness only |
| TSO vs. DSO | LOW | LOW | P3 — one sentence |
| WAPC / UVLS / UFLS | LOW | HIGH | P3 — awareness only |
| Particle Filters | LOW | MEDIUM | P3 — taxonomy |
| GNNs for SE | LOW | LOW (has GNNs) | P3 — mention as frontier |

**P1 = Study before anything else (days 1-2)**
**P2 = Study after P1 is solid (days 3-4)**
**P3 = Skim enough to name and sentence (day 5)**

---

## Anti-Topics (Do Not Over-Invest)

| Topic | Why Not | What to Say Instead |
|-------|---------|---------------------|
| EMT tool hands-on (PSCAD/RTDS) | Preferred-only, out-of-scope per PROJECT.md | "I understand these are the validation environments; I interface with the output, not the model itself" |
| Protection relay engineering | Not in JD; deep EE specialization | Mention GOOSE for protection communication context only |
| Electricity market / LMP depth | Juan has DLMP research — already strong | Don't go deeper; it's a strength, not a gap |
| NERC CIP compliance detail | Utility compliance, not engineer scope | "I'm aware of the cybersecurity requirements that shape federated pipeline design" |
| Go / Rust language | PROJECT.md: Python already qualifies | One sentence only |
| Distribution grid modeling depth | The role is T&D but emphasis is edge algorithms, not power flow modeling for distribution planning | Keep at awareness level |

---

## Sources

- GE Vernova Job Description R5043890 (docs/job-requirements.md)
- ArXiv: "Power System Dynamic State Estimation Using Extended and Unscented Kalman Filters" (2020) — https://arxiv.org/pdf/2012.06069
- ScienceDirect: "State estimation of Active Distribution Networks: Comparison between WLS and iterated Kalman-filter" (ResearchGate confirmed)
- IEEE C37.118.1: Standard for Synchrophasor Measurements — confirmed via Wikipedia/tutorialspoint
- IEEE 738: Standard for Calculating the Current-Temperature Relationship of Bare Overhead Conductors
- WATT-Transmission DLR Review (2018): https://watt-transmission.org/wp-content/uploads/2018/09/1-2018-karimi-musilek-knight.pdf
- ScienceDirect: "Parameter estimation of resistor-capacitor models for building thermal dynamics using UKF" (2019)
- ORNL: "Microgrid Communications Using OpenFMB" — https://www.ornl.gov/publication/microgrid-communications-using-open-source-open-field-message-bus-openfmb-framework
- Nature Communications Engineering: "Data-driven and privacy-preserving risk assessment based on federated learning for smart grids" (2024)
- GE Vernova WAMS product page: https://www.gevernova.com/software/products/gridos/wide-area-management-system
- Synadia: "NATS and Kafka Compared" — https://www.synadia.com/blog/nats-and-kafka-compared
- FlowFuse: "MQTT vs Kafka: Complete Comparison Guide 2026" — https://flowfuse.com/blog/2025/12/kafka-vs-mqtt/

---

*Knowledge domain map for: GE Vernova Senior SE&S — Virtual Sensing & Decentralized Grid Operations*
*Researched: 2026-06-13*
