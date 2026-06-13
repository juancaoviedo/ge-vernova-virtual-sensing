# Information Integrity

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Information_Integrity_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Information Integrity Service

Ensure
that unauthorized changes made to messages or documents may be detected by the
recipient. The use of message or document level integrity checking is
determined by policy, which is tied to the offered quality of the service
(QoS).

Key
definitions:

**integrity:**
[In INFOSEC, the] quality of an information system (IS) reflecting the logical
correctness and reliability of the operating system; the logical completeness
of the hardware and software implementing the protection mechanisms; and the
consistency of the data structures and occurrence of the stored data. Note
that, in a formal security mode, integrity is interpreted more narrowly to mean
protection against unauthorized modification or destruction of information.
[INFOSEC-99]

The
first thought, when it comes to Integrity, is that it is the same issue as
Confidentiality. However, the Confidentiality Service provides protection from
information disclosure not the detection of information modification. It is the
protection from information modification that the Integrity Service represents.

In
order to provide message integrity, an algorithm that generates a result
similar to a CRC needs to executed and imbedded in the message. However, this
alone will not guarantee integrity as a man-in-the-middle attack could change
the message, recalculate the CRC, and then forward the message.

In
order to prevent man-in-the-middle attacks, a digital signature is typically
used on the CRC like result and both are embedded in the message. It is this
digital signature “seal” that actually prevents the attack. Such signatures are
typically referred to as Message Authentication Codes (MACs) and it is
recommended that the Integrity Service be implemented through the use of such
techniques.
