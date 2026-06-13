# RTP Cust Calculations

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_Customer_Calc_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Customer-Specific Rate Calculations Function

## Contents

* [Narrative](CS_RTP_Customer_Calc_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_Customer_Calc_Use_Cases.htm#Steps)

## Narrative

This function uses the base RTP values
calculated by Market Operators to calculate customer-specific RTP
rates, based on their tariffs and market conditions.

This function calculates the customer specific
RTP schedule that is sent to the customer’s BAS for implementation. 
The calculation is first based on the base RTP calculations performed
at the Market Operators level that take into account many factors
including the marginal energy costs, costs of losses, risk adjustments
among others.  These calculations are performed for each settlement
interval in the RTP schedule for every delivery node in the system.

The ESP uses the base RTP and applies factors
related to losses and other costs as well as local tariffs and
contracts with the customer.  The RTP may be combined with the CBL for
the customer if a two part rate is in place.  Once the customer
specify RTP schedule is calculated, it is communicated to the customer
or the customer Building Automation System (BAS) where the customer
can optimize their energy usage.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Base RTP table updates become available on Market Interface Server |  | Base RTP schedules are published on market interface server where the Energy Service Providers RTP system can access them. RTP Calculator application receives information on Base Real-Time Prices and calculates the customer-specific RTP tables for different customers based on contracts and tariffs. | Market  Interface Server | RTP Calculator | Base RTP schedules | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.2 | Updated Customer RTP schedules available |  | RTP calculator publishes customer specific schedules.  These schedules are made available to the customers via agreed communications method.  This could be Fax, Email or through WWW interface. | RTP Calculator | Customer Building Automation System | Customer Specific RTP schedules | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
