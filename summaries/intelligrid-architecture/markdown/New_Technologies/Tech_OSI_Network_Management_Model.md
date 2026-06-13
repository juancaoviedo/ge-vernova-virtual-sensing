# OSI Network Management Model

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_OSI_Network_Management_Model.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### OSI Network Management Model

and CMIP

**URL:** http://www.iso.org  
http://www.iech.ch

The
OSI Network Management model is a conceptual model for managing all
communication “entities” in a network, supported by the Common Management
Information Service and Protocol (CMIS/CMIP). It is based around the concept of
the abstract Management Information Base (MIB), consisting of all the data on a
given device describing the operation of the OSI protocol suite on that device.
CMIP accesses the MIB by extending the object-oriented paradigm over a
communications protocol. It permits instantiation of objects having classes,
attributes and inheritance, and allows them to generate events and alarms based
on the state of the real entities the objects represent. CMIP has also proven
to be effective for managing the behavior of any manner of devices and
processes in an object-oriented fashion, and is frequently used for this
function in addition to its original role in network management. The OSI
network management model is ISO/IEC 7498-4, 10164 and 10165; CMIS/CMIP is
ISO/IEC 9595 and 9596.

**Advantages/Strengths
of CMIP**

One
of CMIP's main advantages lies in the fact that not only can it query information
from the network elements, but it can also carry out actions (tasks) on network
elements that SNMP would find difficult or even impossible to carry out. For
instance, if a terminal on a network cannot reach its file server within a
predetermined number of times, then CMIP can notify the appropriate personnel
of that failure event.

In
addition, CMIP addresses many of the shortcomings of SNMP, including the
security loopholes (although SNMP has addressed some of these concerns in
SNMPv3). It has built in security that supports authorization, access control and security logs. CMIP is a powerful and easily
extensible protocol with flexible naming conventions (based on X.500) and event
driven. Couple that with an object-oriented model, connection-oriented communications and an unlimited data transfer length, and it
is easy to see why the protocol looks so good on paper.

Briefly,
the major advantages of CMIP over SNMP are:

·       CMIP variables
not only relay information, but also can be used to perform tasks. This is
impossible under SNMP.

·       CMIP is a safer
system as it has built in security that supports authorization, access control,
and security logs.

·       CMIP provides
powerful capabilities that allow management applications to accomplish more
with a single request.

·       CMIP provides
better reporting of unusual network conditions.

**Disadvantages/Weaknesses
of CMIP**

Unfortunately,
CMIP has two major disadvantages. Firstly, the amount of processing power
required to run CMIP 'powered' NMS is an order of magnitude more than that
required to run an SNMP NMS. This doesn't just apply to the NMS, but also to
each network element that can quickly mount up the cost of
implementation. This major disadvantage has no "work-around",
and therefore many people believe that the CMIP protocol is doomed to failure.
Additionally, CMIP is very complex thus making it difficult to program;
therefore skilled personnel with specialized training may be required to
deploy, maintain and operate a CMIP based network management system.

These
disadvantages have resulted in very few implementations of CMIP. However,
despite the disadvantages of CMIP, it is supported by a number of network
management systems including **Sun's Solstice® System**, **SpiderCMIP from Shiva** and **HP OpenView**® using the development
toolkit.

**Keywords:** protocol, network management, information model
