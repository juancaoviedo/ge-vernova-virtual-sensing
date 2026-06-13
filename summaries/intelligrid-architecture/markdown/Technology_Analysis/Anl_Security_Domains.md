# Security Domains

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Domains.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security and Security Domains

## Introduction to Security Domains

There are many potential methods through which to
facilitate the discussion of security.  Many desire to discuss security on
an Enterprise basis.  However, there is an issue regarding the definition
and boundaries of the “Enterprise” and those boundaries are always changing.
Thus developing “Enterprise” level security constructs/policies becomes
difficult and un-productive, as they are difficult to manage.

Another method is to perform concrete analysis of
particular systems and communication technologies/topologies.  It is often
difficult to discuss a security models in concrete terms since the technology
used in deployments typically becomes the lowest common denominator that is
discussed.  Such technology based security models tend to be difficult to
scale and understand from a enterprise system perspective.  Likewise, such
concrete models are difficult to extend/scale to address systemic security.

There is another, although less used, concept.  That
is the concept discussing security in regards to atomic “security domains” that
represent security boundaries.

“The concept of a security domain that is introduced in
this paper is not new. Many computer security practitioners have been (either
explicitly or implicitly) using the ideas presented here for many years in
protecting networks.”[1] For instance, **NERC 1200 and 1300 security
requirements** use the term "**Electronic Perimeters**" for Security
Domains.

## Security Domain Definition

“Telecommunications and Network Security domain
encompasses the structures, transmission, methods, transport formats and
security measures used to provide integrity, availability, authentication, and
confidentiality for transmission over private and public communications
networks and media.” [2] Additionally, “In this paper, the term Security Domain is used to
describe a network of computer systems that share a specified security level
through a common element.”[1].

if !vml?![](Anl_Security_Domains_files/image002.gif)endif?

Figure 1:
Representation of Security Domain Concept[[2]](Anl_Security_Domains.htm#_ftn2)

A
Security Domain (SD) represents a set of resources (e.g. network, computational, and physical) that is
governed/secured and managed through a consistent set of security policies and
processes.  Thus each Security Domain is responsible for its own general
security process (e.g. Assessment, Policy, Deployment, Monitoring, and
Training). In addition to the general security process, a Security
Domain provides a well-known set of security functions that are used to secure
transactions and information within that domain.

## Security Management of Security Domains

Security Management is defined as:  “In network management,
the set of functions (a) that
protects telecommunications networks and systems from unauthorized access by persons, acts, or
influences and (b) that includes many subfunctions,
such as creating, deleting, and controlling security services and
mechanisms; distributing security-relevant information; reporting
security-relevant events; controlling the distribution of cryptographic keying
material; and authorizing subscriber
access, rights, and privileges.”[9]  Based upon
this definition, it is the Security Management of an SD that is responsible for
the risk assessment, developing security policies and strategies, and
implementing those policies and strategies.

## Security Functions for Security Domains

A successful Security Domain will define
and implement the following security functions:

* **Access
  Control**: “The prevention of unauthorized use of a resource, including the
  prevention of use of a resource in an unauthorized manner.”[7].
  There are generally three (3) categories of Access Control that need to be
  addressed within a SD: Physical; Resource; and Information.
* **Trust**: “In cryptology
  and cryptosystems, that characteristic allowing one entity to assume that a
  second entity will behave exactly as the first entity expects. Note: Trust may
  apply only for some specific function. The critical role of trust in the authentication
  framework is to describe the relationship between an authenticating entity and
  a certification
  authority; an authenticating entity must be certain that it can trust the
  certification authority to create only valid and reliable certificates. [After
  X.509]”[9]
* **Authentication**.  Trust is established via Authentication. There are two methods
  of authentication that are prevalent in today’s electronic systems: **Role Based
  Authentication** and **Individual Authentication.**
* **Confidentiality**: “The property that information is not made available of
  disclosed to unauthorized individuals, entities, or process.” [7]. There are  two (2) categories of Confidentiality that need to be addressed
  within a SD: **Protection** **from un-intentional disclosure** and **overall protection
  of information**.
* **Integrity**: “The principle that keeps information from being modified or
  otherwise corrupted either maliciously or accidentally.”[8]
* **Security Policy**: “The set of rules and practices that regulate how an
  organization manages, protects, and distributes sensitive equipment and
  information.”[8]
* **Security Management Infrastructure (SMI)**: “(I) System elements and activities
  that support security policy by monitoring and controlling security services
  and mechanisms distributing security information and reporting security
  events.”[10]
* **Training** (as described in the general security process).

### Relationship of Security Processes to Security Functions within a Security Domain

Table 1 shows that the Policy security function is a
function that is required in ALL aspects of the security process. 
Additionally, the table also shows that an appropriate Security Management
Infrastructure needs to be deployed in order to monitor and perform
re-assessment of the security system within a Security Domain.

**Table 1: Relating Security Processes to Functions and
Services**

| **General Security Process Name** | **Secu****rity Function Name** |
| --- | --- |
| Assessment | Policy  SMI |
| Deployment | Trust  Access Control  Confidentiality  Integrity  Policy  SMI |
| Monitoring | SMI  Policy |
| Policy | Policy |
| Training | Policy  Training |

### Relationship of Security Functions to Security Services

Going the next step, in order to actually implement the security functions
within a Security Domain, several [Security Services](Anl_Security_Services.htm) have been identified. 
Table 2 shows the relationships of the Functions to the Security Services that
would be used to actually implement the security function.

**Table 2: Relating Security Functions to Security
Services**

| **Security Function Name** | **Service Name** |
| --- | --- |
| Access Control | Authorization for Access Control  - All Trust related Services |
| Confidentiality | Confidentiality  Path Routing and QOS  Firewall Transversal |
| Integrity | Information Integrity  Profile  Protocol Mapping |
| Policy | Policy |
| Security Management Infrastructure (SMI) | Audit  User and Group Mngt.  Security Assurance  Non-Repudiation  Security Assurance  Policy  -- Management of all services |
| Trust | Identity Establishment  Identity Mapping  Quality of Identity  Credential Conversion  Credential Renewal  Delegation  Privacy  Single Sign-on  Trust Establishment |

### Interrelationships between Security Services

Further, it is notable that there are inter-relationships
between the services themselves. As an example, Table 3 indicates that in order
to provide the Identity Mapping Service the Credential Conversion service is
needed.

Table 3: Primary Services and the additional Security
Services required

| **Service** | **Requ****ired Services** |
| --- | --- |
| Audit | Policy  Security Assurance |
| Authorization for Access Control | Identity Establishment  Information Integrity  Setting and Verifying User   Trust Establishment  Non-Repudiation  Quality of Identity |
| Confidentiality | Identity Establishment  Authorization for Access Control.  Privacy  Trust Establishment  Path Routing and QOS |
| Delegation | Identity Mapping |
| Identity Establishment | Credential Renewal  Information Integrity  Policy  User and Group Management  Audit  Policy |
| Identity Mapping | Identity Establishment  Credential Conversion  Non-Repudiation  Quality of Identity |
| Information Integrity |  |
| Inter-Domain Security | Identity Mapping  Security Protocol Mapping  Security Against Denial of Service  Trust Establishment  Security Service Availability  Path Routing and QOS |
| Non-Repudiation | Audit  Security Assurance |
| Policy |  |
| Profile | Audit  Identity Mapping |

### Security Services Needed for Intra- and Inter-Domain Security

The combination of Table 1 through Table 3 should allow
users to determine what security services need to be implemented in order to
achieve a specific Security Process.  However, there are different services
required for inter-domain and intra-domain exchanges. These services are shown
in Table 4.

Table 4: Services needed for Intra/Inter Domain Security: m
= mandatory; o = optional

| **Security Service** | **Intra-Domain** | **Inter-Domain** | **Comments** |
| --- | --- | --- | --- |
| Audit | m | m |  |
| Authorization for Access Control | m | m |  |
| Confidentiality | o | m |  |
| Credential Conversion | o | m |  |
| Credential Renewal | m | m |  |
| Delegation | o | m |  |
| Firewall Transversal | o | m |  |
| Identity Establishment | m | m |  |
| Identity Mapping | o | m |  |
| Information Integrity | m | m |  |
| Inter-Domain Security | Not Applicable | m |  |
| Non-Repudiation | m | m |  |
| Path Routing and QOS | o | o |  |
| Policy | m | m |  |
| Privacy | o | o |  |
| Profile | m | m |  |
| Quality of Identity | See comment | m | In order to provide this service for inter-domain, it must be available for intra-domain applications to make use of. |
| Security Against Denial of Service | o | m |  |
| Security Assurance | m | m |  |
| Security Protocol Mapping | o | m |  |
| Security Service Availability Discovery | m | m |  |
| Setting and Verifying User Authorization | m | m |  |
| Single Sign-On | m | Not Applicable |  |
| Trust Establishment | m | m |  |
| User and Group Management | m | m |  |
