# Security Policy Issues

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Policies.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security Policy Issues

The Security Domain’s policy service is concerned
with the management of policies. The aggregation of the
policies contained within and managed by the policy service comprises a
Security Domain’s policy set. This service is also responsible for the
enforcement of the domain’s policy for intra-domain and inter-domain exchanges.
The policy service may be thought of as another
primitive service, which is used by the authorization, audit, identity mapping
and other services as needed. The issues addressed include the following:

|  |  |
| --- | --- |
| * [General Policy   Service Process](Anl_Security_Policies.htm#General_Policy_Service_Process) * [Security Requirements of Assets](Anl_Security_Policies.htm#Security_Requirements_of_Assets) * [Risk   Assessment/Analysis](Anl_Security_Policies.htm#Risk_Assessment/Analysis) * [Key Management, PKI   Infrastructure Policy, and Other PKI Issues](Anl_Security_Policies.htm#Key_Management,_PKI_Infrastructure_Policy,_and_Other_PKI_Issues) * [Intrusion   Detection](Anl_Security_Policies.htm#Intrusion_Detection) * [Audit   Service and Non-Repudiation Policy Issues](Anl_Security_Policies.htm#Audit_Service_and_Non-Repudiation_Policy_Issues) * [Credentials   and User Accounts Policy Issues](Anl_Security_Policies.htm#Credentials_and_User_Accounts_Policy_Issues) | * [Personal Identification   Policy Issues](Anl_Security_Policies.htm#Personal_Identification_Policy_Issues) * [URL Addresses](Anl_Security_Policies.htm#URL_Addresses) * [Username/Passwords](Anl_Security_Policies.htm#Username/Passwords_) * [Smart Cards](Anl_Security_Policies.htm#Smart_Cards) * [Digital Certificates](Anl_Security_Policies.htm#Digital_Certificates) * [Virus Protection](Anl_Security_Policies.htm#Virus_Protection) * [User   and Group Account Management](Anl_Security_Policies.htm#User_and_Group_Account_Management) * [Setting and Verifying User Accounts Service](Anl_Security_Policies.htm#Setting_and_Verifying_User_Accounts_Service) |

## General Policy Service Process

The policy service is a process through which
a Security Domain determines its risks vs. costs in order to protect critical
assets.  The policy development must encompass:

* A **Requirements** analysis process
  which is used to determine the critical assets that need protection,
  security needs of the Security Domain, technological choices for implementation, security management and monitoring
  requirements, audit capability, and non-repudiation capability.
* The **Implementation** process that
  monitors and tests the policies as they are implemented.  If there are
  problems detected during implementation, the policy should be revised and
  requirements should be revisited.
* The **Monitoring** process is
  responsible for the detection of security attacks, detection of security
  breeches, and the performance of the installed security infrastructure.
  This process is critical to the overall effectiveness of security.
* The **Analysis** process is
  responsible for determining when the deployed security measures need to be
  re-evaluated.  This re-evaluation may be required due to environment,
  legal, or internally developed metrics.

There is a relevant body of work that can be
found in **EPRI Report 1008988**, ***Scoping Study on Security Processes and
Impacts***.  The following is a summarization of that work.

## Security Requirements of Assets

A policy must determine what assets need to
be protected, determine what attacks need to be mitigated, how to mitigate the
attacks including technology and procedural, and how to detect attempted
attacks.

* **Asset
  Protection**:  In order to determine which assets need to be protected, all
  aspects of the “value” of an asset needs to be determined. 
  This means that legal, community good will, asset value, and cascade
  effects (if an attack did compromise a particular asset) need to be taken into
  account.  Since it is not possible to secure every asset in the
  infrastructure, it is recommended that the high risk or high-value assets be
  protected first.
* Determining
  wha**t Attacks to Mitigate: T**he requirements process must determine what is
  the cost/benefit/probability of a successful attack and what form such an
  attack might take.  The higher the probability of success indicates the
  higher need for mitigation.
* **Mitigation
  Strategies:** The security services, discussed in this report, provide
  suggestions in regards to how to mitigate many of the threats.  It is up
  to each security domain (SMI) to determine the best method to mitigate the
  attack and then write the appropriate policies to reflect that intent.
* **Attack
  Detection:** Since there is no absolute security, detection of an attempted
  attack is an important objective of any security policy.  For each asset
  being secured, a mechanism for detecting attempted/successful attacks needs to
  be part of the policy and it MUST be implemented and monitored on a constant
  basis.

As part of the requirement process, 
ISO/IEC 15408 (e.g. the standardized version of the NIST Common Criteria) should be used as a basis for the technological requirements assessment and
determining threats and mitigation strategies. The requirements phase of policy development
must also take into account risk assessment.

## Risk Assessment/Analysis

“The classical definition of Risk Analysis is
one that describes it as a process to ensure that the security controls for a
system are fully commensurate with its risks.”[[10]](Anl_Security_Policies.htm#_ftn10)

Translated, this means that the amount of
security deployed should be related to the overall asset value (including
collateral assets that could be effected[[11]](Anl_Security_Policies.htm#_ftn11)). 
Thus, risk analysis provides a mechanism to determine which assets should be
protected immediately (based upon relative worth) and not
require that all Security Domain assets be secured.

Some of the other documented benefits of
performing risk assessment are:

* Provides a
  means to cost justify security investments.
* Breaks down business boundaries and build business relationships.
  Business management would be responsible to determine the security risk level
  that would be tolerable for a particular asset.  IT/Security staff would
  need to work with the management team to determine the cost/solution. 
  Based upon both factors, a cost/security ratio could be developed and used as a
  metric.
* Risk Analysis
  allows security to be analyzed from a business needs perspective and not just
  from a technological solution basis.
* The team
  risk analysis activity raises the security awareness to a greater number of
  personnel.
* Provides a
  mechanism to evaluate security in a “consistent” manner.
* Facilitates
  communication between different business entities.

### External Legal Directive Impacts

The policy developed for a particular domain
must take into account binding legal and industry directives as well as
industry best practices.  In regards to the maintenance of security
policy, the impact of binding directives needs to be evaluated/re-evaluated
when directives or best practices are issued from an authoritative and binding source.

***Example***:
A state entity issues a binding directive to supply a given class of
security service for certain financial exchanges.  This directive would
need to be evaluated by the SMI against existing policy and security
services/technologies for the domain. If the directive could not be met with
the existing security domain policy/infrastructure, the domain’s policy should
be revised in order to accommodate the directive.

#### Fault Tolerance

Security issues can impact the fault tolerant aspect of systems.  There are
two(2) prevalent issues that need to be considered in determining a fault
tolerance policy:

* System
  Availability (see page 55).
* Denial of
  Service created by successful security attacks.

Policies and system designs must accommodate
these issues.

### Implementation

As
the selected assets are secured, tests should be executed to make sure
that the created policies and deployed technologies actually perform as
desired.  If not, new policies reflecting new requirements need to be
generated.  Therefore, test procedures need to be considered as part of
the policy development cycle.

As an example, the policies and procedures for physical access should be tested on an
un-announced basis.  This should be written into the policy as well as the
maximum re-test interval allowed.  Additionally, the expected results of
such tests should be documented.  If the expected results are not
obtained, an analysis of the causes for not achieving the expected results
needs to occur.  If the analysis indicates that the policy is in error,
then the policy needs to be revised.

### Analysis

Policies and procedures need to be written to
state how often re-analysis of the existing policies and security
infrastructure needs to occur (given no successful attack or repeated attempted
attacks being detected).  The policy for re-analysis needs to recognize
that shifts in the world political environment (just think of before 9/11
versus now) and technology advances all need to be
taken into account.

![](IECSA_VolumeIV_AppendixA_files/image015.gif)

Figure 5: General trend is security
vulnerabilities (extracted from EPRI Report 1008988)

Figure 5 shows the probability of a
successful attack.  It depicts a high probability prior to security
measures being implemented.  At the time the security measures are
implemented, this represents the “lowest” probability of successful attack if
the security process has worked properly.  However, the figure accurately
reflects that over time the probability of successful
attack increases.  Thus it is important to understand and specify the
periodicity of security re-evaluation in order to keep the probability of
successful attack at an acceptable level.

Thus the aforementioned represent the general
types of problems that must be faced when developing an overall Security Domain
security policy.  However, there are technology specific policies that
also need to be addressed.

Note: ISA-99, Integrating Electronic Security
into the Manufacturing and Control Systems Environment is a document worth
reading.  It discusses, in more detail, the aspects of policy development.

 

## Key Management, PKI Infrastructure Policy, and Other PKI Issues

Note: This section is intended as a simple
discussion of the issues regarding PKI.  There are more authoritative
documents available from NIST or NERC.

The purpose of the Public Key Infrastructure
is to allow the establishment of Trust through the binding of encryption keys
(typically “public” keys) and identities. In order to understand how PKI works,
it is first important to that PKI to understand the three prevalent types of encryption: symmetric, asymmetric, and
public/private.

·     **Symmetric
encryption** refers to the fact that both peers have the knowledge and use the
same encryption key.  Since both peers have and use the same key,
symmetric encryption does not lend itself to unambiguous bindings (e.g. one key
to a particular application/entity), thus symmetric encryption should not be
used as the Trust establishment binding (e.g. should not be used within a PKI
environment).

·     **Asymmetric
encryption** refers to the fact that each entity has its own key.  Unlike
symmetric encryption, asymmetric keys can allow for unambiguous identity
establishment.  However, since cooperating peers would need to have
knowledge of the other peer’s key, it is often difficult to protect the
identifying key.  Although asymmetric keys could facilitate a PKI
environment, the use of such keys for identity binding is not recommended since
the keys must be disseminated/configured on multiple peers and therefore a
prone to being compromised.

·     **Public/Private
key encryption** works on the basis that the use of the public key allows the
decryption of information encrypted with the private key.  Conversely,
information encrypted with the public key can only be decrypted with the
private key. It represents a specialization of asymmetric encryption.

The
use of public/private key encryption can be used for two purposes: encryption
and digital signatures.

![](IECSA_VolumeIV_AppendixA_files/image019.gif)![](IECSA_VolumeIV_AppendixA_files/image017.gif)

Figure 6: Simplified diagram of
Public/Private Key encryption and Digital Signature

Figure 6 shows in order to Node A to encrypt
data to be sent to Node B, the use of Node B’s public key is required.  It
also shows that only the holder of Node B’s private key can decrypt the
information (neglecting encryption attacks).  Likewise, the Digital
Signature exchange shows that Node A’s signature is decoded by Node B through
the use of Node A’s public key.  Thus for both encryption and digital
signatures, only public keys need to be exchanged and therefore
it becomes easier to control and protect the private keys.  Thus
public/private key based PKI systems should be the preferred approach.

Obviously, it is critical to have a robust
PKI infrastructure:

* Create the appropriate
  bindings between public/private keys and identification.
  The typical mechanism for the bindings is through a digital X.509 certificate.
  A public certificate that includes the public key is created, and an equivalent
  is created as the “private certificate” that contains both the private and
  public keys.  It is the creation of these two “certificates” that are
  typically the responsibility of a Certificate Authority (CA).  
    
  The protection of the public certificate/key is not that important, but the
  protection of the private key/certificate is. It is the responsibility of the
  CA to provide adequate protection during the generation process and to protect
  this information even if the certificate has been sent to the actual user.  
    
  Since the CA is the “root” source of the certificate, it is important that the
  CA also provide Certificate Revocation List (CRL) ability so that compromised
  or stolen certificates can be revoked.
* The user of
  a “private certificate” must provide security mechanism to protect the private
  information. 
  The actual mechanism for Security Domain/user archiving is a local issue, but
  great care needs to be taken during the policy establishment to be able to
  quickly and properly detect if there has been un-authorized access to the
  Security Domain private certificates.  The policy must include the
  appropriate mechanism/procedures for reporting the compromised certificate and
  revoking its use locally.
* Even though
  the public certificates do not have the same criticality, the Security Domain
  policy should address the procedures for releasing the public certificate for
  use.
* A mechanism
  for tracking the lifetime expiration date in advance to actual expiration needs
  to be addressed.
* Policies/procedures
  for replacement and renewal of older certificates (prior to expiration) or
  revoked certificates needs to be developed.

 

Of particular concern in IntelliGrid Architecture, and the
utility industry, is how to provide an appropriate revocation capability for a
Security Domain.  There are several design criteria for such an
infrastructure:

* The
  infrastructure must be able to accommodate revocations of certificates that
  have been issued from more than one CA.  
    
  There is no central CA for the utility industry, or the world, and it does not
  appear that there is movement towards such an entity.  Even NERC, in its
  e-Marc program, intends to allow certificates from multiple (although
  “certified”) CAs to be used.  If a insecure CA
  is selected, problems can occur as is demonstrated in the following example

Example: (from
<http://www.iona.com/support/docs/e2a/asp/5.0/corba/ssl/html/OpenSSL2.html>)

![](IECSA_VolumeIV_AppendixA_files/image020.png)

* Many of the
  certificate using computational resources will not be allowed direct access to
  the Internet that would be required in order to query the CRL of a particular
  CA.
  Additionally, CRLs can be large and can consume
  bandwidth and be computationally intensive.
* An ability
  to determine if a particular Certificate has been revoked.
  The X.509 Internet Public Key Infrastructure Online Certificate Status Protocol
  – OCSP (RFC 2560) allows such a capability.  It is worthwhile to note that
  OCSP is a request/response-oriented protocol (e.g. the certificate user must
  request to check if a certificate has been revoked).

However, the fact that OCSP is
request/response means that there is an issue of timeliness in revocation
information.  However such a protocol/procedure does not exist
today.  In a future time, it could be envisioned that a central Security
Domain revocation server (not a CRL server) could be created with the following
attributes:

* Allows
  certificate users to register that certificates are in the user certificate
  cache.
* The
  Revocation Server would query the CAs CRL servers and
  process the revocation list(s).
* Based upon
  the CRL processing, the Revocation Server would notify the certificate user
  that the particular certificate has been revoked.
* Optionally,
  such a Revocation Server could alert Security Domain management that a
  certificate of a particular user is about to expire so that corrective action
  could be taken.
* Optionally,
  such a Revocation Server could respond to OCSP requests so that newly configured
  certificates could be validated as still being valid.

It is believed that work on such an entity is
needed to allow more timely delivery of revocation information and to allow
automation of such tasks.

## Intrusion Detection

Any developed policy must include the ability
to detect and attempt to prevent intrusion. There are no authoritative
technologies that are available today.  There are two issues that need to
be resolved:  How to detect that an intrusion has occurred and how to
report/coordinate the fact that there has been an intrusion.

Intrusion detection is a local issue and may
vary based upon the communication media/technology/protocol that is being
employed.  There are two types of intrusions to be considered: passive
(e.g. eavesdropping) and active where the intruder is actively attempting to
access a particular computational resource. 

Passive
intrusion is difficult if not impossible to detect.  Thus intrusion
prevention becomes a key issue to prevent this type of intrusion.  Passive
intrusion (e.g. eavesdropping by a network analyzer) can be prevented through
the use of encryption and monitoring/controlling network access (e.g. managed
switches).  In a radio environment, intrusion can’t be prevented, but
eavesdropping can be prevented through the use of encryption that prevents a
real security issue of information disclosure.

The active intruder can be detected through
means that are local to the resource.  However there needs to be a
framework in which the detection can be coordinated, verified, and
reported.  There are no relevant standards in regards to intrusion
detection frameworks. However, the closest is the Communication in the Common
Intrusion Detection Framework (CDIF).    

The following are key attributes of an
integrated intrusion detection technology/framework that should be considered:

* A detection
  framework must be able to communicate over the wire in a standardized manner.
* A intrusion
  detection technology must be able to securely contact the proper peer components.
* There must be a mechanism to locate peer components in a secure manner.
* There must be a mechanism for verifying each partner’s authenticity and access
  privileges.
* Additionally,
  an intrusion detection technology should integrate with the audit
  framework/technology.

|  |  |
| --- | --- |
| INT-01 | CDIF Working Group - Communication in the Common Intrusion Detection  Framework v 0.7  Available from:  <http://gost.isi.edu/cidf/drafts/communication.txt> |
| INT -02 | Protocol Anomaly Detection for Network-based Intrusion Detection  Available from: <http://www.sans.org/rr/papers/30/349.pdf> |
| INT-03 | Designing and Implementing a Family of Intrusion Detection Systems  Available from:  http://www.cs.ucsb.edu/~vigna/pub/  2003\_vigna\_valeur\_kemmerer\_esec03.pdf |

Table 40: References regarding Intrusion
Detection

The common thread throughout the references, and
others, is that to perform network based intrusion detection, intrusion
detection component/agents must be able to interact and exchange information
creating a distributed intrusion detection system.

## Specific Policy Issues and Recommendations per Service

Some security services merit specific policy
recommendations that were not expressed within the security service section
explicitly.

### Audit Service and Non-Repudiation Policy Issues

The major policy issues that effect non-repudiation
is the time-frame for which a valid audit trail can be generated.  It is recommended that audit information be
archived and available for no less than a three (3) month period of time.

### Credentials and User Accounts Policy Issues

There are some general issues for credentials
that apply to many of the credential types that have been discussed.

·      How many
credentials of a given type will a user be allocated?
In general, it is recommended to allocate a single physical credential of
each type (e.g. Smart Card, Personal ID card, Token Generator).  This recommendation even applies to Digital
certificates.  Such a policy will minimize the effort required for
management, renewal, and revocation (if needed).

·     Upon
revocation, a policy/mechanism needs to be developed to detect and enunciate if
that credential, even a network address, has been used after revocation.  The policy must
address the expected detection timeframe allowed and the type of response
expected from SMI. 
Note: Typically, the smaller the detection window the higher the cost to
implement.

·     The period
at which credentials need to be renewed/modified.

·     The
determination of an appropriate non-use time that causes an investigation and
potential revocation of the credential if the credential has not been used
within that non-use time period.

·     Determine a
policy for revoking the credentials.

### Personal Identification Policy Issues

The design and management of Personal Identification
cards will impact the ability to enforce physical access control. It is recommended that such ID cards require
a photograph of the person and also have an area where an easy modification can
be made.  As a minimum, it is suggested that these
modifications occur on a monthly basis and be a multi-colored/foil label with a
valid through date printed on it.

### URL Addresses

In order to provide an infrastructure for
monitor and revocation of addresses, it is important to address the two (2)
main address types: statically and dynamically assigned.

#### Statically Assigned Addresses

For
statically address assigned computation resources:

·     The policy
should require that the physical (e.g. Media Access Control address or
equivalent) be recorded.  The policy must also allow for tracking changes
in that address.

·     That the
communication segment has an Access Control List (ACL) that prevents off
segment communication if the address is revoked.
It is recommended that this policy be enforced through the
deployment of SNMP manageable switches. So that an address can be associated
with a switch port, and upon revocation the port is disabled.

·     The
policy/implementation should allow for continuous monitoring/detection
of addresses that should not be present and that have not been used for a
policy specified period of time.
The policy/implementation infrastructure must provide the technology to detect
usage and determine periods of inactivity.

·     A
policy/procedure is needed that allows renewal/reactivation of the address if
the address has been revoked incorrectly.

·     A
policy/procedure is needed that allows re-assignment of a previously assigned
addressed.

#### Dynamically Assigned Addresses

For dynamically addressed computation
resources: 

·       The policy
should prohibit dynamically assigned addresses from being used as single-factor
identification credentials.  The probability of incorrect identity
establishment is high; therefore it should not be allowed.

·       The policy
should not allow off-segment communication unless a challenge-response is
performed.

·       The
policy/procedures/SMI must be able to provide an audit record/trail regarding
the address assigned to the challenge/response so that actual identification of
the user can occur.

·       The
challenge-response should be on an individual basis (e.g.
no group assigned passwords).

### Username/Passwords

There are a couple of recommendations in
regards to the use of usernames/passwords:

* In general,
  a particular user should be allowed one and only one password for a given
  computational resource.
* The size of
  the password, and its required characters/format needs to be specified and
  enforced. The first question that needs to be answered is the character set. 
  It is recommended that upper, lower, punctuation, and numeric
  characters be allowed. This increases the possible permutations of
  passwords dramatically (example assumes ANSI Character Set):

  > Number upper case
  > characters:                    24  
  > Number of lower case characters:                 24  
  > Number of numeric
  > characters:                    
  > 10  
  > Number of punctuation characters[[12]](Anl_Security_Policies.htm#_ftn12):           30

  Based upon a four(4) character password, then number of possible permutations
  is shown to be:

  > Permutations if upper case
  > only:                                   331,776  
  > Permutations if upper and lower case
  > :                       5,308,416  
  > Permutations if upper, lower, numeric case
  > :            
  > 11,316,496  
  > Permutations if  using all characters:                       
  > 59,969,536

  It should be noted that some computational resources may not be able to accept
  punctuation characters within passwords, but it is strongly recommended to
  include upper, lower, and numeric characters within the
  password character set.

Specifically, the policy
needs to determine the minimum size of a password in order to provide adequate
protection. 
Unfortunately, many existing policies assume that password size is the
criteria: however protection comes from the number of possible permutations. 
***Therefore, it is suggested that the minimum number of password permutations be
approximately 1 trillion for any computational resource.***
This means, based upon allowed characters, the minimum password size is :

Table 41: Recommended Minimum Password size

|  |  |
| --- | --- |
| **Character Set Allowed** | **Recommended Password Size** |
| Upper Case Characters Only | 9 |
| Upper/lower case characters only | 8 |
| Upper/lower/numeric characters | 7 |
| All characters | 6 |

It is further recommended that seven (7) characters
be the absolute minimum.

·      The policy
needs to require at least one numeric character, if numeric characters are
allowed.  Additionally, the policy should not allow numeric characters as
the last character of the password.  Such a policy will eliminate the
natural tendency to append a number to a base password when revision of the
password is required.

·      The policy needs to address the period of time that requires
password changing.

### Smart Cards

Smart cards can be used to contain personal
identification information (e.g. username/passwords), digital certificates,
biometric information, and other types of information.  Therefore, the
credential types they contain typically address the credential aspects of a
smart card. 

The major policy issue, specifically related
to smart cards, is the development of policies/procedures relating to the
serialization of the smart cards.

### Digital Certificates

There is a major issue regarding digital
certificates, and that is the handling of revocation. Certificate Authorities (CAs) typically maintain Certificate Revocation Lists (CRLs) that are updated on a twenty-four
(24) hour interval.  A certificate that has been placed on a CRL is no
longer trustworthy and therefore should not be useable.

Policies and procedures should be developed
to specify a
periodicity to check the CAs CRLs
and how to disseminate this information within the security domain.
The NERC DEWG has expressed a major concern in this area and further policy
study in order to develop a specific recommendation
is warranted.

### Virus Protection

The developed policy should address virus and
worm protection.   It is suggested that the following NIST guide be
used as part of the policy development.

NIST, NIST SP 500-166, August 1989, Computer
Viruses and Related Threats: A Management Guide, Springfield, Springfield, VA:
NTIS.

### User and Group Account Management

This service allows the ability to define, assign,
organize, control and maintain mapping for user and group identifiers within
the security domain.  There is no authoritative technology that is
applicable to providing this service and therefore must be rigorously addressed
via policy.

However, there are
several relevant articles that may prove of assistance.

Table 42: Relevant Articles concerning User
and Group Account Management

|  |  |
| --- | --- |
| Oblix | Best Practices in Extranet Portals and Identity Management |
| Oblix | Mastering Supply Chain Partnerships: Achieving Core Business Objectives through Effective Identity Management  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Lowering eBusiness Administrative Costs with Effective Group Management  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | An Overview of Federated Identity Architecture  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Creating a Secure and Unified eBusiness Infrastructure  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | An Overview of Federated Identity Architecture  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Oblix | Creating a Secure and Unified eBusiness Infrastructure  Available from: http://www.oblix.com/resources/whitepapers/index.html |
| Computerworld | Five rules for top-notch user management and provisioning  Available from:  http://www.computerworld.com/securitytopics/security  /story/0,10801,90407,00.html?f=x10 |

If thoroughly reviewed, the articles clearly
indicate that the basic premise of User and Group Management has its
foundations in Identity management (e.g. Identity Establishment and Mapping
services).  Thus, the technological recommendations from those security
services needs to be part of the User and Group Management service. 
Additionally, the following are key recommendations from the literature:

·      **Deprecation**
or changing of all default accounts is needed.
This would mean that for Operating Systems, that the default user accounts
should be removed or a least have the credentials changed (e.g.
passwords).  This should include ALL user accounts, including remote diagnostic
accounts.

·      **Unused
Accounts**
that are not frequently used should be de-activated.
One of the most prevalent issues is determining the usage of a particular user
account.  The Security Domain’s policy should specify a period of
inactivity that causes user accounts to become inactive (e.g. no longer valid
but available to be renewed/re-activated).

·      **Group
Accounts** should be granular enough to provide appropriate access privilege
restriction.
At a general level, the following privileges need to be addressed:

> **Remote Login**: Does the User belong to a group that has the privilege to make
> use of the computational resource remotely.   
>   
> **Execute**: Does the User belong to a group that has the privilege to execute a
> particular program/application.   
>   
> **Access**: Does the User belong to a group that has the privilege to access the
> information contained in a computational resource (e.g. file, database,
> etc…).  There is a need for further granularity based upon the particular
> instance of file/resource.  
>   
> **Modification**: Does the User belong to a group that has the privilege to modify
> the information contained in a computational resource.  Similar
> granularity to Access is typically needed.  
>   
> **View**: Does the User belong to a group that is allowed to view the existence of a
> particular resource (e.g. the ability to have a directory with particular files
> appearing in the directory response).

·      Within the IntelliGrid Architecture, there are two additional privileges that need to
be considered.  These are privileges that typically relate to interactions
with field devices and not business level computational resources, although
they may be needed in some cases (e.g. User Management): Configuration and
Control Privileges.

> **Configuration**: Does the user belong to a group that has the privilege to change
> the configuration of a computational resource.  There may be further
> granularity required based upon the types of configuration supported by the
> computational resource (e.g. users, protective schemes, control settings,
> initial values, setting groups, etc.).  
>   
> **Control**: Does the user belong to a group that has the privilege to change
> /control real-time process aspects of a computational resource.  Further
> granularity may need to be provided based upon the class of controllable
> resources available on a computational resource.

·       Within a
Security Domain, there needs to be centralized management and storage of the
user/account information, typically in a directory like environment.

·       **Single
Sign-On** is a typical objective of intra-domain management.

This service can be subdivided into a policy
part and an actual security service: Setting and Verifying User Accounts. 

### Setting and Verifying User Accounts Service

This service is for assigning and validating
authority given to a user or a group of users in accessing/utilizing specific
enterprise resources.  There is no authoritative technology to
evaluate for this service.  However, from an abstract security service
level such a service needs to exist.  The service needs to provide the
functionality of:

·       Lifecycle
management of user and group account.  This includes the ability to
create, renew, deprecate, modify, and delete users and groups.

·       Credential
Management is required so that passwords, certificates, etc. can be replaced/renewed/deprecated as required.
