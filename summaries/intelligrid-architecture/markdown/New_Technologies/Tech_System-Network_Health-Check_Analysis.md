# System/Network Health-Check Analysis

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_System-Network_Health-Check_Analysis.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### System/Network Health-Check Analysis

This
service determines the set of system/network indicators needed to check the
health of the network and system components. A component is considered not
healthy if it is not working, is congested, or is under a security attack.
Different indicators and thresholds may need to be considered for different
conditions, The service determines threshold values, which if exceeded indicate
heath issues, and also determines health check intervals to efficiently monitor
the resources without utilizing excessive network and system resources. For
example, the availability of a system may be checked with sending periodic messages, the return status of the message will indicate its
availability. To reduce resource consumption, some management mechanisms use
traps, messages from management agents to managers, in order to report a fault
as opposed to periodic health checks (polling).
