# Day Ahead

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/MO_Day_Ahead.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Day Ahead Market Operations

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

The following is a
list of Western RTO functions related to Day Ahead market operations.

Only the listed
functions with asterisks are represented in the diagrams and/or
step-by-step descriptions in section 2.

1.       
Day Ahead Market

a.       [Day
Ahead](MO_Day_Ahead.htm#Day Ahead Auction of Firm Transmission Rights (DAAFTR)) 
[Auction/sale of FTRs](MO_Day_Ahead.htm#Day Ahead Auction of Firm Transmission Rights (DAAFTR)) \*

b.      
[Day Ahead
Submittal of Energy Schedules](MO_Day_Ahead.htm#Day Ahead Submittal of Energy Schedules (DAES)) \*

c.       [Day
Ahead Submittal of Ancillary Service Bids](MO_Day_Ahead.htm#Day Ahead Submittal of Ancillary Services Bids (DAAS)) \*

d.      
[Schedule Adjustment of Energy
Schedules](MO_Day_Ahead.htm#Adjust Energy Schedules (AES)) \*

e.       [Schedule
Adjustment of Ancillary Services](MO_Day_Ahead.htm#Adjust Ancillary Services (AAS)) \*

f.        [NERC
Tagging Management](MO_Day_Ahead.htm#NERC E-Tagging Management (ETAG))  \*

## Day Ahead Auction of Firm Transmission Rights (DAAFTR)

### Description

RTOs/ISOs are required to auction and/or sell
transmission rights and other energy services to Market Participants
(depends on market design), directly involving RTOs/ISOs, Scheduling
Coordinators, Market Participants, Regulators, Auditors, performing
market-established algorithm for allocating transmission rights to
Market Participants, with key interfaces between

1. RTOs and
Scheduling Coordinators

2. RTOs and
Regulators

3. RTOs and Auditors

4. RTOs and Web
Servers for Market Participants,

### Diagram

if !vml?![](MO_Day_Ahead_files/image002.gif)endif?

### Steps for DAAFTR

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Before Day Ahead market | Issue notice of intent | (1) Issue notice of intent to use FTRs and NCRs before Day Ahead market | Scheduling Coordinator | Market Interface Web Server | FTR Notices of intent | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.2 | After previous step | Update intents | (2) Update intents to use FTRs | Market Interface Web Server | Transmission Right Ownership Database | FTR Notices of intent | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.3 | After previous step | (3) Provide updates on un-used FTRs and NCRs | (3) Provide updates on un-used FTRs and NCRs | Transmission Right Ownership Database | Operational Transmission Capacity | Unused FTRs | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4 | After previous step | (4) Trigger posting of FTRs at Schedule Close | (4) Trigger posting of FTRs at Schedule Close | Time Line Manager | Operational Transmission Capacity | Used FTRs | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.5 | After previous step | (5) Post available FTRs as auctionable RTRs | (5) Post available FTRs as auctionable RTRs | Operational Transmission Capacity | Market Interface Web Server | Available FTRs | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.6 | After previous step | (6) Review auctionable RTRs | (6) Review auctionable RTRs | Market Interface Web Server | Scheduling Coordinator | Auctionable RTRs | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.7 | After previous step | (7) Make one-time bid on RTRs and ancillary services | (7) Make one-time bid on RTRs and ancillary services | Scheduling Coordinator | Market Interface Web Server | Bids for RTRs | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.8 | After previous step | (8) Enter RTR bids | (8) Enter RTR bids | Market Interface Web Server | FTR Market Clearing Price Auction Function | Bids for RTRs | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.9 | After previous step | (9) Select highest bidder for RTR and store as RTR owner | (9) Select highest bidder for RTR and store as RTR owner | FTR Market Clearing Price Auction Function | Transmission Right Ownership Database | RTR ownership | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.10 | After previous step | (10) Notify of auction results | (10) Notify of auction results | Market Interface Web Server | Scheduling Coordinator | Auction results | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Day Ahead Submittal of Energy Schedules (DAES)

### Description

Scheduling Coordinators or other Market
Participants must submit 24-hour energy schedules in the Day-Ahead
market. The RTOs/ISOs must validate the submittals (depending on
market design), directly involving Scheduling Coordinators (or other
entities), RTOs/ISOs, Auditors, and other Market Participants.

### Diagram

if !vml?![](MO_Day_Ahead_files/image004.gif)endif?

### Steps for DAES

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 | On-going | Submit energy schedules | (1) Submit Balanced Energy Schedule Database, including self-provided Ancillary Service Schedule, any inter-SC trades, and any generation limit changes, until Schedule Close | Scheduling Coordinator | Market Interface Web Server | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.2 | Submittal of an energy schedule | Validation | (2) Indicates valid input or indicates clerical & format errors | Market Interface Web Server | Scheduling Coordinator | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.3 | Correction | Correction | (3) Corrects errors | Scheduling Coordinator | Market Interface Web Server | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.4a | Valid energy schedule submitted | Energy Schedule Analysis | (4a) Provides Day-Ahead Energy Schedule Database | Market Interface Web Server | Energy Schedule Analysis | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.4b | Simultaneous with previous step | Energy Schedule Database to RTOs | (4b) Provides Day-Ahead Energy Schedule Database relevant to each RTO | Market Interface Web Server | Other 2 RTOs Energy Schedule Processing | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.5a | Analysis of energy schedules | Adjustment to energy schedules | (5a) Adjusts any unbalanced schedules and stores validated input as proposed schedules | Energy Schedule Analysis | RTO Energy & A/S Schedules | Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5b | Simultaneous with previous step | Adjusted energy Schedules to RTOs | (5b) Provides adjusted and validated cross-RTO schedules | Energy Schedule Analysis | Other 2 RTOs Energy Schedule Processing | Energy schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.5c | Simultaneous with previous step | Apply existing energy schedule contracts | (5c) Enter existing contracts | Existing Transmission Contracts | RTO Energy & A/S Schedules | Existing energy schedule contracts | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.6a | Day Ahead Market Close | Time-based trigger | (6a) Initiates Day Ahead security analysis verification after Schedule Close | Time Line Manager | Congestion Management System | Day Ahead Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.6b | Simultaneous with previous step | Retrieve Day-Ahead schedules | (6b) Retrieves all Day Ahead schedules | RTO Energy & A/S Schedules | Congestion Management System | Day Ahead Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.6c | Simultaneous with previous step | Cross-RTO security analysis | (6c) For cross-RTO schedules, validates schedules, adjusts any unbalanced schedules, and provides as proposed schedules | Other 2 RTOs Energy Schedule Processing | RTO Energy & A/S Schedules | Day Ahead Energy schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.7a | After previous step | Security Analysis | (7a) Verifies schedules meet intra-zonal & connection point security requirements | Congestion Management System | RTO Energy & A/S Schedules | Day Ahead Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.7b | Simultaneous with previous step | Cross-RTO security analysis | (7b) For cross-RTO schedules, provide results of Congestion Management analysis | Congestion Management System | Other 2 RTOs Energy Schedule Processing | Day Ahead Energy schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.8a | After previous step | Post results of security analysis | (8a) Posts results of Congestion Management analysis of schedules | RTO Energy & A/S Schedules | Market Interface Web Server | Day Ahead Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.8b | Simultaneous with previous step | Post results of cross-RTO security analysis | (8b) Posts results of Congestion Management analysis of cross-RTO schedules | Other 2 RTOs Energy Schedule Processing | Market Interface Web Server | Day Ahead Energy schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.8c | Simultaneous with previous step | Cross-RTO conflicts | (8c) Notify of cross-RTO conflicts or inconsistencies | Other 2 RTOs Energy Schedule Processing | RTO Scheduler | Cross-RTO conflicts | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.9 | After step 8c | Resolve cross-RTO conflicts | (9) Posts resolutions to cross-RTO conflicts and inconsistencies | RTO Scheduler | Market Interface Web Server | Resolved cross-RTO conflicts | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.10 | After previous step | Notify Scheduling Coordinator | (10) Notifies of schedule acceptances and rejections | Market Interface Web Server | Scheduling Coordinator | Accepted Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.11 | Upon request by Scheduling Coordinator | Revisions to energy schedules | (11) Enter revisions to schedules as needed, until Revision Close | Scheduling Coordinator | Market Interface Web Server | Revised energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Day Ahead Submittal of Ancillary Services Bids (DAAS)

### Description

Scheduling Coordinators must submit Day-Ahead
bids for ancillary services: reserve, regulation, frequency response,
etc., and the RTOs/ISOs must validate the submittals. This function
directly involves Scheduling Coordinators, RTOs/ISOs, Auditors, other
Market Participants. Key interfaces include those between

1. Scheduling
Coordinators and RTOs/ISOs

2. RTOs/ISOs and
neighboring RTOs/ISOs

3. RTOs/ISOs and Web
Server for Market Participants,

### Diagram

if !vml?![](MO_Day_Ahead_files/image006.gif)endif?

### Steps for DAAS

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1 | On-going | Submit ancillary services bids | (1) Submit Ancillary Services resources and bid prices, until Schedule Close | Scheduling Coordinator | Market Interface Web Server | Ancillary services bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.2 | Upon receipt of submittal | Validation of A/S bids | (2) Indicates valid input or indicates clerical & format errors | Market Interface Web Server | Scheduling Coordinator | Validity checks on ancillary services bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.3 | Correction of errors | Corrections of A/S bids | (3) Correct errors | Scheduling Coordinator | Market Interface Web Server | Corrections to ancillary services resources and bid prices | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.4a | Enter A/S | Enter A/S bids | (4a) Enter A/S resources and bid prices | Market Interface Web Server | RTO Energy & A/S Schedules | Ancillary services bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.4b | Notify other RTOs | Notify other RTOs | (4b) Notify of A/S services accepted by other RTOs | Other 2 RTOs | Ancillary Services Procurement Analysis | Ancillary services bids | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 3.5 | Day ahead market close | Analyze A/S bids | (5) Initiates Day Ahead A/S analysis at Schedule Close | Time Line Manager | Ancillary Services Procurement Analysis | Ancillary services bids | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.6 | Previous step | Determine which A/S | (6) Determines which A/S are needed, and calculates either one Market Clearing Price or separate Market Clearing Prices for each Congestion Zone | Ancillary Services Procurement Analysis | RTO Energy & A/S Schedules | Selected A/S bids | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.7a | Previous step | Create Balancing Energy Stack | (7a) Creates the Balancing Energy Stack entries for each Settlement Period | RTO Energy & A/S Schedules | Balancing Energy Stack | Selected A/S bids | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.7b | Simultaneous with previous step | Post results | (7b) Posts results of selection of A/S resources and the Market Clearing Price | RTO Energy & A/S Schedules | Market Interface Web Server | Selected A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.7c | Simultaneous with previous step | Inform other RTOs | (7c) Inform other RTOs of accepted A/S resources | RTO Energy & A/S Schedules | Other 2 RTOs | Selected A/S bids | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 3.8 | Previous step | Notify Scheduling Coordinator | (8) Notifies of A/S resource status | Market Interface Web Server | Scheduling Coordinator | Selected A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.9 | Previous step | Withdraw A/S | (9) Withdrawal of Ancillary Service resources not yet selected | Scheduling Coordinator | Market Interface Web Server | Withdrawn A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Adjust Energy Schedules (AES)

### Description

The RTO/ISOs perform congestion management and security analysis on
submitted energy schedules (depending on market design), directly
involving RTO/ISO Scheduler, Other RTOs, Scheduling Coordinators,
other Market Participants, TransCos, GenCos, Regulators, Auditors,
performing power system analysis of the impact of the proposed energy
on system conditions to determine probable ancillary services and any
violations of power system security conditions. After this analysis is
performed, the Scheduling Coordinators may be asked to adjust their
energy schedules.

Scheduling Coordinators may also submit changes to their energy
schedules, again subject to market rules.

### Diagram

if !vml?![](MO_Day_Ahead_files/image008.gif)endif?

### Steps for AES

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4.1a | Whenever energy schedules need to be adjusted | Submit adjusted schedules | (1a) Submits adjusted schedules for withdrawn RTR and other reasons, during Schedule Adjustment Period | Scheduling Coordinator | Market Interface Web Server | Adjusted schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.1b | Whenever RTRs need to be recalled | Recall RTR | (1b) Recalls RTR (up to 2 hrs before Settlement Period) and submits new schedule using FTR | SC-FTR Owner | Market Interface Web Server | Recalled RTRs  New schedule | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.2a | After previous step | Validation | (2a) Indicates valid input or indicates clerical & format errors | Market Interface Web Server | Scheduling Coordinator | Validated data | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.2b | After validation | Reverts RTRs | (2b) Reverts RTR to original owner as FTR | Market Interface Web Server | Transmission Right Ownership Database | RTR ownership | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.3a | Errors are corrected | Error correction | (3a) Correct errors | Scheduling Coordinator | Market Interface Web Server | Corrected data | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.3b | After 2b | Provide updated FTR | (3b) Provides FTR ownership information | Transmission Right Ownership Database | RTO Energy & A/S Schedules | FTR ownership data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.4 | After 3 | Store validated input | (4) Stores validated input as proposed schedules | Market Interface Web Server | RTO Energy & A/S Schedules | Validated input | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.5 | At specified date and time | Initiate security analysis | (5) Initiates security analysis as needed for adjusted schedules | Time Line Manager | Congestion Management System | Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.6 | After previous step | Test for congestion | (6) Verifies schedules meet intra-zonal & connection point security requirements | Congestion Management System | RTO Energy & A/S Schedules | Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.7 | At specified date and time | Post results | (7) Posts results of FTR ownership and security analysis of schedules | RTO Energy & A/S Schedules | Market Interface Web Server | Energy schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.8 | After close of schedule adjustment period | Update operating plan | (8) Updates Operating Plan after close of Schedule Adjustment period | RTO Energy & A/S Schedules | Operating Plan | Energy schedules and A/S schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.9a | One hour before Settlement Period | Review Operating Plan | (9a) Reviews Final Operating Plan one hour ahead of Settlement Period | Operating Plan database | Area & Resource Operation Centers | Operating Plan | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 4.9b | One hour before Settlement Period | Review Operating Plan | (9b) Reviews Final Operating Plan one hour ahead of Settlement Period | Operating Plan database | Transmission Owner | Operating Plan | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 4.9c | One hour before Settlement Period | Provide Operating Plan | (9c) Provides Operating Plan to other RTOs | Operating Plan database | Other 2 RTOs | Operating Plan | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 4.10a | After previous step | Confirm Operating Plan | (10a) Confirms Operating Plan | Area & Resource Operation Centers | Operating Plan database | Operating Plan | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 4.10b |  | Confirm Operating Plan | (10b) Confirms Operating Plan | Transmission Owner | Operating Plan database | Operating Plan | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 4.11 | At specific date and time | Post Operating Plan | (11) Posts public information of Operating Plan | Operating Plan database | Market Interface Web Server | Operating Plan | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Adjust Ancillary Services (AAS)

### Description

Additional auctions may be held to adjust ancillary services during
the adjustment period. In particular, Local Generation Resources (LGRs)
may be scheduled to reflect new requirements by the RTO/ISOs.

### Diagram

if !vml?![](MO_Day_Ahead_files/image010.gif)endif?

### Steps for AAS

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.1 | Anytime up to 30 minutes before Settlement Period | Submit one-time A/S bids | (1) Submittal of one-time Bids for Ancillary Services up to 30 minutes before Settlement Period | Scheduling Coordinator | Market Interface Web Server | A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.2 | After previous step | Validate | (2) Indicates valid input or indicates clerical & format errors | Market Interface Web Server | Scheduling Coordinator | Error indications | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.3 | After previous step | Correct errors | (3) Correct errors | Scheduling Coordinator | Market Interface Web Server | Corrected A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.4a | After previous step | Enter A/S bids | (4a) Enter A/S resources and bid prices | Market Interface Web Server | RTO Energy & A/S Schedules | A/S bids | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.4b |  | Notify of accepted A/S bids | (4b) Notify of A/S services accepted by other RTOs | Other 2 RTOs | Ancillary Services Procurement Analysis | Accepted A/S bids | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 5.5a | After previous step | Indicate possible need for A/S services | (5a) Indicate probable need for additional A/S resources | Data Acquisition and Control (DAC) Subsystem | Ancillary Services Procurement Analysis | Indication of need for A/S | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.5b |  | Indicate possible need for A/S services | (5b) Indicate probable need for additional A/S resources | Balancing Energy Stack | Ancillary Services Procurement Analysis | Indication of need for A/S | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.6 | After previous step | Determine needed A/S | (6) Determines need for additional A/S resources, and selects lowest bids | Ancillary Services Procurement Analysis | RTO Energy & A/S Schedules | Selected A/S schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.7a | After previous step | Post | (7a) Posts selected A/S resources | RTO Energy & A/S Schedules | Market Interface Web Server | Selected A/S schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.7b |  | Provide A/S | (7b) Provides selected A/S resources | RTO Energy & A/S Schedules | Balancing Energy Stack | Selected A/S schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.7c |  | Inform RTOs | (7c) Inform other RTOs of selected A/S resources | RTO Energy & A/S Schedules | Other 2 RTOs | Selected A/S schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 5.8 | After previous step | Notify | (8) Notifies of A/S resource status | Market Interface Web Server | Scheduling Coordinator | Selected A/S schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.9 | Anytime after previous step | Withdraw A/S | (9) Can withdraw Ancillary Service bids if not already selected by RTO | Scheduling Coordinator | Market Interface Web Server | Withdrawn A/S | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 5.10 | After previous step | Notify | (10) Notify other RTOs of withdrawn A/S bids | Market Interface Web Server | Other 2 RTOs | Withdrawn A/S | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## NERC E-Tagging Management (ETAG)

### Description

NERC requires the tracking of the ownership and characteristics of
all energy schedules through the submittal of e-tagging forms.

### Diagram

if !vml?![](MO_Day_Ahead_files/image012.gif)endif?

### Steps for ETAG

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6.1 | At appropriate times | Submit tags | (1) Submit tags to Tag Authority | Scheduling Coordinator | Tag Authority | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 6.2 | After previous step | Submit tags | (2) Submit all tags requiring RTO approval | Tag Authority | Market Interface Web Server | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 6.3 | After previous step | Submit tags | (3) Submit tags for validation and approval | Market Interface Web Server | Tag Approval Service | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 6.4 | After previous step | Provide approval status | (4) Provide approval status of energy schedules and ancillary services procurements | RTO Energy & A/S Schedules | Tag Approval Service | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 6.5 | After previous step | Provide approval status | (5) Indicate status of tags, based on status of energy and A/S schedules | Tag Approval Service | Market Interface Web Server | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 6.6 | After previous step | Submit tags | (6) Send updated tag information | Market Interface Web Server | Tag Authority | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 6.7 | After previous step | Submit tags | (7) Submit tagging information to NERC | Tag Authority | NERC | E-Tag information | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
