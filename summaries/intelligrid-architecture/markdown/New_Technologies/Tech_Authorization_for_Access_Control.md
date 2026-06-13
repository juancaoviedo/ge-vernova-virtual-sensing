# Auth for Access Control

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Authorization_for_Access_Control.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

## Authorization for Access Control

The
**Authorization for Access Control** security service is concerned with
implementing policy-based
access control decisions, with the assumption that the appropriate
[Identity Establishment](Tech_Identity_Establishment_Service.htm) has
taken place. The
service consumes as input a credential/identity token which embodies the
identity of a service requestor and/or for the resource that the service
requestor requests. Based upon the credentials and trust factors and policy,
the resource will determine if authenticating the peer is to be performed. Once
authenticated, the peers may then process each other’s requests (as authorized), based upon
appropriate policy enforcement (e.g. privilege or role based access).

It
is expected that the hosting environment for Open Grid Services
Architecture (OGSA)-compliant services will
provide access control functions, and it is appropriate to further expose an
abstract authorization service depending on the granularity of the access
control policy that is being enforced. Allow for controlling access to OGSA
services based on authorization policies (i.e., who can access a service, under
what conditions) attached to each service. Also allow for service requestors to
specify invocation policies (i.e. who does the client trust to provide the
requested service). Authorization should accommodate various access control
models and implementation.

### Factors for Access Control Authentication

Authentication
for Access Control relies upon several basic factors being achieved:

·    That the identity of the entity/person is established.
The [Identity Establishment Service](Tech_Identity_Establishment_Service.htm) performs this function.

* That there is an acceptable level of Trust
  established that the entity is who they claim to be.
  The [Trust Establishment](Tech_Trust_Establishment_Service.htm) and
  [Quality of Identity](Tech_Quality_of_Identity_Service.htm) services are involved in
  providing this functionality.
* That there is a policy and management process that
  has been used to determine which entity has the privileges to access
  certain assets, resources, or information.
  The [Policy](Tech_Security_Policies.htm) and **Security
  Management Interface (SMI)-**related services provide this functionality.
* That there is a
  mechanism to enforce the mandates of the policy and management process.
  The **Authorization for Access Control** service is responsible for providing
  this functionality.

### Categories of Access Control

There
are generally three (3) categories of Access Control that need to be addressed
within a security domain: **[Physical Assets](Tech_Authorization_for_Access_Control.htm#Physical_Access_to_Assets);**
**[Computational Resources](Tech_Authorization_for_Access_Control.htm#Computational_Resource);** and **[Information](Tech_Authorization_for_Access_Control.htm#Informational_Technology_Assessment/Specification)**.

#### Physical Access to Assets

The
basic premise of physical access control is intended to allow authorized
individuals to be able to enter the areas for which they have clearance to
enter and to make it difficult for un-authorized individuals to enter. Based on
the Security Domain definition, physical access control is not an inter-domain
issue. However, there are some desirable aspects to any physical access control
system:

·      
The system should be capable of providing an audit trail of who actually
entered a specific area.

·      
The system should be capable of detecting intrusion attempts of an
un-authorized individual to enter an area.

·      
There are issues in regards to the quickness/speed of enunciating
intrusion or intrusion attempts. The speed at which this enunciation can occur
is a key metric in regards to the ability of a SMI to respond to the intrusion.

·      
The system should be robust enough that intrusions can be proven in an
authoritative manner so that legal prosecution has a probability of success.

·      
Properly implemented, a physical access control system can provide
on-site personnel listings/locations in the event of an emergency event.

·      
The choice of access control mechanisms should allow for multi-factor
authentication and ease of management in the event that revocation of access
privileges is required (e.g. User and Group Management issues). In order to
accomplish this service function, there must be a security token that is used
to enable a final access mechanism (e.g. a lock).

·      
A policy/strategy needs to address assets that are not capable of being
physically secured. For these types of resources, informational and resource
security measures will need to be enhanced. Examples of such an assets are
wireless networks and wireless technologies.

·      
A residual risk analysis and recovery plan needs to be developed, as
part of the Policy service, to address resources for which no type of adequate
security can be provided. Examples of such physical resources are transmission
lines and telephone lines.

In
order to provide physical access control, there needs to have a physical barrier
that separates critical or controlled areas from un-controlled areas. These
barriers would typically be fences, walls, or doors that have locks or security
guards so that proper access privileges can be determined.

##### Physical Access Technologies/Specifications

There
are no relevant specifications regarding Physical Authorization for Access
Control. However, there are typical strategies that are worthy of some
discussion (see Table 2).

**Table 2: Typical Physical Access
Control Strategies**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Security Strategy** | **Authentication Factor** | | | **Biometric** | **Comments** |
|  | **Single** | **Two** | **Three** |  |  |
| Security Guard Only |  |  |  |  | Needs to be augmented in order to provide audit capability, at a minimum. |
| Key/Lock | X |  |  |  | Adequate token that can be properly managed but can easily be duplicated that would facilitate un-authorized access. |
| Combination Lock | X |  |  |  | Typically adequate, but can be stolen through observation. |
| Sign-in sheet |  |  |  |  | Should not be used solely. At a minimum, verification of the person’s identity signing-in must be facilitated. |
| Sign-in sheet with Photo-ID | X |  |  | X | Requires a security guard. |
| Sign-in sheet with confirmed clearance to enter. | X |  |  | X | Typically used for guest entry. In order to be biometric, the confirming party must visually recognize and clear the entity requesting entry. |
| Video Surveillance |  |  |  |  | Should be used as audit/security for major/sensitive entrances. Provides a good mechanism for legal prosecution for remote sites. |
| Photo-ID with no sign-in sheet |  |  |  | X | Should not be used since no audit trail is possible. |
| Smart Card | X |  |  |  | It is assumed that SMART Cards would be used in conjunction with computerized locks so that a computerized audit trail can be generated. However, it is typical that only ½ of the audit trail is generated since the cards are typically not required to exit the room. |
| Smart Card with Photo ID Card | X |  |  | X | Has the benefit of the Smart Card, but can also double as a Personal ID. This is a recommended strategy. |
| Smart ID Card used to enable Combination Lock |  | X |  |  | This is the best mechanism for restricting access to sensitive areas. |
| Biometric Combination Lock |  | X |  | X | This is the best mechanism for restricting access to sensitive areas. |

Another
method of analyzing the same strategies would be:

Table 3: Physical Security Strategies vs. Security
Services Provided

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Security Strategy** | **Security Service Provided** | | | **Comment** |
|  | **Identity** | **Trust** | **Access Control** |  |
| Security Guard Only | ? |  |  | It is questionable that a security guard only strategy could provide adequate identification establishment. |
| Key/Lock |  | x | x | Provides a mechanism to establish a relative level of Trust (due to the person having the key) and provides appropriate access control. |
| Combination Lock |  | x | x | Provides a mechanism to establish a relative level of Trust (due to the person having the combination) and provides appropriate access control. |
| Sign-in sheet |  |  |  | Without actual identity establishment, no security can be provided. |
| Sign-in sheet with Photo-ID | x |  |  |  |
| Sign-in sheet with confirmed clearance to enter. | ? | x |  | Only provides Identity Establishment if a photo-ID is used in conjunction with the sign-in sheet. |
| Video Surveillance |  |  |  | Provides audit and repudiation capability only. |
| Photo-ID with no sign-in sheet | x |  |  |  |
| Smart Card |  | x | x | A Smart-Card only does not provide Identity Establishment. Identity Establishment is a required function/service for Access Control. Therefore, the use of Smart-Cards only should not be considered. |
| Smart Card with Photo ID Card | x | x | x | This is a recommended strategy for non-critical area access. |
| Smart ID Card used to enable Combination Lock | x | x | x | This is one of the recommended deployment strategies for critical areas. |
| Biometric Combination Lock | x | x | x | This is one of the recommended deployment strategies for critical areas. |

##### Technological Assessment

The
suggested technology to be used to provide Access Control to critical areas is
the use of multi-factor access control. It is further suggested that SMART-CARD[[2]](Tech_Authorization_for_Access_Control.htm#_ftn2)s that double as personal identification
cards be utilized to enable combination locks. Furthermore, it is also
recommended that such technology deployment be used in conjunction with an
electronic audit mechanism.

#### **Computational Resource**

The
basic premise of computational access control is intended to allow authorized
individuals to be able to access programs for which they have clearance to make
use of. Based on the Security Domain definition, computational access control
is both an inter-domain and intra-domain issue. However, the enforcement of
computation access control is purely an intra-domain issue. For inter-domain
access control the [Identity Mapping](Tech_Identity_Mapping_Service.htm) service (and its required sub-functions)
actually provides the mapping from an external identity to an identity
recognized and managed intra-domain.

·      
The system should be capable of providing an **audit trail** of who accessed
a given computational resource.

·      
The system should be capable of **detecting intrusion** attempts of an
un-authorized individual to a computational resource.

·      
There are issues in regards to the quickness/speed of enunciating
intrusion or intrusion attempts. The speed at which this enunciation can occur
is a key metric in regards to the ability of a SMI to respond to the intrusion.

·      
The system should be robust enough that **intrusions can be proven** in an
authoritative manner so that legal prosecution has a probability of success.

·      
The choice of **access control** mechanisms should allow for multi-factor
authentication and ease of management in the event that revocation of access
privileges is required (e.g. User and Group Management issues). In order to
accomplish this service function, there must be a security token that is used
to enable a final access mechanism (e.g. a lock).

·      
A **policy/strategy** needs to address assets that are not capable of being
secured. For those types of resources, the level of trust should be considered
low.

The
aforementioned issues need to be addressed for a variety of computational
resources: Operating Systems (OSs); programs within a OS that has access
control; programs within an environment where there is no OS access control
required to access the program (e.g. an RTU); and wireless networks.

##### Operating System and Computer Programs

Operating
System (OS) access control requires
[Identity Establishment](Tech_Identity_Establishment_Service.htm) (see the identity
establishment service). The access control service, for OSs, determines which
programs/computational resources the Identified User/Program has privileges to
execute/access.

The
major issues regarding this access are:

·      
To provide an appropriate policy and SMI so that such access is granular
enough to provide enough audit capability.

·      
Managing the configuration in a distributed environment.

·      
The level of trust that can be associated with the OS to perform its
tasks in a secure manner (see ACC-01). Several issues are mitigated if a
“Trusted/Secure” OS is used. However, the use of such OSs in IntelliGrid Architecture
environment is not viable in a majority of the cases,
therefore this section will address non-Trusted OS issues.

For
all OSs, the issue of access control relates to properly managed Access Control
Lists that are typically OS specific. However, care needs to be taken to ensure
that if Role Based Access is used, that an audit mechanism is provided in order
to reference back to the actual individual/entity that has accessed the OS.
Additionally, the information in ACC-02 should be considered when developing
the OS access framework in a distributed environment.

##### **Computer Programs**

In
the cases where an OS does not provide Access Control to the programmatic
level, programs themselves need to provide this capability. This is
particularly true for electronic protocol processes that bypass OS
authentication on the destination of the communication path. In such a situation,
it is incumbent upon the destination program/process to apply the appropriate
security mechanisms.

In
IntelliGrid Architecture there will be computational and communication technologies integrated
of various capabilities. These various capabilities (e.g. process/memory/storage
capacity or bandwidth limitations) require that different technological
solutions be available. However the functional objectives remain consistent:
provide a manageable environment and to provide enough granularity to provide a
capability for non-repudiation.

##### Communication Networks

There
are several types of communication networks that need to be addressed:

·     **Inter-Domain networks** where the physical network are exposed.
The major issue with these types of physical networks is that both domains do
not manage the network segments that provide the inter-domain interfaces. These
segments are typically provided by a third party and therefore constitute a
third Security Domain. Thus it is important that appropriate access control be
provided at the security domain interface points.

·      **Intra-Domain networks** where the physical network is within a Security
Domain.
For intra-domain networks, some Security Domains may desire to control the
computers/computer users that actually have access to the network. Once a
resource is within a Security Domain, there is no reliable mechanism to prevent
physical access to the network. Thus it becomes incumbent upon the SMI to
detect that a non-authorized access to the network has been attempted or been
successful. Additionally, it may be possible to make it more difficult for a
non-authorized resource to make use of the network through proper management of
the network addresses so that no address is assigned to the intruding resource.

·      **Wireless LAN/WAN Networks** whose transmissions can be easily monitored
and spoofed.
This type of network represents an intra-domain network that REQUIRES
management in regards to who can actually make use of the network. The issue
can be easily demonstrated by looking at the prevalence of WI-FI.
In the WI-FI case, hot-spots (e.g. Starbucks, airports) could not recoup their
investment without a challenge response mechanism to ensure that only
authorized (e.g. paid subscription entities) are actually assigned an address
that facilitates real communications.
Such mechanisms may prevent off-segment communications, but will not prevent
denial-of-service attacks (see ACC-03). Thus such systems need to be augmented
beyond challenge-response.

·      **Dial-up Networks**: There is a well-documented history in regards to the
vulnerabilities associated with dial-up networks. These types of networks are
inherently susceptible to denial-of-service attacks and have poor identity
establishment/access control at a physical/network level. This is especially
true for equipment that is deployed in the Transmission and Distribution
environment.

Table 4: References regarding Computational Resource
Access Control

|  |  |
| --- | --- |
| ACC-01 | Stephen Radford - Trusted Operating Systems and Their Evolving Non-Trusted Counterparts , January 23, 2003. SANS Institute |
| ACC-02 | **Fine-Grain Authorization for Resource Management in the Grid Environment**. K. Keahey, V. Welch. *Proceedings of Grid2002 Workshop*,  2002. |
| ACC-03 | AA-2004.02 -- Denial of Service Vulnerability in IEEE 802.11 Wireless Devices (AusCERT) |

##### Technological Assessment Specifications/Standards

Table
5 represents a set of specifications and/or standards that are relevant to the
understanding of the issues regarding access control for computational
resources. Those specifications marked as Recommended or Recommended Reading
should be considered as materials that should be considered prior to actually
implementing the access control service.

Table 5: Relevant Computational
Resource Access Control Standards/Specifications

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| ANSI INCITS 359-2004 | Role Based Access Control | Recommended |
| RFC 2244 | ACAP -- Application Configuration Access Protocol | Recommended |
| RFC 1013 | X Window System Protocol, version 11: Alpha update April 1987 |  |
| RFC 2086 | IMAP4 ACL extension |  |
| RFC 2820 | Access Control Requirements for LDAP | Recommended for Directory Services |
| RFC 1305 | Network Time Protocol (Version 3) Specification, Implementation | Recommended for NTP |
| RFC 2753 | A Framework for Policy-based Admission Control |  |
| RFC 2744 | Generic Security Service API Version 2 : C-bindings |  |
| RFC 2356 | Sun's SKIP Firewall Traversal for Mobile IP |  |
| RFC 1004 | Distributed-protocol authentication scheme |  |
| RFC 2865 | Remote Authentication Dial In User Service (RADIUS) | Recommended for Dial-up Lines |
| RFC 2869 | http://www.armware.dk/RFC/rfc/rfc2869.htmlRADIUS Extensions |  |
| RFC 1221 | Host Access Protocol (HAP) Specification - Version 2 |  |
| ISO/IEC 10164-9:1995 | Information technology -- Open Systems Interconnection -- Systems Management: Objects and attributes for access control |  |
| ISO/IEC 10181-3:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Access control framework | Recommended |
| WebDAV | Access Control Extensions to WebDAV |  |

##### Technological Assessment and Recommendations

###### OS Recommendations

It
is recommended that Trusted OSs be used whenever possible. Additionally, ANSI
INCITS 359-2004 us suggested as an implementation
strategy for Role Based Access.

###### Computer Programs

It
is recommended that the appropriate access control list mechanisms be used in
regards to the applications where such technologies have been noted in Table 5.
Thus, make use of:

·      
RFC 1013 for X Windows applications.

·      
RFC 2086 for IMAP based applications.

·      
RFC 2820 for LDAP.

·      
RFC 1305 in regards to NTP.

Otherwise,
it is suggested to follow the general policies/procedures set forth in ISO/IEC
10181-3:1996 and make use of any application specific access control strategies
set forth.

###### Communication Networks and Protocols

In
general it is recommended that all computational resources, when possible, be
assigned dynamic addresses that allow off-segment communications. There is no
single technology that can accomplish this, but a challenge response mechanism
is suggested as part of the implementation strategy.

For
those resources that require fixed addresses (e.g. servers of data), it is
suggested that network based access control lists be implement in order to
prevent un-authorized off-segment communication.

There
is a substantial amount of work occurring within IEC TC57 WG15 to secure
several of the communication protocols that are intended to be used by IntelliGrid Architecture.
It is suggested that these be adopted and deployed as rapidly as is feasible.

Wireless
networks are extremely susceptible to denial-of-service attacks. In order to
mitigate this issue, AES encryption on wireless links is suggested.

Dial-up
access control should be implemented through the use of RAIDUS (RFC 2865 and
RFC 2869) when this is feasible. Such access should be deployed so that there
is an additional access control list (e.g. a Firewall or router based ACL) that
provides additional security. Thus, when possible, it is suggested that NO
direct dial-up access be given to a computer or a computer process. However,
this is not always feasible in the Transmission and Distribution systems deployed
within IntelliGrid Architecture environment (e.g. RTUs and field devices). For this class of
resource, or resources with similar constraints, it is suggested that the
devices be implemented in such a manner that denial-of-service is mitigated:

* Dial-up connections should be constructed such there is an inactivity
  time-out to prevent a connect/hold the port open denial of service attack.

  * Once the port is connected, there should be a time-out on the connection
    that requires valid communication protocol/application level information flow.
  * It is not suggested to implement a dial-back strategy since these become
    difficult to manage and maintain and does not allow the type of environment
    that IntelliGrid Architecture is attempting to promote.

#### Informational Technology Assessment/Specification

Information
access control is extremely similar to a combination of OS and program access.
However, it is up to each individual program to provide the appropriate level
of access control.

ACC-04
represents a very simple summary of the granularity required in access control
for most databases: Control over Reading; Control over Changing; and Control over
Storing. Additionally, for Object Oriented access, there may need to be an
ability to prevent an entity from discovering that an Object Exists (optional).

Table 6: References relating to Access Control for
Informational Resources

|  |  |
| --- | --- |
| ACC-04 | Access Control on the Semantic Web (wc3.org)  Available from: http://www.w3.org/2002/03/semweb/access-control |
