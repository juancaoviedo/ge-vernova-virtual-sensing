# Emergency Control Base

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Emergency_Control_Baseline.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Automated Control - Emergency Control Baseline Function

## Contents

* [Narrative](TO_Emergency_Control_Baseline.htm#Narrative)
* [Steps](TO_Emergency_Control_Baseline.htm#Steps)

## Narrative

The purpose of the Wide Area Monitoring and
Control Systems - Emergency Operations function is to provide
communications services permitting an operator to take the following
actions in response to a fault in the power system:

* Locate the fault
* Verify that protection has operated
  correctly to clear the fault
* Shed load to ensure that the fault
  does not cause an overload of unaffected lines
* Manually re-route power to restore
  service to subscribers
* Dispatch crews and emergency teams to
  fix the fault
* Capture fault recordings so engineers
  can later analyze the cause of the fault
* This function also addresses handling
  of environmental and security alarms.

A complete narrative of the Function from a
Domain Expert’s point of view, describing what occurs when, why, how,
and under what conditions. This will be a separate document, but will
act as the basis for identifying the Steps in Section 2.

Emergency operations are organizational sequences
of activities that involve multiple integrated actors exchanging
information when a fault is detected on a power system. These
activities are integrated through the use of Wide Area Control and
Monitoring Systems (WAMACS) that provide operational control over the
distributed network of actors that comprise the SCADA system. Each
utility maintains their own WAMACS but in the future these systems
must be linked to provide overall control and monitoring across
multiple organizations to meet the future demands of the suppliers and
users of electrical power.

The remainder of this narrative describes an
example scenario illustrating the characteristics and sequence of
activities that occur on the power system during Emergency Operations.
The example is based on a typical substation with a SCADA system.

if !vml?![](TO_Emergency_Control_Baseline_files/image002.gif)endif?

### Initial State

When a typical substation is operating in the
normal state, called initial state for the purposes of this
discussion, there are at least two incoming lines connected to two
transformers that feed two separate buses that supply the source side
of the feeder circuits. In the initial state both lines and
transformers would be energized and the main breakers would be closed
to allow both buses to be energized. The bus tie breaker between the
two buses is closed so both transformers are sharing the load from all
four feeders.

The lines, transformers, buses and feeders each
are monitored by separate protection relays that can sense
abnormalities in the zone of protection that they are responsible for
and isolate faults in the zone by opening the appropriate breaker.
Adjacent protection relay zones overlap to ensure that there is
protection at every point in the system. Incoming line relays are
responsible for a zone of protection that extends out of the
substation and down the line a certain distance. The other end of the
line is usually owned by the power transmitter and there is similar
distance protection on that end of the line. If a fault occurs on the
line both relays report the distance and direction to the fault. There
should be an overlap in the two fault reports and this is the portion
of the line that the dispatched maintenance crew will check first for
the fault.

In the initial state the SCADA system, shown in
Figure 1, would have no outstanding alarms or abnormal
readings that would require the operator to take action. The SCADA
system, which is made up of these protection IEDs, monitor the
critical areas of the substation and report data to the
Data Concentrator.  The protection IEDs are most often located within a
substation, but may also be located at remote sites or on pole-tops.

if !vml?![](TO_Emergency_Control_Baseline_files/image004.gif)endif?

Figure 1:  SCADA System

GUI – Graphical User Interface

L1/L2 – Line Distance relays

T1/T2 – Transformer relays

M1/M2 – Main Breaker relays

B1/B2 – Bus relays

F1/F2/F3/F4 – Feeder relays

The Data Concentrator  is located in the substation
and is connected with a communication link to each IED. The substation
is often equipped with a local GUI and an alarm logger. The
Data Concentrator  is connected through a different communication link
to one or more GUIs. GUIs can be local to the substation or in an
operations center that monitors several substations.

The operator is located in close proximity to the
GUI, which is the operator’s window into the substation. The
operations center is usually equipped with a logging and trending
system to store analog quantities on a regular interval or on a change
to display the quantities on a graph.  There also must be a method of
storing and accessing fault records that are used by engineers to
analyze the faults.

Data Concentrator s, GUIs, and the communications
links between them and the IEDs are usually redundant, and perform
switchover if one link fails.  Reliability is very important.

### Fault Occurrence and Detection

There are several places where a fault can occur
on this system and several different ways the equipment can be used to
isolate different fault conditions. Some very simple fault scenarios
are used in the discussion to help describe Emergency Operations. Each
zone of protection is equipped with a protection IED, or relay, that
monitors the state of the system and the values of the electrical
quantities that are relevant to the zone of protection. If a fault
occurs the relay is able to cause a breaker and sometimes also a
switch to operate to isolate the fault.

If a fault occurs some distance down the incoming
transmission line the line distance relay associated with that zone is
responsible for detecting the fault, tripping the main breaker and
disconnecting the incoming line disconnect switch. This isolates the
substation from the fault so that the excessive current associated
with the fault does not damage any equipment in the substation. This
operation must occur within one cycle of the power waveform and this
precise timing requires accurate time synchronization to be applied to
the device so that the time the event occurred and the sequence of
events can be determined later. The line distance relay also reports
the system changes caused by the fault to the Data Concentrator  which
in turn passes them to the GUI where the state changes are reported as
system alarms to the operator.

A fault occurring in a different zone of
protection would be handled in a similar way. For example the
transformer relay is responsible for the closed zone of protection
around the transformer. If a transformer fault occurs it opens the
main breaker and then the disconnect switch.

### Fault Record Generated

Often a fault recorder is monitoring the power
system quantities at one or more strategic locations around the
substation. The protection IEDs or the RTU often have built in fault
recorders that can capture data before, during and after a fault.
Engineers will use this information to determine the type, magnitude
and profile of the fault.

During normal operation the fault recorder is
storing several cycles worth of data continuously. If a fault occurs
it triggers the recorder to stop overwriting the pre trigger data and
continue recording the actual fault data. In this way the engineer is
able to observe the stable condition before the fault, (pre trigger),
and exactly what happened at the instant the fault occurred and then
the post fault profile which is the system reaction to the fault.

The fault data profile usually has separate
channels for each of the three phase voltages and currents and can use
other signals as well. The fault data is usually stored in a standard
format in the IED or in the fault recorder that captured the data. A
signal, in the form of an alarm, is sent to the data concentrator and
subsequently to the GUI to notify the operator that a fault file is
available to be analyzed.

### Change of State

Faults cause the system to change state, usually
because one of the protection IEDs has tripped a breaker. The state of
the breaker is detected by a change in position in the detection
device located in close proximity to the breaker. This change of state
is generally detected by the IED and reported to the Data Concentrator 
or detected directly by the Data Concentrator  in other situations. The
Data Concentrator  determines if it is required to communicate the
change of state to the GUI in which case it does. The
Data Concentrator ’s function is to translate the protocol that contains
the state change between the IED and the GUI.

Often there is a large number of devices in the
substation, slow communication links, legacy protocols that do not
have timestamps, sorting requirements or the requirement to send the
change of state data to more than one GUI. All these are reasons why a
Data Concentrator  is required.

### Alarm

A fault causes a breaker to trip which causes a
change of state in the system which is converted to an Alarm by the
GUI to notify the operator of the system change. Usually the alarm
shows up as a flashing text message at the bottom of the active screen
on the operators GUI and is combined with an audible signal in case
the operator is not looking at the screen. The flashing and audible
signal stop when the alarm is acknowledged. Characteristics associated
with each different alarm are preconfigured such as location, priority
and description.

The trip notification is a digital change of
state, accompanied by a timestamp indicating when the event occurred. 
The timestamp is important because it may be later used to reconstruct
a “sequence of events” indicating when various devices and personnel
within the utility took action to address the fault.  For this reason,
time between devices within the SCADA system is typically synchronized
to within 1 millisecond.  Sometimes this takes place over serial links
or LANs, but most commonly is performed by connecting satellite time
sources to each device.

### Retrieve Fault Record

The Fault Record is stored in the IED and a
notification that the record exists is provided and can be obtained.
There is either a manual or automated process in place for retrieving
the Fault Record so that it can be studied. The file is retrieved by
the Data Concentrator  and passed to the GUI where it is stored and
cataloged. The information in the record is analog and digital data
that was captured before, during and after the fault.

There are several issues that can limit the
systems ability to retrieve faults:

* Fault records contain large volumes of
  data that some devices cannot handle.
* Not all Data Concentrator s can forward
  file data.
* Legacy protocols may not support file
  transfer.
* Existing communication links may make
  the transfer of large files too slow.
* Some arrangements require personnel to
  be dispatched to the site to extract the Fault Record
  directly from the IED.

### Change in Line Load

When a breaker trips there is no longer a path
for electrical energy to flow from the live side of the breaker
through to the other side. The breaker has isolated the downstream
equipment by opening the circuit to stop the energy from getting to
the equipment. This always causes a change to the entire load that the
substation is connected to. Anything downstream of the breaker is not
running because the power is removed unless there is a way to feed the
load with energy from another line. The IED monitoring the changed
load is responsible for detecting and reporting the change in the
quantities, such as voltage and current.  The IED provides the
information necessary to understand how the system has changed.

### Analog Data Change

When Analog Data changes in the IED it is
reported to the Data Concentrator  first. If the Data
Concentrator 
identifies the data as being of interest to one or more of the GUIs
that are connected to it and the change in value is significant in
that it exceeds a preconfigured deadband it translates the data from
the IED to the GUI through the communications protocols.

### Change in System Load

When the System Load changes and the GUI is
notified of the change by the Data Concentrator  it must perform several
activities for the operators to be able to investigate:

* Maps the point number of the protocol
  to the appropriate location in the database.
* Scales the data appropriately for
  accurate display in the correct units.
* Updates any values currently being
  displayed.
* Raises appropriate alarms associated
  with the quantities.
* Logs and trends data if required.

### Shed Load or Restore Power

The System Operator addresses the alarm by viewing
the system state displayed on the GUI.  IEDs pass load and switch
state change information to the GUI through the Data Concentrator ,
permitting the System Operator to:

·        
Determine the location of the fault

·        
Verify that the protection equipment has operated
properly to clear the fault (isolate the faulted section).

·        
See the impact of the fault isolation on the rest of the
power system.

The System Operator takes action to address the
alarm.  This action may include any of the following items:

·        
Reset any breakers that should not have tripped.

·        
Disconnect the faulted section of line from the
remainder of the power system, if protection equipment has not already
done so.

·        
Re-route power so the loss of the faulted line does not
cause other portions of the system to be overloaded.

·        
Re-route and restore power so the affected area is
minimized.

·        
Disconnect (shed) load from the power system if there is
no other way to prevent an overload.

From the point of view of the communications
network, the effect of all these actions is the same:  the
System Operator sends control requests to various IEDs within the
substation and elsewhere in the network, to either open or close
switches or breakers.  The System Operator enters these controls at the
GUI.  They are forwarded through the Data Concentrator  to the correct
IED.  At any point in this path, the SCADA System  may reject the
controls if they violate safety rules, e.g. closing a switch to run
power back onto the faulted line.  This is called Interlocking and is
discussed further in the Automated Controls use case.

### Control

If the operator has sent a control the GUI must
format the control into an appropriate request, usually a
Select-Before-Operate service is used, for the Data Concentrator  or IED
and sent through the protocol. The control can be digital such as
changing the state of a breaker or an analog setpoint such as changing
the position of a valve. The information contained in the control
request includes: Point number, operation, duration and setpoint
value.

### Forward Control

If the operator has sent a control that is
destined for a protection IED the Data Concentrator  must forward the
request to the IED. The IED acknowledgement to the request is received
by the Data Concentrator  first and then forwarded to the GUI. This is a
protocol translation function performed by the Data Concentrator . The
indication of the correct state of the control being achieved or the
alarm to indicate that the control failed is also received first by
the Data Concentrator  and then forwarded to the GUI for display on the
screens the operator is looking at. When forwarding the control the
Data Concentrator  uses the Select-Before-Operate service similar to the
GUI. The Data Concentrator  can support multiple GUIs issuing controls
if required.

### Locate Fault

The protection IEDs that monitor the lines, L1
and L2, and the feeders, F1, F2, F3 and F4, usually have the
capability of locating the fault by measuring the impedance of the
line, and then comparing it to known impedances that exist when the
fault is not present and preconfigured characteristics of the line.
Usually the direction and distance to the fault are outputs of the
IEDs calculations. This information is used to make operational and
maintenance decisions by the Data Concentrator , the GUI and the
operator.

### Display Fault Location

The GUI is capable of interpreting the fault data
and providing a meaningful display of the fault location in terms of
the location and distance values that include the overlap provided by
two different relays reporting the same fault from different
locations. It also logs the distance and direction for future
reference by engineers that need to study the characteristics of the
fault.

### Dispatch

The operator dispatches a maintenance crew to an
area where it is believed that the fault exists based on the distance
and direction that was logged and displayed by the GUI. This
dispatching may take place through many types of media, including
radio, telephone, a separate dispatcher, or a computerized system.
Whatever mechanism the operator uses must be wireless at some point
because the crews are mobile. The crew does not utilize the SCADA
network on their own but receives orders directly from the operator.

### Notify

The operator is also responsible for notifying
engineers that study the fault characteristics to determine why the
faults occurred where they did. The priority of this step is increased
if the fault also affected service in a region. The information that
these personnel use is obtained from the Protective Relay, the
Data Concentrator , the GUI and the operator. The personnel interested
in the data are emergency personnel, protection engineers, system
stability analysts and management. The process of notifying additional
personnel may or may not be automated but typically does not use the
SCADA network.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1        1 | Fault | Report Fault | Detects fault and trips appropriate breaker. | Protective Relay | Data Concentrator  (sometimes GUI) | Fault Indication | Must be detected within a cycle.   Timestamp requires accurate synchronization | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 1.2 |  | Generate Report | Send indication that a fault record is available. | Fault Recorder Device | Data Concentrator  or GUI | Fault Indication |  | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 1.3 |  | Report COS | Identifies data as being of interest to the GUI.  Translates protocol from IED to GUI. | Data Concentrator | GUI | Fault Indication | Concentrator required due to slow links, large numbers of devices.  Legacy protocols may not support timestamp.  May sort events by timestamp before transmission  May distribute to multiple GUIs. | [Non-Critical Operations DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 1.4 |  | Notification of Alarm | Identifies the trip as an alarm condition and displays notification on screen.  Maps point number and state to human-readable information.  Logs the alarm / change of state. | GUI | System Operator | Notification of Alarm | Location, priority, description must all be pre-configured. | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.1 | Retrieve Fault | Retrieve Fault | Retrieves the fault record from the fault recorder. | IED | Data Concentrator  or GUI | Analog and digital sample file | Large volumes of data.  Many data concentrators cannot forward files.  Legacy protocols may not support file transfer.  Existing links may make transfer slow.  Sometimes may need to send operator to site. | [Non-Critical Operations DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 3.1 | Change in line load | Change in line load | Detect change in load due to protection activity. | IEDs | Data Concentrator  or GUI | Change in Line Load |  | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 3.2 |  | Change in Analog Data | Identifies data as being of interest to the GUI.  Identifies the change as being significant (deadband).  Converts communications protocol from IED to GUI. | Data Concentrator | GUI | Change in Line Load | May distribute to multiple GUIs. | [Non-Critical Operations DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 3.3 |  | Load Change | Maps point number to database.  Updates values if currently on display.  Raises alarm if threshold exceeded.   Logs data if it is being trended. | GUI | System Operator | Voltage, Current | Scaling is usually pre-configured | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.1 | Shed Load, or Restore Power | Shed Load / Restore Power | Operates control | System Operator | GUI |  |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4.2 |  | Send Control | Sends control or setpoint | GUI | Data Concentrator  or IED | Send Control | Normally uses Select-Before-Operate service.   Occasionally broadcast. | [Non-Critical Operations DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 4.3 |  | Forward Control | Translates control or setpoint and sends to IED. | Data Concentrator | IED | Send Control | Uses Select-Before-Operate service.  Often supports multiple GUIs. | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 5.1 | Locate Fault | Locate Fault | Measures impedance of line and calculates distance based on pre-configured characteristics of the line. | Protective Relay | Data Concentrator  or GUI | Locate Fault |  | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 5.2 |  | Display Location | Displays location and distance on GUI in a manner that shows overlap.  Logs distance and direction. | GUI | System Operator | Display Location |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 6.1 | Dispatch | Dispatch Field Personnel | Dispatches crew based on fault location log and display. | System Operator | Field Personnel | Directions | Currently does not use SCADA network | User Interface |
| 7.1 | Notify | Notify Personnel | Notifies personnel that a service-affecting fault has occurred based on an alarm condition. | GUI, Data Concentrator , System Operator | Protection Engineer, Management Personnel | Request to contact operator | May or may not be automated.  Typically does not use SCADA network | User Interface |
