# Audit Common Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Audit_Common_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Audit Common Service

An
audit service is responsible for producing records known as audit records which
contain audit record fields, which track security relevant events. The
resulting audit records may be reduced and examined in order to address several
key aspects of security within a security domain:

·       Audit records
and audit trails can be used to determine if a pre-scripted security policy is
being enforced.

·       Auditing and
subsequently reduction tooling are used by the security administrators within a
Security Domain to determine the Security Domain’s adherence to the stated
access control and authentication policies.

·       Audit records
that support the recording of usage data, secure storage of that data, analysis
of that data allows Security Domains to detect fraud and intrusion detection.

A
robust auditing mechanism enables a Non-repudiation service through the
creation of an audit trail.

There
are several well-understood audit issues that must be taken into account when
implementing the audit trail. The audit trails need to be analyzed to determine
vulnerabilities, establish accountability, assess damage
and recover the system. Manual analysis of audit trails though cumbersome is
often resorted to because of the difficulty to construct queries to extract
complex information from the audit logs. There are many tools that help in
browsing the audits. The major obstacle in developing effective audit analysis
tools is the copious amounts of data that logging mechanisms generate.

There
are three significant issues in creating an audit trail from various electronic
audit sources:

·      
A coherent and well-defined service to query an audit provider for audit
records.  
  
There needs to be mechanism through which queries for Audit records can be
issued. Although multiple protocols could carry such a request, such a
deployment strategy would require profile-mapping capabilities. While to date,
there is no security specific standards for such a service a general purpose
log query service could be used.

·      
A common and self-describing format for the audit records that can
account for specializations.  
  
The capability to query for audit records allows the start of the information
transfer. However, in order to re-construct an Audit Trail from multiple audit
record sources, there needs to be a common Audit Record format. The format
should be self-describing with standardized contents, but allow for additional
information to be conveyed. Some of the standardized fields might be:  
  
<AuditRecord>, <RecordType>,<AuthBy>,
<SubjectUid>,<TimeStamp>[[1]](Tech_Audit_Common_Service.htm#_ftn1)
, etc… However, there is no internationally recognized specification for such.
What is important here is that the record structure is self describing so that
a general purpose log query service could present log data intelligently.

·      
A well-defined mechanism to detect tampering with the transferred audit
records.  
  
One of the major purposes for audits/audit trails/audit records is provide an
authoritative mechanism to perform non-repudiation. One of the key issues with
providing non-repudiation in an authoritative manner is to prove that the audit
trail/record has not been tampered with.   
  
Although there is no recognized standard for such purposes, there is a
recognized approach to the problem. This is to digitally sign the audit record
or to provide a non-repeating serial number for the record. The actual
mechanics of the digital signature and how to convey the signature would be
issues for the common audit record format specification.

·      
The ability to correlate audit records from multiple audit sources.  
  
It is conceivable that different Security Domains would be in different time
zones. In order to create an inter-domain audit trail, it is necessary to be
able to correlate the times of the various audit records.   
  
Thus all audit records should have a timestamp whose reference time is UTC.
However, the timestamp itself may not have the accuracy to differentiate
between several audit records that occur within the same timestamp period.
Thus, it is also a requirement that an audit record serial number be provided
within each audit record. The combination of the timestamp and serial number
would need to be unique.  
  
Problems with correlation can also occur if the timestamp accuracies of the
audit records are not the same. Thus IntelliGrid Architecture should specify an appropriate accuracy
and time synchronization skew that is allowable.

·      
Determination of where to place auditing capability.  
  
Many security infrastructures/policies have difficulty identifying the types of
applications that need an audit trail. The use of the definition of IntelliGrid Architecture
security services allows the following base recommendations to be made.  
  
Audit records should be generated whenever/wherever the following security
services are invoked: Authorization for Access Control; Credential Conversion;
Credential Renewal; Delegation; Firewall Transversal; Identity Establishment;
Identity Mapping; Profile; Security Protocol Mapping; Setting and Verifying
User Authorization; Single Sign-On; Trust Establishment; User and Group
Management.

·      
Determination of the minimum-maximum audit record time availability.
There is a need to determine/specify through policy a minimum amount of time
that an audit record must be maintained within the audit trail system. In IntelliGrid Architecture environment, this time would need to be specified so that non-repudiation
for an appropriate period of time can be provided.  
if !supportLineBreakNewLine?  
endif?

### Audit Technologies/Specifications

Table
1 represents a set of specifications and/or standards that are relevant to the
understanding of the issues regarding the audit service. Those specifications
marked as Recommended or Recommended Reading should be considered as materials
that should be considered prior to actually implementing the audit service.

Table 1: Relevant Standards/Specifications
relevant to the Audit Service

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| ISO/IEC 10164-8:1993 | Information technology -- Open Systems Interconnection -- Systems Management: Security audit trail function | Recommended |
| ISO/IEC 10181-7:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Security audit and alarms framework |  |
| ISO/IEC 18014-1:2002 | Information technology -- Security techniques -- Time-stamping services -- Part 1: Framework | Recommended Reading |
| ISO/IEC 18014-2:2002 | Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens |  |
| ISO/IEC 18014-3:2004 | Information technology -- Security techniques -- Time-stamping services -- Part 3: Mechanisms producing linked tokens |  |
| 21 CFR Part 11 | Guidance for Industry Part 11, Electronic Records; Electronic Signatures - Scope and Application | Recommended Reading |

### Technological Assessment

An
inspection of Table 1 shows that there are no technology specific
specifications/standards that address the issues/problems previously discussed
in this section.
