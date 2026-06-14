# STK-01: Grid Protocol Stack — Field-to-Cloud Tier Map

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Place every named grid protocol in the correct field-to-cloud tier with one
distinguishing property each — so you can navigate the protocol stack in conversation and
never confuse SCADA with DNP3 or LoRa with MQTT.

---

> **Depth strategy:** FULL depth for **DNP3 vs. Modbus** and the **PMU / IEEE C37.118**
> reporting-rate detail — these are the most likely interview probes. **Awareness only** for
> IEC 61850 internals (that's STK-02) and LoRa RF engineering (CLAUDE.md "What NOT to
> Over-Invest In"). SCADA/OPC-UA gets one conceptual paragraph — you'll elaborate if asked.

---

## 1. The Field-to-Cloud Mental Model

Every grid protocol lives in a tier. The interviewer is not just asking "what is DNP3?" —
they are asking "where does it live and what problem does it solve that nothing else at
that tier solves?" Protocols exist because different tiers have fundamentally different
constraints: a protection relay needs a deterministic sub-4 ms signal that never touches
IP routing; a field RTU needs to push timestamp-stamped events to a SCADA master without
being polled; a wide-area sensor on a pole-top needs to run on battery for 10 years.
Protocols are the shape of those constraints. Know the tier, know the constraint, know
the one property — and you own the conversation.

---

## 2. The Tier Map

| Protocol | Field-to-Cloud Tier | One Key Property | Transport |
|----------|---------------------|-----------------|-----------|
| **SCADA + OPC-UA** | Station level → cloud / control center | RTUs/IEDs aggregate field data; OPC-UA is the integration API bridging SCADA to historians and analytics | TCP/IP |
| **DNP3** | Field → station (RTU/IED to SCADA master) | **Millisecond timestamps on every data point** + unsolicited reporting (RTU pushes on change — no polling) | Serial or TCP/IP |
| **PMU / IEEE C37.118** | Field → regional / cloud (via PDC) | **GPS-synchronized phasors at 10–120 frames/sec** (30/60 common for 60 Hz); enables wide-area state estimation | TCP/IP (streaming) |
| **IEC 61850** | Process bus (GOOSE/SV) and station bus (MMS) | GOOSE <4 ms L2 protection trips; SV = digitized I/V on process bus; MMS = client-server SCADA supervision | L2 Ethernet (GOOSE/SV); TCP/IP (MMS) |
| **LoRa / LoRaWAN** | Field → wide-area (cloud via network server) | **2–15 km range on battery power (5–10 years)**; star-of-stars topology; 0.3–50 kbps | LoRa RF → gateway → TCP |
| **MQTT** | Field → edge broker (device-to-broker) | Lightweight pub/sub; QoS 0/1/2; star topology through broker; **no native timestamping** | TCP/IP |

---

## 3. IEEE C37.118 Reporting-Rate Detail

IEEE C37.118 is the communication standard for synchrophasor (PMU) data. Required baseline
for 60 Hz power systems: **10, 30, or 60 frames per second** (user-selectable). Higher
rates — **120 fps** — are encouraged and common in high-resolution Wide-Area Monitoring
System (WAMS) applications. Every frame carries a **GPS-derived timestamp**, which is what
makes cross-system phase comparison possible: two PMUs on opposite ends of a 500 kV line,
synchronized to UTC, can have their phasors compared to microsecond accuracy. That GPS
lock is what enables the Kalman-based wide-area state estimation the role names.

**One-liner:** "C37.118 is the language PMUs speak — GPS-synchronized phasors at 10–120
frames/sec, TCP streaming to a Phasor Data Concentrator (PDC), enabling wide-area state
estimation at a resolution no SCADA poll can match."

---

## 4. DNP3 vs. Modbus — The Distinction That Powers the Bridge

Modbus was designed in 1979 for industrial automation: simple, poll-only, no timestamps.
DNP3 was designed in the 1990s specifically for the electric utility industry — it adds
three things Modbus does not have:

1. **Millisecond timestamps on every data object.** When an RTU reads an analog input or
   a binary status, the value is packaged with the exact millisecond it was observed. This
   is non-negotiable for post-event analysis and grid protection coordination.

2. **Unsolicited reporting.** An RTU running DNP3 can be configured to push a report to
   the SCADA master the moment a value changes (or crosses a threshold), without waiting to
   be polled. Modbus is poll-only — the master must ask; the slave never volunteers.

3. **Three-layer architecture + DNP3 SAv5.** DNP3 uses a proper application/transport/
   data-link stack (vs. Modbus's simple two-layer) and DNP3 Secure Authentication version 5
   (SAv5) for authenticated communications — critical in utility SCADA where an unauthenticated
   command could open a breaker.

| Dimension | Modbus (Juan has) | DNP3 (gap) |
|-----------|-------------------|------------|
| Origin | Industrial automation (1979) | Electric utility (1990s) |
| Timestamping | No native timestamps | Millisecond timestamps on every data point |
| Reporting mode | Poll-only | Unsolicited reporting + polling |
| Architecture | Two-layer (app/data-link) | Three-layer (app/transport/data-link) |
| Security | None native | DNP3 SAv5 (Secure Authentication v5) |
| Transport | Serial, Ethernet | Serial, TCP/IP, UDP |
| Primary use | PLC/SCADA in industrial | RTU/IED to SCADA master in utility |

---

## <3-min say-aloud version

> "Let me walk the stack bottom to top.
>
> At the bottom, the **field tier**. Two protocols own protection: **IEC 61850 GOOSE and SV**,
> both running Layer-2 Ethernet — they never touch IP routing because they cannot afford to.
> GOOSE delivers a protection trip in **<4 ms**; SV streams digitized current and voltage from
> merging units to protection relays. Both stay inside the substation LAN.
>
> Also in the field tier, **DNP3** — the RTU-to-SCADA workhorse for utility telemetry. Its key
> property: **millisecond timestamps on every data point** and unsolicited reporting, so the RTU
> pushes on change rather than waiting to be polled. That's what makes post-event replay possible.
>
> **PMUs** also live at the field tier, speaking **IEEE C37.118** — GPS-synchronized phasors at
> 10–120 frames per second. Those go to a Phasor Data Concentrator, then to a Wide-Area Monitoring
> System in the cloud. The GPS lock is what lets you compare phase angles across thousands of
> kilometers.
>
> On the wide-area sensing side: **LoRa/LoRaWAN** — 2 to 15 km on battery power for 5 to 10 years,
> star-of-stars topology, 0.3 to 50 kbps. This is for pole-top sensors, fault indicators in rural
> areas, or distribution sensors where you cannot justify fiber or cellular.
>
> Moving up, **MQTT** lives at the device-to-edge-broker tier — lightweight pub/sub, QoS 0/1/2,
> star topology through a broker. No native timestamping; that's my world from OSED.
>
> At the top, **SCADA + OPC-UA**. SCADA aggregates RTU/IED data and provides the operator HMI.
> OPC-UA is the integration API — the bridge from SCADA to historians like OSIsoft PI and to
> analytics pipelines. All over TCP/IP."

---

## → Bridge to your work

> **Two bridges from the CLAUDE.md Summary Reference Table — the exact reframes to use:**
>
> **Bridge 1: Modbus → DNP3**
> "I've used Modbus in production (OSED building automation, HVAC, RTUs). Modbus is polling with
> no timestamps — fine for a controlled environment where you own the polling schedule and latency
> doesn't matter. DNP3 adds the two things Modbus lacks for utility applications: millisecond
> timestamps on every reading, and unsolicited push so the RTU reports on change. It's the same
> register model, but with the timestamp and event discipline utilities require for SCADA and
> post-event reconstruction."
>
> **Bridge 2: Zigbee → LoRa**
> "I've deployed Zigbee in building automation (OSED/HEMS). Zigbee is 250 kbps mesh at 10–100 m
> — perfect indoors. LoRa/LoRaWAN is 0.3–50 kbps star-of-stars at 2–15 km on a battery that lasts
> 10 years — the use case is completely different: pole-top fault indicators, distribution sensors
> in rural areas that don't justify fiber. Same IoT instinct, different constraint set."

| Juan's experience | Grid equivalent | What changes |
|-------------------|----------------|-------------|
| Modbus (industrial RTUs, OSED) | **DNP3** | Add millisecond timestamps + unsolicited push; DNP3 SAv5 for auth |
| Zigbee (HEMS, building automation) | **LoRa/LoRaWAN** | Km-range, years-on-battery, star-of-stars instead of 100 m mesh |

**How to say this in the interview:**

> "I've built with Modbus and Zigbee in production. DNP3 is the utility evolution of Modbus —
> same register-based telemetry idea, but with millisecond timestamps and unsolicited reporting
> so the RTU pushes on change instead of being polled. And LoRa is the km-range, battery-class
> cousin of Zigbee — same IoT instinct, completely different physical constraint. The upgrade
> path from my stack to the utility field stack is a clear step, not a rethink."

---

## Quick-Recall Card (Recite Before the Interview)

1. **SCADA + OPC-UA** — station level to cloud; RTUs/IEDs aggregate, OPC-UA bridges to historians; TCP/IP.
2. **DNP3** — field to SCADA master; **millisecond timestamps** + **unsolicited push**; Serial or TCP/IP.
3. **PMU / IEEE C37.118** — field to cloud via PDC; **GPS-synced phasors at 10–120 fps**; TCP/IP streaming.
4. **IEC 61850** — process bus (GOOSE/SV Layer 2, <4 ms) + station bus (MMS TCP/IP); see STK-02 for internals.
5. **LoRa/LoRaWAN** — field to wide-area cloud; **2–15 km, 5–10 yr battery**; LoRa RF → gateway → TCP.
6. **MQTT** — device to edge broker; lightweight pub/sub; no native timestamps; my background.
7. **DNP3 vs Modbus:** Modbus = poll-only, no timestamps. DNP3 = millisecond timestamps + unsolicited push + DNP3 SAv5 auth.
8. **C37.118 detail:** 10/30/60 fps baseline; 120 fps for WAMS; GPS timestamp on every frame.
9. **My bridge:** Modbus → DNP3 (timestamps + push), Zigbee → LoRa (km-range, battery, star-of-stars).

---

*Sources: CLAUDE.md "Category 3: Grid Protocols" (SCADA, DNP3 vs Modbus table, PMU/C37.118, IEC 61850, LoRa/Zigbee table) and "Summary Reference Table" (bridge raw material); IEEE C37.118 (synchrophasor standard — baseline reporting rates, GPS synchronization); DNP3 (IEC 60870-5 derivative — three-layer architecture, SAv5); IEC 61850 (GOOSE/SV Layer 2, MMS TCP/IP); CV (Modbus in OSED building automation, Zigbee in HEMS/building intelligence).*
