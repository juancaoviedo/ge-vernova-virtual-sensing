# EXTRACTION — Original AGMS Patent Text (OCR)

**Method:** the six `docs/patent-*.pdf` are image-only (0 text layer). OCR'd with
`ocrmypdf --force-ocr` (Tesseract 5.3) → sidecar text in `ocr/`. Quotes below are verbatim
from that OCR (minor OCR noise preserved; `[sic]`/`[≈]` where obvious). Page numbers are
the **PDF page** of each patent. Numbers like `[0019]` / `(23)` are the patent's own
paragraph/clause markers.

---

## A. Scope & applicability — transmission vs distribution

**A1 — Parent, FIG. 1 (adaptive-power · p.1, abstract page).** The system diagram labels
include **"TRANSMISSION & DER & GRID…"**, **"HVDC"**, **"Digital Sub[station]"**,
**"DR/DER/EV [aggregators]"**, **"VIRTUAL POWER PLANT"**, and the field layer of
**"FIELD AGENT [devices]"** / **"CONTROL CELL"**. The whole-grid spread (transmission +
HVDC + DER + field cells) is on the very first figure.

**A2 — Parent ¶[0019] (adaptive-power · p.6).**
> "The grid operation data center 110 may comprise **a transmission and distribution
> management system, a distributed energy resource (DER) and renewable management system**,
> a grid visibility and insight system, a historian system, and a grid devices and asset
> services system communicating over an applications collaboration and integration platform."

**A3 — Parent ¶[0019]–[0020] (adaptive-power · p.7).**
> "System operators 150 may include external systems such as systems associated with the
> power market, **an electric power transmission system operator (TSO), an independent system
> operator (ISO), and a distributed system operator (DSO)**. The adaptive grid management
> system 140 may **aggregate data from the system operators 150**, the grid operation data
> center 110, and the enterprise data center 120 … further aggregate data from cloud services
> 130 …, **virtual power plants 180, and demand response/distributed energy response/electric
> vehicle (DR/DER/EV) aggregators 160** that aggregate power usage information."

**A4 — Parent ¶[0051] (adaptive-power · p.21).**
> "The grid operation data center 410 may comprise **a transmission and distribution
> management system, a DER and renewable management system**, a grid visibility and insight
> system, a historian system, a grid device and asset services system, and security services
> system. … The enterprise data center may comprise enterprise applications and services,
> **DR/DER/EV aggregators, virtual power plant systems**, and other external data and alerts.
> **The grid system operators 425 may comprise transmission system operators and distribution
> system operators.** The market function systems 426 may comprise energy market systems…"

**A5 — Parent clause [00100] (adaptive-power · p.43).**
> "…the one or more devices includes field agent devices associated with one or more of **a
> power plant, a solar farm, a windfarm, a digital substation, a microgrid controller, and an
> electric vehicle [charging station]**."

**A6 — Operation Loop (GRANTED) ¶ (operation-loop · p.4).**
> "…the field agent devices 170 may be geographically distributed and each associated with a
> component or sub-system of the power grid such as **a windfarm, a digital substation, a solar
> farm, a power bank, an electric vehicle (EV) charging station, a [microgrid] controller**, and
> the like."

**A7 — Operation Loop (GRANTED) ¶ (operation-loop · p.11).** Repeats A2/A4 verbatim:
"a transmission and distribution management system, a DER and renewable management system…"
and "The grid system operators 425 may comprise **transmission system operators and
distribution system operators**."

**A8 — Operation Loop (GRANTED) ¶ (operation-loop · p.16).**
> "In some embodiments, **an operating cell may comprise a microgrid or a substation**."

**A9 — Operation Loop (GRANTED) clause (160) (operation-loop · p.31).**
> "…the plurality of assets includes field agent devices associated with one or more of **a
> power grid controller, a power grid substation, a microgrid controller, a power plant, a
> solar farm, a windfarm, and an electric vehicle charging station**."

*Corroboration:* the phrases "transmission and distribution [management system]," "DER and
renewable [management system]," "transmission system operator," and "distribution system
operator" appear in **all of** adaptive-power, asset-portfolio, data-management, and
operation-loop sidecars (grep-confirmed).

---

## B. The ORACS operation loop is defined in DER terms (the DERMS bridge)

**B1 — ORACS definition (operation-loop GRANTED · p.23; identical in asset-portfolio · p.46,
data-management · p.44, logistician-module · p.23).**
> "In some embodiments, **an ORACS operation loop may be defined by level of
> operability/functionalities (observability, device/DER Reachability, adaptability to legacy
> devices, controllability/dispatchability of DERs/microgrid, and security inside the operation
> loop)**."

This is the authoritative expansion of the five ORACS indexes in the original text:
- **O** = observability
- **R** = **device / DER reachability**
- **A** = **adaptability to legacy devices**
- **C** = **controllability / dispatchability of DERs / microgrid**
- **S** = security inside the operation loop

So **DER/microgrid dispatch is built into AGMS's atomic execution unit**, not bolted on.

---

## C. The DER management system is a *subsystem AGMS sits above*

From A2/A4/A7: the **"DER and renewable management system"** (i.e., a DERMS) is listed as
**one component inside the grid operation data center**, peer to the "transmission and
distribution management system," "historian," and "grid device & asset services system."
The **adaptive grid management system** (140/430) is a *separate, higher* element that
**couples to** the grid operation data center and **aggregates data from** it, the system
operators (TSO/ISO/DSO), the enterprise data center, cloud services, **VPP systems**, and
**DR/DER/EV aggregators** (A3/A4). I.e., per the patent's own architecture, the DERMS is a
data/management subsystem; AGMS is the cross-domain orchestration layer over it.

---

## D. What the patents do NOT say (honest negative findings)

Grep across all OCR'd sidecars (adaptive-power, asset-portfolio, data-management,
logistician-module, operation-loop) returns **zero** occurrences of the concrete
power-engineering / DERMS-control vocabulary one might expect:

- **none:** "voltage", "Volt/VAR", "reactive power", "power factor", "capacitor",
  "recloser", "frequency", "load shed", "islanding", "self-healing", "restoration",
  "FLISR", "SCADA", "PMU", "state estimation".
- "VAR" hits are all **"various / variance / variety / variable"** (not volt-amperes-reactive).
- "breaker" appears ~1× in two patents only.

The patents stay at a deliberately **domain-generic** abstraction: "managing a **network of
devices**," "a power grid **component and/or subsystem**," scouts/CaCSM/formation/operating
cells. The only concrete grid nouns are the *asset types* (power plant, solar/wind farm,
digital substation, microgrid controller, EV charging station, HVDC, power bank) and the
*enterprise systems* (T&D management system, DER & renewable management system, historian,
VPP, DR/DER/EV aggregators, TSO/ISO/DSO).

**Implication:** specific DER control functions (Volt/VAR, reactive-power dispatch, FLISR)
are **domain interpretation**, not patent text. The patent's DER coupling is at the
architectural level (ORACS dispatchability of DERs/microgrid; DERMS-as-subsystem), not at
the control-algorithm level.

---

## E. Source files

OCR sidecars (not committed; regenerable): `ocr/{adaptive-power,asset-portfolio,
data-management,logistician-module,operation-loop,scout-command}.txt`. Originals:
`docs/patent-*.pdf` (image-only).
