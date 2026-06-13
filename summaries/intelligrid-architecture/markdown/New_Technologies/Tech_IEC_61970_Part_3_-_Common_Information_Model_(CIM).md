# IEC 61970 Part 3 - Common Information Model (CIM)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC_61970_Part_3_-_Common_Information_Model_(CIM).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC 61970 Part 3 - Common Information Model (CIM)

**URL:**http://www.iec.ch/cgi-bin/procgi.pl/www/iecwww.p?wwwlang=E&wwwprog=dirwg.p&ctnum=1634

The Common Information Model (CIM) is an abstract
model that represents all the major power system objects in an electric utility
enterprise, including some organizational and ownership aspects, but focusing
on power system connectivity. The “instantiation” of a CIM power system model
(conversion from an abstract model into a specific configuration of a specific
utility’s power system) provides the information that is typically needed by
power flow topology models used by multiple applications, such as the EMS and
DMS Network Analysis applications. This model includes public classes and
attributes for these objects, as well as the relationships between them.

The CIM was initially developed under the aegis of
EPRI as the Control Center API (CCAPI) research project (RP-3654-1) project. It
is currently undergoing standardization through the IEC TC57 WG13, as the
document IEC 61970. The following descriptions of the CCAPI concepts are
derived from excerpts from the introduction to the IEC document and other
submissions to the IEC.

The purpose of the CIM is to produce standard interface
specifications for "plug-in" applications for an electric utility
power control center Energy Management System (EMS) or other system performing
the same or similar functions. A "plug-in" application is defined to
be software that may be installed on a system with minimal effort and no
modification of source code. This standard facilitates installation of the same
application program on different platforms by reducing the efforts currently
required.

·      
61970-1 Guidelines and General Requirements - This part of the standard,
IEC 61970-1, provides a set of guidelines and general infrastructure
capabilities needed for the application of the EMSAPI interface standards. This
part describes the reference model that provides the framework for the
application of the other parts of the EMSAPI standards. This reference model is
based on component technology that places the focus of the standards on
component interfaces for information exchange between applications in a control
center environment. The model is also applicable to similar information
exchanges between control center applications and systems external to the
control center environment, such as Distribution Management Systems (DMS).

·      
61970-2 Glossary

·      
61970-3 Information Model - This part of the standard, IEC 61970-301,
defines the CIM Base set of packages, which provides a logical view of the
physical aspects of Energy Management System information. Part IEC 61970-302 defines
the financial and energy scheduling logical view. Part IEC 61970-303 defines
the SCADA logical view. The CIM is an abstract model that represents all the
major objects in an electric utility enterprise typically needed to model the
operational aspects of a utility. This model includes public classes and
attributes for these objects, as well as the relationships between them.

·      
61970-5 Interface Technology Mapping. Since the Level 1 CIS documents
are independent by design of the underlying infrastructure technology, they
must be mapped to specific technologies for implementation purposes. To ensure
interoperability, there must be a standard mapping for each interface to each
technology. For example, if Java is the chosen implementation technology, then
there needs to be a standard mapping of the publishing and event subscription
services specified in the Level 2 CIS document to Java services.

**Keywords:** Object modeling, UML, Enterprise VP, Computational VP
