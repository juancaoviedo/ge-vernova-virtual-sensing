# Common Security Services and Technologies/Standards

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Services.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security Services and Associated Technologies/Standards

This section discusses the common security services and the particular technologies/standards that
could be useful in actually implementing the common service. These security
services are:

|  |  |
| --- | --- |
| * [Audit Common Service](Anl_Security_Services.htm#Audit_Common_Service) * [Authorization   Service for   Access Control](Anl_Security_Services.htm#Authorization_for_Access_Control) * [Confidentiality Service](Anl_Security_Services.htm#Confidentiality) * [Credential Conversion Service](Anl_Security_Services.htm#Credential_Conversion) * [Credential Renewal Service](Anl_Security_Services.htm#Credential_Renewal_Service) * [Delegation Service](Anl_Security_Services.htm#Delegation_Service) * [Firewall Traversal Service](Anl_Security_Services.htm#Firewall_Traversal) * [Identity Establishment Service](Anl_Security_Services.htm#Identity_Establishment_Service) * [Identity Mapping Service](Anl_Security_Services.htm#Identity_Mapping_Service) * [Information Integrity Service](Anl_Security_Services.htm#Information_Integrity_Service) * [Inter-Domain   Security Service](Anl_Security_Services.htm#Inter-Domain_Security) * [Non-repudiation Service](Anl_Security_Services.htm#Non-repudiation) | * [Path   Routing and QOS Service](Anl_Security_Services.htm#Path_Routing_and_QOS_Service) * [Security Policy Service](Anl_Security_Services.htm#Policy) * [Policy   Exchange Service](Anl_Security_Services.htm#Policy_Exchange) * [Privacy   Service](Anl_Security_Services.htm#Privacy_Service) * [Profile   Service (User Profile Service)](Anl_Security_Services.htm#Profile_Service_(User_Profile_Service)) * [Quality   of Identity Service](Anl_Security_Services.htm#Quality_of_Identity_Service) * [Security   against Denial-of-Service](Anl_Security_Services.htm#Security_against_Denial-of-Service) * [Security Assurance Management Service](Anl_Security_Services.htm#Security_Assurance_Management) * [Security Protocol Mapping Service](Anl_Security_Services.htm#Security_Protocol_Mapping) * [Security Service Availability Discovery   Service](Anl_Security_Services.htm#Security_Service_Availability_Discovery_Service) * [Single Sign on Service](Anl_Security_Services.htm#Single_Sign_on_Service) * [Trust Establishment Service](Anl_Security_Services.htm#Trust_Establishment_Service) |

## Audit Common Service

An audit service is responsible for producing records
known as audit records which contain audit record
fields, which track security relevant events. The resulting audit records may
be reduced and examined in order to address several key aspects of security
within a security domain:

·      Audit records and audit trails can be used to determine if a
pre-scripted security policy is being enforced.

·      Auditing and subsequently reduction tooling are used by the security
administrators within a Security Domain to determine the Security Domain’s
adherence to the stated access control and authentication policies.

·      Audit records that support the recording of usage data, secure storage
of that data, analysis of that data allows Security Domains to detect fraud and
intrusion detection.

 A robust auditing mechanism enables a
Non-repudiation service through the creation of an audit trail.

Key definitions:

**audit: 1.** To conduct an
independent review and examination of [system](http://www.atis.org/tg2k/_system.html) records and activities
in order to test the adequacy and effectiveness of [data security](http://www.atis.org/tg2k/_data_security.html) and [data integrity](http://www.atis.org/tg2k/_data_integrity.html)
procedures, to ensure compliance with established policy and operational
procedures, and to recommend any necessary changes. **2.** Independent
review and examination of records and activities to assess the adequacy of
system controls, to ensure compliance with established policies and operational
procedures, and to recommend necessary changes in controls, policies, or
procedures. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

**audit record field:** A [field](http://www.atis.org/tg2k/_field.html) containing [information](http://www.atis.org/tg2k/_information.html) regarding all
entities in a transaction, and indicators of the types of processing performed
by those entities. [After X9.17/95]

**audit trail: 1.** A record
of both completed and attempted accesses and [service](http://www.atis.org/tg2k/_service.html). **2.** [Data](http://www.atis.org/tg2k/_data.html) in the form of a logical
path linking a [sequence](http://www.atis.org/tg2k/_sequence.html)
of events, used to trace the transactions that have affected the contents of a
record. **3.** [In [INFOSEC](http://www.atis.org/tg2k/_infosec.html),
a] chronological record of [system](http://www.atis.org/tg2k/_system.html)
activities to enable the reconstruction and examination of the sequence of
events and/or changes in an event. Note: [Audit](http://www.atis.org/tg2k/_audit.html) trail may apply to [information](http://www.atis.org/tg2k/_information.html) in an [information system](http://www.atis.org/tg2k/_information_system.html)
(IS), to [message](http://www.atis.org/tg2k/_message.html) [routing](http://www.atis.org/tg2k/_routing.html) in a [communications
system](http://www.atis.org/tg2k/_communications_system.html), or to the [transfer](http://www.atis.org/tg2k/_transfer.html)
of [COMSEC material](http://www.atis.org/tg2k/_comsec_material.html).
[INFOSEC-99]

There are several well-understood audit issues that must
be taken into account when implementing the audit trail. The audit trails need
to be analyzed to determine vulnerabilities, establish accountability, assess damage and recover the system. Manual analysis of audit
trails though cumbersome is often resorted to because of the difficulty to
construct queries to extract complex information from the audit logs. There are
many tools that help in browsing the audits. The major obstacle in developing
effective audit analysis tools is the copious amounts of data that logging
mechanisms generate.

There are a number of significant issues in creating an audit
trail from various electronic audit sources:

·      **A coherent
and well-defined service to query an audit provider for audit records**.
There needs to be mechanism through which queries for audit records can be
issued.  Although multiple protocols could carry such a request, such a deployment
strategy would require profile-mapping capabilities.  While to date, there
is no security specific standards for such a service, a general purpose log
query service could be used.

·      **A common
and self-describing format for the audit records that can account for
specializations**.
The capability to query for audit records allows the start of the information
transfer.  However, in order to re-construct an Audit Trail from multiple
audit record sources, there needs to be a common Audit Record format.  The
format should be self-describing with standardized contents, but allow for
additional information to be conveyed.  Some of the standardized fields
might be:  
  
<AuditRecord>, <RecordType>,<AuthBy>, <SubjectUid>,<TimeStamp>[[3]](Anl_Security_Services.htm#_ftn3) , etc…  However, there is no
internationally recognized specification for such. 
What is important here is that the record structure be self describing so
that a general purpose log query service could present log data intelligently.

·      **A well-defined
mechanism to detect tampering with the transferred audit records**.
One of the major purposes for audits/audit trails/audit records is provide an
authoritative mechanism to perform non-repudiation.  One of the key issues
with providing non-repudiation in an authoritative manner is to prove that the
audit trail/record has not been tampered with.
Although there is no recognized standard for such purposes, there is a
recognized approach to the problem.  This is to digitally sign the audit
record or to provide a non-repeating serial number for the record.  The
actual mechanics of the digital signature and how to convey the signature would
be issues for the common audit record format specification.

·      **The ability
to correlate audit records from multiple audit sources**.
It is conceivable that different Security Domains would be in different time
zones.  In order to create an inter-domain audit trail, it is necessary to
be able to correlate the times of the various audit records. 
Thus all audit records should have a timestamp whose reference time is UTC.
However, the timestamp itself may not have the accuracy to differentiate
between several audit records that occur within the same timestamp
period.  Thus, it is also a requirement that an audit record serial number
be provided within each audit record.  The combination of the timestamp
and serial number would need to be unique. Problems with correlation can also
occur if the timestamp accuracies of the audit records are not the same. 
Thus appropriate
accuracy and time synchronization skew should be specified for each
implementation.

·      **Determination
of where to place auditing capability**.
Many security infrastructures/policies have difficulty identifying the types of
applications that need an audit trail.  The use of the definition of IntelliGrid Architecture security services allows the following base recommendations to be made.
Audit records should be generated whenever/wherever the following security
services are invoked: Authorization for Access Control; Credential Conversion;
Credential Renewal; Delegation; Firewall Transversal; Identity Establishment;
Identity Mapping; Profile; Security Protocol Mapping; Setting and Verifying
User Authorization; Single Sign-On; Trust Establishment; User and Group Management.

·      **Determination
of the minimum-maximum audit record time availability**.  There is a need to
determine/specify through policy a minimum amount of time that an audit record
must be maintained within the audit trail system.  In IntelliGrid Architecture
environment, this time would need to be specified so that non-repudiation for
an appropriate period of time can be provided.

·      **The issues
of privacy and legal relevance needs to be addressed**.
There are issues regarding the privacy of emails and text messages. 
However, during the 9/11 terrorism hearings, email evidence was allowed to be
submitted.  However, in the Kobe Bryant trial, the subpoena for text
messages (e.g. via cell phone) is being fought on the basis of privacy. 
Until recently, there have been no publicly available authoritative documents
describing best practices in this area.  However, the Federal Government
(AUDT-01) and the American Bar Association (AUDT-02) have published some
initial work that should be reviewed to determine if the recommendations are
viable within a given security domain.

#### Technologies/Specifications

Table 6 represents a set of specifications and/or standards that are relevant to the understanding of the issues
regarding the audit service. Those specifications marked as Recommended or
Recommended Reading should be considered as materials that should be considered
prior to actually implementing the audit service.

Table 5: Relevant References in regards to Audit processes

|  |  |
| --- | --- |
| AUDT-01 | US Department of Justice:  LEGAL CONSIDERATIONS IN DESIGNING AND IMPLEMENTING ELECTRONIC PROCESSES: A GUIDE FOR FEDERAL AGENCIES  Available from: http://www.cybercrime.gov/eprocess.htm |
| AUDT-02 | Joint Administrative Office/Department of Justice Working Group on Electronic Technology in the Criminal Justice System: Working Group Report.  Available from: http://www.abanet.org/lpm/lpt/docs/ao-doj\_committee\_electronic\_technology\_wg\_report.pdf |

Table 6: Relevant Standards/Specifications relevant to the
Audit Service

| **Identification Num****ber** | **Name** | **Comment** |
| --- | --- | --- |
| [ISO/IEC 10164-8:1993](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18165&ICS1=35&ICS2=100&ICS3=70) | Information technology -- Open Systems Interconnection -- Systems Management: Security audit trail function | Recommended |
| [ISO/IEC 10181-7:1996](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=18200&ICS1=35&ICS2=100&ICS3=1) | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Security audit and alarms framework |  |
| [ISO/IEC 18014-1:2002](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34386&ICS1=35&ICS2=40&ICS3=) | Information technology -- Security techniques -- Time-stamping services -- Part 1: Framework | Recommended Reading |
| [ISO/IEC 18014-2:2002](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34387&ICS1=35&ICS2=40&ICS3=) | Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens |  |
| [ISO/IEC 18014-3:2004](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=34388&ICS1=35&ICS2=40&ICS3=) | Information technology -- Security techniques -- Time-stamping services -- Part 3: Mechanisms producing linked tokens |  |
| 21 CFR Part 11 | Guidance for Industry Part 11, Electronic Records; Electronic Signatures – Scope and Application | Recommended Reading |

#### Technological Assessment

An inspection of Table 6 shows that there are no
technology specific specifications/standards that
address the issues/problems previously discussed in this section.

## Authorization Service for Access Control

The Authorization Service for Access Control is concerned with resolving a policy based access control decision based
upon appropriate Identity Establishment. The service consumes as input a
credential/identity token which embodies the identity of a service requestor
and/or for the resource that the service requestor requests. Based upon the
credentials and trust factors and policy, the resource will determine if
authenticating the peer is to be performed.  Once authenticated, the peers
may process each other’s requests based upon appropriate policy enforcement (e.g.
privilege or role based access).

It is expected that IntelliGrid Architecture environment will provide
access control functions, and it is appropriate to further expose an abstract
authorization service depending on the granularity of the access control policy
that is being enforced. Allow for controlling access to IntelliGrid Architecture services and
resources will be based on authorization policies (i.e., who can access a
service, under what conditions) attached to each service. Also allow for
service requestors to specify invocation policies (i.e. who does the client
trust to provide the requested service). Authorization should accommodate
various access control models and implementation.

It is a design objective that IntelliGrid Architecture services be
supportive of the functions and services defined within OSGA.

Key definitions:

**authenticate: 1.** To
establish, usually by challenge and response, that a [transmission](http://www.atis.org/tg2k/_transmission.html) attempt is
authorized and valid. **2.** [To] verify the identity of a [user](http://www.atis.org/tg2k/_user.html), user device, or other
entity, or the [integrity](http://www.atis.org/tg2k/_integrity.html)
of [data](http://www.atis.org/tg2k/_data.html) stored, transmitted,
or otherwise exposed to unauthorized modification in an [information system](http://www.atis.org/tg2k/_information_system.html)
(IS), or establish the validity of a transmission. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] **3.** A
challenge given by voice or electrical means to attest to the authenticity of a
[message](http://www.atis.org/tg2k/_message.html) or transmission.
[JP1]

**authentication: 1.** [Any] [Security](http://www.atis.org/tg2k/_security.html) measure designed to
establish the validity of a [transmission](http://www.atis.org/tg2k/_transmission.html), [message](http://www.atis.org/tg2k/_message.html), or [originator](http://www.atis.org/tg2k/_originator.html), or a means of
verifying an individual's [authorization](http://www.atis.org/tg2k/_authorization.html)
to receive specific categories of [information](http://www.atis.org/tg2k/_information.html). [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] [After JP 1-02] **2.**
A security measure designed to protect a [communications
system](http://www.atis.org/tg2k/_communications_system.html) against [acceptance](http://www.atis.org/tg2k/_acceptance.html)
of a fraudulent transmission or simulation by establishing the validity of a
transmission, message, or originator. [JP 1-02] **3.** Evidence by proper [signature](http://www.atis.org/tg2k/_signature.html) or seal that a document
is genuine and official. [JP 1-02]

**access control: 1.** A [service feature](http://www.atis.org/tg2k/_service_feature.html) or
technique used to permit or deny use of the components of a communication [system](http://www.atis.org/tg2k/_system.html). **2.** A technique
used to define or restrict the rights of individuals or [application](http://www.atis.org/tg2k/_application.html) programs to
obtain [data](http://www.atis.org/tg2k/_data.html) from, or place
data onto, a [storage](http://www.atis.org/tg2k/_storage.html)
device. **3.** The definition or restriction of the rights of individuals or
application programs to obtain data from, or place data into, a storage device.
**4.** [Limiting](http://www.atis.org/tg2k/_limiting.html) [access](http://www.atis.org/tg2k/_access.html) to [information system](http://www.atis.org/tg2k/_information_system.html)
resources only to authorized users, programs, processes, or other systems. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] **5.** That
function performed by the [resource controller](http://www.atis.org/tg2k/_resource_controller.html)
that allocates system resources to satisfy [user](http://www.atis.org/tg2k/_user.html) [requests](http://www.atis.org/tg2k/_requests.html).

Authentication for Access Control relies upon several basic
factors being achieved:

* That the identity
  of the entity/person is established.
  The Identity Establishment Service performs this function.
* That there is an acceptable level of Trust
  established that the entity is who they claim to be.
  The Trust Establishment and Quality of Identity services are involved in
  providing this functionality.
* That there is a policy and management process that
  has been used to determine which entity has the privileges to access
  certain assets, resources, or information.
  The Policy and SMI related services provide this functionality.
* That
  there is a mechanism to enforce the mandates of the policy and management
  process.
  The Authorization for Access Control service is responsible for providing
  this functionality.

There are generally three (3) categories of Access Control
that need to be addressed within a Security Domain:
[Physical Access Control to Assets](Anl_Security_Services.htm#Physical_Access_Control_to_Assets);
[Access Control to Computational
Resources](Anl_Security_Services.htm#Access_Control_to_Computational_Resources); and [Access Control to Information](Anl_Security_Services.htm#Access_Control_for_Information).

### Physical Access Control to Assets

The basic premise of physical
access control is intended to allow authorized individuals
to be able to enter the areas for which they have clearance to enter and to
make it difficult for un-authorized individuals to enter.  Based on the
Security Domain definition, physical access control is not an inter-domain
issue. However, there are some desirable aspects to any physical access control
system:

·      **Audit
Trail.** The system
should be capable of providing an audit trail of who actually entered a
specific area. Properly
implemented, a physical access control system can provide on-site personnel
listings/locations in the event of an emergency event.

·      **Intrusion
Detection.** The system
should be capable of detecting intrusion attempts of an un-authorized
individual to enter an area. There are
issues in regards to the quickness/speed of enunciating intrusion or intrusion
attempts.  The speed at which this enunciation can occur is a key metric
in regards to the ability of a SMI to respond to the intrusion. The system
should be robust enough that intrusions can be proven in an authoritative
manner so that legal prosecution has a probability of success.

·      **Authentication
Management.** The choice
of access control mechanisms should allow for multi-factor authentication and
ease of management in the event that revocation of access privileges is
required (e.g. User and Group Management issues). In order to accomplish this
service function, there must be a security token that is used to enable a final
access mechanism (e.g. a lock).

·      **Policy.**A
policy/strategy needs to address assets that are not capable of being
physically secured.  For these types of resources, informational and resource
security measures will need to be enhanced.  Examples of such an assets
are wireless networks and wireless technologies.

·      **Recovery
Plan.** A residual
risk analysis and recovery plan needs to be developed, as part of the Policy
service, to address resources for which no type of adequate security can be
provided.  An example of such physical resources are transmission lines
and telephone lines.

In order to provide physical access control, there needs to
have a physical barrier that separates critical or controlled areas from
un-controlled areas.  These barriers would typically be fences, walls, or
doors that have locks or security guards so that proper access privileges can
be determined.

#### Physical Access Technologies/Specifications

There are no relevant specifications regarding Physical Authorization for Access Control. However,
there are typical strategies that are worthy of some discussion (see Table 7).

Table 7: Typical Physical Access Control Strategies

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Security Strategy** | **Authentication Factor** | | | **Biometric** | **Comments** |
| **Single** | **Two** | **Three** |
| Security Guard Only |  |  |  |  | Needs to be augmented in order to provide audit capability, at a minimum. |
| Key/Lock | X |  |  |  | Adequate token that can be properly managed but can easily be duplicated that would facilitate un-authorized access. |
| Combination Lock | X |  |  |  | Typically adequate, but can be stolen through observation. |
| Sign-in sheet |  |  |  |  | Should not be used solely.  At a minimum, verification of the person’s identity signing-in must be facilitated. |
| Sign-in sheet with Photo-ID | X |  |  | X | Requires a security guard. |
| Sign-in sheet with confirmed clearance to enter. | X |  |  | X | Typically used for guest entry.  In order to be biometric, the confirming party must visually recognize and clear the entity requesting entry. |
| Video Surveillance |  |  |  |  | Should be used as audit/security for major/sensitive entrances. Provides a good mechanism for legal prosecution for remote sites. |
| Photo-ID with no sign-in sheet |  |  |  | X | Should not be used since no audit trail is possible. |
| Smart Card | X |  |  |  | It is assumed that SMART Cards would be used in conjunction with computerized locks so that a computerized audit trail can be generated.  However, it is typical that only ½ of the audit trail is generated since the cards are typically not required to exit the room. |
| Smart Card with Photo ID Card | X |  |  | X | if !vml?endif?Has the benefit of the Smart Card, but can also double as a Personal ID.  This is a recommended strategy. |
| Smart ID Card  used to enable Combination Lock |  | X |  |  | This is the best mechanism for restricting access to sensitive areas.  if !vml?endif? |
| Biometric Combination Lock |  | X |  | X | if !vml?endif?This is the best mechanism for restricting access to sensitive areas. |

Another method of analyzing the same strategies are shown in
the following table.

Table 8: Physical Security Strategies vs. Security Services
Provided

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Security Strategy** | **Security Service Provided** | | | **Comment** |
| **Identity** | **Trust** | **Access  Control** |
| Security Guard Only | ? |  |  | It is questionable that a security guard only strategy could provide adequate identification establishment. |
| Key/Lock |  | x | x | Provides a mechanism to establish a relative level of Trust (due to the person having the key) and provides appropriate access control. |
| Combination Lock |  | x | x | Provides a mechanism to establish a relative level of Trust (due to the person having the combination) and provides appropriate access control. |
| Sign-in sheet |  |  |  | Without actual identity establishment, no security can be provided. |
| Sign-in sheet with Photo-ID | x |  |  |  |
| Sign-in sheet with confirmed clearance to enter. | ? | x |  | Only provides Identity Establishment if a photo-ID is used in conjunction with the sign-in sheet. |
| Video Surveillance |  |  |  | Provides audit and repudiation capability only. |
| Photo-ID with no sign-in sheet | x |  |  |  |
| Smart Card |  | x | x | A Smart-Card only does not provide Identity Establishment.  Identity Establishment is a required function/service for Access Control. Therefore, the use of Smart-Cards only should not be considered. |
| Smart Card with Photo ID Card | x | x | x | This is a recommended strategy for non-critical area access. |
| Smart ID Card  used to enable Combination Lock | x | x | x | This is one of the recommended deployment strategies for critical areas. |
| Biometric Combination Lock | x | x | x | This is one of the recommended deployment strategies for critical areas. |

##### Technological Assessment

The suggested technology to be used to provide Access
Control to critical areas is the use of multi-factor access control.  It
is further suggested that SMART-CARD[[4]](Anl_Security_Services.htm#_ftn4)s that double as personal identification
cards be utilized to enable combination locks.  Furthermore, it is also
recommended that such technology deployment be used in
conjunction with an electronic audit mechanism. 

It is recommended
that biometric identification mechanisms be used when applicable.

### Access Control to Computational Resources: Computers and Networks

The
basic premise of computational access control is intended to allow authorized
individuals to be able to access programs for which they have clearance to make use of. Based on the Security Domain definition,
computational access control is both an inter-domain and intra-domain issue.
However, the enforcement of computation access control is purely an
intra-domain issue.  For inter-domain access control the Identity Mapping
service (and its required sub-functions) actually provides the mapping from an external
identity to an identity recognized and managed intra-domain.

·       **Audit Trail.** The system
should be capable of providing an audit trail of who accessed a given
computational resource.

·       **Intrusion Detection.** The system
should be capable of detecting intrusion attempts of an un-authorized
individual to a computational resource. There are
issues in regards to the quickness/speed of enunciating intrusion or intrusion
attempts.  The speed at which this enunciation can occur is a key metric
in regards to the ability of a SMI to respond to the intrusion. The system
should be robust enough that intrusions can be proven in an authoritative
manner so that legal prosecution has a probability of success.

·       **Access Control Management.** The choice
of access control mechanisms should allow for multi-factor authentication and
ease of management in the event that revocation of access privileges is
required (e.g. User and Group Management issues). In order to accomplish this
service function, there must be a security token that is used to enable a final
access mechanism (e.g. a lock).

·       **Security Policy.** A
policy/strategy needs to address assets that are not capable of being
secured.  For those types of resources, the level of trust should be
considered low.

The aforementioned
issues need to be addressed for a variety of computational resources: 
**Operating Systems (OSs)**; programs within a OS that
has access control; **Computer Programs** within an environment where there is no OS access
control required to access the program (e.g. an RTU); and **Communication Networks**.

#### Operating Systems

Operating System
(OS) access control requires Identity Establishment (see the identity
establishment service).  The access control service, for OSs, determines which programs/computational
resources the Identified User/Program has privileges to execute/access.

The major issues
regarding this access are:

·      To provide an appropriate policy and SMI so that such access is granular
enough to provide enough audit capability.

·      Managing the configuration in a distributed environment.

·      The level of trust that can be associated with the OS to perform its
tasks in a secure manner (see ACC-01).  Several issues are mitigated if a
“Trusted/Secure” OS is used.  However, the use of such OSs
in IntelliGrid Architecture environment is not viable in a majority of the cases, therefore
this section will address non-Trusted OS issues.

For all OSs, the issue of access control relates to properly
managed **Access Control Lists** that are typically OS specific.  However,
care needs to be taken to ensure that if Role Based Access is used, that an
audit mechanism is provided in order to reference back to the actual
individual/entity that has accessed the OS. Additionally, the information in
ACC-02 should be considered when developing the OS access framework in a
distributed environment.

#### **Computer Programs**

In the cases where
an OS does not provide Access Control to the programmatic level, programs
themselves need to provide this capability. This is particularly true for
electronic protocol processes that bypass OS authentication on the destination
of the communication path.  In such a situation, it is incumbent upon the
destination program/process to apply the appropriate security mechanisms. 

In IntelliGrid Architecture there
will be computational and communication technologies integrated of various
capabilities.   These various capabilities (e.g.
process/memory/storage capacity or bandwidth limitations) require that
different technological solutions be available.  However the functional
objectives remain consistent: provide a manageable environment and to provide
enough granularity to provide a capability for non-repudiation.

#### Communication Networks

There are several
types of communication networks that need to be addressed:

·      **Inter-Domain networks**where the physical network are exposed.
The major issue with these types of physical
networks is that both domains do not manage the network segments that provide
the inter-domain interfaces.  These segments are typically provided by a
third party and therefore constitutes a third Security Domain. Thus it is
important that appropriate access control be provided at the security domain
interface points.

·      **Intra-Domain networks**where the physical network is within a Security
Domain.
For intra-domain networks, some Security Domains may desire to control the
computers/computer users that actually have access to the network.  Once a
resource is within a Security Domain, there is no reliable mechanism to prevent
physical access to the network.  Thus it becomes incumbent upon the SMI to
detect that a non-authorized access to the network has been attempted or been
successful.  Additionally, it may be possible to make it more difficult
for a non-authorized resource to make use of the network through proper
management of the network addresses so that no address is assigned to the
intruding resource.

·      **Wireless
LAN/WAN Networks** whose transmissions can be easily monitored and spoofed.
This type of network represents a intra-domain network that REQUIRES management
in regards to who can actually make use of the network.  The issue can be
easily demonstrated by looking at the prevalence of Wi-Fi.
In the Wi-Fi case, hot-spots (e.g. Starbucks, airports) could not recoup their
investment without a challenge response mechanism to ensure that only
authorized (e.g. paid subscription entities) are actually assigned an address
that facilitates real communications.
Such mechanisms may prevent off-segment communications, but will not prevent
denial-of-service attacks (see ACC-03).  Thus such systems need to be
augmented beyond challenge-response.

·      **Dial-up Networks:** There is a well-documented history in regards to the
vulnerabilities associated with dial-up networks.  These types of networks
are inherently susceptible to denial-of-service attacks and have poor identity
establishment/access control at a physical/network level.  This is
especially true for equipment that is deployed in the Transmission and
Distribution environment.

Table 9: References
regarding Computational Resource Access Control

|  |  |
| --- | --- |
| ACC-01 | Stephen Radford – Trusted Operating Systems and Their Evolving Non-Trusted Counterparts ,  January 23, 2003. SANS Institute |
| ACC-02 | **Fine-Grain Authorization for Resource Management in the Grid Environment**. K. Keahey, V. Welch. Proceedings of Grid2002 Workshop,  2002. |
| ACC-03 | AA-2004.02 -- Denial of Service Vulnerability in IEEE 802.11 Wireless Devices (AusCERT) |
| ACC-04 | RADIUS Protocol Security and Best Practices, Published: January 1, 2002, By Joseph Davies, Microsoft Corporation  Available from:  <http://www.microsoft.com/technet/itsolutions/network/security/radiusec.mspx> |

 

##### Technological Assessment Specifications/Standards

Table 10 represents
a set of specifications and/or standards that are relevant to the understanding
of the issues regarding access control for computational
resources. Those specifications marked as Recommended or Recommended
Reading should be considered as materials that should be considered prior to
actually implementing the access control service.

Table 10: Relevant
Computational Resource Access Control Standards/Specifications

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
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
| RFC 2869 | RADIUS Extensions |  |
| RFC 1221 | Host Access Protocol (HAP) Specification - Version 2 |  |
| ISO/IEC 10164-9:1995 | Information technology -- Open Systems Interconnection -- Systems Management: Objects and attributes for access control |  |
| ISO/IEC 10181-3:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Access control framework | Recommended |
| WebDAV | Access Control Extensions to WebDAV |  |
| Microsoft | Remote Access Service (RAS) |  |
| OASIS | Extensible Access Control Markup Language (XACML)  Available from:  http://xml.coverpages.org/xacml-schema-policy-v15.pdf | Recommended when used in conjunction with other XML based technologies. |
| IBM | XML Access Control (XACL) | Proprietary but has been implemented as part of IBM’s security framework. |
| CJCSI 6731.01 | Global Command and Control System Security Policy,  Chairman of the Join Chiefs of Staff Instruction,  December 31, 1998 |  |
| FIPS PUB 112 | Password Usage |  |
| FIPS PUB 113 | Computer Data Authentication |  |

 

#### Technological Assessment and Recommendations

#### OS Recommendations

It is recommended
that Trusted OSs be used whenever possible.
Additionally, ANSI INCITS 359-2004 us suggested as an implementation
strategy for Role Based Access.

#### Computer Programs

It is recommended
that the appropriate access control list mechanisms be used in regards to the
applications where such technologies have been noted in Table 10.  Thus, make use of:

·      RFC 1013 for
**X-Windows** applications.

·      RFC 2086 for 
Internet Message Access Protocol (**IMAP**)-based e-mail applications.

·      RFC 2045 for 
Multipurpose Internet Mail Extensions (**MIME**) for the Simple Mail Transfer
Protocol (**SMTP**).

·      RFC 2228 for
File Transfer Protocol (**FTP**) Security Extensions

·      RFC 2820 for Access Control for 
Lightweight Directory Access Protocol (**LDAP**).

·      RFC 1305 in regards to
Network Time Protocol (**NTP**). It is recommended that the authentication,
access control, and other security
extensions in Appendix C be implemented and used. Currently, Simple Network Time
Protocol (**SNTP**) described in RFC 2030 does not address security (pending
work).

·      RFC 3414, RFC 3411, and RFC 1351 for Security for
Simple Network Management Protocol (**SNMP**).  It is also recommended
that SNMPv3 be utilized when possible.    
  
There is an issue regarding the lack of definition of standardized security
related Management Information Base (**MIB**) objects.  IEC TC57 WG15 has
undertaken the task to define security MIB objects that could facilitate
intrusion detection.  It is recommended that the recommendations of IEC
62351-7 (Objects for Network Management) be reviewed carefully when these become
available.

·      RFC 2817 and RFC 2818
for HyperText Transfer Protocol Security 
(**HTTPS**) for security for the HyperText
Transfer Protocol (HTTP).

Otherwise, it is
suggested to follow the general policies/procedures set forth in ISO/IEC
10181-3:1996 and make use of any application specific access control strategies
set forth.

#### Communication Networks and Protocols

In general it is
recommended that all computational resources, when possible, be assigned
dynamic addresses that allow off-segment communications. 
There is no single technology that can accomplish this, but a challenge
response mechanism is suggested as part of the implementation strategy. For those resources
that require fixed addresses (e.g. servers of data), it is suggested that
network based access control lists be implement in order to prevent
un-authorized off-segment communication. There is a
substantial amount of work occurring within IEC TC57 WG15 to secure several of
the communication protocols that are intended to be used by IntelliGrid Architecture.  It is
suggested that these be adopted and deployed as rapidly as is feasible.

Wireless networks
are extremely susceptible to denial-of-service attacks.  In order to
mitigate this issue, AES encryption on wireless links is suggested.

Dial-up access
control should be implemented through the use of **RADIUS** (RFC 2865 and RFC 2869)
when this is feasible.  Such access should be deployed so that there is an
additional access control list (e.g. a Firewall or router based ACL) that
provides additional security.  Thus, when possible, it is suggested that
NO direct dial-up access be given to a computer or a computer process.

However, this is not
always
feasible in the Transmission and Distribution systems deployed within IntelliGrid Architecture
environment (e.g. RTUs and field devices).  For this class of resource, or
resources with similar constraints, it is suggested that the devices be
implemented in such a manner that denial-of-service is mitigated: 

·       Dial-up
connections should be constructed such there is an inactivity time-out to
prevent a connect/hold the port open denial of service attack.

·       Once the
port is connected, there should be a time-out on the connection that requires
valid communication protocol/application level information flow.

It is not suggested to implement a dial-back
strategy since these become difficult to manage and maintain and does not allow
the type of environment that IntelliGrid Architecture is attempting to promote.

### Access Control to Information

Information access
control is extremely similar to a combination of OS and program access. 
However, it is up to each individual program to provide
the appropriate level of access control. 

ACC-04 represents
a very simple summary of the granularity required in access control for most PICOMs:  Control over Reading; Control over
Changing;  and Control over Storing.  Additionally, for Object
Oriented access, there may need to be an ability to prevent an entity from
discovering that an Object Exists (optional).

 

Table 11:
References relating to Access Control for Informational Resources

|  |  |
| --- | --- |
| ACC-04 | Access Control on the Semantic Web (wc3.org)  Available from: http://www.w3.org/2002/03/semweb/access-control |

 

## Confidentiality Service

Protect the
confidentiality of the underlying communication (transport) mechanism, and the
confidentiality of the messages or documents that flow over the transport mechanism in a OGSA compliant infrastructure. The
confidentiality requirement includes point–to–point transport as well as
store-and-forward mechanisms.

Key definitions:

**confidentiality:
1.** Of classified or sensitive [data](http://www.atis.org/tg2k/_data.html),
the degree to which the data have not been compromised; i.e., have not been
made available or disclosed to unauthorized individuals, processes, or other
entities. [After 2382-pt.8] **2.** [Assurance](http://www.atis.org/tg2k/_assurance.html)
that [information](http://www.atis.org/tg2k/_information.html) is not
disclosed to unauthorized persons, processes, or devices. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]
**3.** A property by which information relating to an entity or party is not
made available or disclosed to unauthorized individuals, entities, or
processes. [T1.Rpt22-1993]

There are two main
mechanism to provide confidentiality for electronically transmitted information:
encryption or transmission over a secure infrastructure.

### Encryption

It is important to
realize that there is no 100% effective mechanism to protect electronically
transmitted information for an indefinite length of time.  Initially, when
the Data Encryption Standard (DES) was specified, it
was thought that 56-bit encryption protection could protect information for
20-30 years.  However, with the increase in computational capability, and
the decrease in cost for that capability, in 1999 DES was cracked in under 22
hours (see CONF-02) . Based upon Moore’s Law, today DES could be cracked in
approximately 41 minutes considering. 

To respond to the new reality, NIST and several standards organizations (in
particular IEEE) developed a more advanced and secure encryption standard known
as the Advanced Encryption Standard (AES).

“In
comparison, DES keys are 56 bits long, which means that there are approximately
7.2 x 1016 possible DES keys. Thus, there are on the order of 10 (21) times
more AES 128-bit keys than DES 56-bit keys. Assuming that one could build a
machine that could recover a DES key in a second (i.e. try 255 keys per
second), then it would take that machine approximately 149 thousand-billion
(149 trillion) years to crack a 128-bit AES key. To put this into perspective,
the Universe is believed to be less than 20 billion years old. NIST believes
that AES will remain secure beyond the next twenty years. AES implementations
will also be exportable, and AES implementations in proprietary systems will
just need a one-time review prior to export” [CONF-01]

The above claim is
similar to the claims made by DES when it was first introduced.  Whereas
DES and Triple-DES (3DES) have had almost twenty years of deployment prior to
replacement due to “crackability”, the advent of
Quantum Computers (see CONF-03) may not allow the modern encryption algorithms
the same.  If Quantum Computers were available today, using Grover’s
Algorithm (see CONF-04) it could be extrapolated that even 512 bit DES could be
cracked in approximately 1 second.  AES is more complex and is less prone
to Grover’s Algorithm, however the NIST statement (CONF-01) will definitely not
be true in the near-term future.

The advent of
Quantum Computers raises the issue of how to make encryption effective. 
Even without the advent of Quantum technology, the following recommendations
are valid:

·      Choose a modern encryption algorithm for the purposes of encryption.
There are many factors that enter into an appropriate algorithmic choice. 
The factors that need to be considered are the additional CPU processing that
the use of encryption will require and the bandwidth/transmission performance
characteristics desired.
At the NERC Data Exchange Working Group meeting in April 2004, the following
results were presented for Secure IEC-60870-6 TASE.2 (ICCP): the additional CPU performance requirements, for the use of TLS and AES 256,
represented an increase from 1% to 1.35% for encryption and 1% to 1.41% for
decryption (percentages based upon total CPU being 100%).  It was also
found that AES 256 was more CPU efficient than either DES or 3DES.
It was found that the bandwidth overhead increased by the size of certificates
exchanged, but only increased 1% in regards to normal ICCP traffic once the initial
connection and symmetric keys were established.

·      When using encryption, make sure that the technology used to “negotiate”
encryption can negotiate multiple encryption algorithms.

·      If possible, make sure that the negotiation can be upgraded to newer
encryption algorithms as new, more robust algorithms, become available.

·      Make use of technologies where the encryption keys can dynamically be
re-negotiated without interrupting the communication information flow.

 Table 12: Reference
Relevant to Encryption Technology

|  |  |
| --- | --- |
| CONF-01 | **NIST Announces New Government Aes Encryption Standard - Technology Information**  Available from: <http://articles.findarticles.com/p/articles/mi_m0BNO/is_2000_Nov/ai_66297312> |
| CONF-02 | Jason Meserve , DES code cracked in record time, Network World,  01/20/99  Available from:  <http://www.nwfusion.com/news/1999/0120cracked.html> |
| CONF-03 | Aaron Ricadela, Quantum’s Next Leap, Information Week, May 10, 2004 |
| CONF-04 | Matias Castro ,What Use is My Quantum Computer Now I Have it?    Available From:  http://www.doc.ic.ac.uk/~nd/surprise\_97/journal/vol2/mjc5/ |

### Technological Assessment and Specifications

There are several
different mechanisms through which to develop assessments regarding
encryption.  For the purposes of this section, applicability
to specific communication media will be used. In general, it is
suggested to make use of X.509 certificates to provide public/private key
encryption exchanges when possible.  Such a choice will ease integration
with other certificate technologies (e.g. management) that are being
recommended as part of other security services.

When X.509
certificate use is not appropriate, it is suggested that RFC 2898 (PKCS#5) be
utilized.  This allows encryption to be established based upon
username/passwords.

#### Protocol Basis

In general, it is
recommended to use the appropriately specified encryption standard associated
with the protocol (e.g. HTTPS for HTTP).  There are further recommendation for TCP/IP:

**TCP/IP
Transmissions**

It is recommended
that TLS with AES (RFC 3268) or PPP Encryption Control Protocol (RFC 1968)
be used to provide encryption.  These represent the most modern and secure
mechanism.

#### Media

**Serial**

If the path of the
serial link does not provide enough confidentiality nor the protocol in use over
the link, and confidentiality is still desired then the following is recommended:

·      
If the peers can be upgraded to support encryption, then this should be
the preferred approach.

·      
For legacy systems, that are not upgradeable, it is suggested that
external hardware be applied.  Further it is recommended that AGA 12-1 be
evaluated for this purpose.

**Ethernet,
SONET, FDDI, and Other Cable Media**

It is recommended
to make use of Virtual Private Network (VPN) technology when possible.

**Wi-Fi and
Wireless Technologies**

The Web Encryption
Protocol (WEP) specified in IEEE 802.11b has been proven to be vulnerable and to
not provide adequate protection.  New versions of Wi-Fi and wireless
technologies are coming equipped with AES encryption.  It is the AES
encryption that is recommended.  Further it is recommended that
WPA2/80211.i be adopted in order to achieve the implementation of this
recommendation.

It is further
recommended that any legacy (e.g. WEP based) Wi-Fi equipment be replaced or
upgraded, as the vulnerabilities are well known and not manageable. 

Table 13:
Encryption Related Specifications/Standards

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 3370 | Cryptographic Message Syntax (CMS) Algorithms |  |
| RFC 3447 | Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1 |  |
| RFC 2898 | PKCS #5: Password-Based Cryptography Specification Version 2.0 | Recommended when certificate exchange is not appropriate. |
| RFC 1968 | The PPP Encryption Control Protocol (ECP) |  |
| RFC 2246 | The TLS Protocol Version 1.0 |  |
| RFC 2409 | The Internet Key Exchange (IKE) | Used for VPNs |
| RFC 1040 | Privacy enhancement for Internet electronic mail: Part I: Message encipherment and authentication |  |
| RFC 2946 | Telnet Data Encryption Option |  |
| RFC 2440 | OpenPGP Message Format |  |
| RFC 1423 | Privacy Enhancement for Internet Electronic Mail: Part III: Algorithms, Modes, and Identifiers |  |
| RFC 2408 | Internet Security Association and Key Management Protocol (ISAKMP) | Used for VPNs |
| RFC 2510 | Internet X.509 Public Key Infrastructure Certificate Management Protocols |  |
| RFC 3268 | Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS) |  |
| RFC 2093 | Group Key Management Protocol (GKMP) Specification |  |
| RFC 2459 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |  |
| RFC 2040 | The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms |  |
| FIPS 197 | Federal Information Processing Standards Publication 197,  November 26, 2001, Specification for the Advanced Encryption Standard (AES)  Available from: http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf | Recommended |
| RSA PKCS #12 | Personal Information Exchange Syntax Standard, version 1.0. |  |
| RSA PKCS #8 | Private-Key Information Syntax Standard |  |
| IEEE 802.11b | Web Encryption Protocol |  |
| AGA-12 | Cryptographic Protection of SCADA Communications General Recommendations. |  |
| WPA | Wi-Fi Protected Access |  |
| IEEE 802.11i | Security for Wireless Networks |  |
| WPA2 | Wi-Fi Protected Access Version 2 |  |

 

Table 14: Digital
Certificate Related Specifications/Standards

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 2510 | Internet X.509 Public Key Infrastructure Certificate Management      Protocols. C. Adams, S. Farrell. March 1999. |  |
| RFC 2511 | Internet X.509 Certificate Request Message Format. M. Myers, C.      Adams, D. Solo, D. Kemp. March 1999. |  |
| RFC 2527 | Internet X.509 Public Key Infrastructure Certificate Policy and      Certification Practices Framework. S. Chokhani, W. Ford. March 1999. |  |
| RFC 2560 | X.509 Internet Public Key Infrastructure Online Certificate  Status Protocol - OCSP. M. Myers, R. Ankney, A. Malpani, S. Galperin,      C. Adams. June 1999. |  |

 

### Communication Path Selection

There is a
mechanism of mitigating the need to encryption.  This is to evaluate or
provide a communication path that inherently provides enough protection (see the Path Routing and QOS service for further
information).

## Credential Conversion Service

The credential
conversion service provides credential conversion between one type of
credential to another type or form of credential. This may include such tasks as reconciling group membership, privileges,
attributes and assertions associated with entities (service requestors and
service providers). For example, the credential conversion service may convert
a Kerberos credential to a form which is which is required by the authorization
service. The policy driven credential conversion service facilitates the
interoperability of differing credential types, which may be consumed by
services. It is expected that the credential conversion service would use the
identity mapping service.

Key definitions:

**credential:
1.** In [cryptography](http://www.atis.org/tg2k/_cryptography.html), a subset of [access](http://www.atis.org/tg2k/_access.html)
permissions (developed with the use of media-independent [data](http://www.atis.org/tg2k/_data.html))
attesting to, or establishing, the identity of an entity, such as a birth certificate,
driver's license, mother's maiden name, social security number, fingerprint,
voice print, or other [biometric](http://www.atis.org/tg2k/_biometric.html) parameter(s).
[After X9.69] **2.** [In [security](http://www.atis.org/tg2k/_security.html)],
[information](http://www.atis.org/tg2k/_information.html), passed from
one entity to another, used to establish the sending entity's access rights. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

Credential
conversion is also a required service for Single-Sign on and the Identity
Mapping security services.  Besides performing the actual mappings, there
is an inherent requirement that such a service provide an audit mechanism so
that it is possible to determine the original identity/credential that was
converted.  This is a necessary requirement in order to provide a robust
audit mechanism in a multi-domain environment.

### Technological Assessment

The prevalent work
is being sponsored by the Organization for the Advancement of Structured
Information Standards (OASIS).  This is work in progress but is the first industry/standards based consortium that is
attempting to solve the problem.  However, the current work involves
certificate usage and does not directly address the issue of username/password
conversion nor the audit trail issues. Except for the
general recommendations found in the Identity Establishment service, only
certificates require further recommendations in regards to credential
conversion.

#### Certificate

Furthermore, there
has been little thought in enhancing the SAML specification to standardize a
chain or properties that would allow the Quality of Identity service to be facilitated.  It is suggested that
SAML and the OASIS work be adopted as the foundation for the Credential
Delegation service. However, further work and IntelliGrid Architecture enhancements may be
required.

 Table 15:
References and Specifications regarding Credential Conversion

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS Security Technical Committee | Security for Grid Services  Available from:  http://www.globus.org/Security/GSI3/GT3-Security-HPDC.pdf |  |
| OASIS Security Technical Committee | Attribute Profiles for SAML 2.0  Available from:  http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf | Incomplete, but is on the correct track. |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0  Available from:  http://www.oasis-open.org/committees/download.php/2290/oasis-sstc-saml-1.0.zip | Recommended |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf | Draft that is needed to establish identity within a SAML environment. |
|  |  |  |

 

## Credential Renewal Service

In many scenarios,
a job initiated by a user may take longer than the life span of the user’s
initially delegated credential. In those cases, the user needs the ability to be notified prior to expiration of the
credentials, or the ability to refresh those credentials such that the job can
be completed.

It is worthy to
note that the Credential Renewal service provides some of the capability of
User and Group Management service.  However, it does not include how to
revoke or initially allocate the credentials.  However, in general it is a
Security Domain and IntelliGrid Architecture issue in regards to the period of time required for
credential renewal.

Performing a more
in-depth analysis of the credential renewal process, the general issues are:

·      
Determining when the credentials need to be renewed.  This is
typically a Security Domain’s policy issue.

·      
Determining a mechanism to detect a credential that needs to be renewed.

·      
Provide a mechanism for credential renewal.

 

OASIS specifies
several different types of credentials that need to be considered for
renewal.  Each has different aspects to renewal.  The IntelliGrid Architecture relevant
types are:

·      Internet Protocol-based credentials are
related solely to address resolution as the credential.  Address spoofing
is a prevalent threat in IntelliGrid Architecture environment and therefore the use of this
credential mechanism is not suggested.
In order to renew an addressed based credential, address-to-name resolution is
required as well as appropriate security on such resolution requests.

·      
InternetProtocolPassword makes use of
username/password as well as address resolution to establish credentials.
This credential methodology has the same issues with address credential renewal
as well as verifying that the password is viable or in need of renewal.

·      
Password makes use of a username/password combination in the clear.
Username/Password management is a major issue that needs to be resolved.

·      
PasswordProtectedTransport makes use of an
encrypted transport to transmit a username/password combination (e.g. HTTPS
conveying a username/password).

·      
SmartCard renewal is strictly a policy and SMI
issue.  The policy must address when a SmartCard
must be renewed and the mechanism for performing a renewal.

·      
SmartCardPKI renewal adds the issue of digital
certificate renewal to the need to renew a particular Smart Card.  Since
most digital certificates have an expiration date, it is the certificate date
that should take precedence in the renewal process (e.g. policy may be able to
ignore the renewal of the card itself).  However, this is not the case if
the SmartCardPKI solution is being used as a Personal
Identification card that requires visual inspection for physical access.

·      
SoftwarePKI uses digital certificates and
therefore certificate renewal is the major issue.

·      
TimesyncToken is a hardware token that is used
to generate a unique token as a credential.

·      
Visual Person Identification Card used with visual inspection to provide
physical access control.  
  
Any credential type that can be used to obtain physical access based upon
visual inspection need to be replaced or modified in a timely manner.  The
periodicity of the change is dependent upon the Security Domain’s policies.

 

#### Technological Assessment and Relevant Specifications

There are certain
general recommendations that can be made:

·      When using address resolution and TCP/IP, make use of the Domain Name Service and a authenticated Directory server. 
Dynamic address assignment should be the preferred mechanism with the resulting
address being placed in the authenticated directory server.

·      Visual Credentials should be replaced/modified on a time period based
upon the Security Domain’s policy.  It may be less expensive to adopt a
modification, as opposed to a replace strategy (e.g. the same model as
automobile license tabs versus license plates).

·      Smart Cards should include a renewal date as part of the information
that is contained on the card.  This field should encrypt and digitally
signed so that tampering can be detected.  As the Smart Card is used,
advanced notification of the need for renewal needs to be given to the holder.

·      Certificate based technologies: X.509 certificates are the recommended
certificate type.  Certificates should be accessible via PKCS#10
interfaces.  The date of certificate lifetime expiration should be used as
the renewal date. As the certificate is used, advanced notification of the need
for renewal needs to be given to the holder.

·      Biometric based technologies need to have renewal dates based upon the
Security Domain’s policy.

#### Specific Recommendations

##### Certificates

It is recommended
that RFC 2797 or RFC 2560 (OCSP) to determine if the certificate needs to be
renewed. If neither of these is possible, then it
becomes a local Security Domain/implementation
issue. Certificate renewal should be performed via RFC 2797 when
possible.

Table 16: Relevant
Specification regarding Credential Renewal

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO 9735-9:2002 | Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 9: Security key and certificate management message (message type- KEYMAN) |  |
| NERC | Certificate Policy for the Energy Market Access and Reliability Certificate (e‑MARC) Program Version 2.4  Available from:  ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc |  |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf |  |
| RFC 2459 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |  |
| RFC 2511 | Internet X.509 Certificate Request Message Format |  |
| RFC 2560 | X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP |  |
| RFC 2797 | Certificate Management Messages over CMS |  |
| RFC 2875 | Diffie-Hellman Proof-of-Possession Algorithms |  |
| RFC 2986 | PKCS #10: Certification Request Syntax Specification Version 1.7 |  |
| RFC 3280 | Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure  Certificate and Certificate Revocation List (CRL) Profile |  |
| RFC 3369 | Cryptographic Message Syntax (CMS) |  |
| RFC 3647 | Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework |  |
| RFC 1591 | Domain Name System Structure and Delegation |  |
| RFC 1608 | Representing IP Information in the X.500 Directory | Recommended |
| RFC 1612 | DNS Resolver MIB Extensions | Recommended |
| RFC 2230 | Key Exchange Delegation Record for the DNS |  |
| RFC 2276 | Architectural Principles of Uniform Resource Name Resolution |  |
| RFC 2535 | Domain Name System Security Extensions | Recommended |
| RFC 2592 | Definitions of Managed Objects for the Delegation of Management Script |  |
| RFC 2874 | DNS Extensions to Support IPv6 Address Aggregation and Renumbering |  |
| ISO 10202-1:1991 | Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 1: Card life cycle | Recommended Reading |
| ISO 10202-7:1998 | Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 7: Key management |  |

 

## Delegation Service

Provide facilities
to allow for delegation of access rights from requestors to services, as well
as to allow for delegation policies to be specified. When dealing with delegation of authority from an entity to another,
care should be taken so that the authority transferred through delegation is
scoped only to the task(s) intended to be performed and within a limited
lifetime to minimize the misuse of delegated authority.

Based upon the
aforementioned definition, delegation involves Credential Conversion and
Authorization for Access Control services. There are two primary types of
delegation that need to be addressed:

·      
Delegation of Addresses:  This type of delegation could occur due
to proxies, firewalls or gateways.  The main requirements of such
delegation are to be able to provide an audit mechanism that allows repudiation
to the original address.   
  
A good example of why this is needed is the email SPAM problem that we face
today.  It is difficult with address and email account spoofing to
determine the actual sender of the original SPAM message.

·      
Access Privilege Delegation would typically result in the transformation
of one entity’s privileges to some type of Role Based set of privileges. 
Once the ability to audit the delegation is of primary importance.

 

### Technological Assessment and Relevant Specifications

It is recommended
that either RBAC or SAML be considered as appropriate.

 Table 17: Relevant
Specifications for the Delegation Service

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| BCP 65 | Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures |  |
| RFC 1034 | Domain names - concepts and facilities |  |
| RFC 1507 | DASS - Distributed Authentication Security Service |  |
| RFC 1591 | Domain Name System Structure and Delegation |  |
| RFC 1608 | Representing IP Information in the X.500 Directory |  |
| RFC 1612 | DNS Resolver MIB Extensions |  |
| RFC 2230 | Key Exchange Delegation Record for the DNS |  |
| RFC 2276 | Architectural Principles of Uniform Resource Name Resolution |  |
| RFC 2535 | Domain Name System Security Extensions |  |
| RFC 2592 | Definitions of Managed Objects for the Delegation of Management Script |  |
| RFC 2874 | DNS Extensions to Support IPv6 Address Aggregation and Renumbering |  |
| RFC 3401 | Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS |  |
| RFC 3402 | Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm |  |
| RFC 3403 | Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database |  |
| RFC 3404 | Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource Identifiers (URI) |  |
| RFC 3405 | Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures |  |
| RFC 3761 | The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM) |  |
| STD 13 | Domain Name System | Recommended |
| ANSI INCITS 359-2004 | Role Based Access Control (RBAC) | Recommended |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |

 

## Firewall Traversal Service

A major barrier to
dynamic, cross-domain Grid computing today is the existence of firewalls. As
noted above, firewalls provide limited value within a dynamic Grid
environment. However, it is also the case that firewalls
are unlikely to disappear anytime soon. Thus, the OGSA security model must take
them into account and provide mechanisms for cleanly traversing them—without
compromising local control of firewall policy.

There are several
major issues with the use of firewalls:

·      Firewalls are typically invasive and perform address translation without
providing a useable audit record.

·      Firewalls that have the ability to perform state-based inspection are
not capable of analyzing the complex protocols that IntelliGrid Architecture is considering.

·      Firewalls are difficult to manage and must be monitored as part of the
SMI process.

However, firewalls
are deployed in order to protect critical infrastructure computational
resources and should be deployed at inter-domain connectivity points. 

Within the context
of IntelliGrid Architecture environment, there are several different functions that a firewall
could provide.  It is a policy/deployment issue in regards to which ones
are provided.

·      **Media Isolation**: Provides physical isolation from the extranet to the intranet
of the security domain.  This typically means that two physical media
interfaces are required.  It is worthy to note that bridges and most
routers have two physical interfaces and therefore could be used to provide the
media isolation in a deployment scenario.
It is recommended that media isolation be provided for all firewalls.

·      **Address Translation**: It is often difficult to protect an intranet if the
addresses of that intranet are the same as and accessible of the
extranet.  It is worthy to note that some routers have this capability.
It is recommended that each firewall transversal include address translation if
access control is not implemented.

·     **Protocol/Port Restriction**:  One of the main purposes of a firewall
is to restrict what type of communications can occur in-bound/out-bound through
the firewall.  Typically, domain firewalls should be configured to allow
only the communication traffic set by policy.  This is typically done via
port restriction or some other means.
It is recommended that all firewalls deployed have the capability to restrict
incoming protocol traffic.  It is a policy issue if restriction of
outgoing traffic is needed.

·      **Audit**:  Although many firewalls do not provide adequate audit
capability, this is a mandatory function.  It is recommended that all
address pair (e.g. extranet/intranet pair establishment) be logged into an
audit record.  Additionally, if the protocol/port identification can be
provided in the record, as well as identity, this would also be recommended.

·      **Identity Establishment**:  This function allows a firewall to
establish the identity of an external entity in order to establish trust.

·      **Access Control**:  The ability to make use of the established
identity in order to restrict access to intranet resources.

·      **Confidentiality**:  The ability for a firewall to encrypt
inter-domain information (typically done via establishment of a VPN).

·      
**State based inspection**: The firewall has a knowledge of the protocol and
therefore makes use of the identity established and Access Control to determine
which protocol packets to forward to the intranet.

### Technological Assessment and Relevant Specifications

There are three
major types of firewalls:

·     **Transparent** (see FIRE-01 and FIRE-02): These firewalls perform OSI layer
2 or 3 bridging and do not typically provide state
inspection.  However, they do not obscure addressing information and
tend to be the fastest type of firewall when performance is measured in terms
of packet throughput.  Since these are transparent, these types are the
easiest to transverse when properly configured. 
This is the only firewall type that could possible meet the 4msec performance
requirement.

·    **Non-Transparent:** These firewalls typically perform the following
functions:  packet filtering and proxy service (e.g. address translation).

·      **Non-Transparent with Stateful Inspection**: Same
capability as non-transparent but has the additional ability to examine the
contents of each packet.  This is typically the lowest performance type of
firewall when performance is measured in regards to packet throughput.

Firewall
Transversal is automatically provided when Transparent Firewalls are utilized,
however the issue still remains for both versions of non-transparent firewalls.
The typical mechanism for allowing transversal (e.g. from outside a Security
Domain to inside) is via a proxy service or a set of firewall supplied cookies.
However, there are several issues about sending/receiving such information in
the clear. Therefore, encryption is desired.

Current firewall
transversal thoughts are to create a SSL/TLS tunnel (thereby verifying the
remote node has certain access rights) and then using a internal proxy to
enforce further privilege restrictions.

if !vml?![](Anl_Security_Services_files/image007.jpg)endif?

Figure 3: Example
of SSL/TLS Tunnel for Firewall Transversal[[5]](Anl_Security_Services.htm#_ftn5)

Figure 3 shows the
SSL tunnel being used to a DMZ where the backend application data is proxied on servers located within the DMZ.  It would
also be possible to allow stateful and privilege proxy access directly
to the back-end data providers if needed.  Either
architecture is viable and will be up to the Security Domain to decide
which best meets its needs.

 Whatever the
choice, the functional characteristics found in RFC 2979 should be provided.

Table 18:
References regarding Firewall Transversal

|  |  |
| --- | --- |
| FIRE-01 | Matthew Tanase, **Transparent,** Bridging and In-line Firewall Devices,October 15, 2003  Available from:  <http://www.securityfocus.com/infocus/1737> |
| FIRE-02 | Transparent Cisco IOS Firewall  Available from: http://www.cisco.com/univercd/cc/td/doc/product/software/ios123/123newft/123t/123t\_7/  gt\_trans.htm |

 

Table 19: Relevant
Specifications regarding Firewall Transversal

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 1579 | Firewall-Friendly FTP |  |
| RFC 1919 | Classical versus Transparent IP Proxies | Recommended Reading |
| RFC 2008 | Implications of Various Address Allocation Policies for Internet Routing | Recommended Reading |
| RFC 2401 | Security Architecture for the Internet Protocol |  |
| RFC 2505 | Anti-Spam Recommendations for SMTP MTAs |  |
| RFC 2543 | SIP: Session Initiation Protocol |  |
| RFC 2547 | BGP/MPLS VPNs |  |
| RFC 2764 | A Framework for IP Based Virtual Private Networks |  |
| RFC 2775 | Internet Transparency | Recommended Reading |
| RFC 2888 | Secure Remote Access with L2TP |  |
| RFC 2977 | Mobile IP Authentication, Authorization, and Accounting Requirements |  |
| RFC 2979 | Behavior of and Requirements for Internet Firewalls | Recommended |
| RFC 2993 | Architectural Implications of NAT | Recommended Reading |

 

## Identity Establishment Service

An identity establishment
(e.g. identity authentication) service is concerned with verifying proof of an
asserted identity. The implementation of the service must allow for 
multiple identity authentication mechanisms (e.g. identity tokens) to be utilized. Additionally, the service needs to
provide a mechanism to allow the information from various identity
tokens/identity authentication mechanisms to be electronically conveyed.

The requirement
that the Identity Establishment service be agnostic in regards to technology
can be easily demonstrated.  One Security Domain may make use of a User
ID/password combination as a identity token. Another Security Domain may
require the use of Kerberos based identity tokens.  It is the Security
Management Infrastructure (SMI) and the Security Domain’s security policies
that will determine the actual identity token(s) used and the mechanism(s)
through which they are conveyed.

Key definitions:

**identity
authentication:** The performance of tests to enable a [data processing](http://www.atis.org/tg2k/_data_processing.html) [system](http://www.atis.org/tg2k/_system.html)
to recognize entities. Note: An example of identity [authentication](http://www.atis.org/tg2k/_authentication.html) is the checking of a [password](http://www.atis.org/tg2k/_password.html)
or [identity token](http://www.atis.org/tg2k/_identity_token.html). [2382-pt.8]

**identity
token: 1.** A device, such as a metal [key](http://www.atis.org/tg2k/_key.html)
or [smart card](http://www.atis.org/tg2k/_smart_card.html), used for [identity authentication](http://www.atis.org/tg2k/_identity_authentication.html).
[After 2382-pt.8] **2.** [A] Smart card, metal key, or other physical object
used to [authenticate](http://www.atis.org/tg2k/_authenticate.html) identity. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

**identity
validation:** Tests enabling an [information system](http://www.atis.org/tg2k/_information_system.html)
to [authenticate](http://www.atis.org/tg2k/_authenticate.html) users or
resources. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99] 

### Identity Establishment for Physical Assets

Physical access control
should be based upon multi-factor Identity Establishment.  The use of
multi-factor authentication, using the appropriate technologies can provide a
significant security advantage above and beyond simple identity
cards.  Additionally, the selection and creation of physical access
control policies and procedures would needs to include the capability to manage
and revoke access privileges easily.  This would typically indicate the
need for some type of token/id that can be managed/changed.  However, if
only the picture matching the holder of the identity card determines access,
there is a high probability that such access control mechanisms can be
falsified.  Thus, to improve access security there should be another
security factor used in order to authorize access.

This “other-factor”
should be “something the individual knows” (e.g. username/password) or
combination code.  However, typically username/passwords or combination
codes can be compromised through observation or garbage diving. 
Therefore, it would be recommended that some type of electronic mechanism, with
verification/challenge be implemented.  The most widely deployed example
of this would be the use of a Smart-ID card (e.g. a card that electronically
authorizes the holder to enter a combination and that explicitly bound to the
identity of the holder) and a combination lock.  Only the proper Smart-ID
badge authorization allows the combination to be entered into the lock which
then enable access.  The side benefit of the use of such technology is
that an audit trail of access can be created electronically. 
Additionally, management issues (especially revocation of access privileges)
are eased since the Smart-ID card can be revoked thereby disallowing access.

Should a Security
Domain decide to perform electronic auditing of physical access (recommended),
then appropriate audit trail time-stamping techniques need to be utilized (see
the audit service section).

### Computational Resources

Identity
establishment, for computational resources, is directly related to the types of
credentials that are in use within a Security Domain.  The definition of
the credentials that IntelliGrid Architecture may be using may be found in the Credential Renewal
section (see page 23).  The credential types
used to establish identity are: addresses and address resolution,
username/passwords, smart cards, digital certificates, and biometric
identifications.

The issue with
computational resource identification establishment is that of architecting a
solution that creates a framework for authentication. Table 20 and Table 21
list relevant references and specifications that may aid in the construction of
such a framework within a security domain.

 

Table 20: General
References Regarding Identity Establishment and Identity Infrastructure

 

**A National-Scale Authentication
Infrastructure**. R. Butler, D. Engert, I.
Foster, C. Kesselman, S. Tuecke,
J. Volmer, V. Welch. *IEEE Computer*, 33(12):60-66, 2000.

 

**An Online Credential Repository for the Grid: MyProxy**. J.
Novotny, S. Tuecke, V. Welch. *Proceedings of the Tenth International Symposium on
High Performance Distributed Computing (HPDC-10)*, IEEE Press,
August 2001.

 

**A Community Authorization Service
for Group Collaboration**. L. Pearlman, V. Welch, I. Foster, C. Kesselman, S. Tuecke. *Proceedings of the IEEE 3rd International Workshop
on Policies for Distributed Systems and Networks*, 2002.

 

**X.509 Proxy Certificates for
Dynamic Delegation**. V. Welch, I. Foster, C. Kesselman,
O. Mulmo, L. Pearlman, S. Tuecke,
J. Gawor, S. Meder, F. Siebenlist. *3rd
Annual PKI R&D Workshop*, 2004.

 

**Introduction to Public Key
Technology and the Federal PKI Infrastructure,** **February 26, 2001****, NIST.**

**Available from:
http://www.cccure.org/Documents/PKI/NIST\_pkidraft.pdf**

 

Table 21: Relevant Specifications
regarding Identification Frameworks

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO/IEC 10181-2:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Authentication framework | Recommended |
| ISO/IEC 10181-4:1997 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework | Recommended |
| ISO/IEC 10181-1:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Overview | Recommended |
| ISO 10202-8:1998 | Financial transaction cards -- Security architecture of financial transaction systems | Recommended Reading |

 

### *Technological Assessment and Relevant Specifications*

The following
section discusses issues and potential general resolution to the issues
regarding the use of any particular identification mechanism. In general,
two-factor authentication is desired.

#### General Technologies

##### Address Resolution

The most prevalent issue in using address
resolution as an identification mechanism is address spoofing.  This
attack is easy to generate and is well documented.  Therefore, such a identification
mechanism should not be used on its own.  It must
be augmented with another factor to actually
establish the identity.

Address resolution
is a worthwhile qualifier for actions/information exchanges that are only
supposed to occur between certain peers.  However, this is not a
reasonable mechanism for inter-domain exchanges since neither domain controls
the other domain’s address allocation/changes.

##### Username/Password

This is a typical
mechanism employed by Web based interfaces (especially for customers
interfacing for retrieval of billing information).  However, the use of
cookies or password caches (e.g. the prompt to remember the username password)
represents an issue that should be addressed by the
addition of a challenge/response mechanism. The challenge
response should be user selectable/definable so that they can remember the
response when prompted.

##### Smart Cards

The references
given previously in this section give a large amount of guidance in the
selection of SMART-CARDS that can be used in the implementation of physical or
cyber access control.  The smart card industry embraces ISO 7816 as one of
the prevalent smart card specification and this is
the recommended base specification for smart cards.

However, ISO 7816
does not specify a programmatic interface to such cards that is portable. 
Therefore, it is recommended that the Java Card Platform Specification be used
in conjunction with ISO 7816 technology.

The remaining issue
is how much storage to deploy on the smart cards.  The Gartner Group
published the information found in Figure 4.  At this juncture there is no
recommendation in regards to the amount of storage to deploy.

Table 22: Relevant
Standards Concerning Smart Cards

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO/IEC 7816-1:1998 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 1: Physical characteristics |  |
| ISO/IEC 7816-10:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 10: Electronic signals and answer to reset for synchronous cards |  |
| ISO/IEC 7816-11:2004 | Identification cards -- Integrated circuit cards -- Part 11: Personal verfication through biometric methods |  |
| ISO/IEC 7816-15:2004 | Identification cards -- Integrated circuit cards with contacts -- Part 15: Cryptographic information application |  |
| ISO/IEC 7816-3:1997 | Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 3: Electronic signals and transmission protocols |  |
| ISO/IEC 7816-3:1997/Amd 1:2002 | Electrical characteristics and class indication for integrated circuit(s) cards operating at 5 V, 3 V and 1,8 V |  |
| ISO/IEC 7816-4:1995 | Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 4: Interindustry commands for interchange |  |
| ISO/IEC 7816-4:1995/Amd 1:1997 | secure messaging on the structures of APDU messages |  |
| ISO/IEC 7816-5:1994 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 5: Numbering system and registration procedure for application identifiers | Highly recommended reading as part of the management (e.g. User/Group Management service) |
| ISO/IEC 7816-7:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 7: Interindustry commands for Structured Card Query Language (SCQL) (available in English only) |  |
| ISO/IEC 7816-8:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 8: Security related interindustry commands |  |
| ISO/IEC 7816-9:2000 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional interindustry commands and security attributes |  |
| Java Card | Java Code Smart Card API | Can make use of ISO 7816 Based  smart cards. Referenced by Global Platform and ETSI. |
| Java Card | Java Card Platform Specification v 2.2.1    Available from:  http://java.sun.com/products/javacard/specs.html |  |
| NIST GSC-IS | The NIST Interagency Report 6887 - 2003 edition (Government Smart Card-Interoperability Specification) Version 2.1  Available from:  http://csrc.nist.gov/publications/nistir/nistir-6887.pdf | Recommended Reading. Specifies the use of ISO 7816 GSM based implementations. |
| Smart Card Alliance | Smart Card Primer    Available from: http://www.smartcardalliance.org | Recommended Reading |
| Smart Card Alliance | Privacy and Secure Identification Systems: The Role of Smart Cards as a Privacy-Enabling Technology ­     Available from: http://www.smartcardalliance.org | Recommended Reading |
| Smart Card Alliance | Government Smart Card Handbook    Available from: http://www.smartcardalliance.org | Recommended Reading. Specifies the use of ISO 7816 based implementations. |

 

if !vml?![](Anl_Security_Services_files/image009.jpg)endif?

Figure 4: Estimated
Smart Card Storage Costs

##### Digital Certificates

The industry
accepted digital certificate is an X.509 certificate.  This is the
certificate format that should be used by IntelliGrid Architecture when applicable.  There
are some issues in identifying a certificate:

·      
There is an issue in regards to how to uniquely identify a
certificate.  There are many fields that could be used, however only the certificate Thumbprint is truly unique.  All other
fields could be non-unique.  Therefore, it is the thumbprint that should be
used to identify and match certificates.

·      
Enunciation of lifetime expiration (see Credential Renewal service).

·       Policy
issues in regards to use will need to be addressed.  The NERC e-Marc
certificate policy discusses many of these issues. It is recommended that the
e-Marc policy be used as a basis for certificate usage.    
  
It is worthwhile to note that the NERC policy does not allow the same
certificate to be duplicated.  Should a security domain adopt this as a
policy, the number of certificates required (e.g. in the case of redundancy)
will be higher.

·      
A policy in regards to how applications should react in the case that an
in use certificate is revoked.  
  
Revocation is basically caused when the integrity of a certificate has been compromised
(e.g. the private certificate may have been stolen).  Since none of the
revocation protocols give a indication that could be used to determine if the
certificate was compromised prior to use, the safe option is to terminate use
of the certificate upon revocation.  This may cause information exchange
to be terminated if fail-over procedures are not made part of the policy.

 

Table 23: Public
Key Infrastructure (PKI) Related Specification/Standards

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| RFC 2898 | PKCS #5: Password-Based Cryptography Specification Version 2.0.     B. Kaliski. September 2000. |  |
| RFC 2985 | PKCS #9: Selected Object Classes and Attribute Types Version 2.0.      M. Nystrom, B. Kaliski. November 2000. |  |
| RFC 2986 | PKCS #10: Certification Request Syntax Specification Version 1.7.     M. Nystrom, B. Kaliski. November 2000. |  |
| RFC 3280 | Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile |  |
| ISO/IEC 9594-8:1998 | Information technology -- Open Systems Interconnection -- The Directory: Authentication framework | Definition of X.509 Certificate is found here. |
| ISO/IEC 9594-8:2001 | Information technology -- Open Systems Interconnection -- The Directory: Public-key and attribute certificate frameworks |  |
| X.521 | PKI - Digital certificates and certificate revocation lists profiles |  |
| NERC | Certificate Policy for the Energy Market Access and Reliability Certificate (e‑MARC) Program Version 2.4  Available from:  ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc |  |

##### Digital Signatures

Typically
considered a subset of Digital Certificates, as certificates are required in
order to digitally sign, these have their own benefit for identification
purposes.  In instances where bandwidth or packet size is a limiting
factor, a digital signature can be used in place of a certificate.

In IEC 61850, for
GOOSE, this signature, in conjunction with address
resolution would provide two-factor authentication if properly
implemented.  However, this raises the issue that:

·      Digital signatures should not repeat often in order to prevent spoofing. There
are several different interpretations in regards to what a digital signature
is.
  
It is recommended that RFC 2313 be used as the definitive definition for a
digital signature algorithm:  
  
*“For digital signatures, the content to be signed is first reduced
to a message digest with a  message-digest algorithm (such as MD5), and
then an octet string containing the message digest is encrypted with the RSA
private key of the signer of the content. The content and the encrypted message
digest are represented together according to the syntax in PKCS #7 to yield a
digital signature.”*
  
However, it is recommended that RFC 2437 be the actual Cryptography
specification used[[6]](Anl_Security_Services.htm#_ftn6)

 

Table 24: Relevant
Specifications for Digital Signatures

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| RFC 2313 | <http://www.armware.dk/RFC/rfc/rfc2313.html>PKCS #1: RSA Encryption Version 1.5 |  |
| RFC 2315 | PKCS #7: Cryptographic Message Syntax Version 1.5 |  |
| RFC 2437 | PKCS #1: RSA Cryptography Specifications Version 2.0 |  |

 

#### Biometrics

There is a large
body of biometric work occurring.  The standards development is largely
being performed in ISO JTC1 SC37.  The total scope of work can be obtained
from [www.jtc1.org](http://www.jtc1.org/). 
However, some of the major work items have been included in Table 25. The major
focus of ISO JTC1 SC37 is focused on the biometric aspects of fingerprints
and facial images.  However, from a practical perspective fingerprint
biometrics represents a much lower cost alternative than facial and therefore
would be recommended for IntelliGrid Architecture deployment.

It is also
suggested that the biometric data be encoded on a smart-card so that two-factor
authentication is achievable using the appropriate NISTIR 6529
specified/registered format.

The use of
biometric based authentication mechanisms is becoming acceptable due to the
cost of the technology becoming lower.  There are four biometric
technologies that have been or are being used:

·      
Voice:  Although this is a type of biometric identification, it has
proven to be weak since recording and replay of the key identification
phrase(s) could allow such an authentication system to be spoofed[[7]](Anl_Security_Services.htm#_ftn7).

·      
Fingerprint: There are now electronic mice and locks that are relatively
low cost that can make use of fingerprints as a biometric.  However, there
are multiple competing standards for the metrics that determine what
information needs to be stored (e.g. to represent a fingerprint).  It is
recommended that this technology be used due to its
cost/benefit ratio.

·      
Facial: Facial biometrics could prove to be the biometric technology of
the future.  However, current technology yields has proven to produce
false positives (e.g. identify one individual as being another). The technology
previously needed for facial scanning was difficult, but the technology is
migrating to WebCam like cameras that will lower the
cost of such biometrics. Based upon this trend, the federal government
announced its intent to produce passports with facial biometric information[[8]](Anl_Security_Services.htm#_ftn8).  
  
It is recommended that facial biometrics be considered once the federal system
is proven.

·      
Retinal/Iris pattern mathing: This biometric
is one of the most difficult to spoof, but also one of the most costly to
deploy.  The cost/benefit ratio is questionable within IntelliGrid Architecture
environment.

·      
Hand Geometry: This biometric is one of the most
difficult to spoof, but also one of the most costly to deploy.  The
cost/benefit ratio is questionable within IntelliGrid Architecture environment.

Biometric exchange
formats have now been coordinated under one governing umbrella, the
International Biometric Industry Association (IBIA, www.ibia.org).

Table 25: Relevant
References regarding Biometrics

|  |  |
| --- | --- |
| Global Analytic Information Technology Services | **Fingerprint Recognition**  **Available from:** <http://www.gaits.com/biometrics_fingerprint.asp> |
|  | **Ralph Gross, Quo Vadis Face Recognition? The current state of the art in Face Recognition**    **Available from:** <http://dagwood.vsam.ri.cmu.edu/FaceRecognition/> |
|  | **Philip E. Agre, Your Face is Not a Bar Code: Arguments Against Automatic Face Recognition in Public Places.** |
| ISO JTC1 SC37 | **SD 2 – Harmonized Biometric Vocabulary** |
| ISO JTC1 SC37 | **1.37.19784.1 BioAPI – Biometric Application Programming Interface** |
| ISO JTC1 SC37 | **1.37.19794 – Biometric Data Interchange Format** |
| ISO JTC1 SC37 | **1.37.1974.3 Biometric Data Interchange Format – Part 3: Finger Pattern Spectral Data** |
| ISO JTC1 SC37 | **1.37.1974.4 Biometric Data Interchange Format – Part 4: Finger Image Data** |
| ISO JTC1 SC37 | **1.37.1974.5 Biometric Data Interchange Format – Part 5: Face Image Data** |
| NISTIR 6529 | **Common Biometric Exchange File Format (CBEFF)**    **Available from: http://www.nist.gov/cbeff** |

 

Table 26: Relevant
Specification regarding Biometrics and Smart Cards

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| ISO/IEC 7816-11:2004 | Identification cards -- Integrated circuit cards -- Part 11: Personal verification through biometric methods | Recommended Reading |

 

#### Specific Technologies

##### Relational Databases

The use of
relational databases merits discussion in regards to identity
establishment.  The first issue that needs to be resolved is the
definition of what is a relational database.  For the purposes of this
document, relational databases shall be constrained to any database that
conforms to ANSI X3.135-1989 (SQL’89), ANSI X3.135-1992
(SQL’92), or ANSI X3-135-199x (SQL3- still under
development).

“The
basic security model of SQL consists of three entities: objects, actions, and
users. Objects are defined in the database schema. In SQL'89, the objects are
tables, views, columns of tables, and columns of views. In SQL'92, the objects
also include domains and assertions. In SQL3, objects will include user defined
constructs….

A
privilege is an authorization to a user of an action on an object. A privilege
is a 5-tuple:

(grantor,
grantee, object, action, grantable)….

….some
of these implementations, the user name and password make up the user
identification string in the SQL connect command and this string is passed in
plain text across the network. From a security point of view, that this string
is passed in plain text is not good practice.”[[9]](Anl_Security_Services.htm#_ftn9)

 

Obviously, the use
of plaintext being transmitted across a network IS NOT ACCEPTABLE. 
Therefore, it is recommended that encryption, preferably provided via TLS, be
used.

##### Web Based User Interfaces

There are many
current devices (e.g. the GE UR Relay and others) that embed Web servers that
provide a monitoring and configuration setting
interface.  These definitely need to be secured via some identification
mechanism.  Currently username/passwords are used without
challenge/response. 

It would be
recommended that these interfaces implement a
challenge/response mechanism or be converted to make use of SOAP Web
Services with the appropriate Digital Signature SOAP security (Certificate
based).  It is also recommended that the digital signature be used in
conjunction with encryption provided by TLS.

Table 27: Relevant
Technologies for Web Based User Interfaces

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| W3C | SOAP Security Extensions: Digital Signature | Recommended |

 

## Identity Mapping Service

The identity
mapping service provides the capability of transforming an identity which
exists in one identity domain into a identity within another identity domain.
It is worthwhile to note that there may be multiple
identity domains within a single Security Domain.  There is an additional
attribute to identity mapping, the mapping may result in
either a mapping of a individual into another set of credentials that represent
the individual (but for a different resource) or in a mapping to a role/group
based identity for the resource.

 As an
example, consider an identity in the form of an X.500 Distinguished Name (DN),
which is carried within a X.509v3 digital certificate. The combination of the
subject DN, issuer DN and certificate serial number may be considered to carry
the subject’s or service requestor’s identity. The scope of the identity domain
in this example is considered to be the set of certificates that are issued by
the certificate authority. Assuming that the certificate is used to convey the
service requestor’s identity the identity mapping service via policy may map
the service requestor’s identity to a identity which has meaning (for instance)
to the hosting environment’s local platform registry. The identity mapping
service is not concerned with the authentication of the service requestor;
rather it is strictly a policy driven name mapping service.

The Identity
Mapping can occur due to Credential Conversion or local/programmatic
reasons.  The major issues with Identity Mapping are very similar to the
issues in Credential Conversion: **There needs to be an audit mechanism inserted into the mapping process
so that the originator of the transaction can be identified if needed.**

### Technological Assessment and Relevant Specifications

Relevant
specifications and references may be drawn from the Identity Establishment,
Credential Conversion, and Firewall Transversal services.  In order to be
concise, they will not be repeated in this section.  This section will
only contain additional recommendation above and beyond the other service
recommendations.

#### Address Mapping

It is recommended that Network Address
Translation be used as part of the non-Transparent Firewall deployment. 
However, in the use of NAT or most non-Transparent firewalls, there is an issue
of providing a proxy for multiple “protected addresses” into the public address
space.  It is recommended that firewalls be evaluated for their capability
to proxy and map multiple addresses as it may save
deployment and management cost.

#### UserName/Password

Although there are
no relevant standards/specifications pertaining to this issue, the most natural
mapping service is through the use of single sign-on (SSO).  However, this
does not truly represent the true Identity Mapping (although it is credential
mapping).

#### Digital Certificates

See the discussion
in the Credential Conversion service discussion.

## Information Integrity Service

Ensure that unauthorized
changes made to messages or documents may be detected by the recipient. The use
of message or document level integrity checking is determined by policy, which
is tied to the offered quality of the service (QoS).

Key definitions:

**integrity:** [In [INFOSEC](http://www.atis.org/tg2k/_infosec.html),
the] quality of an [information
system](http://www.atis.org/tg2k/_information_system.html) (IS) reflecting the
logical correctness and [reliability](http://www.atis.org/tg2k/_reliability.html) of
the [operating
system](http://www.atis.org/tg2k/_operating_system.html); the logical
completeness of the [hardware](http://www.atis.org/tg2k/_hardware.html) and [software](http://www.atis.org/tg2k/_software.html)
implementing the [protection](http://www.atis.org/tg2k/_protection.html)
mechanisms; and the consistency of the [data](http://www.atis.org/tg2k/_data.html)
structures and occurrence of the stored data. Note that, in a formal [security](http://www.atis.org/tg2k/_security.html) [mode](http://www.atis.org/tg2k/_mode.html),
integrity is interpreted more narrowly to mean protection against unauthorized
modification or destruction of information. [INFOSEC-99]

The first thought, when it comes to
Integrity, is that it is the same issue as Confidentiality.  However, the
Confidentiality Service provides protection from information disclosure not the
detection of information modification.  It is the protection from
information modification that the Integrity Service represents.

In order to provide message integrity a
algorithm that generates a result similar to a CRC needs to executed and
imbedded in the message.  However, this alone will not guarantee integrity
as a man-in-the-middle attack could change the message, recalculate the CRC,
and then forward the message. 

In order to prevent man-in-the-middle
attacks, a digital signature is typically used on the CRC like result and both
are embedded in the message.  It is this digital signature “seal” that
actually prevents the attack.  Such signatures are typically referred to
as Message Authentication Codes (MACs) and it is
recommended that the Integrity Service be implemented through the use of such
techniques.

## Inter-Domain Security Service

This service represents the capability to
provide additional security services, as needed, in order to facilitate
inter-domain information exchanges.   These additional security
services may not typically be required for intra-domain exchanges

The additional security services that must be
provided for Inter-Domain security are:

·       Confidentiality

·      
Credential Conversion

·       Delegation

·       Firewall Transversal

·       Identity Mapping

·       Security against Denial of
Service

Additionally, a much more robust audit
mechanism should be instituted at the inter-domain boundaries.

## Non-Repudiation Service

This service represents the ability of a
security domain to provide proof that a given exchange action has
occurred.  This ability is used to resolve disputes with other entities
that claim that the action did not occur, thus non-repudiation.  In order
to provide this service, a strong audit service must be present within the security
domain.

Key definition:

**re****pudiation:**
In cryptosystems, the denial by one of the entities involved in a communication
of having participated in all or part of the communication.

In order to provide this service, strong
audit capabilities need to be in place for Identity Establishment, Access
Control, Credential Conversion, and Identity Mapping.  Without an
appropriate level of audit capability on these other services, non-repudiation
will not be able to be performed.

Non-repudiation is typically a manual process
of retrieving the relevant audit records, analyzing those records, creating a
report that summarizes those records and the conclusion.  Thus, strong
policies and procedures must be put in place to accomplish non-repudiation as
well. 

### Technological Assessment and Relevant Specifications

Table 28 shows the relevant specifications
regarding non-repudiation.  In order to provide the non-repudiation
service, it is suggested that a non-repudiation framework similar to what is
specified in ISO/IEC 10181-4 be created.  It is further recommended that
SAML be used and the non-repudiation capabilities of
SAML be integrated into the created framework.

Table 28: Relevant Specification regarding
non-repudiation

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| ISO 9735-5:2002 | Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 5: Security rules for batch EDI (authenticity, integrity and non-repudiation of origin) |  |
| ISO/IEC 10181-4:1997 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework | Recommended |
| ISO/IEC 13888-1:1997 | Information technology -- Security techniques -- Non-repudiation -- Part 1: General | Recommended Reading |
| ISO/IEC 13888-2:1998 | Information technology -- Security techniques -- Non-repudiation -- Part 2: Mechanisms using symmetric techniques |  |
| ISO/IEC 13888-3:1997 | Information technology -- Security techniques -- Non-repudiation -- Part 3: Mechanisms using asymmetric techniques |  |
| ISO/IEC TR 13335-5 | Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security |  |
| WC3 | XML Key Management Specification (XKMS 2.0) Bindings |  |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |

 

## Path Routing and QOS Service

This service represents the ability of a
security domain to applications with the ability to request that a set of
transactions be conveyed over a specific communication path with specific
Quality of Security (QS) being provided.  Such a service may be used in
conjunction with many of the other security services.

There are two major issues
that need to be resolved:

·      The ability to specify the
actual communication path that a given transaction will use.
This type of ability is a direct contradiction to the normal dynamic routing inherent
in most networks, thus normal network infrastructures may not be able to be
used.

·     The ability
to request a Quality of Security to be guaranteed over that path.

### Technological Assessment and Relevant Specifications

#### Communication Path Definition

Although there are several IETF RFCs
regarding the ability to perform this function (e.g. RFC 1940), few if any of
the operating system APIs allow the full path specification to occur.  In
reality, the source routing bit can be set TRUE and the packet will be
delivered to the peer with the path hop information
embedded within it.  Such a mechanism could
allow the receiver to determine if a packet was delivered over an
acceptable path, and this is a useful check.

However, the ability to actually pre-determine
the path that a packet will transverse falls upon manual configuration of
static routing.  It is the this static routing that can actually allow
policy to dictate what route a given communication packet will take. 
Typically, this is a configuration option in Firewalls or Operating
Systems.  Thus it is incumbent upon the SMI function to provide the
appropriate configuration.

#### Quality of Security

There are no known Quality of Security
standards/specifications available to allow packet routing based upon a
requested level of security.  Development of a similar specification to
RFC 2386 (Quality of Service based Routing) is recommended.

 

Table 29: Relevant Specifications for the
Path Routing Service

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| RFC 1102 | Policy routing in Internet protocols | Highly Recommended |
| RFC 1322 | A Unified Approach to Inter-Domain Routing |  |
| RFC 1940 | Source Demand Routing: Packet Format and Forwarding Specification (Version 1) | Highly Recommended |
| RFC 2386 | A Framework for QoS-based Routing in the Internet | Highly Recommended |
| RFC 2725 | Routing Policy System Security | Highly Recommended |

 

## Security Policy Service

The policy service and policy
processes/guidance can be found in [Security Policy](Anl_Security_Policies.htm). 

## Policy Exchange Service

Allow service requestors and providers to
exchange dynamically security (among other) policy information to establish a
negotiated security context between them. Such policy information can contain
authentication requirements, supported functionality,
constraints, privacy rules etc.

Typically, there has been no defined
framework or policy exchange mechanism available
that is technology neutral and therefore such exchanges have not occurred or
have been performed manually.  There are several issues that have
prevented the development of such a framework:

·      Agreement in regards to what
constitutes security policy varies.  Therefore, such an exchange mechanism
would need to provide basic attribute definitions and also allow for a large
amount of customization.

·      There has not been a single
secure and ubiquitous technology available over which to perform such an
exchange.

### Technology Assessment and Relevant Specifications

When analyzing how to exchange policies in IntelliGrid Architecture environment, the problem of having a ubiquitous technology has not been
solved.  There still does not appear to be a solution that can solve
policy exchange issues in the Transmission & Distribution environment
(especially serially connected devices), spanning to
databases, to web technology.  However, there is emerging
specifications in how to perform such exchanges when web services/SOAP
infrastructures are available. 

For policy exchanges via SOAP, it is
recommended that the WS-Policy, WS-PolicyAssertions,
and WS-PolicyAttachment specifications form the basis
of such exchanges.  It is also recommended that customizations be kept to
a minimum in order to maximize interoperability and interworkability.

Table 30: Relevant Specification regarding Policy
Exchange

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS | Web Services Policy Framework (WS-Policy)  Available from:  http://xml.coverpages.org/ws-policyV11.pdf | Recommended |
| OASIS | Web Services Policy Assertions Language (WS-PolicyAssertions)  Available from:    http://xml.coverpages.org/ws-policyassertionsV11.pdf | Recommended |
| OASIS | Web Services Policy Attachment (WS-PolicyAttachment)  Available from:  http://xml.coverpages.org/ws-policyattachmentV11.pdf | Recommended |

## Privacy Service

The privacy service is primarily concerned
with the policy driven classification of personally identifiable information
(PII). Service providers and service requestors may store personally
identifiable information using the Privacy Service. Such a service can be used
to articulate and enforce a Security Domain’s privacy policy. Allow both a
service requester and a service provider to define
and enforce privacy policies, for instance taking into account things like
personally identifiable information (PII), purpose of invocation, etc. (Privacy
policies may be treated as an aspect of authorization policy addressing privacy
semantics such as information usage rather than plain information access.).

Many may consider privacy equivalent to
confidentiality/encryption, however this is not true.  In reality, privacy
is an issue regarding the PII after a secure transfer of that information
occurs.  The issue relevant, mostly to web technology, is how to determine
in advanced if the privacy offered by a web site is sufficient.

### Technological Assessment and Relevant Documents

A review of relevant information reveals that
there are many well know legal/legislative aspects to privacy and disclosure of
that information.  However, there is little relevant work in regards to
being able to determine and enforce the level of privacy electronically. 
The sole exception, that has maturity, is the P3P
specification from W3C.  References PRIV-01 and PRIV-02 are
recommended reading to allow the SMI/policy services to determine if P3P can be
used/monitored within the Security Domain.

Other work in this are is highly recommended.

Table 31: References Regarding Privacy

|  |  |
| --- | --- |
| PRIV-01 | Web consortium backs P3P privacy standard  Available from: http://www.cnn.com/2002/TECH/internet/04/18/p3p.privacy.idg/ |
| PRIV-02 | Web Privacy Standard: It's a Start  Available from: http://www.pcworld.com/news/article/0,aid,94544,00.asp |

 Table 32: Relevant Specification regarding
Privacy

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| W3C | The Platform for Privacy Preferences 1.1 (P3P1.1) Specification  W3C Working Draft 27 April 2004 | Highly Recommended |
| Oblix | Guide to Regulatory Compliance and Privacy | Recommended |

## Profile Service (User Profile Service)

The profile service is concerned with
managing service requestor’s preferences and data
which my not be directly consumed by the authorization service.
This may be service requestor specific personalization data, which for example
can be used to tailor or customize the service requestor’s experience (if
incorporated into an application which interfaces with
end-users.) It is expected that primarily this data will be used by
applications that interface with a person. 

### Technological Assessment and Relevant Specifications

Research and experience indicates the web
user profiles are the trend.  To experience this, use any of the
commercial web portals (e.g. yahoo, msn, etc…).  These all offer the
ability to personalize the information displayed and the actual display
format.  However, it is doubtful that any of the current portal technologies make use of the Semantic Web specification.

It is recommended, when possible, that the
Semantic Web specification be utilized when possible.  If such an
implementation is not feasible or costly, it is recommended to implement based
upon some local means. 

Table 33: Relevant Specifications regarding
the Profile Service

|  |  |  |
| --- | --- | --- |
| **Identification Number** | **Name** | **Comment** |
| Semantic Web | Pervasive Computing Standard Ontology (PERVASIVE-SO) Guide -- Describing User Profile and Preferences    Available from: http://pervasive.semanticweb.org/doc/2004-01-ont-guide/part1/ | Highly Recommended |
| IEEE | IEEE Personal and Private Information (PAPI) draft standard |  |

## Quality of Identity Service

This service allows an entity to determine
the trust level associate with the identity being conveyed.  This is of
particular interest where the source Identity, of the original transaction, has
been mapped several times.

This service represents a specific capability
that could be viewed as a subset of the Identity Service.  However, technical evaluations of existing solutions indicate
that no solutions provide this ability and therefore are worthy of being
defined independently so that the service requirement is not lost.

This is a service that is not widely
recognized, although QID-01 makes a strong case for its need.  The basic
issue raised by QID-01 is that of the ability to trust an identity being
established if the identity has been mapped or its credentials converted
several times.  At a minimum, without a mechanism for originator
determination, there is a relevant issue.  However, originator
determination could be provided by and adequate audit mechanism, but this does
not assist the receptor of a transaction.  Thus there is a need to provide
a mechanism to allow the receptor to determine a level of trust based upon the
number of mappings that have occurred along the transaction path.

Table 34: References Relating to Quality of
Identity

|  |  |
| --- | --- |
| QID-01 | Audun Josang, An Algebra for Assessing Trust in Certification Chains, Telnor R&D  email: audun.josang@fou.telenor.no |

### Technological Assessment and Relevant Specifications

There are two aspects in regards to Quality
of Identity, the ability to determine the number of times that an identity has
been transformed, which is a superset of the number
of times that credentials have been converted. There are no relevant specifications/solutions
that can be applied to the generalized identity mapping
issue, as many of these mappings are local issues.  However, in the particular case of digital
certificate conversion, the SAML specification yields a possible solution.
However, the solution would require that attribute definitions and attribute
chaining be added to SAML’s use within IntelliGrid Architecture
environment. There are no such solutions for
username/password and it may be worthwhile to develop such a specification
based upon the SAML principles. For address based credentials, source routing
offers a potential solution (see Path Routing and QS service).

  

Table 35: Relevant Specification for the
Quality of Idenity Service

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS Security Technical Committee | Attribute Profiles for SAML 2.0  Available from:  http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf | Incomplete, but is on the correct track. |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf | Draft that is needed to establish identity within a SAML environment. |

## Security against Denial-of-Service

This service is for assisting in preventing a
denial of service.  This is not a service that can be invoked
programmatically, rather it is a service that must be designed into the
capabilities of a Security Domain or the implementations deployed within the
domain.

Key definitions:

**denial of service: 1.** The prevention
of authorized [access](http://www.atis.org/tg2k/_access.html) to resources or the delaying of [time](http://www.atis.org/tg2k/_time.html)-critical [operations](http://www.atis.org/tg2k/_operations.html). [2382-pt.8] **2.** The result of any
action or series of actions that prevents any part of an [information system](http://www.atis.org/tg2k/_information_system.html) (IS) from functioning. [[INFOSEC](http://www.atis.org/tg2k/_infosec.html)-99]

The
overall issue is to understand what can allow denial-of-service and then to
take steps to mitigate the causes.  There are several general categories
of denial-of-service attacks that need to be well understood:

·      
Resource exhaustion: Resource exhaustion is a denial-of-service attack
that causes required resources to be un-available for the intended use when a
valid transaction needs to be processed. The recent SYN FLOOD attacks represents
a well known denial-of-service attack.  
  
Resources that can be exhausted are virtual connections, memory, serial ports,
TCP ports, etc.  However these could be generalized into two categories:
connectivity resources and computational resources. 

·      
Buffer overflow: This type of attack causes a memory overrun to occur
within a computational resource.  The end result is typically the
computational process terminates or becomes unstable.  In reality, this
attack exploits poorly implemented programs that actually allow for the overrun
to occur without being properly trapped.  Recent examples of this type of
attack are the PING OF DEATH and some attacks on SNMP.

·      
Protocol oversights: In some protocols, not all state transitions may be
defined.  Exploitation of such oversights could allow a denial of service
attack to cause a protocol deadlock situation.  
  
As an example, from STD 62 (SNMP):

“**Denial
of Service**

*A
Security Model need not attempt to address the broad range of attacks by which
service on behalf of authorized users is denied.  Indeed, such
denial-of-service attacks are in many cases indistinguishable from the type of
network failures with which any viable management protocol must cope as a
matter of course.*”

Basically
is a statement that no DOS countermeasures need to be taken within the
specification.  This is typical of most standards.

·      
Improper Coding Practice:  Both the Buffer Overflow and Protocol
Oversight threats are sub-categories of the improper coding practice
category.  However, this category includes improper use of semaphores,
threads, etc.  that could be utilized to decrease performance/resource
available to the point that a valid transaction could not be processed in a
timely manner.

### Technological Assessment and Relevant Specifications

In
order to provide a denial-of-service attack protection, inter-domain connection
points need to be well-designed and monitored.

For
connectivity resources, it is recommended that timeouts be implemented that are
based upon valid traffic being transmitted/received through the connection
point.  Additionally, it is recommended that
through policy or coding practice that a peer remote be limited to the
number of connectivity resources that it is allowed to consume.

For
protocol oversights, it is recommended that prior to implementation the
protocol(s) are analyzed for vulnerabilities and that these be addressed during
the implementation phase. It is recommended that appropriate coding methodology
be employed to prevent CPU resource exhaustion as well as protocol oversight
vulnerabilities.

It is
also recommended that as part of the policy/SMI of a security domain that
implementations are tested for vulnerabilities with tools that are publicly
available.

Table
36: Relevant Specifications regarding Denial-of-Service

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| ISO/IEC 17799:2000 | Information technology -- Code of practice for information security management |  |
| ISO/IEC TR 13335-1:1996 | Information technology -- Guidelines for the management of IT Security -- Part 1: Concepts and models for IT Security |  |
| ISO/IEC TR 13335-2:1997 | Information technology -- Guidelines for the management of IT Security -- Part 2: Managing and planning IT Security |  |

 

## Security Assurance Management Service

Explicitly
recognize the need for manageability of security functionality within IntelliGrid Architecture
security model. For example, identity management, policy management, key management,
and so forth. The need for security management also includes higher-level
requirements such as anti-virus protection, intrusion detection and protection,
which are requirements in their own rights but are
typically provided as part of security management.

### Technological Assessment and Relevant Specifications

Security
assurance is part of a Security Domain’s policy and SMI.  It is
recommended that ISO/IEC 15408-3:1999
be the guideline for determine and assessing such a policy.

Table
37: Relevant Specifications regarding Security Assurance

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| RFC 2401 | Security Architecture for the Internet Protocol |  |
| RFC 2196 | Site Security Handbook |  |
| RFC 2350 | Expectations for Computer Security Incident Response |  |
| ISO/IEC 15408-1:1999 | Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 1: Introduction and general mode |  |
| ISO/IEC 15408-2:1999 | Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 2: Security functional requirements |  |
| ISO/IEC 15408-3:1999 | Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 3: Security assurance requirements | Highly Recommended |

 

## Security Protocol Mapping Service

Security
protocol mapping services enable distributed security protocols to be
transparently mapped onto native platform security services for participation by
platform resource managers not implemented to support the distributed security
authentication and access control mechanism.

### Technological Assessment

To
date there has been no definition of abstract security
services and their parameters.
The security work found in this section actually defines a set of services,
but further modeling is required in fully specify the parameters that are
conveyed within those services.

The
issue involving the ability to map to different communication technologies will be mitigated if a full abstract model
of IntelliGrid Architecture security services can be developed.

## Security Service Availability Discovery Service

Security discovery
provides a mechanism for an entity to discover what security services are
available for its use. In particular, a
Security Domain should provide a mechanism for an entity to discover what security services are available for its use
across to other Security Domains.

Within
the IntelliGrid Architecture, such a service would be required for Inter-Domain usage
where a-priori knowledge is not available.  It would also be a mandatory
service if Quality of Security routing became a reality.

### Technological Assessment and Relevant Specifications

Although
there is no immediately usable technology to accomplish this service, it is
recommended that the WS-Policy series be extended to provide this
capability.  It should be fairly straightforward to model security service
availability as policy (e.g. the Policy Attachment may need to be
extended).  At a minimum, the information required
to be conveyed needs to be determined in advance of attempting to adopt
WS-Policy.

Since
the discovery service is needed inter-domain, it is reasonable to attempt to
make use of Web Services at the domain interconnect points to provide this
capability.

Table
38: Potentially Relevant Specifications in regards to Security Capability
Discovery

| **Identification Number** | **Name** | **Comment** |
| --- | --- | --- |
| OASIS | Web Services Policy Framework (WS-Policy)  Available from:  http://xml.coverpages.org/ws-policyV11.pdf |  |
| OASIS | Web Services Policy Assertions Language (WS-PolicyAssertions)  Available from:    http://xml.coverpages.org/ws-policyassertionsV11.pdf |  |
| OASIS | Web Services Policy Attachment (WS-PolicyAttachment)  Available from:  http://xml.coverpages.org/ws-policyattachmentV11.pdf |  |

 

## Single Sign on Service

Relieve
an entity having successfully completed the act of authentication once from the
need to participate in re-authentications upon subsequent accesses to
OGSA-managed resources for some reasonable period of time. This must take into
account that a request may span security domains and hence should factor in
federation between identity domains and mapping of
identities. This requirement is important from two perspectives: a) It places a
secondary requirement on an OGSA-compliant implementation to be able to
delegate an entity’s rights, subject to policy (e.g., lifespan of credentials,
restrictions placed by the entity) b) If the credential material is delegated
to intermediaries, it may be augmented to indicate the identity of the
intermediaries, subject to policy.

This
service is a local combination of  the Credential Conversion and Identity
Mapping services.

## Trust Establishment Service

This
service represents the ability of one resource to determine if its peer can be
trusted.  In order to establish trust, well known identities and security
policies must be used.  Additionally, if inter-domain trust establishment
requires an analysis of the security policies and procedures of the peer
security domain.

Key
definitions:

**trust:** In [cryptology](http://www.atis.org/tg2k/_cryptology.html) and
cryptosystems, that characteristic allowing one entity to assume that a second
entity will behave exactly as the first entity expects. Note: Trust may apply
only for some specific function. The critical role of trust in the [authentication](http://www.atis.org/tg2k/_authentication.html)
framework is to describe the relationship between an authenticating entity and
a [certification
authority](http://www.atis.org/tg2k/_certification_authority.html); an
authenticating entity must be certain that it can trust the certification
authority to create only valid and reliable certificates. [After X.509]

Trust establishment is implemented through
the Identity Establishment and Quality of Identity Services.

 

Table 39: Relevant Information regarding
Trust Establishment

|  |  |
| --- | --- |
| DOD | DOD 5200.28-STD  Trusted Computer System Evaluation Criteria |
| DOD | DOD 5200.28-STD 1991 Trusted Database Management System Interpretation of the Trusted Computer System Evaluation Criteria |
