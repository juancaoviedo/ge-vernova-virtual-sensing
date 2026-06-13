# Architectural Principles and Requirements

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Arch_Principles.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Architectural Principles and Requirements

If one were to
envision a utility where an IntelliGrid Architecture based architecture had been completely
adopted, one would see that it provides an ideal platform for higher-level
analysis across the entire enterprise.  A
simple analogy might be that a utility executive ideally wants to drive a
utility much like a pilot might fly an airplane during cloudy conditions.  In this case, a pilot can use just
instruments to get a complete picture. 
That is, all required aspects of fight operation are visible via a well
laid out set of instruments.  Similarly,
since most utility operational information and risk is not visible unaided, a
utility manager uses a set of software components as instruments to get a
complete picture. The instruments condense and summarize all the required
information. To actually direct the airplane, the pilot uses a mechanical
interface consisting of a limited set of pedals, switches, levers, and
“steering wheel”.  How the instruments
and mechanical interface connect to the airplane and outside world is in
someway irrelevant to the pilot.  One could
say that pilots only care that a set of inputs lead to a set of desired results
via comprehensive user interface. 
Similarly, a utility executive wants a simple set of applications to
help direct the utility enterprise.

It is this unified comprehensible user
interface that IntelliGrid Architecture ultimately seeks to enable.  This interface may exist at many levels of
the utility.  For example, an executive
may be primarily concerned with balancing profit and risk whereas an
operational supervisor may be primarily concerned with balancing income and
reliability.  However, it is clear that
the primary goals of IntelliGrid Architecture are to enable a comprehensive view of operations and
analytics in a secure manner.

These end-to-end analysis applications largely
don’t exist today because without a single unifying architecture they are too
expensive to develop.  There are a great
variety of systems being used in a utility. In order to get a true picture of
the entire utility, these systems and data need to be integrated.   Consequently, development of the end to end
analysis application can be hugely expensive. 
Therefore in the past, even though the integration was technologically
feasible, it was not practical because the expense was prohibitive.  It is IntelliGrid Architecture Team’s belief that only via
the deployment of a unified architecture and standard solutions can the new
analysis applications be economically deployed. 
The IntelliGrid Architecture provides a unified architecture to realize this vision.

This
section starts with the requirements of utility industry applications that are
captured in the form of Domain Use Case. However, focusing on the applications
alone often bypasses the creation of common infrastructure capabilities that,
while burdensome to create for a single application, make it possible to realize
the myriad of functions that utility participants anticipate. In order to focus
on the capabilities of the shared architecture upon which secure end-to-end
looking applications can be built, we examine six essential “abstract use
cases” that describe the requirements of the common architecture.  This section shows the derivation of these
Abstract Use Cases and then describes the analysis done by IntelliGrid Architecture team to
develop the architecture.

As the analytical
phases of IntelliGrid Architecture project progressed, the team iteratively analyzed use cases
and derived solutions at subsequent levels of abstraction with increasing
detail.  A useful analogy is to say that
the analysis began by starting from business needs, and gradually descending
towards a more nearly realizable solution via design goals, abstract design and
technology recommendations.  We reprise
this analogy from Volume I section 3 in Figure
1.

 

if !vml?![](IECSA_VolumeIV_files/image002.gif)endif?

Figure
1: IntelliGrid Architecture Framework

This figure shows the levels of abstraction
used during IntelliGrid Architecture Enterprise Architectural Analysis.

 

At each level of
abstraction, the team looked to discover commonality so that a unifying
architecture could be discovered.  The
levels are described in Table
1.

|  |  |
| --- | --- |
| Table 1 Principles Applied to Each Level of Abstraction | |
| **Level of Abstraction** | **Principles applied to each problem area at this level** |
| Business Need | The Business Needs of the power industry were identified and their information requirements were assessed in the analysis of the utility operations functions and management. |
| Strategic Vision | The Strategic Vision for the IntelliGrid Architecture reflects the ultimate objectives for an information infrastructure that can meet all of the business needs, including network configuration requirements, quality of service requirements, security requirements, and data management and exchange requirements.  This Strategic Vision is based on unifying:  if !supportLists?–       endif?Abstract Modeling  if !supportLists?–       endif?Security Management  if !supportLists?–       endif?Network and System Management  if !supportLists?–       endif?Data Management and Exchange  if !supportLists?–       endif?Integration and Interoperability |
| Tactical Approach | TheTactical Approach uses Information Models, Common Services and Generic Interfaces to provide a deployment environment and technology independent solution for implementing interoperable systems and for managing the migration from legacy systems toward fully integrated systems. |
| Technology and Best Practices | This section describes how the Tactical Approach may be realized using implementable technologies.  It compares recommended technologies and discusses their merits in regard to how well they support the IntelliGrid Architecture. |
| Deployment  Guidelines | Provides guidelines on how to apply the architecture in a layered manner.  This is intended to help system designers create migration plans in which legacy applications can be adapted to conform to the architecture and new applications can be non-disruptively added. |

 

The remainder of
this section discusses the principles applied at each level of abstraction in
more detail.
