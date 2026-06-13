# Identity Establishment

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Identity_Establishment_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Identity Establishment Service

An
identity establishment (e.g. identity authentication) service is concerned with
verifying proof of an asserted identity. The implementation of the service must
allow for multiple identity authentication mechanisms (e.g. identity tokens) to
be utilized. Additionally, the service needs to provide a mechanism to allow
the information from various identity tokens/identity authentication mechanisms
to be electronically conveyed.

The
requirement that the Identity Establishment service be agnostic in regards to
technology can be easily demonstrated. One Security Domain may make use of a
User ID/password combination as an identity token. Another Security Domain may
require the use of Kerberos based identity tokens. It is the Security
Management Infrastructure (SMI) and the Security Domain’s security policies
that will determine the actual identity token(s) used and the mechanism(s)
through which they are conveyed.

Key
definitions:

**identity
authentication:** The performance of tests to enable a data processing system
to recognize entities. *Note:* An example of identity authentication is
the checking of a password or identity token. [2382-pt.8]

**identity
token: 1.** A device, such as a metal key or smart card, used for identity
authentication. [After 2382-pt.8] **2.** [A] Smart card, metal key, or other
physical object used to authenticate identity. [INFOSEC-99]

**identity
validation:** Tests enabling an information system to authenticate users or
resources. [INFOSEC-99]

Identity Establishment for
Physical Assets

Physical
access control should be based upon multi-factor Identity Establishment. The
use of multi-factor authentication, using the appropriate technologies can
provide a significant security advantage above and beyond simple identity
cards. Additionally, the selection and creation of physical access control
policies and procedures would needs to include the capability to manage and
revoke access privileges easily. This would typically indicate the need for
some type of token/id that can be managed/changed.
However, if only the picture matching the holder of the identity card determines
access, there is a high probability that such access control mechanisms can be
falsified. Thus, to improve access security there should be another security
factor used in order to authorize access.

This
“other-factor” should be “something the individual knows” (e.g.
username/password) or combination code. However, typically username/passwords
or combination codes can be compromised through observation or garbage diving.
Therefore, it would be recommended that some type of electronic mechanism, with
verification/challenge be implemented. The most widely deployed example of this
would be the use of a Smart-ID card (e.g. a card that electronically authorizes
the holder to enter a combination and that explicitly bound to the identity of
the holder) and a combination lock. Only the proper Smart-ID badge
authorization allows the combination to be entered into the lock, which then
enables access. The side benefit of the use of such technology is that an audit
trail of access can be created electronically. Additionally, management issues
(especially revocation of access privileges) are eased since the Smart-ID card
can be revoked thereby disallowing access.

Should
a Security Domain decide to perform electronic auditing of physical access
(recommended), then appropriate audit trail time-stamping techniques need to be
utilized (see the audit service section).

Computational Resources

Identity
establishment, for computational resources, is directly related to the types of
credentials that are in use within a Security Domain. The definition of the
credentials that IntelliGrid Architecture may be using may be found in the Credential Renewal
section (see page 2-20). The credential types used to establish identity are:
addresses and address resolution, username/passwords, smart cards, digital
certificates, and biometric identifications.

The
issue with computational resource identification establishment is that of
architecting a solution that creates a framework for authentication. Table 15
and Table 16 list relevant references and specifications that may aid in the
construction of such a framework within a security domain.

Table 15: General References Regarding
Identity Establishment and Identity Infrastructure

**A
National-Scale Authentication Infrastructure**. R. Butler, D.
Engert, I. Foster, C. Kesselman, S. Tuecke, J. Volmer, V. Welch. *IEEE
Computer*, 33(12):60-66, 2000.

**An Online
Credential Repository for the Grid: MyProxy**. J. Novotny, S.
Tuecke, V. Welch. *Proceedings of the Tenth International Symposium on
High Performance Distributed Computing (HPDC-10)*, IEEE Press, August 2001.

**A Community
Authorization Service for Group Collaboration**. L. Pearlman,
V. Welch, I. Foster, C. Kesselman, S. Tuecke. *Proceedings of the IEEE 3rd
International Workshop on Policies for Distributed Systems and Networks*,
2002.

**X.509 Proxy
Certificates for Dynamic Delegation**. V. Welch, I. Foster, C.
Kesselman, O. Mulmo, L. Pearlman, S. Tuecke, J. Gawor, S. Meder, F.
Siebenlist. *3rd Annual PKI R&D Workshop*, 2004.

Table 16: Relevant Specifications regarding
Identification Frameworks

| Identification Number | Name | Comment |
| --- | --- | --- |
| ISO/IEC 10181-2:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Authentication framework | Recommended |
| ISO/IEC 10181-4:1997 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Non-repudiation framework | Recommended |
| ISO/IEC 10181-1:1996 | Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Overview | Recommended |
| ISO 10202-8:1998 | Financial transaction cards -- Security architecture of financial transaction systems | Recommended Reading |

Technological Assessment and
Relevant Specifications

The
following section discusses issues and potential general resolution to the
issues regarding the use of any particular identification mechanism. In
general, two-factor authentication is desired.

Address Resolution

The
most prevalent issue in using address resolution as an identification mechanism
is address spoofing. This attack is easy to generate and is well documented.
Therefore, such an identification mechanism should not be used on its own. It
must be augmented with another factor to actually establish the identity.

Address
resolution is a worthwhile qualifier for actions/information exchanges that are
only supposed to occur between certain peers. However, this is not a reasonable
mechanism for inter-domain exchanges since neither domain controls the other
domain’s address allocation/changes.

Username/Password

This
is a typical mechanism employed by Web based interfaces (especially for
customers interfacing for retrieval of billing information). However, the use
of cookies or password caches (e.g. the prompt to remember the username
password) represents an issue that should be addressed by the addition of a
challenge/response mechanism.

The
challenge response should be user selectable/definable so that they can
remember the response when prompted.

Smart Cards

The
references given previously in this section give a large amount of guidance in
the selection of SMART-CARDS that can be used in the implementation of physical
or cyber access control. The smart card industry embraces ISO 7816 as one of
the prevalent smart card specification and this is the recommended base specification
for smart cards.

However,
ISO 7816 does not specify a programmatic interface to such cards that is
portable. Therefore, it is recommended that the Java CardTM Platform
Specification be used in conjunction with ISO 7816 technology.

The remaining issue is how much storage to deploy on
the smart cards. The Gartner Group published the information found in Figure 2.
At this juncture there is no recommendation in regards to the amount of storage
to deploy.

Table 17: Relevant Standards Concerning Smart Cards

| Identification Number | Name | Comment |
| --- | --- | --- |
| ISO/IEC 7816-1:1998 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 1: Physical characteristics |  |
| ISO/IEC 7816-10:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 10: Electronic signals and answer to reset for synchronous cards |  |
| ISO/IEC 7816-11:2004 | Identification cards -- Integrated circuit cards -- Part 11: Personal verification through biometric methods |  |
| ISO/IEC 7816-15:2004 | Identification cards -- Integrated circuit cards with contacts -- Part 15: Cryptographic information application |  |
| ISO/IEC 7816-3:1997 | Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 3: Electronic signals and transmission protocols |  |
| ISO/IEC 7816-3:1997/Amd 1:2002 | Electrical characteristics and class indication for integrated circuit(s) cards operating at 5 V, 3 V and 1,8 V |  |
| ISO/IEC 7816-4:1995 | Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 4: Interindustry commands for interchange |  |
| ISO/IEC 7816-4:1995/Amd 1:1997 | secure messaging on the structures of APDU messages |  |
| ISO/IEC 7816-5:1994 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 5: Numbering system and registration procedure for application identifiers | Highly recommended reading as part of the management (e.g. User/Group Management service) |
| ISO/IEC 7816-7:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 7: Interindustry commands for Structured Card Query Language (SCQL) (available in English only) |  |
| ISO/IEC 7816-8:1999 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 8: Security related interindustry commands |  |
| ISO/IEC 7816-9:2000 | Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional interindustry commands and security attributes |  |
| Java Card | Java Code Smart Card API | Can make use of ISO 7816 Based smart cards. Referenced by Global Platform and ETSI. |
| Java Card | Java Card Platform Specification v 2.2.1    Available from:  http://java.sun.com/products/javacard/specs.html |  |
| NIST GSC-IS | The NIST Interagency Report 6887 - 2003 edition (Government Smart Card-Interoperability Specification) Version 2.1  Available from:  http://csrc.nist.gov/publications/nistir/nistir-6887.pdf | Recommended Reading. Specifies the use of ISO 7816 GSM based implementations. |
| Smart Card Alliance | Smart Card Primer    Available from: http://www.smartcardalliance.org | Recommended Reading |
| Smart Card Alliance | Privacy and Secure Identification Systems: The Role of Smart Cards as a Privacy-Enabling Technology ­     Available from: http://www.smartcardalliance.org | Recommended Reading |
| Smart Card Alliance | Government Smart Card Handbook    Available from: http://www.smartcardalliance.org | Recommended Reading. Specifies the use of ISO 7816 based implementations. |

![](../IECSA_Volumes/IECSA_VolumeIV_AppendixD_files/image004.jpg)

Figure 2:
Estimated Smart Card Storage Costs

Digital Certificates

The
industry accepted digital certificate is an X.509 certificate. This is the
certificate format that should be used by IntelliGrid Architecture when applicable. There are some
issues in identifying a certificate:

·      
There is an issue in regards to how to uniquely identify a certificate.
There are many fields that could be used, however only the certificate
Thumbprint is truly unique. All other fields could be non-unique. Therefore, it
is the thumbprint that should be used to identify and match certificates.

·      
Enunciation of lifetime expiration (see Credential Renewal service).

·      
Policy issues in regards to use will need to be addressed. The NERC
e-Marc certificate policy discusses many of these issues. It is recommended
that the e-Marc policy be used as a basis for certificate usage.   
  
It is worthwhile to note that the NERC policy does not allow the same
certificate to be duplicated. Should a security domain adopt this as a policy,
the number of certificates required (e.g. in the case of redundancy) will be
higher.

·      
A policy in regards to how applications should react in the case that an
in use certificate is revoked.  
  
Revocation is basically caused when the integrity of a certificate has been
compromised (e.g. the private certificate may have been stolen). Since none of
the revocation protocols give an indication that could be used to determine if
the certificate was compromised prior to use, the safe option is to terminate
use of the certificate upon revocation. This may cause information exchange to
be terminated if fail-over procedures are not made part of the policy.

Table 18: Public Key Infrastructure (PKI) Related
Specification/Standards

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| RFC 2898 | PKCS #5: Password-Based Cryptography Specification Version 2.0. B. Kaliski. September 2000. |  |
| RFC 2985 | PKCS #9: Selected Object Classes and Attribute Types Version 2.0. M. Nystrom, B. Kaliski. November 2000. |  |
| RFC 2986 | PKCS #10: Certification Request Syntax Specification Version 1.7. M. Nystrom, B. Kaliski. November 2000. |  |
| RFC 3280 | Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile |  |
| ISO/IEC 9594-8:1998 | Information technology -- Open Systems Interconnection -- The Directory: Authentication framework | Definition of X.509 Certificate is found here. |
| ISO/IEC 9594-8:2001 | Information technology -- Open Systems Interconnection -- The Directory: Public-key and attribute certificate frameworks |  |
| X.521 | TMN PKI - Digital certificates and certificate revocation lists profiles |  |
| NERC | Certificate Policy for the Energy Market Access and Reliability Certificate (e‑MARC) Program Version 2.4  Available from:  ftp://www.nerc.com/pub/sys/all\_updl/cip/pkitf/e-MARC-PKI\_draft\_version\_V2-4b\_March\_2003-rev1.doc |  |

Digital Signatures

Typically
considered a subset of Digital Certificates, as certificates are required in
order to digitally sign, these have their own benefit for identification
purposes. In instances where bandwidth or packet size is a limiting factor, a
digital signature can be used in place of a certificate.

In
IEC 61850, for GOOSE, this signature, in conjunction with address resolution
would provide two-factor authentication if properly implemented. However, this
raises the issue that:

·      
Digital signatures should not repeat often in order to prevent spoofing.

There
are several different interpretations in regards to what a digital signature
is.   
  
It is recommended that RFC 2313 be used as the definitive definition for a
digital signature algorithm:  
  
“For digital signatures, the content to be signed is first reduced to a message
digest with a message-digest algorithm (such as MD5), and then an octet string
containing the message digest is encrypted with the RSA private key of the signer
of the content. The content and the encrypted message digest are represented
together according to the syntax in PKCS #7 to yield a digital signature.”  
  
However, it is recommended that RFC 2437 be the actual Cryptography
specification used[[4]](Tech_Identity_Establishment_Service.htm#_ftn4)

Table 19: Relevant Specifications for Digital Signatures

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| RFC 2313 | http://www.armware.dk/RFC/rfc/rfc2313.htmlPKCS #1: RSA Encryption Version 1.5 |  |
| RFC 2315 | PKCS #7: Cryptographic Message Syntax Version 1.5 |  |
| RFC 2437 | PKCS #1: RSA Cryptography Specifications Version 2.0 |  |

Biometrics

There
is a large body of biometric work occurring. The standards development is
largely being performed in ISO JTC1 SC37. The total scope of work can be
obtained from www.jtc1.org. However, some of the major work items have been
included in Table 20. The major focus of ISO JTC1 SC37 is focused on the
biometric aspects of fingerprints and facial images. However, from a practical
perspective fingerprint biometrics represents a much lower cost alternative
than facial and therefore would be recommended for IntelliGrid Architecture deployment.

It
is also suggested that the biometric data be encoded on a smart-card so that
two-factor authentication is achievable.

Table 20: Relevant References
regarding Biometrics

|  |  |
| --- | --- |
| Global Analytic Information Technology Services | **Fingerprint Recognition**  **Available from:**http://www.gaits.com/biometrics\_fingerprint.asp |
|  | **Ralph Gross, Quo Vadis Face Recognition? The current state of the art in Face Recognition**    **Available from:**http://dagwood.vsam.ri.cmu.edu/FaceRecognition/ |
|  | **Philip E. Agre, Your Face is Not a Bar Code: Arguments Against Automatic Face Recognition in Public Places.** |
| ISO JTC1 SC37 | **SD 2 - Harmonized Biometric Vocabulary** |
| ISO JTC1 SC37 | **1.37.19784.1 BioAPI - Biometric Application Programming Interface** |
| ISO JTC1 SC37 | **1.37.19794 - Biometric Data Interchange Format** |
| ISO JTC1 SC37 | **1.37.1974.3 Biometric Data Interchange Format - Part 3: Finger Pattern Spectral Data** |
| ISO JTC1 SC37 | **1.37.1974.4 Biometric Data Interchange Format - Part 4: Finger Image Data** |
| ISO JTC1 SC37 | **1.37.1974.5 Biometric Data Interchange Format - Part 5: Face Image Data** |

Table 21: Relevant Specification regarding Biometrics and
Smart Cards

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| ISO/IEC 7816-11:2004 | Identification cards -- Integrated circuit cards -- Part 11: Personal verification through biometric methods | Recommended Reading |
|  |  |  |
