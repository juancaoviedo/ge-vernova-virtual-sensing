# For Project Engineers

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Gud_Guidelines_For_Engineers.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Guidelines for Project Engineers

## Designing a System Using the IntelliGrid Architecture

Project engineers (project designers, implementers,
project vendors, etc.) are responsible for implementing the information
infrastructure that is needed to meet the functional requirements specified by
the power system planners. Project engineers may be ‘in-house’ and work with
the power system planners to define the information infrastructure
requirements, and/or (more likely these days), they can be ‘out-sourced’
vendors and implementers who are contracted to implement the functional
requirements described by the power system planners within a set of technical
specifications. In either situation, the project engineers must be familiar
with the specific requirements, not only for new functions, but also most
importantly for all existing systems that the new functions must interact with.

Project engineers can use the IntelliGrid Architecture
for a specific implementation project. These project engineers will utilize the
Power System Functions identified by the power system planners to determine the
detailed requirements associated with each step or ‘environment’ of the power
system functions. These environments link to the appropriate IntelliGrid Architecture website that
describe the Platform Independent Architecture as well as recommended
standards, technologies, and best practices for providing the information infrastructure
needed by these power system functions. The IntelliGrid Architecture website also identify
alternatives and possible solutions for each type of interface, thus providing
choices to the project engineers. Since different implementations will always
have different constraints, existing legacy systems, and corporate policies,
the project engineers will be able to review this range of solutions and select
those solutions which best match the unique needs of their implementation.

The basic steps for a project engineer are:

* [Review the power system functions](Gud_Guidelines_For_Engineers.htm#Review_Power_System_Function_‘Steps’_and_Associated_Environments) as defined by the Power System
  Planners, and, using the IntelliGrid Architecture documents or web pages,
  determine if similar functions are described.
* [Review the IntelliGrid Architecture Strategic Vision](Gud_Guidelines_For_Engineers.htm#Review_IntelliGrid_Architecture_Framework), including the high
  level concepts of Modeling, Security, Network Management, Data Management,
  and Interoperability. These concepts should be directly included in any
  project. In particular, UML modeling should be used to define or describe
  the project, starting with Use Case diagrams. Even if the implementation of
  the function will be outsourced, UML Use Case diagrams can be used to
  develop the functional specifications and the interfaces to external
  systems. Depending upon the complexity of the project and the degree of
  in-house development, additional UML models can be developed.
* [Determine which
  IntelliGrid Environments are relevant to the project](Gud_Guidelines_For_Engineers.htm#Determine_Relevance_of_IntelliGrid_Architecture_Environments), either directly
  from the IntelliGrid functions or from an assessment of the functional
  requirements of the project. Using the IntelliGrid Environment definitions, assess which of the Configuration,
  Security, Network Management, and Data Management requirements are
  applicable to the current project.
* [Assess
  the applicability and degree of importance of each Environment's
  requirements to the project](Gud_Guidelines_For_Engineers.htm#Assess_Requirements_in_Each_Environment_for_Applicability). This assessment will guide or drive the
  ultimate decisions on which technologies to implement.
* [Review the IntelliGrid Architecture
  Tactical Approach](Gud_Guidelines_For_Engineers.htm#Platform_Independent_Model), including the use of platform independent approaches
  which permit the integration of legacy technologies through the use of
  standardized interfaces.
* [Assess the applicability and feasibility of the standards, technologies,
  services, and best practices](Gud_Guidelines_For_Engineers.htm#Technologies,_Services,_and_Best_Practices_for_Each_IntelliGrid_Architecture_Environment) in each of the relevant Environments to
  meet the needs of the project.
* [Determine which of the recommended, possible, or alternative solutions](Gud_Guidelines_For_Engineers.htm#Determine_Which_of_the_Recommended,_Alternative,_and_Possible_Solutions_to_Use)
  to use in implementing the project, using the lists of different types of
  technologies for each of the different types of requirements in each of the
  Environments. This step does require understanding and analysis of those
  technologies in order to determine which are best for the project, while
  still respecting other drivers such as the technologies currently used in
  systems which the new system will have to interface with.

A key thing to keep in mind is that project engineers
cannot simply require vendors to ‘comply with IntelliGrid Architecture’. This is too broad a
statement, since the IntelliGrid Architecture is a *reference*, not
a specification. Instead, project engineers should include IntelliGrid Architecture Platform
Independent Model as a template that they wish vendors to adhere to and may
also select the appropriate standards, technologies, and best practices from
this reference.

### Review Power System Function ‘Steps’ and Associated Environments

![](IECSA_VolumeI_files/image019.jpg)

Figure 19:  Power System Function Steps with
links to IntelliGrid Architecture Environments

Having received
the technical specifications from the power system planners, the project
engineers review the functional requirements and referenced Power System
Function. They review either the paper or IntelliGrid Architecture Website version of the Power
System Function, identify the appropriate Power System Function steps that
apply to the functions, and note IntelliGrid Architecture environments are associated with
each of these steps.

These IntelliGrid Architecture environments are the key methods by
which project engineers can utilize the IntelliGrid Architecture. Each
IntelliGrid Architecture environment, which represents the information infrastructure requirements
of the business needs, links to the three information infrastructure constructs
of the IntelliGrid Architecture Framework (as shown in Figure 19). These constructs are:

§      
Strategic Vision and High Level Concepts

§      
Tactical Approaches

§      
Standards, Technologies, and Best Practices

### 

![](IECSA_VolumeI_files/image020.jpg)

Figure
20: IntelliGrid Architecture Strategic Vision

### Review IntelliGrid Architecture Strategic Vision

The IntelliGrid Architecture Framework, and
the underlying Strategic Vision, High Level Concepts, and Platform Independent
Architecture are relevant for all IntelliGrid Architecture Environments. These concepts provide
the goals toward which all project implementations should to head over the long
term, and are therefore vital to understanding the recommendations made in the
IntelliGrid Architecture.

The overview of the Strategic Vision and
Tactical Approaches are found in Volume I, Section 3 in the paper version, and can
be jumped to from IntelliGrid Architecture website home page as seen in Figure 20.  A
more detailed discussion of the technical issues related to the architecture
can be found in Volume 4.

### 

![](IECSA_VolumeI_files/image021.jpg)

Figure 21: Environments

### Determine Relevance of IntelliGrid Architecture Environments

Project engineers can review key requirements associated
with each relevant IntelliGrid Architecture environment and assess how
applicable they are to the project requirements. These key requirements are discussed in
Volume I, Section 3, or are available on IntelliGrid Architecture website through IntelliGrid Architecture
Home Page as seen in Figure 21.
Analysis of requirements appears in Volume 4 during the derivation of IntelliGrid Architecture

 Platform Independent Architecture.  The description of IntelliGrid Architecture
Environments contains:

§      
Discussion of the characteristics of the environment

§      
The requirements that define the environment

§      
The recommended technologies, services, and best practices

§      
The alternative technologies, services, and best practices

§      
The possible technologies, services, and best practices

![](IECSA_VolumeI_files/image022.jpg)

Figure 22: Requirements for Defining Environments

### Assess Requirements in Each Environment for Applicability

Each IntelliGrid Architecture environment description includes the
list of requirements that defines it. This description can be found in Volume
IV, Appendix D and on IntelliGrid Architecture website as can be seen in Figure 22. The Project Engineers
should review these requirements to ascertain which may be the more important
for the particular project they are working on, and how applicable they are. This prioritization can help
them determine what decisions to make on the various standards, technologies,
and best practices that are associated with the Environment.

### Review Platform Independent Model

Project engineers
can see the Platform Independent Model, either by browsing the IntelliGrid Architecture website or by reading IntelliGrid Architecture Volume 4 document.  Project
Engineers need to promote a clear boundary between application requirements and
the choice of specific technologies.  Achieving a technology independent
design for how to implement a system provides guidance to implementation
engineers and achieves a level of interoperability, while still affording the
flexibility that implementation engineers require to meet project goals and
constraints.

### Assess the Applicability of the Technologies, Services, and Best Practices for Each IntelliGrid Architecture Environment

Project engineers can see the list of
standards, technologies, and best practices associated with a particular
environment, either by scrolling down IntelliGrid Architecture environment web page or by
manually looking up the list in the paper version. From IntelliGrid Architecture website, this
list links directly to brief descriptions of the standards, technologies, and
best practices.

At the same time, project engineers will need
the flexibility to use alternative technologies for specific implementations,
due to existing legacy systems, existing vendor products, time constraints for
implementation, financial constraints, company
policies on technology choices, and a variety of other factors.

### Determine Which of the Recommended, Alternative, and Possible Solutions to Use

**![](IECSA_VolumeI_files/image023.jpg)**

Figure 23: Recommended Standards, Technologies, and
Best Practices

It is for this reason that environments point
not only to ‘Recommended’ standards, technologies, and best practices, but also
include ‘Alternative’ and ‘Possible’ solutions as seen in Figure 23.

* **Recommended** solutions are those that
  mostly meet the Strategic Vision High Level Concepts and are easily interfaced
  with using the Tactical Approaches.
* **Alternative** solutions - those
  technologies that “mostly” meet IntelliGrid Architecture vision
* **Possible** solutions - those technologies
  that don’t adhere to IntelliGrid Architecture vision but functionally meet the requirements.

These distinctions are based on expert opinions
and often fall into ‘gray’ areas where one alternative solution may be better
than another alternative solution under different circumstances, and vice
versa, while a possible solution may still be the only available solution due
to the availability of vendor products, legacy systems, or one-of-a-kind
implementations.

Project engineers should review the recommended
solutions and use those if feasible. Sometimes there may be more than one
recommended solution for the same requirement. This stems from the fact that
one solution cannot possibly meet all needs. For instance, specific
implementations must take into account legacy systems, corporate policies, and
financial situations. Given this, the recommended solution may not be
acceptable for a specific implementation. Or one solution can partially meet a
requirement, but requires another solution to meet the requirement completely.
If no recommended solution is feasible for a particular requirement, then a
migration plan should be included in the specifications to indicate how the
recommended solutions could be achieved at a later date.

Project engineers can use alternative solutions
that best meet the specific requirements. Possible solutions should be avoided
unless no other solution is feasible.
