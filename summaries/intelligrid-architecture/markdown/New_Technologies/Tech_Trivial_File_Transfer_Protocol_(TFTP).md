# Trivial File Transfer Protocol (TFTP)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Trivial_File_Transfer_Protocol_(TFTP).htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Trivial File Transfer Protocol (TFTP)

**URL:**http://www.ietf.org/rfc/rfc1350.txt

Trivial File Transfer Protocol (TFTP) is a simple
protocol to transfer files, and therefore was named the Trivial File Transfer
Protocol or TFTP. It has been implemented on top of the Internet User Datagram
protocol (UDP or Datagrams) so it may be used to move files between machines on
different networks implementing UDP. (This should not exclude the possibility
of implementing TFTP on top of other datagram protocols.) It is designed to be
small and easy to implement. Therefore, it lacks most of the features of a
regular FTP. The only thing it can do is read and write files (or mail) from/to
a remote server. It cannot list directories, and currently has no provisions
for user authentication. It is commonly used during the initial bootstrap or
firmware download/upgrades of devices which lack a persistent local storage,
e.g. a diskless workstation etc, within a trusted environment.

**Keywords:** Internet, datagram, Transport, Protocol, file transfer
