# Security Concerns

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Concerns.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Security Concerns

Security is an issue that several industries and most
businesses are attempting to come to terms with. However, the implementation of
a robust security infrastructure often appears to be a daunting and
overwhelming task.  This can be attributed to several factors:

### There is no defined mechanism to decompose the security problem space and therefore it is perceived to be an impossible task.

Typically there are two major discussion/analysis methods
in regards to security: Enterprise based analysis and/or Technology/Threat
based analysis.  There are obvious pitfalls to both approaches.  The
instantiation of an Enterprise is continuously evolving/changing
and may encompass more than one business entity where a single set of security
policies and technologies cannot be enforced[[1]](Anl_Security_Concerns.htm#_ftn1). Thus any security decisions require a
large amount of coordination and tend to make the security process frustrating.

However, the security problem can be decomposed into
smaller regions of security analysis/management.  This is the “Security
Domain” concept that this appendix introduces on page 3).  This allows a
set of resources to be managed (from a security perspective) independently.

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
Enterprise policy development is overwhelming (see the previous
discussion).  However, the use of the Security Domain concept should help
mitigate this issue.  Nonetheless, the use of the Security Domain concept
means that the domains need to be identified and then the policy needs to be
developed for the domains.

The second issue is there is typically a lack of
understanding of what constitutes a security policy.  In particular, the
policy must address the entire suite of security processes, security functions,
security services, and security management.

The third issue, and typically most daunting, is how to
decide what needs to be secured within the security policy.  Some contend
that every asset needs to be secured.  However, this approach makes
security deployment/adoption costly and could prevent entities from even
attempting to deploy security.

Therefore, **all assets do not need to be secured**,
although all assets *could* be secured.  However, **all assets
should be analyzed in regards to the need of security**.

Thus the issue is raised of the type of analysis that
should be performed. This appendix recommends that a risk assessment approach to
the analysis be taken. The appendix discusses risk analysis at a high level and
then references emerging work regarding risk assessment are given instead of
embedding the intellectual content.

Therefore, Security Policies are a key security service
that should be performed in advance of any security deployment.  This is
discussed in greater detail under the Technical Analysis of Security.

### There has been no authoritative work in regards to defining abstract security services.

IntelliGrid Architecture defines several abstract security services that are
relevant to implementing inter-domain and intra-domain security.  However,
the appendix also identifies that some of the abstract services have no
deployment technologies that can be used to implement the security service. 
The appendix does attempt to define what emerging standards could be used/modified in order to allow the security service to
actually be instantiated.

In regards to abstract security service definitions, those
described in these IntelliGrid Architecture documents should be viewed as a starting point from
which future work can evolve.

### There is typically a lack of understanding in regards to the impact of security on communication requirements.  This is due in large part to the lack of communication/infrastructure requirement definition.

Other IntelliGrid Architecture documents discuss the system requirements from
a communication and user environment perspective.  The security
services/technologies recommended by IntelliGrid Architecture have be correlated and analyzed
against these IntelliGrid Architecture requirements and the power system functions.  Thus,
IntelliGrid Architecture documentation set should ease the identification of impact and aid in
the selection of the appropriate security service and technology.
