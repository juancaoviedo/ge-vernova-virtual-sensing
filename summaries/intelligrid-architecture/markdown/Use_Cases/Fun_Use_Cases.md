# List of Functions

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/Fun_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Complete List of Power System Functions

The following is the complete list of power system functions
identified during the IntelliGrid Project. They were briefly described and
analyzed for their key communications requirements:

* Communication configuration requirements, including
  number of end devices, location of equipment, media
  constraints, compute-constraints, wireless requirements,
  etc.
* Quality of service requirements, including response
  speed, availability, data volumes, data accuracy, data
  exchange frequency, etc.
* Security requirements, including authentication, access
  control, confidentiality, data integrity, non-repudiation,
  sensitivity to denial of service, etc.
* Data management requirements, including managing large
  databases, many databases, timely access, frequent updates,
  data exchanges across organizational boundaries, etc.

The details of the brief analysis of these functions can be found in the
[Volume II,
Appendix F: Task 1 Enterprise Activities](../IECSA_Volumes/IECSA_VolumeII_AppendixF.pdf). The list of these power
system functions is provided below.

* [Market Operations](Fun_Use_Cases.htm#Market_Operations_Domain)
* [Transmission Operations](Fun_Use_Cases.htm#Transmission_Operations_Functions)
* [Distribution
  Operations](Fun_Use_Cases.htm#Distribution_Operations_Domain)
* [HV Generation](Fun_Use_Cases.htm#HV_Generation_Domain)
* [Distributed Energy Resources](Fun_Use_Cases.htm#Distributed_Resources_(LV_Generation)_Domain)
* [Customer Services](Fun_Use_Cases.htm#Customer_Services_Domain)
* [IT Services](Fun_Use_Cases.htm#IT_Services_Domain)

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
RTO/ISO certify generation units

c.     
RTO/ISO analyze generation market for capacity and adequacy to meet
load

d.     
RTO/ISO register and perform credit rating of Market Participants
(MPs)

e.     
RTO/ISO validate and register revenue meters

f.      
TransCos/GenCos propose scheduled transmission and generation outages
which are validated via congestion management analysis

g.     
 RTO/ISO auction, sell, and/or track transmission rights and other
energy services to Market Participants

h.     
Energy Traders, ESPs, and other authorized Market Participants
establish bilateral energy contracts between Generation and Loads

3.     
Short-term Planning (48 hours- one month)

a.     
Corrections of medium-planning actions, available capacity, and
possible ancillary services, based on updated data on transmission
outages, generation maintenance, load forecasts, etc.

4.     Day
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
RTO/ISO provide information to Market
Participants

·      
Provide mandated and other energy
information to Market Participants

·      
Disclose environmental information

·      
Publish notifications

5.    
Real-Time (actual time to next hour)

a.    
Calculate operational parameters in
real-time

b.    
Market Participants submit adjustments to
real-time energy schedules

c.    
Market Participants submit real-time bids
for ancillary services

d.    
RTO/ISO dispatch generation power system
under normal conditions:

·      
RTO/ISO SCADA system monitors power
system

·      
RTO/ISO EMS system performs
Automatic Generation Control (AGC)

·      
RTO/ISO Market Operations system
analyzes transmission capacity and reliability

·      
RTO/ISO Market Operations system
balances energy/ancillary services

·      
RTO/ISO EMS system monitors
interchange schedules with internal and external
Control Areas

e.    
RTO/ISO exchange information with external
entities:

·      
RTO/ISO Market Operations system
coordinates operational activities with
distribution operations of interconnected UDCs

·      
RTO/ISO Market Operations system
coordinates operational activities with
Reliability Councils and NERC

·      
RTO/ISO Market Operations system
coordinates operational activities with Market
Participants

f.     
RTO/ISO redispatch/emergency dispatch

·      
RTO/ISO EMS system redispatches
generation to handle emergency

·      
RTO/ISO Market Operations system
notifies Market Participants of redispatch

·      
RTO/ISO Market Operations system
manages market external price caps

6.    
Post-Dispatch (last hour to prior months)

a.    
Handle energy reporting

·      
RTO/ISO Market Operations system
calculates actual interchange information and
energy schedules

·      
RTO/ISO Market Operations system
calculates actual Locational Marginal Pricing (LMP)

·      
RTO/ISO Market Operations system
calculates actual losses

·      
Meter Data Management Agents (MDMAs)
process meter revenue data

b.    
Market Products Schedule Checkout

·      
Settlement Agents validate
implemented energy schedules against contracted
energy schedules

·      
Settlement Agents reconcile
differences

c.    
Financial Settlements

·      
Settlement Agents reconcile RTO/ISO
market

·      
Settlement Agents reconcile
transmission market

·      
Settlement Agents reconcile Market
Participants spot market

·      
Settlement Agents resolve disputes

·      
Market Participants reconcile
bilateral schedules

d.    
Accounting and Billing

·      
Accounting Agents create budget and
financial forecast

·      
Accounting Agents manage accounts
payable

·      
Accounting Agents manage accounts
receivable

e.    
Market Monitoring and Auditing

·      
Regulators and auditors develop
monitoring criteria

·      
Auditors perform market assessment

·      
Auditors investigate market abuse

·      
Regulators monitor environmental
statistics

## Transmission Operations Functions

1.    
Long term transmission planning (1 year to
5 years ahead)

a.    
Long term load forecast

b.    
Forecast alternatives for generation
sources (Probable market conditions)

c.    
Plan transmission upgrades and additions
(participation in ISO/RTO expansion plan)

d.    
Plan automation of transmission system for
SCADA, Equipment Monitoring, and EMS

e.    
Prepare long-term contracts with
Distribution Utilities:

·      
Transmission voltage management

·      
Distribution reactive power support (power factor)
in the D-T interface

·      
T&D
information exchange

f.     
Prepare emergency response planning, e.g.
Ice Storm, Hurricane, Catastrophic outages

g.    
Ensure hard copies of all schematics,
diagrams, relay settings are available

h.    
Prepare inventory and personnel plans based
on neighboring load, tie point capacity, etc.

2.   Medium-term planning (1 month to 1 year)

a.    
Forecast annual load

b.    
Consider probable generation sources

c.    
Equipment and Line Maintenance

d.    
Calculate system utilization based on
forecast load and nameplate ratings

e.    
Schedule maintenance operations -
time-based

f.     
Schedule maintenance operations -
predictive, based on data and models

g.    
Schedule equipment replacement - based on
age of equipment

h.    
Schedule equipment replacement -
predictive, based on data and models

i.      
Schedule equipment replacement - based on
contingency scenarios

j.     
Schedule spare distribution, ensure
sufficient at each site

k.    
Revise contracts with Distribution
Utilities

3.   Operational planning (1 day to 1 month)

a.    
Short-term load forecast

b.    
Short-term generation alternatives based on
annual maintenance plan and market conditions

c.    
Planned outage management

d.    
Operators determine needed transmission
outages

e.    
Operators analyze contingencies

f.     
Planners/operators perform load analysis of
substation equipment based on data

g.    
Operators submit transmission outages and
constraints to RTO/ISO

h.    
Dynamic equipment capacity

i.      
Protection engineer, to alter relay
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
temperature, sump level) and Monitor security
(door alarm, intrusion, cyber attack)

f.   Monitor security records (audio/video
recording)

g.   Operators handle alarms

h.   Intelligent alarm processing should happen
here as well as in (6).

i.    Distribution of alarms to non-operators:

·      
overloads and replacement issues to
maintenance engineer

·      
automated work management system

·      
fault records and SOEs to protection
engineers

·      
info to billing dept. re: possible refunds or
reliability contract

·      
external security or emergency response teams

j.   Operators perform supervisory
control of switching operations

k.   Manual switching

l.   Transfer of Authority

m.   Automation system controls voltage,
var and power flow based on algorithms, real-time
data, and network linked capacitive and reactive
components

n.   All items listed under 6h could
also be performed under Normal operation as normal
load management, I.e. "peak shaving" or temporary
overloading of equipment due to other manual
operations.

o.   Operators changes setup/options of
EMS functions

·      
Periodicity of real-time
sequence/Cold Initiation

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

p.   Operators prepare for storm
conditions based on weather data and history and
change recloser settings

q.  Operators prepare for storm conditions
based on weather data and history and change alarm
thresholds

r.   Prepare for transformer clipping
(e.g. Solar wind/Solar Magnetic Disturbance
raising ground DC offset)

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
for transformers and breakers based on real time
data from equipment monitors

s.   SCADA/EMS performs pre-arming of fast acting
emergency automation

t.    SCADA/EMS generates signals for emergency
support by Distribution Utilities (according to
the T&D contracts):

·      
Emergency voltage and var control
for providing dispatchable real and/or reactive
loads

·      
Emergency load re-balancing between
T/D substations by feeder reconfiguration

·      
Activation of
interruptible/curtailable load

·      
Activation of direct load control

·      
Activation of distributed resources

·      
Activation of other load management
functions

u.   Operators performs system restorations based
on system restoration plans prepared (authorized)
by operation management

7.   Post operations

a.   All systems archive logs and reports

8.   Power system equipment maintenance (mobile
enabled work force)

a.   Substation and Line Maintenance including
operation blocking

b.   Periodic (time-based) maintenance

c.   Based on age of equipment

d.   Based on predictive models driven by
real-time data

e.   Maintenance staff maintain transmission lines

f.   Request that operator block reclosing for
maintenance purposes

g.   Maintenance staff provides information for
updating relevant databases

h.   Maintenance staff refer to substation
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
periodic training by using the Operator Training
Simulator

b.   Operators and SCADA/EMS personnel participate
in advanced education programs

11. Engineering

a.   Protection engineers perform protection
engineering

·   
Duties: base case, fault studies, relay settings,
protection coordination, fault analysis

·   
Needs data: line/equipment capacity, relay specs,
PT/CT ratios, fault records, SOE data, event info
(relay 'targets' - which element picked up)

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
for updating relevant databases - from the site /
online

e.   Construction personnel refer to substation
drawings (online?)

13. Black Start

## Distribution Operations Domain

1.    
Long term distribution planning (1 year to
5 years)

a.    
Distribution planners forecast loads for
the long term by area

b.    
Distribution planners plan distribution
upgrades and additions in accordance with the
long-term transmission plan (using planning
simulation and optimization software)

·      
New T/D substations

·      
New distribution circuits/conductors

·      
New distribution transformers

·      
New distributed generation,
including distributed resources impact studies

–      
DisCo plans utility-owned DR to meet
reliability and power quality targets

–      
DisCo acquires DR base information (to
provide ratings and device models)

–      
DisCo analyzes DR interconnection to the
power system

·      
New circuit boundaries

·      
New switch allocation

·      
New capacitor allocation

c.    
Distribution planners plan distribution
automation

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
Distribution planners prepare long-term
contracts with transmission companies covering
mutual obligations for the T&D interfaces,
operation coordination, and information exchange.

e.    
Distribution planners prepare long-term
contracts with generators connected to
distribution

f.     
Distribution planners prepare long-term
contract with customers regarding service
reliability and power quality

g.    
Distribution planners generate requirements
for information support of distribution domain
activities

h.    
Distribution planners update the future
layers of relevant databases

2.    
Short-term distribution planning (1 week to
1 year)

a.    
Short-term load forecast

·      
 Load forecast for existing nodal
loads

·      
 Forecast of allocation and amount
of new loads

·      
 Forecast/scheduling of distributed
resources

b.    
Update of circuit boundaries

c.    
Update of switch placement

d.    
Update of capacitor placement and sizing

e.    
Update of no-load tap positions

f.     
Update phase load allocation for better
load and voltage balancing

g.    
Update of contracts with transmission
company

h.    
Update of automation settings

i.      
Short-term distributed resources impact
studies

j.     
Update of contracts with distribution
generators

k.    
Update of contracts with customers

l.      
Contractor /Builder requests new service
connection (see IEC WG14 Use Case #2 and 3)

m.  
Update of relevant databases

n.    
Prepare maintenance plan

·      
 Calculate system utilization based
on forecast load and nameplate ratings

·      
 Schedule maintenance operations -
time-based

·      
 Schedule maintenance operations -
predictive, based on data and models

·      
 Schedule equipment replacement -
based on age of equipment

·      
 Schedule equipment replacement -
predictive, based on data and models

·      
 Schedule equipment replacement -
based on contingency scenarios

·      
 Schedule spare distribution, ensure
sufficient at each site

3.    
Operational planning (1 day to 1 week
ahead)

a.    
Planned outage management by using DA
applications in study/look-ahead mode and DA
databases

·      
 Outage request analysis and
scheduling, taking into account the capabilities
of real-time DA functions.

·      
 Planners/operators perform load
analysis of substation equipment based on data

·      
 Multi-level feeder reconfiguration

·      
 Contingency analysis/reliability
(risk) assessment

·      
 Distributed resources re-scheduling

·      
 Protection coordination analysis

·      
 Switching order generation for
facilitating the planned outages and for return to
normal

b.    
Work management (planning stage)

·      
 Schedulers interface with
contractors

·      
 Schedulers schedule work crews for
scheduled work

·      
 System operators review and approve
scheduled work

·      
 Schedulers identify assets required
for scheduled work

·      
 Work crews perform scheduled work,
coordinating with operators for switching
operations

c.    
Operators prepare (plan) for storm
conditions and other alerting situations based on
weather data, other alarming systems, and history

·      
 Change recloser settings

·      
 Change alarm thresholds

·      
 Prepare for transformer clipping
(e.g.  Solar wind raising ground DC offset)

4.    
Real-time operations

a.    
SCADA system monitors distribution system

·      
 Monitor plant state (open/close)

·      
 Monitor system activity and load
(current, voltage, frequency, energy)

·      
 Monitor equipment condition
(overheat, overload, battery level, capacity)

·      
 Monitor environmental (fire, smoke,
temperature, sump level)

·      
 Monitor security (door alarm,
intrusion, cyber attack, audio/video recording)

b.    
Operators handle alarms

·      
 Intelligent alarm processing by
SCADA system

·      
 Distribution of alarms to
non-operators:

–      
overloads and replacement issues to
maintenance engineer

–      
automated work management system

–      
fault records and SOEs to protection
engineers

–      
info to billing dept. re: possible refunds
or reliability contract

c.    
Operators dispatch field crews for
scheduled work:

·      
 Crew acquires drawings, previous
records, customer profile

·      
 Operator establishes limits on what
crew is permitted to do

·      
 Using mobile radio system

·      
 Using mobile computing

d.    
Work crews provide information for updating
relevant databases

·      
 Work crews log activities and
results of tests

·      
 Work crews identifies assets
installed and/or removed

e.    
Operators perform supervisory and/or manual
(using field crews) control of switching
operations, load tap changers and voltage
controllers, capacitor statuses

f.     
Operator defines objectives and other
parameters of DA functions, e.g.

·      
Closed-loop control of service
restoration function

·      
Use emergency limits for service
restoration

·      
Provide volt/var support for
transmission

·      
Provide Peak Load reduction within
voltage quality limits

·      
Provide Peak Load reduction within
voltage emergency limits

5.    
Automation of distribution operations

a.    
DA system updates power system model and
analyzes distribution operations

·      
 Update topology model

·      
 Update facilities model

·      
 Update load model

·      
 Update relevant transmission model

·      
 Update and analyze real-time
operating conditions using distribution power
flow/state estimation

·      
 Update system capacity based on
real-time equipment monitoring data

·      
 Issue alarming/warning messages to
the operator

·      
 Generate distribution operation
reports and logs

b.    
DA system performs fault location, fault
isolation, and service restoration

·      
 DA indicates the faults cleared by
controllable protective devices

–      
Distinguish faults cleared by fuses

–      
Distinguish momentary outages

–      
Distinguish inrush/cold load current

·      
 DA determines the faulted sections
based on SCADA fault indications and protection
lockout signals

·      
 DA estimates the probable fault
locations based on SCADA fault current
measurements and real-time fault analysis

·      
 DA determines the fault-clearing
non-monitored protective device based on trouble
call inputs and dynamic connectivity model

·      
 DA generates switching orders for
fault isolation, service restoration, and return
to normal (taking into account the availability of
remotely controlled switching devices, feeder
paralleling, and cold-load pickup)

–      
Operators executes switching orders by
using SCADA

–      
Operator authorizes the DA application to
execute the switching orders in closed-loop mode

·      
 DA system isolates the fault and
restores service automatically by-passing the
operator based on operator’s authorization in
advance

·      
 DA considers creation of islands
supported by distributed resources for service
restoration

c.    
DA system performs multi-level feeder
reconfiguration for different objectives:

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

d.    
DA performs relay protection
re-coordination

·      
 After feeder reconfiguration

·      
 In case of changed conditions for
fuse saving

e.    
DA system optimally controls volt/var by
changing the states of voltage controllers,
shunts, and distributed resources in a coordinated
manner for different objectives under normal and
emergency conditions:

·      
 Power quality improvement

·      
 Overload elimination/reduction

·      
 Load management

·      
 Transmission operation support in
accordance with T&D contracts

·      
 Loss minimization in distribution
and transmission

6.    
Real-time emergency operations

a.    
Protection equipment performs system
protection actions

·      
Fault detection, clearing, and
reclosing

·      
 Under-frequency load-shedding

·      
 Under-voltage load-shedding

b.    
Operators manage multiple emergency alarms

·      
Intelligent alarm processing by
SCADA system

c.    
SCADA system performs disturbance
monitoring

·      
Fault current recording

·      
Fault location

·      
Event recording

d.    
Operators dispatch field crews to
troubleshoot system and customer power problems

·      
 Mobile radio system

·      
 Mobile computing

e.    
Operators perform emergency switching
operations

f.     
Operators performs intrusive load
management activities

·      
 Operators or planners identify
critical loads (hospitals, etc.) ahead of time

·      
 DA system locks out load shedding
of critical loads

·      
Operator activates direct load
control

·      
Operator activates load curtailment

·      
Operator applies load interruption

·      
Operators enables emergency load
reduction via volt/var control

·      
Operator applies manual rolling
blackouts

g.    
Operator enables emergency (major event)
mode of operations of operation and maintenance
personnel, and enables major event emergency mode
of operation of DA applications

h.    
Outage management systems collect trouble
calls, generate outage information, arrange work
for trouble shooting

i.      
Interactive utility-customer systems inform
the customers about the progress of events

j.     
DA performs in major event emergency mode

7.    
Post operations

a.    
Basic logging and reporting

·      
Systems create and archive logs and
reports

·      
System records voice logs of
interaction between operators and field crews

·      
All systems transmit reports to key
parties

b.    
Maintenance personnel of the automated
systems (DAS, OMS, WMS) performs diagnostic
analysis of system performance

c.    
Diagnostic analysis based on real-time
equipment monitoring data, e.g. using predictive
models to determine when the equipment needs
maintenance

8.    
Power system equipment maintenance

a.    
Maintenance staff maintain distribution
equipment and lines

·      
 Maintenance staff analyzes
equipment diagnostic results, compares it with the
predictive models

·      
 Maintenance staff prepares outage
requests based on time and condition criteria

·      
 Operations staff review and approve
outage requests

·      
 Maintenance staff identifies assets
and work crew requirements

·      
 Work crew carries out maintenance,
coordinating with operators for switching

b.    
Maintenance staff provides information for
updating relevant databases

·      
 Work crew logs activities and
results of tests

·      
 Work crew identifies assets removed
and/or installed

·      
 Maintenance staff identifies errors
in documentation and maps

·      
 Maintenance staff identifies marks
up documentation ("red/green")

·      
 Maintenance staff indicates
permanent versus temporary changes

9.    
Engineering

a.    
Engineering personnel perform distribution
system engineering

b.    
Engineering personnel specifies
distribution power and control equipment

c.    
Engineering personnel provides information
for updating relevant databases

10. 
Construction management

a.    
Construction managers manage assets
purchases

b.    
Construction managers plan construction
projects

c.    
Construction managers manage crew
assignments

d.    
Construction personnel provides information
for relevant databases

11. 
Power Quality Management

a.    
Utility measures power quality parameters,
transmits them to central location, processes
data, and stores data in PQ database in real time.

b.    
Real time power quality state estimation
system calculates power quality characteristics
based on limited monitoring information from
substations, distribution systems, and customer
systems and models (pseudo-measurements)
supplementing to the needed redundancy

c.    
Utility exposes historical and real-time
power quality data to customers

d.    
Utility correlates data from utility
operations database, lightning database, and other
operations related database with PQ event database
and generates reports and/or stores analysis
results for future reporting.

e.    
The utility PQ evaluation system analyzes
PQ events, trends, and profiles of power quality
levels of the supply system against planning
limits and operation objectives.  The system is
used to generate recommendations and priorities
for system improvements.

f.     
The power quality management system
analyzes PQ events and profiles to identify causes
of PQ problems and possible equipment problems
that could be corrected.  Detailed recommendations
are developed and automatic responses are
implemented where possible.

g.    
The power quality information is evaluated
with respect to specific customer requirements on
the specific system.  Coordination with equipment
and power conditioning equipment within customer
facilities is implemented to improve productivity
and reliability of customer systems.  (See
description in Customer Services Domain)

h.    
Utility accesses PQ database and generates
bill/refund/penalty statement for events that
exceed contract limits.  (see description in the
Customer Services Domain)

i.      
Utility generates various reports from PQ
database for operation, management, engineering,
and customer consumption via e-mail and web
interfaces.

12. 
Dispatcher Training Simulator

## HV Generation Domain

1.    
Real Time Scheduling - Interface to RTO/ISO

2.    
Real Time Commitment - Interface to RTO/ISO

a.    
Unit scheduling

b.    
Unit constraints

·      
Ramp rates

·      
Startup times

·      
Minimum down times

·      
Minimum generation levels

·      
Upper operating limits

·      
Minimum run times

c.    
Price mitigation

·      
Day-Ahead bidding

·      
Spot-Price bidding

d.    
Weather Analysis

e.    
Ancillary services

·      
Reserves commitment

·      
Regulation commitment

3.    
Real Time Dispatching - Interface to RTO/ISO

a.    
Unit dispatching

b.    
Unit constraints

·      
Ramp rates

·      
Startup times

·      
Minimum down times

·      
Minimum generation levels

·      
Upper operating limits

·      
Minimum run times

c.    
Price mitigation

·      
Day-Ahead bidding

·      
Spot-Price bidding

d.    
Weather Analysis

e.    
Ancillary services

·      
Reserves dispatch

·      
Regulation dispatch

f.     
Equipment status

g.    
Equipment control

h.    
Metering

·      
Real Time Power Flow measurements

·      
Real Time Var support measurements

4.    
Real Time Contingency Operations

a.    
Reserve pickup

b.    
Regulation pickup

c.    
Scheduled equipment outage contingencies

d.    
Unscheduled equipment outage contingencies (self-healing)

e.    
Electrical system fault/abnormal operation contingencies
(self-healing)

f.     
Contingency analysis with optimal power flow

g.    
Black Start (healthy grid)

·      
Maximum power output

·      
Reactive power limits

·      
Start-up times

·      
Ramp rates

h.    
Black Start (system restoration)

·      
Physical constraints - startup times, real & reactive
power, ramp times

·      
Scheduling constraints - unit/personnel availability

·      
Policy constraints - owner dictated

i.      
Emergency Response - Disaster preparedness contingencies

j.     
Performance standards data

·      
Power flow

·      
Var support

·      
AGC

·      
Excitation

·      
PSS

·      
Emissions

k.    
Intentional Islanding

l.      
Weather Analysis

5.    
Real Time Plant Operations

a.    
Generator power output and frequency control - governor and
prime mover systems

b.    
Generator voltage control - excitation systems

c.    
Generator real time measurements

d.    
Fuel management

·      
Supply

·      
Fuel system monitor

e.    
Balance-of-Plant SCADA

·      
Equipment status

·      
Equipment control

·      
Equipment monitoring

·      
Real time measurements

f.     
Black start procedures/process

g.    
Diagnostic Maintenance Data

h.    
Emissions monitoring and control

i.      
Contingency Operations

·      
Protection Functions

·      
Scheduled equipment outage contingencies

·      
Unscheduled equipment outage contingencies
(self-healing)

·      
Electrical system fault/abnormal operation contingencies
(self-healing)

·      
Mechanical systems operation contingencies
(self-healing)

j.     
Emergency Response - Disaster preparedness contingencies

k.    
Compliance with performance standards

6.    
Real Time Maintenance Control

a.    
Outage Schedules

b.    
Equipment Maintenance

c.    
Equipment Inspection

d.    
Equipment Replacement

e.    
Equipment Contingencies

f.     
Maintenance History

g.    
Parts Inventory Management

7.    
Long term planning (Years ahead)

a.    
Generation planners perform long terms load forecasts

b.    
Generation planners plan generation

c.    
Market Participants negotiate long term market contracts

d.    
Generation planners plan automated systems, communications, and
interfaces in coordination with ISO/RTO and transmission owners

·      
For measurement of ancillary services

·      
For automated volt/var control to automatically execute
optimal and/or security constrained power flow

8.    
Short-term planning (1 month to 1 year)

a.    
Plant equipment maintenance

b.    
Update the automation settings

c.    
Update the contracts with other market participants

9.    
Operational planning (1 day to 1 month)

a.    
Short-term equipment outage management

b.    
Update short-term bids for energy and ancillary services

10. 
Generator equipment maintenance planning

a.    
Maintenance staff maintain generation equipment

b.    
Automated system maintenance staff maintains the automated
systems, interfaces, communications, and databases

11. 
Construction management planning

a.    
Construction managers manage asset purchases

b.    
Construction managers plan construction projects

c.    
Construction managers manage crew assignments

d.    
Construction personnel provides information for relevant
databases

12. 
Commissioning planning

a.    
example: nuclear

13. 
De-commissioning planning

14. 
Security (generation specific issues)

a.    
Security of nuclear fuel/waste

b.    
Security from cyber threats

c.    
Inter-plan shared level of alert

## Distributed Resources (LV Generation) Domain

1.    
Local Functions (by DER Owners/Operators, which include
Commercial Customers, Industrial Customers, Residential Customers, and
Distribution Utilities). The DER can be located at a customer site or
at a utility site, such as in a substation.  The DER owner/operator
owns and operates the DER directly (no third party).

a.    
DER owner/operator uses DER as automatic backup for key
internal load if main power is lost or may be lost (e.g.  diesel
generator).  The DER system undertakes automatic start of DER device,
disconnects Area EPS, synchronizes and interconnects DER to local EPS,
and performs generation control to meet changing load requirements.

b.    
DER owner/operator sets DER at a specific setpoint to provide a
set level of generation (e.g.  to offset load, to provide local
generation for reliability and/or demand-response, to shave peaks).

c.    
DER owner/operator establishes a permanent building/campus
microgrid (e.g.  utility power as backup)

d.    
DER owner/operator uses DER for internal loads following with
import/export interconnection to Area ESP, set for fixed import/export

e.    
CHP or other factors drive the use of DER with net zero
import/export, so Area EPS is used strictly as backup, so heat
information is also required

f.     
Heat is main purpose for heating hospitals – feed power back to
the networked distribution grid in downtown New Orleans.  Monitored
for power flow when it is on.

g.    
Contractual establishment possibility of microgrids during
power outage or peak shaving.  The DER owners are responsible for
actually establishing the microgrid.  Although no data exchanges now,
in the future they will want far more data and possible control over
the process.

h.    
Greenpower demonstration house with net revenue and
instantaneous metering on residential (up to 25 kW and small
commercial up to 100 kW) – developing load curves from load
monitoring, including after an outage.

i.      
DER owner plans the scheduling/bidding of DER generation in
electricity marketplace, for energy, as ancillary services, as
contracted, as per real-time pricing, etc.  The DER operator then
executes the schedules as required.

j.     
DER operator manages DER system maintenance, including DER
generator, prime mover, local EPS switching and protection,
communications system, and the monitoring and control system

k.    
DER system collects information, logs, and statistics,
including operational information, performance, efficiency, emissions,
environmental parameters, green power %, etc.  This information may be
available in real-time as well as historical.

2.    
Third-Party Remote Operator or Aggregator Functions (by ESP or
DisCo or Other e.g.  RTO/ISO). The DER can be located at a customer
site or at a utility site, such as in a substation.  The DER is
operated by a third party from a remote site.  The third party could
be an Aggregator, and Energy Services Provider, a utility, or other
entity.

a.    
Remote operator monitors generator status only (on/off)

b.    
Remote operator monitors instantaneous metering (status,
alarms, kW output, voltage, amps, statistics, etc.)

c.    
Remote operator monitors DER environment (prime mover, weather,
emissions, protective relays, switches, etc.)

d.    
Remote operator or Aggregator dispatches a local operator to
manually control the DER device.

e.    
Make-before-break DER system picks up local load, then
disconnects from the Area EPS; diesel recips; startup, isolation,
verification, real-time metering, revenue metering both at the PCC and
at the DER, as well as submetering, stop

f.     
Dispatch pricing signal – DisCo dispatches DER on (to run at
full power) or off

g.    
Remote operator or Aggregator sets DER at a specific setpoint
to provide a fixed amount of generation (e.g.  to offset load, to
provide local generation for reliability and/or demand-response, to
shave peaks).

h.    
AGC – Remote operator (e.g.  RTO/ISO or utility) or Aggregator
controls DER operations through automatic control to meet specified
operational needs and contracts (e.g.  power quality, emissions,
economic dispatch, energy schedules, ancillary service contracts,
real-time pricing, local backup, interconnection with distribution
system)

i.      
Remote operator dispatches field crew to perform manual
switching operations on feeders with DER present

j.     
Remote operator performs supervisory control of switching
operations on feeders with DER present

k.    
Remote operator performs supervisory control of load tap
changers and/or voltage controllers with DER present

l.      
Remote operator aggregates multiple DER device information for
DisCo SCADA system

m.  
Remote operator provides DER owners, DisCo, and/or market
operators with the results and other information on DER operations

n.    
Remote operator manages local microgrid operations with DER

o.    
Net metering – ESP or DisCo manages and reads revenue meters
for DER and loads

p.    
ESP or DisCo handles settlements and billing for DER owner

q.    
Regulators and auditors monitor compliance of DER operations
with contractual and environmental commitments

3.    
Automated Distribution Operations (ADO) Functions (by
Distribution Utility) Supported by Advanced Distribution Automation
(ADA). The DER can be located at a customer site or at a utility site,
such as in a substation.  Multiple points of common coupling (PCCs) of
multiple DRs along a feeder need to be taken into account.  The DER is
operated by a distribution utility specifically to meet its normal
operational needs, particularly if there is significant penetration of
DER on some of its feeders or in its substations.  These operational
needs can include power system reliability, power system efficiency,
power quality assessment, outage management, market operations, and
maintenance.

a.    
ADO collects and analyzes distribution operations with
significant DER penetration (multiple PCCs), including basic SCADA,
distribution state estimation and operational analysis, status
estimation of controllable devices, load modeling and analysis,
reliability assessment, dynamic limit calculations, power quality
analysis, etc.

b.    
ADO operates a DER system in a substation or other utility
facility for additional local generation and ancillary services.

c.    
ADO, supported by ADA, provides quality power to customers
under normal conditions and/or as a result of predicted adverse
conditions, based on coordinated volt-var control, contingency
analysis, multi-level feeder reconfiguration, relay protection
re-coordination, feeder phase load and voltage balancing, etc.

d.    
ADO manages DER and distribution facilities planned outages,
using Advanced Distribution Automation (ADA) applications in
study/look-ahead mode, covering distribution operations analysis, DER
availability analysis, multi-level feeder reconfiguration, coordinated
volt-var control, reliability assessment, cold load pickup, work order
creation.

e.    
ADO, supported by ADA, supports market operations for DisCo,
through load forecasting with DER availability and dispatchable load
analysis, look-ahead distribution system analysis, contract-oriented
loss calculations, coordinated volt-var with real-time pricing, etc.

f.     
ADO supports distribution and DER maintenance, by providing
performance and historical statistics of DER and distribution
equipment, as well as risk assessments based on these statistics

g.    
ADO, supported by ADA, coordinates distribution and DER
operations with bulk power system operations, including real and
reactive load/DER management, load shedding, load/DER transfer to
different feeders, etc.

h.    
ADO, supported by ADA,  supports customer services, through
power quality assessment and management, real-time pricing analysis,
and performance analysis

i.      
ADO, supported by ADA,  manages DER interconnected with the
utility grid, through DER forecasting and scheduling, microgrid
creation and management, injection and storage management,
interconnection design, and performance monitoring

j.     
ADO supports database management through asset management,
database consistency management, and database validation management.

4.    
Emergency Operations Functions. The DER can be located at a
customer site or at a utility site, such as in a substation.  The DER
is operated by a distribution utility specifically to meet its
emergency operational needs, particularly if there is significant
penetration of DER on some of its feeders or in its substations. 
These emergency needs can include protection schemes and actions, load
shedding, alarm management, disturbance monitoring, emergency
switching, and establishment of microgrids.

a.    
Protection equipment performs system protection actions on DER
interconnections – fault detection, clearing, and reclosing

b.    
Distribution operator directly trips or verifies trip of
interconnected DER on loss of feeder power

c.    
Distribution operators manage emergency alarms from DER devices

d.    
SCADA system performs disturbance monitoring analysis,
including DER responses

e.    
ADO, supported by ADA, manages forced outages of DER and
distribution facilities, by supporting automated fault clearing
(protective devices), fault indication, fault location, fault
isolation, dynamic limit calculation, service restoration (manual or
closed-loop switching), volt-var adjustment, DER control, microgrid
creation, cold load pickup, paralleling check, relay re-coordination,
etc.

f.     
Operators dispatch field crews to troubleshoot system and
customer power problems

g.    
Operators dispatch field crews to troubleshoot communication
system and customer communication problems

h.    
Operators perform switching operations involving DER
interconnections

i.      
Operators shed loads and/or DER devices intentionally

j.     
Outage management systems collect trouble calls and generate
outage information

k.    
Microgrids of DER devices matched to loads are formed,
operated, and eventually connected back into the distribution system

5.    
Planning, Installation, Commissioning, and Maintenance
Functions (by DER Owners, Energy Service Providers (ESP), and DisCos).
Planning and implementation of DER involves longer term activities,
with multiple parties involved to design, test, and audit DER systems.

a.    
DER sizing, technology, configuration, and installation is
planned and coordinated with DisCo, by providing ratings,
configurations, planned usage, etc.

b.    
Distribution planners study the impact of planned DER
installations on the distribution system, and integrate these results
with other distribution upgrades and additions, as well as ADA
settings

c.    
Installer installs and tests DER devices in the local EPS

d.    
Distribution utility tests DER installation with
interconnection to area EPS

e.    
Distribution utility interacts with DER owner on DER
installation physical and electrical configuration, contractual
arrangements, planned operations, and/or other information

f.     
DER operator tests DER communications system performance and
management

g.    
Vendors of different equipment (including DER systems,
switches, protection, and communications system) gather real-time data
and statistics, and perform troubleshooting of their own equipment.

h.    
DER maintainer maintains DER system

i.      
DER environmental monitoring

j.     
Energy Service Provider meets contractual obligations for
managing the DER system.

## Customer Services Domain

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

## IT Services Domain

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
