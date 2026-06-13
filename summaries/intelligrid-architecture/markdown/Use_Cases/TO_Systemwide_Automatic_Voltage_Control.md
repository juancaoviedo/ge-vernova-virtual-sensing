# Systemwide Volt Control

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Systemwide_Automatic_Voltage_Control.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - System-wide Automatic Voltage Control Function

## Contents

* [Narrative](TO_Systemwide_Automatic_Voltage_Control.htm#Narrative)
* [Steps](TO_Systemwide_Automatic_Voltage_Control.htm#Steps)
* [Steps – Alternative / Exception Sequences](TO_Systemwide_Automatic_Voltage_Control.htm#Steps – Alternative / Exception Sequences)

## Narrative

Perform wide-area voltage control through closed loop control by
measuring the wide area voltages, computing a control solution, and
effecting wide area control

System wide voltage and subsequent power flow can be optimized by
looking at the voltage profile for a large segment of the power grid,
choosing set-points for the voltages at the various control points,
and issuing the appropriate control commands to effect the desired
operating point.

Prior to starting the voltage control process, the system would
need to determine the availability (in/out of service) and capacity of
all the control points around the system.  This information would then
have to be factored into the voltage control algorithm.  For example,
if part of a series capacitor bank is out of service, the remaining
available series impedance shall be reported; if an SVC is out of
service, this shall be reported to the Controller.

Voltage (phase and sequence) from 10 to a few hundred points around
the power system are to be measured and transmitted to one or more
Controllers located around the power system.  Each Controller analyzes
the measured voltages and computes an optimal voltage control
solution.  The control solution would include linear control of
generator voltage and synchronous condenser outputs, transformer tap
changer control, voltage regulator control, Thyristor controlled
Series Capacitor (TCSC) control, Static Var Capacitor control, DC link
power flows, as well as on/off control of series and shunt capacitor
banks and reactor switching.  A measure/control link to
DER/ADA/Consumer/Industrial devices is also envisioned that would
enable some voltage support/load shed (in emergency conditions) from
the distribution system.  Upon issuance of the control command, the
device receiving the command shall acknowledge that the voltage
control command was received and subsequently executed.

This devices in this scenario would also be used for Voltage
Security (see Voltage Security use case) and the steps for Voltage
Security are called out as an alternate sequence in the function
steps.

On failure of the communication system to a particular node, that
node shall resort to local voltage control with previously calculated
set-points.  Failure of communication to any remote node shall be
immediately (within 1 second) to the system operator and other
monitoring points as desirable.

## Steps

### Normal Sequence Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | System Initialization | Initialization | System operator starts the automatic voltage control process | Controller | Controllable Device | Initialization data; configuration data | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 1.2 | Programmed data rate | Measure System Voltage | Measure system voltage and stream to Phasor Data Concentrator | Phasor Measurement Unit | Phasor Data Concentrator | Phasor Data stream | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 1.3 | Programmed data rate | Aggregation | Aggregate phasor data streams from multiple Phasor Measurement Unit sources | Phasor Data Concentrator | Controller | Aggregated Phasor Data | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 1.4 | Programmed data rate | Decision | Manipulation of phasor data to determine the control required to implement the optimal system voltage | Controller | Controllable Device | Control information | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 1.5 | Programmed data rate | Acknowledge | Acknowledge that the Controllable Device received the control command and were able to execute as requested | Controllable Device | Controller | Status information | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |

### 

### Steps – Alternative / Exception Sequences

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 | Large system voltage angle detected | Angle Check | Check the difference of the angles of the voltages across the system | Controller | Regional System Operator; Voltage Security Controller | Voltage Security alarm; Voltage angle difference | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 2.2 | Large system voltage angle detected | Voltage Security Control | Determine the corrective action to be taken upon detection of a voltage security issue | Voltage Security Controller | Controller | System phase angles | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 2.3 | Large system voltage angle detected | Issue Control Action | Issue the control actions to the controllable elements around the system | Controller | Controllable Device | Control | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 2.4 | Control action received | Acknowledge | Acknowledgement that the control action has been received and executed | Controllable Device | Controller | Control Acknowledge | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |

###
