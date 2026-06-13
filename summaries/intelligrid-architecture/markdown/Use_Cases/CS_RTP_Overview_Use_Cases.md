# RTP Use Cases

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_Overview_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Overview of Real Time Pricing (RTP) Function

## Contents

* [List of RTP
  Subfunctions](CS_RTP_Overview_Use_Cases.htm#List of RTP Subfunctions)
* [Narrative](CS_RTP_Overview_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_Overview_Use_Cases.htm#Steps)

## List of RTP Subfunctions

* [RTP Load
  Forecast](CS_RTP_LF_Use_Cases.htm)
* [RTP ESP Aggregation](CS_RTP_ESP_Aggr_Use_Cases.htm)
* [RTP Base Rate Calculations](CS_RTP_Base_Calc_Use_Cases.htm)
* [RTP Customer-Specific Rate Calculations](CS_RTP_Customer_Calc_Use_Cases.htm)
* [RTP Customer Optimization Using Building
  Automation System](CS_RTP_Customer_Optimization_Use_Cases.htm)
* [RTP DER Management](CS_RTP_DER_Mgmt_Use_Cases.htm)
* [RTP Market Operations for Energy Schedules](CS_RTP_Market_Ops_Use_Cases.htm)
* [RTP Market Operations for Ancillary Services](CS_RTP_Market_Ops_Ancilliary_Use_Cases.htm)

## Narrative

### RTP Objective

*The objective of the Real-Time
Pricing Enterprise Activity is to permit customers to
plan and modify their load and generation in response to
price signals in “real-time” (operational timeframe
which can range from seconds to days ahead), received
from an Energy Services Provider who acts as an
intermediary to the Market Operations. Customers can
also provide their forecasted loads and generation into
the Market Operations (possibly through the ESP as an
aggregator) as energy schedules and ancillary
bids/offers. For operators of the power distribution
system, Real-Time Pricing provides a mechanism for
potentially significant changes in aggregated load based
on sharing cost drivers with the customer in an elective
supervisory control scheme.*

### RTP Day-in-the-Life Scenario

A typical day-in-the-life
scenario is as follows (note that the discussion is
marked up with numbers that are used later in the
analysis to derive requirements from the scenario):

In the historical energy supply
system, the time-based analysis of customer consumption
of energy was cost prohibitive. Yet, the actual cost of
providing energy is substantially time and load
dependent. The regulated utility was the great averaging
factor for these variable costs. Today, modern
electronics and communications make it cost effective to
apply a more accurate allocation of costs and usages of
energy. Real-time pricing is a market mechanism to
provide for dynamic feedback control and pricing of
energy based on genuine costs.

**(1)**Periodically,
the RTO/ISO market operations system (or other market
entity, depending upon the market design) forecasts
power system conditions for a specific period, say the
next 24 hours, based on energy schedules and prices
already submitted, ancillary services available, weather
conditions, day of the week, scheduled outage
information from transmission and distribution
operations, and real-time information from transmission
and distribution operations, etc.

**(2)**From
these forecasts, an RTP Calculation function develops
tables of load versus price for each “power system node”
and for each “settlement” period (e.g. each hour). These
tables are the **Base RTP data**. The purpose of this
computation is to accurately forecast the cost of
providing energy during the period.
**(3)**These
Base RTP tables are made available to all subscribers of
this information (depending upon market rules),
typically by being uploaded to a Market Interface
Server.

**(4)**The
Energy Services Provider (ESP) obtains the Base RTP data
tables from the Market Interface Server, and uses them
to develop **Customer-specific RTP rate tables**.
These calculations are based on contractual agreements
between the ESP and the different types of customers it
serves. For example, a large industrial customer that
can curtail large loads during peak hours will get a
different rate than a small commercial customer with
less ability to modify its load. **(5)**The ESP
sends these Customer-specific RTP rate tables to each of
the customers it serves, using different mechanisms:
fax, email, or direct data channels (e.g. dial-up
telephone or AMR system).

**(6)**The
customer’s Building Automation System (BAS) optimizes
its loads and distributed energy resources (DER), based
on the customer-specific rate table it receives, the
load requirements and constraints, and any DER
requirements, capabilities, and constraints. The BAS
understands the nature and opportunity for altering
consumption based on economic and comfort drivers, and,
the physical dynamics of the specific customer premises.
**(7)**The
BAS then issues (or updates existing) schedules and
other control mechanisms for loads and for DER
generation. These control actions may be automatically
implemented or may be reviewed and changed by the
customer. **(8)**The
Customer’s BAS may then send generation schedules to the
DER management system for it to implement during each
“settlement” period.

**(9)**The
BAS system uses the site-optimized algorithms to
forecast its load and DER generation. It also determines
what additional ancillary services it could offer, such
as increased DER generation or emergency load reduction,
and calculates what bid prices to offer these ancillary
services at. **(10)**The
BAS then submits these energy schedules and ancillary
services bids to the ESP (or Scheduling Coordinator,
depending upon market structure), as input to the
RTO/ISO market operations.

**(11)**The ESP aggregates (or leaves as
individual information) the energy schedules and
ancillary service bids, and submits them to the market
operations. These will affect the next iteration of RTP
calculations.

**(12)**As
each “settlement” period is reached or during each
period as optimal, the BAS issues load control commands
to the end devices (setting levels, cycling, turning
on/off, etc.). The DER management system controls the
DER devices according to the DER schedule.

**(13)**The distribution operations systems
monitor any larger DER devices to ensure power quality
constraints are met, and to help manage emergency
situations (detailed in the Advanced Distribution
Automation Use Case). **(14)**Load
and generation deviations, as well as initiation of
ancillary services which have been requested by the
market operations, are handled according to normal
market operations procedures (as detailed in the Market
Operations Use Case).

**(15)**In the post “settlement” period (as
shown in the Meter Reading Use Case), customer load and
generation meters are read by Meter Data Management
Agents (MDMAs) and passed to the market operations
settlement systems (as shown in the Market Operations
Use Case). *{Not shown in the RTP Work Flow drawing}*The availability of fine-grained load profile
information (for example, measurements integrated for
each 15 minute period of consumption during the billing
period), allows for accurate application of the agreed
upon tariff.

**(16)**External regulators and auditors
review the RTP base and customer-specific tables to
ensure compliance with market rules.

if !vml?![](CS_RTP_Overview_Use_Cases_files/image002.gif)endif?

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Market Timer initiates the forecast  of power system conditions | System Forecast | Forecast power system conditions for the next “settlement” periods | - Energy schedules database  - Ancillary service bids/offers database  -Transmission SCADA system  - Distribution SCADA system  - Weather services  - Historical Load Forecast database | Power system Load Forecast application | - Energy schedules  - Ancillary services bids/offers  - Transmission outage and constraint data  - Distribution outage and constraint data  - Weather forecasts  - Historical forecast data and parameters | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2 | Market Timer  initiates the calculation of  Base RTP tables | Base RTP Calculation | Calculate a table of RTP values for each “settlement” period and for different loads at different “power system nodes” | Power system Load Forecast application | Base RTP Calculator | Forecasts of loads and generation at each node | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3 | Market Timer initiates the posting of Base RTP data for ESPs | Base RTP Posting | Base RTP Calculator posts Base RTP tables on Market Interface Server for ESPs to access/download | Base RTP Calculator | Market Interface Server | Base RTP data tables which consist of a matrix of:  ·        Nodes  ·        Settlement periods  ·        Loads  ·        Base prices | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
| 1.4 | Base RTP table updates become available on Market Interface Server | Base RTP Download | RTP Calculator application receives information on Base Real-Time Prices and calculates the customer-specific RTP tables for different categories of customers | Market Interface Server | Energy Services Provider (ESP) RTP Calculator | Base RTP data tables which consist of a matrix of:  ·        Nodes  ·        Settlement periods  ·        Loads  ·        Base prices | [Control Centers to ESPs](file:///C:/Documents/WPM/IntelliGrid/IntelliGrid_Web_Site/IntelliGrid_Architecture/Environments/Env9_Control_Centers_to_ESPs.htm) |
| 1.5 | ESP calculates customer-specific RTP tables | Customer RTP Calculation | ESPs issue customer-specific RTP rate tables to appropriate contracted customers | RTP Calculator | Customer Building Automation Systems (BAS) optimization application | Customer-specific RTP rate tables which consist of a matrix of:  ·        Nodes  ·        Settlement periods  ·        Loads  ·        Customer rates | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.6 | BAS implements a secure session,  receives RTP rate tables and acknowledges | Customer RTP Receipt | BAS Optimization application optimizes loads and DER generation, based on requirements, constraints, and RTP rates | Customer BAS optimization application | Load Schedule database  DER Schedule database | ·        Load schedule  ·        DER generation schedule | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.7 | Customers may review schedules | Customer RTP Review | Issues schedules for review | Customer BAS optimization application | Customer | ·        Load Schedule database  ·        DER Schedule database | User Interface |
| 1.8 | BAS issues schedules | Schedule Generation | BAS updates schedules based on any Customer input | Customer BAS optimization application | Load Schedule database  DER Schedule database | ·        Load Schedule database  ·        DER Schedule database | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.9 | Customer Load Forecast and Ancillary Services bids/offers | Customer Load Forecast | Calculate and update customer load forecasts and generation bids and/or offers | Forecast timer | Customer load forecast and generation bid/offers application | ·        Customer load forecasts  ·        Ancillary services bids and/or offers | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.10 | Submittal of Load Forecasts and A/S bids/offers | Load and A/S Bid Submittal | Submit customer load forecasts and ancillary services bids and/or offers to the EPS for aggregation into the market | Customer load forecast and generation bid/offers application | ESP Aggregator applications | ·        Customer load forecasts  ·        Ancillary services bids and/or offers | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.11 | Aggregate loads and A/S | Aggregate Loads | Submit aggregated loads as energy schedules  Submit A/S bids and/or offers | ESP Aggregator applications | Energy Scheduler and A/S Services application | ·        Aggregated energy schedules  ·        Aggregated A/S bids and/or offers | [Control Centers to ESPs](file:///C:/Documents/WPM/IntelliGrid/IntelliGrid_Web_Site/IntelliGrid_Architecture/Environments/Env9_Control_Centers_to_ESPs.htm) |
