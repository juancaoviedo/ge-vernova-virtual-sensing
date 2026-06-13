# Management of Time-Sensitive Data Flows and Timely Access to Data by Multiple Different Users

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Management_of_Time-Sensitive_Data_Flows_and_Timely_Access_to.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Management of Time-Sensitive Data Flows and Timely Access to Data by Multiple Different Users

Management
of time-sensitive data flows entails ensuring that systems can handle the
streams of data in a timely manner. Although the primary solution to this issue
is to ensure that the systems and communications are appropriately sized, this
sizing can entail addressing the following questions:

·       Is the flow of
data relatively constant or are there bursts of data? (Queuing theory can be
used to establish sizing for this issue).

·       Is maximum time
of data flows critical? If so, then the system should be designed for
deterministic delivery times (as opposed to statistical delivery times) and
sized to handle the maximum throughput. An example is the requirement for
maximum response time of 10 ms for protective relaying. In this case,
non-absolute protocols like Ethernet are not feasible unless they are used in a
switched network (so that essentially there never is a conflict).

·       Is it acceptable
to base the timeliness of data flows on statistical characteristics? For
example, access by Market Participants to market information often has
statistical requirements, e.g. 95% of Market Participants must be able to
access information within one second 99% of the time. The primary solution is
the provision of adequate bandwidth, processor power, and well-deigned
applications to ensure these contractual requirements are met. Additional
solutions include alternative or backup sources of the time-sensitive
information, as well as measures to prevent denial-of-service security attacks.
In addition, performance logging should be implemented so that proof of meeting
the statistical characteristics is available.

·       Must multiple
users be accommodated with contractual commitments for access within specific
time windows (e.g. access within 10 seconds after each hour, or response to a
request within 30 seconds)? The primary solution is the provision of adequate bandwidth,
processor power, and well-deigned applications to ensure these contractual
requirements are met.

In
either case, very precise specifications, statistical analysis of data flows,
and rigorous factory and field testing are the most effective ways of ensuring
this requirement is met.

**Keywords:**keywords
