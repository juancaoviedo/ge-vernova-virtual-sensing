# For Power Engineers

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Rec_Recommendations_PSE.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Recommendations to Power System Engineers

## Key Technologies and Practices

This section summarizes the major recommendations made in
Volume IV regarding the use of a common architecture, technologies, and best
practices.  It is not intended to be comprehensive, but to give the flavor
of the important items.  This does not rule out the use of other practices
and technologies depending on the working environment.

### Architecture Definition

It is important that the energy industry begin to develop networks
using systems architecture concepts and tools.  In particular, the
engineers within the energy industry should:

* Use **UML
  methodologies** for documenting and analyzing systems.   UML is a
  mature technology with a variety of available tools.
* Join with other
  organizations to create **reference designs** for power system
  operations.  The concept of the reference design has been used with great
  success in other industries such as telecommunications.
* **Adopt common
  language(s) and harmonize standards focused on language development.** The
  common language elements adopted and or recommended by IntelliGrid Architecture must be
  continually developed. Developing and using a common language for intelligent
  equipment operations is a key IntelliGrid Architecture recommendation. Language development and
  harmonization is one of the key strategic pathways to systems integration.
  IntelliGrid Architecture calls out prominently language development taking place within key energy
  industry standards communities, however, common language development and
  harmonization is also needed for interoperation with industries outside of
  traditional energy industry standards. These include, but are not limited to,
  residential, commercial and industrial in-building
  communications, as well as systems and enterprise management oriented
  communications with telecommunications industries.

### Object Modeling

The core of interface interoperability is the shared
definition of nouns and verbs to create a common language that can be
unambiguously understood and acted upon by intelligent equipment. A substantial
body of work is available for communications with advanced field equipment and
this work is now emerging as an International Standard under IEC TC 57
committees. Product vendors and energy industry engineers should:

·       Use **IEC
61850 object models** and services for automation of substations, including
the additions currently being developed for distributed energy resources, wind
power, and other applications.

·       Use **BACnet™**
for consumer communications within commercial and industrial in-building
networks automation. Recommended by ASHRAE, it is a leader in its field and
provides common object models. This recommendation also includes continuation
of work to integrate objects for energy related communications developed within
the IEC with the development of the BACnet protocol. This integration enables
two industries to interoperate through using a common language. This not only
leverages development work but also can reduce the need for ‘gateways’ to
translate messages between energy and building automation industries. This
recommendation can also be considered for residential network standards that
use object based communications. As noted later in the Recommendations section,
however, this is a volatile field with a multitude of worthwhile technologies
available. The immediate future of consumer access will likely focus around
common gateways or portals.

·       Use **ANSI****C12.19** for metering data. Its XML representation of data will be a part of
the 2004 release of the updated standard.

·       Use IEC
61970 and IEC 61968 **Common Information Model (CIM), Generic Interface
Definitions (****GID****), and System
Interfaces for Distribution Management (SIDM)** as common interfaces for
energy management and distribution management systems. Once these have been
harmonized with other information models, such as IEC 61850, they should be
used throughout the power system.

·       Use the **self-description**
capabilities of these technologies to enable **electronic access to metadata**.
Metadata is information about the source, format, and meaning of data. Once
this is available online, much of the cost of power systems integration will be
reduced because this information will be freely available, instead of being
either filed in multiple formats or kept in the heads of systems engineers.
Intelligent ‘agents’ or other special applications can then use the metadata to
help create cooperating plug-and-play systems, even when these systems are
developed by multiple vendors with different implementation constraints over
many years of evolving technologies.

### Security

The power industry is only starting to become awake to
security concerns.  In order to implement security in an architectural
fashion, organizations should follow a set of effective practices and implement
security technology standards to ensure the cyber security of their systems.
These practices and standards include:

·       Perform
similar levels of **formal** **risk assessment** on the vulnerabilities
of the communications network and information systems as are currently
performed on the power system itself. Implement a regular risk re-assessment
process.

·       After
analyzing security requirements based upon risk assessment, **define security
policies** based on those requirements, and implement new policies. Note that
the security implementation can sometimes decrease availability of information
from, and control of, the power system. Take this into account when designing
the combined network. It should also be noted that security policy related
requirements are being formed in key organizations, such as North American
Electric Reliability Council (NERC) and government agencies with the charter to
protect critical infrastructures.

·       Security
should be approached as part of your organizations overall security policy
implementation.  Security includes a **portfolio of strategies and
technologies** that are combined to meet the security policies of an
organization.   The technologies included and recommended in IntelliGrid Architecture analyses represent individual elements and components of an overall
security strategy.

·       Consider **open
systems standard security technologies,** such as TLS,
IPSec, PKI and Kerberos, throughout the
power system automation network, along with some specific IEC security standards
for protection relaying.

·       Focus on **security
management** such as the deployment of keys and certificates and how this
affects the organization’s processes.

·       Use **XML-based
security technologies** that integrate data management with security, such as
Security Access Markup Language (SAML) and XML Key Exchange.

### Network and System Management

Today’s automation systems are often characterized as a
collection of pilots that are limited by their existing
infrastructure.   This limitation is often traceable to a lack of
robust systems administration capabilities including network and systems
management.  As the industry seeks to scale up automation equipment to
large numbers of field devices.  Systems administration must become more capable
to enable systems that can be effectively managed on large scales.  IntelliGrid Architecture
emphasis on network and systems management reflects the challenges that come
from massive deployments.  These topics must be rigorously addressed or
the field deployments can quickly become unwieldy to manage. Network and system
management are functions commonly performed in business computing and
telecommunications, but not yet deployed extensively or completely in power
system automation.  The following are a few of the recommendations that
have emerged from project analyses. :

·      
**Expand network management into the power system communications
network** beyond the simple status reporting that SCADA systems often
perform. Begin deploying **the Simple
Network Management Protocol (SNMP)** functions (IETF RFC 1351, 3411, and
3414) or equivalent, i.e. the ability to gather statistics, receive alerts, enable and disable devices from any location in the
network. 

·       **Develop
network and systems management, security management, and power system
applications in parallel**. As systems
are specified it is important to develop requirements for network and systems
management and security at the same time as the applications.  This is
important for small resource constrained devices since the management and
security functions may drive minimum hardware requirements.  Currently,
almost all focus is on the development of power system applications only. 
The portfolio approach to system designs will help to ensure adequate
capability for managing the field equipment including the ability to run
diagnostics in remote equipment as well as managing application execution.

### Data Management Practices

Energy industry engineers are recommended to employ the
IntelliGrid Architecture to develop data management methodologies particularly for
intra-control center functions The IntelliGrid Architecture provides a
common data management approach and also recommends and discusses the merits of
different technologies and services that will help integrate a variety of
operationally focused applications such as EMS,
DMS, GIS, AMS/WMS,
OMS, CIS, and engineering applications. At the same time, IEC TC57 WG14 is
developing CIM object models for exchanging data within the control center
environment, while other standards groups are developing additional types of
data objects (e.g. graphical object models).

However, this work is only the first step toward managing
data and data exchanges within the control center environment. Different
applications from different vendors in different control centers include many
variations in data models and data exchanges, covering many different
requirements. Energy industry engineers should therefore develop tools and
practices focused on:

·       Implementation
of **IntelliGrid Architecture-based metadata management practices** for object models used
within the control centers so that the metadata is “browsable” and available
for manual data mapping procedures, as well as for use by automated data
mapping tools.

·       Utilization
of the results of the **harmonization efforts for IEC61850 device models and
CIM power system models** for both IEC61968 (distribution) and IEC61970
(transmission)

·       Handling of
**data mapping** for different applications

·       Handling of
**IntelliGrid Architecture-based data validation and synchronization** across functions

·       Development
of **role-based ‘Client views’ views’ based on IntelliGrid Architecture namespaces**: the
establishment of what data is available and permissible for being accessed by
different ‘clients’, such as applications, systems, and human users

·       Use the**IEC61970 Part 403 – Generic Data Access (GDA)** as the common application
interface for accessing metadata and data in a backend technology neutral
way.

### High-Speed Measurement

The self-healing grid will not be possible unless data is
exchanged securely and consistently in real time across much wider areas. A
number of technologies are vital to making this possible. The following are a
few recommendations for time synchronization and event communications.

·       Use **ISO/IEC
18014-1** timestamp format, permitting the creation and correlation of secure
***audit*** trails of power system events.

·       Use **IEEE
1588** for sub-millisecond time synchronization across multiple networks.

·       Use **IEC
61850-8-1** Generic Object Oriented Substation Event (**GOOSE**) protocol
for real-time exchange of power system protection and interlocking information
over LANs and WANs.

·       Use either
the **IEEE 37.118** or **IEC 61850-9-2** standards for exchanging
real-time samples of synchrophasor information across LANs and WANs.  This
will move the power system from ‘state estimation’ to simply ‘state
measurement’.

·       Use the**IEC61970 Part 404 – High Speed Data Access** - HSDA as the common application
interface for Wide Area Measurement and Control.  Note that OPC
Data Access (OPC-DA) is an appropriate COM
implementation of the HSDA as the client-server architecture fits well with the
need for multiple applications having access to real-time data as well as for
multiple applications being able to effect real-time control.
