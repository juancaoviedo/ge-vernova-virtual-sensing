# Enterprise Management Technologies

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Enterprise_Recomm.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Enterprise Management Technologies

This section provides an overview of the
enterprise management technologies recommended for using with IntelliGrid Architecture. The
complete set of recommended IntelliGrid Architecture enterprise management technologies are
described in detail in Appendix D of this volume.

### Analysis of Enterprise Management Technologies

The entities required to be managed under
IntelliGrid Architecture range from a large number of computation-resource-limited IEDs or legacy
field devices with limited intelligence, to better equipped
substation-controller systems, to desktop and server computing systems hosting
mission-critical IntelliGrid Architecture client/server applications, to enterprise network
elements such as Local Area Network (LAN)
switches and routers, to long-haul telecommunication equipments such as SONET/SDH
add-drop multiplexers (ADMs).  Given the
diversity of these managed entities and the different operational environments
and requirements they are under, no single enterprise management technology is
currently able to manage them all.  In
this subsection, we will discuss a set of viable enterprise management
technologies and highlight the specific properties, which make them applicable
for the management of particular subsets of IntelliGrid Architecture managed entities under
specific operational environments. In Section 4, we discuss an approach to
integrate the various technologies and provide a unified enterprise management
system.

**Simple Network Management Protocol**
(SNMP) is probably the most widely deployed enterprise management protocol
to-date. It was created to manage simple network components such as LAN
switches and routers. Since its inception, SNMP has been under continuous
extensions so that it can now be used for system and even application
management tasks. For example, extensions based on the operating system and
application level Management Information Base (MIBs) recently defined in IETF
proposed standards: RFCs 2287, 2564 and 2594. There also exist IETF standard
MIBs, which enable SNMP to manage computing hosts (RFC1514) as well as
relational database management systems (RFC 1697).  Moreover, most IETF protocols, designed
to-date, are instrumented to be managed under the SNMP framework, e.g., the
recent IETF MIBs for the support of Multi-protocol Label Switching (MPLS)-based
traffic engineering and the management of Layer 2 and Layer 3
provider-provision virtual private networks (PPVPNs). Notice that, protocols
such as MPLS and PPVPN are particularly relevant to IntelliGrid Architecture because they are top
candidates of the key networking technologies to fulfill the end-to-end
quality-of-service (QoS) and security requirements for mission-critical IntelliGrid Architecture
applications. 

**Common Management Information Protocol**
(CMIP) has its roots from ISO/OSI
initiative and was supposed to provide better solution than SNMP.  In particular, CMIP can support both the
query of information from, and the issuing of task-execution commands to, the
managed network element. CMIP also addresses security by providing
authorization, access control and security logs ever since its inception.
Furthermore, CMIP avoids the unreliable delivery problem of UDP-based SNMP
messages by adopting a connection-oriented, reliable delivery transport
protocol. Given its roots in ISO/OSI,
CMIP was designed for the management of large-scale service provider networks.
As such, it does use the object-oriented model to allow the description of
complex relationships amongst various managed entities and the hiding
(encapsulation) of implementation details when necessary. However, the major
complaint of CMIP is that it is a product of design-by-committee and it looks
better on paper than in the field. In particular, the specification of CMIP is
complex and overloaded with numerous non-essential options. This makes the
implementation and the programming-use of CMIP very complicated. The complexity
of the protocol also translates to high computational and memory requirements
of management systems and applications supporting CMIP. The CMIP stack is large
and can be of issue on ordinary workstations or small devices. The protocol in
the past has only been supported on larger systems where the investment could
be justified. In general, the direction of the industry has been increasingly
towards SNMP, even in the public telecommunication management space, which has
traditionally been the stronghold of CMIP.

**Web-Based Enterprise Management** (WBEM)
is the Distributed Management Task Force (DMTF)’s approach to enterprise
management, and has three major components:

if !supportLists?1.     endif?The
Common Information Model (CIM)[if !supportFootnotes?[9]endif?](Anl_Enterprise_Recomm.htm#_ftn9),
which provides an implementation-neutral common format, language and
methodology for collecting and describing management data. CIM enables common
understanding of management data across different management systems and
facilitates the integration of management information from different sources.
The DMTF CIM uses object oriented modeling principles and techniques to capture
the complex relationships and dependencies amongst various managed objects
within an enterprise. To-date, a rich set of CIM models has been proposed
and/or standardized by DMTF to model common managed entities ranging from
operating-system-free light-weight monitoring/remote-control devices, to
computer systems, to physical elements of a system, to enterprise network
elements such as LAN
switches and routers, to telecommunications equipments, to non-component-based
managed entities such as a Virtual LAN or
IP subnet (together with the necessary mechanisms to deal with QoS supports in
such networks), to operating systems, to mission-critical real-time
applications, to users, as well as management 
policies and SLAs. Note however that, while the DMTF CIM models
available to-date already support most of the management requirements for the
non-power-utility-specific parts of IntelliGrid Architecture, additional DMTF CIM models need to
be defined to allow the management of power-utility specific components of
IntelliGrid Architecture.

if !supportLists?2.     endif?The
xmlCIM Encoding Specification that defines, in the form of a Document Type
Definition (DTD), to represent CIM classes and object instances as XML
elements. The use of XML-based encoding takes advantage of the wide
availability of commercial XML parsing/ processing tools to further shorten
software development cycles.

if !supportLists?3.     endif?The
CIM Operations over HTTP specification which defines a mapping of CIM
operations (i.e. method invocation on CIM objects) into HTTP so that management
systems implementing CIM can interoperate in an open standardized manner while
leveraging the ubiquitous nature of web-based technologies. The use of HTTP
also facilitates the collaboration among a federation of loosely coupled
enterprise management systems potentially belonging to separate administrative
domains, e.g. different energy providers within a same geographical area in the
case of IntelliGrid Architecture.

The key advantage of SNMP is its simplicity,
which makes it possible to instrument devices of limited computational/memory
resources to be managed via SNMP. This is also the reason why a large number of
legacy field monitoring/ controlling devices in the power-utility industries
are managed via SNMP. Owing to its simplicity and proliferation, SNMP is
supported by majority of commercial enterprise management platforms as well as
networking, telecommunications, computing and SCADA equipment manufacturers.
This makes it a popular choice for multi-vendor cross-functional enterprise
management to-date. As exemplified by the wide range of IETF MIBs mentioned
above, SNMP can be readily extended to manage additional types of entities by
adding new SNMP MIBs. The learning curve for extending SNMP via MIB addition is
not as steep as those required by other enterprise management frameworks, such
as CMIP or DMTF CIM. This is due to the simple hierarchical structure of an
SNMP MIB-tree and the lack of association between different components being
managed under the SNMP framework.

Security has been one of the key weaknesses
of SNMP.  In SNMP versions 1 and 2,
authentication is supported only through a simple password mechanism. However,
since the password was sent in clear-text over the network, it is susceptible
to sniffing/ intercepting/ masquerading attacks, especially when the SNMP
message has to be delivered outside a local security perimeter. This will be of
relevance for the support of enterprise management across a federation of
administrative domains where each administrative domain may have its own
security perimeter but the communication links between the domains are not
guaranteed to be secure. Under such circumstances, additional technologies,
such as VPNs, may need to be introduced to mitigate the threat. While SNMP
version 3 addresses the security problem by introducing cryptographic
protection for the SNMP messages, it is expected that the large embedded base
of managed devices that support only SNMP V1 or V2, will continue to exist and
remain vulnerable in the near future. 

SNMP was designed to model simple management
environment in which the interactions between a managed entity, i.e. a switch
or a router, with other parts of the communications/computing infrastructure of
the organization were minimal. As such, SNMP doesn’t define and specify the
associations, dependencies, and interaction relationships between different
SNMP managed entities. The lack of such interactions in SNMP has made it
unsuitable to model and thus manage large scale, complex distributed computing
environments, as found in IntelliGrid Architecture, where the end-to-end service and performance
requirements of the mission-critical distributed computing applications can
only be achieved via the integrated management and control spanning the domains
of device management, system management, enterprise network management,
telecommunications management as well as applications management. To be more
specific, one of the critical aspects of large-scale enterprise management is
the ability to capture the relationships between management classes and
objects. Since SNMP does not support object-oriented (OO) modeling, the only
available construct for specifying inter-managed-object relationships is
"group". In contrast, other modern management frameworks such as the
DMTF CIM/ WBEM, (or even CMIP to a lesser extent), provide much better support
in specifying relationships amongst managed objects via the use of OO modeling
principles and specification techniques. For example, WBEM uses the inheritance
concept in OO modeling to inherit the common shared properties between the
class of a managed object and its derived classes. The use of encapsulation
techniques found in OO modeling also helps WBEM or CMIP to make the modeling of
a complex, distributed enterprise more tractable by separating the specific
implementation details of devices/ managed systems from the its informational
and functional specifications. In this regard, SNMP does not have the construct
of  "classes" to logically
encapsulate / hide related properties of a managed entity and all SNMP MIBs (or
management variables) must be listed in a large indexed table.

A disadvantage of embedded web-based
management model is its complexity, requiring ability to implement a web server
within the agents and support DMTF CIM. Some devices may not have sufficient
computing resources to allow for such features.

A limitation of both SNMP and CMIP is the
tight coupling between their network transport protocol and their
representation of management information. SNMP is defined to be transported
over UDP while most CMIP implementations are limited for OSI
transport networks. This makes them less flexible in taking advantage of
advances in alternate transport protocols. In contrast, DMTF CIM/ WBEM has
consciously separated the management information model, from its encoding, and
from the transport mechanism. This enables DMTF CIM/ WBEM to leverage the benefits
of recent encoding schemes such as XML and transport mechanisms such as HTTP
and Simple Object Access Protocol (SOAP).
Such flexibility is especially important in a heterogeneous, ever-changing
environment like IntelliGrid Architecture. In particular, the self-defining nature of XML-encoding
substantially enhances the interoperability between loosely coupled systems
found across a federation of IntelliGrid Architecture participants. The use of web-service
oriented transports such as HTTP, or HTTPS and SOAP also
facilitates the secure communications across different administrative domains
within a federations, e.g. by leveraging the firewall-traversal capability of
HTTP or HTTPS and the message routing capability in SOAP to
reach destined secure message gateways along a security perimeters. 

While there has been some non-mainstream
proposals, e.g.,  [Chiueh 03[if !supportFootnotes?[10]endif?](Anl_Enterprise_Recomm.htm#_ftn10)], to
extend SNMP to be truly object-oriented and to serve as the unifying enterprise
management protocol for the next generation digitally controlled utility grid,
the technical argument lacks the support of detailed analysis. A more pragmatic
view would be to, on one hand, accept SNMP as 
(1) a existing package that one needs to support in order to preserve
existing investments, and/or (2) the only viable light-weight solution for certain
types of resource-constrained managed entities such as low-cost IEDs or legacy
field devices; and on the other hand, derive a unifying management framework
which can satisfy the challenging management requirements IntelliGrid Architecture while
accommodating and interoperating with the SNMP, CMIP and other proprietary
management protocols/ frameworks. This will be the subject of the next
subsection.

### Overlapping/ Harmonizing/ Missing Enterprise Management Technologies

In the area of networking/telecommunication
equipment management, while SNMP/RMON and CMIP both perform a similar set of
high-level enterprise management functions, there are significant
implementation complexity/cost vs. capabilities/feature trade-offs amongst
these two major protocols as discussed in Section 1.3.1.1. In practice, the
choice of management protocol is mostly dictated by the kind of management
protocol available/supported by the managed devices of interest. This is
particularly true in order to satisfy backward compatibility requirement with
the large amount of legacy-managed devices deployed in the field.

In the area of distributed application/object
management, there are overlapping technologies, such as Java Management
Extension (JMX), and CORBA-based ones, which provide similar management
functions but are designed to support particular distributed computing
platform. For instance, JMX is primarily designed for the management of
distributed application written under the Java platform although it also can be
used to enable management through Java technologies.  On the other hand, there are also overlapping
application management technologies that are platform/language independent.
Examples of such include the Application Instrumentation and Control (AIC)
Standard by the Open Group, the IETF Application MIB, and the Application
Management Specification (AMS).
Overlapping technologies in the desktop management area include the DMTF
Desktop Management Initiative (DMI),
the IETF Host and System MIBs

Various standardization activities are under work
to harmonize the aforementioned overlapping technologies in each area. As
discussed in Section.3.1.1, the DMTF CIM/WBEM initiative provides the umbrella
under which all the areas of enterprise management ranging from the management
of networking devices, to that of telecommunication equipment, computing
systems and application can be unified. 
In particular, with DMTF CIM/ WBEM, SNMP and CMIP-based managed devices
can be managed under the framework. Recently, the TeleManagement Forum (TMF)
and DMTF also initiated a joint effort to further facilitate the convergence of
telecommunications and enterprise management by reviewing and determining
mapping between the existing models proposed by the two organizations while
partitioning new modeling/standardization efforts amongst themselves to avoid
duplicated efforts. They also pledged to work together to highlight areas for
improved integration and federation.

DMTF has also formed an Applications Working
Group to harmonize the integration of various application management standards/
initiatives to-date. These include ongoing initiatives by the Open Group
Enterprise Management Forum, the Open Group Application Quality and Resource
Management (AQRM) forum, the Open Group Application Response Measurement (ARM) working
group, the SUN Java
Community Process (JCP)
Expert group on managing J2EE environments (JCP JSR
77), the W3C Web Services Management Group as well as the Oasis Web Services
Distributed Management (WSDM) Technical Committee. This effort will also establish
the mapping between the application MIBs defined under the auspices of IETF and
the DMTF application run-time model.

Since DMTF CIM has its root for general IT
enterprise management, common information model for power-utility specific
management tasks are yet to be defined. It is critical to pursuit
standardization effort to harmonize IEC 57, 61970 CIM (i.e. the EPRI CIM) with
the DMTF CIM/WBEM framework in order to achieve an integrated energy and
communication management architecture. The existing application management
models and standards, e.g. AIC, AMS and ARM are
geared towards e-commerce applications such as online trading.  Extensions of such application management
standards are needed to better support power-utility specific distributed
computing applications, such as ADA, self-healing grid, WACS/WAMS and RTP
found in IntelliGrid Architecture.

Lastly, another key missing technology is the
methodology and tool to support *automatic* *mapping* of legacy
management information model to and from modern standardized common information
model (CIM) such as the DMTF CIM.  While
ontology-based experimental tools [de Vergara 03[if !supportFootnotes?[11]endif?](Anl_Enterprise_Recomm.htm#_ftn11), Noy
99[if !supportFootnotes?[12]endif?](Anl_Enterprise_Recomm.htm#_ftn12)] of
such do exist, they still require considerable human intervention and need
substantial further development before they can be used in a real-world,
production environment.
