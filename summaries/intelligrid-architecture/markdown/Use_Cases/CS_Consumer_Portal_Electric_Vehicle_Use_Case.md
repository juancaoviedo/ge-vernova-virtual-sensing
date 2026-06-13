# Cust Port Electric Car

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Electric_Vehicle_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Consumer Portal -

# Electric Vehicle Function

## Contents

* [Narrative](CS_Consumer_Portal_Electric_Vehicle_Use_Case.htm#Narrative)
* [Steps](CS_Consumer_Portal_Electric_Vehicle_Use_Case.htm#Steps)
* [Additional Information](CS_Consumer_Portal_Electric_Vehicle_Use_Case.htm#Additional Information)

## Narrative

### Overview

A utility
company wants to promote the increased use of electric vehicles in its
service area by offering significantly reduced electricity rates for
nighttime recharging of vehicle battery. Each EV is given a unique id
which is keyed to the customer so that the utility’s billing system
can bill the customer under the reduced EV charging rates. The system
also permits the customer to use the charging station at another
customer’s site [such as at a friend’s house] and have the system bill
the vehicle owner instead of the customer whose charging station is
used.

### Description

A western utility
has a residential customer base of 1 million meters. The meters are
installed in single-family detached housing (SFD), single-family
attached housing (SFA), apartment buildings, and mobile homes. The
utility wishes to promote the use of alternate fueled cars including
electric vehicles and fuel-cell powered vehicles.

The utility
decides to provide incentives for the residential use of electric
vehicles by offering greatly reduced kWh tariffs for nighttime
recharging. The issues confronting the utility are:

* They need to know which
  homes have electric vehicles by meter number and premise number.

The utility goes
through the following procedures.

1. 
The utility offers discounted electricity to recharge electric
vehicle batteries. To do this a customer must purchase the car and
charging station using their own resources and as an incentive the
utility offers greatly reduced nighttime charging rates/kWh. The
customer plugs in the car to the charger and requests “charge at
cheapest rates”. The utility is notified of the cars presence, its ID
number (which must correspond to the car registered with the
homeowner), and its approximate charge requirement (provided by the
car’s on board computer). The utility schedules the recharge to take
place during the evening hours and at different times than other EV
charging (thus putting diversity into the load).

2.   The billing department now calculates the amount of money to
charge the EV customer based on EV rates and for the measured time
period.

3. 
 The same EV customer drives to a friend’s home (who also has an
EV) and requests a quick charge to make sure that he can get back
home. When he plugs his EV into his friend’s EV charger, the utility
identifies the fact that the EV belongs to a different customer and
places the charging bill on the correct persons invoice, not on the
friend’s bill who offered his charging station.

4.  
The billing department now calculates the amount of money to
invoice the customer who owns the EV, based on EV rates and for the
measured time period.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Customer Request for EV Charging | Request for EV charging | Customer plugs in EV into charging station | EV On-Board System | EV Charging Station and Customer Communication Portal | Charging Request | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.1.1 |  | EV On-Board System Identifies the EV | EV On-Board System sends EV Id Number and charging requirements | EV On-Board System | Customer Communication Portal | EV Id, EV charge requirements | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.1.2 |  | Customer Communication Portal location and EV information | Customer Communication Portal at location sends EV information, Customer Id and Customer Communication Portal location information | Customer Communication Portal | EV Operation System | Customer information and EV/Customer Communication Portal location information | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.2 |  | Determine type of charging to implement | Power Company compares EV and location information to determine type of charging to implement | EV Operation System | EV Operation System | Identify if the vehicle is at customer or third-party location | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.1 | Charging request from customer home | Determine electric rate applicable | EV Operation System queries EV Operation System to determine electric rate applicable to request | Customer Id, EV Id Number | EV Operation System | EV power rates | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.1.1 |  | Confirms charging requirements | EV Operation System confirms charging requirements | EV Operation System | EV Operation System | EV charging requirements | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.2 |  | Assign charging time slot | EV Operation System queries EV Charging Scheduler to assign charging time slot | EV Charging Scheduler | EV Operation System |  | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.2.1 |  | Informs Customer Communication Portal on charging start time | EV Charging Scheduler informs Customer Communication Portal on charging start time | EV Charging Scheduler | Customer Communication Portal | Time slot allotment for EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.3 |  | Turns on Charging Station | Customer Communication Portal turns on Charging Station at assigned time | Customer Communication Portal | EV Charging Station, EV | Initiate EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.3.1 |  | Customer Communication Portal alters meter | Customer Communication Portal alerts meter to start monitoring power used for charging | Customer Communication Portal | Meter Device | Start measuring power consumption | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.3.2 |  | Turn off charging | EV On-Board System turns off Charging station on completing the charging operation | EV On-Board System | EV Charging Station | Turn off power to EV | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.3.3 |  | Power Consumption information | Meter Device sends power consumption information to Customer Communication Portal | Meter Device | Customer Communication Portal | Power consumed for EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 2.3.4 |  | Completion of charging | Customer Communication Portal confirms to EV Operation System on completion of charging operation | Customer Communication Portal | EV Operation System | Completion of charging operation | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.1 | Charging Request from third party location | Mark as third party charging event | EV Operation System alerts EV Operation System to mark charging operation as third party charging event |  | EV Operation System | Flag identifying operation as third-party charging event | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.1.1 |  | Collect EV and Customer information | EV Operation System collects EV customer Id and Customer Communication Portal customer Id [owner of the third-party charging station] information | Customer Id of EV owner, EV Id Number, Customer Id of Customer Communication Portal | EV Operation System | EV and Customer information | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.1.2 |  | Determine electric rate applicable | EV Operation System queries EV Operation System to determine electric rate applicable to request | Customer Id, EV Id Number | EV Operation System | EV power rates | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.1.3 |  | Confirm charging requirements | EV Operation System confirms charging requirements | EV Operation System | EV Operation System | EV charging requirements | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.2 |  | Assign charging time slot | EV Operation System queries EV Charging Scheduler to assign charging time slot | EV Charging Scheduler | EV Operation System |  | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.2.1 |  | Informs Customer Communication Portal on charging start time | EV Operation System informs Customer Communication Portal on charging start time | EV Charging Scheduler | Customer Communication Portal | Time slot allotment for EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.3 |  | Turns on Charging | Customer Communication Portal turns on Charging Station at assigned time | Customer Communication Portal | EV Charging Station, EV | Initiate EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.3.1 |  | Customer Communication Portal alters meter | Customer Communication Portal alerts meter to start monitoring power used for charging | Customer Communication Portal | Meter Device | Start measuring power consumption | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.3.2 |  | Turn off charging | EV On-Board System turns off Charging Station on completing the charging operation | EV On-Board System | EV Charging Station | Turn off power to EV | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.3.3 |  | Power Consumption information | Meter Device sends power consumption information to Customer Communication Portal | Meter Device | Customer Communication Portal | Power consumed for EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.3.4 |  | Completion of charging | Customer Communication Portal confirms to EV Operation System on completion of charging operation | Customer Communication Portal | EV Operation System | Completion of charging operation | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 3.3.5 |  | Power Consumption data sent to Database | Power consumption data flagged to EV owner’s Customer Id | Customer Communication Portal | EV Operation System | Assign power usage to EV owner’s account | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 4.1 |  | Transmit power consumption to Billing | Transmit power consumption information to Customer Billing System | EV Operation System | Customer Billing System | Power consumer and applicable rate for EV charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 4.1.1 |  | Billing information for the power consume | Alert EV owner’s Customer Communication Portal with charge information | Customer Billing System | Customer Communication Portal | Billing information for the power consumed for charging | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 4.1.2 |  | Acknowledgment of charging | Confirm charging operation completion to EV Charging Scheduler | EV Operation System | EV Charging Scheduler | Acknowledgment of charging operation completion | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |

## Additional Information

### Actor (Stakeholder) Roles

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Customer Site*** | | ***Those entities that are located at customer’s premises*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Customer | Person | One signed up to participate in the Distributed Energy Resource (DER) program. |
| Customer Communication Portal | System | Customer Communications Portal (Customer Communication Portal), System handling communications function at customer’s premises [in this case, identifying the customer, communications with the charging station, the EV’s on-board computer, meter, and the utility] |
| Meter Device | Device | Device that can measure the power consumed by the customer along with the time at which the power is consumed (so that in this case the utility can charge the appropriate rate for the EV charging at time) and transmit the information to the utility for billing purposes |
| EV Charging Station | System | System at the customer site used to charge the EV batteries |
| EV Id Number | Device | Unique identification number assigned to each participating EV by the utility for tracking power used to charge the batteries of that vehicle |
| EV On-Board System | System | System in the EV used to communicate with the utility via the EV Charging Station and the Customer Communication Portal at the customer location |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Power Company Electric Vehicle Operations*** | | ***Those entities that are charged with managing the EV-related functions for the power company*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| EV Operation System | System | System that contains information about the rates applicable to Electric Vehicle (EV) charging, customers participating in the EV program, their location, and details of their system, such as EV Id, amount of power needed to charge the system, and so on. |
| EV Charging Scheduler | System | System that manages the scheduling of charging of EV to ensure system load diversity |
| Customer Id | Device | Customer identification key that is used by the power company to identify customer for associating the customer with its billing activities |
| Customer Billing System | System | System that handles generation of bills for the services provided to the customer |
| Utility Communications Network | System | System responsible for managing communications between the utility and the participants in the EV program [for functions such as remote meter reading, controlling EV charging stations at customer sites, monitoring EV charging activities and other related communications activities] |
| EV |  |  |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Others*** | | ***Those entities that are involved in this activity, but do not fit in any of the Groupings above*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Third Party EV Charging Station | System | System at a different customer’s site [other than the owner of the EV being charged] for charging EV batteries |
| Energy Service Provider |  |  |

 

### Information exchanged

 

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| EV Charge Request from Customer’s Home Location | Request from customer to charge EV at “cheapest available rates” from the home location along with EV Id, Customer Id and related EV information |
| EV Charge Implementation at Customer’s Home Location | System order to verify customer information, schedule EV charging after checking other EV charging already scheduled in that area, initiating the charging operation, alerting the Customer Communication Portal and meter to acquire the power used for charging and time when used, collecting the metering information at the conclusion of the charging activity, and flagging the power delivered for appropriate billing rates by the billing system |
| EV Charge Request from Third Party Location | Request from customer to charge EV from a third party location along with EV Id, Customer Id, third party location EV Charging Station and customer id information and related EV information |
| EV Charge Implementation at Third Party Location | System order to verify customer and third party location information, schedule a quick-charge EV charging operation, alerting the Customer Communication Portal and meter to acquire the power used for charging and time when used, collecting the metering information at the conclusion of the charging activity, and flagging the power delivered for appropriate billing rates by the billing system to the customer account associated with the EV (and not the third party location customer whose EV Charging Station was used for the quick charge operation) |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Receive Customer Initiated EV Charge Request | On receipt of customer initiated EV charge request, verify charge request origin by accessing EV Operation System database to compare EV Id with Customer Id sent by the Customer Communication Portal: if the request origin is same as customer home location, then set flag to implement EV charging at customer location; if request origin is not customer home location, then set flag to implement EV charging at third party location. |
| Implement EV Charging | Initiate EV charging actions: access EV Operation System Database to determine charging requirements, access EV Charging Scheduler to assign time slot for charging to ensure load diversity, initiate charging at the assigned time, alert Customer Communication Portal and meter to record power consumption and to transmit power usage data on completion of the charging operation, and signal Customer Communication Portal to turn off the charging station. If the request originated from a third party location, then implement a quick charge operation as soon as possible [so as to enable the customer EV to be charged for travel back to customer home location]. |
| Complete Post-Charge Activities | Initiate actions to transmit metering data to customer billing system to generate a charge based on applicable EV tariff rates. If the operation is customer home location charging, then the customer’s account is billed; if the operation is third party charging, then the customer account associated with the EV is billed for the charging operation. |

### Contracts/Regulations

| ***Contract/Regulation*** | ***Impact of Contract/Regulation on Function*** |
| --- | --- |
| EV Program Tariffs | Reduced electric power rates based on off-peak charging based on customer acquiring required equipment at their cost – such as the EV, the charging station and related equipment |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ***Policy*** | ***From Actor*** | ***May*** | ***Shall Not*** | ***Shall*** | ***Description (verb)*** | ***To Actor*** |
| Install EV Equipment | Customer |  |  | X | Customer needs to buy their EV and install EV Charging system at site to participate in the program | Energy Service Provider |
| Provide EV Id | Energy Service Provider |  |  | X | Provide customer’s EV with a unique id that will be transmitted when the EV is plugged into a charging station | Customer |
| Provide EV Rates | Energy Service Provider |  |  | X | Provide reduced electric power rates that will be applied to charging EV at off-peak times | Customer |

 

|  |  |  |  |
| --- | --- | --- | --- |
| ***Constraint*** | ***Type*** | ***Description*** | ***Applies to*** |
| Charging Period | Rate Availability | A customer can utilize special EV power rates for charging during specified off-peak periods | Request for EV charging by customer |

#
