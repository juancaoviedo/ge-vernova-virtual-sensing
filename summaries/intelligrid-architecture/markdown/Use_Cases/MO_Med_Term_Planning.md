# Medium Term Planning

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/MO_Med_Term_Planning.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Market Operations – Medium and Short Term Planning

## Narrative

As the electricity industry is
deregulated, and as FERC defines more clearly what the market
operation tariffs will encompass, three possible Regional Transmission
Organizations (RTOs) in the Western Interconnection are developing
seamless interfaces for Market Participants to submit energy schedules
and ancillary service bids across these 3 RTOs. The 3 RTOs are
California ISO (existing ISO handling the electricity market in
California), RTO West (potential RTO of many northwestern utilities),
and WestConnect (potential RTO of many southwestern utilities). These
3 RTOs are developing the requirements for the Western RTO functions.

The following is a list of Western RTO
functions related to medium and short term planning for market
operations. The four functions with asterisks are described in this
document.

1.        
Medium/Short Term Planning

a.        
[Load Forecast](MO_Med_Term_Planning.htm#Load Forecasts (LF)) \*

b.       
[Outage Scheduling](MO_Med_Term_Planning.htm#Outage Scheduling (OS)) \*

c.        
[Congestion Management](MO_Med_Term_Planning.htm#Congestion Management (CM)) \*

d.      
[Long term
Auction/sale of Transmission Rights](MO_Med_Term_Planning.htm#Long Term Auction of Transmission Rights (LTATR)) \*

e.        
Bilateral Energy Market

## Load Forecasts (LF)

### Description - Load Forecast

The purpose of RTO/ISO/TransCos/DisCos Forecast
Load function is to provide load MW estimates for each region and
local area, based on energy schedules, weather forecasts, historical
load shapes, forecast special events, and expected new loads at their
connection points , directly involving RTOs, transmission owners,
distribution companies, National Weather Services, Market
Participants, Energy Service Providers, and Customers, performing
regional and local load forecasts for different time periods, updating
the precision of the forecasts, as each time period approaches, with
key interfaces between

> 1. all three types of utilities:
> RTOs, transmission owners, and distribution companies
>
> 2. Utilities and National Weather
> Services
>
> 3. RTOs and Market Participants
>
> 4. DisCos and Energy Service
> Providers
>
> 5. DisCos and Customers,

### Diagram - Load Forecast

if !vml?![](MO_Med_Term_Planning_files/image002.gif)endif?

### Steps - Load Forecast

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1a | Periodic or event driven | Load estimates | Provides load MW estimates from Day Ahead schedules as an auxiliary source of LF data | Scheduling Coordinator | 7-day Load Forecast | Load estimates | User Interface |
| 1.1b | In parallel to step 1a | Forecast weather | Provides weather forecasts and updates for each region | Weather Service | 7-day Load Forecast | Weather data | [Control Center to Corporate](../Environments/Env12_Control_Center_to_Corporate.htm) |
| 1.1c | In parallel to step 1a | Regional loads | Provides regional LF estimates as auxiliary source of LF data | Transmission Owner | 7-day Load Forecast | Load estimates | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.1d | In parallel to step 1a | Historical forecasts | Provides historical input for forecast | Historic Load Database | 7-day Load Forecast | Historical forecasts | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2 | Upon completion of previous step | Adjust forecasts | Adjusts load forecast | RTO Scheduler | 7-day Load Forecast | Adjustments | User Interface |
| 1.3 | Upon completion of previous step | Issue load forecasts | Provides 7-day regional load forecasts | 7-day Load Forecast | Market Participant | Load forecasts | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Outage Scheduling (OS)

### Description

The purpose of Outage Scheduling by TransCos
and GenCos is to propose scheduled transmission and generation outages
which are validated via the Congestion Management Analysis function
(see below) to determine if any major conflicts exist that could cause
power system problems.

### Diagram

if !vml?![](MO_Med_Term_Planning_files/image004.gif)endif?

### Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1a | As needed before a specific day and time when maintenance coordination is to be performed | Send generation outages | (1a) Send Day Ahead Local Generation Resources (LGR) outages, limit and ramp rate changes, and notification of non-LGR units | Scheduling Coordinator | LGR Generation Maintenance Schedule | Generation outages | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.1b | In parallel to step 1a | Send transmission outages | (1b) Request Day Ahead transmission maintenance outages | Transmission Owner | Transmission Outage Schedule | Transmission outages | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.1c | In parallel to step 1a | Send other RTO transmission outages | (1c) Notify of relevant transmission outages | Other 2 RTOs | Transmission Outage Schedule | Transmission outages | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.2a | On the specific day and time | Provide outage schedules | (2a) Provide proposed outage schedules | LGR Generation Maintenance Schedule | Maintenance Outage Function | Generation outages | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2b | In parallel to step 2a | Provide outage schedules | (2b) Provide proposed outage schedules | Transmission Outage Schedule | Maintenance Outage Function | Transmission outages | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3a | On the specific day and time | Provide energy schedules | (3a) Provide proposed energy schedules | Energy Schedule Database | Maintenance Outage Function | Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3b | In parallel to step 3a | Provide load forecast | (3b) Provide 7-day load forecasts for each region | 7-day Load Forecast | Maintenance Outage Function | Load forecasts | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.4 | After previous step | Review outages | (4) Reviews result of Maintenance Outages | Maintenance Outage Function | RTO Scheduler | Generation outages  Transmission outages | User Interface |
| 2.5a | When RTO Scheduler analyzes the impact of outages | Analysis of LGR outages | (5a) Approves or rejects LGR outage | RTO Scheduler | LGR Generation Maintenance Schedule | Indication of approval and rejection of LGR maintenance schedules | User Interface |
| 2.5b | In parallel to step 5a | Analysis of transmission outages | (5b) Approves or rejects transmission outage schedules | RTO Scheduler | Transmission Outage Schedule | Indication of approval and rejection of transmission outage schedules | User Interface |
| 2.6a | After previous step | Notify LGR owners | (6a) Notify LGR Owner of approvals and rejections | LGR Generation Maintenance Schedule | Scheduling Coordinator | Indication of approval and rejection of LGR maintenance schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.6b | In parallel to step 6a | Notify transmission owners | (6b) Notify TO of approvals and rejections | Transmission Outage Schedule | Transmission Owner | Indication of approval and rejection of transmission outage schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.6c | In parallel to step 6a | Warnings on contingencies | (6c) Warn of potential contingencies | Transmission Outage Schedule | Other 2 RTOs | Contingency warnings | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |

## Congestion Management (CM)

### Description

RTO/ISOs must perform congestion management and security analysis
on submitted energy schedules (depending on market design), focusing
on the impact of the proposed energy on system conditions, in order to
determine probable ancillary services and any violations of power
system security conditions.

### Diagram

if !vml?![](MO_Med_Term_Planning_files/image006.gif)endif?

### Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1a | Periodically and/or at specific times and dates | Update constraints | (1a) Update transmission path constraints for each future hour | Transmission Owner | Transmission System Characteristics Database | Future constraints | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 3.1b | In parallel to step 1a | Update constraints | (1b) Provide real-time data on transmission constraints and outages | Data Acquisition and Control (DAC) Subsystem | Transmission System Characteristics Database | Real-time constraints | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.1c | In parallel to step 1a | Update constraints | (1c) Update relevant transmission path constraints for each future hour | Other 2 RTOs | Transmission System Characteristics Database | Future and real-time constraints | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 3.2a | Periodically or upon request or upon event | Provide FTRs | (2a) Provide list of Firm Transmission Rights (FTR) Interfaces and Scheduling Points | Transmission Right Ownership Database | Congestion Management System | FTRs | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.2b | In parallel to step 2a | Provide transmission outages | (2b) Provide approved transmission outage schedules for the appropriate timeframes | Transmission Outage Schedule | Congestion Management System | Transmission outage schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.2c | In parallel to step 2a | Provide LGR outage schedules | (2c) Provide approved LGR outage schedules for the appropriate timeframes | LGR Generation Maintenance Schedule | Congestion Management System | LGR outage schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.2d | In parallel to step 2a | Provide transmission conditions | (2d) Provide update of transmission conditions for the appropriate timeframes | Transmission System Characteristics Database | Congestion Management System | Transmission conditions | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.3 | Periodically | Calculate TTC, ATC, and OTC | (3) Calculate TTC, ATC, and OTC for each FTR Interface and Scheduling Point | Congestion Management System | Operational Transmission Capacity | TTC, ATC, & OTC | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.4 | Upon request | Review OTC | (4) Review OTC data | Operational Transmission Capacity | RTO Scheduler | OTC | User Interface |
| 3.5 | By specific date and time | Approve OTC | (5) Approve OTC data | RTO Scheduler | Operational Transmission Capacity | OTC approvals | User Interface |
| 3.6a | By specific data and time | Updated OTC | (6a) Provide updated TTC, ATC, and OTC data | Operational Transmission Capacity | WMI Web Server | TTC, ATC, & OTC | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.6b | In parallel to step 6a | Calculate FDF | (6b) Provide updated Flow Distribution Factors (FDF) | FTR Requirements Matrix | WMI Web Server | FDF | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 3.6c | In parallel to step 6a | Updated OTC | (6c) Provide updated TTC, ATC, and OTC data | Operational Transmission Capacity | Other 2 RTOs | TTC, ATC, & OTC | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 3.7 | At specific date and time | Provide TTC, ATC, and OTC | (7) Provide TTC. ATC, OTC, and FDF data to Market Participants | WMI Web Server | Market Participant | TTC, ATC, & OTC | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |

## Long Term Auction of Transmission Rights (LTATR)

### Description

Scheduling Coordinators can participate in the auction for
transmission rights, dependent on the market rules.

### Diagram

if !vml?![](MO_Med_Term_Planning_files/image008.gif)endif?

### Steps for Long Term Auction of Transmission Rights

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4.0 | As needed | Input schedules | (As needed) Input schedules for legal existing contractual agreements | RTO Programmer Engineer Personnel | Existing Transmission Contracts | Transmission contracts | User Interface |
| 4.1 | Periodically or at specific time and date | Provide OTC | (1) Provide capacity needed for existing contracts | Existing Transmission Contracts | Operational Transmission Capacity | Transmission contracts | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.2 | After previous step | Calculate FTR | (2) Calculate conservative FTR from OTC minus previously auctioned FTRs, minus existing contracts | Operational Transmission Capacity | Available FTR | OTC | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.3 | At specific time and date | Trigger posting of FTR | (3) Trigger posting of FTRs | Time Line Manager | Available FTR | Trigger | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.4 | At specific time and date | Post FTR | (4) Post available FTRs, transmission outage schedules, & generation maintenance schedules | Available FTR | WMI Web Server | FTR | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.5a | On-going | Enter bids | (5a) Enter bids for FTRs | Scheduling Coordinator | WMI Web Server | Bids for FTR | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.5b | In parallel to step 5a | Enter bids | (5b) Enter bids for FTRs | Eligible Customers | WMI Web Server | Bids for FTR | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.6 | Before auction time | Receive bids | (6) Receive FTR bids during auction | WMI Web Server | FTR Market Clearing Price Auction Function | Bids for FTR | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.7 | At auction time | Trigger auction | (7) Trigger auction function | Time Line Manager | FTR Market Clearing Price Auction Function | Trigger | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.8a | After previous step | Post FTR winners | (8a) Post winners of FTR auction after auction close | FTR Market Clearing Price Auction Function | WMI Web Server | FTR winners | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.8b | In parallel to step 8a | Store FTRs | (8b) Store ownership of FTRs | FTR Market Clearing Price Auction Function | Transmission Right Ownership Database | FTR owners | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.9a | After previous step | Notify winners | (9a) Notify winners (and losers) of FTR | WMI Web Server | Scheduling Coordinator | FTR winners | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.9b | In parallel to step 9a | Notify winners | (9b) Notify winners (and losers) of FTR | WMI Web Server | Eligible Customers | FTR winners | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 4.9c | In parallel to step 9a | Provide FTR information | (9c) Provide FTR information to RTOs | WMI Web Server | Other 2 RTOs | FTR winners | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
