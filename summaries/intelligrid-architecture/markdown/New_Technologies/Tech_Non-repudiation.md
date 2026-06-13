# Non-repudiation

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Non-repudiation.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Non-repudiation

This
service represents the ability of a security domain to provide proof that a
given exchange action has occurred. This ability is used to resolve disputes
with other entities that claim that the action did not occur, thus
non-repudiation. In order to provide this service, a strong audit service must
be present within the security domain.

Key
definition:

**repudiation:**
In cryptosystems, the denial by one of the entities involved in a communication
of having participated in all or part of the communication.

In
order to provide this service, strong audit capabilities need to be in place
for Identity Establishment, Access Control, Credential Conversion, and Identity
Mapping. Without an appropriate level of audit capability on these other
services, non-repudiation will not be able to be performed.

Non-repudiation
is typically a manual process of retrieving the relevant audit records,
analyzing those records, creating a report that summarizes those records and
the conclusion. Thus, strong policies and procedures must be put in place to
accomplish non-repudiation as well.

Technological Assessment and
Relevant Specifications

Table
22 shows the relevant specifications regarding non-repudiation. In order to
provide the non-repudiation service, it is suggested that a non-repudiation
framework similar to what is specified in ISO/IEC 10181-4 be created. It is
further recommended that SAML be used and the non-repudiation capabilities of
SAML be integrated into the created framework.

Table 22: Relevant Specification
regarding non-repudiation

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| ISO 9735-5:2002 | Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 5: Security rules for batch EDI (authenticity, integrity and non-repudiation of origin) |  |
| ISO/IEC 10181-4:1997 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework | Recommended |
| ISO/IEC 13888-1:1997 | Information technology -- Security techniques -- Non-repudiation -- Part 1: General | Recommended Reading |
| ISO/IEC 13888-2:1998 | Information technology -- Security techniques -- Non-repudiation -- Part 2: Mechanisms using symmetric techniques |  |
| ISO/IEC 13888-3:1997 | Information technology -- Security techniques -- Non-repudiation -- Part 3: Mechanisms using asymmetric techniques |  |
| ISO/IEC TR 13335-5 | Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security |  |
| WC3 | XML Key Management Specification (XKMS 2.0) Bindings |  |
| OASIS Security Technical Committee | Bindings for OASIS Security Assertion Markup Language (SAML) V2.0  Available from:  http://www.oasis-open.org/committees/download.php/6773/sstc-saml-bindings-2.0-draft-11-diff.pdf | Draft that specifies how to bind SAML over various protocols. Highly recommended. |
