# Security Avail Discovery

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Security_Service_Availability_Discovery_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Security Service Availability Discovery Service

A
Security Domain must provide a mechanism for an entity to discover what other
security services are available for its use.

Within
the IntelliGrid Architecture, such a service would be required for Inter-Domain usage
where a-priori knowledge is not available. It would also be a mandatory service
if Quality of Security routing became a reality.

Technological Assessment and
Relevant Specifications

Although
there is no immediately usable technology to accomplish this service, it is
recommended that the WS-Policy series be extended to provide this capability.
It should be fairly straightforward to model security service availability as
policy (e.g. the Policy Attachment may need to be extended). At a minimum, the
information required to be conveyed needs to be determined in advance of
attempting to adopt WS-Policy.

Since
the discovery service is needed inter-domain, it is reasonable to attempt to
make use of Web Services at the domain interconnect points to provide this
capability.

Table 32: Potentially Relevant Specifications in regards
to Security Capability Discovery

| Identification Number | Name | Comment |
| --- | --- | --- |
| OASIS | Web Services Policy Framework (WS-Policy)  Available from:  http://xml.coverpages.org/ws-policyV11.pdf |  |
| OASIS | Web Services Policy Assertions Language (WS-PolicyAssertions)  Available from:   http://xml.coverpages.org/ws-policyassertionsV11.pdf |  |
| OASIS | Web Services Policy Attachment (WS-PolicyAttachment)  Available from:  http://xml.coverpages.org/ws-policyattachmentV11.pdf |  |
