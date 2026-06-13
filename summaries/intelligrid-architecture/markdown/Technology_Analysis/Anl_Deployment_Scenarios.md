# Deployment Scenarios

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Deployment_Scenarios.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Deployment Scenarios

This section focuses on the use of existing and emerging
technologies in support of the creation of a “plug and play” utility
integration/analysis architecture. As described in previous sections,
integration of legacy systems is a key prerequisite for the creation of
end-to-end analysis applications.  This
section includes four use cases:

if !supportLists?·      
endif?Integration of devices

if !supportLists?·      
endif?Integration of Enterprise Management

if !supportLists?·      
endif?Integration of applications

if !supportLists?·      
endif?Integration of data

if !supportLists?·      
endif?Integration of energy market systems.

This section uses the standards created within IEC
Technical Committee (TC) Working Group (WG) 10, 13 and 14 as well as DMTF
related technologies as examples of the how an IntelliGrid Architecture based architecture can be
deployed to minimize the effort required to integrate systems.  The common characteristic of these
technologies is that they all provide generic interfaces to access a shared
information model exposed via a rich address space.  The goal of this section is not to promote
the use of these technologies in particular, but to show how the common
approach underlying IEC and DMTF technologies is used to realize the IntelliGrid Architecture.   

## Introduction

The current economic climate and market initiatives
require utilities to perform more efficiently and in more flexible ways. The
dynamic nature of today’s environment means that a utility must be able to
build an integration infrastructure for operational integration and data
analysis quickly to provide a base for knowledgeable and adaptable business
models. A commonly accepted way to achieve a flexible software infrastructure
is via the use of plug and play components. Plug and play means that best of
breed applications can be installed, integrated and upgraded or swapped more
simply and at a lower cost. 

To create a plug and play environment for utility
operational integration and analysis in a cost effective way, several elements
must be agreed upon. First, applications must all employ a common meaning for
the information they exchange. Second, applications must all employ a common
set of mechanisms by which they connect to each other and exchange information.
The first requirement addresses “what” data is exposed and the second addresses
“how” data is exposed. While establishing agreement on both of these issues is
required to achieve complete plug and play, complete agreement on all aspects
of these issues is not possible. This does not mean that the amount of effort
required to perform integration cannot be minimized via the use of standards.
Rather, this means that because of the heterogeneous nature of legacy
applications, complete interchangeability of applications cannot be realized.
This section lays out several examples showing how the high level concepts
described in Volume 1 can be realized to what extent plug and play can be
achieved, as well as which standardized technology can best be used to do so.

Lastly, this section continues the discussion of how to
describe semantics and a generic (semantically neutral) API
to exchange data.  Specifically, several
deployment strategies for dealing with managing heterogeneous semantics are
discussed including:

if !supportLists?·      
endif?Integration of complementary largely
non-overlapping semantic sets. In this case, one model gets extended with
another by adding links or maps that describe how to extend one with another,
using self-description of objects within the models to help automate this
mapping.

if !supportLists?·      
endif?Integration of overlapping semantic sets into
another where the first is assimilated into the second by replacing terms in
the first with terms in the second.

if !supportLists?·      
endif?Integration of overlapping semantic sets where
we don’t want to assimilate one into the other, but instead need to describe
the relationship between them and keep each model and their differences
explicit.  In this case, the links
between models describe differences and similarities.

This section briefly describes how these strategies might
be employed when deploying an IntelliGrid Architecture based architecture.
