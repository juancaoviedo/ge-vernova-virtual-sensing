# Security Policies

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Security_Policies.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Security Policies

The
Security Domain’s policy service is concerned with the management of policies.
The aggregation of the policies contained within and managed by the policy
service comprises a Security Domain’s policy set. This service is also
responsible for the enforcement of the domain’s policy for intra-domain and
inter-domain exchanges. he policy service may be thought of as another
primitive service, which is used by the authorization, audit, identity mapping and other services as needed.

**General Process**

The
policy service is a process through which a Security Domain determines its
risks vs. costs in order to protect critical assets. The policy development
must encompass:

·       A **Requirements**
analysis process which is used to determine the critical assets that need
protection, security needs of the Security Domain, technological choices for
implementation, security management and monitoring requirements, audit
capability, and non-repudiation capability.

·       The **Implementation**
process that monitors and tests the policies as they are implemented. If there
are problems detected during implementation, the policy should be revised and
requirements should be revisited.

·       The **Monitoring**process is responsible for the detection of security attacks, detection of
security breeches, and the performance of the installed security
infrastructure. This process is critical to the overall effectiveness of
security.

·       The **Analysis**
process is responsible for determining when the deployed security measures need
to be re-evaluated. This re-evaluation may be required due to environment,
legal, or internally developed metrics.

There
is a relevant body of work that can be found in EPRI Report 1008988, Scoping
Study on Security Processes and Impacts. The following is a summarization of
that work.

**Security Policy Requirements**

A
policy must determine what assets need to be protected, determine what attacks
need to be mitigated, how to mitigate the attacks including technology and
procedural, and how to detect attempted attacks.

·       Asset
Protection: In order to determine which assets need to be protected, all
aspects of the “value” of an asset needs to be determined. This means that
legal, community good will, asset value, and cascade effects (if an attack did
compromise a particular asset) need to be taken into account. Since it is not
possible to secure every asset in the infrastructure, it is recommended that
the high risk or high-value assets be protected first.

·       Determining what
Attacks to Mitigate: The requirements process must determine what is the
cost/benefit/probability of a successful attack and what form such an attack
might take. The higher the probability of success indicates the higher need for
mitigation.

·       Mitigation
Strategies: The security services, discussed in this report, provide
suggestions in regards to how to mitigate many of the threats. It is up to each
security domain (SMI) to determine the best method to mitigate the attack and
then write the appropriate policies to reflect that intent.

·       Attack
Detection: Since there is no absolute security, detection of an attempted
attack is an important objective of any security policy. For each asset being
secured, a mechanism for detecting attempted/successful attacks needs to be
part of the policy and it MUST be implemented and monitored on a constant
basis.

As
part of the requirement process, ISO/IEC 15408 (e.g. the standardized version
of the NIST Common Criteria) should be used as a basis for the technological
requirements assessment and determining threats and mitigation strategies.

The
requirements phase of policy development must also take into account risk
assessment.

**Risk Assessment/Analysis**

“The
classical definition of Risk Analysis is one that describes it as a process to
ensure that the security controls for a system are fully commensurate with its
risks.”[[5]](Tech_Security_Policies.htm#_ftn5)

Translated,
this means that the amount of security deployed should be related to the
overall asset value (including collateral assets that could be effected[[6]](Tech_Security_Policies.htm#_ftn6)). Thus, risk analysis provides a
mechanism to determine which assets should be protected immediately (based upon
relative worth) and not require that all Security Domain assets be secured.

Some
of the other documented benefits of performing risk assessment are:

·       Provides a means
to cost justify security investments.

·       Breaks down
business boundaries and build business relationships.

Business
management would be responsible to determine the security risk level that would
be tolerable for a particular asset. IT/Security staff would need to work with
the management team to determine the cost/solution. Based upon both factors, a
cost/security ratio could be developed and used as a metric.

·       Risk Analysis
allows security to be analyzed from a business needs perspective and not just
from a technological solution basis.

·       The team risk
analysis activity raises the security awareness to a greater number of
personnel.

·       Provides a
mechanism to evaluate security in a “consistent” manner.

·       Facilitates
communication between different business entities.

**Fault Tolerance**

Security
issues can impact the fault tolerant aspect of systems. There are two(2) prevalent issues that need to be considered in
determining a fault tolerance policy:

·       System
Availability.

·       Denial of
Service created by successful security attacks.

Policies
and system designs must accommodate these issues.

**Implementation**

As
the selected assets are secured, tests should be executed to make sure that the
created policies and deployed technologies actually perform as desired. If not,
new policies reflecting new requirements need to be generated. Therefore, test
procedures need to be considered as part of the policy development cycle.

As
an example, the policies and procedures for physical access should be tested on
an un-announced basis. This should be written into the policy as well as the
maximum re-test interval allowed. Additionally, the expected results of such
tests should be documented. If the expected results are not obtained, an
analysis of the causes for not achieving the expected results needs to occur.
If the analysis indicates that the policy is in error, then the policy needs to
be revised.

**Analysis**

Policies
and procedures need to be written to state how often re-analysis of the
existing policies and security infrastructure needs to occur (given no
successful attack or repeated attempted attacks being detected). The policy for
re-analysis needs to recognize that shifts in the world political environment
(just think of before 9/11 versus now) and technology advances all need to be
taken into account.

![](../IECSA_Volumes/IECSA_VolumeIV_AppendixD_files/image005.gif)

Figure 3: General trend is security vulnerabilities
(extracted from EPRI Report 1008988)

Figure
5 shows the probability of a successful attack. It depicts a high probability
prior to security measures being implemented. At the time the security measures
are implemented, this represents the “lowest” probability of successful attack
if the security process has worked properly. However, the figure accurately
reflects that over time the probability of successful attack increases. Thus it
is important to understand and specify the periodicity of security
re-evaluation in order to keep the probability of successful attack at an
acceptable level.

Thus
the aforementioned represent the general types of problems that must be faced
when developing an overall Security Domain security policy. However, there are
technology specific policies that also need to be addressed.

Note:
ISA-99, Integrating Electronic Security into the Manufacturing and Control
Systems Environment is a document worth reading. It discusses, in more detail,
the aspects of policy development.

**PKI Infrastructure Policy and Issues**

Note:
This section is intended as a simple discussion of the issues regarding PKI.
There are more authoritative documents available from NIST or NERC.

The
purpose of the Public Key Infrastructure is to allow the establishment of Trust
through the binding of encryption keys (typically “public” keys) and
identities. In order to understand how PKI works, it is first important to that
PKI to understand the three prevalent types of encryption: symmetric,
asymmetric, and public/private.

·       Symmetric
encryption refers to the fact that both peers have the knowledge and use the
same encryption key. Since both peers have and use the same key, symmetric
encryption does not lend itself to unambiguous bindings (e.g. one key to a
particular application/entity), thus symmetric encryption should not be used as
the Trust establishment binding (e.g. should not be used within a PKI
environment).

·       Asymmetric
encryption refers to the fact that each entity has its own key. Unlike
symmetric encryption, asymmetric keys can allow for unambiguous identity
establishment. However, since cooperating peers would need to have knowledge of
the other peer’s key, it is often difficult to protect the identifying key.
Although asymmetric keys could facilitate a PKI environment, the use of such
keys for identity binding is not recommended since the keys must be disseminated/configured on multiple peers and therefore a
prone to being compromised.

·       Public/Private
key encryption works on the basis that the use of the public key allows the
decryption of information encrypted with the private key. Conversely,
information encrypted with the public key can only be decrypted with the
private key. It represents a specialization of asymmetric encryption.

if !vml?![](https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/IECSA_VolumeIV_AppendixD_files/image006.png)endif?The use of public/private key encryption can be used for two purposes:
encryption and digital signatures.

if !vml?![](https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/IECSA_VolumeIV_AppendixD_files/image007.jpg)endif?Figure 4:
Simplified diagram of Public/Private Key encryption and Digital Signature

Figure
6 shows in order to Node A to encrypt data to be sent to Node B, the use of
Node B’s public key is required. It also shows that only the holder of Node B’s
private key can decrypt the information (neglecting encryption attacks).
Likewise, the Digital Signature exchange shows that Node A’s signature is
decoded by Node B through the use of Node A’s public key. Thus for both
encryption and digital signatures, only public keys need to be exchanged and
therefore it becomes easier to control and protect the private keys. Thus
public/private key based PKI systems should be the preferred approach.

Obviously,
it is critical to have a robust PKI infrastructure:

·       Create the
appropriate bindings between public/private keys and identification.  
  
The typical mechanism for the bindings is through a digital X.509 certificate.
A public certificate that includes the public key is created, and an equivalent
is created as the “private certificate” that contains both the private and
public keys. It is the creation of these two “certificates” that are typically
the responsibility of a Certificate Authority (CA).  
  
The protection of the public certificate/key is not that important, but the
protection of the private key/certificate is. It is the responsibility of the
CA to provide adequate protection during the generation process and to protect
this information even if the certificate has been sent to the actual user.  
  
Since the CA is the “root” source of the certificate, it is important that the
CA also provide Certificate Revocation List (CRL) ability so that compromised
or stolen certificates can be revoked.

·       The user of a
“private certificate” must provide security mechanism to protect the private
information.   
  
The actual mechanism for Security Domain/user archiving is a local issue, but
great care needs to be taken during the policy establishment to be able to
quickly and properly detect if there has been un-authorized access to the
Security Domain private certificates. The policy must include the appropriate
mechanism/procedures for reporting the compromised certificate and revoking its
use locally.

·       Even though the
public certificates do not have the same criticality, the Security Domain
policy should address the procedures for releasing the public certificate for
use.

·       A mechanism for
tracking the lifetime expiration date in advance to actual expiration needs to
be addressed.

Policies/procedures
for replacement and renewal of older certificates (prior to expiration) or
revoked certificates needs to be developed.

Of
particular concern in IntelliGrid Architecture, and the utility industry, is how to provide an
appropriate revocation capability for a Security Domain. There are several
design criteria for such an infrastructure:

·       The
infrastructure must be able to accommodate revocations of certificates that
have been issued from more than one CA.  
  
There is no central CA for the utility industry, or the world, and it does not
appear that there is movement towards such an entity. Even NERC, in its e-Marc
program, intends to allow certificates from multiple (although “certified”) CAs
to be used. If a insecure CA is selected, problems can occur as is demonstrated
in the following example

Example:
(from http://www.iona.com/support/docs/e2a/asp/5.0/corba/ssl/html/OpenSSL2.html)

![](https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/IECSA_VolumeIV_AppendixD_files/image008.wmz)

·       Many of the
certificate using computational resources will not be allowed direct access to
the Internet that would be required in order to query the CRL of a particular
CA.  
  
Additionally, CRLs can be large and can consume bandwidth and be computationally
intensive.

·       An ability to
determine if a particular Certificate has been revoked.  
  
The X.509 Internet Public Key Infrastructure Online Certificate Status Protocol
- OCSP (RFC 2560) allows such a capability. It is worthwhile to note that OCSP is
a request/response-oriented protocol (e.g. the certificate user must request to
check if a certificate has been revoked).

However,
the fact that OCSP is request/response means that there is an issue of
timeliness in revocation information. However such a protocol/procedure does
not exist today. In a future time, it could be envisioned that a central
Security Domain revocation server (not a CRL server) could be created with the
following attributes:

·       Allows
certificate users to register that certificates are in the user certificate
cache.

·       The Revocation
Server would query the CAs CRL servers and process the revocation list(s).

·       Based upon the
CRL processing, the Revocation Server would notify the certificate user that
the particular certificate has been revoked.

·       Optionally, such
a Revocation Server could alert Security Domain management that a certificate
of a particular user is about to expire so that corrective action could be
taken.

·       Optionally, such
a Revocation Server could respond to OCSP requests so that newly configured
certificates could be validated as still being valid.

It
is believed that work on such an entity is needed to allow more timely delivery
of revocation information and to allow automation of such tasks.
