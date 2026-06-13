# Identity Mapping Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Identity_Mapping_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Identity Mapping Service

The
identity mapping service provides the capability of transforming an identity
that exists in one identity domain into an identity within another identity
domain. It is worthwhile to note that there may be multiple identity domains
within a single Security Domain. There is an additional attribute to identity
mapping, the mapping may result in either a mapping of an individual into
another set of credentials that represent the individual (but for a different
resource) or in a mapping to a role/group based identity for the resource.

As
an example, consider an identity in the form of an X.500 Distinguished Name
(DN), which is carried within an X.509v3 digital certificate. The combination
of the subject DN, issuer DN and certificate serial number may be considered to
carry the subject’s or service requestor’s identity. The scope of the identity
domain in this example is considered to be the set of certificates that are
issued by the certificate authority. Assuming that the certificate is used to
convey the service requestor’s identity the identity mapping service via policy
may map the service requestor’s identity to an identity that has meaning (for
instance) to the hosting environment’s local platform registry. The identity
mapping service is not concerned with the authentication of the service
requestor; rather it is strictly a policy driven name mapping service.

The
Identity Mapping can occur due to Credential Conversion or local/programmatic
reasons. The major issues with Identity Mapping are very similar to the issues
in Credential Conversion:

·      
There needs to be an audit mechanism inserted into the mapping process
so that the originator of the transaction can be identified if needed.

Technological Assessment and
Relevant Specifications

Relevant
specifications and references may be drawn from the Identity Establishment,
Credential Conversion, and Firewall Transversal services. In order to be
concise, they will not be repeated in this section. This section will only
contain additional recommendation above and beyond the other service
recommendations.

Address Mapping

It
is recommended that Network Address Translation be used as part of the
non-Transparent Firewall deployment. However, in the use of NAT or most
non-Transparent firewalls, there is an issue of providing a proxy for multiple
“protected addresses” into the public address space. It is recommended that
firewalls be evaluated for their capability to proxy and map multiple addresses
as it may save deployment and management cost.

UserName/Password

Although
there are no relevant standards/specifications pertaining to this issue, the
most natural mapping service is through the use of single sign-on (SSO).
However, this does not truly represent the true Identity Mapping (although it
is credential mapping).

Digital Certificates

See
the discussion in the Credential Conversion service discussion.
