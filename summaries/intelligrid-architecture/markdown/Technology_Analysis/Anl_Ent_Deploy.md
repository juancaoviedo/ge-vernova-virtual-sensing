# Enterprise Management

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Ent_Deploy.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Enterprise Management and Power Systems Integration Deployment Scenario

This subsection consists of two
parts.  The first deals with the
integration of Enterprise Management Systems with each other.  The second deals with the integration of
Enterprise Management System with the rest of the utility.

#### Enterprise Management Integration

if !vml?![](Anl_Ent_Deploy_files/image002.jpg)endif?

Figure ‑5 Today's Enterprise Management Architecture

Figure 5 shows the logical architecture of today’s enterprise
management. As discussed previously, multiple systems, protocols, standards,
platforms and approaches have been proposed and implemented which often deal
with a group of resources or functions and can create a challenge in providing
a broad and unified management perspective. This problem has been recognized
and solutions have been proposed within the communications and the computing
industries.  A more recent web-based management
initiative focuses on unification of the various management systems rather than
their replacement.  In addition to
providing interoperability, web-based management promises to provide a faster
way to implement and easier to use platform for management of entities through
use of common web languages and protocols such as XML and HTTP. This is to
facilitate information exchange between heterogeneous network management
entities/ platforms [Enns 03] by leveraging the wide availability of XML-based
parsing/ transformation tools.

Various approaches
to use of web technology with the purpose of unification have been proposed and
some are implemented. One approach, which is relatively easier to implement and
a good short-term solution, is to provide a web interface to the existing
enterprise management systems. For this approach, a web server, on the manager
platform, provides the link between the native manager and the web interface.
Clearly, this provides a uniform GUI for accessing management information, but
does not attempt to integrate the semantics of the underlying systems being
managed. As a result, some of the capabilities of management agent embedded
systems are not achieved.  Figure 6 provides the view of a web-based user interface to
enterprise management.

**if !vml?![](Anl_Ent_Deploy_files/image004.gif)endif?**

Figure
‑6 A Web-based Interface to the Enterprise
Management System

 

if !supportLists?4.    
endif?A more involved, but potentially better approach
in the long run, is specified by DMTF WBEM. The objective is not to replace any
existing management protocols/ solution, but rather to provide a set of
management and Internet-based standard technologies to unify the enterprise
management of large scale, heterogeneous distributed computing and
communication environments such as those found in IntelliGrid Architecture. As such, unification
and integration support of existing/ legacy enterprise management technologies
is a key theme of the DMTF WBEM.

Figure 7 depicts the integrated management of a set of heterogeneous
technologies under the DMTF CIM/WBEM framework. The WBEM server receives and
processes WBEM operation requests issued by various management application
clients and performs semantic integration of the underlying systems. With the
help of technology-specific object providers, the WBEM converts a legacy
enterprise manager’s message from its native format to a DMTF CIM schema and on
the reverse side, determines which legacy enterprise manager a message belongs
to and converts that message to the format of that system and technologies. Any
new development of management objects may continue to be web-based and thus
allow for all the functionalities. However, the enterprise can continue to use
the existing network management systems. For communications between native DMTF
CIM-capable managed and/or managing systems, local DMTF CIM scheme expressed in
the Managed Object Format are first converted to XML documents or messages
based on the DMTF XML/CIM encoding scheme. The XML documents or messages are then
transported directly over HTTP protocol. To further align with the approach
taken by the recent Web-services initiatives, there are also ongoing activities
to define standards such that these XML messages/documents can be encapsulated
within SOAP envelopes before transported over HTTP.  In the case where there are more than one
collaborating IntelliGrid Architecture enterprise management systems belonging to multiple
administration domains within a federation, they also communicate with each
other via this xmlCIM-over-HTTP or xmlCIM-over-SOAP-over-HTTP approach as shown in Figure 8. The use of HTTP (or HTTPS) as the transport protocol
will facilitate the activities such as firewall traversal when communication
across multiple security perimeters is required.

A disadvantage of
embedded web-based management is the model complexity, requiring ability to
implement a web server within the agents and support DMTF CIM. Some devices may
not have sufficient computing resources to allow for such features. For these
devices, the doable approach is always to either use or implement a lite agent
functionality on the managed element and add the additional DMTF CIM/WBEM
functionalities on another element, the so-called Object provider, which will
convert the lite model to the DMTF CIM model. This has been shown in Figure 7and Figure 8.

if !vml?![](Anl_Ent_Deploy_files/image006.gif)endif?

Figure
‑7 Web-based Enterprise
Management Architecture, which enables the Integration and Federation of
Heterogeneous IntelliGrid Architecture management technologies

 

if !vml?![](Anl_Ent_Deploy_files/image008.gif)endif?

Figure
‑8 Collaborations amongst multiple Management
Systems

if !vml?![](Anl_Ent_Deploy_files/image010.gif)endif?

Figure
‑9 The Internal Architecture of a WBEM Server
and its interactions with Management Application Clients and Managed
Devices/Systems

 

Figure 9 illustrates the logical components of a WBEM server
and how it interacts with external components including management application
clients and managed systems. The protocol adaptors accept incoming requests
from management client applications through particular, possibly legacy
management protocols such as SNMP and translate these requests for the CIM
Object Manager (CIMOM). Under the DMTF CIM framework, Indicator Handlers are
used to support event-triggering mechanisms similar to SNMP traps. Converters
can be used to map CIM indicators to SNMP traps to support event notification
delivery to SNMP management clients. Note that, besides the usage shown in Figure 9, the protocol adaptors can also be used to interface
with external object providers that do not support xmlCIM-over-HTTP.

The CIMOM is the
central component of a WBEM server. It operates as a service layer and
interface object providers to management clients. The CIMOM responds to
operations defined in the CIM operations specifications. It also handles object
providers registrations and forward requests to object providers and
repositories. It maintains CIM class/instance information and provides
read/write access to management information. It also supports the managed
object query as well as inter-object association traversal.  The object provider is used to instrument
managed objects with one or more aspects of the CIM schema.

The DMTF CIM/WBEM
initiative has been successful in gathering strong supports from major software
and system vendors. Multiple commercial as well as open-source WBEM
implementations are available. These include the Microsoft Windows Management
Instrumentation (WMI), which is part of the Windows 2000 and XP
operating systems, the Solaris WBEM SDK by Sun Microsystems, the Pegasus
open-source WBEM implementation by the Open Group as well as the open-source
Standards Based Linux Instrumentation for Manageability (SBLIM) project
supported by IBM. On the networking front, the Storage
Network Industry Association (SNIA) also adopts the DMTF CIM/WBEM standards to
provider storage management functionality and has the support of major
networking vendors, such as Cisco, especially in the area of storage area
networks.

[Enns 03] R. Enns,
"XMLCONF Configuration Protocol", IETF Internet Draft
draft-enns-xmlconf-spec-00.txt, Feb. 2003

#### Enterprise Management And Power Systems Integration

This section
encompasses the integration of a DMTF based Enterprise Management systems with
TC 57 based utility systems.  It is
assumed that:

if !supportLists?·      
endif?Enterprise Management already successfully
accomplished/integrated using existing Enterprise Management technology (treat
existing Enterprise Management apps as a black box).

if !supportLists?·      
endif?Not trying to replace Enterprise Management -
only integrate it with power system management.

if !supportLists?·      
endif?IntelliGrid Architecture integration only needed so that end-to-end
reliability applications can simultaneously analyze power and communication
systems.

if !supportLists?·      
endif?Enterprise Management and utility system
security cannot be compromised.

With regard to
what data is exchanged, Enterprise Management/power system integration provides
another example where complementary semantic sets can be joined.  Network device models tend to be
communication oriented.  These models can
be seen as less rich and complementary from the point of view of utility power
system enterprise semantics. 
Consequently, as described below, the primary strategy consists of
mapping IT resource communication parameters to utility operational model
elements to extend the later with the former.

With regard to how
data is exchanged, generally IntelliGrid Architecture based Enterprise Management integration
seeks to more fully common model enable device communication technology.  Specifically, IntelliGrid Architecture based device integration
stresses the importance of enhancing IT resource communication models with
utility operational semantics.  Instead
of integrating on the basis of a communication model, integration occurs via
the common use of a model enabled API such as 61970’s High Speed Data Access or
Generic Data Access.  Note that both
communication protocols such as SNMP or CMIP as well as common model enabled
device communication API’s are generic in that they can be applied to
any device type do not hard code device specific semantics into the interface.

This deployment
scenario entails the creation of an Enterprise Integration Bus e.g. an integration
platform used to integrate the utility enterprise. The Enterprise Integration
Bus will support Enterprise Clients e.g. software components residing on the
Enterprise Integration Bus being used by an Enterprise system/network manager
and Enterprise Servers e.g. software components residing on the Enterprise
Integration Bus that carries out Enterprise client requests.

Integration Solution Details

if !supportLists?·      
endif?Various enterprise management information models,
which include routing MIBs, are exposed to Enterprise Bus using IESCA Common
Services.

if !supportLists?·      
endif?Enterprise Clients can browse/read/subscribe to
elements of the routing model as well as request updates to the model.

if !supportLists?·      
endif?Note that typically updates would be performed by an
DMTF or SNMP or CMIP based manager application

if !supportLists?·      
endif?Probably want to leverage the work done in the DMTF

 

if !vml?![](Anl_Ent_Deploy_files/image012.gif)endif?

Figure
‑10 Using A Separate DMTF Integration Layer

 

In Figure 10, the SNMP and CMIP network managers are adapted to
the operational integration bus via a DMTF server.  Analysis applications focused on end-to-end
reliability of the power system consume power system and IT device operations
and management data.  These new
applications can take into account previously unanalyzed variables and
comparisons.  For example:

if !supportLists?·      
endif?Telecom vs. power system load profiles.  A utility’s ability to recover from a fault
that causes a large amount of event data and cascading alarms needs to be
managed.  A utility may choose to
implement some sort of telecom load shedding during heavy power system loading.

if !vml?![](Anl_Ent_Deploy_files/image014.gif)endif?

Figure
‑11 Using DMTF CIM Only On The Enterprise
Integration Layer

 

Figure 11 illustrates the deployment scenario when only the
DMTF CIM are used as the integration technology.

if !vml?![](Anl_Ent_Deploy_files/image016.gif)endif?

Figure
‑12 More Complete Integration

 

Figure 12 illustrates the complete deployment scenario.
