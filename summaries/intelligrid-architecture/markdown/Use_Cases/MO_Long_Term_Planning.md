# Long Term Planning

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/MO_Long_Term_Planning.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Long Term Planning - Market Operations

## Narrative

### Overview

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

### Description

The following is a
list of Western RTO functions related to long term planning for market
operations. Only the listed functions
with asterisks are represented in the diagrams and/or step-by-step
descriptions in section 2. The others are either subsets of the
functions or are not primarily an automated function.

1.       
Long Term Planning

a.       
Registration of Market Participants

·        
Credit rating of Market Participants

b.      
Capacity/Adequacy Market

c.      
[Updating the Power System Model](MO_Long_Term_Planning.htm#Power System Model Update (PSMU) Diagram and Steps)for ISO/RTO Regional Planning\*

·        
Register transmission data with WSCC EHV database

·        
Perform WSCC path studies

·        
Perform grid assessment

·        
Perform new generation connection studies

·        
Perform RMR studies

d.       
[Transmission and Generation Maintenance Coordination](MO_Long_Term_Planning.htm#Maintenance Coordination Function (MC) Diagram and Steps) \*

·        
Establish transmission and generation standards and guidelines

·        
Oversee ISO grid planning

e.       
Generation certification

## Power System Model Update (PSMU) for ISO/RTO Regional Expansion Planning

The purpose of ISO/RTO: Regional Expansion
Planning function is to develop load and capacity forecast
alternatives, by collecting load and capacity forecasts from different
market participants inside and outside the region, developing regional
and local alternatives of load and capacity, including coordination
with customers with special loads and/or generation capabilities. Also
coordinating transmission system planning submitted by transmission
owners, developing future regional power system model alternatives,
calculating and publishing future major operational parameters for the
expansion alternatives, and developing requirements for system
automation., directly involving RTO/ISO planners, Generation planners,
DR planners, transmission planners, distribution planners, regulators,
auditors, regional planning agencies, Special Customers, NERC, and
Market Participants, performing regional, long term load and capacity
planning and coordination of other planners within the region,
including long term adequacy and reliability analysis via studies to
assist in market decisions, with key interfaces between:

> 1. RTO/ISO and other RTOs
>
> 2. RTO and Transmission Owners
>
> 3. RTO and Generation Companies
>
> 4. RTO and DisCos
>
> 5. RTO and Special Customers
>
> 6. RTO and Security Coordinating
> Councils
>
> 7. RTO and NERC
>
> 8. RTO and Regulators
>
> 9. RTO and Auditors
>
> 10. RTO and Planning Agencies
>
> 11. RTO and Government offices,

if !vml?![](MO_Long_Term_Planning_files/image002.gif)endif?

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1a | Periodically or as needed | Update power system model | Provide updated transmission facilities model data and in-service dates | Transmission Owner | Power System Model | Transmission facilities | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.1b | Periodically or as needed | Update power system model | Provide updated generation facilities model data and in-service dates | GenCos | Power System Model | Generation facilities | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.1c | Periodically or as needed | Update power system model | Provide updated connection point model data and in-service dates | DisCos | Power System Model | Distribution facilities | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.1d | Periodically or as needed | Update power system model | Provide updated connection point model data and in-service dates | Eligible Customers | Power System Model | Customer facilities | [Control Center/ Corporations](../Environments/Env12_Control_Center_to_Corporate.htm) |
| 1.1e | Periodically or as needed | Update power system model | Provide updated transmission facilities model data and in-service dates | WSCC | Power System Model | WSCC transmission facilities | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.1f | Periodically or as needed | Update power system model | Provide updated transmission facilities model data and in-service dates | RTO Power System Model | Power System Model | Other RTO transmission facilities | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.2 | Periodically or as needed | Review updates | Review updates | Power System Model | RTO Programmer Engineer Personnel | Updates | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3 | After previous step | Review power model | Assure completeness and accuracy of updated model | RTO Programmer Engineer Personnel | Power System Model | Power System model | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4a | After previous step | Issue updated power system model | Issue updated power system model | Power System Model | Eligible Customers | Power System model | [Control Center/ Corporations](../Environments/Env12_Control_Center_to_Corporate.htm) |
| 1.4b | After previous step | Issue updated power system model | Issue updated power system model | Power System Model | DisCos | Power System model | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.4c | After previous step | Issue updated power system model | Issue updated power system model | Power System Model | GenCos | Power System model | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.4d | After previous step | Issue updated power system model | Issue updated power system model | Power System Model | Transmission Owner | Power System model | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.4e | After previous step | Issue updated power system model | Issue updated power system model | Power System Model | WSCC | Power System model | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 1.4f | After previous step | Issue updated power system model | Issue updated power system model | Power System Model | RTO Power System Model | Power System model | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |

## Maintenance Coordination Function (MC) for Transmission System Planning

The purpose of Transmission Owners/Distribution
Utilities: System Planning function is to develop transmission and
distribution facility plans for the long term, based on load and
capacity forecasts, RTO or other regional plans, regulator
requirements, neighboring utility requirements, and customer
requirements. In addition to facility plans, detailed automation plans
will be developed, directly involving transmission data, distribution
data, generation planners, customers, DR planners, regulators,
auditors, vendors, regional planning agencies, and government
agencies, performing long term transmission and distribution
facilities and automation planning, with key interfaces between

> 1. TransCos and RTOs
>
> 2. TransCos and neighboring utilities
>
> 3. TransCos and generation companies
>
> 4. TransCos and DR owners
>
> 5. TransCos and planning agencies
>
> 6. TransCos and large customers
>
> 7. TransCos and government agencies,

if !vml?![](MO_Long_Term_Planning_files/image004.gif)endif?

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1a | Periodically or upon event | Submit outage schedules | (1a) Submit relevant proposed transmission outage schedules | Other 2 RTOs | Transmission Outage Schedule | Transmission outage schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.1b | Periodically or upon event | Submit outage schedules | (1b) Submit long term proposed transmission outage schedules | Transmission Owner | Transmission Outage Schedule | Transmission outage schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.1c | Periodically or upon event | Submit outage schedules | (1c) Submit long term proposed Local Generation Resources (LGR) generation maintenance schedules | GenCos | LGR Generation Maintenance Schedule | Generation maintenance schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.2a | After previous step | Analyze outage schedules | (2a) Provide proposed transmission outage schedules | Transmission Outage Schedule | Maintenance Outage Function | Transmission outage schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.2b |  | Analyze maintenance schedules | (2b) Provide proposed generation maintenance schedules | LGR Generation Maintenance Schedule | Maintenance Outage Function | Generation maintenance schedules | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
| 2.2c |  | Provide power system model | (2c) Provide Base Case model | Power System Model | Maintenance Outage Function | Power system model | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2d |  | Provide load forecast | (2d) Provide LT Load Forecast | Long Term Load Forecast | Maintenance Outage Function | Load forecast | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.2e |  | Provide energy schedules | (2e) Provide all schedules already submitted by Scheduling Coordinator and all existing contracts | Energy Schedule Database | Maintenance Outage Function | Energy schedules | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3 | At specific time and date | Determine acceptable schedules | (3) Once a month on a specific day, work with maintenance outage requests to determine acceptable outage schedules | Maintenance Outage Function | RTO Scheduler | Outage schedules | User Interface |
| 2.4a | After previous step | Accept transmission outage schedule | (4a) Accept transmission outage schedule | RTO Scheduler | Transmission Outage Schedule | Accepted transmission outage schedules | User Interface |
| 2.4b |  | Reject transmission outage schedule | (4b) Reject transmission outage schedule | RTO Scheduler | Transmission Outage Schedule | Rejected transmission outage schedules | User Interface |
| 2.4c |  | Accept generation maintenance schedule | (4c) Accept generation maintenance schedule | RTO Scheduler | LGR Generation Maintenance Schedule | Accepted generation maintenance schedules | User Interface |
| 2.4d |  | Reject generation maintenance schedule | (4d) Reject generation maintenance schedule | RTO Scheduler | LGR Generation Maintenance Schedule | Rejected generation maintenance schedules | User Interface |
| 2.5a | After previous step | Transmission outage scheduling results | (5a) Receive acceptance or warning on transmission outage schedule | Transmission Outage Schedule | Other 2 RTOs | Outage scheduling results | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 2.5b |  | Transmission outage scheduling results | (5b) Receive acceptance or rejection of transmission outage schedules | Transmission Outage Schedule | Transmission Owner | Outage scheduling results | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.5c |  | Generation maintenance results | (5c) Receive acceptance or rejection of LGR generation maintenance schedules | LGR Generation Maintenance Schedule | GenCos | Generation maintenance schedule results | [Inter-Control Center](../Environments/Env8_Inter-Control_Center.htm) |
