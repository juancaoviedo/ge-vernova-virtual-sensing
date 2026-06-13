# Conclusions

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Meth_Conclusions.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Conclusions

This section presents the conclusions resulting from the
development process that took place during the past 18 months. The conclusions
are divided into two sections:

§      
A summary of how IntelliGrid Architecture hopes to satisfy the industry drivers.

§      
A commentary by the project team on the results and the process used to
develop them.

## The Initial Steps Have Been Taken: Satisfying Industry Drivers

IntelliGrid Architecture was an endeavor to address a set of
industry drivers. Specifically, how has the effort addressed these drivers?

Driver
1: Cost effective use of emerging technology

With its emphasis on incremental deployment of
applications within a framework of interoperable boundaries, IntelliGrid Architecture provides the
ability to add functionality without a requisite construction of
infrastructure. Yet, as applications cross boundaries they can fuse with others
without significant re-engineering, as is the case with today’s technical
islanding approach.

Driver
2: Higher levels of integration across traditional boundaries

The IntelliGrid Architecture has validated the original hypothesis
of the energy industry needing higher levels of integration.  This was in
part validated by requirements gathered within this project as well as by one
of the most significant events that occurred in the electric industry's
history. The August 14,
2003 blackout brought to the surface many of the technical issues
that are directly addressed in IntelliGrid Architecture project and recommendations.

Driver
3: Infrastructure development and standards coordination

The initial steps have been taken to match
emerging stakeholder requirements with emerging and developing standards and
infrastructure.   Many of the key standards and related technologies
as well as other key infrastructure elements that can be used as part of an
overall industry infrastructure are in development and emerging today. 
Project recommendations summarized here and presented in greater depth in other
volumes point to these technologies based on their ability to satisfy
architectural level requirements.  More work is required however to bring
them into full use to meet the demanding needs of future advanced automation
systems.

Driver
4: Responding to new and emerging requirements

By providing a framework for applications
integration and development, IntelliGrid Architecture provides an ongoing repository for
requirements adoption and refinement. By concentrating at the abstract level of
IntelliGrid Architecture, such requirements can be dovetailed into a growing infrastructure with
minimal perturbation of previous applications.

Driver
5: Industry visioning and enabling a robust future

This section briefly reiterates the basic
principles of the architecture.  The IntelliGrid Architecture is based
on state-of-the-art communications concepts and trends in information
engineering, stemming from:

§      
The description and analysis of communication and information **requirements
of power system operational functions**

§      
The use of **system and** **data modeling** to capture and analyze
these requirements

§      
The definition of utility-specific **environments** having common
sets of requirements

§      
The use of **layered technologies** to separate levels of abstraction
and functionality

§      
The use of **common services, information models,** and**technology-independent interfaces** to create an architecture that is not
dependent on one set of technologies.

§      
The recommendation of **specific standard technologies and best
practices** that can meet the power system architectural requirements

§      
The identification of **missing or overlapping technologies** as a
tool for making **technology recommendations**.

## Commentary on the Process

This section provides the qualitative
conclusions of the project team regarding the results of IntelliGrid Architecture project and
the process used to develop them. Those preparing to continue the work on IntelliGrid Architecture
or develop similar projects may find these conclusions useful.

The IntelliGrid Architecture team was challenged at the outset to
devise a starting point for an energy industry architecture that could evolve,
grow, and mesh with the efforts of architecture work in other spheres of
commerce and communications. In this time of rapid technological evolution and
insertion of communications into every aspect of energy delivery and use, it
was necessary to grab a toehold so that projects incorporating communications
technologies could have a path towards integration. It is easy for an office
worker to upgrade his or her technology with a replacement computer every two
or three years. Yet, with capital-intensive facilities such as those operated
for the generation, transport, and use of energy, a far longer-term perspective
is required.

With these two conflicting goals juxtaposed,
IntelliGrid Architecture project was funded and directed to accomplish its work in an 18-month
timeframe. Why 18 months? Because a shorter timescale would preclude serious
in-depth work, and, a longer timescale would come too late to be useful.

The IntelliGrid Architecture team endeavored to take a systems
engineering approach to distilling stakeholder requirements into an
architecture definition.  Due to the large scope of the project, the team
focused their efforts in certain areas. These focuses and other observations are
summarized in the sections that follow. They are described in roughly the order
they were encountered in the project.

All in all, the team believes that an
appropriate balance was indeed achieved in the varied activities of the
project. Obviously, time will tell whether this is correct, and, we will have
to observe the application and extension of IntelliGrid Architecture to ultimately judge these
choices.

Depth
vs. Breadth

During Task 1, the team sought to identify an appropriate
goal for coverage of utility operations for the project. We quickly found that
the most architecturally interesting future applications for the industry
involved transfer of information across departmental and institutional
boundaries, and especially, involved varied interactions with customers. The
team agreed that if we studied the communications requirements of these
cross-organizational types of applications, we could identify most significant
industry requirements. This is especially true because those communications
that remain within a constrained environment are already well understood and
often covered by well-documented industry standards and art.

The IntelliGrid Architecture project was able to study
communications requirements from markets to consumers, from power plants to
substations and pole-tops, and permutations of this breadth. For depth, the
applications were studied with a primary focus on the identification of the
participants in communications, the kinds of information exchanged, and, the
simplified exchange sequences that would typify such applications.

To bring the applications that were reviewed in
this manner to the point where the documentation fully specifies an
implementation would require several additional levels of detail. It would be necessary
for the models of data to be exchanged and all the details of the exchange
sequences, fault accommodation and recovery, etc. to be captured. As noted
elsewhere in the Conclusions and Recommendations, IntelliGrid Architecture is an ongoing process,
and further development of the depth of analysis would be very useful.

Stakeholder
Requirements

A pure systems engineering approach to any
problem will use stakeholder engagement to obtain requirements from potential users
and providers of services. Systems architects then analyze these requirements
in a formal process to identify commonality of need and the technically
detailed design requirements they imply.

In IntelliGrid Architecture project, stakeholder requirements
were captured primarily through the development of a document called the
‘Domain Template’. This document and process were designed to obtain detailed
information from ‘domain experts’ so we could obtain a quantitative view of
industry application requirements. This process is described in Volume II.

While we had great success in obtaining entrée
to those experts in the industry that could provide us with input, these same
experts had very limited time with which to devote on our behalf. Therefore, in
most cases we first populated a series of Domain Templates from the knowledge
and experience of the members on the team. We then presented these for
discussion with industry experts to refine their content. In a few instances,
we were actually able to obtain full Domain Templates from specific
stakeholders, but these cases were not very common

It would therefore be desirable to populate a
greater number of Domain Templates. While the project applied the 80/20 rule,
the last 20% of potential applications can be expected to introduce some new
concepts. This will be recommended for future work.

Functional
Requirements Analysis

The IntelliGrid Architecture Domain Template incorporates a
detailed spreadsheet. This spreadsheet identifies hundreds of potential
architectural requirements that are evaluated by the analyst for each of the
specific steps in the implementation scenario being described.

This analysis was time consuming and proved to
be beyond the effort that the stakeholders were able to invest. Therefore,
based on the engagement interviews, members of IntelliGrid Architecture team performed this
analysis on most of the Domain Templates. Several of these spreadsheets were
not completed, and it would be desirable to complete this in the future.

Mapping
to UML

The requirements were represented in the Domain
Template in the form of a natural language document and an analysis
spreadsheet. The template was arranged to have a careful and specific
correspondence to RM-ODP constructs, the
methodology adopted by the team. These same constructs were then represented in
UML using an automated tool, for import into the Magic Draw modeling tool.

It is possible to achieve several roughly
equivalent mappings that make logical sense in UML. Ultimately, the team chose
an approach that would optimize the match between the modeling tool, the
feature set of the Domain Templates, and the relationships we wanted to
preserve. The team was able to achieve a substantially satisfying result in
this manner. The resulting model carefully preserves all of the semantics
obtained through the Domain Template capture and analysis process, and provided
an explicit means to correlate actors, information objects, data exchanges,
requirements, services, environments, and technologies

However, we used more of a reliance on tagged
values (a UML extension mechanism) than we would have desired, due to their
unique ability to hold multi-valued constraints (a technical but important
detail). In the future, we might prefer to use UML constraints rather than
tagged values because they explicitly describe constraints on interfaces, objects and methods.

Template
Import

The templates were designed to be self contained
and populated by independent individuals and groups. After they were internally
complete, a normalization process was used to make the nomenclature used in the
various templates consistent with each other. This process of normalization
tended to be time consuming since the many objects identified in each template
– actors, information objects, etc. needed to be compared to similar ones from
other templates. A from/to list had to be constructed and the results reviewed
to ensure consistency and sanity of the results.

Although tedious, this was considered a
preferable approach to trying to coordinate all template population efforts to
use a consistent nomenclature while the nomenclature was being discovered
through the engagement process. However, in the future, the extensive list of
names (terms) identified can be used in subsequent uses of the template as a
suggested list to avoid redundant creations.

Parallel
Studies

While the stakeholder engagement process was
expected to derive substantial requirements from an application standpoint, the
team believed that it was necessary to perform a parallel investigation into
general topics such as security and network management, and, the relationship
of IntelliGrid Architecture to other architectures. This analysis was able to produce the next
level of detailed requirements that are beyond the scope of most stakeholders,
yet crucial to the proper operation of a distributed computing environment.

The IntelliGrid Architecture model of services first relies on a set of
simple primitives. These primitives can be combined to allow high level
services to be described. In the course of the project, it was possible to
identify an extensive set of high level abstract services and to somewhat
represent their relationship to architectural elements of IntelliGrid Architecture. However, there
was not sufficient time to apply these high-level services to the individual
steps in the Domain Template scenarios as would be desirable. All the necessary
information is in fact in IntelliGrid Architecture model to permit this to be done.  It
is suggested that this might be a desirable component of future work.

Aggregation
of Atomic Requirements

The requirements that were filled out in the
spreadsheets associated with the Domain Template were termed the atomic
requirements/questions because they were formed as questions using terms that
would be familiar to power system engineers. These 400 atomic
requirements/questions were therefore combined into 63 Aggregated Requirements
that more clearly identified the architectural requirements. Examples of this
mapping from atomic requirements/questions to Aggregated Requirements are:

§      
“Are the distances between communicating entities a few to many miles?”
plus “Location of information producer (source of data) is outside substation,
or another corporation or a customer site while the Location of the information
receiver is outside a substation, or another corporation or a different
customer site” became the Aggregated Requirement to “Support interactions
across widely distributed sites”

§      
“Eavesdropping: Ensuring confidentiality, avoiding illegitimate use of
data, and preventing unauthorized reading of data, is crucial” plus
“Information theft: Ensuring that data cannot be stolen or deleted by an
unauthorized entity is crucial” became the Aggregated Requirement “Provide
Confidentiality Service (only authorized access to information, protection
against eavesdropping)”

Development
of IntelliGrid Architecture Environments

During the analysis of the communication and
information requirements of the power system functions, it became clear that
the nature of these requirements depend upon a few factors:

§      
Locations of the entities exchanging information: some were within a
particular site, while some involved inter-site exchanges

§      
The response times and availability required by the functions: some
required very rapid, deterministic information flows, while others had less
stringent constraints

§      
The criticality of the information: some information flows were very
critical to reliable and safe power system operations, while others had less
impact

§      
Organizational boundaries: some information remained within one
organization, while other information flows involved multiple organizations

***Atomic Requirements Approach***. The
atomic requirement correlations were analyzed against technologies and services
in spreadsheets and the resulting relationships were imported into the UML
model in order to provide a complete integrated object model. The IntelliGrid Architecture team is
made up of primarily energy industry domain experts. As such the perspective
and experience of these members is a necessary and valuable ingredient in the
knowledgeable analysis of the data. However, in order to minimize bias in this
analysis, the correlations were captured at a more or less ‘microscopic’ level
– that of the individual requirements. This process is based on the idea that
if technologies are correlated to individual requirements, and the environments
are correlated to the same requirements, there will be a best fit between a set
of technologies and the description of an environment. This greatly simplifies
the specification process.

Unfortunately, there was not enough time in the
project to both capture this detailed analysis and devise an automated
optimization tool to distill its results that could be verified to be more
accurate than expert opinion. Therefore, while we made the analysis as
objective and specific as possible, no such analysis can be performed without
the need for educated judgment and this was applied.

***Aggregated Requirements Approach***.
In parallel, the 20 IntelliGrid Architecture Environments with their characterizing Aggregated
Requirements were linked to the standard technologies, common services, and
best practices, using expert opinion from IntelliGrid Architecture
team’s combined deep and broad experience in the utility and communications
industries. Although this approach might have permitted some bias, it was
believed that the checks and balances of the different experiences of the team
members, combined with long, in depth discussions of the different
technologies, have prevented any substantive bias.

This spreadsheet was then used to create documents
for each Environment, listing the categorizing Aggregated Requirements and the
associated links. These Environments can be found in Volume IV Appendix E and
on IntelliGrid Architecture website.

IntelliGrid Architecture
Web Pages/Website

The IntelliGrid Architecture, the results of
these analyses and linkages, along with the key discussions on communication
architectural issues were designed to be directly migrated onto IntelliGrid Architecture
website. This website will permit users to have more direct access to IntelliGrid Architecture
work through standard browsing techniques.

IntelliGrid Architecture is indeed a member of the digital society.

Areas
Beyond the Scope of IntelliGrid Architecture

IntelliGrid Architecture makes no recommendations in the following
areas because they are considered to be beyond the scope of this project.

  

|  |  |  |  |
| --- | --- | --- | --- |
| Table 7: Areas beyond the scope of IntelliGrid Architecture. | | | |
| Name | Description | Reasons for Exclusion | Exceptions |
| User Interface | All information exchanges that were identified as occurring between people and devices in the use cases. | Do not address communications between computer systems. | None. |
| Industry Organizational Changes | Changes to the overall business and regulatory structure of the industry. | Not technological issues. | Sometimes discussed with respect to a single organization, as needed to deploy particular strategies such as security. |
| Algorithms and Applications | Details of particular algorithms, such as load shedding, volt/VAR control, or auto-restoration. | Subject to rapid change and innovation, and therefore not a part of a long-term architectural specification. | Where the requirements of particular applications have a specific effect on the com­munications system, e.g. protection in general, but not specific protection schemes. |
| Electrical Power Trends | Emerging trends or ideas that have solely to do with the power system, e.g. the use of more DC links | Not communications issues. | Where trends have an impact on the communications system, e.g. the trend to using more DC links does not affect communications, but the trend to more demand-side management does. |
| Electronic Media | Applications involving the transmission of audio or video within the power system communications network. | To limit the scope, since the logistics and bandwidth needed to implement such applications may outweigh their benefits. | None. |

IntelliGrid Project cannot mandate – only recommend

Architecture documents formally developed by enterprises
and government are typically characterized by calling out the use of ‘mandated’
standards (and associated technologies) as well as ‘candidate’ standards for
use in developing information systems.  Mandated standards are those that
must be adhered to while candidate standards are those that are maturing and
may be mandated at a later date.  The IntelliGrid Architecture project does not have a
charter to mandate use, and therefore may only recommend use and back these
recommendations with analysis.  Users may review both the recommendations
as well as the supporting analysis to determine the strength of the
recommendation.

Not
the Final Word

The work of IntelliGrid Architecture is not done.  In fact, it
has only just started. As noted in the Project Summary, three key steps of
system architecture design remain to be executed:

§      
**Testing** the principles of the architecture in prototypes and
pilot projects.

§      
**Implementation** and validation of the design in real-world,
large-scale systems.

§      
**Integration** of the lessons learned into further iterations of the
process.

In addition, for the vision of a safe,
self-healing, reliable, optimized, and customer-integrated power network to be
realized, the industry must make a cultural and organizational commitment to
the *concept* of a common architecture.

For we must admit to ourselves that the digital
society has arrived, and we definitely must ensure our industry becomes part of
it; but most importantly, we must realize that it is our responsibility to *keep
it running.*

---

[[1]](Meth_Conclusions.htm#_ftnref1) <http://www.ucausersgroup.org/>

[[2]](Meth_Conclusions.htm#_ftnref2)
Kurt Yeager, EPRI CEO in an August
25, 2003 interview on the Lehrer News Hour about the August 14, 2003 East Coast
Blackout.

[[3]](Meth_Conclusions.htm#_ftnref3) IEEE  
STD 1471, 2001

[[4]](Meth_Conclusions.htm#_ftnref4) Hirst, Eric; “Transmission Planning for a New Era”; 1/2004;
<http://www.ehirst.com/PDF/TXPlanning102.PDF>

[[5]](Meth_Conclusions.htm#_ftnref5) IEEE  
STD 1471, 2001

[[6]](Meth_Conclusions.htm#_ftnref6)
Unified Modeling Language and UML are registered trademarks of the Object
Management Group, Inc.

[[7]](Meth_Conclusions.htm#_ftnref7)
IEEE 610.12

[[8]](Meth_Conclusions.htm#_ftnref8)
NIST, “Automated Knowledge Discovery System (AKDS)”, ATP, 2002

[[9]](Meth_Conclusions.htm#_ftnref9)
ISO/IEC 19793 Open Distributed Processing-Reference Model-Use of UML for ODP
viewpoints specifications – Working Draft.
