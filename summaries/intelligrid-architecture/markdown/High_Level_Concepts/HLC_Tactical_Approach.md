# Tactical Approach

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/High_Level_Concepts/HLC_Tactical_Approach.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Tactical Approach

# Based on the Platform Independent Model

TheTactical Approach uses Information Object
Models, Common Services and Generic Interfaces to provide technology
independent solutions for implementing interoperable systems and for managing
the migration from legacy systems toward fully integrated systems.  To
understand why this approach is important, consider the primary methods that
have been used previously to achieve interoperability:

![](../images/Tactical_Approach_Proprietary_Links.jpg)

First Attempt:
Ad Hoc Proprietary Links as an After Thought. This approach is too expensive.

**Islands of Automation** - In the past, each system was developed by
itself, with little or no thought given to interconnecting it with other
systems. ‘Islands of Automation’ as they’ve been called, see Figure 13. With these islands of automation,
if one system needed data from another, some programmer would develop an ad hoc
protocol to link the two systems. This link was usually very simple but gave
the programmer work for life, since only they could fix it whenever it crashed.

![](../images/Tactical_Approach_Database.jpg)

Next Attempt:
Database as Method to Exchange Data. This approach is too inefficient.

**Database-Centric**
– A few years ago it became evident that this approach made these systems very
difficult to maintain, and those vendors were finding it very expensive to
expand and upgrade these systems. A new approach was needed. One tentative
approach was to require all data to be exchanged through databases, see Figure 14. This simplified the
problem of many different protocols by creating a single data exchange
mechanism. Data could be stored in the database by one system, and other system
could retrieve the data at some different time. However, this architecture was
recognized as being too brittle because changes to the database often
necessitated changes in many related systems making maintenance very costly.

**Platform Independent Model** – More recently,
more adaptable architectures have been developed. These architectures allow
systems to operate in concert while avoiding excessive interdependence, and
provide mechanisms for handling legacy systems more easily. The term ‘Platform
Independent Model’ identifies the separation between semantics (the meaning and
purpose of message exchange) and implementation (those specific technologies
that can carry out the message exchange). The Platform Independent Model (PIM)
is that former specification that is independent of any specific technology.

![](../images/Technology_Independence.jpg)

IntelliGrid Architecture Platform Independent Model: Common Information
Models, Common Services and Interfaces. This model manifests the desired
technology independent features described in this section.

The IntelliGrid Architecture tactical
approach is based on these principles:

**Development
and Use of a Technology Independent Design for Communications**–The
use of a technology independent design for communications and integration of
intelligent equipment is one of the more important concepts in the development
of interoperable systems and equipment today. This design is independent of the
physical media and networking protocols so the same language can be used in a
variety of different distributed computing environments.

**Layered
Technologies**–The
concept of technology ‘layering’ is a powerful concept that enables flexibility
in the integration of complex distributed computing systems. In simple terms,
layering enables the messages in communications to be independent of the
technologies that deliver the messages to the devices and equipment that will
comprise the future energy system. It is possible, for instance, to have the
same message carried over different communications media and different types of
networks. The ability to separate the transport of messages from the content
and meaning of the messages enables the powerful concept of a ‘common language’
described below. Layering also can enable the industry to make use of new
physical communications media that has not yet been developed. This can provide
a level of ‘extensibility’ for future systems.
