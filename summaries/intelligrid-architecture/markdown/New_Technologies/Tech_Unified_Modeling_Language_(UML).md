# Unified Modeling Language (UML)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Unified_Modeling_Language_(UML).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Unified Modeling Language (UML)

**URL:**http://www.omg.org

**Abstract
Modeling in UML**

Abstraction,
the focus on relevant details while ignoring others, is a key to learning and
communicating. Modeling is the process of abstracting from the morass of stuff
to develop a coherent, multi-faceted vision. Because of this:

·       Every complex
system is best approached through a small set of nearly independent views of a
model. No single view is sufficient.

·       Every model may
be expressed at different levels, ranging from highly abstract to the concrete.

·       The best models
are connected to reality.

The
generally accepted methodology for software modeling is the Unified Modeling
Language (UML), which has been endorsed by the Object Management Group (OMG),
the leading industry standard for distributed object programming. UML is the
standard language for visualizing, specifying, constructing, and documenting
the artifacts of a software-intensive system. It can be used with all processes,
throughout the development life cycle, and across different implementation
technologies. UML combines the best of the best from Data Modeling concepts
(Entity Relationship Diagrams), Business Modeling (work flow), Object Modeling,
and Component Modeling

Vendors
of computer-aided software engineering products are now supporting UML and it
has been endorsed by almost every maker of software development products,
including IBM and Microsoft (for its Visual Basic environment). UML is a
standard notation for the modeling of real-world objects as a first step in
developing an object-oriented design methodology, and is used as the language
for specifying, visualizing, constructing, and documenting the artifacts of
software systems, as well as for business modeling and other non-software
systems. UML represents a collection of the best engineering practices that
have proven successful in the modeling of large and complex systems.

The
UML modeling methodology is very powerful in that it can be used from the
highest overview levels to actual implementation code,
and from the largest global project to a tiny enhancement project. The key
benefit of using UML is that provides methodologies for visualizing the complex
interactions that must be implemented in an invisible cyber world. It consists
primarily of structured diagrams that are designed to illustrate different
aspects of cyber behavior. A number of CASE tools exist for developing these
UML models as well-structured diagrams. The different UML modeling concepts and
types of diagrams are described below.

**Use
Cases**

Use
Cases are modeling constructs which focus on the interactions between functions
and actors from a users point of view. The basic idea
for a Use Case is to capture the requirements of these actors in relationship
to the function. "Actors" are defined as the ultimate sources or
users of information for a particular Use Case scenario, and do not need to be
humans. For instance, the power system can be seen as an Actor when it provides
the source data for a SCADA system, while a billing system can be the user of
metering data from an Automatic Meter Reading system.

Use
Cases are layered or iterative in concept. For instance, in a Use Case diagram,
a function is defined as a Use Case itself (which sometimes leads to confusion,
but does emphasize the layered nature of Use Cases). As an example, in one Use
Case diagram, the function "Distribution Automation Functions" could
be defined as a single entity within distribution operations, while this same
function could be expanded into its own Use Case, showing the individual
functions as separate entities.

Therefore,
the scope of a particular Use Case is entirely a function of what needs to be
defined. In a broad picture Use Case, distribution system operations can be one
function within utility operations. In a detailed picture Use Case, the
Distribution Automation Volt/Var Optimization application can be the primary
function. Therefore, often Use Cases are used first to define the overall
Business Processes, and then are utilized to take each function within a
Business Process and drill down to more detailed levels.

if !vml?![](../IECSA_Volumes/IECSA_VolumeIV_AppendixD_files/image009.gif)endif?Modeling implies diagrams. Use
Case Diagrams consist of Actors (often represented as little stick people) and
Use Cases (ovals) linked by lines that indicate relationships, such as "is
associated with", "is an aggregation of", or "is a
generalization of". An association, which is represented as a line with
one or two arrows, provides a pathway for communication. The communication can
be between use cases, actors, classes or interfaces.
Associations are the most general of all relationships and consequentially the
most semantically weak. If two objects are usually considered independently,
the relationship is an association. Other relationships include "generalization"
and "dependency".

The
benefits of Use Cases include:

·       Visualizing
processes and interactions which otherwise might be obscure or lost in the
complexity of a system

·       Capturing
requirements from user's perspective

·       Users are not
only involved in providing requirements, but can actually understand and
validate what is being designed

·       A good way to
start identifying information which will be exchanged among the functions and
actors

·       One way of
estimating the percentage of requirements captured

·       Categorizing
functions and determining which impact the others particularly if a
"phased delivery" implementation is planned

·       A better way of
estimating the percentage of requirements completed during development.

·       Test plan can be
immediately generated based on use cases

·       Helps technical
writers in structuring the overall work on the users
manuals at an early stage

·       Better
traceability throughout the system development process

·       Quality of the
software is improved by identifying the exception scenarios earlier in the
development process

**Behavior
Diagrams**

Behavior
Diagrams are used to model the behavior of entities. Two primary types of
diagrams can be used: the Activity Diagram and the State Chart Diagram.

**Activity
Diagrams** provide a way to model the workflow of a business process.
Activity diagrams are very similar to a flowchart because the workflow can be
modeled from activity to activity. An activity diagram is basically a special
case of a state machine in which most of the states are activities and most of
the transitions are implicitly triggered by completion of the actions in the
source activities.

These
diagrams should not replace the original Use Cases, although there is sometimes
a tendency to bypass the Use Case process as unnecessary and jump right to the
Activity Diagrams. However, the Use Case is vital to capturing the views of the
user, which is often overlooked or assumed if the business process analysis
starts with the Activity Diagram.

**State
Chart Diagrams** define the States and the dynamic behavior for going between
States for a particular function (Use Case) or object (Class). These diagrams
show the sequences of states that an entity goes through, the events that cause
a transition from one state to another, and the
actions that result from a state change. State Chart diagrams are closely
related to Activity diagrams. The main difference between the two diagrams is
that State Chart diagrams are state centric, while activity diagrams are
activity centric. A State Chart diagram is typically used to model the discrete
stages of an entity's lifetime, whereas an activity diagram is better suited to
model the sequence of activities in a process.

Each
state represents a named condition during the life of an entity during which it
satisfies some condition or waits for some event. A State Chart diagram
typically contains one start state and multiple end states. Transitions connect
the various states on the diagram. As with activity diagrams, decisions,
synchronizations, and activities may also appear on State Chart diagrams.

An
example from the OASIS submittal of transmission requests is shown in the
Figure OASIS State Diagram (click to enlarge).

**Interaction
Diagrams**, consisting of Sequence Diagrams and Collaboration Diagrams, focus
on the interactions between entities. These diagrams are particularly important
in the development of Information Exchange Models (IEMs).

**Sequence
Diagrams** specify the precise sequence of information flows between
functions, including acknowledgments, error handling, and other details. A
sequence diagram is a graphical view of a scenario that shows object
interaction in a time-based sequence, i.e., what happens first, what happens
next. This type of diagram is best used during early analysis phases in design
because they are simple and easy to comprehend. A sequence diagram has two
dimensions: typically, vertical placement represents time and horizontal
placement represents different objects. Sequence diagrams are normally
associated with Use Cases, since they can be used to focus on the interactions
between Actors and the functions they interact with.

Sequence
diagrams are closely related to collaboration diagrams and both are alternate
representations of an interaction. There are two main differences between
sequence and collaboration diagrams: sequence diagrams show time-based object
interaction while collaboration diagrams show how objects associate with each
other.

**Collaboration
Diagrams** illustrate how entities interact with each other. Collaboration
diagrams and sequence diagrams really are alternative representations of the
same interaction, in which a collaboration diagram shows the order of messages
that implement an operation or a transaction, while a sequence diagram shows
object interaction in a time-based sequence. In some CASE tools, the capability
is provided to create a Collaboration diagram from a Sequence diagram and vice
versa. Collaboration diagrams show objects, their links, and their messages.
They can also contain simple class instances and class utility instances.

**Class
Diagrams** visually describe the structures and relationships of data
entities, explicitly showing their contents (attributes) and their actions
(operations). The word "entity" is used rather than
"object" because Class Diagrams can be used to describe both objects
models of individual data items and metadata models of definitions of data
items and their relationships. The Figure shows a Class Diagram of a metamodel of
an Energy Schedule.

Visually,
Class Diagrams contain icons representing classes, interfaces, and their
relationships, and can be multi-level and nested through the use of Packages.
Packages are used to group similar Class Diagrams.

For
utilities, the best known set of Class Diagrams is the Common Information Model
(CIM) which is a metadata model of the power system (primarily) with additional
Packages describing other aspects of power system operations. This CIM model is
being expanded to encompass distribution operations, asset management, and
other areas.

For
Information Exchange Modeling purposes, Class Models can be used both to define
the metamodels of the data to be exchanged, as well as the structure of the
information messages themselves.

**Implementation
Diagrams** take the abstract information of the other types of diagrams and
convert it into more physical views, using one of many software languages, such
as C++, Java, JavaScriptTM, CORBA, Microsoft's COM, and others. Alternatively,
the conversion can be into a data language, such as Document Type Definition
(DTD) or XML.

**Component
Diagrams** provide a physical view of the current model. A component diagram
shows the organizations and dependencies among software components, including
source code components, binary code components, and executable components.
These diagrams also show the externally-visible behavior of the components by
displaying the interfaces of the components. Calling dependencies among
components are shown as dependency relationships between components and
interfaces on other components. Note that the interfaces actually belong to the
logical view, but they can occur both in class diagrams and in component
diagrams.

Component
diagrams contain Component packages, Components, Interfaces, and Dependency
relationships. A Component Package Specification enables you to display and
modify the properties of a component package. Similarly, a Component
Specification and a Class Specification enables you to display and modify the
properties of a component and an interface, respectively. The information in
these specifications is presented textually. Some of this information can also
be displayed inside the icons representing component packages and components in
component diagrams, and interfaces in class diagrams.

In
some CASE tools, the properties of, or relationships among, component packages,
components, and interfaces can be changed by editing the specification or
modifying the icon on the diagram. The affected diagrams or specifications are
automatically updated. An additional capability of some CASE tools is to
reverse engineer a set of objects that are already in another language (such as
C++ or XML) and convert them back into abstract Classes with all attributes and
relationships where possible.

A
portion of the energy schedule class information, specifically the first couple
of objects in the E-tagging specification, is shown in XML in the Figure.

**Deployment
Diagrams** show processors, devices, and connections, in other words, the
physical location where each of the component models will be implemented.
Therefore, each model contains a single deployment diagram that shows the
connections between its processors and devices, and the allocation of its
processes to processors.

**UML
Methodology**

The
methodology for using UML can be summarized as follows:

1.
**Develop Business Processes, using Use Cases**

Pick
a business process, e.g. Day-ahead Submittal of Energy Schedules by Scheduling
Coordinators

Determine
all the Actors, e.g. Scheduling Coordinator and Time Line Manager

Determine
the Use Case functions or systems involved, e.g. Market Interface Web Server,
Format Validation Procedures, Database of Energy Schedules, and Congestion
Management function. Since business processes are usually at a higher and
broader level than individual functions, these Use Cases are do not focus on a
single function to show basically its inputs and outputs, but show the
"forest" rather than the "trees".

Describe
all performance requirements, pre- and post-conditions, and other assumptions,
e.g. responses to submittals will be within 5 seconds or at pre-specified
times, Scheduling Coordinators are all registered, post-condition is that
schedule is accepted or rejected

Draw
and describe the interactions between the Actors and Use Cases, including
sequences of steps and decisions affecting information flows, e.g. Sequences
for error checking, ability of Scheduling Coordinator to withdraw schedule,
etc. These can be documented in Activity Diagrams, Sequence Diagrams,
Collaboration Diagrams, and State Diagrams, along with text to clarify the
interactions.

2.
**Develop Data and/or Messages Contents, using Class Diagrams**

a.
Identify the Data or Message Type for each interaction in the business process:
Message Type consists of a noun (the data) and a verb (how/when/under what
conditions is the message sent)

·
There are many, many Nouns, e.g. New energy schedule or update to an existing
energy schedule

·
There are very few Verbs, e.g. Send, Request, Acknowledge Response, Error
Response

b.
Organize and list all elements required by each Data or Message Type

·
“Organize” means identify specific parts of a message that are probably
re-usable for other messages, e.g. Message Header, Scheduling Coordinator
information, RTO information, E-tagging information (so that format can be
used), Time and Date information, Other

·
Indicate if there is a one-to-one or a many-to-one correspondence between a
part and the message, e.g. only one Scheduling Coordinator, but one or more
schedules

·
List all elements for each part, e.g. Scheduling Coordinator Corporate name,
Scheduling Coordinator ID, individual sending schedule, etc.

3.
**Translate Classes into Component Models**

a.
Convert the classes into Document Type Definitions (DTD), using IDL or, as is
becoming more common, using XML-DTD.

b.
These components can be translated into actual software code if so desired.

4.
**Register these DTDs** so that all users of the information can access
them. XML Registries can be public (e.g. ebXML uses OASIS XML Registry) or can
be private. This step is not actually part of UML, but is becoming a powerful
means to publish, maintain, and update information exchange templates among
large groups of users.
