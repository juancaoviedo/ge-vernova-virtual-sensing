# Simple Mail Transfer Protocol (SMTP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Simple_Mail_Transfer_Protocol_(SMTP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Simple Mail Transfer Protocol (SMTP)

**URL:**http://www.ietf.org/rfc/rfc0821.txt

The Simple Mail Transfer Protocol (SMTP) was
developed by the IETF for transferring e-mail reliably and efficiently across
the Internet. SMTP is independent of the particular transmission subsystem and
requires only a reliable ordered data stream channel. An important feature of
SMTP is its capability to relay mail across transport service environments. A
transport service provides an inter process communication environment (IPCE).
An IPCE may cover one network, several networks, or a subset of a network. It
is important to realize that transport systems (or IPCEs) are not one-to-one
with networks. A process can communicate directly with another process through
any mutually known IPCE. Mail is an application or use of inter process
communication. Mail can be communicated between processes in different IPCEs by
relaying through a process connected to two (or more) IPCEs. More specifically,
mail can be relayed between hosts on different transport systems by a host on
both transport systems.

**Keywords:** Mail, Email, Internet, Protocol, Application layer
