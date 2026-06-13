# Inter-Area Oscill Damp

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Inter-Area_Oscillation_Damping.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - Inter-Area Oscillation Damping

## Contents

* [Narrative](TO_Inter-Area_Oscillation_Damping.htm#Narrative)
* [Steps](TO_Inter-Area_Oscillation_Damping.htm#Steps)

## Narrative

Low frequency Inter-area oscillations are
detrimental to the goals of maximum power transfer and optimal power
flow. An available solution to this problem is the addition of power
system stabilizers to the automatic voltage regulators on the
generators. The damping provided by this technique provides a means to
minimize the effects of the oscillations.

Inter-Area oscillations result from system
events coupled with a poorly damped electric power system. The
oscillations are observed in the large system with groups of
generators, or generating plants connected by relatively weak tie
lines. The low frequency modes (0.1 to 0.8 Hz) are found to involve
groups of generators, or generating plants, on one side of the tie
oscillating against groups of generators on the other side of the tie.
These oscillations are undesirable as they result in sub-optimal power
flows and inefficient operation of the grid.  The stability of these
oscillations is of vital concern.

Although Power System Stabilizers exist on many
generators, there effect is only on the local area and do not
effectively damp out inter-area oscillations.  It can be shown that
the inter-area oscillations can be detected through the analysis of
phasor measurement units (Phasor Measurement Unit) located around the
system.  In a typical implementation, one or more of the generators in
a system are selected as Remote Feedback Controllers (RFC
Controller).  The RFC Controller received synchronized phasor
measurements from one or more remote phasor sources.  The RFC
Controller analysis the phase angles from the multiple sites and
determines if an inter-area oscillation exists.  If an oscillation
exists, a control signal is sent to the generator’s voltage regulator
that effectively modulates the voltage and effectively damps out the
oscillations.

To overcome the inter-area oscillation, new
equipment such as Static Var Compensator (SVC) and various Flexible AC
Transmission System (FACTS Device) devices, are being increasingly
used. These techniques have become possible due to the recent
advancement in power electronic technology. The involvement of SVC and
FACTS Device in transmission network is through the so-called Variable
Series Compensation (VSC Controller). Besides the FACTS Device
devices, the application of Super-Conducting Magnetic Storage (SMES
Device) to enhance the inter-area oscillation damping is also
reported.

The key to coordinate RFC Controller, VSC
Controller and various controllers is the using of Phasor Measurement
Unit synchronized with the Global Positioning Satellite (GPS).

The natural frequency and damping of the
inter-area mode depends on the weakness of the tie and on the power
transferred through the tie. The action of a dc link, parallel to the
ac tie, is to strengthen the tie. Connection of two areas, through a
dc link alone, does not introduce an inter-area mode owing to the
asynchronous nature of a dc tie. Therefore, the inter-area instability
is avoided. Indeed,  that is one of the reasons for the growth of dc
links.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Any power system state | Send Phasor Measurement | At all times, the PMUs in the field shall synchronously send phasors to the RFC Controller and VSC Controller. | Phasor Measurement Unit | RFC Controller, VSC Controller | Synchro Phasor | Synchro phasors  must be received at a rate of up to 60 phasors per second.  Security is not crucial, however, data integrity is paramount, i.e., no faulty data shall be accepted. | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2 | Power system disturbance (e.g. fault) | Coordinate Global Control | PMUs continue to send phasor data.  Upon detection of df/dt >   e, trigger a storage local storage event; RFCs continue to synchronously receive phasor data and also detect the system event; The RFC Controller/VSCs, upon detection of the event, will trigger local data storage and coordinate the control action in order to counteract the detected inter-area oscillations. |  |  |  | The communication requirements differ from algorithm to algorithm. For the decentralized control, the system is decoupled with known system states. | NA |
| 1.3A | New control calculate | Generator Voltage Control | The RFC Controller, having detected an inter-area oscillation and having computed an appropriate control action, sends the control information to the voltage regulator | RFC Controller | AVR Controller | Controller Settings | Voltage regulator control information shall be issued at the same rate as the synchro voltage receive rate | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3B | New control calculate | FACTS Device Control | The VSC Controller, having detected an inter-area oscillation and having computed an appropriate control action, sends the control information to the FACTS Device system | VSC Controller | FACTS Device | Controller Settings |  | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 1.3C | New control calculate | SMES Device  Control | The SMES Device SMES Controller, having detected an inter-area oscillation and having computed an appropriate control action, sends the control information to the FACTS Device system | SMES Device SMES Controller | SMES Device | Controller Settings |  | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
