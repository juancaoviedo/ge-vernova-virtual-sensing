# Energy Market Integration

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Market_Deploy.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Energy Market Integration Deployment Scenario

The Energy Market Integration deployment scenario
describes how a utility might integrate Energy Market Transaction Servers with
utility operational systems, discussing the management of what data is
exchanged and how data is exchanged.

Energy markets are in a state of flux at this time, and
will most likely never result in a single market environment. Therefore, this
deployment scenario raises interesting questions about how much can or should
be standardized and how much must be left to changing circumstances. Although
these questions are true to some degree for all environments, the market
operations environment is particularly changeable.

Therefore, a uniform strategy for complete energy market
transaction service integration may not be possible.  While it is clear that CME
based transaction servers can be integrated with the CIM with much difficulty,
ETSO and eTagging-based energy trading systems present the a more complex
deployment scenario from the point of view of managing semantic
heterogeneity.  The reason is that unlike
internal application or data integration where data semantics can be
assimilated, the exact meaning of external energy trading may not be able to be
modified. That is, instead of creating adapters to transform the meaning of
data, energy market data must be reproduced more exactly for use in analysis
applications. 

At the same time, energy market semantics do often
conflict with operational semantics.  For
example, ETSO and NERC eTagging messaging models were developed independently
of the CIM.  As a result, utilities may
not be able to achieve complete harmonization of market and operational
semantics.  In this case, the best that
can be done is to precisely describe the differences rather than attempt to
change the different semantics. 
Fortunately, as described in Section 3, RDF and OWL provide this
capability. 

In practice RDF and OWL can be used to describe the
differences in information models in a precise computer digestible way.  Since both ETSO and NERC have only defined a
set of message schemas and not unified information models, an information model
will need to be derived from the message schemas and then linked to the CIM/CME
classes and properties.  

With regard to how data is exchanged, generally IntelliGrid Architecture-based
energy market server integration recommends the use of information model
technologies by market applications, including the use of electronically
available metadata of these information models so that their names, structures,
and differences are discoverable. 
Specifically, instead of using a simple message passing API
to link applications, IntelliGrid Architecture-based application integration employs a complex
model-enabled message passing and data access API’s
such as IEC61970 Generic Eventing and Subscription and Generic Data
Access.  Note that both cross-industry as
well as the model-enabled GID API’s
are generic in that they can be applied to any message type and do not hard
code message specific semantics into the API.

The diagram below depicts an ETSO ebXML or NERC
eTagging-based Energy Market network:

if !vml?![](Anl_Market_Deploy_files/image002.gif)endif?

 

Figure ‑22 ETSO ebXML Or NERC eTagging Based Energy
Market Server

 

 

Figure
22 illustrates a utility energy market server
communicating with external trading partners via the Internet.  In order to perform analysis, this energy
market data must be integrated with the rest of the utility enterprise (subject
to the market rules on authorized access). 

if !vml?![](Anl_Market_Deploy_files/image004.gif)endif?

Figure ‑23 CME
Based Integrated Energy Market Systems

 

Figure
23 illustrates a GID
based adapter that exposes a CME information
model.  That is, the GID
has the capability to expose a namespace created in accordance with harmonized
CIM/CME models. 

 

if !vml?![](Anl_Market_Deploy_files/image006.gif)endif?

Figure ‑24 ETSO or eTagging Based Integrated Energy
Market Systems

 

Figure
24 illustrates a GID
based adapter that not only exposes an eTagging or ETSO information model but
also their exact semantic relationship to CIM/CME.  That is, the GID
has the capability to not only expose a single information model, but also
multiple associated models as well as their inter relationship. 

The question remains how well an analysis application can
perform over this semantic infrastructure. 
In the case of a CME based market
server, an analysis application can perform calculations based on a set of
known facts.  In the case of an ETSO or
eTagging based market server, an analysis application can only perform
calculations based on a set of inferences. 
An inference is a conclusion based on data that is not completely semantically
uniform.  Inferencing technology is a
rapidly growing field of study particularly as it applies to analysis and
searching of Web based resources. 
However, its use has yet to be tested or proven in a more critical
environment.

Again, security, network/enterprise management, and data
management requirements need to be incorporated in this Use Case. The security
requirements are shown in IntelliGrid Architecture RTO to Market Participants Environment are
much more extensive than for the previous Use Cases, and include:

if !supportLists?·      
endif?Identity Establishment Service

if !supportLists?·      
endif?Authorization Service for Access Control

if !supportLists?·      
endif?Information Integrity Service

if !supportLists?·      
endif?Confidentiality Service

if !supportLists?·      
endif?Security Against Denial-of-Service Service

if !supportLists?·      
endif?Inter-Domain Security Service

if !supportLists?·      
endif?Non-repudiation Service

if !supportLists?·      
endif?Security Assurance Service

if !supportLists?·      
endif?Audit Service

if !supportLists?·      
endif?Security Policy Service

if !supportLists?·      
endif?Path and Routing Quality of Security 

if !supportLists?·      
endif?Firewall Transversal

if !supportLists?·      
endif?Privacy Service

if !supportLists?·      
endif?User Profile and User Management

if !supportLists?·      
endif?Security Protocol mapping

if !supportLists?·      
endif?Security Discovery 

Network and enterprise management requirements, as also
shown in IntelliGrid Architecture RTO to Market Participants Environment, can rely on readily
available standard technologies, such as the IETF’s Simple Network Management
Protocol (SNMP) and Web-Based Enterprise Management (WBEM).

Data management requirements, as discussed in this Use
Case, is much more difficult than in the other Use Cases described in this
section, since common information models will most likely never be standardized
or implemented globally. Therefore, data management will have to rely much more
heavily on metadata discovery of the individual market information models, and
as much automated mapping as possible through the capabilities described above,
and through technologies such as RDF. Again, the need for guidelines, tools,
and automated methodologies is paramount to simplifying this complex task.
