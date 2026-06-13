# Application Integration

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Appl_Deploy.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Application Integration Deployment Scenario

This section describes how a deployment of the CIM and GID
can be used to create a platform for legacy application integration. This
migration strategy is based on the deployment of adapters that convert legacy
ways of modeling and exchanging data to CIM and GID.

if !vml?![](Anl_Appl_Deploy_files/image002.gif)endif?

Figure ‑13 Application Integration Scenario

 

In this case, a control center application integration
project is considered. This development integrates the following applications:

if !supportLists?·      
endif?Legacy EMS

if !supportLists?·      
endif?New archive, state estimator, and power flow

if !supportLists?·      
endif?Condition-based monitoring software

if !supportLists?·      
endif?CIM-based power system modeling environment

if !supportLists?·      
endif?Data Engineering Tool

This example
employed a CIM/GID-based message bus as illustrated in Figure 13.

In this example, adapters are used to connect the
applications to the CIM/GID-based Message
Bus.  These adapters server two purposes:

if !supportLists?·      
endif?What data is exchanged

if !supportLists?·      
endif?How data is exchanged

With regard to the internal representation of data within
applications or sets of tightly coupled applications, one can suggest that the
value to the utility of how an application natively models or exchanges data
internally is low. At the most, special analysis applications may only need to
browse the lineage of data (where it came from) for auditing/validation but not
details about native semantics[if !supportFootnotes?[20]endif?](Anl_Appl_Deploy.htm#_ftn20).  Consequently, application integration
provides a scenario where the semantics of each application may be assimilated
into the common model. 

With regard to how data is exchanged, IntelliGrid Architecture
recommendations for application integration include the use of  common model-enabled application integration
technology.  Specifically, instead of
using a cross-industry publish/subscribe API
to link applications, IntelliGrid Architecture-based application integration employs a CIM-enabled
publish/subscribe API such as IEC61970
Generic Eventing and Subscription.  Note
that both cross-industry and common model-enabled publish/subscribe API’s
are generic in that they can be applied to any application type and do not hard
code application specific semantics into the API.

In essence, applications and/or systems can continue to
use their internal data representation and exchange methodologies within their
own domains, but are required to map to the CIM APIs whenever data exchanges
involve external applications and/or systems.

This example illustrates the integration of transmission
related applications using the a message bus as shown in Figure 14:

if !vml?![](Anl_Appl_Deploy_files/image004.gif)endif?

Figure ‑14 Control Center Application Integration

 

Figure 15,
illustrates the specific GID interfaces
required to integrate the applications involved:

if !vml?![](Anl_Appl_Deploy_files/image006.gif)endif?

Figure ‑15 Specific GID
Interfaces Used For Application Integration

 

One advantage of this approach is that it facilitates
incremental upgrading of the EMS and other
systems, primarily within utility operations centers.  In this example, a new state estimator and
power flow application can be integrated with the legacy EMS
using a new CIM based data-engineering tool. 
The data-engineering tool supplies CIM model information to the new
state estimator and power flow application. 
The data-engineering tool also supplies a portion of the power system
model to the Measurement Data Server Adapter. 
As discussed previously, an application uses the GID
to expose information within the context of the CIM.  In this case, the Measurement Data Server
imports a small amount of the power model so that it can expose archive data
within a CIM context. 

Keeping the shared model in sync across multiple
cooperating components is an important task. 
The GID’s Generic Data Access Model
Change Events capabilities are used for this purpose. Figure 16 illustrates this process:

if !vml?![](Anl_Appl_Deploy_files/image008.gif)endif?

Figure ‑16 Data Synchronization

 

The steps of such a Use Case are listed below:

if !supportLists?1.     
endif?The
User adds a new breaker to the EMS system’s
power system model, using the EMS model
server via the modeling server’s GUI.

if !supportLists?2.     
endif?The EMS GDA Server publishes a GDA
Model Change Event onto the Integration Bus.

if !supportLists?3.     
endif?The Model Change Event is
received by the GDA Client in the Asset Management System adapter.  If there is a need to join EMS
and AMS data, a mapping from logical to
physical devices must be maintained.  It
is possible that this mapping will be done in the AMS
or EMS adapter as illustrated in Figure 17. 

if !supportLists?4.     
endif?The
User is prompted to map new logical breaker to new or existing physical breaker
in asset model using the AMS Adapter Mapping
GUI

if !supportLists?5.     
endif?The
archive wrapper also receives a Model Change Event.

if !supportLists?6.     
endif?In
some cases, the Archive may have the ability to create a new archive point on
the basis of a pre-configured template. 
If this is the case, then the Archive adapter can use this template and
the information in the Model Change Event to determine appropriate archive
configuration and add a new archive point automatically.

if !supportLists?7.     
endif?The
CIM model subset in archive is also automatically updated and archiving begins.
It is important to note that in order for the archive to present historical
data within a TC57 namespace, only a relatively small portion of the EMS
model must be maintained in the archive wrapper model manager.

if !vml?![](Anl_Appl_Deploy_files/image010.gif)endif?

Figure ‑17 Keeping the Mapping From Assets To the Power
System In Sync

 

This workflow example can also be applied to information
model changes such as the addition of a new attribute on a purchase order
class.  While these changes are somewhat
more difficult to automate among systems, GDA Model Change Events have been
design specifically to address both instance data and information model
changes.

This scenario shows how applications can be connected
together with adapters that can be supplied off the shelf.  The deployment of TC57 based technology can
lower cost significantly and thereby enable the creation of a single unified
integration architecture that heretofore would be too expensive.

Again, security, network/enterprise management, and data
management requirements need to be incorporated in this Use Case. Security
requirements are shown in IntelliGrid Architecture Intra-Control Center Environment, and
include:

if !supportLists?·      
endif?Authorization Service for Access Control

if !supportLists?·      
endif?Audit Service

if !supportLists?·      
endif?Security Policy Service

if !supportLists?·      
endif?User Profile and User Management

Network and enterprise management requirements, as also
shown in IntelliGrid Architecture Intra-Control Center Environment, can rely on readily
available standard technologies, such as the IETF’s Simple Network Management
Protocol (SNMP) and Web-Based Enterprise Management (WBEM).

Data management requirements, although greatly enhanced by
the available standards such as CIM and GDA, still need guidelines, additional
tools, and automated procedures that will allow actually implementation of
these concepts in the most efficacious manner.
