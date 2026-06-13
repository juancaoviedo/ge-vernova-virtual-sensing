# IntelliGrid Environments

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Environments/Environments.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# IntelliGrid Architecture Environments

***An IntelliGrid Architecture Environment is defined as a
communication/information environment where the configuration, quality
of service, security, and data management requirements of functions
are the same or very similar***

## 

 Figure: 
IntelliGrid Architecture Environments in Power System Operations

## What is an IntelliGrid Architecture Environment?

IntelliGrid Architecture defines an ***Environment*** as a
logical grouping of power system requirements that could be addressed
by a similar set of distributed computing technologies. Within a
particular environment, the information exchanges used to perform
power system operational functions have very similar architectural
requirements, including their:

* Configuration requirements
* Quality of service requirements
* Security requirements
* Data management requirements

An IntelliGrid Architecture environment groups the requirements of
the information exchanges, not necessarily the location of the
applications or databases (although these may affect the information
exchanges and therefore the environment).

The requirements used to define IntelliGrid Architecture
environments have been derived from the Use Cases described in Volume
II.  These Use Cases were in turn developed from industry stakeholder
contributions.  Since the power system functions defined in these Use
Cases may require multiple types of information exchanges, a
particular power system function (or Use Case) may cross several
environments.

A name and a number represent each
environment.  Figure below lists each
environment and illustrates how they may be physically located within
the power utility. The Table
below briefly
summarizes the differences between the environments.

It should be noted that locally there may be
some valid “sub-environments” within what is defined here as a single
IntelliGrid Architecture environment.  Consumer sites, for instance are shown as single
“Intra-Customer” environment.  Consumer sites, however, may have
separate networks for building automation and controls that coexist
with corporate office networking environments.

The sections that follow describe each
environment. Each section first describes the environment generally in
terms of history, typical applications, characteristics, and what
makes it distinct from the other environments.  This description is
followed by a more rigorous list of requirements that defines each
environment.  This set of requirements is derived from the
“architectural issues” that were gathered during stakeholder
engagement.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **No.** | **Name** | **Security** | **QoS** | **Config** | **Data Mgmt** | **Sub** | **CC** | **Field** | **Cust** | **Bus** |
| 1 | Deterministic Rapid Response Intra-Sub | | H | H |  | Y |  |  |  |  |
| 2 | Deterministic Rapid Response Inter-Site | M | H | H | H | Y | Y | Y |  |  |
| 3 | Critical Operations Intra-Substation | H | M | H |  | Y |  |  |  |  |
| 4 | Inter-Field Equipment |  |  | M |  |  |  | Y |  |  |
| 5 | Critical Operations DAC | H | M | H | H | Y | Y | Y |  |  |
| 6 | Non-Critical Operations DAC |  | M |  |  | Y | Y | Y |  |  |
| 7 | Intra-CC |  | M |  | H |  | Y |  |  |  |
| 8 | Inter-CC | H |  | M | H |  | Y |  |  |  |
| 9 | CC to ESP | H |  | M | H |  | Y |  |  | Y |
| 10 | RTO to Market Participant | H |  | M | H |  |  |  |  | Y |
| 11 | CC to Customer Equipment | M | M | H | H |  | Y |  | Y |  |
| 12 | CC to External Corporations | H |  |  | H |  | Y |  |  | Y |
| 13 | Intra-Corporation | M |  | H | H |  | Y |  |  | Y |
| 14 | Inter-Corporation | H |  | M | H |  |  |  |  | Y |
| 15 | DER Monitoring and Control | H | M | H | H |  | Y |  | Y |  |
| 16 | Intra-Customer Site | M | H |  |  |  |  |  | Y |  |
| 17 | Inter-Customer Site | H |  | H |  |  |  | Y | Y |  |
| 18 | Customer to ESP | H |  | H |  |  |  |  | Y | Y |
| 19 | HV Generation Plant | H | M | H |  | Y |  |  |  |  |
| 20 | Field Equipment and Maintenance | M |  | H | H | Y |  | Y | Y |  |

Table Summary
of IntelliGrid Architecture Environment Requirements

General ratings for Security, Quality of Service
(QoS), Configuration (Config) and Data Management (Data Mgmt)

            H = high level of requirements; M=
medium level of requirements; blank = low level of requirements

Indications of physical locations: Substation
(Sub), Control Center (CC), Field Devices (Field), Customer site (Cust),
Business (Bus)

            Y= Yes, involves communication with
that physical location.

## Basic IntelliGrid Architecture Environments

·       **[1.
Deterministic Intra-Substation](Env1_Deterministic_Intra-Substation.htm):** High speed
intra-substation environment (e.g. protective relaying, direct monitoring of
power system parameters by CTs and PTs)

·       **[2.
Deterministic Inter-Site](Env2_Deterministic_Inter-Site.htm):** High speed
inter-site (e.g. distance protective relaying, FSM)

·       **[3.
Critical Operations Intra-Substation](Env3_Critical_Operations_Intra-Substation.htm):** High
security intra-substation environment (e.g. monitoring and control of IEDs,
setting protective relay and other substation equipment parameters, …)

·       
**[4. Inter-Field
Equipment](Env4_Inter-Field_Equipment.htm):** Inter-field devices
environment (e.g. monitoring and control of IEDs on feeders, …)

·       **[5.
Critical Operations DAC](Env5_Critical_Operations_DAC.htm):** High security
between control center and field equipment environment (e.g. monitoring and
control by SCADA of substation and DA equipment, monitoring and control of DER
devices, monitoring of security-sensitive customer meters, monitoring and
control of generation units)

·       
**[6.
Non-Critical Operations DAC](Env6_Non-Critical_Operations_DAC.htm):** 
Lower security interactions among control center, substation, field equipment,
customer sites environment (e.g. monitoring non-power system equipment, less
security-sensitive substations, customer site PQ monitoring, customer metering)

·       
**[7. Intra-Control Center](Env7_Intra-Control_Center.htm):** Within
one control center (e.g. SCADA system, EMS system, ADA functions, real-time
operations)

·       
**[8. Inter-Control Center](Env8_Inter-Control_Center.htm):** Among
control centers (e.g. between utility control centers, between RTOs, between
remote subsidiary or supervisory centers)

·       
**[9. Control Centers
to ESPs](Env9_Control_Centers_to_ESPs.htm):** Between
utility control centers and ESPs/Aggregators (e.g. RTP, metering and
settlements, market operations)

·       
**[10. RTOs
to Market Participants](Env10_RTOs_to_Market_Participants.htm):** 
Between utility/RTO/ISO control centers and Market Participants (e.g. market
operations)

·       
**[11. Control Center
to Customers](Env11_Control_Center_to_Customers.htm):** 
Between customer equipment and utility control
centers (e.g. customer metering, demand response interactions, DER management)

·       
**[12. Control Center
to Corporations](Env12_Control_Center_to_Corporate.htm):** 
Between control centers and external corporations (e.g. weather data,
regulators, auditors, vendors)

·       
**[13. Intra-Corporation](Env13_Intra-Corporation.htm):** Within
corporate utility (e.g. planning, engineering, ADA access to AM/FM and customer
information systems, arena addressed by TC57 WG14)

·       
**[14. Inter-Corporation](Env14_Inter-Corporation.htm):** Between
corporate utility and external corporations (e.g. e-business)

·       
**[15. DER
Monitoring and Control](Env15_DER_Monitoring_and_Control.htm):** Between DER and ESP
(e.g. ESP as Aggregator performing monitoring and control)

·       
**[16. Intra-Customer Site](Env16_Intra-Customer_Site.htm):** Within a
customer site (e.g. building management systems, DER management)

·       
**[17. Inter-Customer Sites](Env17_Inter-Customer_Sites.htm):** Between
customer sites (e.g. microgrid management)

·       
**[18. Customer to ESP](Env18_Customer_to_ESP.htm):** Between
customers and ESPs, Aggregators, MDMAs (e.g. DER management, customer metering,
RTP, demand response)

·       
**[19. HV Generation Plant](Env19_HV_Generation_Plant.htm):** Within an
HV Generation Plant site (e.g. within the electrical and physical site of the
generating plant up to the point of common coupling with the area power system)

·       
[20. Field
Equipment Maintenance](Env20_Field_Equipment_Maintenance.htm)**:** 
Maintenance of field equipment

·       
**User Interface:** User
Interfaces and Person-to-person interactions (not technical
environments)

·       
**Special:** Special environments
...

## Example of IntelliGrid Architecture Environments

An example of three IntelliGrid Architecture environments is shown below

![](../images/Substation_Environments.jpg)
