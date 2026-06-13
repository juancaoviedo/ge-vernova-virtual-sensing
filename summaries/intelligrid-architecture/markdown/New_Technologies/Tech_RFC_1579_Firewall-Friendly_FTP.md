# RFC 1579 Firewall-Friendly FTP

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1579_Firewall-Friendly_FTP.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1579 Firewall-Friendly FTP

**URL:** http://www.ietf.org/rfc/rfc1579.txt

This
document describes a suggested change to the behavior of FTP client programs.
No protocol modifications are required, though we outline some that might be
useful.

The
FTP protocol uses a secondary TCP connection for actual transmission of files.
By default, this connection is set up by an active open from the FTP server to
the FTP client. However, this scheme does not work well with packet
filter-based firewalls, which in general cannot permit incoming calls to random
port numbers. If, on the other hand, clients use the PASV command, the data
channel will be an outgoing call through the firewall. Such calls are more
easily handled, and present fewer problems.

**Keywords:**Policy, Firewall Transversall
