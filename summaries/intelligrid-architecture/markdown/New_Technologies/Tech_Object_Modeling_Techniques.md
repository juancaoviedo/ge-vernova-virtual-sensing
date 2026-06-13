# Object Modeling Techniques

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Object_Modeling_Techniques.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Object Modeling Techniques

for
IEC61850-based Devices

When
an IEC61850-based device object model is
created, the following steps are used:

·       The information
exchange requirements are developed from the functional requirements or Use
Cases for different types of information exchanges*.*

·       Lists of data
are created, which are derived from the Use Cases and from vendor product
specifications. This provides the raw data for the objects

·       A block diagram
is created of the device, showing its different logical parts and functions,
focusing on the information exchange requirements.

·       These logical
parts or functions are further separated into one or more Logical Nodes (LNs).
A Logical Node is a logical grouping of objects required by a particular
function, which could be reused by many different devices. Many Logical Nodes
already exist in the IEC61850-7-4; these should be used if they meet the device
requirements. However, new Logical Nodes must be created to meet new needs,
such as those for the Distributed Resources environment.

·       Each logical
piece of data that may be exchanged between the Server and a Client is defined
as a ***data object***. Many data objects have already been defined in
the IEC61850-7-4, and should be used as defined. New data objects must be
defined when no existing IEC61850-7-4 objects can serve. Data objects may be
simple (e.g. open/close status of a switch), complex (e.g. all ratings and
static characteristics of a device), or an array (e.g. an array of bits
defining alarm reasons). Discussion among experts is sometimes required to
determine exactly what constitutes a particular data object.

·       Existing
IEC61850 Logical Nodes have their data objects already assigned to them. A new
IEC61850 Logical Node must have new and existing data objects assigned to it,
based on their logical role within the device model. Sometimes a data object
could be assigned to more than one Logical Node: therefore, a decision must be
made as to where it most logically lies.

·       Each type of
data object is also assigned to one of the ***Functional Component***
categories (e.g. the open-close status of a water valve is assigned to the ST
functional component category).

·       Each data object
is given a unique ***object name***, which must follow certain
guidelines, but should be relatively self-explanatory (e.g. the open-close
status of a switch is called SwDS, where DS stands for Device State). This name
is critical: it is the way that Clients and Servers can recognize what data is
being transmitted.

·       Each data object
is assigned a ***Common Data*** ***Class***, which defines what
format the data is in (e.g. SwDS is assigned to the CDC *SPS*, which is
defined as a two-bit binary, plus quality code, plus timestamp, plus
description). A CDC can be defined to be a single item, or, more usually, as a
structure of items (such as the SPS CDC, which consists of 4 items). If no
existing CDC can meet the requirements of the data element, then a new CDC must
be developed, following the procedures established for IEC61850.

·       Each data object
is defined as ***mandatory*** or ***optional*** or ***conditional***
(m/o/c column).

·       The meaning of
the ***values*** for each data object are defined; some are implicitly
defined by the type of Class, but certain Classes have flexibility in what values
might mean, so these must be clarified for each data element (e.g. for SwDS,
the two-bit status has the following meanings: 00 = between (in transit), 01 =
closed, 10 = open, 11 = invalid).

·       The ***reporting
objects*** are defined, based on the conditions under which each client
needs to receive data (e.g. SwDS should be reported to Client 1 anytime the
two-bit value or the quality code changes), and what groups (***Data Sets***)
of data objects should be reported. The actual rules for the reporting procedures
are defined in the IEC61850-7-2 standard. Once Data Sets are established on
either side of a link, then only the data (not the long names) can be sent over
the communications network.

**Keywords:**IEC61850, object models, objects, logical nodes
