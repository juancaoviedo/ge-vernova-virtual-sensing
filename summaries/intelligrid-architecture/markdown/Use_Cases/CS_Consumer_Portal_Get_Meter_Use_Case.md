# Cust Port Get Meter

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Get_Meter_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Consumer Portal - Get New Meter Function

## Contents

* [Narrative](CS_Consumer_Portal_Get_Meter_Use_Case.htm#Narrative)
* [Steps](CS_Consumer_Portal_Get_Meter_Use_Case.htm#Steps)
* [Additional Information](CS_Consumer_Portal_Get_Meter_Use_Case.htm#Additional Information)

## Narrative

### Overview

A customer
wants to sign up for the Demand Reduction Program offered by the
utility which would give the utility permission to cycle customer’s
air conditioning system during peak load periods in return for
incentives. The utility representative signs up the customer, handles
installation of needed devices along with a new interval meter for
gathering Measurement and Verification data and implements the
customer’s participation in the program. The data collected by the
interval meter is used in report to the Public Utility Commission as
well as to provide Power Purchases department at the utility with a
tool for economic dispatch, and to the Transmission and Distribution
(Transmission Service Provider) department at the utility for load
reduction dispatch by Transmission Service Provider circuit.

### Description

A western utility has a
residential customer base of 1 million meters. The meters are
installed in single-family detached housing (SFD), single-family
attached housing (SFA), apartment buildings, and mobile homes. The
utility has a high residential turnover rate as customers come to and
leave the service area more frequently than typical utilities.

The utility has demand relief
requirements and has multiple demand response programs in place. It
additionally supports active residential conservation programs as well
as residential alternate, renewable, and distributed generation.

The results of all of these
efforts are reported to the Sate PUC as part of their requirements to
receive credit in rate base.

On Monday morning a residential
customer of utility X calls Customer Service and requests a “sign up”
in the utility’s air-conditioning demand response programs that they
read about in the newspaper. The Customer Service (CSR) representative
transfers the call along with the customers account information
“utility program specialist” while the customer is still on the line.
The program specialist (PS) opens up a computer file that delineates
the features and requirements for participation in each of the
utilities AC demand reduction program (that includes a gateway
product, a smart thermostat product, and a simple switching product,
all with different incentives). The customer selects a specific
program and the specialist asks pertinent questions about the
customer’s participation to help reduce problems.

The specialist sees a “flag” that
shows that the customer is in a new subdivision and that the utility
needs additional Measurement & Verification (M & V) data in that area.
The specialist selects a convenient date for installation of
equipment, including a new interval meter, and to start the program at
the specific residence. Once the program specifics and the customer
specifics are entered into the Demand Response database, the
installation company is notified of the specific program requested,
the installation date, customer information and specific tracking
number/ID. The information is automatically downloaded into a PDA
designed to accommodate the data. The meter shop is also notified and
prepares a meter installation at the same time as the curtailment
equipment. The meter number and associated information is loaded into
the PDA for processing along with the other data.

The installer places the
appropriate equipment, in this case a DLC switch, on the customers AC
unit, tests the system with a handheld unit, and places all
information (including the meter ID) into the same PDA as used to
download the original request. At the end of the day, the PDA is
connected to the installers computer system and via a web-hosted
database all information is uploaded to the utility. The utility
software automatically notifies the Demand Response Program Manager (DRPM),
advises billing that the customer will receive a financial incentive,
which is listed on their monthly bill during the appropriate summer
months and subtracted from the “amount due” line. At the end of the
summer program, the billing software automatically reverts to the
normal invoice and removes incentives from the bill.

In addition to billing, the
program initiation also triggers a summer-months energy
consumption-tracking program. The software recalls specific customer
usage data for the previous year for the months of June, July, August
and September. The database also includes average daily and monthly
ambient temperatures, which will be used with customer usage data to
ascertain savings and relative demand reduction. The information is
inserted into a database that is used by the Demand Response Program
Manager to assess relative load reduction as well as to determine if
free-ridership is an issue. In this case the meter data is also
collected remotely by a contracted M & V firm via satellite. The data
is logged in and specific software calculates actual demand reduction
during the summer curtailment periods. The data is used to advise the
PUC of program results as well as to provide Power Purchases
department at the utility with a tool for economic dispatch, and to
the Transmission and Distribution (Transmission Service Provider)
department at the utility for load reduction dispatch by Transmission
Service Provider circuit.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.2 |  | CSR determines nature of service request | CSR determines nature of service request [in this case, signup for Demand Reduction Program Database] | Customer | CSR | Program signup request | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 1.3 |  | Transfers call to Program Specialist | Transfers call to utility’s Program Specialist | CSR | Utility Program Specialist | Customer account information, Program signup request | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1 | Customer interest in signing up for DLRP | Determines specific DLRP | Utility Program Specialist determines which level of DLRP is appropriate for this customer | Customer Information Database, Demand Reduction Program Database | Customer | DLRP details | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1.1 |  | Signup customer to specific DLRP | Program Specialist signs up customer to the DLC switch program | Customer Information Database, Demand Reduction Program Database | Customer, Customer Billing System | Specific program requirements and reward incentives | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1.2 |  | Schedules installation | Program Specialist schedules installation | Customer Information Database | Customer Site Installation Database, Installer | Installation details | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.2 | Request to install equipment for customer by Utility Program Specialist | Equipment is installed | Specified equipment is installed and tested by installation service providers | Installer | Customer Site Installation Database, Demand Reduction Program Database Manager, Customer Billing System | Installation confirmation | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3 | New customer installation | Monitor energy usage | Customer Communication Portal is alerted to monitor energy usage and ambient temperatures | Customer Communication Portal, Customer Information Database | Demand Reduction Program Database | Average and peak temperatures, customer’s historical energy usage and current energy usage | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.4 |  | Billing system generates billing | Billing system generates summer billing with applicable reward incentives | Customer Billing System | Customer | Monthly billing with deductions for applicable incentives | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.1 | Customer interest in signing up for DLRP | Flag Customer is in a new subdivision | Utility Program Specialist notices “flag” that the customer is in a new subdivision where the utility needs additional M & V data | Customer Information Database, M & V Information Database | Utility Program Specialist | Flag requesting additional M & V data in customer’s location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2 |  | Initiates new interval meter installation request | Utility Program Specialist initiates new interval meter installation request | Utility Program Specialist, Customer Information Database | Utility Metering Department | Customer information and interval meter details | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2.1 | Initiates new interval meter installation request | Metering delegates task to installation service provider (installer) | Metering delivers meter with its assigned meter id to the installation service provider | Utility Metering Department | Customer Site Installation Database, Installer | New interval meter, its id details, Remote Meter Device and associated installation information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2.2 | New meter installation request | Installs meter at customer site | Installation service provider uploads confirmation after the meter is installed in service at the customer site | Installer, Installer Computer | Customer Information Database, Customer Site Installation Database, Utility Metering Department, Satellite Communications Network | Notification of the active interval meter and its id details | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.3 |  | Collect M & V data | Initiate collection of M & V data from customer site | Meter Device, Remote Meter Device , Satellite Communications Network | Customer Information Database, Demand Reduction Program Database, Demand Reduction Program Database Manager,  M & V Information Database, Power Purchase, Transmission Service Provider, Public Utility Commission | Actual demand reduction during the summer curtailment periods | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |

## Additional Information

### Actor (Stakeholder) Roles

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Customer Site*** | | ***Those entities that are located at customer’s premises*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Customer | Person | One requesting the sign up for the Demand Reduction Program. |
| Customer Communication Portal | System | System handling communications function at customer’s premises |
| DLC Switch Controller | Device | Device performing cycling of the air conditioning unit |
| Meter Device | Device | Device capturing energy usage data for use in Measurement & Verification purposes. |
| Remote Meter Device | System | System for transmitting interval meter data on demand to the utility [in this case, using a satellite communications link provided by a third party contracted by the utility]. |

 

.

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Load Serving Entity Customer Service*** | | ***Those entities that are charged with handling customer service functions for the power company*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Load Serving Entity | System | Power company communications system that handles customer call center services |
| CSR | Person | Customer Service Representative (CSR), Person who interfaces with the customer initially for the power company |
| Utility Program Specialist | Person | Person who handles load reduction-related services for the customer |
| Customer Information Database | System | System that contains information about customer accounts of the power company |
| Demand Reduction Program Database | System | System that contains information about all of the  Demand Reduction Program [Demand Reduction Program Database] Database offered by the utility, participation requirements, equipment details and links to customer billing system for passing incentive information |
| Customer Billing System | System | System that handles generation of bills for the services provided to the customer |
| Customer ID Creation | Device | A common customer identification key that is used by service providers authorized by the customer to identify all of their service accounts |
| Customer Site Installation Database | System | System that handles scheduling installation of equipment at customer premises [in this case, the DLC switch], specifying equipment to be installed, confirmation of completion of installation and links to the billing system using the common customer id |
| M & V Information Database | System | System that contains M & V information broken down by utility service area segments [such as residential subdivisions] that can be used by various utility departments, such as Power Purchase, Transmission Service Provider, etc |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Installer*** | | ***Those entities that are associated with the installation function*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Installer | Person | Utility person assigned to handle the specified customer site installation task |
| DLC Switch Controller | System | System handling cycling of air conditioning equipment at customer’s premises [generally consists of a RF receiver and a switch component to turn the air conditioning compressor on/off]. |
| Meter Device | Device | Device for capturing energy usage information along with time periods during the day when the energy was consumed. |
| Meter ID Provider | Device | Unique identifier that can be used by the utility to track specific meter installed at customer site, in this case the new interval meter |
| Remote Meter Device | System | System for transmitting interval meter data on demand to the utility [in this case, using a satellite communications link provided by a third party contracted by the utility]. |
| Installation System | System | System for managing the installation activities at the customer site – in this case consists of a PDA that contains the installation order information, a test unit to verify proper installation and software to record installation details. |
| Installer Computer | System | System for accessing utility’s installation database, downloading specific order information to the InstallationSystem PDA, communications link to the utility’s network to access order data and to upload confirmation data. |
| Customer Site Installation Database | System | System that handles scheduling installation of equipment at customer premises [in this case, the DLC switch], specifying equipment to be installed, confirmation of completion of installation and links to the billing system using the common customer id |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Others*** | | ***Those entities that are involved in this activity, but do not fit in any of the Groupings above*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Metering | Person | Department at the utility that manages meters and their installation at the customer site |
| Power Purchase | Person | Department at the utility company that handles procurement of power resources for the utility company. |
| Transmission Service Provider | Person | Department at the utility company that handles the Transmission and Distribution (T&D) functions for the utility company. |
| Satellite Communications Network | System | System responsible for remote meter reading and transmitting the data to the utility company. |
| Public Utility Commission | Person | State Public Utility Commission {PUC):  The entity that receives results of the utility’s demand reduction program. |
| Demand Response Program Manager | Person | Person managing the Demand Reduction Program Database at the utility |
| Energy Service Provider |  |  |
| Service Provider |  |  |
| Air Conditioning Equipment |  |  |

 

### Information exchanged

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| Customer Demand Reduction Program Signup Request | Information from the customer call for signing up to participate in the utility’s Demand Reduction Program |
| Customer System Installation Order | Information on scheduling the installation at customer’s site, equipment to be installed [interval meter, remote meter reading module and DLC], programming information on cycling regime, details to be passed on to the billing program on initiating incentive reward, intimation to Demand Response Program Manager and triggers to start tracking energy usage for program performance verification, and interval data for utility’s M & V functions |
| M & V Information Request | Information trigger generated by the utility’s customer information database to initiate recording of interval energy usage data |
| M & V Information Delivery | Delivery of M & V information collected from customer’s site to utility’s Power Purchase and Transmission Service Provider departments and to the Public Utility Commission for program results verification |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Signup Customer to Requested Demand Reduction Program | Initiate actions to modify customer’s account information to indicate details of participation in the Demand Reduction Program specified by the customer, generate trigger to installation scheduling program, and generate trigger to the Metering Department to install a new interval meter for M & V functionality |
| Set Up Customer System Installation Order | Initiate actions to schedule installation at customer site, and transmit customer site information, equipment details and scheduling to the installer |
| System Installation | Perform installation of specified load control system at customer site, verify system performance, and upload installation confirmation back to utility; perform installation of interval meter with remote meter reading module, verify operation and notify utility of interval meter installation |
| Installation Follow-up | Initiate actions to update load reduction system to send out appropriate control signals to customer unit, update customer billing information with applicable incentives, alert the applicable Demand Response Program Manager about installation, initiate energy usage tracking, initiate obtaining interval data and set up flags in the billing database to revert to regular billing at the end of incentive period |
| M & V Information Delivery | Initiate actions to transmit interval energy usage data to utility’s Power Purchase and Transmission Service Provider departments, and transmit results of the Demand Reduction Program Database to the Public Utility Commission |

### Contracts/Regulations

 

| ***Contract/Regulation*** | ***Impact of Contract/Regulation on Function*** |
| --- | --- |
| Demand Reduction Program Tariffs | Equipment installed at customer site, cycling regime implemented and incentive rewards applied to customer bill |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ***Policy*** | ***From Actor*** | ***May*** | ***Shall Not*** | ***Shall*** | ***Description (verb)*** | ***To Actor*** |
| Cycle Energy to Equipment | Energy Service Provider | X |  |  | Cycle power to air conditioning unit on utility trigger | Air Conditioning Equipment |
| Provide Load Control Equipment | Service Provider |  |  | X | Install specified equipment at customer site | Customer |
| Provide Incentive Rewards | Energy Service Provider |  |  | X | Provide incentive reward on customer energy bill | Customer |
| Modify Incentive Rewards | Energy Service Provider |  |  | X | Modify incentive reward on customer energy bill | Customer |
| Install Meter Device | Energy Service Provider |  |  | X | Install new interval meter at customer site with remote meter reading capability | Energy Service Provider |

 

|  |  |  |  |
| --- | --- | --- | --- |
| ***Constraint*** | ***Type*** | ***Description*** | ***Applies to*** |
| Program Participation | Level of Participation | The level of Demand Reduction Program participation chosen by the customer | Power cycling regime implemented and amount of incentive reward provided |
| Reward Period | Inactive | Months of the year when the program is not active [i.e., non-summer months for this program] | No incentive reward provided |
| Energy Usage | Minimum Threshold | Tracked energy usage to meet or exceed program requirements to qualify to participate in the program and receive incentive reward on bill | Eligibility to continue participation in the program |

#
