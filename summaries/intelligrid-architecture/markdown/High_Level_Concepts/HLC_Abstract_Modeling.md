# Abstract Modeling

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/High_Level_Concepts/HLC_Abstract_Modeling.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Abstract Modeling

Modeling is one of the most powerful tools
available for understanding, documenting, and managing the complexity of the
infrastructures required to operate the energy system of the future. It is far
less expensive to construct a model to test theories or techniques than to
construct an actual entity only to find out that one crucial technique is wrong
and the entire entity must be re-constructed.

Models have been used extensively by many
industries as the basis to analyze and design complex systems. The
telecommunications industries have made extensive use of modeling to develop
the diverse communications infrastructure(s) in widespread use today. Physical
models are used in many industries, ranging from airplanes and Mars Landers to
circuit breakers and transformers. Building architects use paper models
(blueprints) to capture all the complexity in a modern high-rise building.
Virtual models are increasingly being used to model even more complex concepts,
from weather patterns to cosmology and, of particular interest to IntelliGrid Architecture
project, to information management. One can even make a simple abstract model
of the IntelliGrid Architecture, see Figure 9 below.

![](IECSA_VolumeI_files/image009.gif)

Figure
9: Abstract Model of
the IntelliGrid Architecture

A simple abstract
model of the IntelliGrid Architecture helps visualize what components and
how they interact.

The following abstract modeling methodologies
and concepts were incorporated into the IntelliGrid Architecture:

**Reference
Model for Open Distributed Processing and the Unified Modeling Language****–**Years of engineering have been invested in defining
how enterprise level architecture should be defined. RM-ODP
is an international standard (ISO/IEC 10746) prescribing a methodology for architectural
development. The methodology provides guidance on breaking the problem into
understandable pieces and helps to ensure that important design details are not
forgotten.

By design, RM-ODP
provides the methodology, but does not include a recommended notation for
documenting an architecture. The most popular standardized notation for system
modeling is the Unified Modeling Language (UML), which provides a standardized
way to graphically document the systems and components of an architecture. Together
RM-ODP provides the architectural guidance
and UML provides the standardized notation. It should be noted that as of this
writing, the standards for applying UML to RM-ODP
concepts are under development. As the energy industry moves forward in the
development of advanced automation systems, the adoption of these sophisticated
methods should be encouraged.

**Object
Modeling and Information models** define data names and structures.
These information models can be described informally as consisting of nouns. Nouns
consist of data names and their structure. Examples include simple data points
such as a point called ‘State’ that consists of one 8-bit integer, as well as
more complex data points that include the value, the quality of the value, the
description of the point, etc. These nouns can also range to complete
descriptions of a utility’s power system, for example ‘ABCPowerSystem’, which
consists of thousands of components in some well-known structure. There can be
millions of nouns in any system.

In the power industry, IEC61850 includes such a
model, which is focused on field device characteristics. Another information
model is IEC61970 Common Information Model (CIM), which is focused on modeling **what**
information about the power system structure is to be exchanged among
application programs. It has been expanded to model other types of information
to be exchanged among application programs. As an information model specifies **what**
information is exchanged, it is part of an RM ODP
information view.

**Abstract
Service/Interface Models****–**A **service** model describes the functionality that a software
application provides. IntelliGrid Architecture’s Common Services describe common functionality
needed to operate a utility. For example, the common service of ‘LogOn’
specifies the common function of initiating a secure session with a software
application.

An **interface models** define the mechanics
of how data is passed to get the right information to the right destination at
the right time. These interface models can be described informally as consisting
of verbs. Verbsare the abstract services used to exchange the nouns,
such as ‘request’, ‘send’, ‘report if changed’, ‘add to log’, etc. Although
different verbs/services are used in different environments, the number of
different types of abstract verbs/services is generally on the order of 10 to
20.

In the power industry, IEC61850 includes such a
model, which is focused on field device operation. Another service model is
IEC61970 Generic Interface Definition (GID),
which is focused on **how** information about the power system structure is
to be exchanged among application programs. An interface model specifies **how**
information is exchanged; it is part of an RM ODP
Computational View.

**Naming
and avoiding ambiguity (name collisions)**–One aspect of information models is the need to
uniquely identify all objects within the model. In addition, as the number of
names being used proliferates, there is a need to avoid ‘name’ collisions. That
is the same name used with two different meanings. This is handled by namespace
allocation. Namespace allocation is a very simple concept: different groups can
have the authority to give names their own objects so long as those names are
unique within the group’s domain; however, they do not need to be universally
unique. This permits different groups, whether they are whole industries, or
standards organizations, or types of products, or a department within a
company, to define their own terminology and abstract model names and
structure.

Namespace allocation for the electric power
industry should be performed in a top-down manner that clearly captures the
different arenas. Although some namespaces should be as broad as possible
(i.e., valid across the entire electric power industry), additional namespaces
should be allowed as part of a formal scheme to permit specific utilities,
specific vendors, specific functions, and other groups to apply for and
register their own namespaces.

An example of namespaces within the IEC TC 57 is
the allocation substations to the IEC61850 namespace and the allocation of
transmission power system applications to the IEC61970 namespace.

**Self-Description
and Discovery**–Future advanced automation systems
must have more capable methods for managing networks, connected equipment and
the applications that run on this equipment. This will require more
sophisticated systems to assist system administrators in managing large scale
networks and massively distributed equipment. Concepts such as self-description
and discovery will become a necessary part of future systems or maintenance
could easily become unwieldy.

Self-description and discovery is a fancy name
for what happens when you plug a new printer into a PC: For example:

§      
1st message: “New hardware detected”

§      
2nd message: “Driver xxx is being installed”

§      
3rd message: “Printer is ready for use”

Now, imagine a SCADA/EMS
system performing equivalent actions:

§      
1st message: “New RTU detected”

§      
2nd message: “SCADA database being updated”

§      
3rd message: “Data acquisition commencing”

§      
4th message: “Power System Model being updated”

§      
5th message: “Contingency Analysis is ready to execute”

Self-description and discovery form the basis
for ‘plug-and-play’ technologies. The concept behind self-description and
discovery is that data models can be stored electronically in repositories,
servers, and other distributed databases, using a language for describing data
such as XML. These XML descriptions of the data models are ‘self-describing’: they
contain the standardized name of the data along with the structure and
formatting of the data. Thus, they can be browsed by users who can immediately
understand what they are browsing.

In addition, ‘discovery’ of these data models
can be implemented by special applications (which could be called intelligent
agents or metadata browsers) that ‘read’ the name and format of the data in the
remote server (e.g., ‘New RTU’), set up their own local database (SCADA
database) to reflect this name and format, then establish links so that the
actual information can be read from the remote server and stored in the local
database (Data Acquisition commencing).

**Technology
Independent Design**–Using
a technology independent design is an important concept when developing interoperable
systems and equipment today. A technology independent design must focus on the
behavior and structure of the components within a system and abstract the
implementation details of any particular technology. This key concept allows
for different implementations and technologies to exist, yet still allow these
components to be used interchangeably. Using technology independent design
enables a coherent architecture to be created independently of deployment
specifics. When implemented, the technologies are chosen to meet requirements
but are implemented in a way that complies with the technology independent
design.

Some of the concepts derived from
technology independent design are developed in more detail in the Tactical
Approaches section.
