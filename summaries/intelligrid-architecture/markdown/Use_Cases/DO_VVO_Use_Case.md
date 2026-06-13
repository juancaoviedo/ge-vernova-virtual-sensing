# Volt Var Optim

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DO_VVO_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Distribution Operations - Voltage and Var Control (VVC) Function

## Contents

* [Narrative](DO_VVO_Use_Case.htm#Narrative)
* [VVC
  Function During Scheduled Run](DO_VVO_Use_Case.htm#VVC Function During Scheduled Run)
* [VVC Function
  During Event Run](DO_VVO_Use_Case.htm#VVC Function During Event Run)
* [VVC Function Participation in Severe Emergency in Bulk Power
  System with Intentional Islands](DO_VVO_Use_Case.htm#VVC Function Participation in Severe Emergency in Bulk Power System with Intentional Islands)

## Narrative

This application calculates the optimal settings
of voltage controller of LTCs, voltage regulators, DERs, power
electronic devices, and capacitor statuses optimizing the operations
by either following different objectives at different times, or
considering conflicting objectives together in a weighted manner.

It supports three modes of operation:

1.      
Closed-loop mode, in which the application runs either periodically
(e.g., every 15 min) or is triggered by an event (i.e., topology or
objective change), based on real-time information. The application’s
recommendations are executed automatically via SCADA control commands.

2.      
Study mode, in which the application performs “what-if” studies, and
provides recommended actions to the operator.

3.      
Look-ahead mode, in which conditions expected in the near future can
be studied (from 1 hour through 1 week) by the operator.

The following objectives, which could be preset
for different times of the day and overwritten by operator if need to,
are supported by the application:

a.       
Minimize kWh consumption at voltages beyond given  voltage quality
limits (i.e., ensure standard voltages at customer terminals)

b.      
Minimize feeder segment(s) overload

c.       
Reduce load while respecting given voltage tolerance (normal and
emergency)

d.      
Conserve energy via voltage reduction

e.       
Reduce or eliminate overload in transmission lines

f.        
Reduce or eliminate voltage violations on transmission lines

g.       
Provide reactive power support for transmission/distribution bus

h.       
Provide spinning reserve support

i.         
Minimize cost of energy

j.        
Provide compatible combinations of above objectives

If, during optimization or execution of the
solution, the circuit status changes, the application is interrupted
and solution is re-optimized. If, during execution, some operations
are unsuccessful, solution is re-optimized without involving the
malfunctioning devices. If some of the controllable devices are
unavailable for remote control, solution does not involve these
devices but takes into account their reaction to changes in operating
conditions.

## Steps

### VVC Function During Scheduled Run

if !vml?![](DO_VVO_Use_Case_files/image002.jpg)endif?

### 

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1.1 | Time for ADA VVC Controller scheduled run | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology. It also receives the latest relevant analog data. | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data, status of voltage controllers, DER modes of operation, and settings | Intra-Control Center Environment |
| 3.1.2 |  | Checking real-time data | DOMA function receives the scan of Energy Management System SCADA data to be checked for relevant changes or events. | Energy Management System SCADA database | DOMA function | Energy Management System real-time analog, status, TLQ data | Intra-Control Center Environment |
| 3.1.3 |  | VVC performs optimization according to current objective | The fact that no events and changes in connectivity are detected is communicated to ADA VVC Controller. ADA VVC Controller is triggered by the time schedule. | DOMA function | ADA VVC Controller | No events or changes in connectivity detected, command to start scheduled run | Intra-Control Center Environment |
| 3.1.4 |  | VVC performs optimization according to current objective | VVC receives the excerpts from ADA database. | ADADatabase | ADA VVC Controller | Excerpts from ADA database | Intra-Control Center Environment |
| 3.1.5 |  | VVC performs optimization according to current objective | Relevant results of VVC optimization are displayed for the System Operator. | ADA VVC Controller | System Operator | VVC status, present and recommended bus kV, benefits, expected lowest and highest load voltage | User Interface |
| 3.1.6 |  | VVC performs optimization according to current objective | Relevant results of VVC optimization are sent to controllers in the field. | ADA VVC Controller | DMS SCADA database | Recommended settings to relevant voltage and power electronic controllers, DER modes of operation and settings, capacitor status | Intra-Control Center Environment |
| 3.1.7 |  | VVC performs optimization according to current objective | Relevant results of VVC optimization are stored in ADA historic database. | ADA VVC Controller | ADA Historic Database | VVC and LTC states and settings; VVC limits and benefits; losses, voltage, objective function and total demand before and after optimization, logs | Intra-Control Center Environment |
| 3.1.8 |  | Checking real-time data | DOMA function receives the scan of DMS SCADA data to be checked for changes in topology and confirmation of execution of VVC commands. It also provides the latest relevant analog data. | DMS SCADA database | DOMA function | DMS real-time analog, status & TLQ data, status of voltage controllers, confirmation of execution of VVC commands | Intra-Control Center Environment |
| 3.1.9 |  | Information for System Operator | System Operator’s display is regularly updated with data associated with LTC and VVC performance. | DMS SCADA database | ADA VVC Controller | VVC: status, integrity, settings, limits, bandcenter, objective;  LTC: status, position; bus voltage limits | Intra-Control Center Environment |

### VVC Function During Event Run

if !vml?![](DO_VVO_Use_Case_files/image004.jpg)endif?

### 

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.2.1-1 | ADA VVC Controller during event run | DOMA detects load voltage or overload violation | DOMA function detects load voltage or overload violation and initiates ADA VVC Controller. | DOMA function | ADA VVC Controller | Command to initiate VVC | Intra-Control Center Environment |
| 3.2.1-11,  3.2.1-111,  3.2.1-1111 |  | Checking real-time data | DOMA function checks the real-time data for changes, alarms. | DMS SCADA database | DOMA function | DMS real-time analog, status, TLQ data, confirmation of execution of VVC commands, status of voltage controllers | Intra-Control Center Environment |
| 3.2.1-12,  3.2.1-112,  3.2.1-1112 |  | Checking real-time data | DOMA function checks the real-time data for changes, alarms. | SCADA Energy Management System database | DOMA function | Energy Management System real-time analog, status, TLQ data | Intra-Control Center Environment |
| 3.2.1.13 |  | Changing current objective to load reduction within normal limits due to high energy price | DOMA function detects high-energy price and issues command to change VVC objective. | DOMA function | ADA VVC Controller | Command to change optimization objective | Intra-Control Center Environment |
| 3.2.1.14 |  | VVC performs optimization according to current objective | DOMA function issues command to initiate VVC. | DOMA function | ADA VVC Controller | Command to initiate VVC | Intra-Control Center Environment |
| 3.2.2 |  | VVC performs optimization according to current objective | ADA VVC Controller receives excerpt from ADA database updated with latest SCADA scan. | ADADatabase | ADA VVC Controller | ADA database excerpt | Intra-Control Center Environment |
| 3.2.3 |  | VVC performs optimization according to current objective | VVC issues information relevant for System Operator. | ADA VVC Controller | System Operator | VVC status, present and recommended bus kV, benefits, expected lowest and highest load voltages | User Interface |
| 3.2.4 |  | VVC performs optimization according to current objective | DMS SCADA database receives results of optimization. | ADA VVC Controller | DMS SCADA database | Recommended settings to relevant voltage and power electronic controllers, DER modes of operation and settings, capacitor status | Intra-Control Center Environment |
| 3.2.5 |  | VVC performs optimization according to current objective | Selected results are archived in ADA Historic Database. | ADA VVC Controller | ADA Historic Database | VVC and LTC states and settings; VVC limits and benefits; losses, voltage, objective function and total demand before and after optimization, logs | Intra-Control Center Environment |
| 3.2.6 |  | VVC performs optimization according to current objective | ADA VVC Controller initiates DOMA function after confirmation of execution is received. | ADA VVC Controller | DOMA function | Command to initiate DOMA | Intra-Control Center Environment |
| 3.2.7 |  | DOMA function performs analysis | DOMA function, after detecting a violation present during the after-optimization conditions, sends alarm to System Operator. | DOMA function | System Operator | Alarm for System Operator | User Interface |
| 3.2.8 |  | Prearming RAS function adjusts  settings of relevant groups of load shedding | DOMA function, after detecting that optimization has not eliminated transmission violation, sends an alarm to the System Operator and triggers pre-arming of RAS. | DOMA function | Remedial Action Scheme, System Operator | Information for prearming Remedial Action Scheme | User Interface |
| 3.2.9 |  | Data for System Operator | Relevant for System Operator VVC and LTC settings, limits and statuses are displayed. | DMS SCADA database | System Operator | VVC: status, integrity, settings, limits, bandcenter, objective LTC: status, position | User Interface |
| 3.3.1 |  | VVC determines violation can not be eliminated through optimization | DOMA function detects load voltage or voltage violation. | DOMA function | ADA VVC Controller | Command to initiate VVC | Intra-Control Center Environment |
| 3.3.2 |  | VVC determines violation can not be eliminated through optimization | VVC receives excerpts from ADA database updated with latest SCADA scan. | ADA Database | ADA VVC Controller | Excerpts from ADA database | Intra-Control Center Environment |
| 3.3.3 |  | VVC determines violation can not be eliminated through optimization | VVC initiates MFR to eliminate the violation. | ADA VVC Controller | MFR function | Command to initiate MFR | Intra-Control Center Environment |
| 3.3.4 |  | VVC determines violation can not be eliminated through optimization | ADA historic database receives logs issued by VVC. | ADA VVC Controller | ADA Historic Database | Logs | Intra-Control Center Environment |
| 3.4.1 |  | DOMA function detects distribution model inconsistency | After detecting distribution model inconsistency, DOMA function sets an inconsistency flag to put VVC in a default mode. | DOMA function | ADA VVC Controller | Distribution model inconsistency flag | Intra-Control Center Environment |
| 3.4.2 |  | VVC switches to default settings for portions of distribution system with inconsistent model | The fact that the VVC is switched to default setting has been issued is received by DMS SCADA database. | ADA VVC Controller | DMS SCADA database | Fact that VVC is switched to default setting | Intra-Control Center Environment |
| 3.4.3 |  | VVC switches to default settings for portions of distribution system with inconsistent model | Log is stored in ADA historic database. | ADA VVC Controller | ADA Historic Database | Log | Intra-Control Center Environment |
| 3.5.1 |  | Checking real-time data | DOMA function checks the real-time data for changes, alarms. | DMS SCADA database | DOMA function | DMS real-time analog, status, TLQ data, confirmation of execution of VVC commands, status of voltage controllers | Intra-Control Center Environment |
| 3.5.2 |  | Checking real-time data | DOMA function checks the real-time data for changes, alarms. | SCADA Energy Management System database | DOMA function | Energy Management System real-time analog, status, TLQ data | Intra-Control Center Environment |
| 3.5.3 |  | VVC determines there is room for optimization and performs optimization within emergency limits | DOMA detects transmission emergency limit violation and issues a command to initiate VVC. | DOMA function | ADA VVC Controller | Command to initiate VVC | Intra-Control Center Environment |
| 3.5.4 |  | VVC determines there is room for optimization and performs optimization within emergency limits | VVC receives excerpts from ADA database updated with latest SCADA scan. | ADA Database | ADA VVC Controller | Excerpts from ADA database | Intra-Control Center Environment |
| 3.5.5 |  | VVC determines there is room for optimization and performs optimization within emergency limits | Selected optimization results are displayed for the System Operator. | ADA VVC Controller | System Operator | VVC status, present and recommended bus kV, expected lowest and highest load V, flag of using emergency limits | User Interface |
| 3.5.6 |  | VVC determines there is room for optimization and performs optimization within emergency limits | DMS SCADA database receives relevant optimization results. | ADA VVC Controller | DMS SCADA database | Recommended settings to relevant voltage and power electronic controllers, DER modes of operation and settings, capacitors status | Intra-Control Center Environment |
| 3.5.7 |  | VVC determines there is room for optimization and performs optimization within emergency limits | Selected results are archived in ADA historic database. | ADA VVC Controller | ADA Historic Database | VVC and LTC states and settings; VVC limits and benefits; losses, voltage, objective function and total demand before and after optimization, logs | Intra-Control Center Environment |
| 3.5.8 |  | VVC determines there is room for optimization and performs optimization within emergency limits | ADA VVC Controller initiates DOMA function after confirmation of execution is received. | ADA VVC Controller | DOMA function | Command to initiate DOMA | Intra-Control Center Environment |
| 3.5.9 |  | DOMA function performs analysis | DOMA function, after detecting a violation present during the after-optimization conditions, sends alarm to System Operator. | DOMA function | System Operator | Alarm for System Operator | User Interface |
| 3.5.10 |  | Prearming RAS adjusts settings of relevant groups of load shedding | DOMA function, after detecting that optimization has not eliminated transmission violation, sends an alarm to pre-arming RAS function. | DOMA function | Prearming of RAS schemes function | Alarm for prearming RAS function | Intra-Control Center Environment |
| 3.5.11 |  | Data for System Operator | Relevant for System Operator VVC and LTC settings, limits, and statuses are displayed. | DMS SCADA database | System Operator | VVC: status, integrity, settings, limits, bandcenter, objective LTC: status, position | User Interface |

### VVC Function Participation in Severe Emergency in Bulk Power System with Intentional Islands

if !vml?![](DO_VVO_Use_Case_files/image006.jpg)endif?

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.6.1 | The bulk power system is separated in near-balanced islands to prevent wide-area blackout. The load shedding schemes operated | Creating transmission islands, and load-shedding by fast acting schemes | The conditions of capacity deficit are detected by Energy Management System/SCADA and submitted to VVC as a trigger for changing the objective and perform in emergency mode. | Transmission Energy Management System, Remedial Action Scheme. | ADA load management functions | Command to initiate VVC in load reduction mode; commands from VVC to IEDs and DERs. | Intra-Control Center Environment |
| 3.6.2 |  | Contingency in bulk power system creates transmission islands | SCADA Energy Management System receives status of switches (circuit breakers) in transmission affected by contingency. | Transmission Energy Management System, Remedial Action Scheme. | SCADA Energy Management System database | Status of switches | Intra-Control Center Environment |
| 3.6.3 |  | UFLS balances load and generation and changes distribution circuits connectivity | DMS SCADA database receives status of switches affected by load shedding. | Field Device | DMS SCADA database | Status of switches | Intra-Control Center Environment |
| 3.6.4 |  | Update of the topology and load models | DOMA function receives the latest scan of DMS SCADA database and adjusts the distribution operation model for VVC to perform in emergency load reduction mode. . | DMS SCADA database | DOMA function | DMS real-time analog, status, TLO data, status of voltage controllers. | Intra-Control Center Environment |
| 3.6.5 |  | Changing VVC current objective to load reduction within emergency limits | DOMA issues a command to change VVC objective and initiate optimization. | DOMA | ADA VVC Controller | Command to change VVC objective and optimization | Intra-Control Center Environment |
| 3.6.6 |  | VVC performs optimization with emergency load reduction objective | VVC performs reduction of load not affected by load-shedding schemes to create capacity reserves and restore a portion of shed loads. | ADA VVC Controller | DMS SCADA database | Settings for voltage controllers,  statuses of capacitors, power electronics statuses of DER, modes of operation and settings of DER controllers. | Intra-Control Center Environment |
