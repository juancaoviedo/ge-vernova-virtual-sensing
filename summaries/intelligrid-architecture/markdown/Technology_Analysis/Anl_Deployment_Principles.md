# Deployment Scenario Principles

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Deployment_Principles.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Deployment Scenario Principles

This section
previews Section 4 and briefly describes the principles used to define
guidelines for deploying IntelliGrid Architecture.  These
include:

if !supportLists?·      
endif?Deployment in layers

if !supportLists?·      
endif?Migration plans

### Enterprise Layering

An analysis of
this enterprise architecture brings us back to the fundamental goals of IntelliGrid Architecture project: The notion that we need a common framework for layering
information models and an information access model on top of one another to
support increasing levels of integration and abstraction.  Analysis applications on the enterprise
network need a global view of the enterprise as well as the ability to drill
down to more detailed view of data.  On
the other hand, operational applications need more detail so that operators may
make more immediate decisions.  Layering these
common information models and interfaces are the key to integrating the
previously un-integrated in a cost effective manner.

The previous
discussion of environments highlighted the diversity of deployment scenarios
for utility functions.  However, at a
higher level of abstraction, there is a set of “super environments” that must
be accommodated.  Table 0‑3 describes three levels of the enterprise:

|  |  |  |
| --- | --- | --- |
| Table 0‑3 Enterprise Levels | | |
| Level | Concerned with | Examples |
| Enterprise Level | Functioning of the utility business | if !supportLists?·       endif?Finance and risk management,  if !supportLists?·       endif?Resource planning and allocation  if !supportLists?·       endif?Enterprise security  if !supportLists?·       endif?Customer satisfaction  if !supportLists?·       endif?Wholesale and retail market operations |
| Operations | Operation of the overall power system | if !supportLists?·       endif?Energy management  if !supportLists?·       endif?Reliability, stability and optimization  if !supportLists?·       endif?Physical asset management  if !supportLists?·       endif?System/network management |
| Device | Monitoring and control of specific devices in real-time | if !supportLists?·       endif?Power system related IED’s such as protective relays and substation controllers.  if !supportLists?·       endif?Communication related devices such as routers and firewalls.  if !supportLists?·       endif?Computing hardware such as servers and workstations. |

 

Figure 22 illustrates how a utility might be constructed from
three general enterprise levels:

if !vml?![](Anl_Deployment_Principles_files/image002.gif)endif?

Figure 22 Utility Integration Layering

 

The levels are
significant because communication between levels is generally controlled to
some degree.  Applications at a higher
level may only see an aggregated view of applications at a lower level.  That is the specifics of how a multiple lower
level applications model data may be hidden at a higher level.  In some ways, a higher level should treat the
entire lower level as a black box. 

This does not mean
that lower level data is hidden from a higher level, only that the specifics of
how to communicate and the semantics of lower level applications may be wrapped
by a higher level communication mechanisms and semantics.   Some applications on the enterprise network
need both a global view of the enterprise as well as the ability to drill down
to more detailed view of data.

Discussion of
enterprise layering brings us back to one of the fundamental goals of IntelliGrid Architecture
project: The notion that we need a common framework for layering information
models and a common set of services to support increasing levels of integration
and abstraction. 

### Migration

Besides enterprise
layering, a second fundamental principle in the deployment of any given IntelliGrid Architecture
project will be migration of legacy technologies to the architecture.  IntelliGrid Architecture must outline migration paths for each
of the recommended technologies, either to be phased out or to be made
compatible with the architecture.
