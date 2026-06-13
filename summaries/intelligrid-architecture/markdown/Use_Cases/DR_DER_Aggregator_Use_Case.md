# DER Aggregator

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DR_DER_Aggregator_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Distributed Energy Resources (DER) - DER Aggregator Function

## Contents

* [Narrative](DR_DER_Aggregator_Use_Case.htm#Narrative)
* [Steps](DR_DER_Aggregator_Use_Case.htm#Steps)

## Narrative

The purpose of the distributed generation
aggregator activity is to enable a mechanism whereby a system operator
can call on customers during peak periods of energy usage and who have
backup generators to disconnect from the power grid and power
themselves with their generators.

In areas with high energy costs such as New York
City, load curtailment programs have been initiated where facilities
can make use of on-site generators that provide back-up power and use
them to supply peaking, reserve or load management capability.  In
many instances, the size of the generators are in the 1 MW or so range
and to make economic sense, it is necessary to aggregate multiple
units together into one virtual power plant that can be dispatched as
would a normal power plant by system aggregators.  The system
aggregator is responsible for the collection and aggregation of DG
units.  They generally have a contract to split revenues with the
owners of the DG units.  The system aggregator is the point of
interface to the system operator.  The system aggregator also
maintains a control room and responds to calls and inquiries from the
system operator before, during and after generation.  The system
aggregator generally owns and maintains all communication channels to
the DG units as well as all of the monitoring equipment used for
performance verification.  The system aggregator is responsible for
calculating settlement and verification with the system operator and
distributing payments to the DG unit owners.  The DG owners maintain
the DG units and usually are responsible for starting and stopping the
units.

A typical scenario would be as follows.  It is
August in NYC and the temperature has hit the high 90s for the third
straight day.  As the system peak continues to rise, the NYISO
forecasts that there could be an energy shortage the following day. 
In response, the NYISO asks approved system aggregators if they could
shed load.  In particular, the NYISO asks system aggregator #1 if it
could supply 5 MW.  The system aggregator then contacts its customers
that are under contract if they could run their generators the
following day.  The system aggregator then totals the amount of
expected load that is expected to be relieved from the grid the
following day and submits that to the ISO.  The system aggregator will
try to obtain enough willing customers so that they can reach the 5 MW
goal for the day.  When the next day arrives, the system aggregator
then follows up with each customer to remind them to disconnect from
the power grid and to start their generators.  The system aggregator
and/or system operator monitors over the Internet the output from each
generator and totals them to ensure compliance with the 5 MW load.  It
is important to get near what is asked for maximum revenue can be
obtained and to avoid penalties.  If a generator fails to start, the
system aggregator attempts to get another customer to start their
generator.  At the end of the day, the generators are stopped and data
is collected that is used to verify compliance and to calculate bills
that go to the ISO.  The system aggregator submits the bills to the
ISO and once payment is received, the corresponding revenue is sent to
the DG unit owners.

if !vml?![](DR_DER_Aggregator_Use_Case_files/image002.gif)endif?

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | System Operator  Initiates Curtailment | System Aggregator  Notification | During a heat wave, the system operator forecasts that a possible energy shortage may exist the following day and therefore contacts approved System Aggregator s and asks them if they can provide a set number of MWs the following day | System Operator | System Aggregator | Generation Requests | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
| 1.2 | System Aggregator  Polls DG Unit Owners | DG Unit Owner Pre-Notification | System Aggregator  contacts individual customers requesting that they separate from the grid and run off their generators | System Aggregator | DER Owner | Generation Requests | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.3 | Generation Start Time | DG Unit Owner On Notification | System Aggregator  contacts customers at the start time to make sure customer complies with request | System Aggregator | DER Owner | Generator Status | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.4 | Monitoring | DG Unit Monitoring | System Aggregator  monitors in real-time the generator output to verify goal is being met | Monitoring Device | Central Database | Energy Data | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.5 | Generation End Time | DG Unit Owner Off Notification | System Aggregator  contacts customers at the end time to make sure customer shuts down generators | System Aggregator | DER Owner | Generator Status | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.6 | Settlement | Settlement | System Aggregator  generates settlement reports from the data and submits to the system operator | Central Database | System Operator | Settlement Data | [Control Centers to ESPs](../Environments/Env9_Control_Centers_to_ESPs.htm) |
