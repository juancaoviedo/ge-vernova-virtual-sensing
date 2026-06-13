# Architectural Analysis

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Arch_Analysis.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Architectural Analysis

A primary goal of
IntelliGrid Architecture project is designing a common architecture for utilities.  A key step in this process is discovery of
what is different and what is the same in a utility.  The diversity of utility software is captured
in a set of technologies and environments. 
Technologies correspond to **which** physical means information is
exchange by and are chosen on the basis of the Environment that corresponds to **where**
data is exchanged.  That is, which
technologies are used comprises an RM-ODP Technology View while the Environments
deployed in comprise an RM ODP
Deployment View of the utility.

The commonality of
a utility architecture is captured in a set of common modeling elements.  The IntelliGrid Architecture Common modeling elements include:

if !supportLists?·      
endif?Common Services 
– Common functions that correspond to the RM-ODP **activities** that that interact with
their environments. Common Services comprise an RM ODP Enterprise View of the utility.  Services are the atomic building blocks that
are frequently required in the utility enterprise.  Note that IntelliGrid Architecture Common Services are defined
for security, network management, data management and other non-utility
application specific capabilities.  The
rational for abstracting away from application specific functionality to a
reusable set of Common Services is discussed in high-level concepts text in the
previous section. 

if !supportLists?·      
endif?Common Information Models – Common data this is
exchanged between services.  Common
Information Models correspond to **what** data is exchanged. Common
Information Models comprise an RM ODP Information View of the utility.

if !supportLists?·      
endif?Generic Interfaces – Generic Interfaces are used
as the mechanism for exchanging Common Information Model data between
services.  Generic Interfaces correspond
to **how** data is exchanged. That is, Generic Interfaces comprise an RM ODP Computation View of the utility.

These common
modeling elements are discovered and derived through intensive architectural
analyses. This section describes the architectural analyses undertaken by IntelliGrid Architecture team. It also provides the common modeling element conclusions. Figure 18illustrates the relationship between services,
interfaces, and component packages.  This
section provides a description of these elements.  Further elaboration on the common modeling
elements can be found in the appendix.

Although this
section focuses on the commonalities, it is the objective of the following
section to unfold the diversity of the utility operations and provide
recommendations to the technology utilization, integration and harmonization.
Those technologies correspond to **which** physical means information is
exchanged by. That is, which technologies are used comprises an RM-ODP Technology View.
