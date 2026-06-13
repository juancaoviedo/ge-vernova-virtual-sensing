# RFC 2744 Generic Security Service API Version

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2744_Generic_Security_Service_API_Version_.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2744 Generic Security Service API Version

2 : C-bindings

**URL:** http://www.ietf.org/rfc/rfc2744.txt

This
document specifies C language bindings for Version 2, Update 1 of the Generic
Security Service Application Program Interface (GSS-API), which is described at
a language-independent conceptual level in RFC-2743 [GSSAPI]. It obsoletes
RFC-1509, making specific incremental changes in response to implementation
experience and liaison requests. It is intended, therefore, that this memo or a
successor version thereof will become the basis for subsequent progression of
the GSS-API specification on the standards track. The Generic Security Service
Application Programming Interface provides security services to its callers,
and is intended for implementation atop a variety of underlying cryptographic
mechanisms. Typically, GSS-API callers will be application protocols into which
security enhancements are integrated through invocation of services provided by
the GSS-API. The GSS-API allows a caller application to authenticate a
principal identity associated with a peer application, to delegate rights to a
peer, and to apply security services such as confidentiality and integrity on a
per-message basis.

**Keywords:**
