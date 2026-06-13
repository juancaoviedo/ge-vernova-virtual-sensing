# Cust Port Net Metering

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Net_Metering_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Consumer Portal - Net Metering with DER Function

## Contents

* [Narrative](CS_Consumer_Portal_Net_Metering_Use_Case.htm#Narrative)
* [Steps](CS_Consumer_Portal_Net_Metering_Use_Case.htm#Steps)
* [Additional Information](CS_Consumer_Portal_Net_Metering_Use_Case.htm#Additional Information)

## Narrative

### Overview

A utility company wants to effectively use the DER System Controllers
(DER) installed in customer sites to reduce its contract power
purchase during peak load periods. These customers have signed up for
net-metering and agreed to meet specified Power Quality (PQ) criteria.
The utility would use its internal demand projection models and
communications with the DER, along with guaranteed buy-back of power
agreements, to implement economic peak rate power purchase under its
contract power purchase agreements.

### Description

A western
utility has a residential customer base of 1 million meters. The
meters are installed in single-family detached housing (SFD),
single-family attached housing (SFA), apartment buildings, and mobile
homes. The utility wishes to promote the use of renewable resources
within its residential and light commercial client base.

The utility
decides to provide incentives for the residential and light commercial
use of DER System Controllers (DER) by offering a guaranteed buy-back
of power under specific conditions. The plan requires the customers to
install DER with their own resources and the utility will purchase
power delivered to the grid (specified in DER regulations) during
periods of high demand.

A specific
subset (100 total) of the customers participating in the DER program
resides on a congested T & D feeder in a specific geographic area of
the service territory. Thus it’s advantageous for the utility to
“involve” these customers during times of peak demand or high purchase
power contractual periods.

The issues
confronting the utility during seasonal high demand periods are:

·       
They need to know which
homes of the 100 have DER installed, the size of the DER (kW) and the
type of DER (solar PV, generator, etc).

·       
They need to know which
customers have signed net-metering contracts.

The utility
enters into a typical high demand period; ambient temperatures are
rising and HVAC loads are increasing. The utility desires to call up
DER. and goes through the following procedures:

1. The utility interrogates
   primary line meters on the T & D feeder and starts to
   continuously monitor line loading. The utility has developed
   a model to assess the primary Meter Device load ramp and can
   predict when the feeder will become overloaded at the
   monitored rate-of-change. The model predicts that at the
   present rate of change the line will become critical within
   one hour.
2. Based on this fact, the
   utility calls up an internal database for that specific
   geographic area and determines which customers have DER and
   how much power (kW) they have. Based on the database
   results, the utility interrogates the customer portals to
   assess which units are already on line and which ones are
   available to be called up (available units must provide an
   “availability” signal as part of their contract with the
   utility).
3. The utility notifies the
   customers that specific DER units will be called up within
   30 minutes. The DER is brought on line at a specific time
   and the contractual buy-back rate goes into effect (the rate
   is guaranteed at 90% of purchase power at that time period,
   with the 10% differential going into system O & M). Thus the
   utility is now buying DER power at 90% of a purchase power
   rate that is determined by calling up the utility’s purchase
   power contracts interactive spot-power database.
4. The utility Power Quality
   group examines each customer’s DER to insure that the output
   is within the contractual standards for Power Quality. Units
   not complying are dropped from the line within 500
   milliseconds and a notation is made as to why the unit(s)
   was dropped.
5. The remaining customers’
   net-meters are now supplying the utility enterprise with
   delivered power for a prescribed time that must be credited
   to the customers’ accounts and eventually show up on their
   monthly invoice as a credit.
6. The utility determines that
   the peak demand problem has been averted and does not elect
   to purchase expensive power under contract.
7. The billing department now
   calculates the amount of money to reimburse each DER
   participating customer based on agreed upon rates [see Step
   3 above] and for the measured time period.
8. The Power Quality
   department notifies the DER customers that failed PQ
   monitoring, the reason why and requests repairs to permit
   continued participation in the net-metering/DER program.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | T & D Feeder Line Meter Device Query | Check feeder overload projection | DER system receives ambient temperature, demand data and HVAC load data | Utility T & D data | DER System Controller | Ambient temperature and load data exceeding specified threshold values | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.2 |  | DER system queries | DER system queries utility’s load prediction model | DER System Controller | Load Prediction Model | System data for use by the model | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.3 |  | Identifies feeder line risk | Load prediction model identifies feeder line at risk of overload event | Load Prediction Model | DER System Controller | Information identifying feeder at risk | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.4 |  | Activation trigger for DER program activities | DER system generates trigger to activate DER program for the identified feeder line | DER System Controller | DER Database | Activation trigger for DER program activities | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2 | DER Activation Order | Find Amount and types of power that can be obtained from the customers participating in the DER program | DER system queries DER database to determine power capacity from customers in the affected segment | DER System Controller , T & D system, DER Database | DER System Controller | Amount and types of power that can be obtained from the customers participating in the DER program | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.1.1 |  | Actual available power from the targeted DER customers | DER system signals identified customers to determine availability | DER System Controller , Customer Communication Portal, DER System Controller | DER System Controller | Actual available power from the targeted customers | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.1.2 | DER systems signals to check for availability | Activation alert to customers on pending program activation | DER system alerts customers with available power on system activation in 30 minutes | DER System Controller | Customer Communication Portal, DER System Controller | Activation alert to customers on pending program activation | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.2 |  | Signal to turn on DER equipment at available customer sites | DER system turns on DER equipment at targeted customers’ sites | DER System Controller | Customer Communication Portal, DER System Controller | Signal to turn on DER equipment at available customer sites | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.3 |  | Activate PQ monitoring system | Activates PQ monitoring of delivered power | PQ Monitoring System | DER System Controller | PQ data on delivered power | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.3.1 | DER equipment failing | Turn-off DER equipment | Turn off DER equipment failing PQ criteria | DER System Controller | DER System Controller , Customer Communication Portal | Signal to failing units to turn off | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.3.1.1 |  | Flag PQ failing DER | Flag failing units for follow-up remedial actions | DER System Controller | DER Database | List of DER System Controller units failing PQ criteria | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.4 |  | Record energy delivered to the grid | Alert Customer Communication Portal at conforming DER customers to record power delivery | DER System Controller | Customer Communication Portal, Customer Net-Metering Device -Meter Device | Information on amount of power and duration of power delivered to the grid | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.5 |  | Delay buying power on spot-market | Signal Purchasing Selling Entity to delay spot-market power purchase | DER System Controller | Purchasing Selling Entity | Delay buying decision for power purchase on spot-market | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.6 |  | Determine contract power buy-back rate | 2.6 Query utility’s spot-market power database to determine contract power rate | Purchase Power Contracts Interactive Spot-Power Database - | DER System Controller , DER Database, Customer Billing System | Power buy-back rate applicable to power from DER System Controller to utility grid | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.7 |  | On-going tracking feeder overload | On-going tracking feeder overload condition and load prediction model | Load Prediction Model , T & D | DER System Controller | Status data indicating the need for DER power from customers | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.1 | Monitor T&D data | Predict if DER program and DRP can be terminated | Load Prediction Model and T &D data indicate DER activation can be terminated | Load Prediction Model , T & D | DER System Controller | Trigger to initiate DER event termination | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2 | DER program and DRP can be terminated | DER System Controller initiates termination sequencing | DER System Controller initiates orderly sequencing DER program termination | DER System Controller , DER Database | Customer Communication Portal, DER System Controller | Message to DER System Controller unit on shutdown schedule | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2.1 |  | Transmit DER turn-off signal | Transmit DER turn-off signal to each customer as per the schedule | DER System Controller | Customer Communication Portal, DER System Controller | Signal to individual DER unit to terminate power delivery | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2.2 | Transmit DER turn-off signal | Confirmation of power delivery turn-off | Confirmation by customer unit of power delivery termination | Customer Communication Portal, DER System Controller | DER System Controller | Positive acknowledgment of system turn-off | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3 |  | Power delivered during DER event | Customer site transmits net power delivery during DER event | Customer Communication Portal, Customer Net-Metering Device -Meter Device | DER Database | Details of amount of power delivered, duration of power delivered during the DER event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3.1 |  | Generate power delivery and rate information | Delivered power information and applicable rate data sent to billing system | DER System Controller , DER Database | Customer Billing System | Amount and details of credit to be issued to customer for power delivered during the DER event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3.2 |  | Amount of power purchase avoided due to DER program | Delivered power by customer DER units and peak load averted data to Purchasing Selling Entity | DER Database | Purchasing Selling Entity | Amount of power purchase avoided due to DER program activation | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3.3 |  | Signal no additional DER power to be purchased | Signal Purchasing Selling Entity that no additional power needs to be purchased | DER System Controller | Purchasing Selling Entity | Finalize decision not to purchase power in spot-power market | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4 |  | Retrieve list of failed DER units | Retrieve list of customer DER units that failed PQ criteria | DER Database | DER System Controller | List of customers requiring follow-up actions | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4.1 | DER units failed PQ criteria | Alert customer on PQ failure | Alert these customers on PQ failure details | DER Database | Customer Communication Portal | Details of PQ failure during DER event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4.2 | DER units failed PQ criteria fixed | Request PQ capability compliance confirmation | Request these customers to alert DER System Controller on bringing their system into compliance | DER Database | Customer Communication Portal | Alert affected customers on need for remedial actions | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4.3 |  | Flag affected customer sites | Flag the affected customer sites for future event till compliance confirmation is received | DER System Controller | DER Database | Flag the affected customers to indicate compliance confirmation is needed before they can be considered for program participation during future DER events | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |

## Additional Information

### Actor (Stakeholder) Roles

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Customer Site*** | | ***Those entities that are located at customer’s premises*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Customer | Person | One signed up to participate in the DER System Controller (DER) program. |
| Customer Communication Portal | System | System handling communications function at customer’s premises [in this case, communications with the installed DER, net-Meter Device , power quality system and the utility’s DER operations] |
| Net-Metering Device -Meter Device | Device | Device that can measure and transmit the net flow of power to the customer [i.e., it measures power flow in both directions – into the customer premises from the utility and out to the utility from customer premises – and generates a net Meter Device data that can be used by the utility to bill the customer accordingly] |
| DER System Controller | System | System at the customer site that generates power and is set up to be brought online at the demand of the utility company |
| Remote Meter Device | System | System for transmitting Meter Device data on demand to the utility. |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Power Company DER System Controller Operations*** | | ***Those entities that are charged with managing the DER System Controller functions for the power company to optimize the loading of the Transmission & Distribution grid*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| DER System Controller | System | DER System Controller Center: System at the power company that handles DER operations [such as the system load model, decisions on when to initiate DER activities, triggering communications with other utility departments and the DER program participants, etc] |
| Line Meter Device | Device | Device that measures loading of feeder line in specific T & D grid sectors of the utility |
| Transmission & Distribution Feeder | System | System that handles the T & D function to specific geographic sector in utility’s service area. |
| DER Database | System | System that contains information about customers participating in the DER program, their location, details of their system (such as DER installed, the size of the DER (kW) and the type of DER (solar PV, generator, etc)), whether they have signed net-metering contract, and so on. |
| Customer Billing System | System | System that handles generation of bills for the services provided to the customer |
| PQ Monitoring System | System | Power Quality Monitoring System: System that monitors the operation and the power quality of the power generated by customer’s DER to qualify it for transmission on to utility’s grid |
| Purchase Power Contracts Interactive Spot-Power Database | System | System used by the utility to track and determine the spot price of power that it can purchase under its existing contracts |
| Load Prediction Model | System | System that a models feeder load by automatically tracking weather, load and other conditions to project overload events at specific feeder lines and connected to the DER database |
| Utility Communications Network | System | System responsible for managing communications between the utility and the participants in the DER program [for functions such as remote Meter Device reading, controlling DER units at customer sites, monitoring net-meters and other related communications activities] |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Others*** | | ***Those entities that are involved in this activity, but do not fit in any of the Groupings above*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Metering | Person | Department at the utility that manages meters and their installation at the customer site |
| Purchasing Selling Entity | Person | Department at the utility company that handles procurement of power resources for the utility company. |
| T & D | System | Transmission & Distribution (T & D) Grid : System at the utility company that manages the Transmission and Distribution grid for the utility company and monitors for loading factors, etc. |
| Utility Communications Network | System | System responsible for managing communications between the utility and the participants in the DER program [for functions such as remote Meter Device reading, controlling DER units at customer sites, monitoring net-meters and other related communications activities]. |
| Energy Service Provider |  |  |

 

### Information exchanged

 

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| T & D Feeder Line Meter Device Query | Query from utility’s DER Center to T & D feeder line Meter Device to determine the potential for line overload and generating the trigger to activate the DER program in the affected segment |
| DER Activation Order | System order to initiate DER ahead of projected line overload, communications to the participating customers to alert the onset of DER, verifying DER availability at each customer site, bringing online selected DER at customer sites, monitoring the PQ at each site, alerting the Customer Communication Portal and net-Meter Device at each site to record delivered power and flagging the power delivered for appropriate payment by the billing system |
| DER Order Termination | System order to terminate the DER at the customer site based on model projection of averting peak demand problem, crediting each customer for power delivered as per applicable rates, decision on not purchasing power under contract from other sources and alerting customers whose DER failed to meet applicable PQ criteria |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Determine Potential Feeder Peak Load Problem | Based on ambient temperatures and HVAC loads crossing the threshold values, trigger a query to utility feeder load model to determine if a specific feeder line will face overload problem; if the model predicts potential overload problem, trigger activation of DER activities for that sector |
| Initiate DER Program Activation | Initiate actions to activate DER program activities for the targeted feeder line: query DER database to flag DER customers in the affected segment, identify amount of power (kW) available from registered DER from customers in that segment, generate a query to those customers to determine their DER system availability and generate an alert to those with available DER system to indicate potential program activation within 30 minutes |
| Implement DER | Activate DER systems at customers already alerted and with available systems, alert the Customer Communication Portal and net-meters at those locations to record power delivered and duration of power delivery, activate PQ monitoring of delivered power to verify compliance with system requirements, drop non-complying units from the grid and flag for notice after the event, track feeder load to determine timing for program termination and hold-off contract power purchase on spot market during the DER program period |
| Terminate DER | On indication by the power model of the end of the projected overload problem for the feeder line, send out a trigger to customer DER systems supplying power to terminate operation, record power supplied and duration of power supply, finalize decision not to buy power under spot-market purchase contract and revert system back to monitoring mode for next overload situation |
| Complete Post-DER Activities | Initiate actions to transmit net-metering data to billing to generate credit to customers for the power supplied at the contractual buy-back rate, generate an alert to customers whose DER systems failed to meet prescribed PQ criteria and notify all customers in the DER program that the current DER event has been successfully terminated |

### Contracts/Regulations

| ***Contract/Regulation*** | ***Impact of Contract/Regulation on Function*** |
| --- | --- |
| DER Program Tariffs | Specifications of DER equipment installed at customer site, net-metering equipment at customer site, contractual buy-back rates, PQ acceptance criteria and power supply credits applied to customer bill |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ***Policy*** | ***From Actor*** | ***May*** | ***Shall Not*** | ***Shall*** | ***Description (verb)*** | ***To Actor*** |
| Install DER Equipment | Customer |  |  | X | Customer needs to install DER system at site to participate in the program | Energy Service Provider |
| Install Net-Metering Device -Meter | Energy Service Provider |  |  | X | Install specified net-metering equipment at customer site | Customer |
| Activate DER | Energy Service Provider | X |  |  | Activate and bring online customer’s DER | Customer |
| Meet PQ Criteria | Customer |  |  | X | Customer shall maintain the DER system in a manner that will ensure that the DER meets specified PQ criteria for power delivery | Energy Service Provider |
| Buy-back Power During DER Event | Energy Service Provider |  |  | X | Utility shall buy-back power at contract rates from customer’s DER during a DER event if the customer’s delivered power meets PQ criteria | Customer |

 

|  |  |  |  |
| --- | --- | --- | --- |
| ***Constraint*** | ***Type*** | ***Description*** | ***Applies to*** |
| Program Participation | System Availability | A customer can participate in a given DER event only if the DER system is in “available” state | Selecting customer for DER participation |
| Power Delivery | PQ | Customer’s DER unit to meet specified PQ criteria to be permitted to deliver power to the utility | Acceptance of power from customer’s DER and eligibility to continue participation in the program |
| Power Buy-back | Buy-back Rate | On DER program activation and customer DER meeting availability and PQ criteria, the utility is obligated to buy-back power at 90% purchased power rate at that time | Rate paid by the utility to customer for power delivered to the grid |

#
