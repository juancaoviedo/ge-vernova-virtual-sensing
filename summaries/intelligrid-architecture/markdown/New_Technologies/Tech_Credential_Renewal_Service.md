# Credential Renewal

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Credential_Renewal_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Credential Renewal Service

In
many scenarios, a job initiated by a user may take longer than the life span of
the user’s initially delegated credential. In those cases, the user needs the
ability to be notified prior to expiration of the credentials, or the ability
to refresh those credentials such that the job can be completed.

It
is worthy to note that the Credential Renewal service provides some of the
capability of User and Group Management service. However, it does not include
how to revoke or initially allocate the credentials. However, in general it is
a Security Domain and IntelliGrid Architecture issue in regards to the period of time required for
credential renewal.

Performing
a more in-depth analysis of the credential renewal process, the general issues
are:

·      
Determining when the credentials need to be renewed. This is typically a
Security Domain’s policy issue.

·      
Determining a mechanism to detect a credential that needs to be renewed.

·      
Provide a mechanism for credential renewal.

OASIS specifies several different types of
credentials that need to be considered for renewal. Each has different aspects
to renewal. The IntelliGrid Architecture relevant types are:

·      
Internet Protocol based credentials are related solely to address
resolution as the credential. Address spoofing is a prevalent threat in IntelliGrid Architecture environment and therefore the use of this credential mechanism is not
suggested.  
  
In order to renew an addressed based credential, address-to-name resolution is
required as well as appropriate security on such resolution requests.

·      
InternetProtocolPassword makes use of username/password as well as
address resolution to establish credentials.  
  
This credential methodology has the same issues with address credential renewal
as well as verifying that the password is viable or in need of renewal.

·      
Password makes use of a username/password combination in the clear.  
  
Username/Password management is a major issue that needs to be resolved.

·      
PasswordProtectedTransport makes use of an encrypted transport to
transmit a username/password combination (e.g. HTTPS conveying a
username/password).

·      
SmartCard renewal is strictly a policy and SMI issue. The policy must
address when a SmartCard must be renewed and the mechanism for performing a
renewal.

·      
SmartCardPKI renewal adds the issue of digital certificate renewal to
the need to renew a particular Smart Card. Since most digital certificates have
an expiration date, it is the certificate date that should take precedence in
the renewal process (e.g. policy may be able to ignore the renewal of the card
itself). However, this is not the case if the SmartCardPKI solution is being
used as a Personal Identification card that requires visual inspection for
physical access.

·      
SoftwarePKI uses digital certificates and therefore certificate renewal
is the major issue.

·      
TimesyncToken is a hardware token that is used to generate a unique
token as a credential.

·      
Visual Person Identification Card used with visual inspection to provide
physical access control.  
  
Any credential type that can be used to obtain physical access based upon
visual inspection need to be replaced or modified in a timely manner. The
periodicity of the change is dependent upon the Security Domain’s policies.

Technological Assessment and
Relevant Specifications

There
are certain general recommendations that can be made:

·      
When using address resolution and TCP/IP, make use of the Domain Name
Service and an authenticated Directory server. Dynamic address assignment
should be the preferred mechanism with the resulting address being placed in
the authenticated directory server.

·      
Visual Credentials should be replaced/modified
on a time period based upon the Security Domain’s policy. It may be less
expensive to adopt a modification, as opposed to a replace strategy (e.g. the
same model as automobile license tabs versus license plates).

·      
Smart Cards should include a renewal date as part of the information
that is contained on the card. This field should encrypt and digitally signed
so that tampering can be detected. As the Smart Card is used, advanced
notification of the need for renewal needs to be given to the holder.

·      
Certificate based technologies: X.509 certificates are the recommended
certificate type. Certificates should be accessible via PKCS#10 interfaces. The
date of certificate lifetime expiration should be used as the renewal date. As
the certificate is used, advanced notification of the need for renewal needs to
be given to the holder.

·      
Biometric based technologies need to have renewal dates based upon the
Security Domain’s policy.

Specific Recommendations

Certificates

It
is recommended that RFC 2797 or RFC 2560 (OCSP) to determine if the certificate
needs to be renewed. If neither of these is possible, then it becomes a local
Security Domain/implementation issue.

Certificate
renewal should be performed via RFC 2797 when possible.

Table 11: Relevant Specification regarding Credential
Renewal

| Identification Number | Name | Comment |
| --- | --- | --- |
| ISO 9735-9:2002 | Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 9: Security key and certificate management message (message type- KEYMAN) |  |
| NERC | Certificate Policy for the Energy Market Access and Reliability Certificate (e‑MARC) Program Version 2.4  Available from:  ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc |  |
| OASIS Security Technical Committee | Authentication Context  Available from:  http://www.oasis-open.org/committees/download.php/6539/sstc-saml-authn-context-2.0-draft-04a-diff.pdf |  |
| RFC 2459 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |  |
| RFC 2511 | Internet X.509 Certificate Request Message Format |  |
| RFC 2560 | X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP |  |
| RFC 2797 | Certificate Management Messages over CMS |  |
| RFC 2875 | Diffie-Hellman Proof-of-Possession Algorithms |  |
| RFC 2986 | http://www.armware.dk/RFC/rfc/rfc2986.htmlPKCS #10: Certification Request Syntax Specification Version 1.7 |  |
| RFC 3280 | Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile |  |
| RFC 3369 | Cryptographic Message Syntax (CMS) |  |
| RFC 3647 | Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework |  |
| RFC 1591 | http://www.armware.dk/RFC/rfc/rfc1591.htmlDomain Name System Structure and Delegation |  |
| RFC 1608 | Representing IP Information in the X.500 Directory | Recommended |
| RFC 1612 | DNS Resolver MIB Extensions | Recommended |
| RFC 2230 | Key Exchange Delegation Record for the DNS |  |
| RFC 2276 | Architectural Principles of Uniform Resource Name Resolution |  |
| RFC 2535 | Domain Name System Security Extensions | Recommended |
| RFC 2592 | http://www.armware.dk/RFC/rfc/rfc2592.htmlDefinitions of Managed Objects for the Delegation of Management Script |  |
| RFC 2874 | http://www.armware.dk/RFC/rfc/rfc2874.htmlDNS Extensions to Support IPv6 Address Aggregation and Renumbering |  |
| ISO 10202-1:1991 | Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 1: Card life cycle | Recommended Reading |
| ISO 10202-7:1998 | Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 7: Key management |  |
