# ISO/IEC 18014-2:2002 Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_ISO-IEC_18014-2_2002_Information_technology_--_Security_tech.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### ISO/IEC 18014-2:2002 Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens

**URL:** http://www.iso.ch

ISO/IEC
18014-2:2002 describes time-stamping services producing independent tokens. It
describes a general model for time-stamping services of this type and the basic
components used to construct a time-stamping service of this type, it defines
the data structures and protocols used to interact with a time-stamping service
of this type, and it describes specific instances of such time-stamping
services.

The
usage of independent tokens presumes a high trust on the time-stamping
authority (TSA).

Three
independent mechanisms are currently covered:

Time-stamps
using digital signatures

In
this mechanism the TSA has an asymmetric key pair, and uses the private key to
digitally sign the time-stamp token. Signature verification will use the public
key. This mechanism may require the use of a PKI (Public Key Infrastructure).

Time-stamps
using message authentication codes

In
this mechanism the TSA uses a secret key to digitally bind the time
association. The time-stamp token is authenticated using a Message
Authentication Code (MAC). When using this mechanism, the TSA is needed to
carry out the verification.

Time-stamps
using archiving

In
this mechanism the TSA returns a time-stamp token that only has reference
information to bind the time-stamp to the messageImprint in the time-stamp
token. The TSA archives locally enough information to verify that the
time-stamp is correct.

**Keywords:**TSA, Time Stamping Services, ISO/IEC 18014:2002
