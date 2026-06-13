# Common Services

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Common_Services.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Common Services

Common services,
common information models, and generic interfaces are the key to achieving
higher-level interoperability of power system distributed information systems.
According to W3C (http://www.w3.org/TR/2002/WD-ws-gloss-20021114/),
a service is a “*component performing a task*”. A component is

if !supportLists?*1)*endif?*A software object, meant to interact with other
components, encapsulating certain functionality or a set of functionalities. A
component has a clearly defined interface and conforms to a prescribed behavior
common to all components within an architecture.*

if !supportLists?*2)*endif?*An abstract unit of software instructions and
internal state that provides a transformation of data via its interface.*

In essence, IntelliGrid Architecture Common Services are commonly defined functionality derived by identifying
the crosscutting distributed information requirements.  The IntelliGrid Architecture Generic Interface is an agreement
on how to access those common services.

Conceptualizing a
utility as a set of interoperating services allows components to be treated as
black boxes.  This facilitates greater
flexibility as components are less dependent how each works internally.  This is a key issue in creating interoperable
off the shelf components.  However, the
use of common services does not by itself completely reduce the complexity of
dealing with heterogeneous systems.  For
example, the definition of common services do not necessarily deal with the
discontinuity of different platforms such as Java, Web Services, or .Net.  Also, common services do not necessarily deal
with discontinuities associated with the meaning of data.  Lastly, common services do not deal with the
discontinuities caused by different data access mechanisms associated with
read/writing/or subscribing to data. Therefore, one needs to combine common
service, common information model and generic interface together to achieve
interoperability. This section describes the common serviced identified by
architecture analysis. The subsequent sections will discuss common information
model and generic interface.

### Common System and Network Management Services

The Service model
describes the basic set of the functions used for enterprise management. At the
higher level of abstraction, the team started from the OSI basic functions: Fault Management,
Configuration Management, Accounting Management, Performance Management and
Security Management. Refining this list further, the team extracted, as
described above, the following functions from IntelliGrid Architecture requirements for
enterprise management.

#### Inventory management

This service tracks and maintains the inventory
information software, hardware, network and system entities; provides an
accurate account of information such as ownership, versioning and installation
status of the entities.

#### Communication System/network discovery

This service tracks and reports on the
configuration status, capabilities, resource availability of system/network
entities; also can discover the interconnection pattern/ topology of these
devices.

#### Routing Management

Routing management configures, selects and
prioritizes routes for traffic/messages exchanged amongst various enterprise
entities; implements specified routing policies and preferences; also provides
support for route-reconfiguration, as well as necessary route
diversity/fault-tolerance to fulfill QoS and route-service availability
requirements.

#### Traffic Management

Traffic management provides packet, flow,
call, user, application level scheduling, prioritization, congestion control to
manage resource sharing in terms of, e.g. bandwidth and buffer and
processor-time.

#### Traffic Engineering

Traffic engineering monitors traffic usage
and growth trend and adjusts network/system resource allocation accordingly.
For example, logical data pipes connecting various end-points can be re-sized
dynamically or quasi-dynamically based on measured SLA requirements, actual
usage, or time-of-the-day, day-of-the-week traffic trends and patterns. Traffic
engineering also supports the provisioning of redundancies to assure
reliability requirements.

#### System/network health-check analysis

This service determines the set of
system/network health indicators, threshold values, and health check intervals.

#### Fault diagnosis

Fault Diagnosis provides mechanisms and
algorithms to determine the location of faults by running diagnostic tests on
application/system/network entities. This may also include alarm correlation
and fault data summarization and analysis.

#### Fault correcting

Fault Correcting provides mechanisms to
correct faults which can include: fault isolation, device reset, SW
re-initialization, reconfiguration, rerouting and removal of system/network
entities, as well as the issuing of trouble tickets, and the dispatching of
repair technicians.

#### Service level agreement (SLA) determination and maintenance

This service defines, provisions, enables,
monitors, and maintains SLAs. This also requires the mapping of SLA/user
performance objectives to system/network performance objectives.

#### System/network performance analysis

This service determines the set of
system/network performance indicators, threshold levels and monitoring
intervals.

#### Performance diagnosis

Performance diagnosis determines and isolates
the cause of performance problems based on the analysis of system/network
statistics and measurements.

#### Performance tuning/correction

This is to fix performance problem by means
of system/network reconfiguration, traffic/message rerouting, parameter tuning,
and resource allocation re-adjustment.

#### Accounting and/or Billing

This function helps define accounting metrics
and specifies accounting information to be collected. Also supports the setting
and modifications of accounting limits. It also provides the “toll booth”
measurements on traffic to make them available to a billing entity. It also
controls the storage of and the access to accounting information. Lastly, it generates
accounting/billing reports regarding application/system/network resource usage.

### Common Data Management and Exchange Services

As described in
Volume I Section 3, data management must address a complex set of issues, which
include the following:

if !supportLists?1.    
endif?Validation of source data and data exchanges

if !supportLists?2.    
endif?Ensuring data is up-to-date

if !supportLists?3.    
endif?Management of time-sensitive data flows and timely
access to data by multiple different users

if !supportLists?4.    
endif?Management of data consistency and synchronization
across systems

if !supportLists?5.    
endif?Management of data formats in data exchanges

if !supportLists?6.    
endif?Management of transaction integrity (backup and
rollback capability)

if !supportLists?7.    
endif?Management of the naming of data items (namespace
allocation and naming rules)

if !supportLists?8.    
endif?Logging, reports, and audit trails

This
section describes a limited set of data management services to allow components
in a variety of environments to communicate to meet the list of issues above.

#### Distributed Data Management Service

This service
supports access to metadata and instance data including the reading/writing of
attribute values of managed objects. 
This function also modify the relationships between managed objects

#### Object management service

This service
supports the creation and deletion of objects associated with resources being
managed. Specify attributes and their corresponding ranges associated with a
resource. This function also manages the relationships between managed objects

#### Address & naming management

This assigns,
maintains addressing and naming schemes for entities to be management within
the enterprise(s). This also includes the support of lookup services between
address and names as well as translation/mapping across multiple address/naming
schemes.

TC57 WG 13's 61970
Part 402 Resource ID Service provides an example of a Resource Identification
Service.

#### Generic Eventing And Subscription

A collection of
dynamic, distributed services must be able to notify each other asynchronously
of interesting changes to their state.

TC57 WG 13's 61970
Part 405 Generic Eventing and Subscription (GES) provides an example of an Eventing and
Subscription Service. GES provides publish/subscribe-oriented
interface that supports hierarchical browsing of schema and instance
information. The GES is typically used as an API for publishing/subscribing to XML formatted
messages.

#### Alarm detection/reporting

These functions
supports mechanisms, e.g. polling, use of watchdog timers, process trap etc, to
detect and report application/system/network faults. Also provides the logging
of events and errors as well as the specification and enabling of logging
filters.   

#### Instrumentation and Monitoring Service

Instrumentation
and monitoring services, supporting the discovery of “sensors” in a distributed
environment, the collection and analysis of information from these sensors, the
generation of alerts when unusual conditions are detected, and so forth.

Provided via a
request/reply and/or a publish/subscribe oriented interface to support
hierarchical browsing and querying of schema (class) and instance information
about data.

TC57 WG 13's 61970
Part 404 High Speed Data Access (HSDA) provides an example of an Instrument and
Monitoring Service. Access HSDA provides a request/reply and publish/subscribe
oriented interface that supports hierarchical browsing and querying of schema
(class) and instance information about high-speed data.

#### Measurement Data Logging Service

This service
supports the recording and distribution of time series measurements. That is
sequences of repetitive measurements that can be correlated by time.

TC57 WG 13's 61970
Part 407 Time Series Data Access (TSDA) provides an example of a Measurement
Data Logging Service. Access TSDA provides a request/reply and
publish/subscribe oriented interface that supports hierarchical browsing and
querying of schema (class) and instance information about time-series data.

#### Remote Control

This service
provides supervisory control over remote applications including program
invocation services and the ability to load/upgrade remotely installed
software.

#### Network Time

This is to distribute and upgrade software for
system/network elements within the enterprise(s).

#### File Transfer

This is to distribute and upgrade software
for system/network elements within the enterprise(s).

### Common Platform Services

Common Platform services are typically
defined by the operating platform a component runs in.  For example, the Web Service Communication
stack provides a set of service definitions for these functions.  It is beyond the scope of IntelliGrid Architecture to define
these services in any way except to say that the presence of these services is
assumed and that IntelliGrid Architecture based applications will use them to interoperate. 

Note that although these services are
typically provided by J2EE, .Net, Web Services, CORBA or others, the
implementations of these services on these different platforms typically do not
interoperate.  It is up to the
implementer to use a common platform or deploy platform service adapters.  However, as these services and adapters are
not utility specific, in depth discussion of their functionality and use is out
of scope of this document. 

#### Component Registry Service

Registry Services
provide the mechanisms for services to advertise their existence. Closely
related to Discovery Service.

#### Component Lookup Service

Allows search for
a service and download the code needed to access it;

#### Component Discovery Service

Clients require
mechanisms for discovering available services and for determining the
characteristics of those services so that they can configure themselves and
their requests to those services appropriately and spontaneously find a
community and join;

#### Component Initialization and Termination

This is to provide
means and mechanisms to initialize, shutdown, re-initialization and reset
various networks and systems operations.

#### Storage

This service
provides the capability to reliable store data to distributed storage media.

#### Resource Management

This service is
used to arbitrate component access to computer resources such as CPU time or
random access memory.

#### Transactions

This service is
used to ensure that a system’s distributed state stays consistent.

#### Checkpoint and recovery

This service is
used with the transaction service to ensure that a system’s distributed state
stays consistent.

#### Workflow Service

Support the
coordinated execution of multiple application tasks on multiple distributed
resources.

### Common Security Services

Based upon the
security functions, discussed in section 1.1.2, several security services have
been identified that are needed to provide the security functions.

#### Audit Service

The audit service
is responsible for producing records known as audit records which contain audit
record fields, which track security relevant events.

#### Identity Establishment Service

An identity
establishment (e.g. identity authentication) service is concerned with
verifying proof of an asserted identity.

#### Authorization for Access Control

The authorization
for Access Control is concerned with resolving a policy based access control
decision based upon appropriate Identity Establishment.

#### Confidentiality Service

Protect the
confidentiality of the underlying communication (transport) mechanism, and the
confidentiality of the messages or documents that flow over the transport
mechanism

#### Credential Conversion

The credential
conversion service provides credential conversion between one type of credential
to another type or form of credential.

#### Credential Renewal Service

Provides the
ability to be notified prior to expiration of the credentials, or the ability
to refresh those credentials such that the job can be completed.

#### Delegation Service

Provide facilities
to allow for delegation of access rights from requestors to services, as well
as to allow for delegation policies to be specified.

#### Firewall Traversal

Provide mechanisms
for cleanly traversing firewalls without compromising local control of firewall
policy.

#### Identity Mapping Service

Provides the
capability of transforming an identity which exists in one identity domain into
a identity within another identity domain

#### Information Integrity Service

Ensures that
unauthorized changes made to messages or documents may be detected by the
recipient.

#### Policy Service

The Security
Domain’s policy service is concerned with the management of policies.

#### Privacy Service

The privacy
service is primarily concerned with the policy driven classification of
personally identifiable information.

#### Profile Service

The profile
service is concerned with managing service requestor’s preferences and data
which my not be directly consumed by the authorization service.

#### User and Group management

This is to define,
assign, organize, control and maintain mapping for user and group identifiers
within the enterprises.

#### Security Assurance Management

Satisfies the need
for manageability of security functionality within IntelliGrid Architecture security model.

#### Security Management Infrastructure

A Security Domain’s
infrastructure and personnel that is used to implement Security Management.

#### Security Protocol Mapping

Security protocol
mapping services, enabling distributed security protocols to be transparently
mapped onto native platform security services for participation by platform
resource managers not implemented to support the distributed security
authentication and access control mechanism.

#### Setting & verifying user authorization

This service is
for assigning and validating authority given to a user or a group of users in
accessing/utilizing specific enterprise resources. 

#### Single Sign on Service

Relieve an entity
having successfully completed the act of authentication once from the need to
participate in re-authentications upon subsequent accesses to OGSA-managed
resources for some reasonable period of time. This must take into account that
a request may span security domains and hence should factor in federation
between identity domains and mapping of identities. This requirement is
important from two perspectives: a) It places a secondary requirement on an
OGSA-compliant implementation to be able to delegate an entity’s rights,
subject to policy (e.g., lifespan of credentials, restrictions placed by the
entity) b) If the credential material is delegated to intermediaries, it may be
augmented to indicate the identity of the intermediaries, subject to policy.

#### Security against Denial-of-Service

This service is
for assisting in preventing a denial of service.

#### Inter-Domain Security

This service
represents the capability to provide additional security services, as needed,
in order to facilitate inter-domain information exchanges.  

#### Trust Establishment Service

This service
represents the ability of one resource to determine if its peer can be trusted.

#### Non-repudiation

This service
represents the ability of a security domain to provide proof that a given
exchange action has occurred. 

#### Quality of Identity Service

This service
allows an entity to determine the trust level associate with the identity being
conveyed.

#### Security Service Availability Discovery Service

A Security Domain
must provide a mechanism for an entity to discover what other security services
are available for its use.
