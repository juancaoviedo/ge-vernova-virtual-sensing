# Cust Port Dmd Reduct

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Demand_Reduction_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Consumer Portal - Demand Reduction Program

## Contents

* [Narrative](CS_Consumer_Portal_Demand_Reduction_Use_Case.htm#Narrative)
* [Steps](CS_Consumer_Portal_Demand_Reduction_Use_Case.htm#Steps)
* [Additional Information](CS_Consumer_Portal_Demand_Reduction_Use_Case.htm#Additional Information)

## Narrative

### Overview

A customer
wants to sign up for the Demand Reduction Program offered by the
utility which would give the utility permission to cycle customer’s
air conditioning system during peak load periods in return for
incentives. The utility representative signs up the customer, handles
installation of needed devices and implements the customer’s
participation in the program. At a later, the customer asks to be
transferred to a different load reduction program level and this
change is implemented accordingly.

### Description

A western utility
has a residential customer base of 1 million meters. The meters are
installed in single-family detached housing (SFD), single-family
attached housing (SFA), apartment buildings, and mobile homes. The
utility has a high residential turnover rate as customers come to and
leave the service area more frequently than typical utilities.

The utility has
demand relief requirements and has multiple demand response programs
in place. It additionally supports active residential conservation
programs as well as residential alternate, renewable, and distributed
generation.

The results of all
of these efforts are reported to the Sate PUC as part of their
requirements to receive credit in rate base.

On Monday morning
a residential customer of utility X calls Customer Service and
requests a “sign up” in the utility’s air-conditioning demand response
programs that they read about in the newspaper. The Customer Service
representative [CSR] transfers the call along with the customers
account information “utility program specialist” while the customer is
still on the line. The program specialist [PS] opens up a computer
file that delineates the features and requirements for participation
in each of the utilities AC demand reduction program (that includes a
gateway product, a smart thermostat product, and a simple switching
product, all with different incentives). The customer selects a
specific program and the specialist asks pertinent questions about the
customer’s participation to help reduce problems. The specialist
selects a convenient date for installation of equipment and to start
the program at the specific residence. Once the program specifics and
the customer specifics are entered into the Demand Response database,
the installation company is notified of the specific program
requested, the installation date, customer information and specific
tracking number/ID. The information is automatically downloaded into a
PDA designed to accommodate the data.

The installer
places the appropriate equipment, in this case a DLC switch, on the
customers AC unit, tests the system with a handheld unit, and places
all information into the same PDA as used to download the original
request. After the installation is completed, the PDA is connected to
the installers computer system in the truck and via a web-hosted
database all information is uploaded to the utility. The utility
software automatically notifies the Demand Response Program Manager [DRPM],
advises billing that the customer will receive a financial incentive,
which is listed on their monthly bill during the appropriate summer
months and subtracted from the “amount due” line. At the end of the
summer program, the billing software automatically reverts to the
normal invoice and removes incentives from the bill.

In addition to
billing, the program initiation also triggers a summer-months energy
consumption-tracking program. The software recalls specific customer
usage data for the previous year for the months of June, July, August
and September. The database also includes average daily and monthly
ambient temperatures, which will be used with customer usage data to
ascertain savings and relative demand reduction. The information is
inserted into a database that is used by the Demand Response Program
Manager to assess relative load reduction as well as to determine if
free-ridership is an issue.

The residential
customer participates in the program through July, but after several
110+ degree-days decides that participating in the program at the 100%
cycling strategy (complete AC shut down for the designated curtailment
period) is too severe and wants to be placed in the 50% cycling
program. The request in placed into the system by the utility program
specialist and the customer is automatically removed from the 100%
strategy, placed on the 50% strategy, billing is notified
automatically and the incentive is recalculated. The Program Manager
is notified of the change in participation level, the billing is
advised to adjust the financial incentive and the tracking database
flagged with the information as well.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Customer call to utility | Request program signup | Customer service representative identifies customer account | Customer Information Database | CSR | Customer account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 1.2 |  | Service Request Type | CSR determines nature of service request [in this case, signup for Demand Reduction Program Database] | Customer | CSR | Program signup request | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 1.3 |  | Transfer call | Transfers call to utility’s Program Specialist | CSR | Utility Program Specialist | Customer account information, Program signup request | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1 | Customer interest in signing up for DLRP | Determine which DLRP is appropriate for customer | Utility Program Specialist determines which level of DLRP is appropriate for this customer | Customer Information Database, Demand Reduction Program Database | Customer | Demand Reduction Program Database details | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1.1 |  | Signup customer to specific DLRP | Program Specialist signs up customer to the DLC switch program | Customer Information Database, Demand Reduction Program Database | Customer, Customer Billing System | Specific program requirements and reward incentives | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1.2 | Determines specific DLRP | Schedules installation | Program Specialist schedules installation | Customer Information Database | Customer site installation database | Installation details | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.2 | Request to install specific DLRP | Installation by service provider | Specified equipment is installed and tested by installation service providers | Installer | Customer Information Database, Demand Reduction Program Database Manager, Customer Billing System | Installation confirmation | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3 | Installed new customer site installation | Customer Communication Portal to monitor energy usage | Customer Communication Portal is alerted to monitor energy usage and ambient temperatures | Customer Communication Portal, Customer Information Database | Demand Reduction Program Database | Average and peak temperatures, customer’s historical energy usage and current energy usage | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.4 |  | Billing system generates billing | Billing system generates summer billing with applicable reward incentives | Customer Billing System | Customer | Monthly billing with deductions for applicable incentives | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.1 | Customer request to change participation level | Change Demand Reduction Program Database participation level | Customer requests change from 100% to 50% cycling program level | Customer, Customer Information Database | Utility Program Specialist | Changes in program participation level | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2 | Utility Program Specialist receives change of participation request | Program Specialist confirms change | Program Specialist confirms change in cycling rate and corresponding reward incentives | Utility Program Specialist | Customer, Customer Information Database, Demand Reduction Program Database | Program participation change | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.3 | Customers participation level is changed | Affected parties are informed | Applicable affected parties are informed of the change | Customer Information Database | Customer Billing System, Demand Reduction Program Database Manager | Change in participation level and reward incentive change | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.4 |  | Customer Communication Portal and DLC system notified | Customer Communication Portal and DLC system notified of cycling rate change | Demand Reduction Program Database | Customer Communication Portal, DLC Switch Controller | Programming change to DLC for new cycling rate and revised monitoring instructions to Customer Communication Portal | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |

## Additional Information

### Actor (Stakeholder) Roles

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Customer Site*** | | ***Those entities that are located at customer’s premises*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Customer | Person | One requesting the sign up for the Demand Reduction Program. |
| Customer Communication Portal | Power System | Power System handling communications function at customer’s premises |
| DLC Switch Controller | Device | Device performing cycling of the air conditioning unit |

 

.

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Load Serving Entity Customer Service*** | | ***Those entities that are charged with handling customer service functions for the power company*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Load Serving Entity | Power System | Power company communications system that handles customer call center services |
| CSR | Person | Customer Service Representative (CSR), Person who interfaces with the customer initially for the power company |
| Utility Program Specialist | Person | Person who handles load reduction-related services for the customer |
| Customer Information Database | Power System | Power System that contains information about customer accounts of the power company |
| Demand Reduction Program Database | Power System | Power System that contains information about all of the Demand Reduction Program [Demand Reduction Program Database] Database offered by the utility, participation requirements, equipment details and links to customer billing system for passing incentive information |
| Demand Reduction Program Database Manager | Person | Demand Response Program Manager |
| Customer Billing System | Power System | Power System that handles generation of bills for the services provided to the customer |
| Customer Id | Device | A common customer identification key that is used by service providers authorized by the customer to identify all of their service accounts |
| Installation Schedule Database | Power System | Power System that handles scheduling installation of equipment at customer premises [in this case, the DLC switch], specifying equipment to be installed, confirmation of completion of installation and links to the billing system using the common customer id |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Installer*** | | ***Those entities that are associated with the installation function*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Installer | Person | Utility person assigned to handle the specified customer site installation task |
| DLC Switch Controller | Device | Power System handling cycling of air conditioning equipment at customer’s premises [generally consists of a RF receiver and a switch component to turn the air conditioning compressor on/off] |
| Installation System | Power System | Power System for managing the installation activities at the customer site – in this case consists of a PDA that contains the installation order information, a test unit to verify proper installation and software to record installation details |
| Installer Computer | Power System | Power System for accessing utility’s installation database, downloading specific order information to the InstallationSystem PDA, communications link to the utility’s network to access order data and to upload confirmation data |

 

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community) ,*** | | ***Group Description*** |
| ***Others*** | | ***Those entities that are involved in this activity, but do not fit in any of the Groupings above*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| Public Utility Commission | Person | The entity that receives results of the utility’s demand reduction program. |
| Demand Response Program Manager | Person | Person managing the Demand Reduction Program Database at the utility |
| Energy Service Provider |  |  |
| Service Provider |  |  |
| Air Conditioning Equipment |  |  |

 

 

### Information exchanged

 

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| Customer Demand Reduction Program Signup Request | Information from the customer call for signing up to participate in the utility’s Demand Reduction Program |
| Customer Power System Installation Order | Information on scheduling the installation at customer’s site, equipment to be installed, programming information on cycling regime, details to be passed on to the billing program on initiating incentive reward, intimation to Demand Response Program Manager and triggers to start tracking energy usage for program performance verification |
| Program Change Request | Information from the customer call on the changes to be made to the customer’s participation level in the utility’s Demand Reduction Program |
| Program Change Confirmation | Information confirming the changes made to the account based on the customer call, with appropriate notification and triggers as per those initiated on program activation |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Signup Customer to Requested Demand Reduction Program | Initiate actions to modify customer’s account information to indicate details of participation in the Demand Reduction Program specified by the customer and generate trigger to installation scheduling program |
| Set Up Customer Power System Installation Order | Initiate actions to schedule installation at customer site, and transmit customer site information, equipment details and scheduling to the installer |
| Power System Installation | Perform installation at customer site, verify system performance, and upload installation confirmation back to utility |
| Installation Follow-up | Initiate actions to update load reduction system to send out appropriate control signals to customer unit, update customer billing information with applicable incentives, alert the applicable Demand Response Program Manager about installation, initiate energy usage tracking, and set up flags in the billing database to revert to regular billing at the end of incentive period |
| Customer Request to Change Program Participation | Initiate actions to modify customer account information with the change to the program participation, transmit revised incentive information to billing system, and alert the applicable Demand Response Program Manager about change in participation level |
| Program Change Conformation | Initiate actions to generate a confirmation message to the customer with details of the change made in program participation level and the applicable incentive rewards at the new level |

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

 

|  |  |  |  |
| --- | --- | --- | --- |
| Constraint | Type | Description | Applies to |
| Program Participation | Level of Participation | The level of Demand Reduction Program participation chosen by the customer | Power cycling regime implemented and amount of incentive reward provided |
| Reward Period | Inactive | Months of the year when the program is not active [i.e., non-summer months for this program] | No incentive reward provided |
| Energy Usage | Minimum Threshold | Tracked energy usage to meet or exceed program requirements to qualify to participate in the program and receive incentive reward on bill | Eligibility to continue participation in the program |

#
