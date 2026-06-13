# RTP Base Calculation

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_Base_Calc_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Base Rate Calculation Function

## Contents

* [Narrative](CS_RTP_Base_Calc_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_Base_Calc_Use_Cases.htm#Steps)

## Narrative

Base RTP Calculation function develops tables
of load versus price for each “power system node” and for each
“settlement” period (e.g. each hour). These tables are the Base
RTP data. The purpose of this computation is to accurately
forecast the cost of providing energy during the period.

The RTP Base calculations are performed by the
Market Operations actor after the Load Forecast function is complete
to calculate the costs of delivering energy to customers during each
of the settlement periods (usually 1 hour intervals) in the horizon of
the calculations.  These calculations are usually performed on a
day-ahead basis so the information can be processed, transmitted to
ESPs and finally to the RTP customer in time for action.   RTP can be
calculated or modified on an hourly basis if marginal cost warrant and
customers are willing to subscribe and respond to such a service.

The base calculation require from the Load
Forecaster as well as costs information from a variety of sources.  
These costs include the fuel and variable costs associated with the
generation unit that will serve incremental load, adjustments for line
losses, a risk adders, and congestion fees.  There is concerted effort
in the industry to improve the speed and accuracy of the calculations
for more timely and accurate pricing.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Market Timer initiates the calculation of Base RTP tables | Base RTP Calculator | Calculate a table of RTP values for each “settlement” period and for different loads at different “power system nodes” | Load Forecaster | RTP Base Calculator | Load Forecast and marginal energy costs | [RTOs/Market Participants](../Environments/Env10_RTOs_to_Market_Participants.htm) |
| 1.2 | Market Timer initiates the posting of Base RTP data for ESPs | Market Interface Server | Base RTP Calculator posts Base RTP tables on Market Interface Server  for ESPs to access/download | RTP Base Calculator | Market Interface Server | Base RTP rates table | [Control Centers to ESPs](file:///C:/Documents/WPM/IntelliGrid/IntelliGrid_Web_Site/IntelliGrid_Architecture/Environments/Env9_Control_Centers_to_ESPs.htm) |
| 1.3 | Timer initiates ESP RTP Calculations | ESP Customer RTP rate calculations | ESP RTP system polls market interface server for updates to RTP base calculations.  If new data is available, it is downloaded and ESP Customer Rate Calculations | Market Interface Server | RTP Calculator | Base RTP rates table | [Control Centers to ESPs](file:///C:/Documents/WPM/IntelliGrid/IntelliGrid_Web_Site/IntelliGrid_Architecture/Environments/Env9_Control_Centers_to_ESPs.htm) |
