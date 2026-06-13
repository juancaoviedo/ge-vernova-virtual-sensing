# Protocol-Specific Recomm

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Security_Protocol.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Protocol Specific Recommendations

The previous sections have dealt with
security from a generalized service perspective or from a “physical” network
topology perspective.  However, it is useful to discuss specific security
recommendations for particular protocols that may be prevalent in the IntelliGrid Architecture.
The following are discussed:

* [Security for Network
  Layer Technologies](Anl_Security_Protocol.htm#Security_for_Network_Layer_Technologies)
* [Security Standards from
  WG15 in IEC TC57](Anl_Security_Protocol.htm#Security_Standards_from_WG15_in_IEC_TC57)
* [Security for
  IEC TC57-based Application Protocols](Anl_Security_Protocol.htm#Security_for_IEC_TC57-based_Application_Protocols)

## Security for Network Layer Technologies

There are two prevalent routing network
layers that can be envisioned within IntelliGrid Architecture environment: Internet Protocol
Version 4 (IPv4) and Internet Protocol Version 6 (IPv6). There four(4) basic
security functions that could be provided within the network layer: 
Confidentiality, packet level authentication, integrity,
and address protection.  Each of the prevalent network protocols will
be discussed.

### IPv4

IPv4 (RFC 791) is the currently most widely
deployed version the Internet Protocol.  IPv4 is relatively simple and has
NO Security provisions within the protocol itself.  However, VPN
technologies,  IPSEC (RFC 1826 and RFC 1827)
and ESP (RFC 2406) provide the additional security services needed at the
network layer.

Confidentiality is provided via RFC 1827 and
RFC 2406.

Packet level authentication is provided via
RFC 1826.

Integrity is provided by RFC 1826.

Address protection is provided by RFC 1827
and RFC 2406.

### IPv6

IPv6 (RFC 2460 ) is not interoperable with
IPv4, however it was designed to expand the number of available Internet Addresses from 232 to 2128
(e.g. 4 bytes versus 16 bytes of addressing). Besides the increase in address
space, security extensions were added: Authentication and Encapsulation
Security Payload.  Thus incorporating several of the key security
provisions of RFC 1826 and RFC 2406 into the IPv6 protocol.

Thus Confidentiality, packet authentication,
and integrity can all be provided through the use of the appropriate fields of
IPv6.  However, IPv6 does not protect network addressing information since
the IP Address information occurs before the
security extensions in the IPv6 packet.  Thus if source/destination
address protection is still desired, VPN or tunnel extensions still need to be
used.

Tunneling can occur via the current VPN
technologies (RFC 1826 and RFC 1827 support tunneling of both IPv4 and IPv6) or
RFC 3053 (IPv6 Tunnel Broker) could be utilized.

“The growth of IPv6 networks started mainly
using the transport facilities offered by the current Internet.  This led
to the development of several techniques to manage IPv6 over IPv4
tunnels.    At present most of the 6bone network is built using
manually configured tunnels over the Internet.  The main drawback of this
approach is the overwhelming management load for network administrators, who
have to perform extensive manual configuration for each tunnel.”[[13]](Anl_Security_Protocol.htm#_ftn13)

Thus the selection of technology is dependent
upon the inter-domain connectivity that is being provided.  The current
Internet is a “4bone” network and thus VPN technology would need to be
deployed.  However, if a “6bone” network were in use, then RFC 3053 would
be the preferred approach.

Current deployment technologies would lend
itself to IPv6 use for Inter-domain exchanges and not intra-domain.  Most
intra-domain addressing is still IPv4.

### Transport Layer Technologies (TCP)

The Transmission Control Protocol (RFC 793)
can be used over IPv4 or IPv6 (slight modifications required to interface properly with IPv6).  However, there are no
security provisions within RFC 793 itself.  Thus Transport Layer Security
(TLS)[[14]](Anl_Security_Protocol.htm#_ftn14) is
recommended to provide transport level authentication, integrity, and
confidentiality. 

There is ongoing work in IEC TC57 WG15 to
specify implementation guidelines for TLS, and these should be implemented as
appropriate.

If transport port number protection is
desired, then a network layer security mechanism must be used.

## Security Standards from WG15 in IEC TC57

Since it was formed, WG15 has undertaken the development
of security standards for the four communication protocols: IEC 60870-5, its
derivative DNP, IEC 60870-6 (ICCP), and IEC 61850. These security standards must
meet different security objectives for the different protocols, which vary
depending upon how they are used. Some of the security standards can be used
across a few of the protocols, while others are very specific to a particular
profile. The different security objectives include authentication of entities
through digital signatures, ensuring only authorized access, prevention of
eavesdropping, prevention of playback and spoofing, and some degree of intrusion
detection. For some profiles, all of these objectives are important; for others,
only some are feasible given the computation constraints of certain field
devices, the media speed constraints, the rapid response requirements for
protective relaying, and the need to allow both secure and non-secured devices
on the same network.

This work will be published by the IEC as IEC 62351,
Parts 3-6, titled:

·        
**IEC 62351-3: Data and Communication Security –** **Profiles
Including TCP/IP** (*these security standards cover those profiles used by
ICCP, IEC 60870-5 Part 104, DNP 3.0 over TCP/IP, and IEC 61850 over TCP/IP*)

·        
**IEC 62351-4: Data and Communication Security –** **Profiles
Including MMS** (*these security standards cover those profiles used by ICCP
and IEC 61850*)

·        
**IEC 62351-5: Data and Communication Security – Security for IEC
60870-5 and Derivatives (i.e. DNP 3.0)** (*these security standards cover
both serial and networked profiles used by IEC 60870-5 and DNP*)

·        
**IEC 62351-6: Data and Communication Security –** **Security
for IEC 61850 Peer-to-Peer Profiles** (*these security standards cover those
profiles in IEC 61850 that are not based on TCP/IP – GOOSE, GSSE, and SMV*)

The interrelationship of these security standards and the
protocols are illustrated in the following figure.

if !vml?![](Anl_Security_Protocol_files/image002.gif)endif?

Figure: Interrelationship of IEC
62351 Security Standards and the TC57 Protocols

Draft documents of the security standards have been
developed and are being reviewed by the WG15 members. These draft documents have
not yet been voted on by the IEC, but the expectation is that initial voting
(Committee Draft for Vote) on most of them will take place in the first half of
2005, with the final voting possibly by the end of 2005.

### IEC 62351-3: Profiles Including TCP/IP

IEC 62351-3 provides security for any profile that
includes TCP/IP. Rather than re-inventing the wheel, it specifies the use of TLS
which is commonly used over the Internet for secure interactions, covering
authentication, confidentiality, and integrity. This part describes the
parameters and settings for TLS that should be used for utility operations.

Specifically, IEC 62351-3 protects against eavesdropping
through TLS encryption, man-in-the-middle security risk through message
authentication, spoofing through Security Certificates (Node Authentication),
and replay, again through TLS encryption. However, TLS does not protect against
denial of service. This security attack should be guarded against through
implementation-specific measures.

### IEC 62351-4: Security for Profiles That Include MMS

IEC 62351-4 provides security for profiles that include
the Manufacturing Message Specification (MMS) (ISO 9506), including TASE.2
(ICCP) and IEC 61850. It primarily works with TLS to configure and make use of
its security measures, in particular, authentication: the two entities
interacting with each other are who they say they are.

It also allows both secure and non-secure profiles to be
used simultaneously, so that not all systems need to be upgraded with the
security measures at the same time.

### IEC 62351-5: Security for IEC 60870-5 and Derivatives (i.e. DNP 3.0)

IEC 62351-5 provides different solutions for the serial
version (IEC 60870-5-101) and for the networked versions (IEC 60870-5-104 and
DNP 3.0). Specifically, the networked versions that run over TCP/IP can utilize
the security measures described in IEC 62351-3, which includes confidentiality
and integrity provided by TLS encryption. Therefore, the only additional
requirement is authentication.

The serial version is usually used with communications
media that can only support low bit rates or with field equipment that is
compute-constrained. Therefore, TLS would be too compute-intense and/or
communications-intense to use in these environments. Therefore, the only
security measures provided for the serial version include some authentication
mechanisms which address spoofing, replay, modification, and some denial of
service attacks, but do not attempt to address eavesdropping, traffic analysis,
or repudiation that require encryption. These encryption-based security measures
could be provided by alternate methods, such as VPNs or “bump-in-the-wire”
technologies, depending upon the capabilities of the communications and
equipment involved.

### IEC 62351-6: Security for IEC 61850 Peer-to-Peer Profiles

IEC 61850 contains three protocols that are peer-to-peer
multicast datagrams on a substation LAN and are not routable. The messages need
to be transmitted within 4 milliseconds and so that encryption or other security
measures which affect transmission rates are not acceptable. Therefore,
authentication is the only security measure included, so IEC 62351-6 provides a
mechanism that involves minimal compute requirements for these profiles to
digitally sign the messages.

## Security for IEC TC57-based Application Protocols

### IEC 60870-5/DNP

IEC TC57 WG15 currently has a work item to
address security for 870-5 and DNP.  The current strategy appears to be
headed towards the use of TLS, as specified by WG15, with authentication objects
added to the protocol.

The recommendations from IEC 62351-5 (Security
for IEC 60870-5 and derivatives) should be followed.

### IEC 60870-6 TASE.2 (ICCP)

EPRI sponsored several initiatives to develop
security recommendations for TASE.2.  These recommendations have been the
basis of new work items for IEC TC57 WG15.  It is these developing
standards that should be used.

The recommendations from IEC 62351-3 (Security for profiles
including TCP) and IEC 62351-4 (Security for profiles including MMS) should
be followed.

There is a potential need to provide
intrusion detection capability for IEC 60870-6 TASE.2 implementation. 
There is an issue regarding the lack of definition of standardized security
related Management Information Base (MIB) objects.  IEC TC57 WG15 has undertaken the task to define security MIB
objects that could facilitate intrusion detection.  It is recommended that
the recommendations of IEC 62351-7 (Objects for Network Management) be reviewed
carefully.

### IEC 61850

IEC 61850 has several different communication
profiles.  However, one directly aligns with TASE.2 and it has been
recommended in IEC TC57 WG15 that this profile and TASE.2 implement security in
a similar manner.

The Virtual Lan
(VLAN) high speed profiles used for GOOSE, GSSE, IEC 61850-9-1, and IEC
61850-9-2, have performance requirements (e.g. 4 msecs
or less) that prohibit the use of full encryption.  Current thoughts
within IEC TC57 WG15 are to use a CRC based Message Authentication Code/Seal to
provide integrity.  Authentication would be provided via an address-based
credential.  Confidentiality would need to be provided
through appropriate communication path selection. It is expected that the
MAC mechanism will be addressed in IEC 62351-6 (Security for IEC 61850
profiles).

It is also expected IEC 62351-6 will
reference IEC 62351-3 (Security for profiles including TCP) and IEC 62351-4
(Security for profiles including MMS) in regards to the IEC 61850 MMS based
profile.

There is a potential need to provide
intrusion detection capability for IEC 61850 implementation.  There is an
issue regarding the lack of definition of standardized security related
Management Information Base (MIB) objects.  IEC TC57 WG15 has undertaken
the task to define security MIB objects that could facilitate intrusion
detection.  It is recommended that the recommendations of IEC 62351-7
(Objects for Network Management) be reviewed carefully.

### Modbus

This is a defacto
standard protocol that is in wide deployment.  It can be used in a serial
or network based deployment (TCP based).  There are no provisions in the
basic Modbus protocol for security, nor are any authentication extensions known
to be in development.  However, it is recommended that the Modbus/TCP implementations
be augmented with TLS in a manner similar to the recommendations specified by
IEC TC57 WG15 for TC57 protocols.
