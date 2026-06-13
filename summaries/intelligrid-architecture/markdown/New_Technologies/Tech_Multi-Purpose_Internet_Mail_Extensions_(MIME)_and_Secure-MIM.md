# Multi-Purpose Internet Mail Extensions (MIME) and Secure/MIME

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Multi-Purpose_Internet_Mail_Extensions_(MIME)_and_Secure-MIM.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Multi-Purpose Internet Mail Extensions (MIME) and Secure/MIME

**URL:**http://www.ietf.org/rfc/rfc2045.txt,   
http://www.ietf.org/rfc/rfc2311.txt

Multipurpose Internet Mail Extensions (MIME)
[RFC2045-RFC2049] is a supplementary protocol and an extension to **SMTP**.
Originally designed for only e-mail and SMTP as an encoding method for sending
non-**ASCII** files through e-mail servers, today MIME has been adopted to
also support a way to send non-html documents over the **World Wide Web**.
MIME provides a way for non-text information to be encoded as ASCII text. This
encoding is known as base64. Web servers now must be configured for MIME types
to serve those types of files. Most e-mail clients automatically handle MIME
now and the process is transparent to the user.

The Secure/MIME (S/MIME) is an IETF specification
[RFC 2311], to send and receive secure MIME data, providing the following
cryptographic security services for electronic messaging applications:
authentication, message integrity and non-repudiation of origin (using digital
signatures) and privacy and data security (using encryption).

**Keywords:** Security, Mail, E-mail, Encoding, Internet, Protocol, Application
layer
