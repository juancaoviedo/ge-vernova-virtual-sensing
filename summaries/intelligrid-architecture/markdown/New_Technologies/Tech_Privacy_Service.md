# Privacy Service

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Privacy_Service.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Privacy Service

The
privacy service is primarily concerned with the policy driven classification of
personally identifiable information (PII). Service providers and service
requestors may store personally identifiable information using the Privacy
Service. Such a service can be used to articulate and enforce a Security
Domain’s privacy policy. Allow both a service requester and a service provider
to define and enforce privacy policies, for instance taking into account things
like personally identifiable information (PII), purpose of invocation, etc.
(Privacy policies may be treated as an aspect of authorization policy
addressing privacy semantics such as information usage rather than plain
information access.).

Many
may consider privacy equivalent to confidentiality/encryption, however this is
not true. In reality, privacy is an issue regarding the PII after a secure
transfer of that information occurs. The issue relevant, mostly to web
technology, is how to determine in advanced if the privacy offered by a web
site is sufficient.

Technological Assessment and
Relevant Documents

A
review of relevant information reveals that there are many well know
legal/legislative aspects to privacy and disclosure of that information.
However, there is little relevant work in regards to being able to determine
and enforce the level of privacy electronically. The sole exception, that has
maturity, is the P3P specification from W3C. References PRIV-01 and PRIV-02 are
recommended reading to allow the SMI/policy services to determine if P3P can be
used/monitored within the Security Domain.

Other
work in this are is highly recommended.

Table 25: References Regarding Privacy

|  |  |
| --- | --- |
| PRIV-01 | Web consortium backs P3P privacy standard  Available from: http://www.cnn.com/2002/TECH/internet/04/18/p3p.privacy.idg/ |
| PRIV-02 | Web Privacy Standard: It's a Start  Available from: http://www.pcworld.com/news/article/0,aid,94544,00.asp |

Table 26: Relevant Specification regarding Privacy

|  |  |  |
| --- | --- | --- |
| Identification Number | Name | Comment |
| W3C | The Platform for Privacy Preferences 1.1 (P3P1.1) Specification  W3C Working Draft 27 April 2004 | Highly Recommended |
