# Confidentiality

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Confidentiality.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Confidentiality

Protect
the confidentiality of the underlying communication (transport) mechanism, and
the confidentiality of the messages or documents that flow over the transport
mechanism in an OGSA compliant infrastructure. The confidentiality requirement
includes point-to-point transport as well as store-and-forward mechanisms.

Key
definitions:

**confidentiality:
1.** Of classified or sensitive data, the degree to which the data have not
been compromised; *i.e.,* have not been made available or disclosed to
unauthorized individuals, processes, or other entities. [After 2382-pt.8] **2.**
Assurance that information is not disclosed to unauthorized persons, processes,
or devices. [INFOSEC-99] **3.** A property by which information relating to
an entity or party is not made available or disclosed to unauthorized
individuals, entities, or processes. [T1.Rpt22-1993]

There
are two main mechanisms to provide confidentiality for electronically
transmitted information: encryption or transmission over a secure
infrastructure.

1.1.1.1.1.5                    
Encryption

It
is important to realize that there is no 100% effective mechanism to protect electronically
transmitted information for an indefinite length of time. Initially, when the
Data Encryption Standard (DES) was specified, it was thought that 56-bit
encryption protection could protect information for 20-30 years. However, with
the increase in computational capability, and the decrease in cost for that
capability, in 1999 DES was cracked in under 22 hours (see CONF-02) . In 2004, DES could be cracked in under
5 minutes considering CPU performance increase only.

|  |  |  |  |
| --- | --- | --- | --- |
| Estimated time to crack linear-symmetric encryption technologies | | | |
| Number of bits in encryption key | Estimated time to crack using current technology | | |
|  | DES | Triple DES (3DES) | AES |
| 56 | 4 min | 20 days | 20 days |
| 64 | 1024 min | 70 days | 70 days |
| 128 |  | | 100 days |
| 256 |  | | 200 days |
| 512 |  | | 400 days |

To
respond to the new reality, NIST and several standards
organizations (in particular IEEE) developed a more advanced and secure
encryption standard known as the Advanced Encryption Standard (AES).

“In
comparison, DES keys are 56 bits long, which means that there are approximately
7.2 x 1016 possible DES keys. Thus, there are on the order of 10 (21) times
more AES 128-bit keys than DES 56-bit keys. Assuming that one could build a
machine that could recover a DES key in a second (i.e. try 255 keys per second),
then it would take that machine approximately 149 thousand-billion (149
trillion) years to crack a 128-bit AES key. To put this into perspective, the
Universe is believed to be less than 20 billion years old. NIST believes that
AES will remain secure beyond the next twenty years. AES implementations will
also be exportable, and AES implementations in proprietary systems will just
need a one-time review prior to export” [CONF-01]

The
above claim is similar to the claims made by DES when it was first introduced.
Whereas DES and Triple-DES (3DES) have had almost twenty years of deployment
prior to replacement due to “crackability”, the advent of Quantum Computers
(see CONF-03) may not allow the modern encryption algorithms the same. If
Quantum Computers were available today, using Grover’s Algorithm (see CONF-04)
it could be extrapolated that even 512 bit DES could be cracked in
approximately 1 second. AES is more complex and is less prone to Grover’s Algorithm, however the NIST statement (CONF-01) will definitely
not be true in the near-term future.

The
advent of Quantum Computers raises the issue of how to make encryption
effective. Even without the advent of Quantum technology, the following
recommendations are valid:

·      
Choose a modern encryption algorithm for the purposes of encryption.  
  
There are many factors that enter into an appropriate algorithmic choice. The
factors that need to be considered are the additional CPU processing that the
use of encryption will require and the bandwidth/transmission performance
characteristics desired.  
  
At the NERC Data Exchange Working Group meeting in April 2004, the following
results were presented for Secure IEC-60870-6 TASE.2 (ICCP).  
  
The additional CPU performance requirements, for the use of TLS and AES 256,
represented an increase from 1% to 1.35% for encryption and 1% to 1.41% for
decryption (percentages based upon total CPU being 100%). It was also found
that AES 256 was more CPU efficient than either DES or 3DES.  
  
It was found that the bandwidth overhead increased by the size of certificates
exchanged, but only increased 1% in regards to normal ICCP traffic once the
initial connection and symmetric keys were established.

·      
When using encryption, make sure that the technology used to “negotiate”
encryption can negotiate multiple encryption algorithms.

·      
If possible, make sure that the negotiation can be upgraded to newer
encryption algorithms as new, more robust algorithms, become available.

·      
Make use of technologies where the encryption keys can dynamically be
re-negotiated without interrupting the communication information flow.

Table 7: Reference Relevant to Encryption Technology

|  |  |
| --- | --- |
| CONF-01 | **NIST Announces New Government Aes Encryption Standard - Technology Information**  Available from: http://articles.findarticles.com/p/articles/mi\_m0BNO/is\_2000\_Nov/ai\_66297312 |
| CONF-02 | Jason Meserve , DES code cracked in record time, Network World, 01/20/99  Available from:  http://www.nwfusion.com/news/1999/0120cracked.html |
| CONF-03 | Aaron Ricadela, Quantum’s Next Leap, Information Week, May 10, 2004 |
| CONF-04 | Matias Castro ,What Use is My Quantum Computer Now I Have it?    Available From:  http://www.doc.ic.ac.uk/~nd/surprise\_97/journal/vol2/mjc5/ |

Technological Assessment and
Specifications

There
are several different mechanisms through which to develop assessments regarding
encryption. For the purposes of this section, applicability to specific
communication media will be used.

In
general, it is suggested to make use of X.509 certificates to provide
public/private key encryption exchanges when possible. Such a choice will ease
integration with other certificate technologies (e.g. management) that are
being recommended as part of other security services.

When
X.509 certificate use is not appropriate, it is suggested that RFC 2898
(PKCS#5) be utilized. This allows encryption to be established based upon
username/passwords.

Protocol Basis

In
general, it is recommended to use the appropriately specified encryption
standard associated with the protocol (e.g. HTTPS for HTTP). There are further
recommendations for TCP/IP:

**TCP/IP
Transmissions**

It
is recommended that TLS with AES (RFC 3268) or PPP Encryption Control Protocol
(RFC 1968) be used to provide encryption. These represent the most modern and
secure mechanism.

Media

**Serial**

If
the path of the serial link does not provide enough confidentiality or the
protocol in use over the link, and confidentiality is still desired then the
following is recommended:

·      
If the peers can be upgraded to support encryption, then this should be
the preferred approach.

·      
For legacy systems, that are not upgradeable, it is suggested that
external hardware be applied. Further it is recommended that AGA-12 be evaluated
for this purpose.

**Ethernet,
SONET, FDDI, etc.**

It
is recommended to make use of VPN technology when possible.

**WI-FI
and Wireless Technologies**

The
Web Encryption Protocol (WEP) specified in IEEE 802.11b has been proven to be
vulnerable and to not provide adequate protection. New versions of WI-FI and
wireless technologies are coming equipped with AES encryption. It is the AES
encryption that is recommended. Further it is recommended that WPA2/80211.i be
adopted in order to achieve the implementation of this recommendation.

It
is further recommended that any legacy (e.g. WEP based) WI-FI equipment be
replaced or upgraded, as the vulnerabilities are well known and not manageable.

Table 8: Encryption Related Specifications/Standards

| Identification Number | Name | Comment |
| --- | --- | --- |
| RFC 3370 | Cryptographic Message Syntax (CMS) Algorithms |  |
| RFC 3447 | Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1 |  |
| RFC 2898 | PKCS #5: Password-Based Cryptography Specification Version 2.0 | Recommended when certificate exchange is not appropriate. |
| RFC 1968 | The PPP Encryption Control Protocol (ECP) |  |
| RFC 2246 | The TLS Protocol Version 1.0 |  |
| RFC 2409 | The Internet Key Exchange (IKE) | Used for VPNs |
| RFC 1040 | Privacy enhancement for Internet electronic mail: Part I: Message encipherment and authentication |  |
| RFC 2946 | Telnet Data Encryption Option |  |
| RFC 2440 | OpenPGP Message Format |  |
| RFC 1423 | Privacy Enhancement for Internet Electronic Mail: Part III: Algorithms, Modes, and Identifiers |  |
| RFC 2408 | Internet Security Association and Key Management Protocol (ISAKMP) | Used for VPNs |
| RFC 2510 | Internet X.509 Public Key Infrastructure Certificate Management Protocols |  |
| RFC 3268 | Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS) |  |
| RFC 2093 | Group Key Management Protocol (GKMP) Specification |  |
| RFC 2459 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |  |
| RFC 2040 | The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms |  |
| FIPS 197 | Federal Information Processing Standards Publication 197, November 26, 2001, Specification for the Advanced Encryption Standard (AES)  Available from: http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf | Recommended |
| RSA PKCS #12 | Personal Information Exchange Syntax Standard, version 1.0. |  |
| RSA PKCS #8 | Private-Key Information Syntax Standard |  |
| IEEE 802.11b | Web Encryption Protocol |  |
| AGA-12 | Cryptographic Protection of SCADA Communications General Recommendations. |  |
| WPA | WI-FI Protected Access |  |
| IEEE 802.11i | Security for Wireless Networks |  |
| WPA2 | WI-FI Protected Access Version 2 |  |

Table 9: Digital Certificate Related
Specifications/Standards

| Identification Number | Name | Comment |
| --- | --- | --- |
| RFC 2510 | Internet X.509 Public Key Infrastructure Certificate Management Protocols. C. Adams, S. Farrell. March 1999. |  |
| RFC 2511 | Internet X.509 Certificate Request Message Format. M. Myers, C. Adams, D. Solo, D. Kemp. March 1999. |  |
| RFC 2527 | Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework. S. Chokhani, W. Ford. March 1999. |  |
| RFC 2560 | X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP. M. Myers, R. Ankney, A. Malpani, S. Galperin, C. Adams. June 1999. |  |

Communication Path Selection

There
is a mechanism of mitigating the need to encryption. This is to evaluate or
provide a communication path that inherently provides enough protection (see
the Path Routing and QOS service for further information).
