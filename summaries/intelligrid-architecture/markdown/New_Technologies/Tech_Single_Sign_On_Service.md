# Single Sign On

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Single_Sign_On_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Single Sign On Service

Relieve
an entity having successfully completed the act of authentication once from the
need to participate in re-authentications upon subsequent accesses to an Open
Grid Services Architecture (OGSA) -managed resources for some reasonable period
of time. This must take into account that a request may span security domains
and hence should factor in federation between identity domains and mapping of
identities. This requirement is important from two perspectives: a) It places a
secondary requirement on an OGSA-compliant implementation to be able to
delegate an entity’s rights, subject to policy (e.g., lifespan of credentials,
restrictions placed by the entity) b) If the credential material is delegated
to intermediaries, it may be augmented to indicate the identity of the
intermediaries, subject to policy.

This
service is a local combination of the Credential Conversion and Identity
Mapping services.
