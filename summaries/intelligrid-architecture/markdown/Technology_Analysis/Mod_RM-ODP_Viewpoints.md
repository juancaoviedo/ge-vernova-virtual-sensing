# RM-ODP Viewpoints

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Mod_RM-ODP_Viewpoints.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# RM-ODP Viewpoints: Use of RM-ODP and UML Mapping

The charter of IntelliGrid Architecture is to use a rigorous,
standard modeling methodology. The selected methodology is the International
Organization for Standardization (ISO 10742) Reference Model for Open
Distributed Processing (RM-ODP). RM-ODP, ITU-T Rec. X.901  | ISO/IEC 10746-1 to ITU-T Rec. X.904 |
ISO/IEC 10746-4 [5][6][7][8], provides a framework to support the development of
standards that will support distributed processing in heterogeneous
environments. It is based, as far as possible, on the use of formal description
techniques for specification of the architecture. In support of the generic
design goals, it facilitates specifying integration architecture with the
following properties: openness, flexibility, modularity, federation,
manageability, and provisions for quality of service, security and transparency[3]. Thus, the team has selected RM-ODP as the enterprise
architecture framework for IntelliGrid Architecture.

In the section, we describe RM-ODP and the
modeling concepts used in IntelliGrid Architecture. The team extended the RM-ODP by including
domain specific concepts such as *common services* to represent generic
interfaces and functions that the power system distributed computing system
will use.

RM-ODP is silent on the notation to be used
for rendering architectures. Thus, the team selected the Unified Modeling
Language (UML) [4] tool to provide most of the notation support capabilities
for RM-ODP. The mapping between RM-ODP concepts and UML constructs will be
discussed further below.

## Reference Model for Open Distributed Processing

RM-ODP uses an object modeling approach to
describe distributed systems. Two structuring approaches are used to simplify
the problems of design in large complex systems: five 'viewpoints' provide
different ways of describing the system; and eight 'transparencies' identify
specific problems unique to distributed systems which distributed system standards
may wish to address. Each viewpoint is associated with a language, which can be
used to describe systems from that viewpoint.

if !vml?![](Mod_RM-ODP_Viewpoints_files/image002.gif)endif?

Figure 1: Descriptions of the RM-ODP Standards

 

| **Part** | **Name** | **ITU Standard /   ISO Standard** | **Description** |
| --- | --- | --- | --- |
| 1 | Overview | ITU-T Rec. X.901 /  ISO/IEC 10746-1[5] | The Overview contains justification and explanation of key concepts. The overview begins with the initial list of enterprise activities that facilitate the stakeholder engagement process.  Utilizing a rigorous template (Domain Template), IntelliGrid Architecture interacts with stakeholders to elaborate a set of use cases and architectural requirements, which contribute to the key concepts, interfaces, actors and constraints used to define the architecture. |
| 2 | Foundation | ITU-T Rec. X.902 /  ISO/IEC 10746-2[6] | The Foundation contains the definition of concepts. The UML modeling constructs applied to RM-ODP provides the foundation for the modeling activity.  The modeling tool, in conjunction with the RM-ODP to UML mappings, provides the foundation for the modeling activity.  The MagicDrawÔ tool also provides the team with the capability to cooperate on the development of the model. |
| 3 | Architecture | ITU-T Rec. X.903 /  ISO/IEC 10746-3[7] | The Architecture contains the specification of the required characteristics that qualify distributed processing as open. As the stakeholder inputs are analyzed, the orthogonal viewpoints help to focus the team on details that enable the distributed processing. |
| 4 | Architectural Semantics | ITU-T Rec. X.904 /  ISO 10746-4[8] | The Architectural Semantics contains a formalization of the modeling concepts. Formal notation can be used in conjunction with the modeling tool to specify the constraints and semantics of the architecture. |

Table 1
Description of the RM-ODP Standards

The above table presents the structure of
RM-ODP standard as well as its viewpoints, namely enterprise, information,
computational, engineering and technology viewpoints.

### Enterprise Viewpoint

The *enterprise viewpoint* represents
the business model and the business requirements. This view should be
understandable by all stakeholders in the business environment. It is the
viewpoint used to communicate the business needs to the architecture. The
viewpoint is concerned with purpose, scope, and policies of the enterprise. The
enterprise view of IntelliGrid Architecture provides the business objectives, roles, policies and
the environment with which the enterprise interacts. It covers the role of the
systems in the business as well as the human user roles and business policies.

The key concepts we used in the enterprise
viewpoint are:

**Purpose and objectives** – In RM-ODP,
“purpose and objectives” concept is used to capture the reason for the system.
It defines a set of objects formed to meet an objective, their activities, and
processes in which the system participates. For example, the purpose and
objective of the ‘Base RTP Calculation’ function is defined as:

“To develop tables of load versus price for
each *power system node* and for each *settlement* period. These
tables are the Base RTP data. The purpose of this computation is to accurately
forecast the cost of providing energy during the period.”

**Domain** – In RM-ODP, a domain is a set
of objects with a characterizing relationship, and with a control object that
may be part of the domain or outside it [3]. In IntelliGrid Architecture, a domain is a grouping of enterprise
activities that fall into a natural boundary of the power system operations.
IntelliGrid Architecture partitions the entire architecture into five domains, namely, *Market
Operations, Primary Generation, Transmission Operations, Distribution
Operations, and Distributed Resources.*

**Activity/Enterprise Activity** – In
RM-ODP, an activity is an ordered set of actions. In IntelliGrid Architecture, we use this concept
as well as the term enterprise activity as a specific power system operation.
For example, in the Base RTP Calculation, “Load Forecasting” is an enterprise
activity. This activity is an ordered set of actions, which result in providing
accurate estimates of load at various points in the settlement intervals.

**Community** – As defined in RM-ODP [3], a configuration of interacting objects whose purpose
is to fulfill an objective according to a contract defining how the objective
can be met.  *Market Operators* and *Energy
Service Providers* are examples of communities.

**Actor/Artifact** – An actor is an
enterprise object, a person or a system, which plays a role in the enterprise
view. When the actor is a piece of data/information, we use the term Artifact*.
Load Forecasting Function* and *Market Interface Server* are examples
of actors in the Market *Operators’* community.

**Role** – A unique identifier that
characterizes some behavior [3]. A role defines the behavior of the objects within
the community.

**Scope** – The set of roles, which define
a business, is the scope of that business.

**Contract** – As defined in RM-ODP [3], a specified agreement to some behavior common to a
configuration of objects, that tells the environment what to expect.

**Policy** – RM-ODP defines contract [3] as a set of obligation, prohibition, or permission
rules that either constrain or enable actions, as related to the purpose. A
contract contains zero or more policies.

### Information Viewpoint

The *information viewpoint* is concerned
with the semantics of information and information processing. The information
specification of IntelliGrid Architecture is a model of the information that it holds and of the
changes to that information. The information viewpoint is similar to object
models such as the IEC61970 Common Information Model (CIM) and Utility
Communications Architecture’s (UCAÒ)
Generic Object Model for Substation and Feeder Equipment (GOMSFE).

The key concepts we used in the information
viewpoint are:

**Information
Objects** – The set of objects
in the information viewpoint. This set of objects includes the information
objects used in interactions as well as the objects carried from the enterprise
viewpoint actors and artifacts. For example, in Base RTP Calculation, *Marginal Energy Cost*is
the information object that represents the table of marginal energy
costs for the power system.

**Association** – Defines the relationship between
the information objects. For example the association between the *Market
Operator* and *Energy Service Provider* that is providing regular and continuous RTP base rates for ESP
to calculate RTP customer rates.

**Contract** – As defined in the enterprise
viewpoint. For example in BaseRTP Calculation a contract is the *RTP Tariffs* which
dictates the conditions and limits and
tariff of the RTP contract that can be entered with customer.

**Policy** – As defined in the
enterprise viewpoint. An example is a security policy, which must be
established and used to address all security, needs
at the appropriate/contracted levels.

### Computational Viewpoint

The *computational viewpoint* is
concerned with the interaction patterns between the components (services) of
IntelliGrid Architecture, described through their interfaces. A computational specification of
a service is a model of the service interfaces seen from a client, and the
potential set of other services required by that service. The computational
model defines types of interfaces such as request/reply or publish/subscribe or
whether an interface is designed for exchange of real time or historical data
or both. Example interfaces include Application Programming Interfaces (API’s)
such as Control Center API’s (CCAPI) Generic Interface Definition and UCAÒ’s device oriented Common Application
Service Model (CASM) services.

The key concepts we used in the enterprise
viewpoint are:

**Computational
Objects/Components** – Objects
that interact at interfaces. The set of computational objects were carried from
those defined in enterprise and information viewpoints. For example, in BaseRTP
Calculation *Base RTP Calculator* and *Market Interface Server* are
objects.

**Interactions** – RM-ODP defines [3] interaction as an action that involves one or more
objects and their environment(s) at an interface; set of services that are
offered across a single interface, and are linked to another object with a
binding.

**Interface** – According to RM-ODP, an interface
defines the behavior of an object at a subset of the object’s interactions
constrained by the circumstances for when they occur. An **operation** interface is a type of interface where the interactions
are of type **interrogation**
(request-response) or **announcement** (publish-subscribe). For example, in BaseRTP Calculation *Base
RTP Calculator* interacts with *Market Interface Server,* postingRTP
tables on *Market Interface Server* for ESPs to access/download, through
an interface defined by the *set* operations*.*

**Binding** – RM-ODP defines binding as a
contract between two or more object interfaces that is the result of an agreed
upon behavior.  Bindings support the
interfaces and provide the environment where the interactions can be executed.

**QoS** - Various metrics of Quality of
Service, such as bandwidth, delay and reliability requirements have been used
in IntelliGrid Architecture computational viewpoint.

### Engineering Viewpoint

The *engineering viewpoint* is concerned
with the design of distributed systems. 
Since IntelliGrid Architecture is an architecture framework, independent of implementation
and outside the scope of the current charter of IntelliGrid Architecture.  Future works, based on IECA man contribute to
the definition of the engineering viewpoint.

### Technology Viewpoint

The *technology viewpoint* is concerned
with the provision of an underlying infrastructure. It focuses on the
technologies and the products for implementation. Even though IntelliGrid Architecture is an
architecture framework, the team felt that there are technology considerations
that can be made independent of exact implementation. The technology viewpoint
of IntelliGrid Architecture discusses the technologies, best practices, and standard activities
that can support the environments of IntelliGrid Architecture. It includes the various
alternatives, and identifies technological gaps.

### RM-ODP Rules

In order to maintain consistency among these
viewpoints, RM-ODP puts forth a set of basic rules, object model rules,
structuring and specification rules, and conformance rules. The structuring and
specification rules include organization, properties, naming, behavior, as well
as abstraction, refinement, and composition concepts, which provide unique
capabilities to architect a system. The object model rules provide the powerful
concepts of multiple types that an object can assume, and multiple interfaces
that an object can offer. The OMG and others have accepted these rules and
concepts for specifying a complete characterization of the enterprise.

By design, RM-ODP does not define a specific
notation for rendering architectures. This choice is left to the architects and
as such the team has not been able to identify suitable commercial tools that
directly support its concepts. However, the team has selected OMG’s Unified
Modeling Language (UML) for the architecture specification and rendering.

## RM-ODP to UML Mappings

The team developed a cross reference for
mapping RM-ODP concepts into UML for the purposes of describing IntelliGrid Architecture. A
mapping between RM-ODP and UML is needed since RM-ODP represents powerful
modeling concepts and provides an abstract framework for defining distributed
systems, however, it does not define the notation for describing its
constructs.  On the other hand, UML
provides a rich notational syntax, but lacks the higher order constructs needed
describe a distributed architecture. By analogy, we could say that UML provides
a rich vocabulary and alphabet, but does not have the elements to describe a
literary work.

Even though UML provides a rich notational
syntax, some of the RM-ODP constructs do not have a direct correspondence in
UML. While RM-ODP is gaining in popularity, there are relatively few
comprehensive references illustrating a complex architecture and the references
that do exist, use a different notation for the same RM-ODP constructs. As IntelliGrid Architecture project began, it became obvious that the team needed to standardize on
the notation of certain RM-ODP constructs in order to ensure consistency in the
design.

Adopting UML as the notation used to describe
RM-ODP constructs also exploits the ability of software engineering tools to
test the operation of the architectural components and to observe the
“consequences” of the design choices. Decisions to use certain notational
constructs will affect the ability to enforce design consistency in the
engineering tools. For complex systems it is absolutely critical to choose the
representation that best exploits the consistency and validation checks
available in the modeling tool.

As a result of our research into the mapping
of RM-ODP to UML, it is clear that others are struggling with these notational
constructs of RM-ODP and have differing opinions on how to best map RM-ODP to
UML. For the mapping between RM-ODP viewpoints to UML, we started from the
approximate mapping selected by [17] and created IntelliGrid Architecture specific mapping with domain
specific considerations. The details of the mappings are described in Section 4 as well as in Appendix B of this document.
