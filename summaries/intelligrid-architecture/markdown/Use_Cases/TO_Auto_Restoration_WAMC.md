# Auto Restoration

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Auto_Restoration_WAMC.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - Wide-Area Control System Advanced Auto-Restoration

## Contents

* [Narrative](TO_Auto_Restoration_WAMC.htm#Narrative)
* [Steps](TO_Auto_Restoration_WAMC.htm#Steps)

## Narrative

### Overview

The purpose of advanced auto-restoration is to automatically restore power to
un-faulted sections of a line or feeder, after a fault is
isolated, in networks having complex topologies and multiple
organizational boundaries.

Currently, automatic restoration of service
is performed only within a restricted set of conditions and
network topologies, as described in the WACS Automated Controls
Baseline use case.  In the near future, it is expected that these
restrictions will be removed and the automation system will be
able to restore power in systems which:

> ·       
> There are multiple sources from which to
> restore power
>
> ·       
> The multiple sources may belong to different
> organizations
>
> ·       
> There are multiple possible connection points
> between the sources
>
> ·       
> It is necessary to split the de-energized load
> into sections because any one source cannot re-energize the
> whole load

The remainder of this
narrative describes an example scenario illustrating these
capabilities.

### Initial State

As shown in Figure 1, two neighboring substations are connected in a
manner to make traditional auto-restoration possible, in other words:

> ·       
> Per typical utility operation, there is
> breaker located in the substation connected to each feeder,
> provided with an automatic reclosing function.  These are
> labeled 1A1, 1B1, 2A1, and 2B1 in the figure, following the
> naming convention <substation1/2><feederA/B><switch/breaker#>.
>
> ·       
> Normally-closed switches are located at
> intervals along each feeder to permit auto-sectionalizing
> around a fault.  (e.g. 1B2, 1B3, 1B4).  These switches are
> typically of the “no-load break” variety, for economic
> reasons.  They can open only when there is no load on the
> line.  Some may be of the “load break” variety, which can
> open under normal current.  Usually only those devices at
> the head of the feeder (such as 1A1, 1B1 etc.) will be
> “fault interrupting” breakers capable of opening under fault
> current.
>
> ·       
> A normally-open switch is located at the end
> of adjacent feeders. (e.g. 1C or 2C).  This switch can be
> closed to share load or restore power from one feeder to the
> other.
>
> ·       
> Each breaker and switch is monitored and
> controlled by an Intelligent Electronic Device (IED).
>
> ·       
> A Substation Computer (SC) in each substation
> gathers information and controls the IEDs connected to its
> feeders.  It reports to the Operator for that utility by way
> of a Graphical User Interface (GUI).

In this example, the two adjacent sets of feeders
can also be connected to each other (if necessary) using a number of
normally-open switches (1X, 1Y and 1Z).  This interconnection is
rarely performed because the two substations belong to different
utilities.  In this example, the interconnection switches are owned by
the utility that controls Substation 1.  However, Operator 1 must have
approval from Operator 2 before closing any of these switches.

The scenario begins with each IED reporting its
downstream load and switch status to the Substation Computer.  For the
purposes of this example, we assume that *all* this information
is reported to *both* Substation Computers.  There are two ways
to do this:

> ·       
> Each IED reports its data separately to each
> Substation Computer
>
> ·       
> Each IED only reports to its “own” Substation
> Computer, and the Substation Computers exchange
> information.

The latter case is most likely to be implemented
because:

> ·       
> It reduces the number of communications
> connections between the two utilities, which is desirable
> for security reasons.
>
> ·       
> It reduces the bandwidth and processing power
> required by each IED.

if !vml?![](TO_Auto_Restoration_WAMC_files/image002.gif)endif?

Figure1
Initial System State

From the current data reported by each IED (shown
in italics with arrows), the Substation Computers can calculate the
load on each individual section of the feeders.  This example assumes
that the maximum capacity limit on each feeder is 100A.  Feeder 1B, in
that case, is operating near capacity, while the other feeders are
about 50% loaded.

### Fault Detection

As shown in Figure 2, a fault occurs on feeder 1B between switches 1B2
and 1B3.  Breaker 1B1 trips and de-energizes 90A of load, including
60A that is downstream from the fault.

All IEDs on feeder 1B report to Substation
Computer 1 the fault and the loss of current.  Those IEDs that saw the
fault current (1B1 and 1B2) may send an estimated distance to the
fault.  IED 1B1 reports that it has tripped and has started reclosure
timers.  Substation Computer 1 forwards the information to Substation
Computer 2, but SC2 takes no action because the fault is not in its
territory.

if !vml?![](TO_Auto_Restoration_WAMC_files/image004.gif)endif?

Figure2
Fault Detection

### Auto-Sectionalization

As shown in Figure 4, the IEDs on feeder 1B take action to isolate, or
auto-sectionalize, the fault.  There are two possible methods for
doing so, with different communications requirements.

> ·       
> **High-Speed Communication.** One possible
> method is that Substation Computer 1 determines which two
> switches (1B2 and 1B3) to open using fault direction and
> distance information provided by the IEDs.  This method
> would require fast communication between the 1B IEDs and
> SC1, in order to open the switches between reclosings of the
> breaker (measured in seconds).  It would likely also require
> the IEDs to provide a specialized communications service,
> i.e. “open the next time you see zero current”.
>
> ·       
> **Fault-Interruption Counting.** A more
> robust and distributed method would be for each IED to be
> programmed to open its switch after a pre-configured
> reclosure attempt.  Each IED would open its switch under the
> following conditions:

o      
The IED has observed fault current

o      
The IED has seen the fault current drop to zero,
indicating the breaker has tripped

o      
These two conditions have occurred a pre-configured
number of times.  The number is different for each IED on the feeder.

 Figure 3 illustrates how this occurs in the example.  No IED
is permitted to open its switch between the initial fault and the
first reclosure attempt, in case the fault is transient.  1B4 is
permitted to open its switch between the first and second reclosure
attempts, but does not do so.  Because 1B4 is downstream from the
fault and has no other source of current, it does not observe the
fault current and its opening conditions are therefore not met. 
Similarly, 1B3 does not observe fault current and so does not open in
its time window.

IED 1B2, however, has seen the same current as
1B1, and has been counting the fault interruptions.  After the third
reclosure attempt, 1B2 opens its switch, isolating the fault from any
source of current.  This is **auto-sectionalization**, and is shown
as step (1) in Figure 4.  When 1B1 recloses the fourth time, it is
successful, and 10A of load is restored to that section of feeder 1B. 
This is step (2) in Figure 4.

if !vml?![](TO_Auto_Restoration_WAMC_files/image006.gif)endif?

Figure3
Fault-Interruption Counting for Auto-Sectionalization

if !vml?![](TO_Auto_Restoration_WAMC_files/image008.gif)endif?

Figure4
Auto-Sectionalization and Load
Splitting

### Isolating the Fault

The final step in auto-sectionalization, shown in
step (3) of Figure 4, is to isolate the fault.  Substation Computer 1
observes that 1B3 and 1B4 have reported zero current and voltage
without having reported fault current.  It therefore determines
(possibly with the assistance of distance-to-fault data from 1B1 and
1B2) that the fault is between 1B2 and 1B3.  Substation Computer 1
recommends to Operator 1 that switch 1B3 be opened in order to isolate
the fault.  Operator 1 confirms this operation, and SC1 sends the
message to 1B3 causing it to open.

### Load Splitting

Whichever auto-sectionalizing method is used, the
fault is now isolated and auto-restoration can begin.  Substation
Computer 1 reviews the data provided prior to the fault.  It
calculates the loading on each segment of each feeder, as shown in
Figure 4.  It determines that there is 60A of load that can
be restored.

However, the “traditional” solution, to close
switch 1C, will not solve the whole problem.  Feeder 1A is already
loaded at 60A.  If it accepts the whole downstream load of 60A, it
will be overloaded, since the example began with the assumption of
100A maximum limit per feeder.

The Substation Computer determines that it will
be necessary to “split” the downstream load and re-energize it from
multiple sources.  Substation Computer 1 recommends to Operator 1 that
switch 1B4 be opened, receives confirmation from Operator 1, and opens
the switch by sending a message to 1B4.  This is step (4) in Figure 4.

### Auto-Restoration

The final steps in auto-restoration are shown in
Figure 5.  Utility 1 has a policy in place that load is to
be restored from Utility 1 sources whenever possible.  Therefore
Substation Computer 1 recommends that switch 1C be closed, rather
than, for instance, switch 1Z.  Operator 1 confirms this operation and
SC1 sends the message to IED 1C, restoring 30A of service.

Substation Computer 1 recommends that switch 1Y
be closed to restore the remaining un-faulted section of feeder
between 1B3 and 1B4.  Operator 1 contacts Operator 2 at Utility 2,
requesting permission to close switch 1Y.

Before making this decision, Operator 2 does the
following:

> ·       
> Reviews the sequence of events logs generated
> by SC2 showing the auto-sectionalizing sequence.
>
> ·       
> Confirms that Utility 1 has isolated the fault
> between 1B2 and 1B3.
>
> ·       
> Confirms from records generated by SC2 that
> the de-energized section between 1B3 and 1B4 previously was
> loaded at 30A.
>
> ·       
> Checks on the SC2 GUI that feeder 2A can
> handle the additional 30A load.

Finally, Operator 2 contacts Operator 1, giving
permission to close switch 1Y.  Operator 1 confirms the operation with
SC1, which sends the message to 1Y and restores the remaining 30A of
service.

if !vml?![](TO_Auto_Restoration_WAMC_files/image010.gif)endif?

Figure5
Auto-Restoration

### Load Balancing

Following auto-restoration, feeder 1A is loaded
at 90A and 2A is loaded at 80A, while 2B is only loaded at 50A. 
Operator 2 may choose to close switch 2C in order to lighten the load
on feeder 2A.

In theory, the whole system could be more
efficiently loaded by also closing switch 1Z.  However, neither
Substation Computer would make this recommendation because:

> ·       
> The power on the two feeders is likely
> incompatible due to differences in frequency, voltage, and
> phase angle.  Therefore, it would be necessary to open 1C
> before closing 1Z.
>
> ·       
> Opening 1C would cause a momentary outage
> downstream of 1B4.  Furthermore, if 1C was not a “load
> break” switch, it would be necessary to first break the load
> at 1A1, meaning that the outage would occur for all of
> feeder 1A.
>
> ·       
> Utility 1 would lose the 30A of load
> downstream of 1B4 to Utility 2 until the fault could be
> repaired.  This would be unacceptable from a business point
> of view.

### Summary

Performing advanced auto-restoration will require
the following measures beyond those required for existing
auto-restoration mechanisms:

> ·       
> Real-time sharing of data between Substation
> Computers
>
> ·       
> Calculation of loads on each feeder or line
> section, and storing these recent historical values in the
> Substation Computer.
>
> ·       
> More advanced logic in each Substation
> Computer to evaluate each possible switching action, perhaps
> on the order of the Contingency Analysis programs currently
> used by EMS stations.
>
> ·       
> Reliable communications between neighboring
> operators, either by voice or by data
>
> ·       
> One of the following features:
>
> > o      
> > **Full breakers and protection
> > relays on each section**, or “load break” or
> > “fault-interrupting” switches.  Utilities are
> > unlikely to do this because of the significantly
> > higher cost.
> >
> > o      
> > **Fault-Interruption counting**,
> > as discussed in this example. Fault-interruption
> > counting has one major drawback:  Ideally, it
> > requires the same number of reclosures as there
> > are switches on the feeder.  Typically, utilities
> > do not use a high number of reclosures because:

-         
It causes excessive wear on the breaker

-         
It annoys the customers, who see multiple small outages within a short
period of time.

Therefore it is rare to see
more than two or three reclosures.   This example, with four
reclosures, would be extremely rare.  This limits the granularity with
which load can be restored, and increases the number of subscribers
affected by an fault.

o      
**High-speed communications** between remote IEDs and
the substation computer.  In this example, it would permit the
Substation Computer to immediately determine that 1B2 and 1B3 switches
should open, and do so quickly, between the first and second
reclosings of breaker1B1.   This is shown as an alternate scenario in
the use case below.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1A | Fault | Report Fault | IEDs upstream from the fault report seeing fault current | IED 1B1, IED 1B2 | Substation Computer Device  1 | Fault Detected | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 1B | Loss of current and voltage | Report Loss of Service | IEDs downstream from the fault report loss of current and voltage | IED 1B3, IED 1B4 | Substation Computer Device  1 | No Current Detected,  No Voltage Detected | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 2.1 |  | Initial Trip | First feeder IED (relay) trips breaker and reports the action.  Starts reclosure timer. | IED 1B1 | Substation Computer Device  1 | Trip | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 2.2 | Recloser timer expires | First Reclose Attempt | Upon expiry of reclosure timer, first IED recloses the breaker.  Reports the action. | IED 1B1 | Substation Computer Device  1 | Switch State (close) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 2.3 | Fault | Report Fault | IEDs upstream from the fault report seeing fault current again.  This message indicates that the fault was not intermittent and that the SC should attempt to auto-sectionalize. | IED 1B1, IED 1B2 | Substation Computer Device  1 | Fault Detected | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 2.4 |  | 2nd Trip | First IED trips breaker and reports the action.  Starts reclosure timer.  This message indicates that the SC can now attempt to open a switch for auto-sectionalization. | IED 1B1 | Substation Computer Device  1 | Trip | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 2.5 |  | Auto-sectionalize | Computer determines the correct switch to open based on the fact that the upstream switches reported fault current, while the downstream switches reported no current or voltage.  Directs the correct switch to open between reclosures of the breaker. | Substation Computer Device  1 | IED 1B2 | Switch Control (open) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 2.6 | Reclosure timer expires | Report Upstream Power Restored | Upon expiry of the reclosure timer, first feeder IED recloses the breaker.  Reports the action. Power is now restored from the substation to switch 1B1. | IED 1B1 | Substation Computer Device  1 | Switch State (close),  Current,  Voltage | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 3.1 | Logic timer expires | Request Isolation | Computer detects (using a timer) that no fault has occurred since 1B1 reclosed the breaker.  Determines that switch 1B3 is the first switch downstream from the fault and should be opened.  Requests confirmation from System Operator . | Substation Computer Device  1 | System Operator  1 | Request   (open 1B1) | User Interface |
| 3.2 |  | Confirm Isolation | Tells the Substation Computer Device  it is permitted to open the first downstream switch (1B3). | System Operator  1 | Substation Computer Device  1 | Confirm | User Interface |
| 3.3 |  | Isolate Fault | Requests that the first downstream switch (1B3) open. | Substation Computer Device  1 | IED 1B3 | Switch Control (open) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 3.4 |  | Report Isolation Complete | The IED controlling the first downstream switch reports that the switch is open. | IED 1B3 | Substation Computer Device  1 | Switch State (open) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 4.1 |  | Request Load Split | Computer determines from the Current and Voltage information stored prior to the fault that service cannot be restored from a single source.  Determines which switch to operate (1B4) and requests confirmation from the System Operator . | Substation Computer Device  1 | System Operator  1 | Request  (open 1B4) | User Interface |
| 4.2 |  | Confirm Load Split | System Operator  confirms that the Computer may open the switch to split the load (1B4) | System Operator  1 | Substation Computer Device  1 | Confirm | User Interface |
| 4.3 |  | Split Load | Computer opens the switch to split the load (1B4) | Substation Computer Device  1 | IED 1B4 | Switch Control (open) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 4.4 |  | Report Load Split Complete | IED (1B4) reports that the switch is open and the load is split. | IED 1B4 | Substation Computer Device  1,  Substation Computer Device  2 | Switch State | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 5.1 |  | Request Local Restoration | Computer determines that half the load can be restored by closing the local normally open switch (1C), and requests permission from operator. | Substation Computer Device  1 | System Operator  1 | Request  (close 1C) | User Interface |
| 5.2 |  | Confirm Local Restoration | System Operator  confirms that the Computer may close the normally open switch (1C) | System Operator  1 | Substation Computer Device  1 | Confirm | User Interface |
| 5.3 |  | Restore from Local Source | Computer closes the switch to restore power from the local source (1C). | Substation Computer Device  1 | IED 1C | Switch Control (close) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 5.4 |  | Local Restoration Complete | IED (1C) reports that the switch is closed and current is restored to half the load. | IED 1B4 | Substation Computer Device  1,  Substation Computer Device  2 | Switch State (close),  Current | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 6.1 |  | Request Inter-Utility Restoration | Computer determines that the other half of the load can be restored by closing the inter-utility switch (1Y), and requests permission from operator. | Substation Computer Device  1 | System Operator  1 | Request  (close 1Y) | User Interface |
| 6.2 |  | Request Linking Utilities | System Operator  1 verifies Computer 1’s request and forwards it to System Operator  2 at the other utility. | System Operator  1 | System Operator  2 | Request  (close 1Y) | User Interface |
| 6.3 |  | Confirm Linking Utilities | System Operator  2 verifies the request and gives System Operator  1 permission to proceed. | System Operator  2 | System Operator  1 | Confirm | User Interface |
| 6.4 |  | Confirm Inter-Utility Restoration | System Operator  confirms that the Computer may close the normally open inter-utility switch (1Y) | System Operator  1 | Substation Computer Device  1 | Confirm | User Interface |
| 6.5 |  | Restore from Inter-Utility Source | Computer closes the switch to restore power from the other utility source (1Y). | Substation Computer Device  1 | IED 1Y | Switch Control (close) | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |
| 6.6 |  | Inter-Utility Restoration Complete | IED (1Y) reports that the switch is closed and current is restored to the remaining load. | IED 1Y | Substation Computer Device  1,  Substation Computer Device  2 | Switch State (close),  Current | [Deterministic Rapid Response Intra-Sub](../Environments/Env1_Deterministic_Intra-Substation.htm) |

if !supportEndnotes?  
 endif?

##
