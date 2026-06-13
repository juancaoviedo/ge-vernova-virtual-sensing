# RTP DER Mgmt

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_RTP_DER_Mgmt_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - RTP Customer's Optimization Function

## Contents

* [Narrative](CS_RTP_DER_Mgmt_Use_Cases.htm#Narrative)
* [Steps](CS_RTP_DER_Mgmt_Use_Cases.htm#Steps)

## Narrative

The DER Device management system controls the
DER Device (s) according to the DER Device schedule. The
customer’s Customer Building Automation System receives the RTP
signals from the Energy Service Provider and performs
optimizations on the best mix of load reductions and DER Device
function based on the customer’s criteria. At the beginning of
each interval, the Customer Building Automation System sends the
appropriate commands to the DER Device Manager to initiate the DER
Device functions for that interval. The DER Device Manger
processes those commands, initiates the DER Device utilization and
monitors the DER Device (s) for compliance with commands. Any
failure to produce the scheduled DER Device results in an alarm
broadcasted to the Customer Building Automation System where the
customer can take appropriate action. The monitored DER Device
activity is made available in real-time to the Customer Building
Automation System where the data can be made available to the
customer and Energy Service Provider.

In addition to RTP responses, the Customer
Building Automation System may bid into the energy and ancillary
services markets if all business constraints are first met. If these
bids are accepted, additional commands may be set to the DER Device
management system to implement those bids. The Customer Building
Automation System will monitor the response to insure the bid services
are supplied.

The Energy Service Provider is responsible for
monitoring DER Device facilities while operating to ensure power
quality constraints are met, and to help manage emergency situations
(detailed in the Advanced Distribution Automation Use Cases).

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Timer for beginning of interval |  | Customer Building Automation System sends signals to DER Device manager for the upcoming interval. These commands would include generation and ancillary services support. | Customer Building Automation System | DER Device manager | DER Device schedule | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.2 | DER Device receives schedule for interval |  | DER Device implements schedule starting or stopping generation and switching loads. |  | DER Device devices | DER Device Device Start/Stop/Set Commands | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1..3 | DER Device implements generation |  | Monitors DER Device performance and reports status to Customer Building Automation System | DER Device manager | Customer Building Automation System | DER Device Status | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.4 | DER Device performance data published |  | Makes DER Device performance data available to Energy Service Provider | Customer Building Automation System | Energy Service Provider DER Device and Ancillary Services Monitoring | DER Device Status | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.5 | Failure to meet DER Device goals |  | If DER Device goals are not met, the Customer Building Automation System will signal the customer with an alarm so that action can be taken. | Customer Building Automation System | Customer | DER Device Status | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
