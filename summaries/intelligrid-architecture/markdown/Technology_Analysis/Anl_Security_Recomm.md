# Security Tech Overview

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Recomm.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security Technology Overview

Security is a
complicated and multi-faceted topic.  The
interdependencies of overall Security Domain security policy, security
implementations, and communication technologies make the analysis and
suggestion of specific technologies difficult due to many degrees of freedom in
the analysis of the overall problem. 
This clause reflects some of the recommendations, whose specifics may be
found in the Security Appendix.  This
clause is NOT 100% inclusive of all of the recommendations found in the
Security Appendix, but instead highlights some significant technologies and
issues that need to be addressed.

### Interdependencies

The typical
non-ending cycle of security processes (e.g. Assessment, Policy Creation,
Deployment, Training, and Audit) can be directly correlated to the Security
Domain functions (e.g. Access Control, Trust, Confidentiality, Integrity,
Security Policy, Security Management Infrastructure, and Training) as defined
within the Appendix.  However, there have
been approximately twenty-six (26) various security services identified.  Some of these services are directly involved
in the electronic protection of information/assets.  Other services are more business process
related, although required in order to have a robust security infrastructure.

Of these
twenty-six services, further analysis showed that the services themselves are
inter-related.  Based upon this
information, it is now possible for a user to determine what security services
need to be addressed.  However, one major
dimension to the problem has yet to be discussed.

Based upon the
analysis, several of the security services appear to be mandatory in the case
of inter-domain exchanges whereas there is one service that appears to be
optional (e.g. at the discretion of the security domain).  Table
3 shows the services whose use varies based upon
inter/intra domain usage.

|  |  |  |
| --- | --- | --- |
| Table 3: Security Services vs. Security Domain Usage | | |
| Security Service | Intra-Domain | Inter-Domain |
|  |  |  |
| Confidentiality | o | m |
| Credential Conversion | o | m |
| Delegation | o | m |
| Firewall Transversal | o | m |
| Identity Mapping | o | m |
| Inter-Domain Security | Not Applicable | m |
| Path Routing and QOS | o | o |
| Privacy | o | o |
| Security Against Denial of Service | o | m |
| Security Protocol Mapping | o | m |
| Single Sign-On | o | Not Applicable |

 

The following are
the most interesting, or controversial conclusions:

if !supportLists?·      
endif?The use of single sign-on is a security domain
specific issue and by definition is not usable in a inter-domain exchange.  This is due to the fact that the credentials
would need to be converted at the domain boundary. Thus it could look/feel like
single sign-on from the initial security domain was still being used, but at
the peer-domain there would need to be a conversion thereby typically to a
group identity.

if !supportLists?·      
endif?The use of confidentiality, within a security
domain, is the choice of the security domain. 
However, it is clear that for inter-domain exchanges, the ability to
provide a mechanism of confidentiality is important and mandatory.

if !supportLists?·      
endif?Denial of Service protection is mainly a
inter-domain issue.  Thus, it is more
important to protect the exposed inter-domain interfaces than all of the
intra-domain interfaces from denial-of-service attacks.

if !supportLists?·      
endif?The ability to guarantee privacy is an optional
security service.  The use of a privacy
policy/exchange may be dictated via policy that may typically be driven via
legal issues.

### Service Specific Technological Recommendations

The following is a
summary of some of the more interesting technological recommendations.  For individual security service technological
recommendations, or details, please refer to the Security Appendix.

#### Identity Establishment Service

There are several
interdependencies between the identity establishment, identity mapping, and
quality of identity services.  Based upon
these interdependencies, it is suggested that the Security Assertion Markup
Language (SAML) Version 2 be used when possible.

The SAML
technology is the only identified technology that appears to be extensible so
that the issues regarding Identity Quality could be solved.  It is worthy to note that these attribute
extension do not currently exist, but are possible to create.

#### Confidentiality

There were two
mechanisms identified that can provide some level of confidentiality:
encryption and communication path selection (e.g. being able to select the
communication path through trusted parties). 
For encryption, it is recommended that the Advanced Encryption Algorithm
(e.g. FIPS 197 of 2001) be used when possible. 
Additionally, it is recommended that a minimum key size of 128 bits be
utilized with 256 bits being preferable.

Some readers may
be concerned about the processing power required to perform the AES encryption. 
However, recent tests of the proposed Secure ICCP/TASE.2 profile that
makes use of either DES or AES 256 with TLS showed that AES required slightly less CPU than DES. 
However, there is significant improvement in the level of protection.

The communication
path selection, currently, is a configuration issue (e.g. static routing,
etc.).  However, it is envisioned that
such a service could be created in the future in conjunction with the Policy
Exchange service that has been specified.

#### Policy

The Policy service
is more of a business process service. 
However, it is required to be well developed, understood, and
implemented in order to create a viable security domain.  Identified issues that need to be addressed include,
but are not limited to:  requirements
gathering, monitoring for intrusions, monitoring for computational environment
changes that may put the developed policies at risk, timeliness of response,
and the issue of residual risk.

#### Audit

The general recommendation
for the audit service is to tailor it in accordance with the Security Domain’s
logging capabilities.  There was no
particular standard/technology that could be identified, however there are
authoritative specifications on how to create a realizable audit
frameworks.  It is recommended that
ISO/IEC 10164 be used as the basis for such a framework. Additionally, 21 CFR Part 11 should be an objective of any audit
system implemented by a security domain.

There are some
policy issues that must be decided, as they impact resources:  the amount of time that audit records will be
available and the mechanism to prove that such records have not been tampered
with during audit trail creation.

### Communication Technology Specific Recommendations

There are other views
to the security technology issue besides via security services.  One typical question is what security
technologies should be used in regards to a particular communication
technology.  This section attempts to
summarize some of the recommendations based upon a communication technology
view.  Table
0‑4 provides a summary of the recommendations in regards
to Identity Establishment and Confidentiality

 

|  |  |  |
| --- | --- | --- |
| Table 0‑4: Summary of recommendations for Identity Establishment and Confidentiality | | |
| Communication Technology | Confidentiality | Identity Establishment |
| Web | Secure HTTP (e.g. HTTPS) | X.509 Certificates  Username/Password with challenge if certificate usage is not possible. |
| WI-FI | WPA 2 and 802.11i  (AES encryption) | Address resolution in conjunction with Username/password. |
| Ethernet Local Area Network (LAN) | None to be provided at the physical/Media Access Control level. | None to be provided at the physical/Media Access Control level.  Recommended strategy for restricting off-LAN segment exchanges. |
| Dial-up | None to be provided by modem technology. | Recommended username/password and challenge mechanism if no other available.  Recommended against dial-back modems due to management difficulties. |
| TCP/IP | TLS | TLS |

 

In general
two-factor identity establishment has been recommended.  This indicates that there needs to be a
revocable token (e.g. smart card, time token generator, etc…) used in order to
allow ease of management.  However, with
all identity establishment technologies, the policy established within a
security domain MUST address the renewal/re-evaluation interval so that
re-issuing of an identity is well controlled and understood.

### Technologies that need to be created

Several of the security services and communication
technologies have no technological solution to their security issues.  Some of the identified problem areas are:

* There is no standard for audit record format or
  a standardized mechanism to retrieve and aggregate such records.
* There is no
  standard through which to enforce physical access.  Since physical access is presumed in
  many security scenarios, security domains must develop their own
  proprietary mechanisms for authorizing physical access and detecting
  attempted/successful intrusions.
* There is no
  technological mechanism through which to exchange security service
  definitions/availability from one security domain to another.  It has been recommended that extensions
  to the recommended policy exchange mechanism be evaluated for this
  purpose.  However, there is no
  ubiquitous policy exchange technology available.
* There is no
  technological mechanism through which to request a given communication
  path or quality of security. 
  However, there are technologies available to determine the path
  that a given communication packet traveled (e.g. source routing).  However, more disturbing is there
  appears to be no authoritative work regarding the use of security as a
  quality of service to be provided.
* Of major concern,
  is there is no well-defined methodology or technology to disseminate
  Certificate Revocation Lists (CRLs) within a Security Domain.  Additionally, there has been only
  minimal work in regards to the actual behavior from a communication
  perspective once a in-use certificate has been revoked.  It has been suggested that such a
  revocation should result in the communication being associated with the
  revoked certificate be terminated. 
  However, such an implementation could result in loss of
  communication at an inopportune time and therefore must be carefully
  considered as part of the security domain’s security policy.
