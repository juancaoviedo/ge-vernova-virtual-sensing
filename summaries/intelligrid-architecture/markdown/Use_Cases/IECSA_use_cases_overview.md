# Power Functions

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/IECSA_use_cases_overview.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# IntelliGrid Architecture Power System Functions

## Table of Contents

* [Executive Summary](IECSA_use_cases_overview.htm#Executive Summary)
* [Introduction](IECSA_use_cases_overview.htm#Introduction)
* [Identification of Power System Functions](IECSA_use_cases_overview.htm#Identification of power system functions)
* [Identification of Power System Domains](IECSA_use_cases_overview.htm#Identification of Power System Domains)
* [Areas of Concentration](IECSA_use_cases_overview.htm#Areas of Concentration and Addressing Application Domains)
* [Detailed Domain Use Cases](IECSA_use_cases_overview.htm#Domain Use Cases)

## Executive Summary

The foundation of an architecture begins
with a collection of requirements that span the scope of the
energy industry enterprise. As IntelliGrid Architecture is envisioned to span
from the Energy Traders desk to the thermostat in the home, the
requirement space and subsequent stakeholder community was
extensive. Volume II covers the requirements development processes
and resultant requirements content that the team was able to
gather within IntelliGrid Architecture project.

The requirements gathering process was
structured and based on the IEC standard “Reference Model for Open
Distributed Processing – RM-ODP”. This standard identifies the
fundamental information needed for architecture development such
as “who” is involved in an activity, “what” data is being
exchanged, and “how” the data is being exchanged (i.e. –
communication Quality of Service requirements). The requirements
gathering process was facilitated by a “Domain Template” developed
by the team, which solicited information based on the RM-ODP
guidelines. In particular, the template format (included in
Appendix C) starts with a Narrative that describes, in plain
language, the particular function being detailed. The template
then proceeds to guide the stakeholder through the identification
and definition of the various entities (actors) involved in a
process, the data exchanged between the actors, the sequence of
steps involved in the data exchange, and the communication
requirements (such as data speed, reliability, security, etc.) for
the data exchange.

As many “pieces” of the IntelliGrid Architecture
are in place and operating as “legacy” systems, the requirements
gathering focused on “new” and “architecturally challenging”
applications, however, several “baseline” applications were
detailed and subsequent gaps and seams in the existing
architectures, functionalities, and technologies were identified.
An application was deemed “architecturally challenging” if it
stretched the boundaries of performance, reliability, security,
configuration (number of devices with which to connect), data
management, etc. To this end, requirements gathering focused on
four areas that were identified as migration areas for the Power
System of the Future, namely: Market Operations, Wide Area
Measurement and Control (WAMAC), Advanced Distribution Automation
(ADA) / Distributed Energy Resources (DER), and the Consumer
Interface (including Real Time Pricing). It should be noted that
these focus areas “cut across” multiple power system domains such
as Generation (primary and distributed), Transmission,
Distribution, and Consumer Services.

In addition to the power system and energy
applications, it was determined that the next generation Energy
Architecture would require a management system for the
communication system itself. These network management requirements
were often identified in the Use Cases and been identified as
“Common Services”, that is, services that span the entire
architecture. These Common Services are detailed in Volume IV.

As mentioned earlier, in order to span the extensive range of
requirements, an equally extensive range of stakeholders had to be
identified. To this end, a stakeholder identification and
engagement process was prepared and conducted, a process that is
ongoing. Engagement took place on two fronts, namely, education
and requirements capture and included over 100 engagements with
over 1000 individuals. Invariably, all engagements started with an
educational presentation on IntelliGrid Architecture. Different levels of education
were prepared and presented based on the audience type. With
appropriate targeted audiences, detailed requirements gathering
would be facilitated, typically resulting in the filling-in of a
Domain Template resulting in a Use Case. A description of the
stakeholder engagement process can be found in Appendix A and the
list of stakeholders engaged to date can be found in Appendix B. A
description of the Domain Template can be found in Appendix C.

The captured requirements should serve to
further make the case for architecture development and larger
scales of integration than is being either achieved or addressed
within standards communities today. It must be kept in mind that
these requirements are not exhaustive for every identified
application that could use or be integrated with IntelliGrid Architecture. In this
way the associated common services and related architectural
issues for the entire industry can be addressed by IntelliGrid Architecture’s
carefully selected representative sample of application
requirements and associated analyses. In effect, this completed
set of IntelliGrid Architecture requirements will cover most of the major
architectural issues likely to be encountered by any foreseeable
application, however, it should be noted that IntelliGrid Architecture needs to be a
living document that is periodically updated with new use cases
and new technologies as identified.

## Introduction

Volume II presents the beginning
of the architecture development process, that is, the
collection of the function descriptions or “use cases”
that the architecture needs to support, the process for
identifying stakeholder and source information, and the
process for capturing the functional requirements.  The
appendices of this document include lists of
stakeholders engaged and the detailed captures resulting
from stakeholder engagement, along with descriptions of
the functions.

### Requirements Gathering Process

The requirements gathering
process used an iterative and stepwise refinement based
methodology.  In parallel with the main requirements
development process, there was a continuous stakeholder
engagement track that fed information into and out of
the project as necessary.  This approach facilitated the
requirements gathering process by stimulating
stakeholder interest, collaborating on new ideas, and
obtaining stakeholder buy-in.

The stakeholder engagement
process identified different kinds of stakeholders and
different kinds of engagements.  Note that besides the
collection of information, a very important aspect of
the stakeholder engagement process was education on the
concept and process of building an architecture, as well
as the goals and scope of IntelliGrid Architecture itself.  Numerous
presentations to technical groups and individuals were
made, along with detailed discussions with selected
individuals and small groups.  To date, over 100
engagements have been made to over 1000 individuals. 
Details of the engagement process can be found in
Appendix A and a list of the groups/individuals engaged
either actively or passively can be found in Appendix
B.

The core requirements gathering
process track started with a scoping exercise that
resulted in the identification and documentation of over
400 existing and future utility functions at a
preliminary level.  Section 2 of this document describes
this process in more detail and summarizes the results. 
Appendix E contains the details of the information
captured and the on-line version of the deliverable set
provides hyperlinked documentation of these functions
and their key attributes.

Early in the requirements
gathering process, the entire energy enterprise was
broken down into a few manageable chunks (domains):

> ·        
> Generation
>
> ·        
> Market Operations
>
> ·        
> Transmission Operations
>
> ·        
> Distribution Operations
>
> ·        
> Consumer Services
>
> ·        
> Distributed Resources

A preliminary analysis of these
domains was done to describe the overarching challenges that
need to be addressed and to identify and associate core
functions relevant to each domain.  A preliminary analysis
of these domains indicated a high degree of overlap and
interdependence of the identified functions within the
domains.  Section 3 of this volume describes each domain
including the key applications and architecturally
significant issues that need to be addressed.

To focus on those functions that
would set boundaries on the architecture, an evaluation was
performed that examined performance, security, data
management, and configuration requirements in the identified
functions.  The evaluation identified four primary areas for
detailed study, namely, Market Operations, Transmission
(Wide Area Measurement and Control), Distribution Operations
including Distributed Energy Resources and Advanced
Distribution Automation, and the Consumer Interface.  In
these four areas, those functions that, from a preliminary
evaluation perspective, appeared to have “architecturally
challenging issues” were selected for detailed analysis. 
Section 4 of this volume describes these areas of
concentration.

In addition to the primary study
areas, the need for services to manage the network was
clearly identified.  These services are extensive and cover
areas such as time synchronization, network management,
automatic configuration, etc.  Details on these topics can
be found in Volume IV.

Detailed description, requirements
gathering, and analysis of the selected functions was
structured through the use of a standardized format known as
the Domain Template.  The Domain Template solicited common
information from each evaluated function such as a textural
description of each function, identification of “actors” in
the function, the information exchanged by the actors, and
the transaction sequences in which the information was
exchanged.  The process of filling out the Domain Template
resulted in the creation of a Use Case.

Associated with each transaction
sequence in a use case was a set of non-functional modifiers
that quantified items such as the required Quality of
Service, Security, Configuration, and Data Management
expectations.   This information was captured in an embedded
spreadsheet in the use case document.  The structured format
of the use cases provided by the Domain Template enabled
automatic importation of the various use-cases into a
standard Universal Modeling Language (UML) modeling tool. 
Details on the structure of the Domain Template are found in
Appendix C.

A Domain Expert thoroughly familiar
with the topic about which they were writing typically
filled in the Domain Template.  The primary focus of the
narrative development was to clearly illuminate the
architectural issues associated with the use case in order
to allow further architectural analysis.  The narrative type
of explanation also facilitated sharing scenarios with other
related domain experts.

Having identified the information
needed, the next step was finding sources for the required
information.  To this end, the stakeholder engagement
process described earlier was utilized.  A printable form of
the resulting use cases can be found in Appendix D.  The use
cases are best reviewed, however, within the hyperlinked
electronic form of IntelliGrid Architecture final report.  Only in the
electronic version can the detailed attributes captured
relative to Quality of Service, Security, Configuration, and
Data Management be viewed.  Also, the navigable model
illustrates clearly the interdependencies between functions
and domains.

The specific use cases captured
during the project were primarily used to identify the key
architectural issues facing IntelliGrid Architecture and to facilitate the
development of the architecture to address them.  It is
intended however, that this formal requirements and use case
capture process be used during the development of an
implementation of the IntelliGrid Architecture for a specific
project.

The IntelliGrid Architecture results are intended to be
extensible, that is, as new concepts, features, and
functions are developed, the Domain Template and subsequent
model analysis tools can be used to extend the knowledge
base by adding new use cases in order to keep pace with the
changing times and technology.

### Audience

This volume was designed as a tool for
use by all prospective audiences, which include

> ·        
> Utility system planners, designers,
> and executives.
>
> ·        
> Regulators and Auditors
>
> ·        
> Vendors and suppliers
>
> ·        
> Regional Transmission Organizations
> and Independent System Operators
>
> ·        
> Industry groups include utility
> associations and organizations
>
> ·        
> Government Institutions:
>
> ·        
> End User Groups, organizations
>
> ·        
> Standards making organizations
>
> ·        
> The academic community
>
> ·        
> The international community outside
> of standards making organizations

### How to Use this Document

This volume discusses the process
that was utilized to determine and describe the enterprise
level functions, discusses the power system domains and
domain areas of concentration, and the application domains. 
These provide a high level overview of the scope and focus
of the requirements as well as an introduction to the use
cases.  In addition to serving an introductory role, this
material can be utilized on a standalone basis to lay the
foundation for the analysis covered in subsequent volumes.

The use cases contained in this
volume – both in the form of the captured narratives in
Section 6 and with the full documents contained in Appendix
D – can be used by different individuals/groups – depending
on their needs.   Example applications include:

> ·      **Study of present baseline
> applications** - For those individuals who wish to
> gain an understanding of how certain utility
> systems operate today, they could read the
> narrative descriptions of the “baseline” use cases
> on SCADA, Market Operations, Contingency Analysis,
> etc.
>
> ·      **Identify gaps/seams with existing
> implementations** - For product planners or users
> planning new developments or new system
> installations, the use cases provide a baseline
> from which gap and seam analysis can be
> performed.  This process entails identifying the
> deficiencies of existing installations and then
> identifying the enhancements to the products or
> systems that would eliminate or minimize the
> deficiency.
>
> ·      **Identify functional requirements for
> specifications** - For procurement personnel or
> anyone writing a functional specification, review
> of the functions performed and the services
> required in the identified use cases can serve as
> a guide for features and functions required in
> procurement.  For example, a utility getting ready
> to issue a procurement for electronic home meters
> could read the scenarios and see that they might
> want to include intelligence for real time
> pricing, perhaps the incorporation of a consumer
> portal for remote user access, secure
> communications with authentication, and the
> capability to add-on a wireless home communication
> port.
>
> ·      **Aid for the Communication System
> Architect** - As the communication system architect
> lays out long term plans for his or her utility,
> review of the detailed use cases can provide
> valuable information as far as the number of
> devices that must be connected, the level of
> communication system performance (e.g. point to
> point communication times) that will be required
> in the future, degree of availability/reliability
> of the communication network, security
> requirements (including device access), amount of
> data that will need to be managed, etc.
>
> ·     
> **Utility Executive Vision Development**- As many of the use cases address future utility
> functionality, the utility executive could use the
> narratives to help formulate a long-tern vision
> for his or her company.
>
> ·      **Aid for the Power System Planning/
> Design Engineer** - As the planners and designers
> set their sights on the future of the electric
> power grid, having knowledge of what is being done
> and what may be done in the future is valuable. 
> For example, knowing that and inter-area
> oscillation can be damped through the application
> of a wide area closed loop control system could
> aid in solving a problem identified by the
> planner/designer.
>
> ·      **Checklist of system design issues** -
> For any system designer, the narratives provide a
> convenient checklist of issues to address in their
> design.  In particular, the Excel spreadsheet
> associated with the Domain Template provides over
> 400 check boxes of items to be considered in a
> design.
>
> ·      **Communication of Research Results** -
> As a researcher develops a new concept for the
> protection, monitoring, or control of some element
> in the electric power grid, the use cases provide
> a standard mechanism of communicating the
> communication requirement that his/her design will
> require.

## Identification of Power System Functions

The initial task in developing IntelliGrid Architecture was to define clearly the scope of the architecture to
be addressed in the project. Of particular importance was to
identify and address the industry-wide and enterprise-wide
power system operation functions that carried architectural
significance. The key to defining IntelliGrid Architecture Scope was to
identify the major activities and categorize all of the
stakeholders and their potential interactions for plausible
operational and business scenarios.  In addition, the team
assessed the status of existing distributed computing and
communications technology standards and the de facto
practices used by industry in general and by the utility and
in-building automation industries specifically.

The IntelliGrid Architecture team began by drafting
scenarios of current and future power industry operations
and placing these descriptions into a format that could be
carried forward into the requirements process. The purpose
of these initial descriptions was to illustrate plausible
future operations and to stimulate input from the
stakeholder communities. There are many power system
applications and a large number of potential stakeholders
who participate in power system operations. There will be
even more stakeholders taking part in future applications,
spanning the enterprise from the energy producers to the end
consumers.

To expedite this, IntelliGrid Architecture team
developed business models identifying a strawman set of
entities and addressing the key interactions between them.
These models established a set of working relationships
between industry entities in the present and the future,
including intermediate steps from vertical operations to
restructured operations. Within the context of these
business models, the team created application descriptions
(enterprise activities) that were carried forward into the
stakeholder engagement/requirements gathering process as a
framework upon which to build the architecture.

One of the initial steps was to
identify a myriad of enterprise activities for present and
future power system functions. The energy industry was
organized into six (6) functional domains:

> ·        
> Market operations
>
> ·        
> Transmission operations
>
> ·        
> Distribution operations
>
> ·        
> Centralized generation
>
> ·        
> Distributed energy resources
>
> ·        
> Customer services

A seventh domain, federated systems
management, was also identified, which consists of
technological functions, such as network management and
security that cut across all of the other domains.

Domain experts in IntelliGrid Architecture Team then
developed draft lists of functions (termed enterprise
activities) within each domain, defining present and future
activities that involve electric energy operations.
Ultimately, 80 high-level activities composed of more than
417 supporting activities were identified. These can be
found in Appendix E.  These descriptions helped define the
scope of the project and served as a starting point for
developing a more complete vision of future utility
operations.

At the same time, architecture
experts developed a set of key criteria (quality attributes)
to analyze the significance of the impact of each function
on the IntelliGrid Architecture. These key criteria are

> ·        
> **Communication configuration
> requirements**, such as one-to-many, mobile,
> WAN, LAN, etc.
>
> ·        
> **Quality of service and
> performance requirements**, such as
> availability, response timing, data accuracy, etc.
>
> ·        
> **Security requirements**, such
> as authentication, access control, data integrity,
> confidentiality, and non-repudiation
>
> ·        
> **Data management requirements**,
> such as large databases, many databases
> particularly across organizational boundaries,
> frequent updates, etc.
>
> ·        
> **Constraints and concerns related
> to technologies**, such as media bandwidth
> constraints, system compute-constraints,
> prevalence of legacy systems, unproven technology,
> etc.

Each enterprise activity within each
domain was then briefly described. The description is at a
high level since the initial goal was to develop a scope for
IntelliGrid Architecture effort.  Once described, each enterprise activity
was evaluated according to the key criteria. The focus was
to identify those key criteria that would be architecturally
significant and that will need to be taken into account as
the architecture was developed.

The next step was to evaluate the
impact of the key criteria for each enterprise activity,
using a rating system of 0 (no significant architectural
impact) to 3 (very significant architectural impact).

Then the team identified all
activities that had ratings of 2 or 3 in any of the key
criteria, and expanded on the exact nature of the
significance. Thus, for one specific enterprise activity, a
security rating of 3 might be expanded to indicate that
confidentiality was the main significance, while a quality
of service rating of 2 might be expanded to indicate that
availability and response time were of key importance.

As the scoping effort progressed, a
number of key issues were identified as being even more
critical to the success of IntelliGrid Architecture project than was
initially envisioned. This recognition led to the following
recommendations for any review of technologies and
requirements with a goal of additional focus in the key
areas of:

* **Legacy Systems.** 
  Coping with legacy systems within a
  state-of-the-art architecture, and developing
  migration plans for gradual upgrades of these
  legacy systems to the IntelliGrid Architecture
  technologies is vital to the acceptance of the
  architecture by the industry, which has an
  extensive infrastructure already in place.
* **Security Requirements.**The utility industry has become more aware
  that reliability of the power system is reliant on
  the security of the information and control of
  devices. The primary need is to assess the
  security requirements for the enterprise
  activities and the information assets, and develop
  practical, risk-based, and cost-effective
  solutions for meeting the security threats.
* **Data Management**.
  Automation of the power system operations, market
  operations, and customer services implies accurate
  information that is available at the right time in
  the right place. Therefore, it is crucial to
  understand the increasingly complex requirements
  for data management across disparate systems**,**
  and to develop methods for maximizing the accuracy
  and consistency of databases while minimizing the
  cost of the continual database maintenance
  efforts.

 The development of the functions
includes a complete traversal from the domain description of
a business function through modeling of its details. In the
course of this exercise, the following steps were executed:

1. *Enumeration* of as
   many utility enterprise activities as IntelliGrid Architecture
   project team could identify prior to consulting
   with stakeholders.
2. *Definition* of the
   utility enterprise activities in a manner
   illustrating the requirements they will place on
   the communications system
3. *Prioritization* of the
   activities, in two levels, to identify which
   activities are most likely to place the highest
   demands on the resulting architecture.
4. Detailed *description*
   of a “day in the life” use case for a single
   business activity that was identified as
   containing many architecturally challenging
   quality attributes.
5. *Validation* of the
   tools used to develop the architecture

 The enumeration, definition and
prioritization steps were applied to all enterprise
activities and were used as a starting point for the
definition of requirements, along with additional
information gathered from stakeholders.

The results of this process can be
found in Appendix E.

## Identification of Power System Domains

The initial step in developing IntelliGrid Architecture involved defining clearly the scope of the
requirements of the power system functions and identifying
all the stakeholders. There are many power system
applications and a large number of potential stakeholders
who already participate in power system operations. In the
future more stakeholders, such as customers responding to
real-time prices, Distributed energy Resource (DR) owners
selling energy and ancillary services into the electricity
marketplace, and consumers demanding high quality, will
actively participate in power system operations. At the same
time, new and expanded applications will be needed to
respond to the increased pressures for managing power system
reliability as market forces push the power system to its
limits. Power system security has also been recognized as
crucial in the increasingly digital economy. The key is to
identify and categorize all of these elements so that their
requirements can be understood, their information needs can
be identified and eventually synergies among these
information needs can be determined. Accordingly, the
following power system domains were identified:

* **Market operations**,
  including energy transactions, power system scheduling,
  congestion management, emergency power system management,
  metering, settlements and auditing.
* **Transmission operations**,
  including optimal operations under normal conditions,
  prevention of harmful contingencies, short term operations
  planning, emergency control operations, transmission
  maintenance operations and support of distribution system
  operations.
* **Distribution operations**,
  including coordinated volt/var control, automated
  distribution operation analysis, fault location/isolation,
  power restoration, feeder reconfiguration, DR management,
  and outage scheduling and data maintenance.
* **Customer services**,
  including AMR, time-of-use and real- time pricing, meter
  management, aggregation for market participation, power
  quality monitoring, outage management and, in-building
  services and services using communications with end use
  loads within customer facilities.
* **Generation at the
  transmission level**, including automatic
  generation control, generation maintenance scheduling and
  coordination of wind farms.
* **Distributed resources at
  the distribution level**, including
  participation of DR in market operations, DR monitoring and
  control by non- utility stakeholders, microgrid management
  and DR maintenance management.

A seventh domain, federated
systems management, was also suggested, which consists of
technological functions, such as network management and
security that cut across all of the other domains.  A
detailed discussion of each domain follows

### Market Operations

With the advent of deregulation and
market operations, utilities must develop an entirely new
set of applications. These applications vary from utility to
utility and from RTO to ISO, but generally can be grouped
into the applications listed in Appendix E.

This list of applications illustrates
the complexity of this new area of the electric power
industry. Many of these functions were developed only within
the last few years. Some may exist in name, but in reality
are not yet concrete and or widely used. Others have been
implemented, but then subjected to repeated ad-hoc
modifications that cripple them for general use.

This is largely due to the fact that
market rules and the power system organizational structures
have not yet stabilized. The FERC has mandated the
establishment of four RTOs and propagated a Standard Market
Design (SMD), but the established Independent System
Operators have not evolved into full fledged RTOs and not
all ISOs, RTOs, state regulatory bodies, and individual
utilities have embraced either or both the RTO and SMD
concept.

This leads to a great gap in how
these applications will work together, and how they are
interfaced with each other. Some work has been started. 
Other work is ripe for the support of an information
architecture, namely IntelliGrid Architecture, to guide developers using
modern concepts and state-of-the-art technologies.

### Transmission Operations

The purpose of transmission systems
is to provide adequate, secure and efficient operating
conditions when the power system is in the normal mode of
operations, and to minimize the harm to the customers and
the power system components when the system is in an
emergency situation. The still-evolving market environment
and uncertainty over the pace of restructuring and FERC
regulation have set a much higher standard for existing
transmission system operations and have generated a number
of new capability requirements.

The specifics of these requirements,
which will be imposed on the transmission systems by the
energy market, are still in a state of flux. At the same
time, it is reasonable to assume that eventually the market
rules will incorporate all capabilities that provide value
to the market participants. When the market rules were
initially defined, some operational issues were simplified,
creating discrepancies between the actual value of a
capability and its representation in the market. For
example, the currently accepted methodologies for accounting
energy losses associated with energy contracts may create
unfair advantages for some market participants and
disadvantages for others. Future transmission system
capabilities must be much more comprehensive, accurate and
timely than the current ones.

The self-healing concept set other
high standards for transmission operations, such as dynamic
optimization of multiple criteria, prevention and fast
response to emergencies, and rapid self-restoration of
services. To meet these requirements, in addition to
improving the performance of the current capabilities, new
functions will be required. Currently, there are practically
no fully automated (closed-loop) transmission operations.
However, some new requirements cannot be met by using
advisory modes of applications and supervisory
implementation of the recommendations. In many cases, the
operator will be outside of the real-time control loop.

### Distribution Operations

Distribution automation is integral
to the concept of a self-healing grid. Distribution
automation applications improve the efficiency of system
operation, reconfigure the system after disturbances,
improve both reliability and power quality, and identify and
resolve system problems. Many distribution automation
applications can also be extended to coordinate with
customer services such as time-of-use, real-time pricing and
load management and distributed resources.

Some distribution automation
applications (such as many substation automation functions)
can be implemented utilizing only local information.
However, most applications that can improve performance of
the overall distribution systems through centralized
optimization require communications and information
exchanges to monitor conditions at different locations in
the system. Obviously, the systems architecture being used
will play a critical role in future distribution automation
applications that have been slow to develop due to the lack
of communication infrastructure and standards.

### Customer Services

Customer services consist of more
than a meter reader walking past a house once a month to
scan the meter from a distance. With the advent of
deregulation, interacting with customers has suddenly become
more important, for two major reasons:

> ·      Customers can (and have) switch(ed)
> energy providers
>
> ·      Customers can now be an additional
> source of revenue if new energy services can be
> sold to them, or if the utility rights within the
> customer premises can be used to sell access to
> other businesses

The expansion of coordination and
control of system operations down to end user facilities is
one of the main advantages of IntelliGrid Architecture. This offers a
tremendous opportunity for improved efficiency of operation,
improved control of customer processes based on supply
system conditions, use of customer-owned and operated
generation and power quality improvement technologies as
part of the overall system management and reduced costs to
achieve the required levels of reliability and power quality
at the end user level.

Applications related to customer
service must be coordinated closely with the distribution
automation applications and the distributed resource
applications. Key applications include real time pricing,
load management, and residential customer applications, such
as load control in response to real time pricing incentives,
direct customer energy management and load control during
emergencies, automatic evaluation of and recommendations for
increasing energy efficiency based on profiles of the
customer site and loads, control and performance evaluations
for residential generation, and power quality assessments
and control. Also important are commercial and industrial
(C&I) applications including commercial customer
participation in energy markets through aggregation of
backup generation and energy management, participation in
ancillary services (such as volt/var control, harmonic
control, and reserve generation), real time commercial
facility power quality assessment solutions integrated with
the distribution system operation and integration of real
time information concerning system power quality and
reliability.

### Generation at the Transmission Level

As the power industry restructures,
the role of transmission-connected generation has been
moving away from the vertically integrated model where the
owner of the transmission (and sometimes distribution)
system also owns the generation.  Now other utilities or
independent power producers may own the generation, which
raise challenges for both transmission and generator
owners/operators.  Issues such as market operations,
dispatch, and availability have created a need for real time
information flow between transmission owner/operators and
generator owner/operators.  Applications such as automated
generation control (AGC) and generator maintenance and
scheduling are becoming more widespread in restructured
markets.  The emergence of RTOs/ISOs reflects the changing
relationship between transmission and power generation
systems.

Another issue of concern/application
is the increasing presence of bulk wind plants on
transmission systems.  The intermittent nature of this
generation resource necessitates an additional set of
requirements regarding the ability to disconnect the wind
plant from the transmission system.  Unlike many other
generation sources, wind is not readily dispatched, so
transmission system/market operators must treat it
differently.

### Distributed Energy Resources

The IntelliGrid Architecture can have a major impact on
distribution connected DR management. Few, if any,
applications exist to analyze the impact of DR equipment
connected to the distribution system. Primarily, some of the
existing distribution automation applications for planning,
analysis, and operational control will need to be
significantly modified to take into account the impacts of
DR.

DR devices are becoming functioning
parts of distribution power systems, regardless of who owns
or operates the DR devices.To derive maximum benefits from
DR, avoid possible adverse system impacts and address safety
issues, those utilities which are responsible for
distribution operations will need the ability to monitor and
control the DR devices in real time. Real-time management of
these devices requires communications links and the exchange
of information between the DR systems and the distribution
operations centers.

DR will have increased impacts on the
operations of distribution utilities, due not only to
improvements in DR device technology, cost, and efficiency,
but also to the rapid growth of the deregulated electricity
marketplace. These deregulation forces have spurred interest
in non-standard and dispersed sources of generation to meet
increasingly competitive requirements for energy, ancillary
services, and other energy services. Another consideration
for the DR operations is that there are many stakeholders,
particularly in deregulated electricity markets.. DR
stakeholders are the people or companies with a role in
respect to the DR devices.  These roles determine the
information transactions, namely what information they have
and what information they need.

By managing these distributed
resources effectively, distribution utilities can benefit
from DR capabilities, including using DR for energy,
reserve, backup, VAR control, and power quality enhancement.

## Areas of Concentration and Addressing Application Domains

To facilitate the requirements
gathering process, IntelliGrid Architecture team felt it was useful to
visualize a set of power industry activities that all have a
common purpose or "theme". These areas of concentration
represent  a number of different activities, functions,
devices, networks, organizations and people that are
involved in these activities.  The team used the functional
grouping to prioritize the components of the power industry
in order to tackle the significant architectural challenges
first.  Although there were four distinct areas of
concentration, there is significant overlap with many
sharing the same, well known architectural issues. However,
the distinctions between the areas represent really
important issues that ultimately define the boundaries of
the architecture.

In this way, the team analyzed the
enterprise activities and identified four distinct areas
that have complex requirements that aid in defining the
challenging architectural requirements for IntelliGrid Architecture.  These
areas of concentration are

1)     **Market Operations**: Energy transactions, power system
scheduling, congestion management, emergency power system
management, metering, settlements and auditing.

2)     **Consumer Services**: Real time pricing, integrated with
market operations and consumer end use load control as well
as power quality monitoring.  This includes consumer
dispatch of onsite DER in response to peak pricing/ancillary
service provisioning.

3)    
**Transmission: wide area measurement**, monitoring and
real time control.

4)     **Distribution operations**:  This covers both
distribution operations/automation and integration of DER
integration and focuses on issues such as system protection
integration, volt/var management and managed islanding.

Each of these areas feature
distributed computing system administration functions, such
as security, which were developed side by side with the
power engineering application scenarios. This provided an
overall context to explore both distinct as well as
crosscutting requirements.

Once the team identified all of the
activities and subsequent ratings followed by the selection
of the areas of concentrations, the team needed to further
identify application domains within each area of
concentration to focus on.  This was done in order to select
applications that would cover the architecturally specific
items within each area of concentration.

As shown in Appendix E, there are
sixteen top-level functions under the Consumer domain with
several to many sub-functions under each top-level
function.  Architecturally significant top-level functions
were selected along with corresponding sub-functions for
detailed analysis and use case development.  Use cases were
selected in order to cover as broadly as possible and either
directly or indirectly most of the top-level functions.

The reasons for this approach are
two-fold.  First, the magnitude and extent of the number of
sub-functions dictated that careful selection of those for
detailed analysis is made in order to cover the most areas
based on the project budget and schedule.  Secondly, as
mentioned earlier, there was some significant overlap
between areas of concentration such that specific use cases
would be applicable to several, if not many, different areas
of architectural significance.  Missing a single activity
from the list would only be critical if that activity were
composed of quality attributes not required by any other
activity.

Following is a discussion of
significant application domains under each area of
concentration.  Separate web pages
contain the narratives of the use cases described for each
of these areas.

### Market Operations Domain

As the electricity industry is
deregulated and as FERC defines more clearly what the market
operation tariffs will encompass, market operations, which
are essentially the rules that define how the Regional
Transmission Organizations (RTOs) deal with each other, will
become very important in the future.  This area of
concentration deals with bulk power sales and transfers and
hence involves potentially millions of dollars.   Since a
lot of money could be changing hands on practically a
real-time basis, data security and accuracy is critical,
thereby putting extreme significance on the communication
infrastructure.

Even though the final market rules and
market operations have not been finalized, the team studied
in depth at how three possible RTOs in the Western
Interconnection are developing seamless interfaces for
market participants to submit energy schedules and ancillary
service bids across these three RTOs. The three RTOs are
California ISO (existing ISO handling the electricity market
in California), RTO West (potential RTO of many northwestern
utilities), and WestConnect (potential RTO of many
southwestern utilities). These three RTOs are developing the
requirements for the Western RTO functions.

For this area of concentration, there
were six top-level functions identified that were all
related to market operations but organized and separated for
convenience by timeline, i.e. real-time, day ahead, short
term, long term, etc.  Use cases describing these functions
across each timeline were completed.  These functions have
never been implemented as yet because the actual market
rules have not been agreed upon and are waiting for several
general FERC decisions and some FERC RTO-specific approvals.
Nonetheless, the functions represent conceptually many of
the key types of market operations that are needed in any
electricity market and therefore are applicable to all
potential markets.

### Consumer Services Domain

As mentioned above, there are sixteen
top-level functions under the consumer services domain.  Of
those sixteen, the team felt that three stood out as
covering a wide range of architectural issues as discussed
in the following paragraphs.  The functions were responding
to real-time pricing (RTP) signals, load control and power
quality data collection.

 RTP is important because it requires
communication between the customer and the ESP in terms of
the ESP providing RTP signals to the customer and the
customer potentially providing bids and forecasts back to
the ESP.  Quality of service including high availability and
timeliness of data is crucial.  There are large numbers of
customer with sensitive information on pricing and usage;
therefore security is a key consideration.  Since future
power system operating scenarios will involve more two-way
communication with the customer and the ESP, RTP was
selected for detailed analysis.

Additionally, a use case on load
control was added near the end to account for demand
response aspects where instead of responding to price
signals, the signal comes directly from the ESP to control
customer loads.  Customer side load control covers a wide
range of issues – especially security across organizational
domains and the need for two-way communications to confirm
load control actions for future advanced demand responsive
systems.

The third important aspect is data
collection from the consumer side.  In terms of power
quality data, the information is intermittent and sometimes
infrequent, but timely, communication and notification is
very important when events do occur.  Several use cases were
written to account for the communication aspects associated
with data collection from power monitoring instruments.

 With these use cases, the emerging
concept of the consumer portal can be addressed.

### Transmission Domain

The Transmission area of concentration
focuses primarily on real-time network analysis and normal
and emergency operation of the transmission grid,
specifically known as Wide Area Measurement and Control (WAMAC). 
The team felt that these real-time top-level functions stood
out in importance among the thirteen total top-level
functions in this domain.

WAMACS Automated Control describes a
set of functions that are typically automated within a
substation, but are not directly associated with protection,
fault handling, or equipment maintenance.  In general, they
serve to optimize the operation of the power system and
ensure its safe operation by preventing manually generated
faults.  These functions include:

n        
Changing transformer taps to regulate system
voltage

n        
Switching capacitor banks or shunts in and out
of the system to control voltage and reactive load

n        
Interlocking of controls to prevent unsafe
operation

n        
Sequencing controls to ensure safe operation

n        
Load balancing of feeders and transmission
lines to reduce system wear and resistive losses

n        
Restoring service quickly in the event of a
fault, with or without operator confirmation

 In order to describe these functions,
several use cases were written.  The main objective of these
was to evaluate power system behavior in real-time, prepare
the power system for withstanding credible combinations of
contingencies, prevent wide-area blackouts, and accommodate
fast recovery from emergency to normal state.

Individual devices acting alone
traditionally performed many of the functions described in
the use cases.  When implemented this way, they do not
effect the communications system.  However, in the last five
to seven years, these functions have been distributed across
the substation.  That is, the software logic controlling the
function now often resides on a different device than the
one providing the inputs or outputs to the process. This
change has taken place because the use of substation LANs
has made it economical to place Intelligent Electronic
Devices (IEDs) close to the equipment they are monitoring
and controlling.  Logic therefore has either been
centralized with a single Substation Computer using the IEDs
as remote controllers or it has been distributed among the
IEDs themselves.  In either case, the communications system
has now become part of the automation functions.

These functions are critical in
avoiding a repeat of the August 14 like blackout and hence
are very important to the overall IntelliGrid Architecture.

### Distribution Operations Domain

The Distribution Operations area of
concentration is actually comprised of two top-level
domains, Distribution Operations and Distributed Resources. 
This combination allowed the team to address both of these
domains, which cover extremely challenging areas such as
system protection integration, volt/var management, and
managed islanding in a very efficient manner.  These domains
were comprised of thirteen and eleven top-level functions
respectively, which were further elaborated into many
sub-functions.

 Two large use cases covering many
sub-functions were constructed to cover what the team felt
were the most important top-level functions – Advanced
Distribution Automation (ADA) and integration of Distributed
Energy Resources (DER).

 The first use case domain template
consisted of a collection of use cases utilized to fully
cover the ADA function.  The objective of Advanced
Distribution Automation Function is to enhance the
reliability of power system service, power quality, and
power system efficiency by automating the following three
processes of distribution operation control:

> > ·        
> > Data preparation in near-real-time

·        
Optimal decision-making

·        
Control of distribution operations
in coordination with transmission and generation
systems operations

The second use case covered Data
Acquisition and Control (DAC) and is applicable to other
domains including transmission and consumer services as
well.  The DAC function comprises multiple types of
mechanisms for data retrieval from field equipment and the
issuing of control commands to power system equipment in the
field, including

> ·        
> Field devices
>
> ·        
> Between field devices and systems
> located in substations
>
> ·        
> Between field devices and various
> systems (including, but not limited to, SCADA
> systems) located in DER and utility control
> centers and engineering/planning centers

The DAC function provides real-time
data, statistical data, and other calculated and
informational data from the power system to systems and
applications that use the data. The DAC function also
supports the issuing of control commands to power system
equipment and the setting of parameters in IEDs and other
field systems.

These use cases together cover a wide
range of sub-functions in this area of concentration, which
the team felt which the team felt were some of the most
important in terms of the future application of IntelliGrid Architecture.

## Detailed Domain Use Cases

In IntelliGrid Architecture project, the areas of interest were categorized
into six Domains:

* Market Operations
* Transmission Operations
* Distribution Operations
* HV Generation
* Distributed Energy Resources
* Consumer Services

### Market Operations Use Cases

a.      
Long Term Planning

·       
Transmission and Generation Maintenance Coordination

·       
Updating the Power System Model

b.     
Medium/Short Term Planning

·       
Load Forecast

·       
Outage Scheduling

·       
Congestion Management

·       
Long term Auction/sale of FTRs

c.      
Day Ahead Market

·       
Auction/sale of FTRs

·       
Day Ahead Submittal of Energy Schedules

·       
Day Ahead Submittal of Ancillary Service Bids

·       
Schedule Adjustment of Energy Schedules

·       
Schedule Adjustment of Ancillary Services

d.     
Real-Time

·       
Operational calculations

·       
Real-time Submittal of Schedules

·       
Real-time Submittal of Ancillary Services

·       
Normal Dispatch

·       
Redispatch/Emergency Dispatch

e.      
Post-Dispatch

·       
Metering

·       
Market Products Schedule Checkout

·       
Financial Settlements

·       
Accounting and Billing

·       
Market Monitoring and Auditing

·       
Transmission and Generation Maintenance Coordination

·       
Updating the Power System Model

### [Transmission Operations](TO_Transmission_Use_Cases.htm)

a.      
Automated Control Baseline

b.     
Emergency Operations Baseline

c.      
Wide Area Monitoring and Control Automated Control

d.     
Wide Area Monitoring and Control Emergency Operations

e.      
Wide Area Monitoring and Control Advanced Auto Restoration

f.       
Advanced Auto Reclosing

g.      
Synchro-Phasor

h.      
Voltage Security

i.        
Transmission System Contingency Analysis (Baseline)

j.       
Transmission System Contingency Analysis (Future)

k.     
Self-Healing Grid (across both transmission and distribution)

### [Distribution Operations](DO_Distribution_Use_Cases.htm)

*Distribution operations include significant
penetration of DER in the distribution system*

a.      
Data Acquisition and Control (DAC)

b.     
Distribution Operation Modeling and Analysis (DOMA)

c.      
Fault Location, Isolation and Service Restoration (FLIR)

d.     
Distribution System Contingency Analysis (CA)

e.      
Multi-level Feeder Reconfiguration (MFR)

f.       
Relay Protection Re-coordination (RPR)

g.      
Voltage and Var Control (VVC)

h.      
Pre-arming of Remedial Action Schemes (RAS)

i.        
Coordination of Emergency Actions

j.       
Coordination of Restorative Actions

k.     
Intelligent Alarm Processing

### [Distributed Energy Resources (DER)](DR_DER_Use_Cases.htm)

a.      
DER as Backup

b.     
DER Operated by Aggregator

### [Consumer Services](CS_Customer_Use_Cases.htm)

a.      
Real Time Pricing (RTP)

b.     
Power Quality Monitoring (PQ)

c.      
Customer Communication Portal (CCP)

This categorization was for convenience only, since many
functions involve more than one Domain.
