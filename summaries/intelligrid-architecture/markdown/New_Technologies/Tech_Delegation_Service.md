# Delegation Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Delegation_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Delegation Service

Provide
facilities to allow for delegation of access rights from requestors to
services, as well as to allow for delegation policies to be specified. When
dealing with delegation of authority from an entity to another, care should be
taken so that the authority transferred through delegation is scoped only to
the task(s) intended to be performed and within a limited lifetime to minimize
the misuse of delegated authority.

Based
upon the aforementioned definition, delegation involves Credential Conversion
and Authorization for Access Control services. There are two primary types of
delegation that need to be addressed:

·      
Delegation of Addresses: This type of delegation could occur due to
proxies, firewalls or gateways. The main requirements
of such delegation are to be able to provide an audit mechanism that allows
repudiation to the original address.   
  
A good example of why this is needed is the email SPAM problem that we face
today. It is difficult with address and email account spoofing to determine the
actual sender of the original SPAM message.

·      
Access Privilege Delegation would typically result in the transformation
of one entity’s privileges to some type of Role Based set of privileges. Once
the ability to audit the delegation is of primary importance.

Technological Assessment and
Relevant Specifications

It
is recommended that either RBAC or SAML be considered as appropriate.

Table 12: Relevant Specifications for the Delegation
Service

| Identification Number | Name | Comment |
| --- | --- | --- |
| BCP 65 | Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures |  |
| RFC 1034 | http://www.armware.dk/RFC/rfc/rfc1034.htmlDomain names - concepts and facilities |  |
| RFC 1507 | DASS - Distributed Authentication Security Service |  |
| RFC 1591 | http://www.armware.dk/RFC/rfc/rfc1591.htmlDomain Name System Structure and Delegation |  |
| RFC 1608 | Representing IP Information in the X.500 Directory |  |
| RFC 1612 | DNS Resolver MIB Extensions |  |
| RFC 2230 | Key Exchange Delegation Record for the DNS |  |
| RFC 2276 | Architectural Principles of Uniform Resource Name Resolution |  |
| RFC 2535 | Domain Name System Security Extensions |  |
| RFC 2592 | http://www.armware.dk/RFC/rfc/rfc2592.htmlDefinitions of Managed Objects for the Delegation of Management Script |  |
| RFC 2874 | http://www.armware.dk/RFC/rfc/rfc2874.htmlDNS Extensions to Support IPv6 Address Aggregation and Renumbering |  |
| RFC 3401 | Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS |  |
| RFC 3402 | Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm |  |
| RFC 3403 | Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database |  |
| RFC 3404 | Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource Identifiers (URI) |  |
| RFC 3405 | Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures |  |
| RFC 3761 | The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM) |  |
| STD 13 | Domain Name System | Recommended |
| ANSI INCITS 359-2004 | Role Based Access Control (RBAC) | Recommended |
| OASIS Security Technical Committee | SAML 2.0: Security Assertion Markup Language Version 2.0 | Recommended |
