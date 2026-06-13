# For SBOs and EPRI

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Rec_Recommendations_EPRI.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Recommendations to EPRI and Standards Organizations

## Achieve IntelliGrid Architecture’s Long-Term Goals

The recommendations to EPRI include a specific
action plan to ensure that IntelliGrid Architecture is successfully implemented. This plan
proposes specific steps be taken in the following areas:

·       Contributing
to standards development organizations and consortia

·       Sponsoring
pilot projects and field trials

·       Developing
engineering tools and notation methods

·       Encouraging
the adoption of IntelliGrid Architecture

·       Initiating
work to continue systems analysis of the utility industry in more detail

·       Integrating
IntelliGrid Architecture with other architectures

## Continually Evolve Specifications

Do not wait for standards…develop and drive
them to completion!

This section contains recommendations for
actions that can be taken by consortia and other industry groups. These groups
are vital to create consensus on interoperability issues so that formal
standards can be written. For many of these groups, they *are* the de facto
standards organization in their area. Work on some of these items is already
underway. In those cases, EPRI and other industry organizations
must try to provide resources to encourage the work.

This section recommends an action plan for
ensuring that an industry-level architecture can be successfully implemented.
Adopting IntelliGrid Architecture will require educating the general utility populace,
implementing IntelliGrid Architecture principles, developing and standardizing new needed
technologies, and harmonizing those technologies that exist and presently
overlap.

This section provides recommendations for
contributing to standards development organizations and consortia in order to:

§       Develop missing IntelliGrid Architecture technologies

§       Harmonize overlapping technologies

§      
Integrate existing technologies into IntelliGrid Architecture

§      
Ensure IntelliGrid Architecture recommended technologies are all standardized

## Develop Contributions to Standards Organizations and Consortia to Progress key Infrastructure Elements

Standards organizations and consortia make
progress through contributions that refine the standard as a result of analysis
or actual implementation. This important aspect of standards development is
often overlooked in most projects that seek to implement them. As part of the
IntelliGrid Project, Table 5 represents steps in this direction. These
recommendations must be further developed and new recommendations added as
follow-on work continues. These are some of the necessary steps to build the
components of an industry-wide architecture.

In Table
5, TC is defined as Technical Committee and WG is defined as Working
Group. Unless otherwise noted, all working groups cited belong to the IEC TC 57
on Power Systems. Some of this work is already underway, in which case EPRI’s roles should support the work.

|  |  |  |
| --- | --- | --- |
| Table 5: Recommendations for Standards Organizations and Consortia | | |
| **Recommended Action** | **Possible Group** | **Description** |
| Harmonize CIM and IEC 61850 | Ad Hoc WG07 | The IEC 61968 and 61970 Common Information Model addresses the overall power system, while the IEC 61850-7 object models address devices and functions within substations. The IEC should either merge the two object models or define a standardized mapping defined between the two. This will enable the exchange of data between systems implementing the different models, and permit the creation of configuration tools shared between EMS and SCADA systems. |
| Harmonized 61970 GID and 61850 ACSI and 61968 Messaging Model | Ad Hoc WG07 | The 61970 GID provides a way to access operational information once it has been transmitted by field communication networks.  However, how to exactly integrate 61970 with 61968 and 61850 has not been standardized.  The IEC should standardize the mechanics for **HOW** off the shelf components can be made interoperable. |
| Add missing Security for Legacy Protocols | WG3, WG15, DNP TC | The most popular serial protocols between and inside substations (DNP3, IEC 60870-5, ModBus®, Profibus) need standardized security solutions for authentication and encryption, both on LAN/WANs and serial links. The IEC should create these solutions. Adding such measures will permit utilities to continue to deploy these protocols where they are most effective without security concerns. |
| Endorse AGA 12-1 Retrofit Security | WG3, WG15 | The IEC should endorse the AGA 12-1 security standard for serial links currently being developed by the American Gas Association and Gas Technology Association. This standard defines a protocol and device requirements for ‘bump in the wire’ encryption of serial links. Endorsing this technology in the power system can reduce costs because security can be added to legacy systems without ‘forklift’ upgrades. |
| Endorse IEEE 1588 LAN Time Synchronization | WG10 | The IEC should endorse the IEEE 1588 standard for Precision Time Protocol (PTP) time synchronization over local area networks. IEEE 1588 allows synchronization down to the microsecond level which is required in applications such as SunchroPhasor Implementation of IEEE 1588 will reduce substation integration costs by eliminating the need for a separate LAN to distribute high-resolution time synchronization throughout each substation. |
| Create Security Risk Assessment and Deployment policies, procedures and metrics. | WG15, NERC, other? | The industry needs to develop process, procedures, and target metrics in regards to how security risk assessments should be applied to utilities and other power system organizations.  NERC guidelines will help to set requirements, but the procedures and policies necessary to allow the development of policies based upon risk assessment need to be developed. |
| Integrate Legacy Protocol Mapping Rules. | WG10, WG3 | The industry needs standards on how to map data from legacy protocols (such as DNP3, IEC 60870-5, ModBus, Profibus ) onto IEC 61580 and CIM information models. Providing such mappings may encourage automation of substation and field equipment configuration, reducing errors and cost. |
| Support Multicast IP. | WG10 | The IEC should expand on the Generic Object-Oriented Substation Event (GOOSE) and Sampled Measured Value (SMV) protocols to permit their use in wide-area networks using multicast IP addresses. This will permit the centralization of protection algorithms over wide areas and the distribution of phasor information in real-time to control centers. Application on VLANs should also be considered |
| Secure GOOSE and SMV | WG15, WG10 | The IEC should develop a standard mechanism for securing the high-speed GOOSE and SMV protocols between sites so they can be carried over organizational boundaries. This work is in the proposal stage. |
| Unify Utility Enterprise Management | WG12, WG13, DMTF | The IEC 61968 and IEC 61970 Common Information Models are missing information on enterprise (i.e. network or system) management. In addition, the IEC CIM should be integrated with work outside the power industry, in the Data Modeling Task Force (DMTF). The DMTF also has a CIM, which does not contain power system information yet. Harmonizing these two models will help to harmonize utility control network and corporate IT operations. |
| Harmonize Utility Security Management | WG10, WG15, WG13, WG14 | There are currently no power system object models for managing security, i.e. detecting intrusions, logging user accesses, enabling or disabling security associations. The IEC should add these models and harmonize them with those of enterprise management (separate item). Creation of standard models will enable standardized tools for security management and smooth integration of security systems across the industry. They could lead to a nationwide ‘utility security dashboard’, as envisioned by the Department of Homeland Security. |
| Extend Power System Configuration Language | WG10 | The existing Substation Configuration Language (SCL) defined by IEC 61850-6 addresses only substation devices. The IEC should expand the scope of this schema to include all types of power system equipment and concepts from the Common Information Model (CIM). Such an expanded configuration language would enable shared simultaneous configuration of various levels of masters and data concentrators within the power system. This would reduce cost and improve reliability of system upgrades, especially across organizational boundaries. |
| Create standards for Data Warehousing |  | The IEC should develop standards for a set of interfaces for gathering data from multiple data warehouses (data integration) containing metering data, asset information, etc. The groundwork for this capability has been laid in the IEC CIM, but it needs to be clarified. This work can enable the creation of ‘CEO Portals’ that can display real-time summaries of the working state of a utility, enabling better reliability, safety, and customer response. |
| Harmonize and Integrate OpenGIS® for Utility Industry | Expand scope of WG14? | The IEC should endorse and integrate the work of the OpenGIS Consortium (OGC) into the utility industry, especially distribution automation. This will standardize the power industry information models with Geographical Information Systems developed for other industries, notably the telecommunications industry and other utilities. Eventually, this will enable multi-utility displays that can be shared across organizational boundaries, encouraging cooperation between organizations in emergency situations. |
| Standardize Device Documentation |  | The IEC should standardize formats for providing documentation on intelligent power system devices. This type of standardization will reduce costs and errors in making equipment changes by encouraging the development of advanced management and administration capabilities. |
| Harmonize Power Industry eCommerce | WG16 | The IEC should standardize the means by which existing eCommerce initiatives can be integrated into the power industry. Both wholesale and retail markets need to be addressed; they will likely involve different procedures and possibly different technologies. Guidelines should be provided on when wholesale or retail rules apply. |
| Standardize Broadband over PowerLine | IEEE | EPRI should encourage the work that is beginning on standardizing broadband communications over power lines. This will simplify the choice of multiple existing technologies and facilitate many of the future consumer use cases predicted by IntelliGrid Architecture. |
| Standardize Security Revocation Server | IETF | The current CRL and OCSP technologies are polling (e.g. request/response) based.  There are performance and timeliness issues that are caused by the size of CRLs and the polling intervals.  The power industry needs a server that can be deployed within a security domain that has a knowledge of the certificates that are in use and which applications/entities use those certificates.  The revocation server would then alert those entities if the certificate were revoked. |
| Create Security Audit Record Format | W3C® | There is currently no standard that defines the contents of an Audit Record.  There needs to be a standard developed whose semantic content is extensible. |
| Create Security Audit Record Retrieval | W3C, OASIS | There is currently no standard mechanism for retrieving audit records.  An abstract service needs to be defined to provide this capability.  This service then needs to be mapped to various technologies (e.g. Web Services, IEC 61850, etc.). |
| Add Security: SAML Extensions | OASIS | There is no mechanism for an entity to determine how many credential conversions have occurred to provide the credential that is being provided.  The SAML attributes need to be extended so that the chain of identity/credential mappings can be determined in order to facilitate the security Quality of Identity service. As part of this work, there needs to be a mechanism to determine the actual chain of credentials.    SAML also needs to be extended to support other credential types (e.g. address and username/password). |
| Add Security: Password Renewal | IETF | There is no standardized mechanism, similar to PKI renewal, to allow password renewal and management. |
| Create Security: Quality of Security Service | IETF | The Quality of Service concept (e.g. to facilitate routing based upon cost/performance) needs to be extended to allow security to be used as part of the routing path determination. As part of this work, security metrics need to be defined in a standardized manner. |
| Add Security: Communication Path definition | IETF | The source routing option in IPv4 and IPv6 allows the packet recipient to know the hops/routes that the packet has taken.  However, there is no mechanism for the sender of the packet to specify a particular path. This capability is needed in order to allow ‘secure’ and specific communication paths to be defined via software configuration. |
| Create Security: Service Discovery | OASIS | Currently there is no mechanism for determining what security services are available for use.  A standardized abstract API/service needs to be developed to allow peers to determine the security services available by their peer.  WS-Policy should be extended to allow this. |
| Extend Self-Description for existing protocols | DNP User’s Group, ModBus IDA, Profibus Trade Org. | Develop and adopt additions to existing protocols that will enable self-description and other services similar to that found in IEC 61850. This may include developing XML schemas for configuration that are compatible or integrated with IEC 61850-6 Substation Configuration Language.  This will reduce installation costs improve reliability and safety due to easier integration with IntelliGrid Architecture systems. |
| Extend Security for existing protocols | DNP User’s Group, ModBus IDA, Profibus Trade Org. | Develop a security scheme for securing DNP3, preferably one in common with IEC 60870-5, as discussed in the previous section. Develop security schemes for other common protocols. This covers security ‘holes’ in the communications networks that are currently addressed by specific existing protocols. |
| Create Reference Designs | Various | Create ‘reference designs’ for particular domain areas, such as a Consumer Interface, Demand Response, See discussion in Section 0for explanation. This will speed implementation of new utility applications and technologies. |
| Develop Consumer Portal | ASHRAE®, BACNet®, UPnPTM,Home Plug Alliance, other vendors | Develop common object models, a reference design, and pilot projects for connecting consumer devices to the power system communications network. This will resolve overlap and confusion in consumer device protocols by designing a common point of connection to the power industry. |
| Create Demand Response Object Model | UCA International User’s Group | Develop common object models for performing Demand Response. The UCA International User’s Group can serve as a clearinghouse for this effort, which involves many consortia and standards bodies, including W3C, IETF, OASIS, IEC, IEEE, industry vendors. This will reduce industry ‘churn’ in developing access points for this application. |
| Develop Security Policies | IEC, NIST, ISA, NEMA®, DHS, AGA | Develop a security policy best practice document that includes processes and metrics to be evaluated.  This document would also contain information in regards to how to perform risk assessment. This allows entities to follow similar steps ensure key assets are secured properly. |
| Improve Security Education | IEC, NIST, ISA, NEMA, DHS, AGA | A cohesive and coordinated set of educational seminars should be created to discuss the various aspects of security and its implementation.  One of the prevalent issues is that often seminars offer opposing and conflicting ideas. This will facilitate ongoing, non-conflicting education/training. |
| Extend Revocation Server | IETF | The IETF should develop a specification for a central Security Domain revocation server (not a CRL server) with the following attributes:  §   Allows certificate users to register that certificates are in the user certificate cache.  §   The Revocation Server would query the CAs CRL servers and process the revocation list(s).  §   Based upon the CRL processing, the Revocation Server would notify the certificate user that the particular certificate has been revoked.  §   Optionally, such a Revocation Server could alert Security Domain management that a certificate of a particular user is about to expire so that corrective action could be taken.  §   Optionally, such a Revocation Server could respond to OCSP requests so that newly configured certificates could be validated as still being valid.  It is believed that work on such an entity is needed to allow more timely delivery of revocation information and to allow automation of such tasks. |

### Bring Forward Object Based Communications Models

Several of the recommendations listed involve the
development and standardization of object models. EPRI should take the lead in
encouraging and providing resources for the development of these object models,
using the excellent methodology pioneered in the current EPRI DER/ADA project. This methodology
covers:

§      
Initial drafts of object models (using the appropriate IEC61850 and/or
CIM templates) using vendor information

§      
Analysis of the current and future data requirements, based on
analytical studies and critical Use Cases

§      
Use of these data requirements to update the draft object models

§      
Mapping updated object models into software tools which conform to
appropriate standards, in order to validate the object model conformance

§      
Developmental laboratory tests to verify that the analytical studies
have determined the sufficient set of data, which includes all necessary data
items, but does not include extra or unnecessary data items

§      
Field tests to verify the laboratory tests under actual conditions

§      
Submittal of these vetted object models to the appropriate standards
body

§      
Follow through with the standards bodies to support adoption of the
object models as standards

§      
Support to stakeholders to ensure implementation and deployment of the
standard object models

### Recommendations for Continuing IntelliGrid Architecture Research

Recommendations
for Smart Toolset to Maintain IntelliGrid Architecture Over Time

The previously discussed systems engineering
approach has been rigorously used during the development of IntelliGrid Architecture. To deal with
such an overarching architecture development, the team has adopted the
Reference Model of Open Distributed Processing, ITU-T Rec. X.901 | ISO/IEC
10746-1 to ITU-T Rec. X.904 | ISO/IEC 10746-4, commonly referred to as RM-ODP
standard framework as a conceptual guideline. RM-ODP
provides an excellent conceptual framework that has been accepted by the Object
Management Group (OMG) and others for
providing a complete characterization of the enterprise.

By design, RM-ODP
does not provide any notation and method; IntelliGrid Architecture team has not been able to
identify suitable commercial tools that directly support its concepts.
Rendering and representing architectures remains the subject of significant debate;
there is no widespread consensus on how it should be approached. Therefore, a
discussion on tool selection is central to architecture development.

The tools used for developing IntelliGrid Architecture
framework can also be used to expand it and develop applications based on it.
However, developing a *smart toolset*, such that it correlates, discovers,
and recovers architecturally relevant solutions when provided with a new set of
requirements will greatly enhance the usability of IntelliGrid Architecture. This can be based on
on-going research in language processing, artificial intelligence and knowledge
discovery[[8]](Rec_Recommendations_EPRI.htm#_ftn8).
The team recommends development of *smart toolset* to increase the
usability and applicability of IntelliGrid Architecture.

Construction of such a toolset would encompass:

§      
Absorbing the contents of the ISO2004[[9]](Rec_Recommendations_EPRI.htm#_ftn9) for mapping RM-ODP
to UML. This would allow accommodating a deeper and emerging standard mapping
to RM-ODP.

§      
Revising the UML model of all import data to this extended mapping

§      
Migrating IntelliGrid Architecture import and analysis tools to XML and adding some
consistency validation to the word editing process (text sections and
spreadsheet) -- this can include what has been done as a manual normalization
process today.

§      
Producing a cookbook and necessary toolset to allow IntelliGrid Architecture process of
Domain Template => UML import and normalization process to be replicated by
interested and independent groups.

Research
the Impact of Communication Failures on Power System Design

Determine how failures in the communications
system itself can impact the stability and reliability of a next generation
power system that depends upon it. What are the types of failures, including
equipment failures, operational failures, errors, deliberate attacks, etc.?
What are the communication failure mechanisms and mitigation strategies when
such failures occur? What are the impacts of the initial communication failures
on power system operations? What are the impacts of the failure management
strategies, such as alternate paths, failover of equipment, etc on power system
operations?

Study
Strategies on Managing Disparate Technology Life Cycles

Communication technologies, with life cycles varying
from months to years, change far more rapidly than the power system equipment
with life cycles of years to decades. Communication technologies often involve
continuous version updates and software patches that may or may not be
thoroughly tested – especially considering that software gets better with age.
What strategies are needed to manage these disparities? How can users be sure
of the degree of testing that has been performed? What degree of assurance is
needed for different functions?

Research
on Distributed Control Strategies

Research should be undertaken to measure the
stability and effectiveness of distributed control strategies in real-time and
over larger periods of time. Distributed control strategies include closed-loop
local and wide area, distributed and central control concepts. No matter what
the underlying communications architecture and specific technological
implementation, it needs to be demonstrated that use of the IntelliGrid Architecture
to achieve a variety of local and globally optimized control strategies is
possible. Research must be done to identify those implementations that are
feasible, stable, cost effective, and enhance rather than diminish the power
system reliability – a danger if the architecture and strategies are too complex.
For example, control theory needs to be extended to deal with distributed,
probabilistic response functions and the relative improvement in performance
based on wide-area vs. local feedback measurements. Wide-area control
strategies need to be simulated and perfected off-line before they are applied
on a ‘live’ power system.

Development
of High-Speed Authentication/Encryption Technologies

It was suggested in Table
5 above that standards bodies consider development of encryption technologies
for high-speed device to multi-device communications (as will be required for
sending phasor data from one measurement site to multiple subscribing hosts).
It is to be noted that although this is a goal, the required level of
technology is not available today. Specifically, an encryption technology is
required on a point to multi-point message that will not slow down the delivery
of the message.

Migration
and Maintenance of IntelliGrid Architecture Website

For IntelliGrid Architecture to have visibility, the information
captured and developed during this project must be readily available to all
interested parties. In addition, as the final deliverable is primarily being
presented in electronic format, IntelliGrid Architecture.org website must be migrated to a
final server and maintained on a consistent basis. It is a strong
recommendation that this task be undertaken as soon as possible. The site
should be designed for ease of navigation with links to the primary
functionality of IntelliGrid Architecture being visible on the home page. Also to be included are constructs
to solicit comments and easy access to the various tools that were developed
during the course of the project (including a link to the Magic DrawTM Viewer).

Develop
an IntelliGrid Architecture Users Guide

Although IntelliGrid Architecture Report provides a general
guideline to assist different users in utilizing IntelliGrid Architecture results (discussed
earlier in this volume), a complete Users Guide could provide more details and
more examples. In addition, an accompanying IntelliGrid Architecture seminar would provide
individual support for different groups of users.

The IntelliGrid Architecture Users Guide would provide detailed
procedures for using IntelliGrid Architecture for each of the different types of users: power
system planners, project engineers, information specialists, regulators and
advisors, and standards developers. It would also include extensive examples of
how the main IntelliGrid Architecture deliverable could be utilized to develop concrete equipment
and systems design specifications for implementations of IntelliGrid Architecture. This
document would foster the necessary peer review of IntelliGrid Architecture deliverable and its
implications on the design of the power system of the future. The results of
such stakeholder review and comment would be used to focus and direct IntelliGrid Architecture
follow on R&D that takes the next step and works to recommend a concrete
set of design specifications and test implementations.

The IntelliGrid Architecture User’s Guide would be a key part of
IntelliGrid Architecture workshops discussed in section 6.6.5 below.

Develop
Reference Design for Advanced Distribution Automation (ADA)

Multiple projects within and outside of EPRI are
underway, which involve advanced distribution automation (ADA) and other
automated distribution operations (ADO).
This area of utility operations, as indicated in IntelliGrid Architecture project, has become
increasingly critical for future power system operations, as distributed generation
becomes more widespread, market forces call for demand response capabilities,
energy is becoming less easily available and therefore more expensive, and
financial pressures are requiring more efficient energy transmittal operations.

At the present time, a few isolated
implementations of portions of ADA are being undertaken by utilities. However, a
full reference design including implementation procedures toward the
distribution system of the future has not been developed. Presently, there is no
consortium to address ADA; this could be resourced through EPRI.

The following steps are recommended to develop
and build on a reference design for ADA.

§      
Develop roadmap for ADA studies and projects toward the distribution
system of the future, using expert opinion and stakeholder inputs

§      
Develop the actual reference design, coordinating across groups which
are involved with different aspects of ADA to work toward common goals,
including utilities, vendors, integrators, regulators, etc.

§      
Support ongoing studies, pilot projects, and system-wide projects
involving ADA to ensure compliance with the roadmap. Some are discussed in
section 6.6.4 below.

§      
Support periodic updating of the ADA reference design.

Applying
the IntelliGrid Architecture to Legacy Systems

The need to integrate legacy systems is far more
common than building systems from scratch, and the legacy system integration
process is by far more complex. The IntelliGrid Architecture discusses
these integration issues, but additional Use Cases, specific application of IntelliGrid Architecture recommendations to these Use Cases, and benefit-cost analysis of these
recommended technologies in different legacy systems situations are needed to
provide the supplemental information for information specialists to address the
problems of their own legacy systems.

Since different types of legacy systems usually
present unique problems, seminar material could be developed to cover different
types of legacy systems, with experts presenting these seminars to different
groups.

Develop
Metadata User’s Guide

One of the most challenging issues with data
management is the fact that different data is needed by different applications.
In addition, these needs vary from implementation to implementation, and in the
same implementation over time. Using common information models and common
interfaces is a major contribution to solving this problem. The technologies
recommended in IntelliGrid Architecture, such as CIM, GID, and
the IEC 61850 object models, provide mechanisms for
self-discovery of the metadata describing the data that is available in the
network. However, a User’s Guide is necessary to explain to implementers how
best to make use of the metadata and self-description concepts, both to publish
data and to find the data that is needed. Such a User’s Guide should explain:

·      
Methodologies for categorizing data within servers

·      
Techniques for making use of multiple hierarchies of data in order to
determine the meaning of data that is not yet part of a common information
model.

Research must be done to identify what analysis
and decision support applications are required to facilitate the creation of a
self-healing grid. For example, real time analysis and decision support
applications that fuse data from power system security analysis with asset
management applications.

These data management methodologies should be
used as the basis for the intra-control center testbed
project described below.

### Recommendations for deployments and construction of reference implementations

Key
reference designs

A *reference design* is a document
describing the design of a system in generic terms. Multiple vendors can use
this single generic design to create their own particular implementations that
have value-added features but that are nevertheless compatible with each other.
For instance, cell-phone vendors have produced reference designs for the next
generation of phones.

The benefit of a reference design is that it
reduces the time to develop and deploy a technology within an industry because
the common elements of the system are only designed *once*. A vendor using
a cell-phone reference design need not research the components necessary to
make a new phone compatible with the network, but can focus on meeting specific
market needs.

The IntelliGrid Architecture team recommends that power industry
consortia develop reference designs in the following areas that represent new
power utility applications:

·      
Consumer interface, and in particular a Consumer Portal device (see next
section)

·      
Control and monitoring of Demand Response (Real-Time Pricing)

·      
Control and monitoring of Distributed Energy Resources

·      
Organization of Micro-grids

·      
Energy marketing and trading

The IntelliGrid Architecture use cases captured in these areas can
be used as starting points for the reference designs.

Consumer
Portal

The consumer interface and the home automation
portion of the power industry are in significant flux at the moment. There are
a huge number of different ‘standards’ being promoted by different
organizations and vendors, with the result that there is very little
interoperability.

This lack of standards (or surplus of standards,
depending on your point of view) is a barrier to the development of important
industry applications such as real-time pricing, demand response, micro-grids,
and centralized building automation.

The IntelliGrid Architecture team recommends that resolution to
this problem focus around the concept of a ‘consumer portal’, also known as a
gateway or aggregator. This portal would be able to convert from various
technologies that are used on a customer site, to a common object model and a
smaller set of technologies (or a standard link between new technologies and
the internal workings of the consumer portal) that would be used to connect the
portal to the utility network.

The steps in this development should be:

1.             
Develop common object models for various consumer devices. These models
would include objects for meters, sensors, controls, appliances, and so on, as
well as an object model for the consumer portal itself.

2.             
Identify and prioritize requirements for the portal itself, starting
with the capability to implement the object models for a variety of devices.

3.             
Work with industry consortia to select a technology subset to enable
connecting the consumer side to the energy infrastructure (e.g. power line
carrier technologies, XML based transactions and object models, financial
transaction models, etc.)

4.             
Create a *reference design* (see the previous section) for the
portal that vendors can use as a starting point for building one. A key part of
this design should be that a portal could be embodied on a number of different
platforms, such as an appliance, a meter, or as a separate stand-alone device.

5.             
Work with appliance vendors to develop IntelliGrid Architecture-enabled appliances, either
directly or through a portal.

6.             
Encourage pilot projects to demonstrate the technology.

*7.*Create application notes based on the pilot projects so that
subsequent projects can deploy the technology better and faster.

Recommended
Field Trials and Pilot Projects

This section provides recommendations for
sponsoring pilot projects and field trials in order to:

§      
Illustrate key IntelliGrid Architecture architectural principles.

§      
Demonstrate interoperability between IntelliGrid Architecture devices and systems.

§      
Develop missing IntelliGrid Architecture technologies.

§      
Develop wrappers, gateways or translators
important to the success of IntelliGrid Architecture.

§      
Validate IntelliGrid Architecture work in real-world environments, and provide feedback
to EPRI on IntelliGrid Architecture process.

In general, IntelliGrid Architecture team recommends that
EPRI and other cross-industry
organizations monitor projects that are being initiated by utilities,
governments, and regulators, and try to introduce IntelliGrid Architecture architectural concepts
and technologies into these projects. A wide variety of such projects are being
initiated in response to the September
11, 2001 terrorist attacks and large-scale blackouts. Initiators
include:

§      
U.S. Department of Homeland Security

§      
U.S. Department of Defense

§      
Independent system operators

§      
State research and development agencies

This section provides a summary of proposed
trials and projects. Subsequent sections provide more description of the
projects.

  

|  |  |  |
| --- | --- | --- |
| Table 6: Recommended IntelliGrid Architecture Field Trials and Pilot Projects | | |
| Project Name | Purpose | Highlighted Concept(s) |
| Eastern Interconnect Phasor Project( | Develop a system of Phasor Measurement Units and associated communications that span the eastern grid | Selection of recommended communication technologies; view of future closed loop control needs |
| Utility Operations Test Bed | Establish a facility that can be used to test IntelliGrid Architecture concepts, and demonstrate several new applications that cross environment boundaries. | Prioritize and implement relevant IntelliGrid Architecture environments. Provide the needed test/certification process required. Previous test beds have focused only on a few environments. |
| DER/ADA Field Trials | Demonstrate specialized advanced distribution automation and Distributed Energy Resources devices/ functions using standardized object models in a real utility/industrial environment. | Implementation and acceleration of object model technologies and ADA algorithms. Highlights IntelliGrid Architecture major conclusion of need for a ‘common language’. Links, expands and accelerates the work already in progress. |
| Harmonized Common Object Models | Demonstrate the benefits of a harmonized 61850, 61968, and 61970 object model. | Highlight IntelliGrid Architecture recommendation for the use of Object Modeling and enable IntelliGrid Architecture ‘backbone’ common information model. |
| IntelliGrid Architecture-based GIS/DMS Integration | Demonstrate linkage of IntelliGrid Architecture with commercially available Geographical Information Systems (GIS) and DMS applications. | Integration of applications to provide the new integrated services of real-time asset management and equipment monitoring. |
| CEO Portal | Demonstrate that one can use commercially available tools with an IntelliGrid Architecture-based architecture to quickly create a website that displays summarized real-time data from an IntelliGrid Architecture network. | Use of IntelliGrid Architecture concepts; Application of recommended architecture and technologies to provide a centralized, integrated data retrieval service. |
| Object-Oriented Risk Management | Demonstrate the benefits of performing Risk Management using IntelliGrid Architecture-based data integration. | Demonstrate ability to integrate data models; demonstrate ease of implementation using standard tools; provide a vital but missing power system function in risk management. |
| Phasor Assisted State Estimation/ State Measurement | Demonstrate that synchrophasor information can be gathered from a variety of devices to augment and/or measure system state data from all desired portions of a network. Demonstrate that this leads to improved reliability in simulated emergency situations. | Meet advanced functional requirements identified by IntelliGrid Architecture, especially in the Contingency Analysis realm; Apply architectural solutions. |
| Wide-Area Protection and Control | Apply IntelliGrid Architecture vision to the architecture for a Wide-Area protection scheme / liaison with Fast Simulation and Modeling. | Apply the requirements gathering process identified in IntelliGrid Architecture; apply existing requirements; apply architectural recommendations |
| Cross-Organizational Trust Management | Develop a demonstration of security technologies to permit cross-organizational control of power equipment. | Highlight and test the security technologies defined in IntelliGrid Architecture |
| Security Challenge | Demonstrate the use of IntelliGrid Architecture security technologies to secure a particular communication link. Identify areas requiring improvement. | Highlight and test the security technologies defined in IntelliGrid Architecture. |
| Independent System Operators  Architecture Board Liaison | Develop a close liaison with the national ISO Architecture Board | Promulgation of IntelliGrid Architecture vision and architecture concepts |
| Real Time Pricing Architecture Development | Develop a standard ‘model’ of a Real Time Pricing architecture | Create IntelliGrid Architecture recommendations into a document that can be a model for utilities and regulatory bodies across the country |
| GridWiseTM Coordination | Provide technology transfer into the DOE sponsored GridWise Alliance architecture project | Enable re-use of IntelliGrid Architecture tools, processes, observations, and recommendations |
| Meta-Data | Test the use of IntelliGrid Architecture-based Meta-Data User’s Guide to demonstrate new information models. | Use of self-description and common information models |
| Inter-Control Center Data Management | Implementing common object models and IntelliGrid Architecture-based metadata access methods between control centers. | Further testing of the common IntelliGrid Architecture and access to information models discussed in the Harmonized Object Models project. |

Eastern
Interconnect Phasor Project EIPP

The Eastern Interconnect Phasor Project (EIPP)
has as its objective the establishment of a network of Phasor Measurement Units
(PMUs) throughout the eastern US power grid that are
networked via Phasor Data Concentrators. Present implementations are based on a
communication protocol developed in 1988, which was designed to enable the
necessary phasor data to be exchanged on existing 4800 bps communication lines.
The proposal is to work with the Standards task force of the EIPP and to
recommend architecture solutions based on IntelliGrid Architecture

Utility
Operations Test Bed

As the utility grid is required to be ‘highly
available’, it is necessary to thoroughly test new technologies in environments
that closely resemble the actual operating conditions found in the utility
enterprise. To meet this requirement, the recommendation is made to create a
Utility Test Bed that can simulate these environments. The test bed would be
configurable and adaptable to the environment/technology under test, and to be
able to simulate as many of IntelliGrid Architecture environments as possible. This
recommendation should be coordinated with NERC and the U.S. Department of
Energy.

DER/ADA Field Trials

In parallel with IntelliGrid Architecture, work sponsored by
EPRI is ongoing to develop standard object models for Distributed Energy
Resources (DER) in existing and future
scenarios using Advanced Distribution Automation. It is recommended that the
field trials be covered by IntelliGrid Architecture umbrella, - that is, that all aspects of
the field trials be viewed with regard to the overall architecture concept –
and that these trials expand their scope to focus on the actual ADA functions
and algorithms as well as object models. As such, consideration of
interconnection with the various utility control and monitoring centers be
considered.

Before executing these field trials, it is
necessary to develop an Advanced Distribution Automation reference design, as
discussed above in this section.

Harmonized
Common Object Models

In as much as one of the primary recommendations
of IntelliGrid Architecture is the use of Object Models as the common denominator in IntelliGrid Architecture
profile, the harmonization of the models described in IEC 61850, 61968, and
61970 is required. To achieve this goal, coordination of this effort is
suggested as a follow-on activity. This activity would entail identifying the
commonalities and defining the linkages (such as the linkage between a current
transformer and the measurement of a current)

IntelliGrid Architecture-based
GIS/DMS Integration

Demonstrate the benefits of an IntelliGrid Architecture based
architecture to perform real-time equipment monitoring when displayed in a
user-friendly manner. Use a commercial GIS
and existing EMS or DMS applications and
connect the two based on IntelliGrid Architecture architectural principles in a demonstration of
how ‘off the shelf’ applications can communicate in a standard manner, to
perform asset management of primary equipment over a large geographical area.
The demonstration would compare real-time equipment monitoring data with
nameplate specifications, location, and network location to visually display
asset status.

CEO
Portal

Using the IntelliGrid Architecture and ‘recommended
technologies’ list, demonstrate that one can use commercially available tools
to quickly create a website that displays summarized real-time data from an
IntelliGrid Architecture (object based) network, tailored to different users with different
interests. Ideally display data from a number of different database
technologies, historians and/or data warehouses as
well as demonstrating the ease of migrating object based data into data
warehouses and historians.

Standards
Based Power System Risk Management

Demonstrate the benefits of performing Risk
Management using in IntelliGrid Architecture based integration infrastructure. As some of the
needed financial data objects do not yet exist, part of the task would be to
demonstrate how new financial objects could be developed and test the process
for submitting them for standardization as part of CIM or 61850.

Phasor
Assisted State Estimation/State Measurement

Room for improvement exists in solving the state
estimation problem. Present implementations suffer from poor solutions under
lost data scenarios and ‘loosely coupled’ system topologies. Phasor assisted
augmentation of State estimators has been undertaken, however, further
work/migration to State Measurement is needed. A demonstration is proposed to
show that synchrophasor information can be gathered from a variety of devices
to augment and/or measure system state data from all desired portions of a
network. Show that this leads to improved reliability in simulated emergency
situations. This work would most likely require upgrading an existing utility
communication network (using IntelliGrid Architecture recommended technologies) to accept higher
volumes and speeds of data.

Wide
Area Protection/Control (FSM Collaboration)

A major component of the Self-healing grid is
the ability to dynamically protect and control the electric grid. In a
follow-on effort, EPRI is sponsoring work in a Fast Simulation and Modeling (FSM)
project. It is recommended that a liaison be established with the FSM
project to enable assimilation of IntelliGrid Architecture concepts into the FSM
work. It should be noted that IntelliGrid Architecture provides a sound starting point for
requirements for the FSM function. It is
expected that as FSM migrates into the
demonstration phase, the improved reliability benefits from wide area
protection and control will become obvious.

Cross-Organizational Trust Management

As more of the
electron enterprise is incorporated into the utility communication network, the
need increases to demonstrate how IntelliGrid Architecture application and security technologies
can be used to permit cross-organizational control of power equipment. The
proposed task would be to develop an emergency scenario requiring participation
and control of the power system by multiple energy organizations, including
authentication and establishing a ‘chain of trust’. Implement the scenario
using IntelliGrid Architecture technologies.

Security
Challenge Demonstration

Demonstrate the use of IntelliGrid Architecture security
technologies to secure a particular communication link or set of environments.
Identify areas requiring improvement. Build a secure system on the Utility
Operations Test bed, issue a ‘hacker challenge’ and
invite a NERC red team evaluation of the network.

ISO
Architecture Board Liaison

During the stakeholder engagement process, it
was discovered that the Independent System Operators throughout the country
have established a national ‘architecture’ group that looks at communication
issues throughout the ISO locations around the country. It is proposed that a
liaison be established with this architecture group to provide education on the
results of IntelliGrid Architecture and to provide guidance as to the application of the results.
Input would be made through involvement in teleconferences as well as
attendance at group meetings.

RTP Architecture Development

Many utilities, public utility commissions, and
energy commissions are working toward developing a Real Time Pricing (RTP)
system architectures in order to better manage the supply and demand of
electricity. It is desirably that nationally, if not internationally, that a
common architecture be applied to this solution. It is recommended that a
‘model’ of an RTP architecture be developed
and be made generally available to the industry. In addition, there is much
opportunity to bring the cross-domain concepts of IntelliGrid Architecture to bear on the creation
of the ‘big picture’.

GridWise Coordination

The GridWise Alliance
is a DOE sponsored effort to further the development of an architecture,
similar to IntelliGrid Architecture, which provides a reference model and guidelines for
stakeholder communication and decision-making. GridWise
also recognizes the need for an overarching initiative to provide perspective
to these efforts as contrary approaches may lead to confusion and duplication
of efforts. It is proposed that tight coordination with the GridWise
Architecture Board be established so that the results of IntelliGrid Architecture can provide a
foundation for any architecture work that GridWise
may undertake.

### Recommendations for stakeholder outreach

Ongoing stakeholder outreach is critical for
ensuring successful implementation and adoption of IntelliGrid Architecture. In addition to
getting the end product into the hands of those who will be building equipment
and systems utilizing the architecture, it is essential to extend and build
upon the stakeholder outreach conducted during the requirements gathering and
development phase. This is necessary to continue collecting additional use
cases to support expansion of the architecture as well as ensure awareness and
acceptance of it.

Conducting effective stakeholder outreach to
potential implementation targets, as well as the various stakeholder publics,
will facilitate adoption and implementation as well as reinforce the perceived
merits and benefits of the architecture. This can help to inform and obtain
support from individuals who may not be directly involved in implementation,
but who can aid in getting IntelliGrid Architecture before regulators and standards making
organizations.

Key goals for the ongoing stakeholder
engagement process include:

§      
Establish and build an IntelliGrid Architecture as a brand name within the electric power
industry – e.g., ‘IntelliGrid Architecture Inside’

§      
Educate audiences on what IntelliGrid Architecture is and why it is needed

§      
Provide timely, accurate information on IntelliGrid Architecture development and
implementation process and scope to stakeholders and other interested parties

§      
Facilitate awareness of what IntelliGrid Architecture is (and what it isn’t)

§      
Facilitate stakeholder awareness, understanding, and buy in of IntelliGrid Architecture

§      
Bring to the table and discuss concerns and issues that audiences may
have about IntelliGrid Architecture and implementing it

§      
Establish dialogue and facilitate public involvement in the
implementation of IntelliGrid Architecture on a national and international level and within the
various stakeholder groups – utility personnel, vendors, regulators, standards
making organizations

§      
Provide a consistent baseline message to all the stakeholder groups and
the general public

§      
Facilitate the implementation of IntelliGrid Architecture within the EPRI community

§      
Provide a support mechanism for implementation of IntelliGrid Architecture through training
programs and ongoing support via a users group

§      
Lay the basis for IntelliGrid Architecture to be incorporated into standards and
regulations – ideally as a whole but probably either in pieces or as an example
of best practices

Effective stakeholder outreach lays the
foundation for implementing IntelliGrid Architecture out in the field. Ongoing information
dissemination and education/tech transfer will reinforce stakeholder outreach
conducted during the development phase and maintain support for the end product
and its implementation. Targeted audiences for these efforts include:

§      
**Utilities:** There is a definite need to educate utility employees
on the vision and value of IntelliGrid Architecture; create buy-in of the concept with utility
executives; and engage key employees (managers and technical leaders) regarding
the architecture to facilitate its adoption and implementation.

§      
**Regulators and Auditors:** Regulators and auditors have an interest
in ensuring that power systems meet their reliability, performance, market, and
financial obligations. There is a need to assist regulatory commissions in
understanding the nature and need for an industry-wide architecture and the
benefits of implementing IntelliGrid Architecture.

§      
**Vendors and Suppliers:** Vendor stakeholders are interested in
designing, building, integrating, and servicing products that would effectively
become a part of the implementation of IntelliGrid Architecture. These individuals would be
adopters of the architecture specifications and associated standards. The
purpose of outreach to this audience is to raise awareness and obtain buy-in
and acceptance. Many vendors participate in standards bodies and IntelliGrid Architecture must be
presented in the context of building upon existing standards development work.

§      
**RTOs / ISOs**: Regional Transmission Organizations and Independent
System Operators are responsible for the real-time dynamic operation of the
electric power grid. There is a need to continue outreach to gain acceptance of
the scope and concepts of IntelliGrid Architecture project. This is an audience sector similar
in scope and purpose to utilities.

§      
**Industry Groups:** Industry groups include utility associations and
organizations, customer representative groups, users groups, standards organizations,
technology development associations, and other groups involved with energy and
technologies. There is a need to build awareness and gain acceptance and
support of implementation from industry groups such as the Edison Electric
Institute, UCA Users Group, DNP Users Group, ModBus Users Group, NERC, GRI,
APPA, ASHRAE, SEMI, 24/7 Group, etc. who
represent important sectors of the energy, electric power, related and
supporting industries. These groups will play a large part in generating a
favorable reception to the implementation of IntelliGrid Architecture by facilitating industry
sector ‘buy-in’.

§      
**Government Institutions:** Government institutions are looking to
the utility industry to develop its own solutions to the new demands of
deregulation, security, and enabling technologies. The technologies need to be
founded upon existing standards and industry-at-large solutions where possible,
but also through the development of architectures and roadmaps that address the
unique requirements of energy systems. The governmental institutions need to
feel comfortable that IntelliGrid Architecture will meet the societal obligations of a reliable
and safe power infrastructure, the financial obligations of a fair and strictly
managed electricity market, and the security obligations for a robust and
flexible information infrastructure able to meet future challenges. The goal of
engaging this audience is to educate about the needs and issues of the national
power grid as well as to gain acceptance of IntelliGrid Architecture from influential agencies or
commissions. Government organizations are likely to become a driving force for
change and thus, once educated about IntelliGrid Architecture, will push
for national acceptance of the architecture.

§      
**End User Groups / Organizations:** Direct end users include those
whose jobs would be directly impacted by implementation of IntelliGrid Architecture including
customer energy managers, energy services providers, and other users. Many
energy consumers would fall into this category as well as building owners and
consumers whose lives may be impacted by rate structures and other concepts
enabled by IntelliGrid Architecture. The purpose is to inform representatives of key groups of
energy users about IntelliGrid Architecture, its benefits, and how it will be implemented.
Interest in IntelliGrid Architecture generated by end-users is crucial to initiating demand for
the advanced end-user services that IntelliGrid Architecture can facilitate. This in turn
results in vendors creating products to satisfy that demand.

§      
**Standards Bodies:** The purpose of outreach to these groups is to
gain acceptance and incorporation of IntelliGrid Architecture into current and proposed standards.
Outreach to standards groups such as the IEEE, IEC, ASHRAE, NIST, and others
will need to continue. These groups are positioned to provide ongoing input for
refining and enhancing the architecture as well as playing a large part in
facilitating industry sector ‘buy-in’. Since an ultimate goal is to standardize
IntelliGrid Architecture work through one or more of these organizations, buy-in is critical
to the success of the project.

§      
**International Community**: The United States accounts for only 25%
of the world market in utility spending. As such, in order to obtain
world-class manufacturer buy-in, IntelliGrid Architecture needs to appeal to the larger world
market. Learning from the lessons of UCA, we can draw the conclusion that
overall acceptance of IntelliGrid Architecture will come only after international acceptance.
To that end, it is important to engage international stakeholders in
conjunction with the other category groups.

Stakeholder outreach, training
and support should consist of the following components

§      
**Information and Promotion** – to inform the overall stakeholder
community about IntelliGrid Architecture, the value it provides, and how it can and will be
implemented.

§      
**Education and Training** – developing and delivering training in
the development, construction, and implementation of IntelliGrid Architecture.

§      
**Support –** developing and delivering a support mechanism,
providing a distribution means and tools for implementing IntelliGrid Architecture.

Information
and Promotion

The information and promotion component should
consist of various communications strategies and tactics, including a rollout
event, technical papers, articles, presentations, etc., to raise awareness and
acceptance of IntelliGrid Architecture within the electricity industry and associate stakeholder
communities. Key items include:

§      
**IntelliGrid Architecture Website** – the collaboration web (www.iecsa.org) is already
in existence and will require migration to support stakeholder engagement in
the development phase An IntelliGrid Architecture website will continue to be a depository for
press releases, white papers, background materials, Frequently Asked Questions
(FAQs)
and other content. This material needs to remain publicly accessible (requires
no user identification or password) and will be branded as a central
destination where anyone can be directed for more information. Getting the site
listed with the major search engines will be a key priority. The website will
serve as the main avenue for support – housing the help desk/hotline and
serving as the gateway for IntelliGrid Architecture users group
website. The site will need to be updated to describe the final deliverables
and provide a means to operate the support mechanism – hot line, FAQs, etc. Additionally, the site will serve as a
depository for new use cases and implementation success stories, utilities
using products that utilize IntelliGrid Architecture, etc.

§      
**Brochure** – An overview brochure on IntelliGrid Architecture was developed to support
stakeholder engagement in the development phase. This brochure could still be
utilized, but an expanded brochure should be created explaining what IntelliGrid Architecture is,
its scope, its benefits, how it will be implemented, and how it will be
supported. This brochure could be distributed in hard copy and electronically
at conferences, meetings, training events, presentations, and in
person-to-person and group interactions. It will also be made available in
electronic format on IntelliGrid Architecture website. There should also be an effort to
develop a product explaining IntelliGrid Architecture in non-technical terms for the general
public.

§      
**Newsletter** – Develop a regularly-distributed newsletter will inform
audiences about IntelliGrid Architecture, its goals, case studies of successful implementation,
scheduled events (training events, annual user group conference), news, etc.
The newsletter should be distributed in electronic format to individuals who
sign up on IntelliGrid Architecture website, attend workshops, or who are identified as
targeted audiences. A limited number of hard copies could be produced for
distribution at conferences, workshops, and other appropriate forums.

§      
**Briefing Materials** – Presentations on IntelliGrid Architecture and the process and
progress of the project have already been developed. These should be revised to
reflect the final deliverables and focus on implementation rather than on the
development. Both short form and long form versions should be developed, as
well as versions specifically targeted at various audiences – utilities,
vendors, regulators, etc. A presentation describing IntelliGrid Architecture in easy to
understand, non-technical terms would be useful as well.

§      
**Conference Presentations and Speeches** – A pool of speakers
consisting of key EPRI leaders and technical personnel, EPRI partners and
advisers, early adopters of IntelliGrid Architecture concepts, IntelliGrid Architecture and other
EPRI project
contractors, and other industry experts should be identified and matched to
potential speaking/presentation opportunities. A list of presentation venues
running the gamut from ‘big think’ talks to technical papers should be compiled
and speakers targeted at those events.

§      
**Articles** – as with conference presentations, these would consist
of ‘big think’ pieces targeted towards high-level and general audiences and
technical pieces oriented towards key groups – utilities, vendors, regulators,
and standards making organizations. Targeted publications range from utility
and communication industry trade press to ‘op-ed’ pieces with bylines for
senior EPRI management that could go into the Wall Street Journal or the
New York Times. The targeted audiences for these include policy makers, utility
managers, and designers/implementers.

§      
**Fact Sheets** – these should reflect the final deliverables and
address a range of topics related to particular audience groups – utilities,
vendors, standards making organizations, etc. These would be posted on the
website and made available at workshops, conferences, and events as well as
directly to stakeholders.

§      
**Press Releases and Kits** – There should be a concerted, aggressive
process for generating and approving press releases and distributing them.
Press releases could be distributed via the wire service utilized by EPRI
and also sent directly to targeted media. Contacts should be made to targeted
media to pitch press release and stories about IntelliGrid Architecture, especially focusing on
demonstration projects and success stories.

§      
Editors and writers with utility and communications industry trade
publications (including websites and information services) as well as general
press (particularly business or technology oriented newspapers, magazines, and
broad/webcast outlets) can be a key ally in helping
to implement IntelliGrid Architecture. Effective, positive coverage of IntelliGrid Architecture can aid in the
implementation process and maintain a flow of information that keeps the
various stakeholder groups and general audiences interested. This is
particularly important given the demographic and geographic diversity of the
various stakeholder groups. Also, media coverage can aid in reaching
international audiences.

§      
**Media Events** – A series of media events should be held shortly after
the release of IntelliGrid Architecture. These could be held in various locations and possibly in
conjunction with already scheduled industry events. The goal would be to
provide a venue to reach and inform the press and the stakeholder communities.

Education
and Training

A key component in implementing IntelliGrid Architecture will be
the development and delivery of training programs. This will facilitate
transfer of technology as well as build support for the adoption and
implementation of IntelliGrid Architecture. It is recommended that there be the development,
scheduling, and delivery of a series of workshops discussing the benefits and
scope of IntelliGrid Architecture, the final deliverables, and how the results can be applied to
new systems, legacy equipment, and the entire utility enterprise.

These workshops will range in scope and tone
from high-level overview to nuts and bolts “here’s the architecture,
here’s how to use it.” This should begin with the development of a series of
outlines targeted towards specific audience groups, then move towards
development of presentation materials, scheduling the workshops, identification
of the best resources to teach the workshops, and actual conducting of the
workshops.

The IntelliGrid Architecture workshops would be 1-3 days, with 1-3
speakers, depending upon the area and degree of interest. The workshops would
include presentations, hands-on examples of using IntelliGrid Architecture Use Cases, hands-on
examples of using the IntelliGrid Architecture, and other topics. A key
component would be IntelliGrid Architecture User’s Guide, discussed above.

It is suggested that the workshops be handled
using a ‘train the trainer’ approach where implementation facilitators undergo
training on IntelliGrid Architecture and are then ‘certified’ to teach the workshops to others.

These workshops should be scheduled in
conjunction with industry conferences and other events – especially related to
the standards making organizations and conducted on both a regional basis and
as requested to ensure that everyone has an opportunity to attend a workshop.
In addition to in person training, there should be an effort to put together WebExÔ conferences
to address audiences – primarily utilities – that have limited travel budgets.

Support

In addition to information/education and training,
ongoing support will be a key component in ensuring the successful
implementation of IntelliGrid Architecture. EPRI should consider a commitment to making this
support available 24/7 to the various stakeholder categories. Key activities
include:

§      
**Support Hotline and Website**. An IntelliGrid Architecture Answers Hotline should be
established to receive and answer questions. The hotline does not necessarily
have to be a 24/7 operation, but there should be experts available to field
calls and answer questions. When the line is not staffed, calls should be
recorded and followed up within 24 hours. The IntelliGrid Architecture website should feature a
strong support section housing the final deliverables, training materials,
supplemental use cases, and a Frequently Asked Questions page that will address
both technical and non-technical questions related to IntelliGrid Architecture and its implementation.
The site should be accessible to registered users, who would not pay for
registration. Also, as implementations are conducted and experience gained, it
is important to incorporate lessons learned, new use cases, case studies, and
other information into the on-line deliverables section of IntelliGrid Architecture website.

§      
**IntelliGrid Architecture Users Group.** An IntelliGrid Architecture Users Group needs to be established
and supported. This would be open to membership by any interested party,
although utility, vendor, regulatory, and standards making organization
personnel would be encouraged to join. The user group would maintain a website
located off the main IntelliGrid Architecture website and would aid in the development and posting
of FAQs, all supporting materials, and assistance
with hot line questions. It is suggested that the group be governed by an
advisory council of selected individuals representing key sectors – utility,
vendor, government, etc. that provide direction to the group and advise on
group and implementation activities. The group should have at least one meeting
per year that is open to the public and feature both a technical – seminar,
workshop – and administrative component targeted at discussion of
implementation concerns, scheduling, etc. The advisory council and the group as
a whole would provide input into development of information and education
materials and the implementation process as a whole. In order to accelerate
creation of IntelliGrid Architecture Users Group, it is recommended that the UCA International
Users Group, as a funded and viable body, be considered as a means for making
it happen.

### Recommendations for integration with other architectures

It was identified in the introduction that the
successful enterprise and industry-wide scope of IntelliGrid Architecture will interact with in
whole or in part parallel efforts by other large stakeholder groups. Included
are other key architectures in development at Federal, State and even
International levels. It is essential to avoid the need for duplication and
proliferation of translation layers and gateways that convergence be pursued
between the energy industry and IntelliGrid Architecture, and, the following efforts.

Major architectural frameworks:

§      
Federal Enterprise Architecture

§      
Department of Defense Architecture Framework (DODAF)

§      
State Level Architecture Developments

§      
International Level Architectures

In addition, the following commercial and
standards based architectural frameworks will impact products and services of
use to the energy industry:

§      
OMG’s Model Driven Architecture, MDA

§      
ISO/IEC 10746 Reference Model for Open Distributed Processing, RM-ODP

§      
Grid Computing (www.gridforum.org)
