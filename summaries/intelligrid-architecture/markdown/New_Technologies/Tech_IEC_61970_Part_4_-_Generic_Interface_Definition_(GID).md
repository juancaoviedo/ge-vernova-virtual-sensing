# IEC 61970 Part 4 - Generic Interface Definition (GID)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC_61970_Part_4_-_Generic_Interface_Definition_(GID).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC 61970 Part 4 - Generic Interface Definition (GID)

**URL:** 

The Generic Interface Definition (GID) is part of
IEC61970 and comprises Part 4

·      
61970-4 Component Interfaces - The purpose of the Part 4 CIS documents
is to specify the interfaces that a component shall use to facilitate
integration with other independently developed components. Although typical
applications and functions are identified in Annex B to assist in defining the
types of information that must be transferred, the purpose is not to attempt to
define components per se. The component vendors should be free to package
different collections of component interfaces into component packages while still
remaining compliant with the EMSAPI standards.

·      
401 - Part 401 provides a framework for the specification of the Level 1
Functional Requirements documents. It explains the separation of these
specifications into two major groups. One group of standards defines the
generic services that a component can use for exchanging information with
another component or for accessing public data. The other group defines the
information content of messages that a component or system exchanges with other
components. Part 401 provides an overview of the generic services defined for
the CIS standards. These specifications describe in narrative terms with text,
Unified Modeling Language (UML) notation, and Interface Definition Language
(IDL), the interface functionality that is standardized. These specifications
define the generic services that can be used by any application to exchange
information with another application or for public data access. It also
provides a roadmap to explain the contents of each of the specifications in
this series and the underlying industry de facto standards that are
incorporated.

·      
402 - These base services incorporate the following industry de facto
standards. 402 Includes IECTC57 Namespace - a mechanism by which the CIM is
presented via TC 57 API’s. That is, it is essentially an agreement on how to
communicate the CIM hierarchies via an OPC/DAIS API.

·      
403 - Generic Data Access. This part contains the API services that are
needed to access public data based on the CIM organization of information. In
other words, a client can access data maintained by another component (either
an application or database) or system without any knowledge of the logical
schema used for internal storage of the data. Knowledge of the CIM is
sufficient. This request and reply-oriented service is intended for
synchronous, non-real time access of complex data structures as opposed to
high-speed data access of SCADA data, for example, which is provided by Part
404, High Speed Data Access. An example where Request and Reply would be used
is for bulk data access of a persistent store to initialize a State Estimator
application with the current state of a transmission network, and then storage
of the results with notification.

·      
404 - High Speed Data Access. This part contains the API services needed
for high-speed access of simple data structures, where multiple instances are
typically accessed as a data group and need to be efficiently mapped to
variables in the client memory space. Typically data groups will be predefined
and then published at either periodic intervals or upon change, although it is
also possible to use this API with a request and reply data exchange pattern
for these same data groups.

·      
405 - Generic Eventing and Subscription. This part contains the API
services needed for a general-purpose capability to publish and subscribe to
events and alarms. This includes the ability to publish and subscribe to
topics. It also supports the event “send and forget” data exchange pattern,
where events are simply published once, with no knowledge on the part of the
server of the intended recipients. An example application is for alarms, where
the server capability to publish alarm events and the client capability to
subscribe to selected alarms is needed.

·      
407 - Time Series Data Access. . This part contains the API services
needed for access time series data. This includes the ability for request/reply
as well as publish/subscribe oriented exchanges.

**Keywords:**

#### OPC

**URL:**www.opcfoundation.org

OPC is a foundation dedicated to open connectivity in
industrial automation and the enterprise systems that support industry. To this
aim, OPC has created a series of open standards specifications with the goal of
assuring interoperability. Based on fundamental standards and technology of the
general computing market, the OPC Foundation adapts and creates specifications
that fill industry-specific needs. OPC will continue to create new standards as
needs arise and to adapt existing standards to utilize new technology. There
are currently seven standards specifications completed or in development, of
which the following four are the most important to the power industry.
