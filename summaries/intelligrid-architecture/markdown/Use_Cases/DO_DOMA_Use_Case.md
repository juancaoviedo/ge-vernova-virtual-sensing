# DOMA

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DO_DOMA_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Distribution Operation Modeling and Analysis (DOMA)

Link to
[DOMA Steps](DO_DOMA_Use_Case.htm#DOMA Steps)

## DOMA Narrative

This application is based on a real-time
unbalanced distribution power flow for dynamically changing
distribution operating conditions. It analyzes the results of the
power flow simulations and provides the operator with the summary
of this analysis. It further provides other applications with
pseudo-measurements for each distribution system element from
within substations down to load centers in the secondaries. The
model is kept up-to-date by real-time updates of topology,
facilities parameters, load, and relevant components of the
transmission system.

The Distribution Operation Modeling and Analysis
supports three modes of operation:

1.     
 Real-time mode, which reflects present conditions in the power
system.

2.     
 Look-ahead mode, which reflects conditions expected in the
near future (from one hour to one week ahead)

3.     
 Study mode, which provides the capability of performing the
“what if” studies.

![](images/ADA_Information_Flows.jpg)

The key sub-functions performed by the
application are as follows:

### Modeling Transmission/Sub-Transmission System Immediately Adjacent to Distribution Circuits

This sub-function provides topology and
electrical characteristics of those substation transformers and
transmission/sub-transmission portions of the system, where loading
and voltage levels significantly depend on the operating conditions of
the particular portion of the distribution system.  The model also
includes substation transformers and transmission/sub-transmission
lines with load and voltage limits that should be respected by the
application.

### Modeling Distribution Circuit Connectivity

This sub-function provides a topological model
of distribution circuits, starting from the distribution side of the
substation transformer and ending at the equivalent load center on the
secondary of each distribution transformer. A topological consistency
check is performed every time connectivity changes. The model input
comes from SCADA/EMS, Distribution SCADA, from field crews, from DISCO
operator, from AM/FM/GIS, WMS, and OMS databases, and engineers.

### Data Management Issues between AM/FM/GIS and ADA Distribution Connectivity Database

Standard interfaces between different AM/FM/GIS
databases, data converters, and ADA database are not developed yet for
practical use. The AM/FM/GIS databases were not designed for real-time
operational use. They lack many objects and attributes needed for ADA.
The population of the databases is not supported by an interactive
consistency check. The existing extractors of data and the converters
into ADA databases do not determine all data errors. The ADA
applications must conduct additional data consistency checking and
data corrections before recommendations and controls are issued.
Typically utility do not have established procedures for regular
update of the AM/FM/GIS databases by the operation and maintenance
personnel. Therefore many changes implemented in the field remain
unnoticed by the databases. Synchronization of the field state with
the ADA database is a challenge in modern utilities.

### Data Management Issues between CIS and AM/FM/GIS and ADA Distribution Connectivity Database

For the ADA applications, the AM/FM/GIS data
must be associated with the corresponding customer information data
from the CIS database. This data include billing data and description
of the customer specifics, such as rate schedule, customer code, meter
number, address, etc. The critical information is the billing data.
This data is updated based on metering cycles (typically one month)
and is not well synchronized. In order to synchronize billing data an
automated meter reading system should be implemented. In order to
update the ADA databases more frequently, which would increase the
resolution of ADA functions to individual distribution transformers
and even customers, a high capacity communication system should be
introduced to gather the data from hundreds of thousands of meters at
the same time. Some of the modern procedures enabled by AMR conflict
with the needs of ADA model.An example is the consolidated bills,
where the individual load data of distribution transformers located in
different sites of the consolidated company becomes unavailable for
the external to CIS world.

### Modeling Distribution Nodal Loads

This sub-function provides characteristics of
real and reactive load connected to secondary side of distribution
transformer or to primary distribution circuit in case of primary
meter customers. These characteristics are sufficient to estimate kW
and kvars at a distribution node at any given time and day and include
the load shapes and load-to-voltage sensitivities (for real and
reactive power) of various load categories. In real-time mode, the
nodal loads are balanced with real-time measurements obtained from
corresponding primary circuits. A validity check is applied to
real-time measurements.  The load model input comes from Distribution
SCADA, from CIS supported by AMR and linked with AM/FM/GIS, and
weather forecast systems.

### Modeling Distribution Circuit Facilities

This sub-function models the following
distribution circuit facilities:

1.     
Overhead and underground line segments

2.     
Switching devices

3.     
 Substation and distribution transformers, including step-down
transformers

4.     
 Station and feeder capacitors and their controllers

5.     
 Feeder series reactors

6.     
 Voltage regulators (single- and three-phase) and their
controllers

7.     
 LTC’s and their controllers

8.     
 Distribution generators and synchronous motors

9.     
Load equivalents for higher frequency models

All facilities should be modeled with sufficient
details to support the required accuracy of Distribution Operation
Modeling and Analysis application.

### Distribution Power Flow

The sub-function models the power flow including
the impact of automatically controlled devices (i.e., LTCs, capacitor
controllers, voltage regulators), and solves both radial and meshed
networks, including those with multiple supply busses (i.e. having
Distributed Energy Resources (DER) interconnected to the power
system).

### Evaluation of Transfer Capacity

This sub-function estimates the available
bi-directional transfer capacity for each designated tie switch. The
determined transfer capacity is such that the loading of a tie switch
does not lead to any voltage or current violations along the
interconnected feeders.

### Power Quality Analysis

This sub-function performs the power quality
analysis by:

1.      
Comparing (actual) measured and calculated voltages against the limits

2.      
Determining the portion of time the voltage or imbalance are outside
the limits

3.      
Determining the amount of energy consumed during various voltage
deviations and imbalance

4.      
Recording the time when voltage violations occur

5.      
Performing modeling of higher harmonics propagation and resonant
conditions based on information available from the sources of harmonic
distortion

6.      
Performing modeling of rapid voltage changes based on information
available from the sources of voltage distortion

The sub-function provides the ability to estimate
the expected voltage quality parameters during the planned changes in
connectivity and reactive power compensation.

### Loss Analysis

This sub-function bases its analysis on technical
losses (e.g., conductor I2R losses, transformer load and
no-load losses, and dielectric losses) calculated for different
elements of the distribution system (e.g., per feeder or substation
transformer). For the defined area, these losses are accumulated for a
given time interval (month, quarter, year, etc.). They are further
compared with the difference between the energy input (based on
measurements) into the defined area and the total of relevant billed
kWh (obtained from the database), normalized to the same time
interval. The result of the comparison is an estimate of commercial
losses (e.g., metering errors and theft).

### Fault Analysis

This sub-function calculates three-phase,
line-to-line-to-ground and line-to-ground fault currents for each
protection zone associated with feeder circuit breakers and field
reclosers. The minimum fault current is compared with protection
settings while the maximum fault current is compared with interrupting
ratings of breakers and reclosers. If the requirements are not met, a
message is generated for the operator.

### Evaluation of Operating Conditions

This sub-function determines the difference
between the existing substation bus voltage and the substation bus
voltages limits.

The sub-function also estimates the available
dispatchable real and reactive load obtainable via volt/var control.  
The operator or other applications can use this information for
selective load reduction. The sub-function provides aggregated
operational parameters for the transmission buses to be used in
transmission operation models.

## DOMA Steps

The DOMA Steps include:

* [DOMA Data Conversion](DO_DOMA_Use_Case.htm#DOMA Setup)
* [DOMA without Events](DO_DOMA_Use_Case.htm#DOMA without Events)
* [DOMA with Events Causing
  It to Run](DO_DOMA_Use_Case.htm#DOMA Event Run)
* [DOMA Runs Based on a Schedule](DO_DOMA_Use_Case.htm#DOMA Scheduled Run)
* [DOMA Used in Study
  Mode or Look-Ahead Mode](DO_DOMA_Use_Case.htm#DOMA Study/Look-Ahead Mode)

### DOMA Data Conversion

[![](images/ADA_Data_Conversion_small.jpg)](images/ADA_Data_Conversion.jpg)

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1.1 | Data conversion and validation | Extraction, conversion & validation | ADA Database Administrator authorizes the Conversion and Validation function to extract, convert, and validate circuit connectivity and distribution transformer loading data. This is referred to as Stage 1 validation. | ADA Database Administrator | Conversion and Validation function | Authorization to start Stage 1 validation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.2 |  | Checking real-time data | The data in the latest download of DMS SCADA data is checked by DOMA function for changes in topology and used to obtain the latest relevant analog data. | DMS SCADA Database | DOMA function | DMS real-time analog, status & TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.3 |  | Connectivity change | Topology Update function prepares changes in connectivity based on the latest DMS SCADA data for updating ADA database | DOMA function | Topology Update function | Changes in connectivity | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.4 |  | ADA database update | Topology Update function updates ADA database | Topology Update function | ADA Database | ADA database update | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.5 |  | Extraction, conversion & validation | Conversion and Validation function receives initial (before any corrections) connectivity, billing and facility parameter data. | AM/FM/CIS database | Conversion and Validation function | Initial connectivity, billing and facility parameter data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.6 |  | Issuing initial Stage 1 report | After Conversion and Validation function completes Stage 1 analysis it issues a report with incorrect circuit connectivity and transformer loading | Conversion and Validation function | ADA Database Administrator | Report with incorrect circuit connectivity and transformer loading | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.7 |  | Stage 1 corrections | After reviewing the Stage 1 report, the ADA Database Administrator issues an authorization to perform Stage 1 corrections. | ADA Database Administrator | IT technician | Authorization to perform Stage 1 corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.8 |  | Stage 1 corrections | AM/FM/CIS database is corrected based on the Stage 1 report after ADA Database Administrator authorized the procedure. | IT technician | AM/FM/CIS database | Stage 1 corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.9 |  | Extraction, conversion & validation | Conversion and Validation function receives connectivity, billing and facility parameter data after Stage 1 corrections have been implemented. | AM/FM/CIS database | Conversion and Validation function | Connectivity, billing and facility parameter data after Stage 1 | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.10 |  | Issuing report requiring no database corrections after Stage 1 | After Conversion and Validation function completes Stage 1 analysis it issues a report showing that no further corrections associated with connectivity, billing or facility parameter data are required. | Conversion and Validation function | ADA Database Administrator | Report showing that circuit connectivity and transformer loading require no corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.11 |  | Update of ADA Test Database after Stage 1 corrections | After Stage 1 corrections produce a report with no connectivity and transformer loading problems, the Conversion and Validation function updates the ADA Test Database which sets the stage for Stage 2 validation. | Conversion and Validation function | ADA Test Database | Update of ADA Test Database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.12 |  | Load Flow and Load Transfer Analyses | ADA Database Administrator authorizes the Conversion and Validation function to validate facility parameters via load flow and load transfer analyses. This is referred to as Stage 2 validation. | ADA Database Administrator | Conversion and Validation function | Authorization to start Stage 2 validation | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.13 |  | Load Flow and Load Transfer Analyses | Conversion and Validation function receives excerpts from ADA Test Database (after they were updated with Stage 1 corrections) to perform Stage 2 analyses. | ADA Test Database | Conversion & Validation function | Excerpts from ADA Test Database after Stage 1 corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.14 |  | Load Flow and Load Transfer Analyses | Conversion and Validation function receives latest statuses and measurements from ADA Database (which in turn are updated by DMS SCADA Database) to perform Stage 2 analyses. | ADA Database | Conversion & Validation function | Latest statuses and measurements from ADA Database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.15 |  | Load Flow and Load Transfer Analyses | After performing Stage 2 analyses, Conversion and Validation function issues a report for ADA Database Administrator. | Conversion & Validation function | ADA Database Administrator | Report on unreasonable load and voltage violations, corresponding facility parameters, results of comparative analyses and correction of inconsistencies | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.16 |  | Stage 2 corrections | After reviewing the Stage 2 report, the ADA Database Administrator issues an authorization to perform Stage 2 corrections. | ADA Database Administrator | IT technician | Authorization to perform Stage 2 corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.17 |  | Stage 2  corrections | AM/FM/CIS database is corrected based on the Stage 2 report after ADA Database Administrator authorized the procedure. | IT technician | AM/FM/CIS database | Stage 2 corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.18 |  | Extraction, conversion & validation | Conversion and Validation function receives connectivity, billing and facility parameter data after Stage 2 corrections have been implemented. | AM/FM/CIS database | Conversion and Validation function | Connectivity, billing and facility parameter data after Stage 2 | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.19 |  | Update of ADA Test Database after Stage 2 corrections | The Conversion and Validation function updates the ADA Test Database. | Conversion and Validation function | ADA Test Database | Update of ADA Test Database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.20 |  | Load Flow and Load Transfer Analyses | Conversion and Validation function receives excerpts from ADA Test Database (after they were updated with Stage 2 corrections) to perform the next round of Stage 2 analyses. | ADA Test Database | Conversion & Validation function | Excerpts from ADA Test Database after Stage 2 corrections | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.21 |  | Load Flow and Load Transfer Analyses | Conversion and Validation function receives latest statuses and measurements from ADA Database (which in turn are updated by DMS SCADA Database) to perform the next round of Stage 2 analyses. | ADA Database | Conversion & Validation function | Latest statuses and measurements from ADA Database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.22 |  | Issuing report requiring no database corrections after Stage 2 | After Conversion and Validation function completes Stage 2 analysis it issues a report showing that no further corrections associated with unreasonable load and voltage violations, or corresponding facility parameters are required. | Conversion & Validation function | ADA Database Administrator | Report showing that no further corrections associated with unreasonable load and voltage violations, or corresponding facility parameters are required. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.23 |  | Update of ADA Database | After reviewing the Stage 2 report requiring no further corrections, ADA Database Administrator authorizes the update of ADA database. | ADA Database Administrator | IT technician | Authorization to update ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.24 |  | Update of ADA Database | After permission to update ADA database is given, IT technician receives the needed update from ADA Test database. | ADA Test Database | IT technician | ADA database update | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.1.25 |  | Update of ADA Database | IT technician updates ADA database | IT technician | ADA Database | ADA database update | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |

### DOMA Runs but Senses No Events

![](images/DOMA_with_No_Events.jpg)

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.2.1 | DOMA No Events | Checking real-time data | DOMA function receives the latest scan of DMS SCADA database to be checked for relevant changes or events. | DMS SCADA database | DOMA function | DMS real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2.2 |  | Checking real-time data | DOMA function receives the latest scan of EMS SCADA database to be checked for relevant changes or events. | EMS SCADA database | DOMA function | EMS real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2.3 |  | Checking real-time data | DOMA determines that no changes or events are present in SCADA scan. | DOMA function | DOMA function | No changes or events are detected. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2.4 |  | DOMA function status verification | DOMA status is verified (on/off) for reporting it to the operator. | DOMA function | Operator | DOMA function status | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |

### DOMA Runs Due to Events

[![](images/DOMA_Runs_Upon_Event_small.jpg)](images/DOMA_Runs_Upon_Event.jpg)

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.3.1 | DOMA Event Run | Checking real-time data | DOMA function receives the latest scan of DMS SCADA database to be checked for relevant changes or events. | DMS SCADA database | DOMA function | DMS real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.2 |  | Checking real-time data | DOMA function receives the latest scan of EMS SCADA database to be checked for relevant changes or events. | EMS SCADA database | DOMA function | EMS real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.3 |  | Checking real-time data | DOMA, after detecting changes in connectivity, transfers relevant data to Topology Update function. | DOMA function | Topology Update function | Changes in connectivity | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.4 |  | ADA database update | Topology Update function updates ADA database with detected changes in connectivity detected by DOMA function and with latest analog measurements. | Topology Update function | ADA database | Changes in connectivity and latest analog measurements | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.5 |  | Checking distribution model integrity | Topology Update function gives permission to DOMA function to analyze the distribution model integrity after ADA database is updated with latest changes. | Topology Update function | DOMA function | Permission to analyze distribution model integrity | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.6 |  | Checking distribution model integrity | DOMA function receives the data from ADA database needed for integrity check. | ADA database | DOMA function | Excerpts from ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.7a |  | Checking distribution model integrity | The distribution model integrity is confirmed and DOMA gives the permission for performing state estimation and power flow calculations. | DOMA function | DOMA function | Permission for performing state estimation and power flow calculations | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.8a |  | State estimation and power flow calculations | DOMA function receives the data from ADA database needed for state estimation and power flow calculations. | ADA database | DOMA function | Excerpts from ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.9a |  | State estimation and power flow calculations | Upon completion of state estimation and power flow calculations, DOMA function makes the connectivity, facility (including controllers), load and transmission data available to FLIR function. | DOMA function | FLIR function | Connectivity, facility (including controllers), load and transmission data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.10a |  | State estimation and power flow calculations | Upon completion of state estimation and power flow calculations, DOMA function makes the connectivity, facility (including controllers), load and transmission data available to VVC function. | DOMA function | VVC function | Connectivity, facility (including controllers), load and transmission data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.11a |  | Analysis of distribution state estimation and power flow results | DOMA makes results of power flow calculations available for analysis. | DOMA function | DOMA function | Results of power flow calculations | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.12a |  | Analysis of distribution state estimation and power flow results | DOMA issues a report with results of analysis of state estimation and power flow calculations for storage in historic ADA database. | DOMA function | Historic ADA database | Power flow results, dispatchable kW & kvar, bus voltage limits, customer extreme voltages, segment and xmfr overloads, imbalances, load transfer capacity for selected ties, losses, quality and fault analyses, alarms (if any) about load/voltage violations and from fault analysis, logs | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.13a |  | Analysis of distribution state estimation and power flow results | Selected results of analysis of state estimation and power flow calculations are made available for the operator, EMS, and distributed intelligence schemes. | DOMA function | Operator, EMS | DOMA function status, dispatchable kW & kvar, bus voltage limits, aggregated load characteristics, transfer capacity, customer extreme voltages and imbalances, alarms (if any) about load/voltage violations and from fault analysis | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.14a |  | Analysis of distribution state estimation and power flow results | If analysis of state estimation and power flow calculations detect a voltage or overload violation, VVC is initiated | DOMA function | VVC function | Initiation of VVC | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.7b |  | Checking distribution model integrity | If checking the distribution model integrity identifies a model inconsistency, a message describing the inconsistency is issued for storage in ADA database. | DOMA function | ADA database | Message describing distribution model inconsistency | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.8b |  | Checking distribution model integrity | If checking the distribution model integrity identifies a model inconsistency, a message describing the inconsistency is issued for the operator. | DOMA function | Operator | Message describing distribution model inconsistency | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.9b |  | Checking distribution model integrity | If checking the distribution model integrity identifies a model inconsistency, a command to switch VVC to default settings is issued. | DOMA function | VVC | Command to switch VVC to default settings | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3.10b |  | Checking distribution model integrity | If checking the distribution model integrity identifies a model inconsistency, a command to switch FLIR to default settings is issued. | DOMA function | FLIR | Command to switch FLIR to default settings | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |

### DOMA Runs Based on a Schedule

[![](images/DOMA_Scheduled_Run_small.jpg)](images/DOMA_Scheduled_Run.jpg)

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.4.1 | DOMA Scheduled Run | Checking real-time data | DOMA function receives the latest scan of DMS SCADA database to be checked for relevant changes or events. | DMS SCADA database | DOMA function | DMS real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.2 |  | Checking real-time data | DOMA function receives the latest scan of EMS SCADA database to be checked for relevant changes or events. | EMS SCADA database | DOMA function | EMS real-time analog, status, TLQ data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.3 |  | Checking real-time data | DOMA determines that no changes or events are present in SCADA scan. | DOMA function | DOMA function | No changes or events are detected. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.4 |  | State estimation and power flow calculations | DOMA function receives the data from ADA database needed for state estimation and power flow calculations. | ADA database | DOMA function | Excerpts from ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.5 |  | State estimation and power flow calculations | Upon completion of state estimation and power flow calculations, DOMA function makes the connectivity, facility (including controllers), load and transmission data available to FLIR function. | DOMA function | FLIR function | Connectivity, facility (including controllers), load and transmission data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.6 |  | State estimation and power flow calculations | Upon completion of state estimation and power flow calculations, DOMA function makes the connectivity, facility (including controllers), load and transmission data available to VVC function. | DOMA function | VVC function | Connectivity, facility (including controllers), load and transmission data | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.7 |  | Analysis of distribution state estimation and power flow results | DOMA makes results of power flow calculations available for analysis. | DOMA function | DOMA function | Results of power flow calculations | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.8 |  | Analysis of distribution state estimation and power flow results | DOMA issues a report with results of analysis of state estimation and power flow calculations for storage in historic ADA database. | DOMA function | Historic ADA database | Power flow results, dispatchable kW & kvar, bus voltage limits, customer extreme voltages, segment and xmfr overloads, imbalances, load transfer capacity for selected ties, losses, quality and fault analyses, alarms (if any) about load/voltage violations and from fault analysis, logs | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.9 |  | Analysis of distribution state estimation and power flow results | Selected results of analysis of power flow calculations are made available for the operator and EMS. | DOMA function | Operator,  EMS | DOMA function status, dispatchable kW & kvar, bus voltage limits, customer extreme voltages and imbalances, alarms (if any) about load/voltage violations and from fault analysis | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.10 |  | Analysis of distribution state estimation and power flow results | Analysis of power flow results includes transfer capacity of selected ties, which is transmitted to distributed intelligence schemes. | DOMA function | Distributed intelligence schemes | Transfer capacity of selected ties | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4.11 |  | Analysis of distribution state estimation and power flow results | If analysis of power flow calculations detect a voltage or overload violation, VVC is initiated | DOMA function | VVC function | Initiation of VVC | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) |

### DOMA Study/Look-Ahead Mode

[![](images/DOMA_Study_Mode_small.jpg)](images/DOMA_Study_Mode.jpg)

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environment | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.5.1 | DOMA Study/Look Ahead Mode | Data conversion and validation | Conversion and validation function receives the latest database download to extract, convert and validate circuit connectivity and transformer loading data (Stage 1) as well as to validate facility parameters via load flow and load transfer analyses (Stage 2). | AM/FM/CIS database | Conversion and validation function | Connectivity, billing and facility parameters | [Control Center to Corporate](../Environments/Env12_Control_Center_to_Corporate.htm) | |
| 1.5.2 |  | Data conversion and validation | Conversion and validation function updates ADA database with the latest changes in AM/FM/CIS database. | Conversion and validation function | ADA database | Update of ADA database | [Control Center to Corporate](../Environments/Env12_Control_Center_to_Corporate.htm) | |
| 1.5.3 |  | Preparation of distribution system states as input for DOMA | ADA dispatching routine, responsible, among other things, for triggering scheduled runs of various ADA functions, issues a command to initiate the look-ahead mode. | ADA dispatching routine | DOMA function | Command to initiate look-ahead mode. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.4 |  | Preparation of distribution system states as input for DOMA | Operator gives the command to initiate the study mode. | Operator | DOMA function | Command to initiate study mode. | User Interface | |
| 1.5.5 |  | Preparation of distribution system states as input for DOMA | DOMA receives information about the outages: present and future, which is reflected in preparation of distribution system state. | WMS | DOMA | Schedules presently active or authorized for future outages | [Control Center to Corporate](../Environments/Env12_Control_Center_to_Corporate.htm) | |
| 1.5.6 |  | ADA database update | Environmental data for DER operation forecasting is updated in ADA database. | Environmental daily data collector | ADA database | Environmental data for DER load and schedule forecast | [Control Center to Corporate](../Environments/Env12_Control_Center_to_Corporate.htm) | |
| 1.5.7 |  | Preparation of distribution system states as input for DOMA | Load forecaster receives distribution transformer daily loading data and environmental data for DER load to be used in preparation of distribution system state. | ADA database | Load forecaster | Distribution transformers daily loading, environmental data for DER load and schedule forecasts | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.8 |  | Preparation of distribution system states as input for DOMA | DOMA receives the distribution transformer loading and DER operational forecasts needed for preparation of distribution system states to be studied in the study and look-ahead modes. | Load forecaster | DOMA function | Distribution transformer loading and DER operational forecasts | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.9 |  | Preparation of distribution system states as input for DOMA | DOMA receives the excerpts from ADA database needed for preparation of distribution system states. | ADA database | DOMA function | Excerpts from ADA database | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.10 |  | Preparation of distribution system states as input for DOMA | Statuses and analogs associated with the given distribution system state are made available for study and look-ahead modes. | DOMA function | DOMA function | Statuses and analogs | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.11 |  | Checking distribution system state | The given distribution system state is checked for inconsistencies. | DOMA function | DOMA function | Input data for a given distribution system state | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.12 |  | Performing distribution state estimation and power flow calculations | DOMA function performs distribution power flow calculations making the results available for analyses. | DOMA function | DOMA function | Results of distribution state estimation and power flow calculations | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.13 |  | Analysis of distribution power flow calculations results | Analysis of the results of the distribution power flow calculations are made available for archiving. | DOMA function | ADA historic database | Power flow results, dispatchable kW and kvar, bus voltage limits, customer extreme voltages and imbalances, losses, quality and fault analyses, alarms about load/voltage violations, logs. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
| 1.5.14 |  | Analysis of distribution power flow calculations results | Analysis of the results of the distribution power flow calculations are made available for the operator. | DOMA function | Operator | DOMA status, dispatchable kW and kvar, bus voltage limits, customer extreme voltages and imbalances, alarms about load/voltage violations. | User Interface | |
| 1.5.15 |  | Preparation of distribution system states as input for DOMA | Upon completion of analysis of the results of the distribution power flow calculations DOMA function issues a command to start the study of the next distribution system state. | DOMA function | DOMA function | Command to start the study of the next distribution system state. | [Intra-Control Center Environment](../Environments/Env7_Intra-Control_Center.htm) | |
