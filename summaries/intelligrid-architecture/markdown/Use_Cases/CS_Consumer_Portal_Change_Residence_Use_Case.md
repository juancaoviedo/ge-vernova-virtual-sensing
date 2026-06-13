# Cust Port Change Res

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_Consumer_Portal_Change_Residence_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Consumer Portal - Change Residence Function

## Contents

* [Narrative](CS_Consumer_Portal_Change_Residence_Use_Case.htm#Narrative)
* [Steps](CS_Consumer_Portal_Change_Residence_Use_Case.htm#Steps)

## Narrative

An
existing customer wants to close out his existing account and
transfer that to his new residence, along with all applicable
utility service and billing account information.  This transfer is
to be accomplished as an one-stop service in which the customer
makes one call to the power company whose service representative
handles all of the actions.

A western utility has a
residential customer base of 1 million meters. The meters are
installed in single-family detached housing (SFD), single-family
attached housing (SFA), apartment buildings and mobile homes. The
utility has a high residential turnover rate as customers come to and
leave the service area more frequently than typical utilities.

The utility has demand relief
requirements and has multiple demand response programs in place. It
additionally supports active residential conservation programs as well
as residential alternate, renewable and distributed generation.

The results of all of these
efforts are reported to the Sate PUC as part of their requirements to
receive credit in rate base.

On Monday morning a residential
customer of utility X calls Customer Service and requests that their
power be turned off because they are moving from their SFD home in the
suburbs to a condo in town. They want to simplify their lives. They
advise the utility that they already have the condo purchased and
wondered if they could transfer their utility bill to the new address
and pay on the same monthly schedule as they now have. They also ask
if the electric utility can facilitate the shut-off and/or transfer of
all of their utilities including gas, water, trash collection, cable
TV service and telephone.

The progressive utility assures
the customer that they can provide one-stop service and in fact can
take care of everything. The Customer Service representative (CSR)
calls up the customer’s account information and forwards the entire
request, along with the information to a “relocation specialist” (RS)
while the customer is still on the line. The relocation specialist
opens up a regional web-hosted database and using the electric
utility’s identification number, calls up all utility services that
the client has signed up for. By placing in the moving data and
relocation information, the database software automatically notifies
all other utilities of the pending move. Each utility can then provide
final billing information on the old residence and set up the services
at the new residence. The residential customer receives a transaction
report, much like a stock market purchase/sell order, that identifies
all utilities, all accounts, dates and transitions the customer to a
new residence and sets up new account information. The transition
invoice lists services provided up to the transition date as cost “X”
and starts new billing information (on the same monthly invoice) that
delineates costs for services provided at the new residence for the
remaining days of the month.

The residential customer moves to
the new home and all utilities are in service and they receive a
monthly invoice at the usual time that includes old house and new
house billing information. The process is seamless, transparent to the
customer, and of value to the utilities involved.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Customer calls utility | Request account change | Customer calls utility to request account change | Customer | CSR | Customer account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 1.1 | Customer call received by CSR | Identifies Customer Account | Customer service representative (CSR) identifies customer account | Customer Information Database | CSR | Customer account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 1.2 | Customer request account change | Service Request Type | CSR determine nature of service request [in this case, account change] | Customer | CSR | Service Request Type | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 1.3 |  | Customer account change | Transfer call to Customer Relocation Specialist | Customer Information Database | CRS | Customer account change | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.1 | Customer call to utility | Request Close out current location services | Customer Relocation Specialist determines when services to current location are to be turned off | Customer | CRS | Account close date | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.2.0 | Closing service at current Customer location | Initiate Close out current location services | Customer Relocation Specialist initiates action to turn off power to current location on specified date | Customer Information Database | Customer Communication Portal | Power turn off command to current location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.2.1 | Power Turn-Off Request | Transmit final reading | Customer Relocation Specialist instructs Customer Communication Portal to transmit final reading on service turn off | Customer Information Database, Customer Communication Portal | Customer billing system | Final reading at current location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3 | Request for Final Billing | Identify current service provider | CRS accesses regional database to identify services provided to customer at current location using the common customer id | Customer Information Database, Regional Customer Information Database | CRS | List of services and service providers to the customer at the current location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3.1 | Customer moving out, Identified current service provider | Close out current location services | CRS instructs each of the service provider to turn service off to location on specified date | Customer Information Database, Regional Customer Information Database, CRS | Customer billing system, Regional Customer Information Database, Customer Communication Portal, Energy Service Provider | Service turn off command to current location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3.2 | Customer moving out, request for final billing | Transmit final billing information | RS requests each service provider to transmit final billing information on current account | CRS, Regional Customer Information Database, Energy Service Provider | Customer Information Database, Customer billing system, Regional Customer Information Database | Final reading | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 2.4 | Customer moving out of the current location, close services | Close out current location services | CRS instructs the billing system to close current location account | CRS | Customer billing system, Regional Customer Information Database | account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.1 | Customer moving to a new location | Set up services at the new customer location | Customer provides new location information to RS | Customer, Customer Information Database | CRS, Customer Information Database, Customer billing system, Regional Customer Information Database | New location information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.1.1 | Customer moving to a new location, service begin date | Start up date at the new customer location | Customer indicates when power service is to be resumed at new location | Customer | CRS, Customer Information Database, Customer billing system | Date for turning on power at new customer location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.1.2 | Customer requests to initiate new services | Customer authorizes CRS | Customer authorizes CRS to initiate other services to the new location on the specified date | Customer, Customer Information Database, Regional Customer Information Database | Customer Information Database, Customer billing system, Regional Customer Information Database, Energy Service Provider | New location account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2 | Customer authorizes CRS to initiate services | CRS instructs system to initiate power service | CRS instructs system to initiate power service to new location on the specified date | CRS, Customer Information Database | Customer Information Database, Customer billing system, Customer Communication Portal | Turn on power to the new location on the specified date | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2.1 |  | CRS accesses service providers | CRS accesses regional database to transfer new location information to each of the service providers | CRS, Customer Information Database, Regional Customer Information Database | Regional Customer Information Database | New location account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2.2 |  | Transfer final billing to new account | CRS instructs billing system to transfer final billing read to the new location account | CRS, Customer Information Database | Customer billing system | Final billing read from the old customer location | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2.3 | Customer moving to a new location, need to link billing | New location to link to customer account | CRS instructs Customer Communication Portal at new location to link to customer account | CRS, Customer Information Database | Customer Communication Portal | Customer account information | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2.4 |  | Send out change confirmation to the customer | CRS instructs billing system to send out change confirmation to the customer | CRS, Customer Information Database, Customer billing system, Regional Customer Information Database | Customer, Customer Information Database, Regional Customer Information Database, Energy Service Provider | New location account confirmation | [Customer / ESP](../Environments/Env18_Customer_to_ESP.htm) |
