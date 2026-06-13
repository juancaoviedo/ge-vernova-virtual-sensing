# Document Overview

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Doc_Overview.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Document Overview

This is the technical analysis
volume. It is based on the architectural principles introduced in Volume I
section 3. Specifically it discusses in several concise sections and some large
appendices the details of the analysis and technical results produced by the
project.

To summarize, this
volume discusses:

|  |  |
| --- | --- |
| if !supportLists?·       endif?Architectural Principles | Relates the principles introduced in Volume I to the specifics of the analyses detailing them herein |
| if !supportLists?·       endif?Architectural Analysis | The high-level strategies used to solve the problem, the different environments, as well as common services, information models, and interfaces that were identified as the results of this analysis. |
| if !supportLists?·       endif?Technology Analysis | A comparative analysis of the universe of technologies available and which are most closely aligned with IntelliGrid Architecture requirements |
| if !supportLists?·       endif?Deployment Scenarios | To identify common integration scenarios and detail how IntelliGrid Architecture can be used to accomplish them. |
| if !supportLists?·       endif?Benefits and Conclusions | A brief summary of the benefits from a technology and interoperability standpoint. |
| if !supportLists?·       endif?Appendices A..E | Detailed discussions of research by the team |

## Architectural Principles

This section
reprises the levels of abstraction framework presented in Volume I. By successively
abstracting the architectural analysis via these descriptions, the dominant
aspects of architectural issues were exposed and detailed.

if !supportLists?·      
endif?Business needs

if !supportLists?·      
endif?Strategic vision

if !supportLists?·      
endif?Tactical approach

if !supportLists?·      
endif?Deployment scenarios

## Architectural Analysis

A primary goal of IntelliGrid Architecture project is designing a common architecture for utilities. This section
summarizes the principle modeling/analysis elements identified and applied in
IntelliGrid Architecture

 

|  |  |
| --- | --- |
| if !supportLists?·       endif?Requirements | Common industry requirements permit application constraints to be concisely and precisely defined. |
| if !supportLists?·       endif?Services | Refining applications into the services that can be combined in various ways to achieve functional goals. |
| if !supportLists?·       endif?Information models | Common building blocks of information exchanged to accomplish applications. |
| if !supportLists?·       endif?Interfaces | Low level primitives that act as atoms to build the molecular common services of IntelliGrid Architecture. The definition of these atoms facilitates the conveyance of the common services across environmental boundaries that may utilize different technologies. |

## Technology Analysis

This section
summarizes the results of detailed analysis performed on the following
important but often considered independent subjects crucial to collectively
achieving a robust architecture.

if !supportLists?·      
endif?Enterprise management

if !supportLists?·      
endif?Data management

if !supportLists?·      
endif?Platform

if !supportLists?·      
endif?Communications

if !supportLists?·      
endif?Security

## Deployment scenarios

In deploying
applications using IntelliGrid Architecture, this section identifies the issues to consider and
proposed solutions in performing integration.

 

|  |  |
| --- | --- |
| if !supportLists?·       endif?Field Device Integration | Shows how 61850 and DNP3 based SCADA systems can be integrated to provide unified rich model based device access and control. |
| if !supportLists?·       endif?Enterprise Management | Encompasses the integration of a DMTF based Enterprise Management systems with TC 57 based utility systems. |
| if !supportLists?·       endif?Application Integration | How a deployment of the CIM and GID can be used to create a platform for legacy application integration. |
| if !supportLists?·       endif?Data Analysis | As recovery of money spent on asset related operations is not guaranteed, it is critical that asset related costs be managed wisely. |
| if !supportLists?·       endif?Energy Market Integration | Describes how a utility might integrate Energy Market Transaction Servers with utility operational systems. |

## Benefits and conclusions

This section briefly
summarizes how IntelliGrid Architecture facilitates the realization of the following benefits:

if !supportLists?·      
endif?Reusable infrastructure

if !supportLists?·      
endif?Interoperability through standards

if !supportLists?·      
endif?Available off the shelf adaptors

if !supportLists?·      
endif?3rd party applications

if !supportLists?·      
endif?Extensibility

if !supportLists?·      
endif?Incremental approach

## What is in this volume

The following
table identifies and summarizes the major sections in this volume:

 

|  |  |
| --- | --- |
| **Section 1 Principles and Requirements** | The overall principles and requirements used to develop the architecture and a brief description of the problems it was intended to solve. |
| **Section 2 Analysis** | The high-level strategies used to solve the problem, the different environments, as well as common services, information models, and interfaces that were identified as the results of this analysis. |
| **Section 3 Technology**  **Recommendations** | Discussion of the implementation of the common modeling elements (services, information models, and interfaces) using specific recommended technologies within the defined set of environments. |
| **Section 4 Deployment Scenarios** | Guidelines and examples of how the architecture should be deployed by utilities. |
| **Section 5 Benefits** | Summarized the benefits of IntelliGrid Architecture from a technical standpoint |
| **Appendix A: Security** | A comprehensive discussion of security considerations for energy industry and related communications |
| **Appendix B: Network Management Technologies** | A discussion of network management technologies and needs |
| **Appendix C: Resilient Communication Services** | Discusses those technologies and requirements that are necessary for robust communications networks. |
| **Appendix D: Technologies, Common Services, and Best Practices** | A detailed summary of all the individual technologies, common services, and best practices identified by IntelliGrid Architecture project |
| **Appendix E: Environments** | A detailed description of IntelliGrid Architecture environments |
