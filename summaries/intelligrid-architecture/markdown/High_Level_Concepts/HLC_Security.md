# Security Issues

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/High_Level_Concepts/HLC_Security.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security Issues

![](../Overview_Guidelines/IECSA_VolumeI_files/image010.gif)

Figure 10: The
Information Security Process Security is one of the strongest drivers
for applying architecture principles across the industry.

*See
[Security Organization](../Technology_Analysis/Anl_Security_Overview.htm)
for a detailed listing of all security-related IntelliGrid Architecture web
pages.*

Security is the second concept under IntelliGrid Architecture’s
strategic vision. Security is one of the strongest drivers for applying
architecture principles across the industry. The cyber security of advanced
automation and consumer communications systems is one of the most important and
challenging technical issues of our time. Increasing demand for information
technology and reliance on advanced automation has created substantial
challenges for system administrators as they try to keep their cyber systems
secure from attack. Higher levels of integration across the industry and using
open systems combine to raise the challenges of securing systems. Security
policy implementation, a recommended practice, requires many of the concepts
that architectures bring forward including system documentation, and structure.

Cyber security encompasses a variety of
functions for the next generation of distributed computing systems, including,
but not limited to: developing and implementing security policies (for
individual enterprises and the industry), threat and vulnerability assessments,
system ‘hardening’ against intrusions, and managing the ‘residual risk’.

The public electric power system is now
characterized as among several critical infrastructures that must apply
security practices more rigorously. This project has identified several
stakeholder communities that are likely to increasingly put forward security
requirements for energy system operations. Requirements from diverse sources
are a part of the security approach taken by IntelliGrid Architecture project.

Security functions are also necessary to design
into the architecture as well as the equipment that will comprise the next
generation of advanced automation. Specifying security upfront is particularly
important for small resource constrained devices that have limited computing
resources. This is because security functions can drive minimum requirements
for small equipment.

‘Security by Obscurity’ is no longer an
acceptable solution in the electric power industry. Cyber-security has become a
major issue for utilities due in part to the increased vulnerability of
utilities as they network computer systems and power system equipment; this is
also due in part to the competitive environment where crucial information
(gathered legally or illegally) can translate into millions of dollars.
Deregulation pressures and opportunities are encouraging the transfer of energy
between increasingly distant business and operating entities, with energy flows
varying dramatically as the price of energy fluctuates during the day and over
the year. These market-driven fluctuations increase the complexity of
congestion management, so that reliability requirements are demanding rapid and
accurate information about the real-time state of the power system and the
equipment that monitors and controls it. In addition, the power system is
increasingly required to respond as ‘intelligently’ as possible to abnormal or
at-the-limit conditions.

Increasing numbers of customers are adding
cogeneration and ‘backup’ distributed generation at their facilities, and
selling back to the grid when the prices make it worthwhile. As the trend
toward local generation increases, power systems will see increased and rapid
fluctuations in power flows as marketers buy and sell energy and ancillary services
from these local generators as well as from the larger generators. Only through
rapid access to accurate and secure information from these diverse sources will
the power systems continue to be operated reliably.

The public Internet is a very powerful,
all-pervasive medium. It can provide very inexpensive means exchange
information with a variety of other entities. The Internet is being used by
some utilities for exchanging sensitive market information, retrieving power
system data, and even issuing some control commands to generators. Although
standard security measures, such as security certificates, are used, a number
of vulnerabilities still exist. These vulnerabilities include inadequate
security policies, inadequately enforced security policies, and lack of
security countermeasures for different types of security threats (such as
denial of service).

Not all data are equal when it comes to
sensitivity to security threats. The key to assessing the sensitivity of data
is to determine the impact, both financial and societal, on compromising its
security, and to determine the risk of that compromise occurring. For instance,
the financial and societal impact of eavesdropping on the meter readings of a
single residential home is far less than the impact of issuing unauthorized
breaker-trip commands to high voltage transmission lines. Therefore, the
primary need is the assessment of financial and societal costs of different
security vulnerabilities, along with the assessment of the financial and
societal costs of implementing security measures.  The IntelliGrid Architecture security
strategy is documented in Appendix A for those technologies that have
identified the issues in their respective environments (e.g. IEC61850). 
The security strategy for other technologies/applications will have to be
developed based on the requirements of the particular application and using the
technologies and practices found in Appendix A.

## Security Concerns

Security is an issue that several industries and most
businesses are attempting to come to terms with. However, the implementation of
a robust security infrastructure often appears to be a daunting and
overwhelming task.  This can be attributed to several factors:

### There is no defined mechanism to decompose the security problem space and therefore it is perceived to be an impossible task.

Typically there are two major discussion/analysis methods
in regards to security: Enterprise based analysis and/or Technology/Threat
based analysis.  There are obvious pitfalls to both approaches.  The
instantiation of an Enterprise is continuously evolving/changing and may
encompass more than one business entity where a single set of security policies
and technologies cannot be enforced[[1]](HLC_Security.htm#_ftn1).
Thus any security decisions require a large amount of coordination and tend to
make the security process frustrating.

However, the security problem can be decomposed into
smaller regions of security analysis/management.  This is the “Security Domain”
concept that this appendix introduces on page 3).  This allows a set of resources to be managed (from a security perspective) independently.

However, this raises the issue of how to provide a
security mechanism for inter-domain exchanges.  To solve this issue, the
appendix introduces several abstract security services that may be bound to
different security technologies.

The technology only based analysis approach could be
classified as flawed from the outset.  Since security is an ongoing and
evolving process, selection of security based upon today’s technology may
prevent adopting more advanced security technologies in the future.  This
appendix introduces a set of abstract security services that can be mapped to
current or future technologies, in order to resolve this analysis dilemma.

### There may be a lack of understanding in regards to the importance of a security policy and a commitment to implement that policy.

The first problem that is typically encountered is that
Enterprise policy development is overwhelming (see the previous discussion). 
However, the use of the Security Domain concept should help mitigate this
issue.  Nonetheless, the use of the Security Domain concept means that the
domains need to be identified and then the policy needs to be developed for the
domains.

The second issue is there is typically a lack of understanding
of what constitutes a security policy.  In particular, the policy must address
the entire suite of security processes, security functions, security services,
and security management.

The third issue, and typically most daunting, is how to
decide what needs to be secured within the security policy.  Some contend that
every asset needs to be secured.  However, this approach makes security
deployment/adoption costly and could prevent entities from even attempting to
deploy security.

Therefore, **all assets do not need to be secured**,
although all assets *could* be secured.  However, **all assets should be
analyzed in regards to the need of security**.

Thus the issue is raised of the type of analysis that
should be performed. This appendix recommends that a risk assessment approach
to the analysis be taken. The appendix discusses risk analysis at a high level
and then references emerging work regarding risk assessment are given instead
of embedding the intellectual content.

Therefore, Security Policies are a key security service
that should be performed in advance of any security deployment.  This is
discussed in greater detail under the Technical Analysis of Security.

### There has been no authoritative work in regards to defining abstract security services.

IntelliGrid Architecture defines several abstract security services that are
relevant to implementing inter-domain and intra-domain security.  However, the
appendix also identifies that some of the abstract services have no deployment
technologies that can be used to implement the security service.  The appendix
does attempt to define what emerging standards could be used/modified in order
to allow the security service to actually be instantiated.

In regards to abstract security service definitions, those
described in these IntelliGrid Architecture documents should be viewed as a starting point from
which future work can evolve.

### There is typically a lack of understanding in regards to the impact of security on communication requirements.  This is due in large part to the lack of communication/infrastructure requirement definition.

Other IntelliGrid Architecture documents discuss the system requirements from
a communication and user environment perspective.  The security
services/technologies recommended by IntelliGrid Architecture have be correlated and analyzed against
these IntelliGrid Architecture requirements and the power system functions.  Thus, IntelliGrid Architecture
documentation set should ease the identification of impact and aid in the
selection of the appropriate security service and technology.

## Security Processes

Protection and securing of networked communications,
intelligent equipment, and the data and information that are vital to the
operation of the future energy system is one of the key drivers behind
developing an industry-level architecture.  Cyber security faces substantial
challenges both institutional and technical.  The IntelliGrid Architecture documents serve to
provide context to this complex topic as well as providing a pathway by which
the industry can work to develop a robust portfolio of technologies to meet the
critical issues that encompass security.

Security of the energy and communications systems
addressed by IntelliGrid Architecture faces multiple challenges from the following major trends:

·       Need
for greater levels of integration with a variety of business entities

·       Increased
use of open systems based infrastructures that will  comprise the future energy
system

·       The
need for appropriate integration of existing or “legacy” systems with future
systems

·       Growing
sophistication and complexity of integrated distributed computing systems

·       Growing
sophistication and threats from hostile communities

**Figure 1: General Security Process**

![](IECSA_VolumeIV_AppendixA_files/image001.png)Security
must be planned and designed into systems from the start.  Security functions
are integral to the designs of systems. Planning for security, in advance of
deployment, will provide a more complete and cost effective solution.  Additionally,
advanced planning will ensure that security services are supportable (may be
cost prohibitive to retrofit into non-planned environments.  This means that
security needs to be addressed at all levels of the architecture.

Security is a ever evolving process and is not static.  It
takes continual work and education to help the security processes keep up with
the demands that will be placed on the systems.  Security will continue to be a
race between corporate security policies/security infrastructure and hostile
entities.  The security processes and systems will continue to evolve in the
future.  By definition there are no communication connected systems that are
100% secure.  There will be always be residual risks that must be taken into
account and managed.

The normal thought process in regards to security.  It
accurately reflects that the security process is a never-ending process.  Thus,
in order to maintain security constant vigilance and monitoring is needed as
well as adaptation to changes in the overall environment. The process depicts
five (5) high level processes that are needed as part of a robust security
strategy.  Although circular in nature, there is a definite order to the process:

**Security Assessment** – Security assessment is the
process of assessing assets for their security requirements, based on probable
risks of attack, liability related to successful attacks, and costs for
ameliorating the risks and liabilities. The recommendations stemming from the
security requirements analysis leads to the creation of security policies, the
procurement of security-related products and services, and the implementation
of security procedures.

The implication of the circular process is that a security
re-assessment is required periodically.  The re-evaluation period needs to be
prescribed for periodic review via policy. However, the policy needs to
continuously evaluate the technological and political changes that may require
immediate re-assessment.

**Security Policy** – Security policy generation is the
process of creating policies on managing, implementing, and deploying security
within a Security Domain. The recommendations produced by security assessment
are reviewed, and policies are developed to ensure that the security
recommendations are implemented and maintained over time.

**Security** **Deployment** – Security deployment is
a combination of purchasing and installing security products and services as
well as the implementation of the security policies and procedures developed
during the security policy process. As part of the deployment aspect of the
Security Policies, management procedures need to be implemented that allow
intrusion detection and audit capabilities, to name a few.

**Security** **Audit (Monitoring) –** Security audit
is the process responsible for the detection of security attacks, detection of
security breaches, and the performance assessment of the installed security
infrastructure.

However, the concept of an audit is typically applied to
post-event/incursion.  The Security Domain model, as with active security
infrastructures, requires constant monitoring.  Thus the audit process needs to
be enhanced.

**Security Training** – Continuous training on security
threats, security technologies, corporate and legal policies that impact
security, Security measures analysis is a periodic, and best practices is
needed.  It is this training in the security process that will allow the
security infrastructure to evolve.

When attempting to evaluate the security process on an
enterprise basis, as is required by IntelliGrid Architecture, it is impossible to account for all
of the business entities, politics, and technological choices that could be
chosen by the various entities that aggregate into the enterprise.  Thus to discuss
security on an enterprise level is often a daunting task that may never come to
closure.  In order to simplify the discussion, allow for various entities to
control their own resources, and to enable the discussion to focus on the
important aspects, security will be discussed in regards to Security Domains.
