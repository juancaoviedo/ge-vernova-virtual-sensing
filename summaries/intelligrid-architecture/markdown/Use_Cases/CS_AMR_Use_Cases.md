# AMR Use Cases

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_AMR_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Automatic Meter Reading (AMR) and Related Customer Service Functions

***Involving the Customers in Making
Decisions about their Use of Energy***

## Introduction to AMR and Related Customer Service Functions

Figure 1 illustrates the AMR function: with
interconnections between Automatic Meter Reading (AMR) systems and
customers. In this function, three types of customers are identified:

> ·       
> Residential customers
>
> ·       
> Commercial customers
>
> ·       
> Industrial customers

In addition three types of AMR systems are
identified and are described in the following sections:

> ·       
> [Hand-held or drive-by van AMR system](CS_AMR_Use_Cases.htm#Hand-Held or Drive-by Van AMR Function)
>
> ·       
> [One-way
> fixed network AMR system](CS_AMR_Use_Cases.htm#One-Way Fixed Network AMR Function)
>
> ·       
> [Two-way fixed network C&I consumer gateway](CS_AMR_Use_Cases.htm#Two-Way Fixed Network C&I Consumer Gateway)

Figure 1: Automatic Meter Reading and
Related Customer Services

## Business Drivers and Opportunities for AMR and Related Customer Services

Customers have come to expect
high levels of service, where the click of a mouse button provides
instant response, and companies are (all too) aware of personal
interests. Provision of electrical services are no different.
Increasingly, different types of customers are expecting different
levels of service with commensurate tariff rates, such as:

* **Customer control over energy usage** with real-time
  information on their current energy usage, their demand
  level, and current energy prices, combined with various
  options for the customers to control their usage, ranging
  from manual customer actions, to the use of Building
  Automation Systems (BAS) making pre-authorized energy usage
  adjustments , to direct load and generation control by
  remote Energy Services Providers ([ESPs](../Glossary/Glossary_E.htm#Energy Service Provider (ESP))).
* **Sharing automation costs with customers**, where
  both utilities and customers would benefit from the
  automation systems. This concept is most likely to be of
  interest to commercial and industrial customers, but could
  become of interest to residential customers in specific
  instances.
* **Sharing benefits from market-driven "demand response"
  activities with customers**, for instance, by sharing with
  customers the sale of energy to external entities,
  particularly during peak demand times when customers have
  been asked to reduce their demand.
* **Highly reliable energy**, with backup sources of power
  such as from a second feeder from a different substation, or more
  often, backup generation in the form of a Uninterruptible
  Power Supply (UPS) and a diesel generator unit.
* **High power quality**, where the frequency and voltage
  levels are maintained within a specific band, and spikes,
  harmonics, and other anomalies are minimized.
* **Net metering**, where the customer can either use energy
  from the grid or supply energy to the grid through the use
  of distributed resources.
* **Consolidated billing** for multiple sites
* **Sub-metering** of individual apartments, campus
  buildings, departments, and equipment
* **Real-Time access to energy billing** information
* Participation in individual or aggregated market
  opportunities through time-of-use (TOU) or
  [Real-Time Pricing (RTP)](CS_RTP_Overview_Use_Cases.htm) 
  schemes.
* **Lower "interruptible" tariff rates** in return for providing interruptible
  loads, load management, or managing energy usage as
  requested by the utility.
* **Lowest price** with minimal services, but with
  innovative approaches to help those customers who are least
  able to pay for their energy.

These services require
automation. Much of the automation is in the billing and accounting
department; other automation is in the call center to handle trouble
reporting and billing questions. Nonetheless, some automation must reach
out to the customer sites. The benefit-cost of different schemes is a
subject of much discussion, and no single answer is appropriate for
all situations. One result is clear, however: establishing an AMR
system only for reading meters and for no other function is not
cost-effective. Therefore, it is vital to add ("piggy-back") other
functions on to the pure AMR in order to make the best use of the
automation. As with the entire electric industry, enabling
technologies are also changing the benefit-cost environment, sometimes
on a monthly basis.

The following discussions
address the customer services involving information from customer
sites (as opposed to in-house billing and accounting systems).

### Possible Customer Services Involving Customer Site Automation

The
customer services often involve the use of Automatic Meter Reading
(AMR) technologies, although AMR is not required for all functions. In
fact, AMR is really a misnomer, since it implies only the reading of
meters, while customer automation is far more extensive. However, the
term AMR has become almost synonymous with customer automation by most
utilities.

Customer
services can include:

* ***Periodic electric meter reading:*** Periodic
  meter reading is normally used for traditional billing. It
  can therefore be regarded as replacement of manual meter
  reading, and does not provide more information. It can,
  however, be beneficial for hard to read meters and in
  neighborhoods where manual reading may be dangerous.
  Automatic periodic reading can also reduce missed readings
  and reading errors. 
  [Drive-by
  AMR](CS_AMR_Use_Cases.htm#Hand-Held or Drive-by Van AMR Function) is often used for periodic AMR, since the cost of
  fixed communications is difficult to justify. When
  [fixed
  communication systems](CS_AMR_Use_Cases.htm#One-Way Fixed Network AMR Function) are used, readings can be
  scheduled, for individual meters or groups of meters, to be
  taken on specific metering cycles, a feature that may be
  desired by some large customers.
* ***Time of Use (TOU)
  metering:***   Separate metering of the energy consumed
  during periods to which different rates apply (e.g., peak,
  shoulder, and off peak rates, and possibly also rates for
  for different day types). TOU bills can be calculated from
  accurate interval readings or from multi-register meters, in
  which each register is dedicated  to the accumulation of the
  energy consumed in one of the time-of-use periods. TOU
  meters do not necessarily require AMR, and are often read by
  hand held devices with optical coupling the the meters. The
  meter reader can also use the hand held device to
  resynchronize the meters' clocks and to reprogram them for a
  new rate schedule. TOU meters operating under an AMR system
  require two-way communications, so that the meter clocks can
  be remotely synchronized and they can be remotely
  reprogrammed.
* ***Interval energy reading:*** Interval metering is
  the capability to take readings at given time intervals,
  such as hourly, or every 15 minutes, or even every minute.
  Usually interval readings require the use of the more
  sophisticated digital meters. Interval readings are normally
  taken and stored automatically by the customer site end
  equipment (the meter or the meter interface unit of the AMR
  system), and are later retrieved by the AMR master. This
  ensures that readings are not lost due to temporary
  communications problems or when the AMR master is not
  available for a while. Local reading of the meters also
  permits all the meters or large groups of meters to be read
  simultaneously at precise points in time. Readings taken
  exactly on schedule can be employed for all kinds of
  billing, including periodic (usually monthly) billing,
  time-of-use billing, and to determine demand charges. If 
  [Real Time Pricing (RTP)](CS_AMR_Use_Cases.htm#Real Time Pricing (RTP))
  is instituted in the future, interval metering can be
  used to determine the customer's power consumption for each
  price period. Accurate time keeping by the end equipment is
  however required for interval readings to be used for time
  dependent billing, and this implies a capability to remotely
  synchronize the end unit clocks from time to time.
* ***Load Profile information:*** Interval readings
  can be used to produce a load profile of the total or
  sub-totals of customer energy usage.. Load profile data can
  be used both by the customer and the utility. Individual
  customer load profiles can be used by the customer to
  monitor energy usage at specific times of day or under
  specific circumstances. Utilities can use load profiles as
  part of general load surveys as well as input to
  Distribution Automation load models.

* ***Peak demand metering:*** Certain customer tariffs
  can include charges that depend on the maximum demand over
  the billing period. Peak demand can be derived from interval
  metering. Some electronic meters for C&I customers can also
  provide a peak demand reading.
* ***On-demand electric meter reading:*** With two-way
  fixed communications it may be possible to read individual
  meters at any time on demand. This allows readings to be
  taken when service is transferred to a new customer, and is
  useful for customer service personnel when answering
  inquiries and complaints by customers. One installed a
  demand reading capabilities for their large Commercial and
  Industrial (C&I) meters, with the primary objective of real
  time monitoring of compliance with load curtailing requests,
  so that customers who fail to meet their obligations can be
  immediately contacted.
* ***Energy
  usage and billing Information***: Many customers
  can benefit from having access to their current energy usage,
  demand measurements, historical usage, and billing
  information. This information can be supplied locally if the
  customer has a building management system, or
  could be provided over secure connections via the Internet.

* ***Power quality
  monitoring:*** Capabilities to monitor voltage,
  harmonics, sags and surges, and other power quality
  characteristics in addition to diverse energy metering
  functions are available for electronic meters (also called
  digital meters) from several manufacturers, usually as extra
  cost options. Some meters are designed to detect and report
  deviations from preset power quality parameters, and other
  meters provide a comprehensive power quality analysis and
  log a large number of parameters. These meters are usually
  available with a variety of communications interface options
  such as EIA-232 and, more recently, internet interfaces, and
  with various communications protocols such as DNP 3.0 and
  MODBUS. Sophisticated electronic meters are often used in
  AMR systems that are limited to C&I customers, and may be
  included in system-wide AMR that employs simpler metering
  for the residential customers.
* ***Outage detection:***
  Outage detection devices are installed at customer sites and
  call the utility as soon as power is lost. Outage detection
  can be included in interface modules that are added to
  residential meters to prepare them for AMR, and inexpensive
  modules just for outage reporting are also available..
  Outage detection modules from Amron or Itron are plugged
  into any outlet and into a telephone jack at the customer's
  premise. These units call the utility when power goes out,
  and may also call to report over and under voltage. The
  system at the utility identifies the calling number, and
  therefore the account that lost power. Utilities usually
  place more than one outage detection unit on every branch of
  the distribution network in order to avoid false alarms when
  the customer trips a breaker in his home's electric panel or
  pulls the outage detection unit from the outlet.
* ***Tamper detection:***
  A tamper detection capability is available in many meters,
  including residential meters. Such meters will identify
  removal of the meter from its socket or reverse power flow
  as tampering. Tampering event can be flagged as a status
  flag, logged in meters that store readings - possibly with a
  time stamp, or can be reported in AMR system with two-way
  communications. Tamper detection can also be performed by
  analyzing customers meter data, in particular when interval
  readings are available.
* ***"Soft"
  Customer connect and disconnect:***  This term
  refers to remote reading of a meter when an account is
  initiated and when an account is terminated.
* ***"Hard"
  Customer connect and disconnect:*** As an adjunct
  to the meter reading capability, an AMR system with two-way
  communications may also allow physical disconnection and
  reconnection of power to a customer. This requires,
  obviously, a large relay rated for the capacity of the
  customer's circuitry.

* ***Load Management:***
  Remote shedding of customer devices for peak shaving and
  emergency load relief can be considered the oldest customer
  automation function. It has been practiced for decades,
  starting when European utilities used "ripple control",
  injection of very low frequency signals into the
  distribution feeders to control relays at the customer homes
  to disconnect water heaters during peak times. Since then
  several communications technologies have been developed for
  remote control of customer loads, and the same customer
  communications are sometimes shared for AMR. More
  sophisticated load control technologies, that allow for
  instance remote setting of thermostats instead of shedding
  loads are emerging.
* ***Real Time Pricing (RTP):***
  If a utility sent short term pricing information, say for
  the next hour, the customers could use this information to
  reduce cost by managing their energy consumption. RTP
  benefits both the utility and the customers by sharing the
  savings accrued from shifting loads to periods when it costs
  the utility less to serve them. RTP is only beginning to
  develop, and is beginning to be offered to large customers.
  When high penetration of RTP to residential customers
  becomes practical, the manufacturers of appliances can be
  expected to support it. For instance, cloths dryers may
  allow the user to set the appliance to start only when the
  cost of a kWh price goes below a certain price.
* ***Gas and water meter reading:*** Many AMR end-user
  units for electric meters support additional inputs, from
  pulse generators and possibly from encoders, for gas and
  water meters. This capability is obviously useful for
  electric and Gas utilities, but can also be a source of
  revenue by collecting metering data for other utilities and
  is, of course used by meter data management agents (MDMAs).
  Indeed the electric utility is in the best position to be
  the owner of an AMR system that is shared for gas and water
  metering, because electricity is readily available for an
  AMR end-user device at the electric meter, whereas gas and
  water end devices often use batteries.
* ***Whole house and by appliance***: In-building
  systems usually can monitor individual appliances or areas
  within a building, as a means for analysis of energy usage.
* ***Distributed Resources management:*** DR devices
  can be monitored and controlled remotely.

### Stakeholders for Customer Services

As can be seen from the long list of possible customer services, many
different stakeholders must become involved in the provision of
customer services. These include:

* **Utility departments** (which may or may not be part of
  larger utility entities and may or may not consist of the
  same group):
  + Construction department, which is responsible for
    designing and constructing the interconnection
    between the electric wires (usually distribution)
    and the customer site.
  + Maintenance department, which is responsible for
    maintaining the quality of service at the point of
    interconnection as was contracted between the
    utility and the customer, including repairs, power
    quality monitoring, and implementing solutions to
    problems.
  + Operations department, which is responsible for
    operating the power system in accordance with the
    contracted quality of service. This usually
    entails responding to outages by restoring power
    as rapidly as possible, but can include load
    control, requesting load reductions from
    interruptible customers, and, in the future,
    establishing current prices for energy for
    Real-Time Price (RTP) customers.
  + Customer services department, which interfaces
    with the customer. The types of interfaces vary
    depending upon the contracted quality of service,
    ranging from responding to billing questions and
    issues to one-on-one meetings to providing various
    energy services in addition to electrical energy.
  + Metering department, which provides, maintains,
    and periodically reads the customer meters.
  + Billing department, which calculates invoices
    based on each customer's tariff, energy usage and
    other factors.
  + Accounts receivable department, which handles
    payments from customers.
* **Customers**:
  + The electrical customer physically interconnected
    to the power system and receiving the electrical
    energy at their premises
  + The billing customer responsible for paying for
    the electrical services. For residential
    customers, this is usually is the same as the
    electrical customer, but for many industrial and
    commercial customers, often a centralized accounts
    payable department is responsible for handling the
    bills.
  + Owner of distributed resources which are
    electrically interconnected to the power system.
* **Others**:
  + [Energy Service Providers (ESPs)](../Glossary/Glossary_E.htm#Energy Service Provider (ESP)) which may
    provide energy services in addition to, or instead
    of, utilities.
  + [Meter Data Management Agencies (MDMAs)](../Glossary/Glossary_M.htm#Meter Data Management Agents (MDMA)), which
    may read the customer meters in addition to, or
    instead of, utilities.
  + In-building service providers, which provide
    building energy management systems and other
    services for supporting customer needs.
  + Market brokers, who broker energy contracts for
    individual customers or aggregates of customers.
  + Distributed Resources management providers, which
    manage the use, operations, and/or maintenance of
    customer-side generation.

## Hand-Held or Drive-by Van AMR Function

### Narrative

The purpose of the Hand-Held or Drive-by Van
AMR function is to perform monthly and/or special reads of customer
meters. These AMR systems are primarily oriented toward residential
customers, but are often used for smaller commercial and industrial
customers as well. Normally different meter reading systems are used
for the larger commercial and industrial customers.

The meter readers either walk or drive by
customer sites, and use the mobile meter-reading device (hand-held or
within a van) to read each meter using vendor-proprietary protocols.
At the end of the meter reader’s shift, these mobile meter-reading
devices upload the meter readings into a metering database. Typically,
each customer site has its meters read once a month, but special
circumstances can involve special reads. For example, if a meter
reading is either “invalid” or the customer is questioning it, then a
special reading may be required. Other special circumstances include
disconnecting meters when customers move or fail to pay, and
connecting meters when new customers move in.

In the metering system, the energy usage of
each customer is determined, either as a direct read from an
electronic meter or as calculated by subtracting previous meter
readings of analog meters. Demand measurements per period (e.g. for
each 15-minute period) are also uploaded if the electronic meters can
provide that information.

The energy usage and demand measurements are
then passed to the Customer Information System (CIS) and/or the
Billing System.  If stored in the CIS, these energy usage and demand
measurements are then available to Customer Representatives to look up
and inform customers if they call in.

At the appropriate time in the billing cycle
for each customer, the Billing System, using the appropriate tariffs,
issues invoices to the customers based on their energy usage and, if
part of their tariff, their demand measurements.

### Steps for Hand-Held or Drive-by Van AMR

The following steps provide the details of the
narrative described above.

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Type of Info Exchanged | IntelliGrid Architecture Environment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Once a month | Read meter | Read the meter once a month using a hand-held device or a drive-by van | Meter | Meter-reading device | Meter energy and demand readings | Intra-Vendor Environment (not within IntelliGrid Architecture scope) |
| 1.2 | Upon special request | Read meter | Read the meter once a month using a hand-held device or a drive-by van. These meter readings can be used for customer inquiries, soft disconnect/connect requests, or reading validations | Meter | Meter-reading device | Meter energy and demand readings | Intra-Vendor Environment (not within IntelliGrid Architecture scope) |
| 1.3 | End of shift | Upload metering data | Upload metering data from the metering device into metering database. In the metering system, energy usage is determined, either as read from meter or as calculated by subtracting previous meter readings. Demand measurements per period (e.g. for each 15-minute period) are also uploaded if the meters provide that information. | Meter-reading device | Metering database | Meter energy and demand readings | Intra-Vendor Environment (not within IntelliGrid Architecture scope) |
| 1.4 | Periodically, such as once a day | Provide customer energy usage | Provide each customer’s energy usage, along with dates of readings and other metering information. This information can be used for customer inquiries, soft disconnect/connect requests, or reading validations | Metering database | Customer Information System (CIS) | Energy usage, dates of readings, average usage, etc. | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |
| 1.5 | Periodically, such as once a month for groups of customers | Generate invoices | Generate invoices for customers based on their energy usage per period (e.g. one month) and the appropriate tariffs | Customer Information System (CIS) | Billing system | Energy usage | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |

## One-Way Fixed Network AMR Function

### Narrative

The purpose of the One-Way Fixed Network AMR
Function is to collect meter information from customer sites,
including monthly meter readings, on-demand meter readings, tamper
detection, soft connects and disconnects (on-demand meter readings),
and outage detection. These systems can be used for all types of
customers.

The one-way fixed network AMR system must first
be installed. These AMR systems are “in-bound” vendor-proprietary
networks using different media, such as telephone, power line carrier,
satellite pager systems, wireless cellular systems, and possibly the
Internet. Different vendors provide different functionalities, which
are constantly changing as technologies and equipment prices change.
Some fixed network AMR systems are basically one-way, but can provide
limited two-way functionality, possibly through low bandwidth signals
or Internet Web pages providing information back to the customer. *(For IntelliGrid Architecture project, the internal functioning of these
vendor-proprietary systems is out of scope: interested readers are
directed to the Web Sites of the various AMR vendors.)*

The metering information is collected
periodically or upon demand from the customer meters. This information
can include:

> ·       
> Monthly metered energy readings
>
> ·       
> On-demand energy readings (used for
> validation, soft connects and disconnects, and customer
> requests)
>
> ·       
> Time of Use (TOU) or periodic (e.g. hourly)
> metered energy readings
>
> ·       
> Demand readings within periods
>
> ·       
> Tamper detection
>
> ·       
> Outage detection

This information is stored in a metering
database with the metering system passing certain data on to other
systems. For instance, the outage data is sent to the Outage
Management System, while tamper detection alarms and on-demand energy
readings are immediately sent to the Customer Information System,
where customer representatives can use the information to pass on to
customers or to initiate other actions.

In the metering system, the energy usage of
each customer is determined, either as a direct read from an
electronic meter or as calculated by subtracting previous meter
readings of analog meters. Demand measurements per period (e.g. for
each 15-minute period) are also uploaded if the electronic meters can
provide that information.

The energy usage and demand measurements are
then passed to the Customer Information System (CIS) and/or the
Billing System.  If stored in the CIS, these energy usage and demand
measurements are then available to Customer Representatives to look up
and inform customers if they call in.

At the appropriate time in the billing cycle
for each customer, the Billing System, using the appropriate tariffs,
issues invoices to the customers based on their energy usage and, if
part of their tariff, their demand measurements.

### Steps for One-Way Fixed Network AMR

The following steps provide the details of the
narrative described above.

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Type of Info Exchanged | IntelliGrid Architecture Environment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 | Daily or other periodicity | Read meter | Read the meter over the network, capturing either meter readings or energy usage over multiple time periods, e.g. on a daily basis, read 5-minute energy usage data. If available in the meter, read the demand measurements for specific time periods, e.g. demand for each 15-minute period. | Meter | Metering database | Energy usage for multiple time periods.  Demand measurements for multiple time periods | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 2.2 | Upon special request | Read meter | Read the meter upon request, capturing either meter readings or energy usage, and demand measurements if available. These meter readings can be used for customer inquiries, soft disconnect/connect requests, or reading validations | Meter | Metering database | Energy usage for multiple time periods.  Demand measurements for multiple time periods | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3.1 | Upon outage detection | Outage detection | An outage at one or more meters is detected | Meter | Metering system | Outage data | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 2.3.2 |  | Outage detection | Metering system issues an alarm of an outage detected at one or more meters | Metering system | Outage Management System | Outage alarm and supporting data | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |
| 2.4 | Periodically, such as once a day | Provide customer energy usage | Provide each customer’s energy usage, along with dates of readings and other metering information. These meter readings can be used for customer inquiries, soft disconnect/connect requests, or reading validations | Metering database | Customer Information System (CIS) | Energy usage, dates of readings, average usage, etc. | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |
| 2.5 | Periodically, such as once a month for groups of customers | Generate invoices | Generate invoices for customers based on their energy usage per period (e.g. one month) and the appropriate tariffs | Customer Information System (CIS) | Billing system | Energy usage | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |

## Two-Way Fixed Network C&I Consumer Gateway

### Narrative

The purpose of the true two-way fixed network
C&I Consumer Gateway is to collect meter information from customer
sites, and to provide control commands and information back to the
customer.

These systems can theoretically be used for all
types of customers, but at the present time, because of the expense of
true two-way communications, the focus is primarily on commercial and
industrial customers. Alternatively, for direct load control of
residential customer equipment, one-way “out-bound” systems can be
implemented (see Load Management). This may change as new technologies
are developed.

The two-way fixed network C&I consumer gateway
system must first be installed. Many of these systems are based on
Itron’s MV-90 system which became the industry de facto standard for
interacting with larger customers, with a number of vendors providing
value-added products over the basic system. In addition, other two-way
networks have been developed using vendor-proprietary protocols and
equipment over different media, including telephone and wireless
cellular systems. Many also rely on the Internet for providing large
volumes of information back to the customer in addition to the
commands or signals provided as part of the two-way system.

Different vendors provide different
functionalities, which are constantly changing as technologies and
equipment prices change. *(For IntelliGrid Architecture project, the internal
functioning of these vendor-proprietary systems is out of scope:
interested readers are directed to the Web Sites of the various AMR
vendors.)*

Similarly to the one-way AMR system, the
information is collected periodically or upon demand from the consumer
gateways. This information can include:

·       
Monthly metered energy readings

·       
On-demand energy readings (used for validation, soft
connects and disconnects, and customer requests)

·       
Time of Use (TOU) or periodic (e.g. hourly) metered
energy readings

·       
Demand readings within periods

·       
Tamper detection

·       
Outage detection

This information is stored in a metering
database with the metering system passing certain data on to other
systems. For instance, the outage data is sent to the Outage
Management System, while tamper detection alarms and on-demand energy
readings are immediately sent to the Customer Information System,
where customer representatives can use the information to pass on to
customers or to initiate other actions.

In the metering system, the energy usage of
each customer is determined, either as a direct read from an
electronic meter or as calculated by subtracting previous meter
readings of analog meters. Demand measurements per period (e.g. for
each 15-minute period) are also uploaded if the electronic meters can
provide that information.

The energy usage and demand measurements are
then passed to the Customer Information System (CIS) and/or the
Billing System.  If stored in the CIS, these energy usage and demand
measurements are then available to Customer Representatives to look up
and inform customers if they call in.

At the appropriate time in the billing cycle
for each customer, the Billing System, using the appropriate tariffs,
issues invoices to the customers based on their energy usage and, if
part of their tariff, their demand measurements.

The information provided to the customer can
include:

·       
Load management direct control commands, that provide
direct remote control over customer equipment, such as air
conditioning, heating, water heaters, pool pumps, and other equipment
over which the customer has agreed to allow remote control.

·       
Distributed Energy Resources (DER) direct control
commands, that provide direct control over customer generation
equipment

·       
Load curtailment signals, that request the customer to
control load and/or their DER equipment but do not actually issue the
control commands, thus putting the customer more closely in the load
management loop to decide how best to meet these requirements

·       
Aggregated load curtailment signals, that request the
customer to negotiate with members of a group of customers (which was
previously established as an aggregated group of customers) to
determine which members of the group will curtail how much load

·       
Pricing signals, that indicate the cost of energy and/or
demand for the current period or in the future

·       
Energy and demand usage information, that provides usage
information, such as current rate of energy usage, current demand
level, energy usage since last billing, energy usage over the last 24
hours, etc.

·       
Billing information, such as current billing charges,
historical billing information, projected billing charges at current
rate of energy usage, etc.

### Steps for Two-Way Fixed Network C&I Consumer Gateway

The following steps provide the details of the
narrative described above.

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Type of Info Exchanged | IntelliGrid Architecture Environment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1 | Daily or other periodicity | Read meter | Read the meter over the network, capturing either meter readings or energy usage over multiple time periods, e.g. on a daily basis, read 5-minute energy usage data. If available in the meter, read the demand measurements for specific time periods, e.g. demand for each 15-minute period. | Meter | Metering database | Energy usage for multiple time periods.  Demand measurements for multiple time periods | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.2 | Upon special request | Read meter | Read the meter upon request, capturing either meter readings or energy usage, and demand measurements if available. These meter readings can be used for customer inquiries, soft disconnect/connect requests, or reading validations | Meter | Metering database | Energy usage for multiple time periods.  Demand measurements for multiple time periods | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.3.1 | Upon outage detection | Outage detection | An outage at one or more meters is detected | Meter | Metering system | Outage data | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.3.2 |  | Outage detection | Metering system issues an alarm of an outage detected at one or more meters | Metering system | Outage Management System | Outage alarm and supporting data | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |
| 3.4 | Periodically, such as once a day | Provide customer energy usage | Provide each customer’s energy usage, along with dates of readings and other metering information. These meter readings can be used for customer inquiries, soft disconnect/connect requests, or reading validations | Metering database | Customer Information System (CIS) | Energy usage, dates of readings, average usage, etc. | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |
| 3.5 | Periodically, such as once a month for groups of customers | Generate invoices | Generate invoices for customers based on their energy usage per period (e.g. one month) and the appropriate tariffs | Customer Information System (CIS) | Billing system | Energy usage | [Intra-corporation Environment](../Environments/Env13_Intra-Corporation.htm) |
| 3.6 | Upon request from Load Management System | Issue direct load control command | Issue a direct load control command to customer equipment that is part of load management | Load Management System | Consumer Gateway | Load control commands | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.7 | Upon request from Load Management System | Issue direct DER control command | Issue a direct generation control command to customer DER systems | Load Management System | Consumer Gateway | DER control commands | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.8 | Upon request from Load Management System | Issue curtailment request | Issue curtailment request which, upon agreement by customer, can be fulfilled either by load reduction or by increased DER generation | Load Management System | Consumer Gateway | Curtailment request | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.9 | Upon request from Load Management System | Issue aggregated curtailment request | Issue aggregated curtailment request to all members of an aggregated group of customers who will negotiate amongst themselves as to who will undertake what levels of load reduction or increased DER generation | Load Management System | Consumer Gateway | Aggregated curtailment request | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.10 | Upon request from Load Management System | Issue pricing signal | Issue pricing signal, which may then be used by the customer to determine what reaction, if any, they will make | Load Management System | Consumer Gateway | Pricing signal | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
| 3.11 | Periodically or upon customer request | Provide energy usage information | Provide energy usage, demand measurements, and billing information to the customer | Customer Information System (CIS) | Consumer Gateway | Energy, demand, and  billing information | [Customer to ESP Environment](../Environments/Env18_Customer_to_ESP.htm) |
