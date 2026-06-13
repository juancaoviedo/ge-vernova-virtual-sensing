# Tactical Approach

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Tach_Approach.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Tactical Approach

This section
previews Section 2 of this Volume that discusses the principles used to define
IntelliGrid Architecture at the tactical, day-to-day level. 
These include:

if !supportLists?·      
endif?IntelliGrid Architecture environments – a discussion of the
diversity of where IntelliGrid Architecture can be applied.

if !supportLists?·      
endif?Common Modeling Elements – a discussion of
technology independent utility commonality that includes common services,
information models, and interfaces.

if !supportLists?·      
endif?Assessment of technologies – a discussion of the
diversity of solutions that used to implement the common modeling elements
within the confines of specific environments.

To get a better
sense of what all IntelliGrid Architecture terms mean consider the diagram below:

if !vml?![](Anl_Tach_Approach_files/image002.gif)endif?

Figure
18 Diagram of Components, Services, and Interfaces

 

The previous
sections describe a technology-independent architecture that in an abstract way
describes a design for interoperation integration solutions.  However, when applying the architecture to a
specific problem, real, tangible technologies must be used.  In other words, the architecture must be
realized using concrete technologies that are suitable for each operating
environment that the architecture gets deployed in.  IntelliGrid Architecture is based on a technology-independent
set of common modeling elements, and also provides a technology assessment to
facilitate the decision of how to implement the architecture in each
environment.

**NOTE**:  Within IntelliGrid Architecture, the term “technology” is used
to encompass any protocols, international standards, best practices,
regulations, de facto standards or conventions that enable the integration of
the communications network.

### Environments

The IntelliGrid Architecture team has
categorized common requirements into a series of non-mutually exclusive sets
called Environments.  An IntelliGrid Architecture
Environment typically is associated with a location or network where one or
more of the information exchanges of Power System Operations functions have
essentially the same technical requirements, including:

if !supportLists?·      
endif?Configuration requirements

if !supportLists?·      
endif?Quality of service requirements

if !supportLists?·      
endif?Security requirements

if !supportLists?·      
endif?Data management and exchange requirements

Environments
correspond to **where** data is exchanged. 
That is, environments consist of an RM-ODP Deployment View of the utility. The details
of IntelliGrid Architecture environments and the recommended technologies to be used in each
environment to implement the common modeling elements are discussed in later
sections and in the Appendix D to this volume.

### Technology Independent Architecture

Successful
integration of a utility’s various systems requires a method that does not
require existing applications to be disturbed. Typically, integration is
performed by employing a run-time integration infrastructure and component
adapters.  The run-time integration
infrastructure provides a common platform for component links.

Adapters for
existing applications provide a standardized interface on a legacy
component.  That is, adapters accommodate
heterogeneity due to difference in:

if !supportLists?·      
endif?Data Management and Exchange Technologies

if !supportLists?·      
endif?Platform Technologies

if !supportLists?·      
endif?Communications Infrastructure Technologies

if !supportLists?·      
endif?Security Technologies

This architecture
is illustrated below:

if !vml?![](Anl_Tach_Approach_files/image004.gif)endif?

Figure 19 Adapters Use

 

As seen above, the
primary problem in power system data management is the wide variety of
platforms, protocols, data management and exchange, and security technologies
that need to be integrated.  The IntelliGrid Architecture
proposal is to define common modeling elements that can be mapped onto a
variety of technologies as needed, using adapters around a core of integration
infrastructure.    

While adapters can
accommodate the above listed heterogeneity, to achieve interoperability using **off
the shelf** components, it needs **standards** for what data and how data
is exchanged.  Furthermore, these
standard information models and interfaces must be applicable to the variety of
utility services.  A standardized common
information model solves “what” is exchanged. 
A standardized set of abstract interfaces solves “how” data is exchanged.  Given that a single technology for every
environment will never be agreed upon, adapters will very often still be
required to convert between differing technologies. 

Figure 20 illustrates the concept of an architecture that is
technology independent, based on standard common services, a common information
model, and generic interfaces to connect it together. 

if !vml?![](Anl_Tach_Approach_files/image006.gif)endif?

Figure 20 Technology-Independent Architecture

 

### Technology Assessment

Part of
architecture analysis is identification and evaluation of the various
technologies needed to support the implementation of IntelliGrid Architecture common functions and
services. The technologies were identified using the requirements gathered from
stakeholders and organized according to the following major areas:

if !supportLists?·      
endif?Enterprise Management Technologies, including
network management and system management.

if !supportLists?·      
endif?Data Management and Exchange Technologies
including configuration, format, and exchange of utility-specific data.

if !supportLists?·      
endif?Platform Technologies, the base level
technologies used to provide an operating environment for applications.

if !supportLists?·      
endif?Communications Infrastructure Technologies, the
technologies to move data within a network.

if !supportLists?·      
endif?Security of the information carried on the
communications network.

A complete list of
technologies considered are provided in Appendix D. A key subset of these
technologies was further analyzed and elaborated on in order to provide a more
complete assessment. This analysis appears in Section 3. The team analyzed the
technologies in an effort to identify relevance, ability to best meet the
requirements and vendor support. Clearly, based on these criteria, in many
cases, the resulting analysis concluded with multiple competing and overlapping
technologies which can be used to support a given common service or function.
The team tried to compare the various competing technologies, discuss the
trade-offs and provide an unbiased assessment. With multiple competing
technologies, in some cases it is possible to provide an umbrella platform to
integrate and unify a federation of different technologies co-existing within
IntelliGrid Architecture. In such cases, the team provided proposal for this unification. In a
number of areas, gaps and missing technologies were identified and documented.
The team has also provided a more comprehensive analysis in form of a
spreadsheet to assess the relevance of each specific technology in fulfilling
the given user and system requirements. This spreadsheet can be found in
Appendix C. There is also another spreadsheet provided in Appendix D that
presents in detail the applicability of each individual technology under
various operating environments within IntelliGrid Architecture.

### Architecture Conclusions

IntelliGrid Architecture prescribes a
specific model for each RM-ODP
viewpoint:

if !supportLists?·      
endif?RM-ODP prescribes a separate Functional Model in
the Enterprise View.  IntelliGrid Architecture prescribes
the standardization of services. 
Examples of this in practice include the WG 13/14 application categories
or the WG 10 Device Models.

if !supportLists?·      
endif?RM-ODP prescribes a separate Information Model in
the Information View.  IntelliGrid Architecture prescribes
that the Information Model be explicit and discoverable.  Examples of this in practice include the WG
13/14 CIM, or the WG 10 Object Models.

if !supportLists?·      
endif?RM-ODP prescribes a separate Interface Model in the
Computational View. IntelliGrid Architecture prescribes that the set of Interfaces be
generic.  Examples of this in practice
include the WG 13/14 Generic Interface Definition or the WG 10 Abstract
Communication Service Interface.

if !supportLists?·      
endif?RM-ODP prescribes a separate Deployment Model in
the Engineering View.  IESCA presents a
deployment neutral architecture that can be applied to a variety of
Environments.

if !supportLists?·      
endif?RM-ODP prescribes a separate Technology Model in
the Technology View.  IntelliGrid Architecture presents a
technology neutral architecture that can be realized with a variety of
technologies.  Examples of Deployment and
Technology models in practice include WG 13’s Technology Profiles and WG 10’s
Communication Stack Profiles.

Figure 21 illustrates the process of deriving IntelliGrid Architecture views
corresponding to the five RM-ODP
Views.

if !vml?![](Anl_Tach_Approach_files/image008.gif)endif?

Figure
21 IntelliGrid Architecture Analysis Logic Flow

 

Each RM-ODP View and IntelliGrid Architecture View is orthogonal to every
other one:

if !supportLists?·      
endif?From the Enterprise View, services such as a
Confidentiality Service can be implemented using a variety of
technologies. 

if !supportLists?·      
endif?From the Information View, information models
such as the CIM can exist in many deployment scenarios environments and be
implemented using a variety of technologies. 
Furthermore the CIM has been developed of any one service or technology
independent interface.

if !supportLists?·      
endif?From the Computation View, a generic interface
can be used to transmit data from any information model.  This means that component interfaces do not
need to be recoded when the information model gets extended or updated.  Similarly, as platform technologies such as
CORBA and Java evolve, the platform neutral specification generic interface can
remain stable and provide the design for a bridge for interoperability over time.

if !supportLists?·      
endif?From the Engineering View, the Common Services,
Information Models and Generic Interfaces can be deployed in many
environments.  While the environment
determines what technology a utility may use, as technology advances the
environment stays more or less the same.

if !supportLists?·      
endif?From the Technology View, the actual technology
chosen can only be seen as snap shot in time. 
Technology advances rapidly.  The
technology independent design of IntelliGrid Architecture ensures that a coherent base for
interoperability remains.
