# Automated Control Base

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Auto_Control_Baseline.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Wide-Area Monitoring And Control – Automated Control Functions

## Contents

* [Narrative](TO_Auto_Control_Baseline.htm#Narrative)
* [Normal Sequence Steps](TO_Auto_Control_Baseline.htm#Normal Sequence Steps)
* [Steps – Alternative / Exception Sequences](TO_Auto_Control_Baseline.htm#Steps – Alternative / Exception Sequences)

## Narrative

Transmission Automated Control (Baseline) describes a set of
functions that are typically automated within a substation, but are
not directly associated with protection, fault handling, or equipment
maintenance.  In general, they serve to optimize the operation of the
power system and ensure its safe operation by preventing manually
generated faults.  These functions include:

* Changing transformer taps to regulate
  system voltage
* Switching capacitor banks or shunts in
  and out of the system to control voltage and reactive load
* Interlocking of controls to prevent
  unsafe operation
* Sequencing controls to ensure safe
  operation
* Load balancing of feeders and
  transmission lines to reduce system wear and resistive
  losses
* Restoring service quickly in the event
  of a fault, with or without operator confirmation

The functions described in this use case were
traditionally performed by individual devices acting alone.  When
implemented this way, they did not have any effect on the
communications system.  However, in the last five to seven years,
these functions have been distributed across the substation.  That is,
the software logic controlling the function now often resides on a
different device than the one which provides the inputs or outputs to
the process.

This change has taken place because the use of
substation LANs has made it economical to place Intelligent Electronic
Devices (IEDs) close to the equipment they are monitoring and
controlling.  Logic has therefore either been centralized, with a
single Substation Computer using the IEDs as remote controllers, or it
has been distributed among the IEDs themselves.  In either case, the
communications system has now become part of the automation functions.

### Voltage Regulation using Tap Changers

In voltage regulation, the automation system
ensures a constant voltage on the substation bus by adjusting the tap
of one or more transformers.  A monitoring IED provides a voltage
value to the Substation Computer, which has been programmed with
threshold and hysteresis logic. The IED is usually monitoring the bus
side of a transformer.  In more complex situations, IEDs may monitor
multiple voltages throughout the station and pass them all to the
Substation Computer as input to the logic. When the logic indicates
that the bus voltage must be adjusted, the Substation Computer issues
a control operation to the IED connected to the transformer tap.  This
will change the monitored voltage, which will be fed back through the
logic.

The voltage control logic typically has a
pre-programmed qualification delay in the tens of seconds – adjusting
the tap causes wear on the equipment, so adjustments should not be
made lightly.  Therefore, an appropriate update time for the monitored
voltage is on the order of one-half second to one second.  Because of
the wear on the transformer and tap, and the impact on the rest of the
system if adjusted wildly, tap raise/lower operations are typically
performed with select-before-operate logic.  Redundancy and
reliability of the communications path is important.

### Volt/VAR Regulation using Capacitor or Shunt Control

In capacitor bank control, the automation system
optimizes the voltage and inductive load on a line or bus by
connecting or disconnecting one or more capacitor banks.  It prevents
the imaginary part of the load from becoming too large, reducing
voltage and the efficiency of the system.  The banks may be widely
located across the power system, or within the substation.  There are
many different logic algorithms for performing capacitor bank
control.  The simplest is calendar or time of day control, in which
the load on the power system is not even monitored.  The logic simply
assumes that the inductive load will be higher at certain times of the
day or year.  In areas where inductive load is largely caused by air
conditioning, logic may switch based on ambient temperature.  Some
algorithms monitor voltage only and switch when it passes certain
thresholds.  More sophisticated algorithms monitor both current and
voltage and switch based on either the calculated power factor or
directly on the calculated inductive load (VARs).  There are typically
hysteresis settings on such logic to prevent frequent switching. 
Shunt control occurs under similar conditions, but with the addition
or removal of inductive loads.

In distributed Volt/VAR control, one IED controls
one capacitor bank on a given line, and each IED makes switching
decisions individually.  In centralized Volt/VAR control, each IED
reports monitored values back to a Substation Computer.  The
Substation Computer may make switching decisions based on averages or
groupings of voltages.  When it decides a switch is necessary, it
sends a control message to the appropriate IED, which may or may not
be the device reporting the controlled measurements.

The hysteresis in some Volt/VAR algorithms may
often be in hours, so communication delays in tens of seconds are
easily acceptable.  It is fairly common to broadcast capacitor bank
control messages, without any select-before-operate logic, since the
effect of any given control is usually small.  When capacitor banks
are located remotely, pagers have sometimes been used as a
communications media – one number to switch the bank in, one to
disconnect it.

### Interlocking

Interlocking prevents unsafe operation of the
various switches and breakers within a substation.  When an Operator
or software application attempts to operate a control, the automation
system evaluates the state of the entire system and may reject the
control request based on pre-programmed logic.  This logic corresponds
directly to the topology and interconnection of the substation. 
Simpler substations may have little or no interlocking.  The most
complex logic is associated with complex transformer and bus
redundancy systems.

For instance, an operator will close an earthing
switch on a section of the bus to ground it prior to permitting
maintenance on the equipment.  However, the operator may not be aware
that the bus section is still live due to an interconnection with
another bus section or a feeder fed by another bus section.  The
automation system must prevent a fault by rejecting the Operator’s
request.

Interlocking is most reliably and efficiently
performed by the device that must perform the requested operation.  In
the past, it may have been performed by the substation GUI or SCADA
master station, when those were the only locations that could perform
switching.  It is still often performed by a Substation Computer or
Data Concentrator which serves as a clearinghouse for all control
operations to the substation.  This centralized logic mechanism is
still used, especially because deregulation has increased the number
of master stations that require access to the substation.

However, more and more frequently, interlocking
is performed by logic on the IEDs themselves, operating on data
distributed by peer-to-peer communications between the devices.  This
peer-to-peer communications has been made possible by the introduction
of the substation LAN.  Performing interlocking at the IED permits the
same logic and performance to be in effect regardless of whether the
control request originates at a remote site, at a substation GUI, at
the control panel of the IED, or even a manual panel switch.

In an ideal system, the state information
required to perform interlocking would be updated simultaneously
throughout the system.  Any delay provides a window in which a control
could be mis-operated.  However, in practice, it is sufficient to
update the state of the system in less than a second or two.  This
interval represents the typical time between the moment an Operator
checks the state of the system on a GUI or display panel, and the
moment the Operator makes the control request.  As more automation
applications are deployed in the substation, human reaction time will
become less of a factor, and the demands on interlocking will
increase.  Today, a challenging interlocking requirement for an
advanced substation is less than 200 milliseconds between updates.

The control itself is typically issued with
select-before-operate logic.  The distribution of state information
for interlocking may be broadcast or multicast.  Redundancy and
reliability is extremely important.

### Sequenced Controls

While interlocking is intended to prevent
Operator-initiated faults by rejecting invalid controls, sequenced
controls automate some portion of the Operator’s tasks to eliminate
the possibility of an invalid control ever being issued.

For example, consider a substation with two
transformers and a normally open switch between the two bus sections
connected to each transformer.  There are two different philosophies
that an Operator may employ to take one of the transformers out of
service.  In “make before break”, the Operator should (1) connect the
two buses, (2) disconnect the transformer from the bus, and (3)
disconnect the transformer from the upstream transmission line.  This
method ensures there will be no outage of service.  In “break before
make”, however, the Operator should (A) disconnect the transformer,
then (B) quickly connect the bus and then (C) disconnect the
transmission line.  This results in an outage, but prevents side
effects resulting from mis-matched transformers sharing the same bus.

if !vml?![](TO_Auto_Control_Baseline_files/image002.gif)endif?

In a sequenced control, the Operator simply
requests the isolation of the transformer, and the automation system
performs the controls in the sequence required by the utility.  The
Operator is not permitted to perform any other sequence.  In the
“break before make” case above, it also ensures that the resulting
outage is as small as possible, because the automation system can
perform the sequence faster than a human.

The speed of a sequenced control is related to
the components involved in the sequence.  For instance, the logic may
need to wait for motorized switches to connect or disconnect before
proceeding with the next control in the sequence.  In a “break before
make” sequence as described above, however, the length of the outage
must be minimized and a value of less than half a second is typically
desired.  All sequenced controls are typically service-affecting and
are therefore executed with select-before-operate logic.

### Load Balancing

Load balancing is typically a distribution
operation, performed between two transformers within a substation, but
may also be performed in transmission systems between substations.  In
the distribution case, two feeders serviced by separate transformers
are connected at their remote ends by a normally open switch.  A
pole-top IED controls the switch.  Other IEDs monitor load on the
line.  The IEDs report the state and load of the system to a
Substation Computer.  The Substation Computer detects the condition
when one transformer is heavily loaded and the other has excess
capacity, and sends a message to the pole-top IED to close the
switch.  Now, instead of one line loaded at 90% and the other at 25%,
both may be loaded at 50%.  Since resistive losses vary with the
square of the current, this action improves the efficiency of the
power system and reduces wear on equipment.  In transmission systems,
two substations having lines feeding the same third substation may
share load.  This type of logic is typically centralized, not
distributed.

if !vml?![](TO_Auto_Control_Baseline_files/image004.gif)endif?

As with tap changing, load balancing is not an
action that is typically performed lightly.   Qualification times for
the logic may be measured in minutes or even hours.  Therefore, update
times and control transmission times may be measured in seconds.  In
distribution operations, this is fortunate because IEDs controlling
the switches may be remote and only reached via slow links.  Some
utilities may prefer that the process not be completely automated, and
that the automation system request confirmation from the Operator
before taking action.  Reliability of the data is important and
redundant links may be used.

### Automated Service Restoration

Automated Service Restoration is typically a
distribution operation, but may be performed in transmission systems
when “loops” are possible between substations.  In the distribution
case, two feeders are connected at their remote ends by a normally
open switch.  Several other switch / breaker combinations are located
at other points along the feeders.  All the switches and breakers are
monitored by IEDs.  When a fault occurs, the IEDs on the upstream side
of the fault trips its breaker.  It notifies the Substation Computer
of its action.  The IED on the downstream side of the fault notifies
the Substation Computer of the loss of current and estimates the
direction of the fault.  Based on that information and pre-configured
logic, the Substation Computer recommends to the Operator that the
breaker of the downstream IED should be opened and the normally open
switch should be closed.  The Operator typically directs the
Substation Computer to do so, and the Substation Computer forwards the
decision to the IEDs.  When the IEDs perform the operations, power is
restored to all portions of the feeders except the section in which
the fault occurred.  The more break points there are in the feeders,
the fewer customers will be affected by a given fault.

if !vml?![](TO_Auto_Control_Baseline_files/image006.gif)endif?

Time is of the essence in service restoration,
but utilities typically require an Operator approve the decision of
the system, so the human Operator is usually the slowest link in the
system.  Communications times may be measured in seconds.  The breaker
tripping is done by an individual IED without need for communications.

An alternative scenario occurs if the fault is
not on the main feeder but on a lateral.  In this case, the fault
causes the protection IED at the substation to trip and attempt
reclosure.  While the current is zero between reclosure attempts, the
IED nearest the fault opens its switch to clear the fault.  This is
called “auto-sectionalization”.  Then, when the next reclosure occurs,
service is restored to all subscribers except those on the lateral. 
In this case, there is no effect on the communications system other
than to monitor that the events occurred.

if !vml?![](TO_Auto_Control_Baseline_files/image008.gif)endif?

## Normal Sequence Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Voltage Change | Change in Voltage | VOLTAGE REGULATION.  IED identifies that the voltage has exceeded the deadband to be recognized as a change and notifies the Substation Computer Device.   May be performed by one or more IEDs depending on the logic being used.  Substation Computer Device maps the point number into its database, stores the value, and runs the voltage control logic.  Typically starts a qualification timer to avoid rapid and frequent tap changes. | IEDs | Substation Computer Device | Voltage | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 1.2 | Qualification Timeout | Tap Change | Substation Computer Device identifies that the voltage change(s) received from the IED(s) represent a significant change and require action.  Issues a command to the IED.  IED performs the tap change through local I/O.  Causes voltage change (1.1) and cycle repeats. | Substation Computer Device | IED | Tap Change Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 2.1 | Load Change | Change in Load | VOLT/VAR REGULATION.  IED identifies that the voltage and/or current has exceeded the deadband to be recognized as a change and notifies the Substation Computer Device.   May be performed by one or more IEDs depending on the logic being used.  Substation Computer Device maps the point number into its database, stores the value, and runs the Volt/VAR control logic.  Starts a qualification timer if appropriate.  If extremely simple control logic is being used (e.g. calendar, time-of-day, this step may be omitted). | IED | Substation Computer Device | Voltage, Current | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 2.2 | Qualification Timeout | Adjust Reactive Load | Substation Computer Device decides that it is time to adjust the load and issues a control to the appropriate IED.  Applies qualification times and hysteresis algorithms to avoid many rapid adjustments.  May not be the same IED as last reported a Load Change.  Adjustment usually causes a Load Change (2.1) and cycle repeats. | Substation Computer Device | IED | Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 3.1 | System State Change | Change of System State | INTERLOCKING.  IED detects a change in a switch or breaker that it is monitoring and transmits the state change to the device implementing the logic, either the Substation Computer Device or one or more peer IEDs.  Substation Computer Device or peer IED maps the point number into its database, stores the value, and thus updates its current “picture” of the system state. | IED | IED or Substation Computer Device | Switch State, Voltage, Current | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 3.2 | Switch Request | Request Switch | System Operator  requests that a particular switch or breaker be opened or closed.  Device receiving the command runs interlocking logic and either denies (3.3) or accepts (3.4) the request. | System Operator | IED or Substation Computer Device | Control Request | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 3.3 |  | Deny Request | Device performing the interlocking logic rejects the attempt as being unsafe. | IED or Substation Computer Device | System Operator | Control Status | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.1 | Sequenced Control Request | Request Sequenced Control | SEQUENCED CONTROL.  System Operator  requests a sequence to be performed. | System Operator | Substation Computer Device | Control Request | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.2 |  | Send Control | Substation Computer Device runs the sequence logic and issues the next control to an IED. | Substation Computer Device | IED | Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 4.3 | Feedback | Send Feedback | IED provides feedback about whether the last control was successful.    Substation Computer Device maps the point number into its database, stores the value, and runs the sequence logic.  Typically logs the state change and its time.  If feedback was successful, Substation Computer Device initiates next control (4.2).  If not, if the feedback timed out, or if this was the last control, may terminate sequence (4.4). | IED | Substation Computer Device | Switch State | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 4.4 | Sequence Complete | Terminate Sequence | Substation Computer Device stops the sequence logic and indicates to System Operator  the status of the sequence. | Substation Computer Device | System Operator | Control Status | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.1 | Load Change | Change in Load | LOAD BALANCING.  IED identifies that the current has exceeded the deadband to be recognized as a change and notifies the Substation Computer Device.   May be performed by one or more IEDs depending on the logic being used.  Substation Computer Device maps the point number into its database, stores the value, and runs the load balancing control logic. | IED(s) | Substation Computer Device | Current, Voltage | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 5.2 | Request to Connect Feeders / Lines | Request Connection to Feeders / Lines | Substation Computer Device determines that load has exceeded acceptable thresholds and that conditions are met to perform balancing.   Requests that System Operator  connect a particular two feeders or lines.  System Operator  either confirms the operation (5.3) or does nothing, and load continues to increase (5.1). | Substation Computer Device | System Operator | Automated Control Request | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.3 |  | Confirm Request | System Operator  issues control accepting the request. | System Operator | Substation Computer Device | Confirm | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 5.4 |  | Balance Load | Substation Computer Device issues a control to connect the two feeders or lines.  Load will readjust and cycle repeats (5.1). | Substation Computer Device | IED | Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 6.1 | Fault | Breaker Trip | AUTOMATIC SERVICE RESTORATION.  IED detects fault and trips breaker.  Notifies Substation Computer Device of the trip, and (through the point number) the direction and distance to the fault. | Upstream IED | Substation Computer Device | Trip | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 6.2 | Loss of Current | Report Loss of Current | IEDs detect loss of current.  Notify Substation Computer Device of the event and the suspected direction and distance of the fault. | Downstream IEDs | Substation Computer Device | No Current Detected,  No Voltage Detected | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 6.3 |  | Request Restoration | Substation Computer Device runs auto-restoration logic and determines which switch should open.  Requests permission to open that switch and close the normally-open switch.  System Operator  will either confirm the request (6.4), or decide to perform some other operation through the Substation Computer Device. | Substation Computer Device | System Operator | Automated Control Request | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 6.4 |  | Confirm Request | System Operator  tells the Substation Computer Device to execute the restoration. | System Operator | Substation Computer Device | Confirm | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| 6.5 |  | Open Switch | Substation computer performs control to open the downstream switch nearest the fault. | Substation Computer Device | Downstream IED | Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 6.6 |  | Close Switch | Substation Computer Device performs control to close the normally-open switch. | Substation Computer Device | IED controlling normally open switch | Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 6.7 |  | Send Feedback | IEDs update system state and load to Substation Computer Device.  Substation Computer Device maps data and stores in database. | IEDs | Substation Computer Device | Switch State, Current, Voltage | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |

if !supportEndnotes?

---

endif?

## Steps – Alternative / Exception Sequences

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1 |  | Execute Request | Device performing the interlocking logic tells the IED to operate the control request.  May be the same IED. | IED or Substation Computer Device | IED | Control | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| 3.2 |  | Confirm Request | Device performing the interlocking logic informs the System Operator  that the request has been successfully performed. | IED or Substation Computer Device | System Operator | Control Status | [Intra-control center](../Environments/Env7_Intra-Control_Center.htm) |
| X.1 | Fault | Trip Breaker | IED detects fault and trips breaker.  Notifies Substation Computer Device of the trip, and (through the point number) the direction and distance to the fault.  Starts reclosure timer. | Upstream IED | Substation Computer Device | Trip | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| X.2 |  | Report Lateral Switch Open | IED detects the fault and that current is zero. Waits a configured number of reclosure attempts, then opens the switch for the Lateral.  Notifies the Substation Computer Device. | Lateral IED | Substation Computer Device | Switch State | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
| X.3 |  | Breaker Reclosed | Upstream IED successfully recloses the breaker and notifies the Substation Computer Device that service is restored. | Upstream IED | Substation Computer Device | Switch State | [Critical Operations intra-sub](../Environments/Env3_Critical_Operations_Intra-Substation.htm) |
