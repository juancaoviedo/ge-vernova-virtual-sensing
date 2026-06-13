# RFC 1305 Network Time Protocol (Version 3) Specification, Implementation

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### RFC 1305 Network Time Protocol (Version 3) Specification, Implementation

**URL:** http://www.ietf.org/rfc/rfc1305.txt

This
document describes Version 3 of the Network Time Protocol (NTP). It supersedes
Version 2 of the protocol described in RFC-1119 dated September 1989. However,
it neither changes the protocol in any significant way nor obsoletes previous
versions or existing implementations. The main motivation for the new version
is to refine the analysis and implementation models for new applications at
much higher network speeds to the gigabit-per-second regime and to provide for
the enhanced stability, accuracy and precision required at such speeds. In
particular, the sources of time and frequency errors have been rigorously
examined and error bounds established in order to improve performance,
provide a model for correctness assertions and indicate timekeeping quality to
the user. The revision also incorporates two new optional features, (1) an
algorithm to combine the offsets of a number of peer time servers in order to
enhance accuracy and (2) improved local-clock algorithms that allow the poll
intervals on all synchronization paths to be substantially increased in order
to reduce network overhead. It also adds recommendations in regards to
security.

**Keywords:**Authorization for Access Control, Policy, Spoof, Security
