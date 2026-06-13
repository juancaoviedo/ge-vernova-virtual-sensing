# Credential Conversion

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Credential_Conversion.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

## Credential Conversion

The
credential conversion service provides credential conversion between one type
of credential to another type or form of credential. This may include such
tasks as reconciling group membership, privileges, attributes
and assertions associated with entities (service requestors and service
providers). For example, the credential conversion service may convert a
Kerberos credential to a form which is which is required by the authorization
service. The policy driven credential conversion service facilitates the
interoperability of differing credential types, which may be consumed by
services. It is expected that the credential conversion service would use the
identity mapping service.

Key
definitions:

**credential:
1.** In cryptography, a subset of access permissions (developed with the use
of media-independent data) attesting to, or establishing, the identity of an
entity, such as a birth certificate, driver's license, mother's maiden name,
social security number, fingerprint, voice print, or other biometric
parameter(s). [After X9.69] **2.** [In security], information, passed from
one entity to another, used to establish the sending entity's access rights.
[INFOSEC-99]

Credential
conversion is also a required service for Single-Sign on and the Identity
Mapping security services. Besides performing the actual mappings, there is an
inherent requirement that such a service provide an audit mechanism so that it
is possible to determine the original identity/credential that was converted.
This is a necessary requirement in order to provide a robust audit mechanism in
a multi-domain environment.

Technological Assessment

The
prevalent work is being sponsored by OASIS. This is work in progress but is the
first industry/standards based consortium that is attempting to solve the
problem. However, the current work involves certificate usage and does not
directly address the issue of username/password conversion or the audit trail
issues.

Except
for the general recommendations found in the Identity Establishment service,
only certificates require further recommendations in regards to credential
conversion.

Certificate

Furthermore,
there has been little thought in enhancing the SAML specification to
standardize a chain or properties that would allow the Quality of Identity
service to be facilitated.

It
is suggested that SAML and the OASIS work be adopted as the foundation for the
Credential Delegation service. However, further work and IntelliGrid Architecture enhancements may
be required.

Table 10: References and Specifications regarding
Credential Conversion

| Identification Number | Name | Comment |
| --- | --- | --- |
| OASIS Security Technical Committee | Security for Grid Services  Available from:  http://www.globus.org/Security/GSI3/GT3-Security-HPDC.pdf |  |
| OASIS Security Technical Committee | Attribute Profiles for SAML 2.0  Available from:  http://www.oasis-open.org/committees/download.php/6344/sstc-hughes-mishra-baseline-attributes-03.pdf | Incomplete, but is on the correct track. |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf | Draft that is needed to establish identity within a SAML environment. |
