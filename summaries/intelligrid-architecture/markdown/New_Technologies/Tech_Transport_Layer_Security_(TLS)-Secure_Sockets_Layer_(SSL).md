# Transport Layer Security (TLS)/Secure Sockets Layer (SSL)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Transport_Layer_Security_(TLS)-Secure_Sockets_Layer_(SSL).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Transport Layer Security (TLS)/Secure Sockets Layer (SSL)

**URL:** http://www.ietf.org/rfc/rfc2246.txt

The
Transport Layer Security (TLS) [RFC 2246] is based on Secure Socket Layer (SSL)
protocol ["The SSL 3.0 Protocol", Netscape Communications Corp., Nov
18, 1996.]. TLS/SSL provides privacy and data integrity between two
communicating applications. TLS is application protocol independent.

SSL
is a Public Key Infrastructure (PKI) based protocol used for authenticated and
encrypted communication between clients and servers. SSL uses a program layer
located between the Internet's Hypertext Transfer Protocol (HTTP) and Transport
Control Protocol (TCP) layers. SSL is included as part of both the Microsoft
and Netscape browsers and most Web server products. SSL uses the
public-and-private key encryption system from RSA, which also includes the use
of a digital certificate.

The
SSL protocol runs above **TCP/IP** and below higher-level protocols such as **HTTP**
or **IMAP**. It uses **TCP/IP** on behalf of the higher-level protocols,
and in the process allows an SSL-enabled server to authenticate itself to an
SSL-enabled client, allows the client to authenticate itself to the server, and
allows both machines to establish an encrypted connection. SSL has recently
been succeeded by **Transport Layer Security (TLS)**, which is based on
SSLv3, but is not interoperable with SSL.

The
TLS protocol is composed of two layers: the TLS Record Protocol and the TLS
Handshake Protocol. The TLS Record Protocol, on top of some reliable transport
protocol (e.g., TCP), provides security with private and reliable connection.
The TLS Handshake Protocol provides connection security such that (i) The
peer's identity can be authenticated using asymmetric, or public key,
cryptography, (ii) The negotiation of a shared secret is secure: the negotiated
secret is unavailable to eavesdroppers, and (iii) The negotiation is reliable:
no attacker can modify the negotiation communication without being detected by
the parties to the communication.

**Keywords:**Internet, Security, Protocol, transport layer, Integrity, Confidentiality
