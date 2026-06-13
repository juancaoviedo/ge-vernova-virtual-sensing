# RTP Ancilliary Services

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_Market_Ops_Ancilliary_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Market Operations Ancillary Services Function

## Contents

* [Narrative](CS_RTP_Market_Ops_Ancilliary_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_Market_Ops_Ancilliary_Use_Cases.htm#Steps)

## Narrative

Market Operations Energy Services, for the
purposes of this use case, collects bid and offers into the
ancillary services market from Energy Service Providers (Energy
Service Provider) and other aggregators of distributed ancillary
resources.

Market Operations Energy Services, for the
purposes of this use case, collects bid and offers into the ancillary
services market from Energy Service Providers (Energy Service
Provider) and other aggregators of distributed ancillary resources. 
Market Operations evaluates incoming bids against needs and accepts or
rejects those offers.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Energy Service Provider aggregates bids and offers |  | Energy Service Provider transmits ancillary services  bid/offer data to market operations | Energy Service Provider | Market Interface Server | Aggregate ancillary services  bids and offers | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
| 1.2 | Completion of previous Step |  | Bid evaluation system processes loads data from market interface server.  Bids are processed and evaluated against needs for the period.  Some or all of the bids maybe accepted or rejected. | Market Interface Server | Bid Evaluation System | Aggregate ancillary services  bids and offers | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.3 | Completion of previous Step |  | Acceptance or rejections status is transferred to the market interface server | Bid Evaluation System | Market Interface Server | Accepted ancillary services  bids and offers | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.4 | Timer |  | Energy Service Provider polls Market Server for bid status.  Status is transferred to the Energy Service Provider Aggregation System. | Market Interface Server | Energy Service Provider Aggregation System | Accepted ancillary services  bids and offers | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
