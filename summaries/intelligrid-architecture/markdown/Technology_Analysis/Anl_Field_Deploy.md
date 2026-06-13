# Field Device Integration

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Field_Deploy.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Field Device Integration Deployment Scenario

This example shows how IEC61850 and DNP3-based SCADA
systems can be integrated to provide unified rich model-based device access and
control. 

Today's field devices
are multifunctional Intelligent Electronic Devices (IEDs) that have become the
standard in new or upgraded integrated substation protection, monitoring and
control systems, as well as other field installations. The changes in
the industry result as well in changes in the requirements for the communications
capabilities of such devices. Multifunctional IEDs with advanced communications
capabilities allow the utilities to deal with many important issues such as:

if !supportLists?·      
endif?Requirements for local and remote user interface
for different types of corporate clients

if !supportLists?·      
endif?Requirements for extensive data sources from the
field for integrated data acquisition and control systems

if !supportLists?·      
endif?Requirements for distributed power system event
and disturbance recording devices

if !supportLists?·      
endif?Requirements for integrating seamless
transitions between local actions by individual and neighboring field devices
and distributed actions from control centers for global protection, control and
monitoring functionality

if !supportLists?·      
endif?Requirements for more efficient and very high
speed communications-based transmission line or centralized wide area
protection schemes

The selection of the communications protocol used at the
substation and distribution feeder level is one of the critical factors to
consider in the design of substation automation, energy management systems, and
distribution automation systems. The protocol should provide all required
capabilities that will allow the optimal implementation of different substation
and system functions. The IntelliGrid Architecture recommends those common services,
generic interfaces, standard technologies, and best practices that provide
those capabilities, such as the use of discoverable information models to give
standardized names to classes and properties, and to describe their
relationships, their formats, and their interactions in standardized ways.

Most of the widely used communications protocols have been
designed to meet only the specific requirements of conventional SCADA systems.
They do not include security other than “security by obscurity”, network
management is limited to knowing only if communications are available or not,
and data management consists of tediously mapping point list numbers to
locations in a real-time SCADA database. As a result, these protocols cannot
completely meet the functional requirements for use in IntelliGrid Architecture-based energy
management solutions. DNP3 is one of the most popular SCADA protocols that is a
typical example of the challenges of integration of legacy IEDs in systems
implementing CIM/GID models and services.

With regard to what data is exchanged, legacy device
integration provides an example where complementary semantic sets can be
joined.  Traditional device models tend
to be communication oriented, namely multiple lists of points that are just an
index number into an array.  These simple
communication models can be seen as less rich and complementary from the point
of view of enterprise semantics. 
Consequently, as described below, the primary strategy consists of
mapping communication parameters to utility operational model elements to
extend the later with the former.

For data exchange methods, the IntelliGrid Architecture
recommends the use of common information models to support device
integration.  Specifically, IntelliGrid Architecture-based
device integration stresses the importance of enhancing communication models
with utility operational semantics. 
Instead of requiring integration on the basis of a communication model,
integration can occur via the use of a model-enabled API
such as IEC61850 Abstract Common Services Interface (ACSI) or IEC61970’s High
Speed Data Access (HDA).  Note that
communication protocols such as DNP3 or IEC61850 ACSI as well as other common
model enabled device communication API’s are
generic in that they can be applied to any device type and do not hard code
device specific semantics into the interface, meaning that their object models
are separate from the services.

The main problem, therefore, is mapping the data elements
in the IEDs to “well-known” object names. IEC61850 performs this mapping to
IEC61850 object models at the device level, while IEC61970 needs to perform
this mapping to the CIM power resource object model in the control center.
Since these are different mappings, they need to be harmonized. The solution in
this example presupposes a harmonized IEC61850/61970 information model as shown
in Figure 1. 

if !vml?![](Anl_Field_Deploy_files/image002.gif)endif?

Figure ‑1 Proposed Harmonized IEC61850 and IEC61970
Information Models

 

Figure
1 illustrates a proposed harmonization of IEC61850 and
IEC61970 information models.  Two UML
associations are key.  The inheritance
association between IEC61970 Equipment and IEC61850 GeneralEquipment allows the
extension of a CIM device with IEC61850 device information. The association
between IEC61970 Measurement and IEC61850 DataAttribute allows us to map CIM
measurements to IEC61850 object model values.  

DNP3 is not as simple to map because it uses simple
objects that do not provide self-description. The diagram below illustrates a
DNP3-based and IEC61850-based SCADA Networks.

if !vml?![](Anl_Field_Deploy_files/image004.gif)endif?

Figure ‑2DNP and
IEC61850 Based SCADA Networks

 

Since DNP3 has been developed as a Master - Slave protocol
for the power system data acquisition and control domain, it is not suitable
for any high-speed protection or control applications defined in IntelliGrid Architecture
Deterministic Rapid Response environment. It
is also not designed to easily support the configuration of protective relays
or other multifunctional IEDs with hundreds of settings nor to adequately
represent the multi-layer functional hierarchy of such devices. Control
functions in DNP3 are based on three control models.  Measurements in DNP3 are available through the analog
input and counter (accumulator) objects. Each IED maps individual measurements
to unstructured point index numbers in vendor-specific ways. The serial version
of DNP can not support most standard security measures in the environments it
is typically used in, namely with low bit-rate communications channels.

It is clear that one of the main limitations of a DNP
network is the limited amount of metadata that can be associated with a DNP3
device or measurement point.  The
proposed solution in this example is to present DNP3 data within a richer
namespace presented by a GID server.  Ideally, this namespace would be compatible
with not only IEC IEC61850, but also IEC IEC61970 CIM Power System models and
DMTF CIM Enterprise Management models. 
In other words, the sparse DNP3 model is decorated with rich
IEC61850/61970/DMTF metadata so that the DNP3 data is made more meaningful to
people and applications.

Since IEC IEC61970
defines a CIM set of packages which provide a logical view of the different
aspects of Energy Management System information, the integration of legacy DNP3
based devices requires the mapping of the DNP3 points into the CIM object
models.

The figure below shows
the mapping of four analog measurements (voltage, active power, current and
reactive power) available in two protection IEDs that support the DNP3 protocol
into a CIM based rich model. These measurements are represented in DNP3 as 4
data points. Each of them has to be mapped into the hierarchical rich model
defined in CIM. 

In the CIM model of Figure 1, a PowerSystemResource (PSR) may have zero to many
measurements associated with it. Each measurement may contain one or more
measurement values. Measurements of a PSR are classified by MeasurementType.

The MeasurementType.name
in the CIM model is the IEC IEC61970 name assigned, while the
MeasurementType.aliasName is the name assigned to the type in IEC IEC61850. For
example ***Volts*** in the figure below is the MeasurementType.aliasName for
the ***Voltage***
MeasurementType.name.

if !vml?![](Anl_Field_Deploy_files/image006.gif)endif?

Figure ‑3 Mapping a Device Model to the CIM

 

The key, therefore, is the mapping of DNP data items into
the IEC61850 namespace and then exposing this rich namespace via the GID.
This solution goes a long way toward supporting the interoperability of
telemetry data servers with telemetry data clients.  Once mapping is complete, the enriched
namespaces of a DNP3 server can be based on the same information model as an
IEC61850 server.  Consequently, the
namespaces can be aggregated into a single integrated whole.  The fact that DNP3 or IEC61850 are used for
the field communications can be completely hidden from the client by the GID
interface.  From the client’s point of
view, there is only a single telemetry server that presents the rich name space
of IEC61850.  Adoption of standard ways
of representing **what** data is
exchanged combined with standards ways for **how**
data is exchanged allow us to fully integrate SCADA systems and use the SCADA
protocol most appropriate for the environment.

In this example a new GID
Client for EMS operations applications, as
well as a second GID Client for network
analysis applications are being integrated with the DNP3 and IEC 61850 field
devices using a CIM based solution. The GID
servers are used to present the DNP3 and IEC 61850 devices data within the
context of the CIM. They interface with the different IEDs connected to the
DNP3 and IEC 61850 networks and receive from them the data required by the two GID
Client applications.

The CIM/GID integration
of DNP3 legacy field device and an IEC 61850 device includes the following
applications:

if !supportLists?·      
endif?CIM-based power system modeling environment
within the control center

if !supportLists?·      
endif?DNP3 field device GID
server

if !supportLists?·      
endif?IEC 61850 field device GID
server

if !supportLists?·      
endif?GID Client
for operations applications

if !supportLists?·      
endif?GID Client
for network analysis

All GID clients and
servers are connected to a CIM/GID based
message bus. As shown in the figure below, adapters are used to connect the
DNP3 based service manager and the IEC 61850 based service manager to the CIM/GID
Based Message Bus.  These adapters server
two purposes:

if !supportLists?·               
endif?Define **What**
data is exchanged

if !supportLists?·               
endif?Define **How**
the data is exchanged

if !vml?![](Anl_Field_Deploy_files/image008.gif)endif?

Figure ‑4 Wrapping DNP with a IEC61850 Based Namespace

 

The goal of seamless integration of field devices that
support different field device data monitoring techniques can be provided by a
CIM/GID-based system. Therefore, the GID
Clients functionality can take full advantage of the CIM regardless of what
devices are used for the interface with the electric power system and its
components. This allows the integration of existing or future CIM based EMS
applications developed independently by different vendors regardless of the
communications protocols supported by the field devices used as the data source
or to execute the required control action in the substations.

Security technologies are being standardized for both DNP3
and IEC61850 through on-going work in IEC TC57 WG15. When this work is
completed, the more complete suite of security requirements will need to be
incorporated in the CIM/GID/IEC61850/DNP
integrated package. Likewise, additional network management efforts will need
to be incorporated as the understanding of these needs are developed more
fully.

As shown in IntelliGrid Architecture Environment for Critical Operations
Data Acquisition and Control, the key security requirements that should be
added to the CIM/GID/IEC61850/DNP integrated
package, include:

if !supportLists?·      
endif?Authorization Service for Access Control

if !supportLists?·      
endif?Information Integrity Service

if !supportLists?·      
endif?Audit Service

Since this Environment cuts across at least two and
possibly more security domains (substation, field sites, control center), the
security solutions must be a combination of security policy, security
technologies, and security practices (such as training and rigorous monitoring
of security).

The mapping of DNP objects to IEC61850 objects, and the
subsequent “discovery” of these objects through the GID
capabilities, warrant additional focus on guidelines that address exactly how
these mappings should be done, and how they can best be at least partially
automated. The use of electronically available metadata models of the IEC61850
objects is clearly the starting point, but the next steps need to be clarified.
