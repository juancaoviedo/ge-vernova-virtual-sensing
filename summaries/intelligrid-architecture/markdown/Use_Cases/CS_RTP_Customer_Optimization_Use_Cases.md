# RTP Cust Optimization

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_Customer_Optimization_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Customer's Optimization Function

## Contents

* [Narrative](CS_RTP_Customer_Optimization_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_Customer_Optimization_Use_Cases.htm#Steps)

## Narrative

The RTP system provides the RTP schedule
through email, pager, bulletin board or direct transfer.   The RTP
operator at for the customer must enter the schedule into the
building automation software (BAS) and perform the necessary
optimization activities to implement the RTP goals.  Note that EMS
or Energy Management System is often used interchangeably with
BAS.

The Energy Services Provider (Energy Service
Provider) obtains the Base RTP data tables from the Market Interface
Server, and uses them to develop Customer-specific RTP rate tables.
These calculations are based on contractual agreements between the
Energy Service Provider and the different types of customers it
serves. For example, a large industrial customer that can curtail
large loads during peak hours will get a different rate than a small
commercial customer with less ability to modify its load.   The Energy
Service Provider sends these Customer-specific RTP rate tables to each
of the customers it serves, using different mechanisms: fax, email, or
direct data channels (e.g. dial-up telephone or AMR system).

The customer’s Building Automation System (BAS)
optimizes its loads and distributed energy resources (DER), based on
the customer-specific rate table it receives, the load requirements
and constraints, and any DER requirements, capabilities, and
constraints. The BAS understands the nature and opportunity for
altering consumption based on economic and comfort drivers, and, the
physical dynamics of the specific customer premises. The BAS then
issues (or updates existing) schedules and other control mechanisms
for loads and for DER generation. These control actions may be
automatically implemented or may be reviewed and changed by the
customer. The Customer’s BAS may then send generation schedules to the
DER management system for it to implement during each “settlement”
period.  Note that the BAS may be a human as apposed to a software
system.

The BAS system uses the site-optimized algorithms
to forecast its load and DER generation. It also determines what
additional ancillary services it could offer, such as increased DER
generation or emergency load reduction, and calculates what bid prices
to offer these ancillary services at.  The BAS then submits these
energy schedules and ancillary services bids to the Energy Service
Provider (or Scheduling Coordinator, depending upon market structure),
as input to the RTO/ISO market operations.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Timer or Notification of new rates available | Customer processes RTP schedule | The customer receives and processes the RPT schedule for the next period.  This could be by accessing a web page or reading email. | Energy Service Provider | Customer | RTP rates | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.2 | Receipt of new rates | Customer Enters data into BAS | The customer enters the RTP schedule for the next period into the BAS. | Customer | Customer Building Automation System | RTP rates | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.3A.1 | Entry of new rates | Load Optimizations based on RTP | Customer Building Automation System optimizes projected loads, deferrable load and DER based on requirements, constraints and RTP rates. | Customer Building Automation System | Customer | Load deferment and DER schedules | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.3A.2 | BAS optimizations complete | Customer Review of BAS optimizations | Customer reviews the load schedule and approves based on external criteria | Customer | Customer | Load deferment and DER schedules | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.3A.3 | Load deferment and DER schedules approved | Implement Load and DER schedules | The customer now implements the approved load and der schedules either manually or enabling the schedule in the BAS. | Customer |  | Load deferment and DER schedules | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.3B.1 |  | Energy / ancillary services bids | Customer BAS evaluates bids into energy and ancillary services. | Customer Building Automation System | Customer | Energy / ancillary services bids | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.3B.2 | BAS optimizations complete | Customer review of energy and ancillary services bids | Customer reviews the proposed bids into energy and ancillary services markets, verifying availability and bid data. | Customer | Customer | Energy / ancillary services bids | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.3B.3 | Review of energy and ancillary services bid | Transmit Bids to Energy Service Provider | Customer, having approved the energy and or ancillary bids, transmits those bids to the Energy Service Provider or market operator | Customer | Energy Service Provider | Energy / ancillary services bids | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
