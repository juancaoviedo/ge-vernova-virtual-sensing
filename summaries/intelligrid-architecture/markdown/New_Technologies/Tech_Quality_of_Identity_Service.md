# Quality of Identity

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Quality_of_Identity_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Quality of Identity Service

This
service allows an entity to determine the trust level associate with the
identity being conveyed. This is of particular interest where the source Identity,
of the original transaction, has been mapped several times.

This
service represents a specific capability that could be viewed as a subset of
the Identity Service. However, technical evaluations of existing solutions
indicate that no solutions provide this ability and therefore are worthy of
being defined independently so that the service requirement is not lost.

This
is a service that is not widely recognized, although QID-01 makes a strong case
for its need. The basic issue raised by QID-01 is that of the ability to trust
an identity being established if the identity has been mapped or its
credentials converted several times. At a minimum, without a mechanism for
originator determination, there is a relevant issue. However, originator
determination could be provided by and adequate audit mechanism, but this does
not assist the receptor of a transaction. Thus there is a need to provide a
mechanism to allow the receptor to determine a level of trust based upon the
number of mappings that have occurred along the transaction path.

Table 28: References Relating to Quality of Identity

|  |  |
| --- | --- |
| QID-01 | Audun Josang, An Algebra for Assessing Trust in Certification Chains, Telnor R&D  email: audun.josang@fou.telenor.no |
|  |  |

Technological Assessment and
Relevant Specifications

There
are two aspects in regards to Quality of Identity, the ability to determine the
number of times that an identity has been transformed, which is a superset of
the number of times that credentials have been converted.

There
are no relevant specifications/solutions that can be applied to the generalized
identity mapping issue, as many of these mappings are local issues.

However,
in the particular case of digital certificate conversion, the SAML
specification yields a possible solution. However, the solution would require
that attribute definitions and attribute chaining be added to SAML’s use within
IntelliGrid Architecture environment.

There
are no such solutions for username/password and it may be worthwhile to develop
such a specification based upon the SAML principles.

For
address based credentials, source routing offers a potential solution (see Path
Routing and QS service).

Table 29: Relevant Specification for the Quality of
Identity Service

| Identification Number | Name | Comment |
| --- | --- | --- |
| OASIS Security Technical Committee | Attribute Profiles for SAML 2.0  Available from:  http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf | Incomplete, but is on the correct track. |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf | Draft that is needed to establish identity within a SAML environment. |
|  |  |  |
