# Security Risk Assessment

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Risk_Assessment.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security Risk Assessment

## Power System Operations and Security

if !vml?![](Anl_Security_Risk_Assessment_files/image002.jpg)endif?
Figure 1:
August 14, 2003 Blackout (***NOAA
processed the data from the Defense Meteorological Satellite
Program. Please credit NOAA/DMSP)***

In the power
industry, the focus has been almost exclusively on implementing equipment
that can keep the power system reliable. Until recently, communications and
information flows have been considered of peripheral importance. However,
increasingly the information infrastructure that supports the monitoring and
control of the power system has come to be critical to the reliability of
the power system. With the exception of the initial power equipment problems
in the August 14, 2003 blackout, the on-going and cascading failures were
almost exclusively due to problems in providing the right information to the
right place within the right time.

Communication protocols are one of the most critical
parts of power system operations, responsible for retrieving information
from field equipment and, vice versa, for sending control commands. Despite
their key function, to-date these communication protocols have rarely
incorporated any security measures, including security against inadvertent
errors, power system equipment malfunctions, communications equipment
failures, or deliberate sabotage. Since these protocols were very
specialized, “Security by Obscurity” has been the primary approach. After
all, only operators are allowed to control breakers from highly protected
control center. Who could possibly care about the megawatts on a line, or
have the knowledge of how to read the idiosyncratic bits and bytes the
appropriate one-out-of-a-hundred communication protocols. And why would
anyone want to disrupt power systems?

However, security by obscurity is no longer a valid
concept. In particular, the electricity market is pressuring market
participants to gain any edge they can. A tiny amount of information can
turn a losing bid into a winning bid – or withholding that information from
your competitor can make their winning bid into a losing bid. And the desire
to disrupt power system operations can stem from simple teenager bravado to
competitive game-playing in the electrical marketplace to actual terrorism.

It is not only the market forces that are making
security crucial. The sheer complexity of operating a power system has
increased over the years, making equipment failures and operational mistakes
more likely and their impact greater in scope and cost. In addition, the
older, “obscure” communications protocols are being replaced by
standardized, well-documented protocols that are more susceptible to hackers
and industrial spies.

As the power industry relies increasingly on
information to operate the power system, two infrastructures must now be
managed: not only the **Power System Infrastructure**, but also the **Information Infrastructure**. The management of the power system
infrastructure has become reliant on the information infrastructure as
automation continues to replace manual operations, as market forces demand
more accurate and timely information, and as the power system equipment
ages. Therefore, the reliability of the power system is increasingly
affected by any problems – either deliberate security attacks, or just
ordinary failures, malfunctions, and mistakes – that the information
infrastructure might suffer.

if !vml?![](Anl_Security_Risk_Assessment_files/image004.gif)endif?
if !vml?![](Anl_Security_Risk_Assessment_files/image006.jpg)endif?
Figure 2: Two Infrastructures Must Be Managed,
Not Just One

## Overview of the Security Process

Protection and securing of networked communications,
intelligent equipment, and the data and information that are vital to the
operation of the future energy system is one of the key drivers behind
developing an industry-level architecture.  Cyber security faces substantial
challenges both institutional and technical from the following major trends:

·        
Need for greater levels of integration with a variety of
business entities

·        
Increased use of open systems based infrastructures that will 
comprise the future energy system

·        
The need for appropriate integration of existing or “legacy”
systems with future systems

·        
Growing sophistication and complexity of integrated
distributed computing systems

·        
Growing sophistication and threats from hostile communities

 Security must be planned and designed into systems
from the start.  Security functions are integral to the designs of systems.
Planning for security, in advance of deployment, will provide a more
complete and cost effective solution.  Additionally, advanced planning will
ensure that security services are supportable (may be cost prohibitive to
retrofit into non-planned environments.  This means that security needs to
be addressed at all levels of the architecture.

As shown in Figure 3,
security is an ever evolving process and is not static.  It takes continual
work and education to help the security processes keep up with the demands
that will be placed on the systems.  Security will continue to be a race
between corporate security policies/security infrastructure and hostile
entities.  The security processes and systems will continue to evolve in the
future.  By definition there are no communication connected systems that are
100% secure.  There will be always be residual risks that must be taken into
account and managed.  Thus, in order to maintain security, constant
vigilance and monitoring are needed as well as adaptation to changes in the
overall environment.

The process depicts five high level processes that
are needed as part of a robust security strategy.  Although circular in
nature, there is a definite order to the process:

if !vml?![](Anl_Security_Risk_Assessment_files/image008.jpg)endif?
Figure 3: General Security Process –
Continuous Cycle

**Security Risk Assessment** – Security risk
assessment is the process of assessing assets for their security
requirements, based on probable risks of attack, liability related to
successful attacks, and costs for ameliorating the risks and liabilities.
The recommendations stemming from the security requirements analysis leads
to the creation of security policies, the procurement of security-related
products and services, and the implementation of security procedures.

The implication of the circular process is that a
security re-assessment is required periodically.  The re-evaluation period
needs to be prescribed for periodic review via policy. However, the policy
needs to continuously evaluate the technological and political changes that
may require immediate re-assessment.

**Security Policy** – Security policy generation
is the process of creating policies on managing, implementing, and deploying
security within a Security Domain. The recommendations produced by security
assessment are reviewed, and policies are developed to ensure that the
security recommendations are implemented and maintained over time.

**Security** **Deployment** – Security
deployment is a combination of purchasing and installing security products
and services as well as the implementation of the security policies and
procedures developed during the security policy process. As part of the
deployment aspect of the Security Policies, management procedures need to be
implemented that allow intrusion detection and audit capabilities, to name a
few.

**Security Training** – Continuous training on
security threats, security technologies, corporate and legal policies that
impact security, Security measures analysis is a periodic, and best
practices is needed.  It is this training in the security process that will
allow the security infrastructure to evolve.

**Security** **Audit (Monitoring) –** Security
audit is the process responsible for the detection of security attacks,
detection of security breaches, and the performance assessment of the
installed security infrastructure. However, the concept of an audit is
typically applied to post-event/incursion.  The Security Domain model, as
with active security infrastructures, requires constant monitoring.  Thus
the audit process needs to be enhanced.

When attempting to evaluate the security process on
an enterprise basis, it is impossible to account for all of the business
entities, politics, and technological choices that could be chosen by the
various entities that aggregate into the enterprise.  Thus to discuss
security on an enterprise level is often a daunting task that may never come
to closure.  In order to simplify the discussion, allow for various entities
to control their own resources, and to enable the discussion to focus on the
important aspects, security will be discussed in regards to Security
Domains.

## Security Requirements, Threats, and Attacks

This section provides a brief overview of security
requirements, security threats, and possible security attacks.

### Security Requirements and Threats

Users, whether they are people or software
applications, have zero or more of four basic security requirements, which
protect them from four basic threats:

·        
**Confidentiality** – preventing the unauthorized access to
information

·        
**Integrity** – preventing the unauthorized modification or
theft of information

·        
**Availability** – preventing the denial of service and
ensuring authorized access to information

·        
**Non-Repudiation** – preventing the denial of an action
that took place or the claim of an action that did not take place.

These security requirements and the threats that they
counter are shown in Figure 4.

if !vml?![](Anl_Security_Risk_Assessment_files/image010.gif)endif?
Figure 4: Security Requirements, and the
Threats They Counter

### Security Attacks

The threats can be realized by many different types
of attacks, some of which are illustrated in Figure 5.
As can be seen, the same type of attack can often be involved in different
security threats. This web of potential attacks means that there is not just
one method of meeting a particular security requirement: each of the types
of attacks that presents a specific threat needs to be countered. Details on
these different types of attacks can be found in many books, web pages, and
security manuals.

if !vml?![](Anl_Security_Risk_Assessment_files/image012.gif)endif?
Figure 5: Security Requirements, Threats,
and Possible Attacks

## Security Countermeasure Services

Security countermeasures, as illustrated in Figure
2‑6, are also a mesh of interrelated
technologies and policies. At first glance, this mesh seems to be a daunting
collection of security measures. However, not all security countermeasures
are needed or desired all of the time for all systems and assets: this would
be vast overkill and would tend to make the entire information
infrastructure virtually unusable or very ponderous. Therefore, the first
step is to identify which countermeasures are beneficial to meet which
security requirements. Once these are determined, an analysis of the actual
configurations and performance requirements of the systems to be protected
will lead to different technologies and techniques to fulfill the security
countermeasure requirements.

These breakdowns are illustrated in Figure 7,
Figure 8, Figure 9,
and Figure 10, and are discussed in the
following sections.

if !vml?![](Anl_Security_Risk_Assessment_files/image014.gif)endif?
Figure 6: Overall Security: Security
Requirements, Threats, Countermeasures, and Management

### NERC 1200/1300 Security Policy and Management Documents

NERC’s 1300 document contains (among others) three
key statements related to security for power system operations:

1.      
“*Critical business and operational functions performed by
cyber assets affecting the bulk electric system necessitate having security
management controls*.”

2.      
“*This
standard [NERC’s 1300 document] requires that entities identify and protect
critical cyber assets related to the reliable operation of the bulk electric
system*.”

*3.     
“In order to protect these assets, it is necessary to identify the
electronic perimeter(s) within which these assets reside. When electronic
perimeters are defined, different security levels may be assigned to these
perimeters depending on the assets within these perimeter(s).”*

In these
statements, NERC has identified three key concepts:

·        
Cyber security involves not just passive encryption of
information exchanges (a common misperception), but active management
controls. Management of security measures must be an on-going process,
constantly re-visited to ensure that new requirements are properly met and
that new threats are properly assessed and ameliorated (if not eliminated).

·        
The most effective way to handle security is to identify the
cyber assets and protect them. In this context, “assets” are physical
computer-based hardware, software applications, databases containing
information, and data exchange messages.

·        
Since assets are often strongly interconnected with one
another, it would be very difficult to handle each one completely
separately. However, assets with similar security requirements are often
within well-defined boundaries (e.g. within a substation, within a control
center, at all customer sites), which can be used as “electronic perimeters”
or (as often termed) identified as “security domains”. The same security
countermeasures can then be applied to all assets within a security domain,
based on the security requirements of the most sensitive asset. This
minimizes the effort required within a security domain, and allows more
attention to be paid to the complex security issues for exchanging
information between different security domains.

### Confidentiality Security Countermeasure Services

Although Figure 6
appears very complex, the security countermeasures can be organized into
different basic security services, in which “security services” are generic
descriptions of security measures without identifying specific technologies
or techniques for implementing them. For example, the security requirement
for Confidentiality needs the key security services of (see Figure 7):

·        
**Authorization for Access Control**. Authorization
requires a method for establishing a person’s (or software application’s)
identity so that their permission to access confidential data can be
determined. People typically use **Passwords** to authenticate
themselves, while applications use **Certificates**. This identity must
have been previously established.

·        
**Identity Establishment and Authentication**. In the power
system environment, most authentication should be role-based – that is,
authentication is related to the role that someone is playing, rather than
who they are. For instance, a person can be the System Operator for the East
Division during the day, but could be the overall Supervisor for all
Divisions at night. That same person would also be an individual user of
email, accessing only his own account.

·        
**Credential Establishment**. The most common method for
establishing mutual credentials to ensure confidentiality of transactions
over the Internet is through the use of **Public Key Infrastructure (PKI)**.
For the power industry, **IEC 62351** will provide similar technologies
that are specifically tailored to meet the configuration and performance
requirements of some IEC TC57 communication protocols. One of the main
efforts that is external to the security technologies is the management of
keys and certificates.

·        
**Message Encryption**. Confidential messages that are sent
between entities require encryption. On the Internet, the most commonly used
message encryption technology is **Transport Layer Security (TLS)**. TLS
can use different encryption encoding techniques based on **DES** and/or
(more commonly nowadays) **AES**. An alternate technique is the use of **Virtual Private Networks (VPN)**, which provide an end-to-end secure
channel between two entities, such as between a laptop’s email program and
the corporate email server. For wireless media such as WiFi, other standards
are being developed to handle message encryption. For the gas and power
industry, the American Gas Association (AGA) has developed the **AGA 12-1**
specifications for encryption boxes that are designed to be placed at either
end of point-to-point connections, using “bump-in-the-wire” technology.

·        
**Security Assessment Measures.** All functions that
require confidentiality should also include **Audit Logging** and some
type of **Intrusion Detection System (IDS)**. These provide a means to
assess whether confidentiality has been maintained. In addition, if networks
are used between security domains, then **Firewalls** with **Access
Control Lists (ACL)** should also be implemented to limit network access.
If PCs, particularly PCs based on Windows, are used within networks that
cross security domains, then **Anti-Virus** and **Anti-Spyware**
programs should be installed.

if !vml?![](Anl_Security_Risk_Assessment_files/image016.gif)endif?

Figure 7: Confidentiality Security Countermeasures

### Integrity Security Countermeasure Services

As can be seen from Figure 8,
the security countermeasures for meeting the Integrity requirement are very
similar to the Confidentiality countermeasures. In particular, the set of
countermeasures for Authorization for Access Control, Identity Establishment
and Authentication, Credential Establishment, Message Encryption, and
Confidentiality Assessment Measures are identical. The only additional
countermeasures are:

·        
**Digital Signatures**. Digital signatures can be used to
verify that the data is coming from an authenticated source. This can ensure
that the data is being received from the entity that it claims to come from,
and therefore has not been tampered with on the way. However, it does not
entirely ensure the integrity of the data, which may have been compromised
before it was sent.

·        
**Cyclical Redundancy Check (CRC)**. The CRC code added to
the end of a message helps to ensure that the data was not modified as it
was being transmitted. However, it cannot completely ensure the integrity of
the data, since a “man-in-the-middle” attack could simply generate a new CRC
after changing the data.

if !vml?![](Anl_Security_Risk_Assessment_files/image018.gif)endif?
Figure 8: Integrity Security
Countermeasures

### Availability Security Countermeasure Services

“Availability” is the ability for an authorized
entity to have access to the data or system in a timely manner whenever it
needs that access. The threat is termed “Denial of Service” when it is due
to a deliberate attack.

However, the most common cause for unavailability is
a malfunction of the system, whether a computer software “crash”, hardware
failure, or interrupted communications. For power system operations,
unavailable data can have very serious consequences: as noted above, the
main contributing factor in the August 14, 2003 blackout was the
unavailability of key data to the right place at the right time (not due in
this case to terrorism, but that more pernicious causes of carelessness and
poor design). In a broad sense, security of the information infrastructure
includes measures to detect and announce the unavailability of information,
even if not caused by deliberate attacks.

The primary countermeasures (equally valid whether
the denial of service was deliberate or inadvertent) are:

·        
**Techniques to Minimize Denial of Service**. In essence,
this means good system and network design that is adequately monitored so
that failures, software anomalies, data inconsistencies, and performance
problems can be detected and corrected.

·        
**Backup and Recovery**. Backup and recovery mechanisms are
vital to recovering from losses of data for any reason, but even more so for
data that might have been tampered with. Special care should be taken to
ensure that compromised data does not wipe out legitimate data during a
backup process.

·        
**Network and System Management (NSM)**. Network and system
management is not always considered part of “security”, but in reality,
managing the information infrastructure is as crucial to the secure and
reliable operation of the power system as any encryption or access
management security schemes. Often SCADA systems perform some minimal
communications monitoring, such as whether communications are available to
their RTUs, and then they flag data as “unavailable” if communications are
lost. However, it is then up to the maintenance personnel to track down what
the problem is, what equipment is affected, where the equipment is located,
and what should be done to fix the problem. Where availability is a critical
security requirement, network and system management should be implemented.
The most common technology is the **Simple Network Management Protocol
(SNMP)** that was developed by the IETF for the Internet. In addition, **IEC 62351-7** – Management Information Bases (MIBs) for Network and System
Management – is under development to create standardized objects for
monitoring and controlling utility-specific equipment.

if !vml?![](Anl_Security_Risk_Assessment_files/image020.gif)endif?
Figure 9: Availability Security
Countermeasures

### Non-Repudiation Security Countermeasure Services

Non-repudiation implies ensuring that entities cannot
deny that a transaction took place, nor its opposite: claim that a
transaction did take place when it did not. As seen in Figure 10,
from a cyber point of view, the primary method for handling non-repudiation
is digital signatures:

·        
**Digital Signatures.** Digital signatures require the full
suite of authentication. They need to ensure, first of all, that the
identity of the entities are established and valid. Then, in order to
exchange the digital signature over insecure networks, authentication,
authorization, and encryption is required.

·        
**Security Attack Litigation.** Since attempts to repudiate
transactions are often associated with legal or financial issues, having a
good audit trail along with digital signatures is particularly important. In
addition, power system operations should have audit logs (including sequence
of events logs) with very precisely synchronized time, in order to track and
cross-correlate operational states and control commands across different
substations, utilities, and regions.

if !vml?![](Anl_Security_Risk_Assessment_files/image022.gif)endif?
Figure 10: Non-Repudiation Security
Countermeasures
