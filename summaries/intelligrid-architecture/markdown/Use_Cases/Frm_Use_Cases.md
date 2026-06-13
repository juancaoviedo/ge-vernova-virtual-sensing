# Frame of Use Cases

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/Frm_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# List of Enterprise Activities

## Market Operations Domain

1.     
Long Term System Planning (1 month to 5 years for new construction)

a.     
RTO/ISO update the system-wide power system model

b.     
RTO/ISO certify generation units

c.     
RTO/ISO analyze generation market for capacity and adequacy to meet
long term load

d.     
RTO/ISO coordinate long term transmission and generation maintenance

e.     
RTO/ISO register and perform credit rating of Market Participants
(MPs)

f.      
RTO/ISO register meters

2.     
Medium/Short Term Planning (Week ahead to months ahead for installing
equipment)

a.     
RTO/ISO/TransCos/DisCos forecast load

b.     
TransCos/GenCos propose scheduled transmission and generation outages

c.     
RTO/ISO perform congestion management and security analysis on
proposed outages

d.     
RTO/ISO auction/sell long term transmission rights and other energy
services to Market Participants

e.     
Market Participants enter into bilateral energy contracts

3.     Day
Ahead Market (24 hours to 48 hours ahead)

a.     
RTO/ISO auction/sell short term transmission rights and other energy
services to Market Participants

b.     
Market Participants submit Day-Ahead energy schedules

c.     
Market Participants submit Day-Ahead bids for ancillary services:
reserve, regulation, frequency response, etc.

d.     
RTO/ISO perform bid/auction management

e.     
RTO/ISO perform congestion management and security analysis on
submitted energy schedules

f.      
RTO/ISO calculate operational parameters for Day-Ahead planning:
Available Transmission Capacity (ATC), Regulated Must Run (RMR),
Locational Marginal Price (LMP)

g.     
RTO/ISO provide information to Market Participants

·      
Provide mandated and other energy information to Market
Participants

·      
Disclose environmental information

·      
Publish notifications

4.     
Real-Time (actual time to next hour)

a.     
Calculate operational parameters in real-time

b.     
Market Participants submit adjustments to real-time energy schedules

c.     
Market Participants submit real-time bids for ancillary services

d.     
RTO/ISO dispatch generation power system under normal conditions:

·      
RTO/ISO SCADA system monitors power system

·      
RTO/ISO EMS system performs Automatic Generation Control
(AGC)

·      
RTO/ISO Market Operations system analyzes transmission
capacity and reliability

·      
RTO/ISO Market Operations system balances
energy/ancillary services

·      
RTO/ISO EMS system monitors interchange schedules with
internal and external Control Areas

e.     
RTO/ISO exchange information with external entities:

·      
RTO/ISO Market Operations system coordinates operational
activities with distribution operations of interconnected UDCs

·      
RTO/ISO Market Operations system coordinates operational
activities with Reliability Councils and NERC

·      
RTO/ISO Market Operations system coordinates operational
activities with Market Participants

f.      
RTO/ISO redispatch/emergency dispatch

·      
RTO/ISO EMS system redispatches generation to handle
emergency

·      
RTO/ISO Market Operations system notifies Market
Participants of redispatch

·      
RTO/ISO Market Operations system manages market external
price caps

5.     
Post-Dispatch (last hour to prior months)

a.     
Handle energy reporting

·      
RTO/ISO Market Operations system calculates actual
interchange information and energy schedules

·      
RTO/ISO Market Operations system calculates actual
Locational Marginal Pricing (LMP)

·      
RTO/ISO Market Operations system calculates actual
losses

·      
Meter Data Management Agents (MDMAs) process meter
revenue data

b.     
Market Products Schedule Checkout

·      
Settlement Agents validate implemented energy schedules
against contracted energy schedules

·      
Settlement Agents reconcile differences

c.     
Financial Settlements

·      
Settlement Agents reconcile RTO/ISO market

·      
Settlement Agents reconcile transmission market

·      
Settlement Agents reconcile Market Participants spot
market

·      
Settlement Agents resolve disputes

·      
Market Participants reconcile bilateral schedules

d.     
Accounting and Billing

·      
Accounting Agents create budget and financial forecast

·      
Accounting Agents manage accounts payable

·      
Accounting Agents manage accounts receivable

e.     
Market Monitoring and Auditing

·      
Regulators and auditors develop monitoring criteria

·      
Auditors perform market assessment

·      
Auditors investigate market abuse

·      
Regulators monitor environmental statistics

## Transmission Operations Functions

1.   Long term transmission planning (1 year to 5
years ahead)

a.        Long term load forecast

b.        Forecast alternatives for generation
sources (Probable market conditions)

c.        Plan transmission upgrades and
additions (participation in ISO/RTO expansion plan)

d.        Plan automation of transmission system
for SCADA, Equipment Monitoring, and EMS

e.        Prepare long-term contracts with
Distribution Utilities:

·   
Transmission voltage management

·   
Distribution reactive power support (power factor) in the D-T
interface

·    T&D
information exchange

f.         Prepare emergency response planning,
e.g. Ice Storm, Hurricane, Catastrophic outages

g.        Ensure hard copies of all schematics,
diagrams, relay settings are available

h.        Prepare inventory and personnel plans
based on neighboring load, tie point capacity, etc.

2.   Medium-term planning (1 month to 1 year)

a.        Forecast annual load

b.        Consider probable generation sources

c.        Equipment and Line Maintenance

d.        Calculate system utilization based on
forecast load and nameplate ratings

e.        Schedule maintenance operations -
time-based

f.         Schedule maintenance operations -
predictive, based on data and models

g.        Schedule equipment replacement - based
on age of equipment

h.        Schedule equipment replacement -
predictive, based on data and models

i.         Schedule equipment replacement - based
on contingency scenarios

j.         Schedule spare distribution, ensure
sufficient at each site

k.        Revise contracts with Distribution
Utilities

3.   Operational planning (1 day to 1 month)

a.        Short-term load forecast

b.        Short-term generation alternatives
based on annual maintenance plan and market conditions

c.        Planned outage management

d.        Operators determine needed transmission
outages

e.        Operators analyze contingencies

f.         Planners/operators perform load
analysis of substation equipment based on data

g.        Operators submit transmission outages
and constraints to RTO/ISO

h.        Dynamic equipment capacity

i.         Protection engineer, to alter relay
settings

4.   Real-time normal operator actions (Using
SCADA/EMS)

a.   SCADA system monitors transmission system

b.   Monitor plant state (open/close)

c.   Monitor system activity and load (current,
voltage, frequency, energy)

d.   Monitor equipment condition (overheat,
overload, battery level, capacity)

e.   Monitor environmental (fire, smoke,
temperature, sump level) and Monitor security (door alarm, intrusion,
cyber attack)

f.   Monitor security records (audio/video
recording)

g.   Operators handle alarms

h.   Intelligent alarm processing should happen
here as well as in (6).

i.    Distribution of alarms to non-operators:

j.    overloads and replacement issues to
maintenance engineer

k.   automated work management system

l.    fault records and SOEs to protection
engineers

m.  info to billing dept. re: possible refunds or
reliability contract

n.   external security or emergency response teams

o.   Operators perform supervisory control of
switching operations

p.   Manual switching

q.   Transfer of Authority

r.   Automation system controls voltage, var and
power flow based on algorithms, real-time data, and network linked
capacitive and reactive components

s.   All items listed under 6h could also be
performed under Normal operation as normal load management, I.e. "peak
shaving" or temporary overloading of equipment due to other manual
operations.

u.   Operators changes setup/options of EMS
functions

·   
Periodicity of real-time sequence/Cold Initiation

·   
Event triggers

·   
Manual initiations

·   
Contingency list

·   
Application tuning parameters

·   
Other

v.   Operators prepare for storm conditions based
on weather data and history and change recloser settings

w.  Operators prepare for storm conditions based
on weather data and history and change alarm thresholds

x.   Prepare for transformer clipping (e.g. Solar
wind/Solar Magnetic Disturbance raising ground DC offset)

5.   Network Analysis (real-time)

a.   EMS system performs model update, state
estimation, bus load forecast

b.   EMS system performs contingency analysis,
recommends preventive and corrective actions

c.   EMS system performs optimal power flow
analysis, recommends optimization actions

d.   EMS system or planners perform stability
study of network

6.   Real-time emergency operations (system
protection level)

a.   Power System Protection

b.   Emergency Operations performs Under-frequency
load/generation shedding

c.   Emergency Operations performs Under-voltage
load shedding

d.   Emergency Operations performs Conditional
localized load shedding

e.   Recovery from voltage or frequency-based load
shedding

f.   LTC control/blocking

g.   Shunt control

h.   Series compensation control

i.    System separation detection

j.    Wide area real time instability recovery

k.   Operators manage emergency alarms

l.    SCADA/EMS aids operators in locating fault

m.  Operators dispatch field crews for restoration

n.   SCADA system performs intelligent alarm
processing

o.   Local alarm reduction within substation

p.   Centralized alarm reduction based on events
from multiple substations

q.   SCADA system performs disturbance monitoring
analysis (including fault location)

r.   SCADA/EMS performs dynamic limit calculations
for transformers and breakers based on real time data from equipment
monitors

s.   SCADA/EMS performs pre-arming of fast acting
emergency automation

t.    SCADA/EMS generates signals for emergency
support by Distribution Utilities (according to the T&D contracts):

> ·      
> Emergency voltage and var control for
> providing dispatchable real and/or reactive loads
>
> ·      
> Emergency load re-balancing between T/D
> substations by feeder reconfiguration
>
> ·      
> Activation of interruptible/curtailable load
>
> ·      
> Activation of direct load control
>
> ·      
> Activation of distributed resources
>
> ·      
> Activation of other load management functions

u.   Operators performs system restorations based
on system restoration plans prepared (authorized) by operation
management

7.   Post operations

a.   All systems archive logs and reports

8.   Power system equipment maintenance (mobile
enabled work force)

a.        Substation and Line Maintenance
including operation blocking

b.        Periodic (time-based) maintenance

c.        Based on age of equipment

d.        Based on predictive models driven by
real-time data

e.        Maintenance staff maintain transmission
lines

f.         Request that operator block reclosing
for maintenance purposes

g.        Maintenance staff provides information
for updating relevant databases

h.        Maintenance staff refer to substation
drawings (online?)

9.   SCADA/EMS Maintenance

a.   SCADA/EMS personnel updates SCADA/EMS
databases

b.   SCADA/EMS personnel updates EMS applications

c.   SCADA/EMS personnel updates operator
interfaces

d.   SCADA/EMS personnel updates interfaces with
other systems

e.   SCADA/EMS personnel performs diagnostics of
the SCADA/EMS systems

10. Operator and SCADA/EMS personnel training

a.   Operators and SCADA/EMS personnel perform
periodic training by using the Operator Training Simulator

b.   Operators and SCADA/EMS personnel participate
in advanced education programs

11. Engineering

a.   Protection engineers perform protection
engineering

·   
Duties: base case, fault studies, relay settings, protection
coordination, fault analysis

·   
Needs data: line/equipment capacity, relay specs, PT/CT ratios, fault
records, SOE data, event info (relay 'targets' - which element picked
up)

b.   Substation engineers perform substation
engineering

c.   Transmission engineers perform transmission
line engineering

d.   Engineering staff provides information for
updating relevant databases - from site / online

12. Construction management

a.   Construction managers manage asset purchasing

b.   Construction managers plan construction
projects

c.   Construction managers manage crew assignments

d.   Construction personnel provides information
for updating relevant databases - from the site / online

e.   Construction personnel refer to substation
drawings (online?)

13. Black Start

## 1.3         Distribution Operations Domain

1.     
Long term distribution planning (1 year to 5 years)

a.     
Distribution planners forecast loads for the long term by area

b.     
Distribution planners plan distribution upgrades and additions in
accordance with the long-term transmission plan (using planning
simulation and optimization software)

·      
New T/D substations

·      
New distribution circuits/conductors

·      
New distribution transformers

·      
New distributed generation, including distributed
resources impact studies

–      
DisCo plans utility-owned DR to meet reliability and power
quality targets

–      
DisCo acquires DR base information (to provide ratings and
device models)

–      
DisCo analyzes DR interconnection to the power system

·      
New circuit boundaries

·      
New switch allocation

·      
New capacitor allocation

c.     
Distribution planners plan distribution automation

·      
 SCADA

·      
 DA functions

–      
 Fault Location

–      
 Fault isolation and service restoration

–      
 Outage statistics calculations

–      
 Volt/Var control

–      
 Planned outage management

–      
 Feeder reconfiguration

–      
 Cold load pickup

–      
 Dynamic limit calculations

–      
 Feeder paralleling

–      
 Integration with EMS/MOS

–      
 Equipment monitoring and diagnostics

–      
 Other

d.     
Distribution planners prepare long-term contracts with transmission
companies covering mutual obligations for the T&D interfaces,
operation coordination, and information exchange.

e.     
Distribution planners prepare long-term contracts with generators
connected to distribution

f.      
Distribution planners prepare long-term contract with customers
regarding service reliability and power quality

g.     
Distribution planners generate requirements for information support of
distribution domain activities

h.     
Distribution planners update the future layers of relevant databases

2.     
Short-term distribution planning (1 week to 1 year)

a.     
Short-term load forecast

·      
 Load forecast for existing nodal loads

·      
 Forecast of allocation and amount of new loads

·      
 Forecast/scheduling of distributed resources

b.     
Update of circuit boundaries

c.     
Update of switch placement

d.     
Update of capacitor placement and sizing

e.     
Update of no-load tap positions

f.      
Update phase load allocation for better load and voltage balancing

g.     
Update of contracts with transmission company

h.     
Update of automation settings

i.       
Short-term distributed resources impact studies

j.      
Update of contracts with distribution generators

k.     
Update of contracts with customers

l.       
Contractor /Builder requests new service connection (see IEC WG14 Use
Case #2 and 3)

m.   
Update of relevant databases

n.     
Prepare maintenance plan

·      
 Calculate system utilization based on forecast load and
nameplate ratings

·      
 Schedule maintenance operations - time-based

·      
 Schedule maintenance operations - predictive, based on
data and models

·      
 Schedule equipment replacement - based on age of
equipment

·      
 Schedule equipment replacement - predictive, based on
data and models

·      
 Schedule equipment replacement - based on contingency
scenarios

·      
 Schedule spare distribution, ensure sufficient at each
site

3.     
Operational planning (1 day to 1 week ahead)

a.     
Planned outage management by using DA applications in study/look-ahead
mode and DA databases

·      
 Outage request analysis and scheduling, taking into
account the capabilities of real-time DA functions.

·      
 Planners/operators perform load analysis of substation
equipment based on data

·      
 Multi-level feeder reconfiguration

·      
 Contingency analysis/reliability (risk) assessment

·      
 Distributed resources re-scheduling

·      
 Protection coordination analysis

·      
 Switching order generation for facilitating the planned
outages and for return to normal

b.     
Work management (planning stage)

·      
 Schedulers interface with contractors

·      
 Schedulers schedule work crews for scheduled work

·      
 System operators review and approve scheduled work

·      
 Schedulers identify assets required for scheduled work

·      
 Work crews perform scheduled work, coordinating with
operators for switching operations

c.     
Operators prepare (plan) for storm conditions and other alerting
situations based on weather data, other alarming systems, and history

·      
 Change recloser settings

·      
 Change alarm thresholds

·      
 Prepare for transformer clipping (e.g.  Solar wind
raising ground DC offset)

4.     
Real-time operations

a.     
SCADA system monitors distribution system

·      
 Monitor plant state (open/close)

·      
 Monitor system activity and load (current, voltage,
frequency, energy)

·      
 Monitor equipment condition (overheat, overload,
battery level, capacity)

·      
 Monitor environmental (fire, smoke, temperature, sump
level)

·      
 Monitor security (door alarm, intrusion, cyber attack,
audio/video recording)

b.     
Operators handle alarms

·      
 Intelligent alarm processing by SCADA system

·      
 Distribution of alarms to non-operators:

- overloads and replacement issues to maintenance engineer

- automated work management system

- fault records and SOEs to protection engineers

- info to billing dept. re: possible refunds or reliability contract

c.     
Operators dispatch field crews for scheduled work:

·      
 Crew acquires drawings, previous records, customer
profile

·      
 Operator establishes limits on what crew is permitted
to do

·      
 Using mobile radio system

·      
 Using mobile computing

d.     
Work crews provide information for updating relevant databases

·      
 Work crews log activities and results of tests

·      
 Work crews identifies assets installed and/or removed

e.     
Operators perform supervisory and/or manual (using field crews)
control of switching operations, load tap changers and voltage
controllers, capacitor statuses

f.      
Operator defines objectives and other parameters of DA functions, e.g.

·     Closed-loop control of
service restoration function

·     Use emergency limits
for service restoration

·     Provide volt/var
support for transmission

·     Provide Peak Load
reduction within voltage quality limits

·     Provide Peak Load
reduction within voltage emergency limits

5.     
Automation of distribution operations

a.     DA
system updates power system model and analyzes distribution operations

·      
 Update topology model

·      
 Update facilities model

·      
 Update load model

·      
 Update relevant transmission model

·      
 Update and analyze real-time operating conditions using
distribution power flow/state estimation

·      
 Update system capacity based on real-time equipment
monitoring data

·      
 Issue alarming/warning messages to the operator

·      
 Generate distribution operation reports and logs

b.     DA
system performs fault location, fault isolation, and service
restoration

·      
 DA indicates the faults cleared by controllable
protective devices

–      
 Distinguish faults cleared by fuses

–      
 Distinguish momentary outages

–      
 Distinguish inrush/cold load current

·      
 DA determines the faulted sections based on SCADA fault
indications and protection lockout signals

·      
 DA estimates the probable fault locations based on
SCADA fault current measurements and real-time fault analysis

·      
 DA determines the fault-clearing non-monitored
protective device based on trouble call inputs and dynamic
connectivity model

·      
 DA generates switching orders for fault isolation,
service restoration, and return to normal (taking into account the
availability of remotely controlled switching devices, feeder
paralleling, and cold-load pickup)

–      
 Operators executes switching orders by using SCADA

–      
 Operator authorizes the DA application to execute the
switching orders in closed-loop mode

·      
 DA system isolates the fault and restores service
automatically by-passing the operator based on operator’s
authorization in advance

·      
 DA considers creation of islands supported by
distributed resources for service restoration

c.     DA
system performs multi-level feeder reconfiguration for different
objectives:

·      
 Service restoration

·      
 Overload elimination

·      
 Load balancing

·      
 Transmission facilities overload

·      
 Loss minimization

·      
 Voltage balancing

·      
 Reliability improvement

d.     DA
performs relay protection re-coordination

·      
 After feeder reconfiguration

·      
 In case of changed conditions for fuse saving

e.     DA
system optimally controls volt/var by changing the states of voltage
controllers, shunts, and distributed resources in a coordinated manner
for different objectives under normal and emergency conditions:

·      
 Power quality improvement

·      
 Overload elimination/reduction

·      
 Load management

·      
 Transmission operation support in accordance with T&D
contracts

·      
 Loss minimization in distribution and transmission

6.     
Real-time emergency operations

a.     
Protection equipment performs system protection actions

·    Fault detection,
clearing, and reclosing

·      
 Under-frequency load-shedding

·      
 Under-voltage load-shedding

b.     
Operators manage multiple emergency alarms

·     Intelligent
alarm processing by SCADA system

c.     
SCADA system performs disturbance monitoring

·     Fault current recording

·     Fault location

·     Event recording

d.     
Operators dispatch field crews to troubleshoot system and customer
power problems

·      
 Mobile radio system

·      
 Mobile computing

e.     
Operators perform emergency switching operations

f.      
Operators performs intrusive load management activities

·      
 Operators or planners identify critical loads
(hospitals, etc.) ahead of time

·     DA system locks out
load shedding of critical loads

·     Operator activates
direct load control

·     Operator activates 
load curtailment

·     Operator applies load
interruption

·     Operators enables
emergency load reduction via volt/var control

·     Operator applies manual
rolling blackouts

g.     
Operator enables emergency (major event) mode of operations of
operation and maintenance personnel, and enables major event emergency
mode of operation of DA applications

h.     
Outage management systems collect trouble calls, generate outage
information, arrange work for trouble shooting

i.       
Interactive utility-customer systems inform the customers about the
progress of events

j.      DA
performs in major event emergency mode

7.     
Post operations

·      All systems create and
archive logs and reports

·     System records voice
logs of interaction between operators and field crews

·     All systems transmit
reports to key parties

a.     
Maintenance personnel of the automated systems (DAS, OMS, WMS)
performs diagnostic analysis of system performance

b.     
Diagnostic analysis based on real-time equipment monitoring data, e.g.
using predictive models to determine when the equipment needs
maintenance

8.     
Power system equipment maintenance

a.     
Maintenance staff maintain distribution equipment and lines

·        Maintenance staff
analyzes equipment diagnostic results, compares it with the predictive
models

·        Maintenance staff
prepares outage requests based on time and condition criteria

·      
 Operations staff review and approve outage requests

·        Maintenance staff
identifies assets and work crew requirements

·      
 Work crew carries out maintenance, coordinating with
operators for switching

b.     
Maintenance staff provides information for updating relevant databases

·        Work crew logs
activities and results of tests

·      
 Work crew identifies assets removed and/or installed

·      
 Maintenance staff identifies errors in documentation
and maps

·      
 Maintenance staff identifies marks up documentation
("red/green")

·      
 Maintenance staff indicates permanent versus temporary
changes

9.     
Engineering

a.     
Engineering personnel perform distribution system engineering

b.     
Engineering personnel specifies distribution power and control
equipment

c.     
Engineering personnel provides information for updating relevant
databases

10.  
Construction management

a.     
Construction managers manage assets purchases

b.     
Construction managers plan construction projects

c.     
Construction managers manage crew assignments

d.     
Construction personnel provides information for relevant databases

11.  Power
Quality Management

a.     
Utility measures power quality parameters, transmits them to central
location, processes data, and stores data in PQ database in real time.

b.     
Real time power quality state estimation system calculates power
quality characteristics based on limited monitoring information from
substations, distribution systems, and customer systems and models
(pseudo-measurements) supplementing to the needed redundancy

c.     
Utility exposes historical and real-time power quality data to
customers

d.     
Utility correlates data from utility operations database, lightning
database, and other operations related database with PQ event database
and generates reports and/or stores analysis results for future
reporting.

e.     The
utility PQ evaluation system analyzes PQ events, trends, and profiles
of power quality levels of the supply system against planning limits
and operation objectives.  The system is used to generate
recommendations and priorities for system improvements.

f.      
The power quality management system analyzes PQ events and profiles to
identify causes of PQ problems and possible equipment problems that
could be corrected.  Detailed recommendations are developed and
automatic responses are implemented where possible.

g.     The
power quality information is evaluated with respect to specific
customer requirements on the specific system.  Coordination with
equipment and power conditioning equipment within customer facilities
is implemented to improve productivity and reliability of customer
systems.  (See description in Customer Services Domain)

h.     
Utility accesses PQ database and generates bill/refund/penalty
statement for events that exceed contract limits.  (see description in
the Customer Services Domain)

i.       
Utility generates various reports from PQ database for operation,
management, engineering, and customer consumption via e-mail and web
interfaces.

12.  
Dispatcher Training Simulator

## 1.4          HV Generation Domain

1.     
Long term planning (months to years ahead for new construction)

a.     
Generation planners perform long terms load forecasts

b.     
Generation planners plan generation

c.     
Market Participants negotiate long term market contracts

2.     
Operational planning (Day ahead to months ahead for
installing/maintaining equipment)

a.     
Generation planners determine needed generation outages

b.     
Generation planners submit generation outages and constraints to
RTO/ISO

3.     
Real-time SCADA operations (real-time)

a.     
Generation operators operate the generation units

b.     
Generators respond to control commands from RTO/ISO/Control Area EMS
systems

4.     
Post operations

a.     All
systems archive logs and reports

b.     All
systems create reports

c.     
Environmental system collect environmental and pollution statistics

5.     
Generator equipment maintenance

a.     
Maintenance staff maintain generation equipment

6.     
Construction management

a.     
Construction managers manage assets

b.     
Construction managers plan projects

c.     
Construction managers manage crew assignments

Distributed Resources
(LV Generation) Domain

1.     
Long term planning (months to years ahead for new construction)

a.     
Distributed Resources (DR) owner plans for DR devices

b.     
DisCo acquires DR base information (to provide ratings and device
models)

c.     
DisCo analyzes DR interconnection to the power system

d.     
Energy services provider installs and tests DR and DR interconnection

2.     
Interconnected DR management

a.     DR
owner SCADA monitors and controls DR devices

b.     
DisCo SCADA system monitors and controls DR devices (see above)

3.     
Post operations

a.     All
systems archive logs and reports

b.     All
systems create reports

4.     DR
equipment maintenance

a.     DR
maintenance staff maintain DR equipment

b.     
Regulators monitor DR environmental statistics

Customer Services
Domain

1.   Automatic meter reading (AMR)

a.   Meter Data Management Agent (MDMA) reads
meters with handheld/mobile technologies

b.   MDMA reads industrial and/or commercial
meters with fixed AMR technology

c.   MDMA reads residential meters with fixed AMR
technology

d.   MDMA provides individual and aggregated meter
readings to market settlements, DisCos, and/or TransCos

e.   MDMA or DisCo provides individual energy
usage and billing to customers

f.   Prepay metering

g.   Non-electric metering -- subcontracted
submetering for non-electric utilities -- Note: focus on aspects of
shared infrastructure and not the actual metering

h.   Sub-metering -- customer bill dis-aggregation
and rental space allocations

i.    Non-intrusive load monitoring -- deducing
load contributions by monitoring aggregate consumption changes

j.    Outage isolation

2.   Customer Management

a.   DisCo provides tamper detection, load
profiles, etc.

b.   DisCo provides connect, disconnect, energy
usage and billing information, etc. to customers

c.   DisCo provides information for updating
relevant databases

3.     Customer trouble call management

a.   Customer reports trouble and trouble ticket
is generated (see Customer Information under Corporate Services)

b.   Trouble ticket is used by outage management
function (see Distribution Operations)

c.   Trouble ticket is used for statistical
analysis (see Distribution Operations)

4.   Real-time Pricing (RTP)

a.   ESP updates RTP schedules for subscribing
customers

·    ESP
receives base RTP schedule from Market Operations

·    ESP
calculates customer-specific RTP schedules

·    ESP
multicasts RTP schedules to customers

b.   Customer EMS manages energy usage based on
RTP

·   
Customer EMS determines optimal mix of current load, deferred load,
and DR generation, based on RTP schedule

·   
Customer EMS implements load and DR management

5.   Load management

a.   ESP applies direct load control measures -
residential

·   
Applies/requests direct load control (cycle water heaters, air
conditioners, and other loads)

·   
Curtails customer loads

·   
Interrupts customer loads

·   
Sheds customer loads (under frequency / under voltage)

·   
Requests load-reducing volt/var control

b.   Permissive power provision -- devices can
request a limit of power. This would allow an emergency device to use
power while other loads might not. Scheduled and load limited.
Authenticated level control

c.   Aggregation of customers who are asked to
reduce load amongst them when asked to curtailed. Pagers to signal

6.   Building/Home Energy Management Services

a.   ESP monitors building security systems
(illegal entry, environmental alarms, health care signals, etc.) - no
remote control

b.   Customer EMS manages building environment,
based on preset parameters (security settings, temperature,
appliances, lighting management, etc.)

c.   Customer status/control of building
environment locally and/or remotely by modifying parameters

d.   Customer EMS bids into power market for
dynamic load profile

·   
Machine bidding for power consumption

·   
Buildings of same owner collaborate on load profile

·   
Negotiate for poor power quality events

e.   Customer EMS tracks billing

·    EMS
receives bill to date

·    EMS
receives pricing forecasts

·    EMS
receives history data - minute by minute and events

f.   Offsite premise management

·   
Provide analysis and control of homes / businesses /vacation property

g.   Occupancy based heating and lighting controls

h.   Building VAR Control

7.   Weather

a.   Lightening and severe weather alert
notification

·   
Notification of emergency transient conditions

b.   Weather to consumer

·   
Provide day or multi-day ahead weather forecasts, alerts

·   
Provide dynamic/periodic wind/solar/thermal/precipitation status for
optimal control

c.   Weather from consumer

·   
Retrieve microclimate data from consumer controls -- outside air,
solar, precipitation

8.   Third party services

a.   Contractor use of utility gateway and
communications

·   
Remote servicing of HVAC control

b.   Home owner can access utility gateway and
manage his house appliances

9.   Power Quality

a.   Notify customer of current PQ information

·   
Current harmonic content

·    PQ
events

b.   Implement power quality contracts

c.   Coordinate with power conditioning equipment
and process equipment to improve performance

·   
Power factor correction and harmonic filters

·    UPS
and power conditioning equipment

·   
Process equipment and machine controls

d.   Improve power quality through supervisory
control

e.   Prioritize system improvements based on
reliability and PQ levels being supplied to customers

10. Electric Vehicle / home co-generation

a.   Billing a "consumption event"

·    When
consumer charges up at another customers "pump" (charging station) (*not
perceived as important)*

b.   EV as generator

·   
Permit EV generator to emit power into power grid

11. Energy efficiency monitoring

a.   Appliance performance monitoring

·   
Monitor and compute energy efficiency for appliances and subsystems

b.   Fault detection and diagnostics

·   
Detect specific appliance signature and analyze for drift or fault

12. Indoor Air Quality

a.   Monitoring of sensors

·   
Regulatory support / documentation of compliance

·   
Remote monitoring and alarming of measurements

13. ISP services to customer

a.   Reselling of bandwidth to conventional
communication service providers (including telephone, TV, and ISP)

14. Third party Service Support

a.   Homes security services - owner managed

b.   Home health (patient monitoring / health
emergency alarm)

c.   Alarm qualification

d.   Remote video surveillance -- monitoring of
home "web cams"

e.   Home alarms -e.g. -water in basement

15. Transmission and Distribution Operations
Support

IT Services Domain

1.     
Telecommunications Infrastructure

a.     
Domains determine their telecommunication requirements

2.     
Security Management (Federation)

a.     
Security managers implement cyber security policies

b.     
Security technologies manage security appropriately for each type of
interaction

3.     
Network and system management (Federation)

a.     
Network and system managers (NSMs) assess NSM requirements

b.     NSM
systems monitor and control communications networks and equipment

c.     NSM
systems monitor and control systems and applications

d.     NSM
systems analyze and report performance

e.     NSM
staff perform preventative and emergency maintenance

4.     
Data management (Federation)

a.     
Data maintenance staff update data in databases

·      
Automated mapping and facilities management databases

·      
SCADA databases

·      
Customer Information databases

b.     
Systems synchronize data across all interfaced systems

c.     
Data maintenance staff troubleshoot data problems

d.     All
systems archive reports and logs of data maintenance activities

Corporate Services
(External Domain)

1.     
Executive management

2.     
Finance

3.     
Human resources

4.     
Customer information

5.     
Accounting and billing
