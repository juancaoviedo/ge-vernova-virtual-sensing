# RTP Mrkt Operations

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_Market_Ops_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Market Operations for Energy Schedules Function

## Contents

* [Narrative](CS_RTP_Market_Ops_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_Market_Ops_Use_Cases.htm#Steps)

## Narrative

Market Operations Energy Services, for the
purposes of this use case, collects bid and offers into the energy
market from Energy Service Providers (ESP) and other aggregators
of distributed energy resources.

For this use case, the ESP or other aggregator
submits bids and/or offers based upon bids and offers made by their
customers.  The aggregator may submit bids in several tiers to
accommodate a range in quality and price of services.

Market Operations Energy Services, for the
purposes of this use case, collects bid and offers into the energy
market from Energy Service Providers (ESP) and other aggregators of
distributed energy resources.  Market Operation System  evaluates
incoming bids against needs and accepts or rejects those offers.  The
detailed process for evaluating bids and offers is detailed in Market
Operation System  cone, Day Ahead use cases.

Once the bids and offers are evaluated and
accepted or declined, the results are posted on the marker interface
server is used or transmitted to the ESP for scheduling and action.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | ESP aggregates bids and offers |  | ESP transmits energy bid/offer data to market operations | ESP | Market Interface Server | Aggregate energy bids and offers | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.2 | Completion of previous Step |  | Bid evaluation system processes loads data from market interface server.  Bids are processed and evaluated against needs for the period.  Some or all of the bids maybe accepted or rejected. | Market Interface Server | Bid Evaluation System | Aggregate energy bids and offers | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.3 | Completion of previous Step |  | Acceptance or rejections status is transferred to the market interface server | Bid Evaluation System | Market Interface Server | Accepted energy bids and offers | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.4 | Timer |  | ESP polls Market Server for bid status.  Status is transferred to the ESP Aggregation System, | Market Interface Server | ESP Aggregation System | Accepted energy bids and offers | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
