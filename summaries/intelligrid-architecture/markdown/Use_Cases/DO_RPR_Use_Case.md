# Relay Re-coordination

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DO_RPR_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Distribution Operations - Relay Protection Re-coordination (RPR) Function

## Contents

* [Narrative](DO_RPR_Use_Case.htm#Narrative)

## Narrative

This application
adjusts the relay protection settings to real-time conditions based on
the preset rules. This is accomplished through analysis of relay
protection settings and operational mode of switching devices (i.e.,
whether the switching device is in a switch or in a recloser mode),
while considering the real-time connectivity, tagging, and weather
conditions. The application is called to perform after feeder
reconfiguration, and, in case, when conditions are changed and fuse
saving is required. No fault calculations are needed in this
application, if the distribution system is radial without significant
DER.

With DERs in
distribution, the situation is much more complex, especially when
supporting the fuse-saving protection policy.  There are a variety of
relationships between fault currents through the protective devices
and through fuses.  The room for adjustment of the settings of the
protective devices is limited.  Hence, it is possible, that under some
conditions, the coordination for the fuse saving protection cannot be
provided.  Therefore, the relay protection coordination application
should include a fault calculation routine determining probable fault
currents through the protective devices and through the fuses.  The
range of these fault currents should be compared with the
corresponding settings, and a decision about the coordination should
be made.  If the coordination with existing settings cannot be
provided, and changes of settings of the protective devices are
possible, then the recommended changes should be implemented.  The
assumption here is that the future protective devices will be
available for remote change of their settings.

Another consideration
in regards to fuse saving protection is the disconnection of the DER
before the reclosing to avoid asynchronous connections.  If the
interruption of DER services for fuse saving purposes is unacceptable
(contractual agreement between DER owner and DISCO), then the fuse
saving protection cannot be implemented.  The input data for the
application should include the DER characteristics needed for
calculations of the fault currents (different types of DER will have
different characteristics) and the relevant contractual conditions, if
any.

The situation is different when the coordination
of several protective devices along the feeder should be coordinated,
and there are DERs connected to the circuits between the protective
devices.  In this case, the fault current through the protective
device downstream from the DER will be greater than the fault current
upstream from the DER, and it is easier to provide coordination.  But,
if the DER disconnects before the fault is cleared due to low voltage,
then the margin for coordination becomes smaller.  This relationship
between the residual voltage at the DER PCC, timing of the relay
protection, and relay protection setting should be taken into account
in the relay protection coordination application.
