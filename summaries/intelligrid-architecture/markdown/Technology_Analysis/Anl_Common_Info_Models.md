# Common Information Models

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Common_Info_Models.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Common Information Models

In order to
precisely describe the meaning of a set of terms, engineers often create an
information model. An information model describes a collection of related real
world objects. An information model describes objects in terms of classes,
attributes and relationships and provides unique names and definitions to each
object.  This section describes what an
information model is and how it is typically used as well some example
information models.

### Enterprise Management Common Information Models

The IntelliGrid Architecture
Enterprise Management Information
Model represents the structure and storage of the information and their
relationship. The commonly used term of *Structure of Management Information*
(SMI) refers to the representation of objects,
its syntax and their management semantics. The *Management Information Base*
(MIB) stores the objects used by both agents and managers. The various
enterprise management architectures vary in the details of their information
model and one approach for integration of the various systems is to map the
information from one into the other.

Examples of common
information models used in the industry are Simple Network Management Protocol
(SNMP) SMI, OSI SMI, and the newly developed Web-Based
Enterprise Management (WBEM) Common Information Model (CIM).

 

**NOTE:** The DMTF/WBEM Common Information Model
models different objects and was developed by a different group of people than
the IEC Common Information Model.  The
DMTF CIM models data for Enterprise Management and the IEC CIM models data for
power systems.

 

SNMP objects,
consists of an object identifier, syntax, and encoding. SMI is the language used to define the
management information residing in a managed network entity. Such a definition
is needed to ensure that the syntax and semantics of the network management
data are well defined and unambiguous.  RFC 2578[if !supportFootnotes?[5]endif?](Anl_Common_Info_Models.htm#_ftn5) specifies the basic data types in the SMI MIB module-definition language. Although the
SMI is based on the ISO ASN.1 (Abstract Syntax Notation One)
object-definition language, considerable SMI-specific data types have been added to ISO ASN.1.  In
addition to the basic data types, the SMI data definition language also provides
higher-level constructs, such as the "OBJECT-TYPE" construct, which
specifies the data type, status and semantics of a managed object.  There are nearly 10,000 defined objects in
various Internet RFCs. There is also the "MODULE-IDENTITY" construct,
which allows related objects to be grouped together within a module.  In addition to containing   the OBJECT-TYPE definitions and the managed
objects within the module, the MODULE-IDENTITY construct contains clauses to
document contact information of the author of the module, the date of last
update, a revision history and a textual description of the module. For more
details[if !supportFootnotes?[6]endif?](Anl_Common_Info_Models.htm#_ftn6).

Unlike SNMP, the OSI SMI is truly object oriented and utilizes the
concepts of inheritance. For more details on OSI SMI, see[if !supportFootnotes?[7]endif?](Anl_Common_Info_Models.htm#_ftn7).

WBEM[if !supportFootnotes?[8]endif?](Anl_Common_Info_Models.htm#_ftn8) developed CIM, an object-oriented information model. Allowing CIM information to be
represented in eXtensible Markup Language (XML) brings the benefits of XML and its related technologies to
management information, which uses the CIM meta-model. The XML encoding
specification defines XML elements, written in Document Type Definition (DTD),
which is used to represent CIM classes and instances. The encoded XML message
could be encapsulated within HTTP. Further, WBEM defines a mapping of CIM
operations onto HTTP that allows implementations of CIM to operate in a
standardized manner.

### Power Systems Common Information Models

For power systems,
the EPRI/IEC Common Information Model (CIM) provides an example of an IntelliGrid Architecture
Information Model.  The CIM describes
data typically used in a utility’s operational systems. In general, the benefit of creating
an information model include:

if !supportLists?·       
endif?Models give context to data
improving understanding and productivity.

if !supportLists?·       
endif?Models enable automation of setup
and maintenance tasks.

The diagram below illustrates a sample information model.

 

if !vml?![](Anl_Common_Info_Models_files/image002.gif)endif?

Figure
‑15 Example Information Model

 

In the CIM based example above, Power System Resource
is the parent class of all logical equipment, such as circuit breakers, and
equipment containers, such as a substation. In the CIM, the term “asset” refers
to a physical object. Assets are associated one to one with logical equipment.
Assets exist at a location that can be represented on a map. Elsewhere, the
IEC61968 CIM also defines a parent document class. Outage reports, equipment
lists, work orders, and inspection schedules are sub types of the document
class. An outage report contains an equipment list that refers to one or more
assets. And so on.

It is important to note that an information
model does not model utility data in an application-specific way. An
information model is used to model data aggregated by many different
applications and not what is modeled by a single application internally.
Without a common model by which to exchange data, utilities are often required
to perform many custom data transformations in order to integrate
applications. 

It is also important to note that an information
model is not a database schema or even in a database at all.  For example when used for application
integration, each application communicates using the same common model,
but this model may only be realized in the structure of the messages. Using a
common model in this way reduces the number of data transformations required
from N \* (N-1) to N. In this case, integrating legacy applications typically
involves the creation of application wrappers that map legacy data formats to a
common one as shown in Figure
16.

 

if !vml?![](Anl_Common_Info_Models_files/image004.gif)endif?

Figure
16 Use
of a Common Exchange Model
