# IEC 60870-6 (ICCP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC_60870-6_(ICCP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC 60870-6 (ICCP)

**URL:**http://www.iec.ch/cgi-bin/procgi.pl/www/iecwww.p?wwwlang=E&wwwprog=dirwg.p&ctnum=1186

The IEC60870-6 Telecontrol Application Service
Element 2 (TASE.2) protocol (informally known as the InterControl Center
Communications Protocol (ICCP)) was developed by IEC TC57 WG07 for data
exchange over Wide Area Networks (WANs) between a utility control center and
other control centers, other utilities, power plants and substations.

TASE.2 (ICCP) is used in almost every utility for
inter-control center communications between SCADA and/or EMS systems. It is
supported by most vendors of SCADA and EMS systems.

Since it was first developed in the mid 1990's before
object models had been developed for SCADA applications, TASE.2 (ICCP) was not
designed to support the transfer of different types of object models, beyond
those defined in Part 802.

The TASE.2 protocol allows for data exchange over
Wide Area Networks (WANs) between a utility control center and other control
centers, other utilities, power plants and substations.

·      
60870-6-503 Services and Protocol - This part of IEC 60870 defines a
mechanism for exchanging time-critical data between control centers. In
addition, it provides support for device control, general messaging
and control of programs at a remote control center. It defines a standardized
method of using the ISO 9506 Manufacturing Message Specification (MMS) services
to implement the exchange of data. The definition of TASE.2 consists of three
documents. This part of IEC 60870 defines the TASE.2 application modeling and
service definitions.

·      
60870-6-602 Transport Protocols - This Technical Report describes the
Transport Profiles for the IEC 60870-6 Series over WAN with Reference to
International Standardized Profiles (ISP’s) used by distributed SCADA/EMS
applications in control centers, power plants and
substations. The Transport Profiles use virtually any standard or de-facto
standard (including TCP/IP) connection-mode and connectionless-mode network
services over any type of transmission media.

·      
60870-6-702 Profiles - This specification defines the Application
Profile (Layers 5-7) for use with ICCP. It is needed for vendors implementing
protocol stacks that support the ICCP application layer. Most users of ICCP
will not be concerned with this specification.

·      
60870-6-802 Object Model - This part of IEC 60870 proposes object models
from which to define object instances. The object models represent objects for
transfer. The local system may not maintain a copy of every attribute of an
object instance.

**Keywords:**

#### IEC 61970 - CIM, CIM Extensions, and GID
