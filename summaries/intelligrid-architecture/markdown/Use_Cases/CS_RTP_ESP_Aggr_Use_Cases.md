# RTP ESP Aggregation

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_ESP_Aggr_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP ESP Aggregation Function

## Contents

* [Narrative](CS_RTP_ESP_Aggr_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_ESP_Aggr_Use_Cases.htm#Steps)

## Narrative

Energy Service Provider (ESP) collects energy
and ancillary services bids and offers from RTP and other DER
subscribing customers.  The ESP combines those bids into an
aggregate bid into the market operations bid/offer system.  When
accepted, the ESP notifies the end customer of the status and
requests scheduling of the services.

Energy Service Provider (ESP) collects energy and
ancillary services bids and offers from RTP and other DER subscribing
customers.  The ESP combines those bids into an aggregate bid into
market operations.  The incoming bids are prioritized and based on
price, quality and size.  Bids may be based upon distributed
generation or other resource such as deferrable load or switch-able
capacitors for reactive power supply/voltage support.  These bids are
combined and offered into the market operations bid/offer system. 
Market Operations evaluates the bids against the energy and ancillary
services needs in the system based upon the load forecast, energy
schedules and marginal costs for generation.  Market operations will
notify the ESP of acceptance of the bids and requests that the
services be scheduled.  The ESP then determines the best set of
customer bids to meet the accepted aggregate bid.  The ESP then
notifies the selected customers of the accepted bids and requests that
the services be scheduled.

It is possible that Market Operations may issue
new RTP base tables if the energy bids significantly effect marginal
costs.  If so an iteration of the RTP pricing process may be initiated
if the tariffs allow for such.

Some customers may be subscribers to independent
energy and ancillary services aggregation provides who intern offer
into Market Operations bid/offer system.  This use case deals
specifically with ESP RTP customers.

## Steps

| # | Event | Primary Actor | Name of Process/ Activity | Description of   Process/ Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Customer completes bid / offer optimizations | Customer |  | Customer makes calculations indicating advantages to bidding energy or ancillary services to ESP/aggregator.  Customer transmits bids to ESP. | Customer | ESP Bid and Offer System | Customer Bids and Offers | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.2 | ESP Receives bids | ESP Bid and Offer System |  | ESP aggregates bid from multiple customers. | ESP Bid and Offer System | ESP Aggregation System | Customer Bids and Offers | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.3 | ESP Aggregates bids and offers | ESP Aggregation System |  | ESP submits bids and offers to Market operations energy and ancillary services bid and offer system for evaluation and acceptance | ESP Aggregation System | Market Ops. Bid and Offer System | Aggregated Bids and Offers | [RTOs/ Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.4 | Market Operations evaluates bid/ offers | Market Ops. Bid and Offer System |  | Market Operations evaluates bids and offers from multiple sources and accepts some and rejects others.  Notification of bid or offer status is sent to bidders | Market Ops. Bid and Offer System | ESP Aggregation System | Acceptance of Aggregated Bids and Offers | [RTOs/ Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.5 | Market Ops accepts bids and offers | ESP Aggregation System |  | ESP evaluates the overall bid acceptance, and allocates various customer bids to fulfill commitments. | ESP Aggregation System | ESP Bid and Offer System | Acceptance of Bids and Offers | [RTOs/ Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.6 | ESP bid acceptance | ESP Bid and Offer System |  | Customers are notified by ESP of bid status. | ESP Bid and Offer System | Customer | Acceptance of Bids and Offers | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
