# Voltage Security

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Voltage_Security.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - Voltage Security Function

## Contents

* [Narrative](TO_Voltage_Security.htm#Narrative)
* [Steps](TO_Voltage_Security.htm#Steps)

## Narrative

The Voltage Security function is designed to detect severe low
voltage conditions based on phasor measurements of Power and Voltage
and upon detection, initiate corrective action such as load shed.

It has been shown through simulation that for certain credible
contingencies on a power system, there can occur unacceptable
consequences that are characterized by severe low voltages,
excessively high power and MVar flows, and likely split-up of a
utility’s interconnections.  System studies have shown that a combined
measurement of phasor measurements (only angle needed) and power flow
can be used to provide a robust (both dependable and secure)
indication of proximity of power system collapse.  To be included in a
typical measurement set are EHV and HV system voltages and generator
MVar production.  Classification type Decision Trees models are
utilized to predict voltage security status.  Results of the Decision
Tree are executed through control actions on loads and generators
throughout the system.

A stressed power system is characterized by widening angular
separation of bus voltage angles as it moves towards voltage
insecurity. Decision Trees exploit the complex non-linear relationship
between voltage security status and generator Vars/angular difference
in term of hierarchical rules extracted from a large number of
off-line load-flow simulations.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Dq > s.p.  DP > s.p.  DVar > s.p. |  | The Phasor Measurement Unit shall continuously send data to the Decisioner.  On detection of a trigger event, the Phasor Measurement Unit may and the decisioner should log the stream of phasors being delivered | Phasor Measurement Unit | Decisioner | Phasor data | Need to be able to synchronize received data | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
| 2 | Voltage Security Compromised |  | The decisioner shall issue controls to the controllable devices – either on/off or linear control | Decisioner | Field controllable devices | Controls |  | [Non Critical DAC](../Environments/Env6_Non-Critical_Operations_DAC.htm) |
