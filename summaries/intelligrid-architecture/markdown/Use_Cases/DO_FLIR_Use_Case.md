# Fault Loc, Iso, & Restore

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DO_FLIR_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Fault Location, Isolation and Service Restoration (FLIR)

This application detects the fault, determines
the faulted section and the probable location of fault, and recommends
an optimal isolation of the faulted portions of the distribution
feeder and the procedures for the restoration of services to its
healthy portions. The key sub-functions performed by the application
are as follows:

## Fault Location

This sub-function is initiated by SCADA inputs,
such as lockouts, fault indications/location, and, also, by inputs
from OMS, and, in the future, by inputs from fault-predicting
devices.  It determines the specific protective device, which has
cleared the sustained fault, identifies the de-energized sections, and
estimates the probable place of the actual or the expected fault. It
distinguishes faults cleared by controllable protective devices from
those cleared by fuses, and identifies momentary outages and
inrush/cold load pick-up currents.

## Fault Isolation and Service Restoration

This sub-function supports three modes of
operation:

1.      
Closed-loop mode, in which the sub-function is initiated by the Fault
location sub-function. It generates a switching order (i.e., sequence)
for the remotely controlled switching devices to isolate the faulted
section, and restore service to the non-faulted sections. The
switching order is automatically executed via SCADA.  .

2.      
Advisory mode, in which the sub-function is initiated by the Fault
location sub-function. It generates a switching order for remotely-
and manually-controlled switching devices to isolate the faulted
section, and restore service to the non-faulted sections. The
switching order is presented to operator for approval and execution

3.      
Study mode, in which the sub-function is initiated by the user. It
analyzes a saved case modified by the user, and generates a switching
order under the operating conditions specified by the user.

If during execution, there is change in
connectivity, the sub-function interrupts the execution and
re-optimizes the solution based on new conditions. If during service
restoration, there is another fault, the sub-function runs again
considering a new fault scenario. When work is completed, the
sub-function is instructed to generate a switching order for
restoration of the normal configuration. The generated switching
orders are based on considering the availability of remotely
controlled switching devices, feeder paralleling, creation of islands
supported by distributed energy resources, and on cold-load pickup
currents.

### Services

* ADA indicates faults cleared by controllable protective
  devices by distinguishing between:

> > a)
> > faults cleared by fuses
> >
> > b)
> > momentary outages
> >
> > c)
> > inrush/cold load current

* ADA determines the faulted sections based on SCADA fault
  indications and protection lockout signals
* ADA estimates the probable fault locations based on
  SCADA fault current measurements and real-time fault
  analysis
* ADA determines the fault-clearing non-monitored
  protective device based on trouble call inputs and dynamic
  connectivity model
* ADA generates switching orders for fault isolation,
  service restoration, and return to normal (taking into
  account the availability of remotely controlled switching
  devices, feeder paralleling, and cold-load pickup):

> > a) Operator executes switching
> > orders by using SCADA
> >
> > b)
> > Operator authorizes ADA application to execute
> > switching orders in closed-loop mode

* ADA isolates the fault and restores service
  automatically by-passing the operator based on operator’s
  authorization in advance
* ADA pre-arms Distributed Intelligence schemes
* ADA considers creation of islands supported by
  distributed resources for service restoration

## Steps

The following FLIR functions are described:

* [FLIR First Fault with Only Manual Switches](DO_FLIR_Use_Case.htm#FLIR First Fault with Only Manual Switches)
* [FLIR Second Fault (Related to First Fault which is Not
  Resolved Yet) with Only Manual Switches](DO_FLIR_Use_Case.htm#FLIR Second Fault (Related to First Fault which is Not Resolved Yet) with Only Manual Switches)
* [FLIR Fault with Remotely-Controlled and Manual Switches](DO_FLIR_Use_Case.htm#FLIR Fault with Remotely-Controlled and Manual Switches)
* [FLIR Fault with Remotely-Controlled and Manual Switches and
  Distributed Intelligence System (DIS)](DO_FLIR_Use_Case.htm#FLIR Fault with Remotely-Controlled and Manual Switches and Distributed Intelligence System (DIS))
* [FLIR Fault with DER Connected to Healthy Section](DO_FLIR_Use_Case.htm#FLIR Fault with DER Connected to Healthy Section)

### FLIR First Fault with Only Manual Switches

if !vml?![](DO_FLIR_Use_Case_files/image002.jpg)endif?

 

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1.1 | FLIR first fault with only manual switches | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology. It also provides the latest relevant analog data. | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.2 |  | Checking real-time data | DOMA function receives the scan of Energy Management System SCADA data to be checked for relevant changes or events. | Energy Management System SCADA database | DOMA function | Energy Management System real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.3 |  | Checking real-time data | DOMA function receives the scan of environmental data to be checked for changes affecting DER performance forecast. | Environmental daily data collector | DOMA function | Real-time environmental data for DER schedule forecast | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.4 |  | Checking real-time data | DOMA function receives the scan of latest schedules of presently active or authorized for future outages to be checked for changes during the time of repair. | Outage Management System | DOMA function | Schedules of presently active or authorized for future outages | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.5 |  | ADA Topology Update System changes connectivity | After DOMA detects fault in distribution, relevant information is provided to topology function. | DOMA function | ADA Topology Update System | Circuit breaker lockouts, inputs from Outage Management System | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.6 |  | ADA Topology Update System changes connectivity | After fault is detected, ADA database is updated. | ADA Topology Update System | ADA Database | Update of ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.7 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Topology function initiates fault location sub-function of the FLIR function. | ADA Topology Update System | FLIR function | Fault location sub-function initiation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.8 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Fault location sub-function receives the needed data from ADA database after it was updated with fault information. | ADA Database | FLIR function | Excerpts from ADA database updated after fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.9 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Fault location sub-function provides the System Operator with information needed for him to make operational decisions, i.e., dispatching the field crew, etc. | FLIR function | System Operator | Circuit breaker lockouts, inputs from Outage Management System, fault-related de-energized sections | User Interface |
| 2.1.10 |  | Fault- location relay informs System Operator | System Operator receives distances to fault location provided by the fault location relay. | Fault location function | System Operator | Distances to fault location | User Interface |
| 2.1.12 |  | System Operator informs field crew | System Operator authorizes to patrol the faulted line to locate fault and perform binary search if needed. | System Operator | Field Personnel | Authorization to patrol faulted line | User Interface |
| 2.1.13 |  | Field Personnel informs System Operator | After locating the fault, the crew informs the System Operator about the status of switches involved in initial fault isolation. | Field Personnel | System Operator | Status of switches involved in initial fault isolation | User Interface |
| 2.1.14, 2.1.15 |  | Entering status of switches and faulted section into ADA database | The System Operator enters status of switches (pseudo-statuses) involved in initial fault isolation and the faulted section into ADA database. | System Operator | ADA Database | ADA database update after initial fault isolation | User Interface |
| 2.1.16 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | By entering the faulted section into the ADA database, the System Operator initiates fault isolation and service restoration sub-function. | System Operator | FLIR | Initiation of fault isolation and service restoration sub-function | User Interface |
| 2.1.17 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated after initial fault isolation. | ADA Database | FLIR function | ADA database excerpts updated after initial fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.18 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report for archiving in ADA historic database | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1.19 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A generated list of recommended switching orders is presented to the System Operator. | FLIR function | System Operator | List of recommended switching orders | User Interface |
| 2.1.20 |  | System Operator informs field crew | System Operator selects a switching order and authorizes its implementation. | System Operator | Field Personnel | Switching order authorized for implementation | User Interface |
| 2.1.21 |  | Field Personnel informs System Operator | Upon final isolation and service restoration to healthy sections, the field crew informs the System Operator about final status of relevant switches (cuts). | Field Personnel | System Operator | Status of switches involved in final fault isolation and service restoration to healthy sections. | User Interface |
| 2.1.22, 2.1.23 |  | Entering status of switches involved in final fault isolation and service restoration to healthy sections into ADA database | The System Operator enters status of switches/cuts (pseudo-statuses) involved in final fault isolation and service restoration to healthy sections into ADA database | System Operator | ADA Database | ADA database update after final fault isolation and service restoration | User Interface |
| 2.1.24 |  | FLIR updates the switching order in accord with the final fault isolation | System Operator receives the final switching order from FLIR and dispatched the crew to implement it | FLIR,  System Operator | System Operator,  Field Personnel | Switching order, instructions to the crew | User Interface |

### FLIR Second Fault (Related to First Fault which is Not Resolved Yet) with Only Manual Switches

 

if !vml?![](DO_FLIR_Use_Case_files/image004.jpg)endif?

 

| # | Event | Name of Process/Activity | | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.2.1 | FLIR second fault (related to first fault which is not resolved yet) with only manual switches | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology. It also provides the latest relevant analog data. | | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data at time of first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.2 |  | Checking real-time data | DOMA function receives the scan of Energy Management System SCADA data to be checked for relevant changes or events. | | Energy Management System SCADA database | DOMA function | Energy Management System real-time analog, status, TLQ data at time of first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.3 |  | Checking real-time data | DOMA function receives the scan of environmental data to be checked for changes affecting DER performance forecast. | | Environmental daily data collector | DOMA function | Real-time environmental data for DER schedule forecast at time of first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.4 |  | Checking real-time data | DOMA function receives the scan of latest schedules of presently active or authorized for future outages to be checked for changes. | | Outage Management System | DOMA function | Schedules of presently active or authorized for future outages at time of first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.5 |  | ADA Topology Update System changes connectivity | After DOMA detects first fault in distribution, relevant information is provided to topology function. | | DOMA function | ADA Topology Update System | First fault: circuit breaker lockouts, inputs from Outage Management System | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.6 |  | ADA Topology Update System changes connectivity | After first fault is detected, ADA database is updated. | | ADA Topology Update System | ADA Database | Update of ADA database after first fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.7 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | After the first fault is detected, topology function initiates fault location sub-function of the FLIR function. | | ADA Topology Update System | FLIR function | Fault location sub-function initiation after first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.8 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Fault location sub-function receives the needed data from ADA database after it was updated with the first fault information. | | ADA Database | FLIR function | Excerpts from ADA database updated after first fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.9 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Fault location sub-function provides the System Operator with information on the first fault needed for him to make operational decisions, i.e., dispatching the field crew, etc. | | FLIR function | System Operator | First fault: circuit breaker lockouts, inputs from Outage Management System, fault-related de-energized sections | User Interface |
| 2.2.10 |  | System Operator informs field crew | System Operator authorizes to patrol the faulted line to locate first fault and perform binary search if needed. | | System Operator | Field Personnel | Authorization to patrol faulted line to locate first fault | User Interface |
| 2.2.11 |  | Field Personnel informs System Operator | After locating the first fault, the crew informs the System Operator about the status of switches involved in initial fault isolation. | | Field Personnel | System Operator | Status of switches involved in initial first fault isolation | User Interface |
| 2.2.12, 2.2.13 |  | Entering status of switches and faulted section into ADA database | The System Operator enters status of switches (pseudo-statuses) involved in initial first fault isolation and the faulted section into ADA database. | | System Operator | ADA Database | ADA database update after initial isolation of first fault | User Interface |
| 2.2.14 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | By entering the faulted section, associated with first fault, into the ADA database, the System Operator initiates fault isolation and service restoration sub-function. | | System Operator | FLIR | Initiation of fault isolation and service restoration sub-function | User Interface |
| 2.2.15 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated after initial first fault isolation. | | ADA Database | FLIR function | ADA database excerpts updated after initial isolation of first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.16 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report after the first fault for archiving in ADA historic database | | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers after first fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.17 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A generated list of recommended switching orders related to first fault is presented to the System Operator. | | FLIR function | System Operator | List of recommended switching orders related to first fault | User Interface |
| 2.2.18 | FLIR second fault (related to first fault which is not resolved yet) with only manual switches | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology. It also provides the latest relevant analog data. | | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data at time of second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.19 |  | Checking real-time data | DOMA function receives the scan of Energy Management System SCADA data to be checked for relevant changes or events. | | Energy Management System SCADA database | DOMA function | Energy Management System real-time analog, status, TLQ data at time of second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.20 |  | Checking real-time data | DOMA function receives the scan of environmental data to be checked for changes affecting DER performance forecast. | | Environmental daily data collector | DOMA function | Real-time environmental data for DER schedule forecast at time of second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.21 |  | Checking real-time data | DOMA function receives the scan of latest schedules of presently active or authorized for future outages to be checked for changes. | | Outage Management System | DOMA function | Schedules of presently active or authorized for future outages at time of second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.22 |  | ADA Topology Update System changes connectivity | After DOMA detects second fault in distribution, relevant information is provided to topology function. | | DOMA function | ADA Topology Update System | Second fault: circuit breaker lockouts, inputs from Outage Management System | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.23 |  | ADA Topology Update System changes connectivity | After second fault is detected, ADA database is updated. | | ADA Topology Update System | ADA Database | Update of ADA database after second fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.24 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | After the second fault is detected, topology function initiates fault location sub-function of the FLIR function. | | ADA Topology Update System | FLIR function | Fault location sub-function initiation after second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.25 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Fault location sub-function receives the needed data from ADA database after it was updated with the second fault information. | | ADA Database | FLIR function | Excerpts from ADA database updated after second fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.26 |  | Fault isolation and service restoration sub-function determines whether second fault impacts switching for first fault | Fault isolation and service restoration sub-function determines whether second fault impacts switching for first fault. | | FLIR function | FLIR function | Second fault: circuit breaker lockouts, inputs from Outage Management System, fault-related de-energized sections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.27 |  | Fault isolation and service restoration sub-function determines whether second fault impacts switching for first fault | Fault isolation and service restoration sub-function cancels the previous switching order if it needs to. | | FLIR function | System Operator | Cancellation of first-fault-related switching order | User Interface |
| 2.2.28 |  | System Operator informs field crew | System Operator authorizes to patrol the faulted line to locate second fault and perform binary search if needed. | | System Operator | Field Personnel | Authorization to patrol faulted line to locate second fault | User Interface |
| 2.2.29 |  | Field Personnel informs System Operator | After locating the second fault, the crew informs the System Operator about the status of switches involved in initial second fault isolation. | | Field Personnel | System Operator | Status of switches involved in initial second fault isolation | User Interface |
| 2.2.30, 2.2.31 |  | Entering status of switches and faulted section into ADA database | The System Operator enters status of switches (pseudo-statuses) involved in initial second fault isolation and the faulted section into ADA database. | | System Operator | ADA Database | ADA database update after initial isolation of second fault | User Interface |
| 2.2.32 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | By entering the faulted section, associated with second fault, into the ADA database, the System Operator initiates fault isolation and service restoration sub-function for both faults. | | System Operator | FLIR | Initiation of fault isolation and service restoration sub-function | User Interface |
| 2.2.33 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated after initial second fault isolation. | | ADA Database | FLIR function | ADA database excerpts updated after initial isolation of second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.34 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report after the second fault for archiving in ADA historic database | | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers after second fault | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2.35 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A generated list of recommended switching orders related to both faults is presented to the System Operator. | | FLIR function | System Operator | List of recommended switching orders related to second fault | User Interface |
| 2.2.36 |  | System Operator informs field crew | System Operator selects a switching order and authorizes its implementation. | | System Operator | Field Personnel | Switching order authorized for implementation after second fault | User Interface |
| 2.2.37 |  | Field Personnel informs System Operator | Upon final isolation and service restoration to healthy sections, the field crew informs the System Operator about final status of relevant switches for the  second fault. | | Field Personnel | System Operator | Status of switches involved in final fault isolation and service restoration to healthy sections after second fault. | User Interface |
| 2.2.38, 2.2.39 |  | Entering status of switches involved in final fault isolation and service restoration to healthy sections into ADA database | The System Operator enters status of switches (pseudo-statuses) involved in final fault isolation and service restoration to healthy sections into ADA database | | System Operator | ADA Database | ADA database update after final fault isolation and service restoration | User Interface |
| 2.2.40 | FLIR | System Operator receives the final switching order from FLIR and dispatched the crew to implement it | FLIR,  System Operator | | System Operator | Field Personnel | Switching order, instructions to the crew | User Interface |
if !supportMisalignedColumns?|  |  |  |  |  |  |  |  |  |
endif?

### FLIR Fault with Remotely-Controlled and Manual Switches

if !vml?![](DO_FLIR_Use_Case_files/image006.jpg)endif?

 

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.3.1 | FLIR fault with remotely-controlled and manual switches | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology. It also provides the latest relevant analog data. | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.2 |  | Checking real-time data | DOMA function receives the scan of Energy Management System SCADA data to be checked for relevant changes or events. | Energy Management System SCADA database | DOMA function | Energy Management System real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.3 |  | Checking real-time data | DOMA function receives the scan of environmental data to be checked for changes affecting DER performance forecast. | Environmental daily data collector | DOMA function | Real-time environmental data for DER schedule forecast | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.4 |  | Checking real-time data | DOMA function receives the scan of latest schedules of presently active or authorized for future outages to be checked for changes. | Outage Management System | DOMA function | Schedules of presently active or authorized for future outages | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.5 |  | Checking real-time data | DOMA function receives the distance to fault location, which is provided by Fault location function in the presence of the fault. | Fault location function | DOMA function | Distance to fault location | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.6 |  | ADA Topology Update System changes connectivity | After DOMA detects fault in distribution, relevant information is provided to topology function. | DOMA function | ADA Topology Update System | Circuit breaker lockouts, inputs from Outage Management System | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.7 |  | ADA Topology Update System changes connectivity | After fault is detected, ADA database is updated. | ADA Topology Update System | ADA Database | Update of ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.8 |  | Fault location sub-function identifies fault-related protective devices and de-energized sections | Topology function initiates fault location sub-function of the FLIR function. | ADA Topology Update System | FLIR function | Fault location subfunction initiation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.9 |  | Fault location subfunction identifies fault-related protective devices and de-energized sections | Fault location subfunction receives the needed data from ADA database after it was updated with fault information. | ADA Database | FLIR function | Excerpts from ADA database updated after fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.10 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault location subfunction initiates fault isolation and service restoration sub-function of the FLIR function. | Fault location function | Fault isolation and service restoration subfunction | Fault isolation and service restoration sub-function initiation, probable fault location with alternatives | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.11 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated with fault information. | ADA Database | FLIR function | ADA database excerpts | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.12 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report for archiving in ADA historic database. | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers before additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.13a |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A list of recommended switching orders using remotely controlled switches is presented to the System Operator. | FLIR function | System Operator | List of switching orders recommended after fault detection | User Interface |
| 2.3.13b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | In advisory mode, System Operator considers the list of switching order alternatives and selects the best SO based on predefined criteria | FLIR function | System Operator | List of switching orders recommended after fault detection | User Interface |
| 2.3.14a |  | SO execution | In the advisory mode, the System Operator, after reviewing SO, issues supervisory commands to execute it. | System Operator | DMS SCADA database | Supervisory command to execute SO issued after fault detection | User Interface |
| 2.3.14b |  | SO execution | In the closed-loop mode, FLIR issues command to execute the best SO. | FLIR | DMS SCADA database | Supervisory command to execute SO issued after fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.15 |  | System Operator informs field crew | System Operator authorizes to patrol the faulted section to accurately locate the fault and perform binary search if needed. | System Operator | Field Personnel | Authorization to patrol faulted line | User Interface |
| 2.3.16 |  | Field Personnel informs System Operator | After accurately locating the fault, the crew informs the System Operator about the status of switches involved in additional switching to isolate the smallest possible faulted section. | Field Personnel | System Operator | Status of switches involved in isolating the smallest possible faulted section | User Interface |
| 2.3.17, 2.3.18 |  | Entering status of switches and faulted section into ADA database | The System Operator enters status of switches (pseudo-statuses) involved in finall fault isolation and the faulted section into ADA database. | System Operator | ADA Database | ADA database update additional fault isolation | User Interface |
| 2.3.19 |  | Entering status of switches and faulted section into ADA database | Entering the faulted section into ADA database initiates FLIR for generating final SO | ADA Database | FLIR | Fault isolation and service restoration sub-function initiation after additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.20 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated after additional fault isolation. | ADA Database | FLIR function | ADA database excerpts | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.21 |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report for archiving in ADA historic database. | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers after additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3.22a |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A list of recommended final switching orders is presented to the System Operator. | FLIR function | System Operator | List of switching orders recommended after additional fault isolation | User Interface |
| 2.3.23a |  | SO execution | In the advisory mode, the System Operator, after reviewing SO, issues supervisory commands to execute it. | System Operator | DMS SCADA database | Supervisory command to execute SO issued after additional fault isolation | User Interface |
| 2.3.23b |  | SO execution | In the closed-loop mode, FLIR issues commands to execute SO. | FLIR | DMS SCADA database | Supervisory command to execute SO issued after additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |

### FLIR Fault with Remotely-Controlled and Manual Switches and Distributed Intelligence System (DIS)

if !vml?![](DO_FLIR_Use_Case_files/image008.jpg)endif?

 

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.4.1a | Fault with remotely-controlled and manual switches and with DIS | DIS identifies relevant protective device, de-energized sections and probable fault location and finds service restoration solution | Distributed Intelligence System (DIS) receives the real-time local status and analog data. | IEDs of DIS members | Distributed Intelligence Schemes | Real-time local status and analog data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.2a |  | DIS identifies relevant protective device, de-energized sections and probable fault location and finds service restoration solution | DIS communicates to DIS members the switching instructions for fault isolation and service restoration. | Distributed Intelligence Schemes | IEDS of DIS members | Command to isolate fault and restore service to healthy sections. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.3a |  | DIS identifies relevant protective device, de-energized sections and probable fault location and finds service restoration solution | Changes in connectivity implemented by DIS are downloaded into DMS SCADA database. | Distributed Intelligence Schemes | DMS SCADA database | Changes in connectivity implemented by DIS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.4a |  | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology. It also receives the latest relevant analog data. | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data, phasor data from WAMACS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.5a |  | Checking real-time data | ADA Topology Update System receives the changes in connectivity implemented by DIS | DOMA function | ADA Topology Update System | Changes in connectivity implemented by DIS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.6a |  | ADA Topology Update System changes connectivity | ADA database is updated with changes in connectivity implemented by DIS | ADA Topology Update System | ADA Database | Changes in connectivity implemented by DIS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.1b |  | DIS identifies relevant protective device, de-energized sections and probable fault location and can not find service restoration solution | Distributed Intelligence System (DIS) receives real-time local status and analog data. | IEDs of DIS members | Distributed Intelligence Schemes | Real-time status and analog data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.2b |  | DIS identifies relevant protective device, de-energized sections and probable fault location and can not find service restoration solution | Indication of DIS inability to find a solution is downloaded into DMS SCADA database. | Distributed Intelligence Schemes | DMS SCADA database | Indication of DIS inability to find a solution | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.3b |  | Checking real-time data | Due to DIS inability to find a solution, ADA is initiated. | DMS SCADA database | DOMA function | Command to initiate ADA, DMS real-time analog, status & TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.4b |  | Checking real-time data | DOMA function receives the scan of latest schedules of presently active or authorized for future outages to be checked for changes. | Outage Management System | DOMA function | Schedules of presently active or authorized for future outages | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.5b |  | Checking real-time data | DOMA function receives the scan of Energy Management System SCADA data to be checked for relevant changes or events. | Energy Management System SCADA database | DOMA function | Energy Management System real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.6b |  | Checking real-time data | DOMA function receives the scan of environmental data to be checked for changes affecting DER schedule forecast. | Environmental daily data collector | DOMA function | Real-time environmental data for DER schedule forecast | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.7b |  | Checking real-time data | DOMA function receives the distance to fault location, which is provided by fault-locating relay in the presence of the fault. | Fault location function | DOMA function | Distance to fault location | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.8b |  | ADA Topology Update System changes connectivity | After DOMA detects fault in distribution, relevant information is provided to topology function. | DOMA function | ADA Topology Update System | Circuit breaker lockouts, inputs from Outage Management System | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.9b |  | ADA Topology Update System changes connectivity | After fault is detected, ADA database is updated. | ADA Topology Update System | ADA Database | Update of ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.10b |  | Fault location subfunction identifies fault-related protective devices and de-energized sections | Topology function initiates fault location sub-function of the FLIR function. | ADA Topology Update System | FLIR function | Fault location subfunction initiation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.11b |  | Fault location subfunction identifies fault-related protective devices and de-energized sections | Fault location subfunction receives the needed data from ADA database after it was updated with fault information. | ADA Database | FLIR function | Excerpts from ADA database updated after fault detection | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.12b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault location subfunction initiates fault isolation and service restoration sub-function of the FLIR function. | Fault location function | Fault isolation and service restoration subfunction | Fault isolation and service restoration sub-function initiation, probable fault location with alternatives | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.13b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated with fault information. | ADA Database | FLIR function | ADA database excerpts | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.14b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report for archiving in ADA historic database. | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers before additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.15b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A list of recommended switching orders is presented to the System Operator. | FLIR function | System Operator | List of switching orders recommended after fault detection | User Interface |
| 2.4.16b |  | SO execution | In the advisory mode, the System Operator, after reviewing SO, issues a supervisory command to execute it. | System Operator | DMS SCADA database | Supervisory command to execute SO issued after fault detection | User Interface |
| 2.4.17b |  | System Operator informs field crew | System Operator authorizes to patrol the faulted line to accurately locate fault. | System Operator | Field Personnel | Authorization to patrol faulted line | User Interface |
| 2.4.18b |  | Field Personnel informs System Operator | After locating the fault, the crew informs the System Operator about the status of switches involved in additional switching to isolate the smallest possible faulted section. | Field Personnel | System Operator | Status of switches involved in isolating the smallest possible faulted section | User Interface |
| 2.4.19b, 2.4.20b |  | Entering status of switches and faulted section into ADA database | The System Operator enters status of switches (pseudo-statuses) involved in final fault isolation and the faulted section into ADA database. | System Operator | ADA Database | ADA database update additional fault isolation | User Interface |
| 2.4.21b |  | Entering status of switches and faulted section into ADA database | Entering the faulted section into ADA database initiates FLIR | ADA Database | FLIR | Fault isolation and service restoration sub-function initiation after additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.22b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | Fault isolation and service restoration sub-function receives ADA database excerpts updated after additional fault isolation. | ADA Database | FLIR function | ADA database excerpts | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.23b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | FLIR issues a report for archiving in ADA historic database. | FLIR function | ADA Historic Database | Report including interrupted, un-served and restored load, and number of customers after additional fault isolation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4.24b |  | Fault isolation and service restoration sub-function generates list of recommended switching orders | A list of recommended switching orders is presented to the System Operator. | FLIR function | System Operator | List of switching orders recommended after additional fault isolation | User Interface |
| 2.4.25b |  | SO execution | The System Operator, after reviewing SO, issues a supervisory command to execute it, if remotely controlled switches are used. If manual switches are involved, the System Operator dispatches the crew to implement the switching order. | System Operator | DMS SCADA database | Supervisory command to execute SO issued after additional fault isolation; instructions for the crew. | User Interface |

### FLIR Fault with DER Connected to Healthy Section

if !vml?![](DO_FLIR_Use_Case_files/image010.jpg)endif?

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.5.1 | Fault in a circuit with DER connected to healthy section cleared by fast circuit breaker trip and by reverse protection from DER fault injection creating a self-sufficient island | Unintentional self-sufficient island is created | DOMA receives the scan of DMS SCADA data and historic load data to be checked for changes in topology and loading during the time of repair. | DMS SCADA database | DOMA | DMS real-time analog, status & TLQ data, phasor data from WAMACS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5.2a |  | Checking the sufficiency of the island during the time of repair | DOMA determines the sufficiency of the island during the time of repair and enables FLIR for location of the fault within the de-energized section. | DOMA | FLIR | Instructions to FLIR | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5.2b |  | Checking the sufficiency of the island during the time of repair | DOMA determines the insufficiency of the island during the portion of time of repair and enables FLIR for location of the fault within the de-energized section and solving restoration for the customers connected to the island. | DOMA | FLIR | Instructions to FLIR | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5.3 | Fault in a circuit with DER connected to healthy section cleared by fast circuit breaker trip and by reverse protection from DER fault injection, creating an insufficient island | Unintentional insufficient island is created, DER is separated with or without balanced load | DOMA receives the scan of DMS SCADA data and historic load data to be checked for changes in topology and loading during the time of repair. | DMS SCADA database | DOMA | DMS real-time analog, status & TLQ data, phasor data from WAMACS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5.4 |  | Checking the sufficiency of the island during the time of repair | DOMA determines the insufficiency of the island during the time of repair and enables FLIR for location of the fault within the de-energized section and solving restoration for the de-energized customers connected to the island. | DOMA | FLIR | Instructions to FLIR | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5.5 | Fault in a circuit with DER connected to healthy section cleared by circuit breaker and by relay protection of DER at the PCC | The feeder is de-energized, DER is separated with or without balanced load | DOMA receives the scan of DMS SCADA data and historic load data to be checked for changes in topology and loading during the time of repair. | DMS SCADA database | DOMA | DMS real-time analog, status & TLQ data, phasor data from WAMACS | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5.6 |  | Checking the topology to ensure that DER is separated | DOMA determines the after-fault topology, the loading during the time of repair, and enables FLIR for location of the fault and solving isolation of the fault and restoration for the de-energized customers connected to the healthy portions of the feeder. | DOMA | FLIR | Instructions to FLIR | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
