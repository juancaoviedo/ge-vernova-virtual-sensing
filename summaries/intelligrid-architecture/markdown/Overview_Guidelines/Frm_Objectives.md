# Objectives

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Frm_Objectives.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Introduction

The Integrated Energy and Communications Systems
Architecture (IntelliGrid Architecture) project represents the initial steps on a journey toward a
more capable, secure, and manageable energy provisioning and delivery system.
The IntelliGrid Architecture project envisions a variety of plausible futures for electric and
energy service operations ranging from advanced automation to dynamic consumer
response. The project results propose the next steps in the process of bringing
this vision to fruition. These steps include using more rigorous systems
engineering practices, application of IntelliGrid Architecture principles, and implementing the
project recommendations.

IntelliGrid Architecture builds upon existing information industry
infrastructure and standards development work and proposes a series of pathways
by which the industry can more effectively integrate advanced automation and
consumer systems over the long term. It should be noted that developing an
industry-level architecture is a process, not an end in itself. The IntelliGrid Architecture
project represents only the initial steps in a longer journey toward more
effective long term and intelligent use of advanced technology.

## Historical Perspective

One can consider IntelliGrid Architecture to be the third wave of focused
efforts endeavoring to define reusable architectural components for energy
enterprise and industry-wide applications. The first two waves of industry
efforts were the Integrated Utility Communications Project and the UCA® 2
Effort.

Integrated Utility Communications
Project

The first effort was performed through the
efforts of the Integrated Utility Communications Project, which initiated by
EPRI® in 1986. Through these initial efforts, a cadre of utility domain experts
was consulted and their views combined into the first incarnation: UCA(Utility
Communications Architecture). What was most impressive about this effort was
the top-down, requirements-driven analysis performed by objective professionals
in pursuit of a common communications denominator in the utility industry.

UCA 2 Effort

EPRI furthered the effort in a series of
tailored collaborations that endeavored to apply the original UCA architecture.
As UCA implementations efforts moved forward, improvements and clarifications
were made to the document, which resulted in the issuance of enhanced
architectural descriptions that became know as UCA 2.0.  Crucial to the success
of UCA was the involvement of domain experts and developers in the application
of the concepts. At this time, EPRI took steps to submit the UCA documents to
the International Electrotechnical Commission (IEC) Technical Committee 57,
where the work was accepted into the IEC 61850 standards process.

These original EPRI efforts succeeded in establishing a
direction for the industry and creating momentum toward abstract modeling and
interoperability. The IEC 61850 standards are beginning to mature and major
vendors are developing products from these standards. In addition, EPRI has
worked to develop the Control Center API project into the Common Information
Model through contributions to the IEC TC57 standards initiatives. Finally,
EPRI has facilitated the formation of a users and vendors association, The UCA
International Users Group[[1]](Frm_Objectives.htm#_ftn1).

More than a dozen years have
elapsed since the first UCA effort. During this period two things have become
apparent. First, an extraordinary evolution in communications and computing
technology has occurred and will continue. Second, the scale and scope of
advanced automation extends beyond the standards that have developed for the
energy industry. Standards and infrastructure development from a variety of
industries must now be included in the design and enhancement of an
industry-level architecture for the energy industry. The energy industry
architecture must now include standards from information technology, building
and home automation, and eCommerce, to name just a few. It is important to now
advance the concepts originally conceived and laid down by the UCA into the
modern age. The IntelliGrid Architecture project represents this effort.

## Industry Trends and Project Drivers

The IntelliGrid Architecture project was initiated in response to several
significant trends and drivers facing the energy services and power delivery
industries. Of these trends, five main technical development and business
drivers were key forces behind the conception of the IntelliGrid Project. Each key
driver, discussed individually below, carries important business and technical
implications for the energy services industry as it moves ahead in the areas of
advanced automation systems and consumer communications.

Driver 1: Cost effective use of
emerging technology

The migration toward effective use of more
capable open standards is crucial for a robust power marketplace where hundreds
of companies supply products that enable future visions to become a reality. As
such, the need for greater, and more effective, use of advanced communications
and computing technologies is a key driver in the goal to improve the overall
energy system.

The industry, as a whole, must strive to
leverage investment in communications and advanced automation by more effectively
using installed information automation equipment. Incremental investments in
advanced automation and communication infrastructure must support multiple
applications today and be extensible for future needs. The industry cannot
afford to install single-purpose automation applications and equipment; this
inevitably leads to layered, redundant infrastructures.

Designing the IntelliGrid Architecture to address
this first driver will help overcome the limitations of proprietary systems and
standards that are too narrowly defined. Large collections of disparate
systems, sometimes with partially overlapping functionality, can quickly become
confusing and unwieldy to manage. By comparison, a well-designed architecture
enables initial designs and installations that take into account for future
operating scenarios. Developing a cohesive architecture and intelligently using
open systems will also assist in more effective life-cycle management of
equipment. An overall architecture will help ensure that systems are initially
built with a robust set of initial requirements so they are adequately
specified and designed for both present and future needs. Architected systems
will enable future integration and extensibility so that adding a new function
does not require wholesale upgrades or replacement of systems.

Driver 2: Higher levels of
integration across traditional boundaries

The need to better integrate advanced systems
across traditional boundaries and barriers to create interoperable systems is
the second key driver for the IntelliGrid Project. Industry changes are driving
tighter operational integration between a greater diversity of business
entities - for example, integrating electric energy generation and delivery
with consumer premises equipment. In response to this demand, the industry is
attempting to dynamically integrate consumer operations through a collection of
applications, under the phrase ‘demand response’. A myriad of technical and
management issues must be addressed, however, to enable this vision to reach maturity.

Unfortunately, this emerging paradigm will
require a massive level of interoperability previously unseen in the power
industry. Connecting end consumers to power system operations will call for the
integration of millions, or even billions, of devices. Furthermore,
administration of such a system presents a huge burden for entities using the
equipment.

Development of an industry architecture will
result in migration to more uniform systems development, thus easing the burden
on systems administrators. More powerful systems administration capabilities
(including data management, security, monitoring, and diagnostics) can be
designed and built directly into equipment, enabling systems management that
can scale to the levels now envisioned for the energy industry.

Driver 3: Infrastructure
development and standards coordination

The third IntelliGrid Architecture driver responds to the need for
greater coordination and integration of the myriad of standards and
infrastructure development initiatives currently taking place across the
industry. Standards are necessary for systems to interoperate. However, it is
important to note that the *standards* developed by the industry must also
work together or these very standards contribute to the greater problem of
balkanized systems on large scales.

Development of an industry-level architecture
is a necessary response to the need for greater integration within, and
between, standards communities, as well as enterprises. The energy industry has
had some painful examples of system installations that failed to scale to large
numbers, or to interoperate effectively with systems from different vendors. An
architecture will play a critical role in developing and integrating future
standards by providing a context and a larger-scoped framework than is normally
considered by a single standard. Only in this way can standards hope to
interoperate today and scale to address the needs of tomorrow.

Driver 4: Response to new and
emerging requirements

The fourth IntelliGrid Architecture driver arises from emerging enterprise-level
and industry-level requirements. Since new system requirements appear
constantly, any proposed power system must be robust enough to both anticipate
and adapt to changing requirements. Many systems that are installed today will
eventually require upgrading to meet future requirements. Systems that are
inadequately specified to meet future needs are effectively obsolete, even
before they are installed.

The IntelliGrid Architecture project has particularly emphasized
system requirements to capture scenarios involving future operations. These
requirements for future system functions originate from a variety of sources.
Most requirements are *constructive* in nature and seek to add
capabilities or integrate with more systems. Other requirement sources,
however, can be bluntly described as ‘hostile’. While advances in new
communication, embedded computing, and information technologies can provide
significant benefits, they also bring with them a serious dark side that must
be addressed. System architects designing future energy provisioning systems
must be concerned with meeting plausible requirements from an expanding set of *hostile*
sources. In addition to cross-industry integration, requirements are emerging
in key areas of policy-based systems management and cyber security. That which
was once deemed a reasonable level of protection is inadequate today and for
the future.

It should be noted that IntelliGrid Architecture project
emphasizes that it is not only important for the energy industry to use new and
emerging technology, but also vitally important to address how the technology
is implemented.

Driver 5: An industry vision to
enable a robust future

Finally, IntelliGrid Architecture project is about creating a
vision for the future and embarking on robust and strategic pathways to enable
applications envisioned today, as well as those not yet imagined. To operate in
a manner unimpeded by traditional thinking, an industry architecture must
address the former and enable the latter.

The IntelliGrid Architecture project has created plausible
scenarios for future operations that extend beyond traditional energy service
provisioning. IntelliGrid Architecture’s reach extends from central generation systems and natural
direct energy sources to operations within and between consumer end-use
equipment. IntelliGrid Architecture goes beyond the flow of electric energy into end-use equipment
to encompass performance and functions both within and peripheral to this
equipment. By definition, an architecture at this level must be used for
visioning with a scope broad enough to embrace the future effectively. This visioning
is not exhaustive within IntelliGrid Architecture, but rather *representative* of the types
of interaction and integration that are both useful and possible within the
energy services industry.

## IntelliGrid Project Scope

The scope of IntelliGrid Architecture project, by definition, must consider
the entire energy enterprise: the *power engineering* and *information
technology/distributed computing* elements. Since the distributed computing
systems must support both power engineering applications and information
systems, the requirements for the future distributed computing system are
subordinate to the needs of the power engineering and business support systems
and to the system management functions. IntelliGrid Architecture is required to integrate customer
interaction, power system monitoring and control, energy trading, and business
information systems. It will reach across customers, feeders, substations,
control centers and energy traders.

IntelliGrid Architecture is a roadmap for a next generation power system
consisting of automated transmission and distribution systems that support
efficient and reliable supply and delivery of power. The goal is to create a
power system capable of handling emergency and disaster situations, while also
able to accommodate current and future utility business environments, market
requirements, and customer needs.

“We have a digital economy and we're still trying to provide
power to it through a mechanical design system that was designed over 50 years
ago. It is a marvelous system, but we've been effectively borrowing against the
future to pay for the present, and the future has caught up with us, we need to
build the system to serve the digital society of the 21st century.

...And it's then the controllability of that system. Once we
have those digital controls in, we can instantaneously manage the power system
so it is self healing, that is it can detect instantaneously a difficulty and
correct for it locally so that cascading effects can be eliminated and
fundamentally improve the reliability of the system so that computers and other
sensitive equipment that has come in over the last decade [are] not upset by
power disturbances.”[**[2]**](Frm_Objectives.htm#_ftn2)

## Adoption of Advanced Tools and Methods

In any vision of the future energy industry, operations
will be substantially more complex than today. This complexity must be managed
on a variety of levels, including business relationships, regulatory processes,
and technology integration. An architecture must account for these
relationships and complexity. To meet the challenges posed by this project, IntelliGrid Architecture team found it necessary to innovate tools and methods to capture the
complexity of future energy industry operations. This required adopting both
systems engineering methods and emerging standards for representing high-level
architectures. As a result, IntelliGrid Architecture project introduces necessary terms and
language emerging from architecture development and systems engineering
communities.

IntelliGrid Architecture is not an endorsement of
specific methods, tools, or products

The tools and methods used within this project
were selected for the purpose of developing IntelliGrid Architecture Framework. The project
used systems-engineering-related standards and notations to document
relationships and content specific to those relationships. While these
standards and methods represent some of the best thinking in the industry, they
also continue to mature as a technical discipline. While the specific tools and
methods selected for IntelliGrid Architecture project are useful to define architectural level
issues, this generally does not constitute an endorsement of these specific
tools. The team selected tools and methods on the basis of the best available
approach for defining and evaluating large complex distributed computing
systems. However, the underlying systems engineering discipline and the
community developing the industry-level architectures will continue to mature.
The team anticipates further refinement and improvement of the specific methods
and notations used within this project and recognizes that there will be
additional valid methods for representing industry level architectures.

Systems engineering methods are
recommended

The energy service provisioning industries have
reached the point where managing technical and business complexity is of
paramount importance. The combination of information technology, advanced
automation, and communications systems, (collectively referred to as
‘distributed computing’) does not yet have the technical rigor of traditional
engineering disciplines, such as electrical, mechanical, or civil engineering.
This requires greater discipline than traditionally used in development or
implementation of many advanced automation and distributed computing systems.
Systems engineering is the discipline of rigorously defining systems through a
series of technical steps where design decisions are traceable back to
requirements. The IntelliGrid Project recommends that the next steps in the
development of an integrated industry architecture follow the disciplines
underlying systems engineering.

## A Shortage of Integration and Cooperation, Not Technology

An architecture is fundamentally about integrating a wide
variety of components into a coherent and beneficial whole. While there is no
apparent shortage of base technologies and components that may comprise the
future energy system, there is a significant shortage of interoperability and
integration between individual technologies and components. Examples of base
technologies include computers, communications, and field devices. The free
market does well developing these base technologies and stand-alone products
but is not as successful when developing infrastructure. This is understandable
since the principal goal for vendors of products is differentiation, not
uniformity.

There is a particular need in the power industry for an
organized infrastructure (standards and technology) that will enable valuable
and cost effective interoperation between products developed by different
vendors. Without substantial demand (or pull) from the user community, there is
little incentive for vendor ‘A’ to facilitate interoperability with products
from vendor ‘B’. Instead, vendors must recognize that interoperation is the
minimum common requirement and that differentiation will come from feature sets
and service offerings.

## Infrastructure Required to Move Energy Industry Forward

For a century the electric industry has focused
predominantly on developing the electric system that we know today. The system
of power plants and power delivery system components comprise a significant
energy infrastructure. This electric infrastructure has grown during a century
of technical development and is the most capital-intensive of all the public
service infrastructures described as utilities. As we look to the future of
this system, it will increasingly rely on another infrastructure that must be
developed in parallel to move the industry effectively toward the future.

This second infrastructure, the information
infrastructure, will be made up of communications technologies, networking
technologies, intelligent equipment, and algorithms that can execute increasingly
sophisticated operations functions. This second infrastructure can be
collectively described as ‘distributed computing’ since it comprises a variety
of technologies that enable the sharing of data and controls within intelligent
equipment.

## Architecture Defined

An architecture is directed toward the development,
integration, organization, and life-cycle management of information
technologies and advanced automation systems. The architecture community has
developed a few working definitions that can be applied to IntelliGrid Architecture project:

An architecture is the fundamental organization of a system
embodied in its components, their relationships to each other, and to the
environment, and the principles guiding its design and evolution.[**[3]**](Frm_Objectives.htm#_ftn3)

Though there are several different definitions for
architecture, all include the following recurring themes:

High-Level Perspective

The most common theme defining an architecture
is that it must have a high-level perspective. This perspective enables an
organization to view its operations in the context of how it integrates with
multiple systems, both within the enterprise and outside of it. The IntelliGrid Project is unique from this perspective as it views the operations of the
future electric energy services industry from a high perspective level that
cuts across traditional boundaries.

Need for Common Language on
Different Levels

The high-level perspectives of an architecture
often expose challenges when attempting to integrate business or operational
entities that have not considered operations beyond their traditional domain.
Bringing these systems together requires effort to develop a common language
across all business and operating domains. A common language is required for
both business discussions and technical ’computer to computer’ communications.

Life Cycle Strategies

An architecture seeks to develop strategies by
which new levels of integration can be achieved across the enterprise and
across the industry. Additionally, an architecture examines the system from a
long term perspective with an eye to how the system may evolve. A good
architecture should require little change over time. Indeed, a strong
architecture plans for change and includes a process to adapt and evolve, lest
it become obsolete itself.

Integration of Standards and
Technologies

The essence of an architecture is the use and
integration of standards and technologies into an interoperable framework. In
this project, the reader will see several references to standards, technologies
and best practices as the building blocks of an industry architecture. However,
an architecture is not simply about making better use of standards and
associated technologies. Today’s standards and infrastructure are often
developed with narrow scopes or with specific groups of applications in mind.
In comparison, architecture development implies working within the standards
communities to develop methods and strategies through which the standards can
work together more effectively. It also means that in some cases, those working
on standards and their associated technologies will discover new capabilities
and requirements.

Integrating standards strategies is, therefore,
one outcome of architecture development. Several examples of standards and
technology integration needs have surfaced within IntelliGrid Architecture. The IntelliGrid Architecture framework,
if followed by those implementing technologies, will provide a strategic
pathway by which systems that were once islands can become integrated.

Recognizing a Variety of Audiences

An architecture addresses technical issues that
arise at an enterprise or industry level. The implications of these issues may
be manifest at various levels within an enterprise. Architecture development
carries implications for both business operations and technical operations
within an enterprise. For this reason, architecture development has
implications for the high level business process, as well as for lower level
tasks, such as just getting two products to interoperate. As such,
architectures must address a variety of audiences, ranging from business
strategy planners to field engineers. The primary audience, however, is system
architects who are concerned with enterprise level systems integration. These
individuals are typically associated with either information technology systems
or advanced automation systems.

Integration with other developing
architectures

IntelliGrid Architecture’s enterprise and industry-wide scope
necessarily means that other architectures undergoing development in parallel
will become part of the implemented form of IntelliGrid Architecture. For example, other key
architectures in development at federal, state and even international levels
will need to be integrated with IntelliGrid Architecture to some degree.

Emerging federal and state information
technology architectures are establishing policies to integrate information
systems within government agencies. IntelliGrid Architecture’s reach will include the combination
of information and advanced automation systems needed to integrate with
developing federal and state level architectures. Examples of possible
integration include business-to-business, electronic commerce, and basic
consumer service functions. Policies, including system management and security,
must be compatible across architectures to achieve the desired levels of system
integration and interoperability. The energy provisioning industry must
integrate strategically with other developing architectures to achieve the
visions put forward by the industry.

Several emergent architectures that are
predicted to be integrated with the energy services architecture are discussed
below. It should be noted that these architectures are driven by federal
legislation, Government Accounting Office (GAO) guidance, and other mandates
that are key drivers:

Federal
Enterprise Architecture

The Federal Enterprise Architecture (FEA) was
developed as the result of federal legislation passed during the 1990s. The
FEA’s purpose is to integrate the information systems of all federal agencies.
While it predominantly targets information systems environments, the policies
that FEA presents, such as the development of e-commerce and e-government, have
implications for integrating energy industry initiatives. The FEA has been
undergoing development for the past several years and represents a serious
effort to integrate federal agency systems. Information systems installed by
federal agencies must show compliance or migration to the FEA in order to
continue to receive funding to support these systems.

Department
of Defense Architecture Framework

The Department of Defense Architecture Framework(DODAF) is the architecture
intended to integrate the systems of the Pentagon and all branches of the U.S.
military. This architecture prescribes policies for integrating information
systems and advanced automation systems with military buildings and business systems.
Energy systems seeking to interoperate with Federal DoD buildings (for example,
building automation systems) will be subject to the policies within the DODAF.

State
Level Architecture Development

Many states have begun developing architectures
to integrate systems and services at the state level. These architectures are
directed toward integrating state office functions and public services,
including, but not limited to, state and local public services. Similarly,
these architectures will address business and government electronic commerce
systems. States, such as Arizona, Ohio and others, have begun establishing
enterprise architectures and policies for information systems. In addition,
organizations, such as the National Association of State Chief Information
Officers, endorse the concept of architecture development. Policies emerging
from state architecture development related to security policy management,
systems integration, e-commerce and e-government can be foreseen to impact the
implementation of energy related functions with government buildings and
information systems.

International
Level Architectures

Architectural elements and rules of governance
are under development by international communities to address issues such as
models of governance and commerce across national lines.

## The Products of an Architecture

An architecture is comprised of a variety of elements
including requirements, models, analyses, terminology, and recommendations. All
of these elements were addressed during IntelliGrid Architecture project.

Recommendations

It has been stated that an architecture is a
journey and not a destination. One of the most important outputs from an
architecture development effort is a clear view of what lies ahead, as well as
the path to get there.

As such, the IntelliGrid Architecture provides a
collection of recommendations for using and applying a variety of standards and
technologies, which, in turn, can be used as the building blocks of
integration. Also included are best practices for the energy industry to follow
as the integrated architecture is implemented. In addition, IntelliGrid Architecture project
has highlighted technical issues that must be addressed to ’complete’ the
standards, technologies, and best practices for the future energy services
industry to operate effectively. An example of these issues can be seen in the
variety of requirements now emerging for industry operations, which pose unique
challenges to future advanced automation systems. Integrating the required
technologies is an emerging technical need. These recommendations are presented
in Volume IV of this series.

Analyses

The IntelliGrid Architecture also contains analyses
that support the project team’s recommendations. The analyses may utilize a
variety of methods to understand future energy industry operations. This
project used a variety of analysis methods that were based on the requirements
gathered during the project, as well as on the team’s experience within the
industry and standards communities. However, all analyses, no matter how
rigorous, are grounded in human, subjective terms. It is therefore imperative
that all decision points are traceable back to requirements. Only in this way
are the conclusions meaningful.

Requirements for future systems

For this project, a series of future
operational scenarios and their associated requirements were developed. The
requirements were developed through a combination of studies and interactions
with some stakeholders of the future energy system. The set of requirements
captured within this project do not exhaustively cover every possible
application of advanced automation or information technology. A comprehensive
list of applications could number in the thousands.

It should be noted that the requirements
considered in this project were developed for a select set of applications that
were believed to carry ‘architectural significance’ for the industry. These
requirements and associated operations scenarios, known as ‘use cases’, form a
framework of functions that encompasses most architecture challenges faced by
the energy industry. Architecturally-significant issues addressed in IntelliGrid Architecture
project included challenges arising from implementing systems on a large scale
and over a wide diversity of businesses and technical operating environments.
These issues include integration and interoperability issues, implementing
consistent policies and developing the techniques to manage systems on large
scales.

A
Model of Future Operations

The IntelliGrid Architecture
project also developed a model of future operations using a combination of two
sets of standards for architectural modeling. The complexity of the future
energy system requires modeling to effectively capture relationships and
integration between systems. Developing a model for an Integrated Energy and
Communications Systems Architecture prior to its detailed design and
implementation is as essential as having a blueprint for a large building. Good
models assure the robustness of the design and are necessary for communicating
among stakeholders.

Terminology

One of the largest challenges any architecture
project faces is bringing forward a common set of terms that are useful for
discussions across traditional operating boundaries. Just as a model is
critical to communicating among stakeholders, so too is standardized terminology.
It is impossible to have consensus on meaning and intent without first
establishing definitions for the terminology. It is equally important to have
definitions traceable back to standards bodies in order to maintain consistency
in meaning across disciplines and industries.

To that end, terminology is presented and used
in the model of future industry operations. Ideally, terminology is traceable
to the standards that are adopting the terms. Within IntelliGrid Architecture project,
priority is given to terminology being developed within key standards
organizations.

## Vision and Process for a Seamless, Managed Architecture

IntelliGrid Architecture’s vision for the architecture uses an integrated
approach to describe the enterprise requirements. An approach focused solely on
applications does not easily yield the type of interoperability needed or
desired. Instead, a rigorous *systems engineering approach* was adopted
for soliciting requirements from key stakeholders. Enterprise domains tell us
what the top level requirements are, and analysis reveals key applications that
could realize those requirements. Key applications with the promise of exposing
common services to enable interoperability are further explored. Analysis of
those common services can allow the team then to enumerate the communication
requirements for interoperable systems.

When conducting analysis at different levels (enterprise,
application, services, communication), it is important to understand the
context of each requirement. A formal framework for capturing the full context
of each requirement was adopted. The methodology used by the team separated the
description of the systems and subsystems into five different viewpoints. Just
as a building plan relies on differing views (plumbing, structural, electrical,
etc.) to represent the whole, so too does a communication architecture rely on
different descriptions. As seen in Figure
3, the model breaks down into five viewpoints that can be roughly portrayed as describing (1) **Who** participates, (2) **What** information is exchanged, (3) **How** is the data processed or interpreted, (4)
**Where** are the interacting devices located and (5) **Which**
technologies are used to facilitate or manage the exchange.

![](IECSA_VolumeI_files/image003.jpg)

Figure 3: Introduction to IntelliGrid Architecture

The
Architecture must be understandable to architects and lay people alike to be
useable.
