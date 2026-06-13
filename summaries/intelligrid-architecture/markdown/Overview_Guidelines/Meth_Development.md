# IntelliGrid Development

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Meth_Development.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# The IntelliGrid Architecture Development Process

Before discussing exactly how system architects, power
system engineers, and system designers will use the IntelliGrid Architecture, the following subsections describe how the IntelliGrid Architecture was developed and what it contains.

Overview of the IntelliGrid Architecture Development Process

The development of the IntelliGrid Architecture and the process for using it are illustrated in and are described
in more detail below:

1.    
**Use Cases**, developed by IntelliGrid Architecture team and stakeholder domain
experts, were developed both to describe current and future power system
operational functions, as well as to illustrate the range of functional
requirements for power system operations that involve distributed information.
These Use Case descriptions contained three major components:

§      
Narratives that describe the function in plain language so readers can
fully understand the functions themselves

§      
The sequences of communications that need to occur between the various
‘actors’ that are either producing or consuming information as well as
identification of the information being communicated

§      
Identification of the requirements for each communication sequence such
as the Quality of Service required, security needs, configuration issues, and
data management needs.

Examples of Use Cases include wide area
measurement and control of transmission systems, real-time pricing, and
advanced distribution automation.

2.    
Both **domain and architecture experts** extracted the distributed
information requirements from the Use Cases and stored these requirements in a
database consisting of the distributed information requirements, organized by
the four issue areas

§      
Configuration issues

§      
Quality of Service issues

§      
Security issues

§      
Data Management issues

3.    
**The IntelliGrid Architecture High Level Concepts** for all
distributed information technologies were developed by IntelliGrid Architecture and Stakeholder
Architecture Experts through the analysis of current information technology
concepts and trends. These architectural constructs form the basis for the
detailed recommendations for the different technology solutions.

4.    
**The IntelliGrid Architecture Environments** were extracted by reviewing the
architecture requirements of all Use Cases and identifying patterns of similar
distributed information requirements. These environment-linked requirements
were analyzed to determine the appropriate technical solutions and best
practices that would be needed to provide solutions to the requirements.
Examples of environments include deterministic rapid response interactions within
a substation; secure interactions between field devices and control centers;
interactions among systems within a control center; and interactions between
market participants and Regional Transmission Organizations/Independent System
Operators (RTOs/ISOs).

5.    
**IntelliGrid Architecture Abstract Services** **and Generic Interfaces** were
identified as the abstract representation of the architectural requirements, in
which each requirement was assumed to have some abstract service able to meet
it. Thus, the confidentiality requirement became the Common Service ‘Provide
Confidentiality’. Common services are abstract because they do not represent
any specific technology for actually providing this confidentiality. Common
Services connect to one another via a set of Generic Interfaces.

6.    
**Recommended, Alternative, and Possible Technology Solutions and Best
Practices** were analyzed by IntelliGrid Architecture team and stakeholder technology
experts to link them to the technology independent architecture for each IntelliGrid Architecture Framework environment. Most of the recommended solutions met the
systems engineering principles and the high level concepts, while alternative
and possible solutions include legacy technologies as well. The capabilities of
the technology independent architecture, as well as the technology solutions
and best practices, are described briefly. In addition, their specific advantages/strengths and disadvantages/weaknesses are also
described.

## Development of IntelliGrid Architecture Environments

Use Cases described their architectural requirement in the
domain template spreadsheet. The IntelliGrid Architecture environments were
extracted from these Use Case spreadsheets, such that each environment was made
up of similar architectural requirements. These environments appeared as
patterns of ‘x’s’ in the spreadsheets.

Iterations on these environments allowed one environment
to be split into multiple environments if distinctions appeared in patterns,
or, vice versa, multiple environments to be merged into one environment, if it
turned out that no significant differences were found.

[![](../images/Using_IECSA_Reference_Architecture_small1.jpg)](../images/Using_IECSA_Reference_Architecture.jpg)

Figure
24: Development and Use of the Reference Architecture for Power System
Operations with Distributed Information (the IntelliGrid Architecture)

The figure
depicts the process the team used to develop IntelliGrid Architecture as well as the process
by which it gets used.
