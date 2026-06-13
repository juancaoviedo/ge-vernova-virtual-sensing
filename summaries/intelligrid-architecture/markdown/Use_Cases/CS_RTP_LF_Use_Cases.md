# RTP Load Forecast

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_LF_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Load Forecasting Function

## Contents

* [Narrative](CS_RTP_LF_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_LF_Use_Cases.htm#Steps)

## Narrative

The Load Forecasting function of RTP uses
transmission and distribution information, energy schedules,
weather, and past history to forecast loads on and
interval-by-interval basis.  The forecast is used, in part, to
develop the Base RTP calculation.

Periodically, the Market Timer, (the RTO/ISO
market operations system or other market entity, depending upon the
market design) forecasts power system conditions for a specific
period, say the next 24 hours, based on energy schedules and prices
already submitted, ancillary services available, weather conditions,
day of the week, scheduled outage information from transmission and
distribution operations, and real-time information from transmission
and distribution operations, etc.

The Load Forecasting function uses historical
load forecasts databases and combines that information about the
energy generation schedules, transmission and distribution system
constraints and ancillary services bids to estimate the load for areas
within the system studied.  Various load forecasting packages approach
the problem in different ways but all use these input and combine
weather, time of the year, day of the week and other correlated
variables to predict customer behavior for the specific settlement
periods being forecasted.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Market Timer initiates the forecast power system condition |  | Forecast power system conditions for the next “settlement” periods |  |  |  |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.1 |  |  | Load energy schedules from Energy Schedule Database. | Energy Schedule Database |  | Energy schedules | APIs needed between databases and application | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.2 |  |  | Load Ancillary services bids/offers from database | Ancillary Services Bids/Offers |  | Ancillary Services Bids | APIs needed between databases and application | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
| 1.1.3 |  |  | Load weather forecasts from Weather Service | Weather Service |  | Weather forecasts | Existing weather protocol  and weather format must be used | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.4 |  |  | Load historical load data a from historical load database | Historic Load Database |  | Historical load data | APIs needed between databases and application | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.5 |  |  | Load transmission system information for outages and constraints | Transmission System Data |  | Transmission outage and constraint data | Inter utility communications must be supported | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.6 |  |  | Load distribution system information for outages and constraints | Distribution System Data |  | Distribution outage and constraint data | Inter utility communications must be supported | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2 | Completion of Load Forecasting application |  | Post results of load forecast to load forecast database for other applications to access (RTP base rate calculator) | Load Forecaster | Forecast Loads | Load Forecast | APIs needed between databases and application | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
