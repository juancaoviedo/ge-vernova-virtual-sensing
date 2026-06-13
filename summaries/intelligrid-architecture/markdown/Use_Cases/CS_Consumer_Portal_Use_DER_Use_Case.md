# Cust Port Use DER

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Use_DER_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Consumer Portal - Use Customer DER Function

## Contents

* [Narrative](CS_Consumer_Portal_Use_DER_Use_Case.htm#Narrative)
* [Steps](CS_Consumer_Portal_Use_DER_Use_Case.htm#Steps)
* [Additional Information](CS_Consumer_Portal_Use_DER_Use_Case.htm#Additional Information)

## Narrative

### Overview

A utility company wants to effectively use the DER System Controllers
(DER) installed in customer sites to reduce its contract power
purchase during peak load periods. These customers have signed up for
net-metering and there are other customers who have signed up for load
curtailment during peak demand periods in return for rebates. The
utility would use its internal demand projection models and
communications with the DER, along with guaranteed buy-back of power
agreements and curtailment of major loads during peak periods, to
implement economic peak rate power purchase under its contract power
purchase agreements.

### Description

A western
utility has a residential customer base of 1 million meters. The
meters are installed in single-family detached housing (SFD),
single-family attached housing (SFA), apartment buildings, and mobile
homes. The utility wishes to promote the use of renewable resources
within its residential and light commercial client base.

The utility has
demand relief requirements and has multiple demand response programs
in place. It additionally supports active residential conservation
programs as well as residential alternate, renewable, and distributed
generation.

The results of
all of these efforts are reported to the Public Utility Commission as
part of their requirements to receive credit in rate base.

The utility
decides to provide incentives for the residential and light commercial
use of DER System Controllers (DER) by offering a guaranteed buy-back
of power under specific conditions. The plan requires the customers to
install DER with their own resources and the utility will purchase
power delivered to the grid (specified in DER regulations) during
periods of high demand.

Additionally the
utility offers demand responsive programs wherein customers receive
financial incentives for curtailing HVAC, pool pumps, and electric
water heaters during peak demand periods.

A specific
subset (100 total) of the customers participating in these programs
resides on a congested Transmission Service Provider feeder in a
specific geographic area of the service territory. Thus it’s
advantageous for the utility to “involve” these customers during times
of peak demand or high purchase power contractual periods.

The issues
confronting the utility during seasonal high demand periods are:

Ø     
They need to know which
homes of the 100 have DER installed, the size of the DER (kW) and the
type of DER (solar PV, generator, etc.

Ø     
They need to know which
customers have signed net-metering contracts, and which customers
participate in incentivized load control programs.

Ø     
They need to have
access to purchase power contract pricing information

The utility
enters into a typical high demand period; ambient temperatures are
rising and HVAC loads are increasing. The utility has orchestrated a
“smart system” approach and goes through the following procedures.

1.     
The utility
interrogates primary line meters on the Transmission Service Provider
feeder and starts to continuously monitor line loading. The utility
has developed a model to assess the primary Meter Device load ramp and
can predict when the feeder will become overloaded at the monitored
rate-of-change. The model predicts that at the present rate of change
the line will become critical within one hour.

2.     
Based on this fact, the
utility calls up an internal database for that specific geographic
area and determines which customers have DER and how much they have
(kW). Based on the database results the utility interrogates the
customer portals to assess which units are already on line and which
ones are available to be called up (available units must provide an
“availability” signal as part of their contract with the utility).

3.     
The utility notifies
the customers that specific DER units will be called up within 30
minutes. The DER is called on line at a specific time and the
contractual buy-back rate goes into effect (the rate is guaranteed at
90% of purchase power at that time period, with the 10% differential
going into system O&M). Thus the utility is now buying DER power at
90% of a purchase power rate that is determined by calling up the
utility’s purchase power contracts interactive spot-power database.

4.     
The customers
net-meters are now supplying the utility enterprise with delivered
power for a prescribed time that must be credited to the customer’s
account and eventually show up on their monthly invoice as a credit.

5.     
The utility continues
to monitor the primary meters and determines that the acquired DER has
slowed the rate of change, but the system will still overload during
the peak demand period. Thus it decides to curtail customers
participating in ongoing demand reduction programs.

6.     
The utility
interrogates the specific customers on the feeder and determines which
customers have controllable loads that are in service. The utility
sends out a signal that advises of an upcoming curtailment and then
reads the primary Meter Device just before the curtailment signal is
sent, and 15 minutes after the curtailment signal is sent.

7.     
The utility determines
that the peak demand problem has been averted and does not elect to
purchase expensive power under contract.

8.     
The billing department
now calculates the amount of money to reimburse each DER participating
customer based on agreed upon rates and for the measured time period.

9.     
The billing department
calculates the amount of incentives to pay each of the participating
DSM customers. Free-riders are subtracted from the customers to be
rewarded as are those that overrode the event (an option of the
program.)

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Transmission Service Provider Feeder Line Meter Device Query | Demand data and HVAC load data | DER system receives ambient temperature, demand data and HVAC load data | Utility Transmission Service Provider data | DER System Controller | Ambient temperature and load data exceeding specified threshold values | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.2 |  | Check feeder overload projection | DER system queries utility’s load prediction model | DER System Controller | Load Prediction Model | System data for use by the model | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.3 |  | Identifies line at risk of overload | Load prediction model identifies feeder line at risk of overload event | Load Prediction Model | DER System Controller | Information identifying feeder at risk | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 1.4 | Identifies feeder line at risk of overload | Activates DER program for identified feeder line | DER system generates trigger to activate DER program for the identified feeder line | DER System Controller | DER Database | Activation trigger for DER program activities | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.1 | DER and Demand Reduction Program Database Activation Order | DER system determines DER capacity | DER system queries DER database to determine power capacity from customers in the affected segment | DER System Controller , Transmission Service Provider system, DER Database | DER System Controller | Amount and types of power that can be obtained from the customers participating in the DER program | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.1.1 |  | Actual available power from the targeted customers | DER system signals identified customers to determine availability | DER System Controller , Customer Communication Portal, DER System Controller | DER System Controller | Actual available power from the targeted customers | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.1.2 | DER systems signals to check for availability | Activation alert to customers on pending program activation | DER system alerts customers with available power on system activation in 30 minutes | DER System Controller | Customer Communication Portal, DER System Controller | Activation alert to customers on pending program activation | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.2 |  | Signal to turn on DER equipment at available customer sites | DER system turns on DER equipment at targeted customers’ sites | DER System Controller | Customer Communication Portal, DER System Controller | Signal to turn on DER equipment at available customer sites | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.3 |  | Record energy delivered to the grid | Alert Customer Communication Portal at conforming DER customers to record power delivery | DER System Controller | Customer Communication Portal, Customer Net-Metering Device -Meter Device | Information on amount of power and duration of power delivered to the grid | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.4 |  | Delay buying power on spot-market | Signal Purchasing Selling Entity to delay spot-market power purchase | DER System Controller | Purchasing Selling Entity | Delay buying decision for power purchase on spot-market | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.5 |  | Determine contract power buy-back rate | Query utility’s spot-market power database to determine contract power rate | Purchase Power Contracts Interactive Spot-Power Spot Price Database - | DER System Controller , DER Database, Customer Billing System | Power buy-back rate applicable to power from customer DER to utility grid | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.6 |  | On-going tracking feeder overload | On-going tracking feeder overload condition and load prediction model | Load Prediction Model and Transmission Service Provider Grid | DER System Controller | Status data indicating the need for DER power from customers | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.7 |  | Identify Demand Reduction Program Database participating customers | Generate query to Demand Reduction Program Database Database to identify participating customers in the affected grid line | Demand Reduction Program Database | DER System Controller | List of customers participating in the Demand Reduction Program Database load curtailment program | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.7.1 |  | Trigger Demand Reduction Program Database load curtailment alert | Trigger Demand Reduction Program Database load curtailment alert signal to participating Demand Reduction Program Database customers | Demand Reduction Program Database | Customer Communication Portal and DLC Switch Controller | Signal alerting identified customers of load curtailment | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.7.2 | Trigger Demand Reduction Program Database load curtailment alert | Monitor load curtailment | Monitor load curtailment in progress [to ensure customer has not chosen to override the curtailment] | Demand Reduction Program Database | Customer Communication Portal, DLC Switch Controller and Meter Device | Verify load curtailment for the duration of the event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 2.7.3 |  | Record of curtailment at details at customer site | Alert Customer Communication Portal to record duration and details of load curtailed | Customer Communication Portal | Meter Device and DLC Switch Controller | Record of curtailment at details at customer site | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.1 | Monitor T&D data | Predict if DER program and Demand Reduction Program Database can be terminated | Load Prediction Model and T &D data indicate DER and Demand Reduction Program Database activation can be terminated | Load Prediction Model and Transmission Service Provider Grid | DER System Controller | Trigger to initiate DER event termination | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2 | DER program and Demand Reduction Program Database can be terminated | DER System Controller initiates termination sequencing | DER System Controller initiates orderly sequencing DER program and Demand Reduction Program Database event termination | DER System Controller , DER Database | Customer Communication Portal, DER System Controller | Message to customer DER unit on shutdown schedule | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2.1 |  | Transmit DER turn-off signal | Transmit DER turn-off signal to each customer as per the schedule | DER System Controller | Customer Communication Portal, DER System Controller | Signal to individual DER unit to terminate power delivery | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2.1.1 | Transmit DER turn-off signal | Confirmation of power delivery turn-off | Confirmation by customer unit of power delivery termination | Customer Communication Portal, DER System Controller | DER System Controller | Positive acknowledgment of system turn-off | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2.2 | Transmit Demand Reduction Program Database Order Termination | Transmit signal to turn on curtailed loads | Transmit signal to turn on curtailed loads to participating customers | Demand Reduction Program Database | Customer Communication Portal, DLC Switch Controller | Signal to terminate load curtailment activity | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.2.2.1 | Transmit signal to turn on curtailed loads | Confirmation of load curtailment | Confirmation of customer of terminating load curtailment | Customer Communication Portal | DER System Controller | Positive acknowledgment of Demand Reduction Program Database event termination | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3 |  | Power delivered during DER event | Customer site transmits net power delivery during DER event | Customer Communication Portal, Customer Net-Metering Device -Meter Device | DER Database | Details of amount of power delivered, duration of power delivered during the DER event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3.1 |  | Generate power delivery and rate information | Delivered power information and applicable rate data sent to billing system | DER System Controller , DER Database | Customer Billing System | Amount and details of credit to be issued to customer for power delivered during the DER event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.3.1.1 |  | Amount of power purchase avoided due to DER program | Delivered power by customer DER units and peak load averted data to Purchasing Selling Entity | DER Database | Purchasing Selling Entity | Amount of power purchase avoided due to DER program activation | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4 | Demand Reduction Program Database Event | Customer site transmits Demand Reduction Program Database event data | Customer site transmits curtailed load data during the Demand Reduction Program Database event | Customer Communication Portal, Meter Device | Demand Reduction Program Database | Details of loads curtailed, duration of curtailment, and amount of power consumption saved | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4.1 |  | Customer site transmits Demand Reduction Program Database event data for billing | Curtailed load and duration information to billing system | Demand Reduction Program Database | Customer Billing System | Amount of credits to be applied to customer for load curtailed during the Demand Reduction Program Database event | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4.1.1 |  | Amount of power purchase avoided due to Demand Reduction Program Database activation | Peak load demand averted data to Purchasing Selling Entity | Demand Reduction Program Database | Purchasing Selling Entity | Amount of power purchase avoided due to Demand Reduction Program Database activation | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.4.2 |  | Signal no additional DER power to be purchased | Signal Purchasing Selling Entity that no additional power needs to be purchased | DER System Controller | Purchasing Selling Entity | Finalize decision not to purchase power in spot-power market | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |
| 3.5 | DER and Demand Reduction Program Database event | Get credit for DER and Demand Reduction Program Database from Public Utility Commission | Submit total load averted [from DER program and Demand Reduction Program Database activities] to Public Utility Commission for awarding rate credits | DER System Controller , Demand Reduction Program Database | Public Utility Commission | Details of power load averted due to the DER Program and DER activities | [DER Monitoring and Control](../Environments/Env15_DER_Monitoring_and_Control.htm) |

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
| Meter Device | System | System for transmitting Meter Device data on demand to the utility. |
| DLC Switch Controller | Device | Device performing cycling of major load, such as the air conditioning unit, pool pump heater, etc |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Load Serving Entity DER System Controller Operations*** | | ***Those entities that are charged with managing the DER System Controller functions for the power company to optimize the loading of the Transmission & Distribution grid*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| DER System Controller | System | DER System Controller Center: System at the power company that handles DER operations [such as the system load model, decisions on when to initiate DER activities, triggering communications with other utility departments and the DER program participants, etc] |
| Line Meter Device | Device | Device that measures loading of feeder line in specific Transmission Service Provider grid sectors of the utility |
| Transmission & Distribution Feeder | System | System that handles the Transmission Service Provider function to specific geographic sector in utility’s service area. |
| DER Database | System | System that contains information about customers participating in the DER program, their location, details of their system (such as DER installed, the size of the DER (kW) and the type of DER (solar PV, generator, etc)), whether they have signed net-metering contract, and so on. |
| Customer Billing System | System | System that handles generation of bills for the services provided to the customer |
| Customer Id | Device | A common customer identification key that is used by service providers authorized by the customer to identify all of their service accounts |
| Customer Information Database | System | System that contains information about customer accounts of the power company |
| Demand Reduction Program Database | System | Demand Reduction Program [Demand Reduction Program Database] Database: System that contains information about all of the Demand Reduction Programs offered by the utility, participation requirements, equipment details and links to customer billing system for passing incentive information |
| Demand Response Program Manager | Person | Person managing the Demand Reduction Program Database at the utility |
| Purchase Power Contracts Interactive Spot-Power Spot Price Database | System | System used by the utility to track and determine the spot price of power that it can purchase under its existing contracts |
| Load Prediction Model | System | System that a models feeder load by automatically tracking weather, load and other conditions to project overload events at specific feeder lines and connected to the DER database |
| Utility Communications Network | System | System responsible for managing communications between the utility and the participants in the DER program [for functions such as remote Meter Device reading, controlling DER units at customer sites, monitoring net-meters and other related communications activities] |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Others*** | | ***Those entities that are involved in this activity, but do not fit in any of the Groupings above*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Metering | Person | Department at the utility that manages meters and their installation at the customer site |
| Purchasing Selling Entity | Person | Department at the utility company that handles procurement of power resources for the utility company. |
| Public Utility Commission | Person | State Public Utility Commission {PUC):  The entity that receives results of the utility’s demand reduction program. |
| Transmission Service Provider | System | Transmission & Distribution (Transmission Service Provider) Grid : System at the utility company that manages the Transmission and Distribution grid for the utility company and monitors for loading factors, etc. |
| Utility Communications Network | System | System responsible for managing communications between the utility and the participants in the DER program [for functions such as remote Meter Device reading, controlling DER units at customer sites, monitoring net-meters and other related communications activities]. |
| Energy Service Provider |  |  |
| Service Provider |  |  |
| Specified Loads |  |  |
| Meter Device |  |  |
| Meter Device |  |  |

 

### Information exchanged

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| Transmission Service Provider Feeder Line Meter Device Query | Query from utility’s DER Center to Transmission Service Provider feeder line Meter Device to determine the potential for line overload and generating the trigger to activate the DER program in the affected segment |
| DER Activation Order | System order to initiate DER ahead of projected line overload, communications to the participating customers to alert the onset of DER, verifying DER availability at each customer site, bringing online selected DER at customer sites, alerting the Customer Communication Portal and net-Meter Device at each site to record delivered power and flagging the power delivered for appropriate payment by the billing system |
| Demand Reduction Program Database Implementation | System order to alert customers on Demand Reduction Program Database to curtail participating loads, track curtailed loads and transmit curtailment information to the system for applying credits on termination of the curtailment order |
| DER Order Termination | System order to terminate the DER at the customer site based on model projection of averting peak demand problem, crediting each customer for power delivered as per applicable rates, and decision on not purchasing power under contract from other sources |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Determine Potential Feeder Peak Load Problem | Based on ambient temperatures and HVAC loads crossing the threshold values, trigger a query to utility feeder load model to determine if a specific feeder line will face overload problem; if the model predicts potential overload problem, trigger activation of DER activities for that sector |
| Initiate DER Program Activation | Initiate actions to activate DER program activities for the targeted feeder line: query DER database to flag DER customers in the affected segment, identify amount of power (kW) available from registered DER from customers in that segment, generate a query to those customers to determine their DER system availability and generate an alert to those with available DER system to indicate potential program activation within 30 minutes |
| Implement DER | Activate DER systems at customers already alerted and with available systems, alert the Customer Communication Portal and net-meters at those locations to record power delivered and duration of power delivery, activate PQ monitoring of delivered power to verify compliance with system requirements, drop non-complying units from the grid and flag for notice after the event, track feeder load to determine timing for program termination and hold-off contract power purchase on spot market during the DER program period |
| Implement Demand Reduction Program Database | On indication by the power model to initiate load shedding, contact customers participating in the Demand Reduction Program Database to alert them about load curtailment in 15 minutes, curtail specified loads, monitor the duration and load curtailed, and continue the curtailment till system requests termination of the Demand Reduction Program Database event |
| Terminate DER and Demand Reduction Program Database | On indication by the power model of the end of the projected overload problem for the feeder line, send out a trigger to customer DER systems supplying power to terminate operation, record power supplied and duration of power supply, send out trigger to Demand Reduction Program Database customers to turn on curtailed load, finalize decision not to buy power under spot-market purchase contract and revert system back to monitoring mode for next overload situation |
| Complete Post-DER and Demand Reduction Program Database Program Activities | Initiate actions to transmit net-metering data to billing to generate credit to customers for the power supplied at the contractual buy-back rate, transmit curtailed load and curtailment duration for participating Demand Reduction Program Database customers to the billing system for applying applicable incentive credits, and notify all customers in the DER program and Demand Reduction Program Database that the current DER and Demand Reduction Program Database event has been successfully terminated |

### Contracts/Regulations

| ***Contract/Regulation*** | ***Impact of Contract/Regulation on Function*** |
| --- | --- |
| DER Program Tariffs | Specifications of DER equipment installed at customer site, net-metering equipment at customer site, contractual buy-back rates, PQ acceptance criteria and power supply credits applied to customer bill |
| Demand Reduction Program Tariffs | Equipment installed at customer site, cycling regime implemented and incentive rewards applied to customer bill |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ***Policy*** | ***From Actor*** | ***May*** | ***Shall Not*** | ***Shall*** | ***Description (verb)*** | ***To Actor*** |
| Install DER Equipment | Customer |  |  | X | Customer needs to install DER system at site to participate in the program | Energy Service Provider |
| Install Net-Metering Device -Meter | Energy Service Provider |  |  | X | Install specified net-metering equipment at customer site | Customer |
| Activate DER | Energy Service Provider | X |  |  | Activate and bring online customer’s DER | Customer |
| Participate in Demand Reduction Program Database | Customer | X |  |  | Customer needs to agree to participate in the Demand Reduction Program Database and permit the utility to curtail specified loads during peak demand periods | Energy Service Provider |
| Buy-back Power During DER Event | Energy Service Provider |  |  | X | Utility shall buy-back power at contract rates from customer’s DER during a DER event if the customer’s delivered power meets PQ criteria | Customer |
| Cycle Energy to Equipment | Energy Service Provider | X |  |  | Cycle power to air conditioning unit on utility trigger | Specified Loads |
| Provide Load Control Equipment | Service Provider |  |  | X | Install specified equipment at customer site | Customer |
| Provide Incentive Rewards | Energy Service Provider |  |  | X | Provide incentive reward on customer energy bill | Customer |

 

|  |  |  |  |
| --- | --- | --- | --- |
| ***Constraint*** | ***Type*** | ***Description*** | ***Applies to*** |
| Program Participation | System Availability | A customer can participate in a given DER event only if the DER system is in “available” state | Selecting customer for DER participation |
| Load Curtailment | Turn Off Loads | Customer to permit specified major loads [such as HVAC, Pool Pump, etc] to be turned off by the utility | Customer’s eligibility for participation in the program to receive incentives |
| Reward Period | Inactive | Months of the year when the program is not active [i.e., non-summer months for this program] | No incentive reward provided |
| Energy Usage | Minimum Threshold | Tracked energy usage to meet or exceed program requirements to qualify to participate in the program and receive incentive reward on bill | Eligibility to continue participation in the program |
| Power Buy-back | Buy-back Rate | On DER program activation and customer DER meeting availability criteria, the utility is obligated to buy-back power at 90% purchased power rate at that time | Rate paid by the utility to customer for power delivered to the grid |

#
