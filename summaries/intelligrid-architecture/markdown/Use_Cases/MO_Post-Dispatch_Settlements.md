# Post Dispatch

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/MO_Post-Dispatch_Settlements.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Post Dispatch Settlements

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
Western RTO functions. The descriptions of the functions below may or
may not represent the final market rules and market operations,
because these have not been finalized yet.

The following is a
list of Western RTO functions related to Post Dispatch Market
Operations.

Only the listed
functions with asterisks are represented in the diagrams and/or
step-by-step descriptions in section 2.

1.       
Post-Dispatch

a.       
[Metering Data Collection](MO_Post-Dispatch_Settlements.htm#Metering Data Collection (MDC))
\*

·        
Register meters

·        
Process meter revenue data

b.      
[Transmission and Distribution Schedule Checkout](MO_Post-Dispatch_Settlements.htm#Transmission and Ancillary Services Schedule Checkout (TASC)) \*

c.       
[Financial
Settlements](MO_Post-Dispatch_Settlements.htm#Market Operations Financial Settlements (MOFS)) \*

·        
LMP Calculation

·        
Losses calculation

·        
Reconcile ISO market

·        
Reconcile real-time market

·        
Resolve disputes

d.      
[Accounting
and Billing](MO_Post-Dispatch_Settlements.htm#Market Operations Accounting and Billing (MOAB)) \*

·        
Create budget and financial
forecast

·        
Manage accounts payable

·        
Manage accounts receivable

·        
Purchasing

e.       
[Market Monitoring and
Auditing](MO_Post-Dispatch_Settlements.htm#Market Monitoring and Auditing (MMA)) \*

·        
Develop monitoring criteria

·        
Perform market assessment

·        
Investigate market abuse

## Metering Data Collection (MDC)

### Description

Revenue metering data for each interval must be collected from all
sites in order to provide the actual values for use during
Settlements.

### Diagram

if !vml?![](MO_Post-Dispatch_Settlements_files/image002.gif)endif?

### Steps for Metering Data Collection

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1a | Every metering cycle | Provide interval meter readings | Provide interval meter readings | Interval Meters | Eligible Customer Metered Entity | Meter readings |  |
| 1b |  | Provide interval meter readings | Provide interval meter readings | Interval Meters | Metered Entities | Meter readings |  |
| 2a |  | Provide metering data | Provide metering data | Metered Entities | Settlement Data Mgmt Agent | Meter readings |  |
| 2b |  | Provide monthly meter readings | Provide monthly meter readings | Standard Customers Meters | Settlement Data Mgmt Agent | Meter readings |  |
| 2c |  | Provide interval metered data | Provide interval metered data | Eligible Customer Metered Entity | Settlement Data Mgmt Agent | Meter readings |  |
| 2d |  | Apply load profiles to non-interval meter readings | Apply load profiles to non-interval meter readings | Load Profiles | Settlement Data Mgmt Agent | Load data |  |
| 3 |  | Provide metering data | Provide metering data | Metered Entities | Transmission Owner | Meter readings |  |
| 4a |  | Provide validated metering data in a standard meter format | Provide validated metering data in a standard meter format | Transmission Owner | RTO Meter Data Management System | Meter readings |  |
| 4b |  | Provide validated and aggregated metering data in a standard meter format | Provide validated and aggregated metering data in a standard meter format | Settlement Data Mgmt Agent | RTO Meter Data Management System | Meter readings |  |

## Transmission and Ancillary Services Schedule Checkout (TASC)

### Description

Actual versus Submitted Schedules must be verified by both the
Scheduling Coordinators and the RTO/ISOs.

### Diagram

if !vml?![](MO_Post-Dispatch_Settlements_files/image004.gif)endif?

### Steps for Transmission and Ancillary Services Schedule Checkout

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (1a) | Cycle for checking out actual vs. planned energy schedules | Provide actual schedule | Provide actual schedule | Operating Plan | Settlement System | Actual energy schedule |  |
| (1b) |  | Provide actual schedules from other RTOs | Provide actual schedules from other RTOs | Other 2 RTOs | Settlement System | Actual energy schedule |  |
| (2) |  | On 1st day after Trading Day, initiate preliminary schedule checkout | On 1st day after Trading Day, initiate preliminary schedule checkout | Settlement Administrator | Settlement System | Actual energy schedule vs. planned energy schedules |  |
| (3) |  | Provide preliminary schedule checkout | Provide preliminary schedule checkout | Settlement System | Scheduling Coordinators | Actual energy schedule vs. planned energy schedules |  |
| (4) |  | By 4th day after Trading Day, file schedule disputes | By 4th day after Trading Day, file schedule disputes | Scheduling Coordinators | Settlement System | Disputed energy schedules |  |
| (5) |  | Review and resolve disputes | Review and resolve disputes | Settlement System | Settlement Administrator | Disputes |  |
| (6) |  | By 5th day after Trading Day, initiate final schedule checkout | By 5th day after Trading Day, initiate final schedule checkout | Settlement Administrator | Settlement System | Final resolutions on energy schedule |  |
| (7a) |  | Report validated schedules to NERC | Report validated schedules to NERC | Settlement System | NERC | Final validated energy schedules |  |
| (7b) |  | Report validated schedules to other RTOs | Report validated schedules to other RTOs | Settlement System | Other RTOs | Final validated energy schedules |  |

## Market Operations Financial Settlements (MOFS)

Financial transactions must be finalized based on the market rules
and the actual vs submitted schedules.

### Diagram

if !vml?![](MO_Post-Dispatch_Settlements_files/image006.gif)endif?

### Steps for Market Operations Financial Settlements

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (1a) | Cycle for handling market operations settlements | Provide metering data | Provide metering data | RTO Meter Data Management System | Settlement System | Metering data |  |
| (1b) |  | Provide relevant metering data | Provide relevant metering data | RTO Meter Data Management System | Transmission Owner | Metering data |  |
| (2) |  | On day 46 after Trading Day, initiate preliminary settlement | On day 46 after Trading Day, initiate preliminary settlement | Settlement Administrator | Settlement System | Preliminary settlement information |  |
| (3) |  | Provide preliminary settlement | Provide preliminary settlement | Settlement System | Scheduling Coordinators | Preliminary settlement information |  |
| (4) |  | By day 52, file settlement disputes | By day 52, file settlement disputes | Scheduling Coordinators | Settlement System | Any disputed settlements |  |
| (5) |  | Review and resolve disputes | Review and resolve disputes | Settlement System | Settlement Administrator | Disputed information |  |
| (6) |  | By day 58, issue final settlement | By day 58, issue final settlement | Settlement Administrator | Settlement System | Final settlement information |  |
| (7) |  | Provide final settlement | Provide final settlement | Settlement System | Scheduling Coordinators | Final settlement information |  |

## Market Operations Accounting and Billing (MOAB)

### Description

Accounting and billing must be finalized for each settlement
period, according to the market rules.

### Diagram

if !vml?![](MO_Post-Dispatch_Settlements_files/image008.gif)endif?

### Steps for Market Operations Accounting and Billing

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (1a) | Cycle for Accounting and Billing | Provide settlement information | Provide settlement information | Settlement System | Billing System | Settlement data |  |
| (1b) |  | Provide transmission metering data | Provide transmission metering data | RTO Meter Data Management System | Billing System | Metering data |  |
| (2) |  | Issue invoice | By day 91, issue invoice | Settlement Administrator | Billing System | Invoice |  |
| (3) |  | Pay invoices | By day 96, pay invoices | Scheduling Coordinators | Billing System | Payment |  |
| (4) |  | Pay Transmission Owners | By day 97, pay Transmission Owners based on metering data | Billing System | Transmission Owner | Payment |  |

## Market Monitoring and Auditing (MMA)

### Description

All schedules, actions, and actual energy flows must be available
to market monitors. The exact set of auditable data must be set by the
market rules.

### Diagram

if !vml?![](MO_Post-Dispatch_Settlements_files/image010.gif)endif?

### Steps for Market Monitoring and Auditing

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1a | Periodically or Spot Check | Review archival information | Review archival information | Auditor | Archives | Market operations information |  |
| 1b |  | Review logs | Review logs | Auditor | Logs | Market operations information |  |
