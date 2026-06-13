# Time Stamping

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Time_Stamping.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Time Stamping

Time
stamps are crucial for determining the time of an event. Different resolutions
are required by different situations, but typically time resolutions for power
system events should be within 1 to 10 milliseconds.

Time
accuracy and time synchronization requirements across many systems and devices
can also vary, but again for power system operations, typical **relative**
accuracy/synchronization requirements are:

·       Events within a
substation should be timestamped with a relative accuracy within the substation
of 1 millisecond

·       Events across
multiple substations should be timestamped with a relative accuracy of 10
milliseconds

With
the availability of GPS time, the requirements for **absolute** time
accuracy are becoming more stringent, and 1 millisecond absolute accuracy
across large territories can now be met if GPS devices are connected to the
time-critical devices.

Time
stamps are particularly important for:

·       Data values, to
indicate exactly what time they were monitored

·       Control actions,
to indicate exactly when a control action took place

·       Alarms, to
indicate when the event took place that caused the alarm, as well as additional
time stamps to indicated when an alarm was acknowledged and when the situation
that caused the alarm was resolved

·       Events, to
indicate when events took place

**Keywords:**Time, relative time, absolute time, GPS
