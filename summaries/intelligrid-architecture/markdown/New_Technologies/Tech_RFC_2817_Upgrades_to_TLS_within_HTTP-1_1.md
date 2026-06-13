# RFC 2817 Upgrades to TLS within HTTP/1.1

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2817_Upgrades_to_TLS_within_HTTP-1_1.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2817 Upgrades to TLS within HTTP/1.1

**URL:** http://www.ietf.org/rfc/rfc2817.txt

This
document extends the use of TLS (e.g. HTTPS) so that hostnames can be
exchanged.  
  
TLS, a.k.a., SSL (Secure Sockets Layer), establishes a private end- to-end
connection, optionally including strong mutual authentication, using a variety
of cryptosystems. Initially, a handshake phase uses three subprotocols to set
up a record layer, authenticate endpoints, set parameters, as well as report
errors. Then, there is an ongoing layered record protocol that handles
encryption, compression, and reassembly for the remainder of the connection.
The latter is intended to be completely transparent. For example, there is no
dependency between TLSs record markers and or certificates and HTTP/1.1's
chunked encoding or authentication.

**Keywords:**keywords
