# Overview of Functions

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/Fun_Functions_Overview.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Power System Functions

As part of the initial scoping activity of IntelliGrid Architecture project, over 400 power system functions were identified and briefly
assessed for their information exchange needs and issues. After these 400
functions were reviewed, a few of them were selected as key functions for more
in-depth analysis.

The power system experts within IntelliGrid Architecture team
and a number of stakeholders outside IntelliGrid Architecture team developed detailed
descriptions of these key existing and future power system operation functions,
which were considered ‘architecturally significant’ in terms of having unique
and/or complex information requirements. These functions were captured in narratives,
diagrams, and detailed steps, using the concepts of the Unified Modeling
Language™ (UML™[[6]](Fun_Functions_Overview.htm#_ftn6))
which is the prevalent method for capturing and expressing the complex
interactions of functions.

To achieve this first deliverable, IntelliGrid Architecture
team created a list of all functions related to power system operations. This
covered six ‘Domain Areas’ including: (1) Market Operations, (2) Transmission
Operations, (3) Distribution Operations, (4) High Voltage Generation, (5) Distributed
Energy Resources, and (6) Customer Services. Ultimately, more than 400
functions were identified at the very top levels. These functions were then
assessed for key architectural issues, such as unique configuration
requirements, stringent quality of service requirements, strong security
requirements, and complex data management requirements. From these functions, a
few key functions were selected, analyzed and evaluated in more depth, in order
to understand the architecturally significant requirements in greater detail. Table 2 lists the power system
operations functions that were analyzed in greater depth (see the Website and
Volume II for more complete descriptions):

Table 2: List of Power System Applications
analyzed in some detail

Some power system
functions were thought to expose architecturally significant issues and were
examined in more detail than others.

**1.****Market
Operations**

a.    Long Term Planning (Transmission and
generation maintenance coordination, updating the power system model)

b.    Medium/Short Term Planning (Load forecast,
outage scheduling, congestion management, long-term auction/sale of FTRs)

c.    Day Ahead Market (Auction/sale of FTRs, day
ahead submittal of energy schedules, day ahead submittal of ancillary service
bids, schedule adjustment of energy schedules, schedule adjustment of
ancillary services)

d.    Real-Time (Operational calculations, real
time submittal of schedules, real time submittal of ancillary services,
normal dispatch re-dispatch/emergency dispatch)

e.    Post-Dispatch (Metering, market products
schedule checkout, financial settlements, accounting and billing, market
monitoring and auditing, transmission and generation maintenance
coordination, updating the power system model, transmission operations)

 

**2.****Transmission
Operations**

a.    Automated Control Baseline

b.    Emergency Operations Baseline

c.    Wide Area Monitoring and Control Automated
Control

d.    Wide Area Monitoring and Control Emergency
Operations

e.    Wide Area Monitoring and Control Advanced
Auto Restoration

f.      Advanced Auto Reclosing

g.    Synchrophasor

h.    Voltage Security

i.      Transmission System
Contingency Analysis (Baseline)

j.      Transmission System
Contingency Analysis (Future)

k.    Self-Healing Grid (across both transmission
and distribution)

 

**3.****Distribution
Operations (includes significant penetration of** **DER****in distribution system)**

a.       Data Acquisition and
Control (DAC)

b.       Distribution Operation
Modeling and Analysis (DOMA)

c.       Fault Location, Isolation
and Service Restoration (FLIR)

d.       Distribution System
Contingency Analysis (CA)

e.       Multi-level Feeder
Reconfiguration (MFR)

f.        Relay Protection
Re-coordination (RPR)

g.       Voltage and Var Control (VVC)

h.       Pre-arming of Remedial
Action Schemes (RAS)

i.        Coordination of Emergency
Actions

j.        Coordination of
Restorative Actions

k.       Intelligent Alarm
Processing

 

**4.****Distribution
Operations (includes significant penetration of** **DER****in distribution system)**

a.       DER as Backup

b.       DER Operated by Aggregator

 

**5.****Consumer
Services)**

a.       Real time pricing (RTP)

b.       Power quality monitoring
(PQ)

c.       Customer communication
portal (CCP)
