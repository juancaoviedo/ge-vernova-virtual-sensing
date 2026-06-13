# Real-Time Operations

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/MO_Real-Time_Operations.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Real-Time RTO Power System Operations

## Narrative

As the electricity
industry is deregulated, and as FERC defines more clearly what the
market operation tariffs will encompass, three possible Regional
Transmission Organizations (RTOs) in the Western Interconnection are
developing seamless interfaces for Market Participants to submit
energy schedules and ancillary service bids across these 3 RTOs. The 3
RTOs are California ISO (existing ISO handling the electricity market
in California), RTO West (potential RTO of many northwestern
utilities), and WestConnect (potential RTO of many southwestern
utilities). These 3 RTOs are developing the requirements for the
Western RTO functions.

The descriptions of
the functions below may or may not represent the final market rules
and market operations, because these have not been finalized yet.

The following is a
list of Western RTO functions related to Real-Time market operations.

Only the listed
functions with asterisks are represented in the diagrams and/or
step-by-step descriptions in section 2.

> 1.       
> Real-Time
>
> > a.        Operational calculations
> >
> > b.       Real-time Submittal of Schedules
> >
> > c.        Real-time Submittal of Ancillary
> > Services
> >
> > d.      
> > [Normal Real-Time Dispatch Operations](MO_Real-Time_Operations.htm#Normal Real-Time Dispatch Operations) \*
> >
> > e.       [Normal Generation Control Operations](MO_Real-Time_Operations.htm#Normal Generation Control (NGC))\*
> >
> > f.        [Scheduling Coordinators Redispatch](MO_Real-Time_Operations.htm#Scheduling Coordinators Redispatch (SCRD)) \*
> >
> > > ·         Redispatch
> > >
> > > ·         Notify Scheduling Coordinators
> > > of redispatch
> >
> > g.      
> > [Emergency Ancillary Services](MO_Real-Time_Operations.htm#Emergency Ancillary Services (EAS)) \*
> >
> > h.      
> > [Real-Time Power System Historical Records](MO_Real-Time_Operations.htm#RT Power System Historical Records (PSH))
> > \*

## Normal Real-Time Dispatch Operations

### Description

RTO/ISO system operators monitor the power system and either
initiate control commands directly on the power system equipment, or
request the transmission owners to issue the commands, if needed for
power system reliability.

### Diagram

if !vml?![](MO_Real-Time_Operations_files/image002.gif)endif?

### Steps for Normal Real-time Dispatch Operations

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1a | Continuous | Monitor | Monitor transmission system | Transmission Power System | Transmission Owner | Transmission data | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 1b |  | Monitor | Monitor distribution system | Distribution Power System | DisCos | Distribution data | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 2a | After previous step | Monitor | Receive transmission system data via ICCP links | Transmission Owner | Data Acquisition and Control (DAC) Subsystem | Transmission data | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 2b |  | Monitor | Receive distribution system data at connecting points via ICCP links | DisCos | Data Acquisition and Control (DAC) Subsystem | Distribution data | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 2c |  | Monitor | Receive real-time RTO data via ICCP links | Other 2 RTOs | Data Acquisition and Control (DAC) Subsystem | Real-time data from other RTOs | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 3a | After previous step | Monitor | Provide real-time data to RTOs via ICCP links | Data Acquisition and Control (DAC) Subsystem | Other 2 RTOs | Real-time data to other RTOs | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 3b |  | Monitor | Monitor power system operations | Data Acquisition and Control (DAC) Subsystem | RTO Operator | User Information | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3c |  | Monitor | Provide real-time raw data for State Estimator | Data Acquisition and Control (DAC) Subsystem | Real Time Network Analysis Sequence | Subset of real-time data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3d |  | Import power system model | Provide power system model | Power System Model | Real Time Network Analysis Sequence | Power system connectivity and characteristics | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4 | After previous step | Analyze power system | Issue alarms for potential power system contingencies | Real Time Network Analysis Sequence | RTO Operator | Alarms | User Interface |
| 5 | After previous step | Control | Authorize or override control commands | RTO Operator | Data Acquisition and Control (DAC) Subsystem | Control commands | User Interface |
| 6a | After previous step | Control | Issue transmission equipment instructions by phone | Data Acquisition and Control (DAC) Subsystem | Transmission Owner | Control commands | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 6b |  | Control | Issue distribution equipment instructions by phone | Data Acquisition and Control (DAC) Subsystem | DisCos | Control commands | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 7a | After previous step | Control | Actual direct control over transmission system equipment | Transmission Owner | Transmission Power System | Control commands | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |
| 7b |  | Control | Actual direct control over distribution system equipment | DisCos | Distribution Power System | Control commands | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |

## 

## Normal Generation Control (NGC)

### Description

RTO/ISO system operators dispatch generation
according to energy schedules:

- RTO/ISO SCADA
system monitors power system

- RTO/ISO EMS system
performs Automatic Generation Control (AGC)

- RTO/ISO Market
Operations system analyzes transmission capacity and reliability

- RTO/ISO Market
Operations system balances energy/ancillary services

RTO/ISO EMS system monitors interchange
schedules with internal and external Control Areas, directly involving
RTO System Operator, RTO/ISO SCADA EMS, Scheduling Coordinators, Area
Control Centers, Generators, performing Automatic Generation Control,
with key interfaces between

1. RTO SCADA/EMS and
Generators

2. RTO SCADA/EMS and
TransCos

3. RTO SCADA/EMS and
DisCos

4. RTO SCADA/EMS and
other RTO SCADA/EMS

5. RTO SCADA/EMS and
Scheduling Coordinators

### Diagram

if !vml?![](MO_Real-Time_Operations_files/image004.gif)endif?

### Steps for Normal Generation Control

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | On-going | Submit energy schedules | (1) Submit Balanced Energy Schedules, including self-provided Ancillary Services Schedules, any inter-SC trades, and any generation limit changes, until Schedule Close | Scheduling Coordinators | Market Interface Web Server | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2 | Submittal of an energy schedule | Validation | (2) Indicates valid input or indicates clerical & format errors | Market Interface Web Server | Scheduling Coordinators | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3 | Correction | Correction | (3) Corrects errors | Scheduling Coordinators | Market Interface Web Server | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4a | Valid energy schedule submitted | Energy Schedule Analysis | (4a) Provides Day-Ahead Energy Schedules | Market Interface Web Server | Energy Schedule Analysis | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4b | Simultaneous with previous step | Energy Schedules to RTOs | (4b) Provides Day-Ahead Energy Schedules relevant to each RTO | Market Interface Web Server | Other 2 RTOs Energy Schedule Processing | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5a | Analysis of energy schedules | Adjustment to energy schedules | (5a) Adjusts any unbalanced schedules and stores validated input as proposed schedules | Energy Schedule Analysis | RTO Energy & A/S Schedules | Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 5b | Simultaneous with previous step | Adjusted energy Schedules to RTOs | (5b) Provides adjusted and validated cross-RTO schedules | Energy Schedule Analysis | Other 2 RTOs Energy Schedule Processing | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5c | Simultaneous with previous step | Apply existing energy schedule contracts | (5c) Enter existing contracts | Existing Transmission Contracts | RTO Energy & A/S Schedules | Existing energy schedule contracts | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 6a | Day Ahead Market Close | Time-based trigger | (6a) Initiates Day Ahead security analysis verification after Schedule Close | Time Line Manager Function | Congestion Management Function | Day Ahead Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 6b | Simultaneous with previous step | Retrieve Day-Ahead schedules | (6b) Retrieves all Day Ahead schedules | RTO Energy & A/S Schedules | Congestion Management Function | Day Ahead Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 6c | Simultaneous with previous step | Cross-RTO security analysis | (6c) For cross-RTO schedules, validates schedules, adjusts any unbalanced schedules, and provides as proposed schedules | Other 2 RTOs Energy Schedule Processing | RTO Energy & A/S Schedules | Day Ahead Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 7a | After previous step | Security Analysis | (7a) Verifies schedules meet intra-zonal & connection point security requirements | Congestion Management Function | RTO Energy & A/S Schedules | Day Ahead Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 7b | Simultaneous with previous step | Cross-RTO security analysis | (7b) For cross-RTO schedules, provide results of Congestion Management analysis | Congestion Management Function | Other 2 RTOs Energy Schedule Processing | Day Ahead Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 8a | After previous step | Post results of security analysis | (8a) Posts results of Congestion Management analysis of schedules | RTO Energy & A/S Schedules | Market Interface Web Server | Day Ahead Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 8b | Simultaneous with previous step | Post results of cross-RTO security analysis | (8b) Posts results of Congestion Management analysis of cross-RTO schedules | Other 2 RTOs Energy Schedule Processing | Market Interface Web Server | Day Ahead Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 8c | Simultaneous with previous step | Cross-RTO conflicts | (8c) Notify of cross-RTO conflicts or inconsistencies | Other 2 RTOs Energy Schedule Processing | RTO Scheduler | Cross-RTO conflicts | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 9 | After step 8c | Resolve cross-RTO conflicts | (9) Posts resolutions to cross-RTO conflicts and inconsistencies | RTO Scheduler | Market Interface Web Server | Resolved cross-RTO conflicts | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 10 | After previous step | Notify Scheduling Coordinators | (10) Notifies of schedule acceptances and rejections | Market Interface Web Server | Scheduling Coordinators | Accepted Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 11 | Upon request by Scheduling Coordinators | Revisions to energy schedules | (11) Enter revisions to schedules as needed, until Revision Close | Scheduling Coordinators | Market Interface Web Server | Revised energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Scheduling Coordinators Redispatch (SCRD)

### Description

Scheduling Coordinators to submit energy
schedule adjustments in the Hour-Ahead market if needed due to power
system emergencies or other factors, and the RTOs/ISOs to validate the
submittals. This function involves the Scheduling Coordinators,
RTOs/ISOs, Auditors, and other Market Participants.

### Diagram

,if !vml?![](MO_Real-Time_Operations_files/image006.gif)endif?

### Steps for Scheduling Coordinators Redispatch

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (1) | Emergency event | Provide alarm information | Notifies SCs of emergency congestion and other problems | Data Acquisition and Control (DAC) Subsystem | Market Interface Web Server | Emergency alarm data | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (2) |  | Notify Scheduling Coordinators | Notifies of problems requiring rescheduling | Market Interface Web Server | Scheduling Coordinators | Emergency alarm data and rescheduling request | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (3) |  | Update schedules | Update schedules due to generator outage or reduced transmission rights | Scheduling Coordinators | Market Interface Web Server | Updated schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (4) |  | Validate schedules | Update valid schedules | Market Interface Web Server | Energy Schedules | Validated updated schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (5) |  | Analyze updated schedules | Analyze updated schedules | Energy Schedules | Maintenance Outage Function | Updated schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (6) |  | Review updated schedule | Review updated schedules | Maintenance Outage Function | RTO Operator | Updated schedule | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| (7) |  | Approve updated schedule | Verify updated schedule is acceptable | RTO Operator | Energy Schedules | Approved updated schedule | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| (8a) |  | Update operating plan | Update operating plan | Energy Schedules | Operating Plan | Updated Operating plan | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| (8b) |  | Indicates acceptance or rejection | Accepts or rejects updated schedule | Energy Schedules | Market Interface Web Server | Acceptance or rejection notice | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (9a) |  | Indicates acceptance or rejection | Notify of acceptance or rejection of updated schedule | Market Interface Web Server | Scheduling Coordinators | Acceptance or rejection notice | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (9b) |  | Provide updated Operating Plan | Provide updated Operating Plan | Operating Plan | Other RTOs | Operating Plan | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Emergency Ancillary Services (EAS)

### Description

Scheduling Coordinators submit Hour-Ahead bids for ancillary
services: reserve, regulation, frequency response, etc., in order to
resolve emergencies conditions, and the RTOs/ISOs to validate the
submittals.

RTO/ISO Market Operations system manages market external price caps
(if they exist in the respective market).

### Diagram

if !vml?![](MO_Real-Time_Operations_files/image008.gif)endif?

### Steps for Emergency Ancillary Services

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (1a) | Emergency on power system | Request additional A/S | Request additional ancillary services | RTO Operator | Market Interface Web Server | Emergency request | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (1b) |  | Override Operating Plan | Manually override Operating Plan in an emergency | RTO Operator | Operating Plan | Override | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| (1c) |  | Authorize emergency dispatch | Authorize emergency dispatch procedures | RTO Operator | Area & Resource Operation Centers | Emergency dispatch | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (2a) |  | Notify Scheduling Coordinators | Notify SCs of A/S request | Market Interface Web Server | Scheduling Coordinators | Notification of need for A/S | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (2b or 6b) |  | Update Balancing energy stack | Update Balancing Energy Stack to indicate that emergency conditions apply | Operating Plan | Balancing Energy Stack | Update | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| (3a) |  | Submit A/S bids | Submit bids for ancillary services | Scheduling Coordinators | Market Interface Web Server | A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (4a) |  | Analyze A/S bids | Analyze A/S bids | Market Interface Web Server | Ancillary Services Procurement Analysis | A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (5a) |  | Accept A/S bid | Accept A/S bid | Ancillary Services Procurement Analysis | Market Interface Web Server | A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (5b) |  | Update Operating plan | Update Operating Plan with new A/S | Ancillary Services Procurement Analysis | Operating Plan | Updates to Operating Plan | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| (6a) |  | Notify of A/S bid acceptance | Notify of A/S bid acceptance | Market Interface Web Server | Scheduling Coordinators | Bid Acceptance | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (6c) |  | Provide updated Operating Plan | Provide updated Operating Plan | Operating Plan | Area & Resource Operation Centers | Operating Plan | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (6d) |  | Provide updated Operating Plan | Provide updated Operating Plan | Operating Plan | Transmission Owner | Operating Plan | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| (6e) |  | Provide updated Operating Plan | Provide updated Operating Plan | Operating Plan | Other 2 RTOs | Operating Plan | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 7 |  | Issue validated volt/var and AGC raise/lower or setpoint commands | Issue validated volt/var and AGC raise/lower or setpoint commands | Balancing Energy Stack | Area & Resource Operation Centers | Control commands to implement Operating Plan | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## RT Power System Historical Records (PSH)

### Description

All real-time conditions and actions must be logged and recorded in
historical files.

### Diagram

if !vml?![](MO_Real-Time_Operations_files/image010.gif)endif?

### Steps for Historical Records

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1a | At end of each Settlement Period | Provide power system model and state estimated data | Provide power system model and state estimated data | Real Time Network Analysis Sequence | Network Sensitivity Calculations | Power System Model  State Estimated data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1b |  | Provide real-time power system data | Provide real-time power system data | Data Acquisition and Control (DAC) Subsystem | Network Sensitivity Calculations | Real-time data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1c |  | Provide power system data snapshots, calculated data, disturbance data, alarms, and other key data for historical records | Provide power system data snapshots, calculated data, disturbance data, alarms, and other key data for historical records | Data Acquisition and Control (DAC) Subsystem | Historical Records | Data snapshots | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1d |  | Provide transmission loss calculations | Provide transmission loss calculations | Network Sensitivity Calculations | Historical Records | Loss calculations | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1e |  | Provide MOD generation information | Provide MOD generation information | Merit Order Dispatch Function | Historical Records | Merit Order Dispatch data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1f |  | Provide operating plan information | Provide operating plan information | Operating Plan | Historical Records | Operating Plan | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2 |  | Post required power system information | Post required power system information | Historical Records | Market Interface Web Server | Posting of the historical records | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
