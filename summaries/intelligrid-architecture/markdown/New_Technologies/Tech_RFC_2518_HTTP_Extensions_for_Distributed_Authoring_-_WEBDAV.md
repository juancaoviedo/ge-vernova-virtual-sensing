# RFC 2518 HTTP Extensions for Distributed Authoring - WEBDAV

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_2518_HTTP_Extensions_for_Distributed_Authoring_-_WEBDAV.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 2518 HTTP Extensions for Distributed Authoring - WEBDAV

**URL:** http:///www.ietf.org/rfc/rfc2518.txt

This
document describes an extension to the HTTP/1.1 protocol that allows clients to
perform remote web content authoring operations. This extension provides a
coherent set of methods, headers, request entity body formats, and response
entity body formats that provide operations for:

Properties:
The ability to create, remove, and query information about Web pages, such as
their authors, creation dates, etc. Also, the ability to link pages of any
media type to related pages.

Collections:
The ability to create sets of documents and to retrieve a hierarchical
membership listing (like a directory listing in a file system).

Locking:
The ability to keep more than one person from working on a document at the same
time. This prevents the "lost update problem," in which modifications
are lost as first one author then another writes changes without merging the
other author's changes.

Namespace
Operations: The ability to instruct the server to copy and move Web resources.

Requirements
and rationale for these operations are described in a companion document,
"Requirements for a Distributed Authoring and Versioning Protocol for the
World Wide Web" [RFC2291].

**Keywords:**
