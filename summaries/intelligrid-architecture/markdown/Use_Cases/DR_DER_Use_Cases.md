# Distributed Resources

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/DR_DER_Use_Cases.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Distributed Energy Resources (DER) Power System Functions

## Introduction

The following Use Cases can be reviewed for content and can be used to
link to the appropriate Environments and potential technical solution and best practices:

a.     
[DER Operated by Aggregator](DR_DER_Aggregator_Use_Case.htm)

---

## List of Distributed Energy Resources Functions

The following DER functions have been described and their communication
requirements have been identified, but they have not been analyzed in great
detail.

## 1.1           Interconnection Planning (months to years ahead for new construction)

### 1.1.1                   Distributed Resources (DR) Owner Plans (technically) for DR Devices

The purpose of DISTRIBUTED RESOURCES (DR) OWNER PLANS
(TECHNICALLY) FOR DR DEVICES function is to determine whether a proposed DR
installation will likely provide the required electrical power economically at
the appropriate time without detriment to the grid and to estimate the value of
the proposed installation to the grid. directly involving DR owner, DR
Aggregator, DisCo, Permitting Authorities (government agencies), performing load
forecast and energy requirements, pricing projections, site analysis,
environmental impact studies, review of interconnection requirements and
economics, with key interfaces: between

      - DR owner and Permitting Authority,

      - DR owner and DisCo,

      - DR owner and DR Aggregator,

      - DR Aggregator and RTO/ISO,

This function has the following key requirements:

·        
With communication configuration requirements of e-mail, phone,
fax, document transfer to communicate with parties involved. Internet access to
download DisCo interconnection specs, government regulations, etc.

·        
With communication service quality requirements of Medium
availability and response; not a real-time process. Data must be timely and
accurate to minimize approval delays,

·        
With security requirements of high confidentiality of DR owner
plans for competitive reasons and to prevent use of the plans for acts aimed at
disrupting the owners operation,

·        
With data management requirements of tracking numerous legal and
contractual documents; a few databases with variant forms of data updated
infrequently,

·        
With constraints/concerns: highly iterative nature of procedure to
identify appropriate sites, or to negotiate the value of a particular site, that
can meet the technical interconnection requirements and satisfy economic
constraints. Numerous procedural delays are common extending.

### 1.1.2                   DisCo Studies the Impact of High Levels of DR on Distribution System

The purpose of DISCO STUDIES THE IMPACT OF HIGH LEVELS OF
DR ON DISTRIBUTION SYSTEM function is to determine general limits for DR
connections to the distributions systems and to establish standards for system
design to better accommodate DR in the future. directly involving distribution
planners, consultants, DR vendors, research organizations (DOE, EPRI, national
laboratories). performing detailed performance studies on both specific systems
and generalized systems for transient and steady-state performance with a
variety of DR located throughout the system. with key interfaces: between

      - DisCo Planners and DisCo Protection personnel,

      - DisCo Planners and Consultants,

      - Consultants and Research funding agencies,

      - DisCo Planners and Research funding agencies,

      - DisCo Planners and DR vendors.

This function has the following key requirements:

·        
With communication configuration requirements of e-mail, phone,
fax, document transfer to communicate with parties involved. Connection to
internal planning and system model databases.

·        
With communication service quality requirements of Medium
availability and response; not a real-time process. Data must be timely and
accurate to facilitate studies.

·        
With security requirements of Low to high confidentiality. Many
reports of results will be public or made available to prospective DR sites, but
system data may be considered confidential.

·        
With data management requirements of converting system model data
from some stored form to a form appropriate for transfer third parties (e.g..
consultants) to perform studies (likely several variant forms of model data and
documents) with studies updated every few years,

·        
With constraints/concerns: obtaining accurate system data and
descriptions of characteristics of DR devices suitable for studies..

### 1.1.3                   DisCo Acquires DR Base Information (to provide ratings and device models)

The purpose of DISCO ACQUIRES DR BASE INFORMATION (TO
PROVIDE RATINGS AND DEVICE MODELS) function is to perform studies, to determine
how to dispatch the DR, directly involving DisCo planners, Disco DMS, DR vendor,
DR owner, DR aggregator, performing detailed system performance studies to
determine best locations on system, or the value of a specific location, for DR
of particular type and size, with key interfaces: between

      - DisCo Planners and DR Owners,

      - DR owners and DR vendors,

      - DisCo Planners and DisCo DMS,

      - DR aggregators and DR owners,

This function has the following key requirements:

·        
With communication configuration requirements of e-mail, phone,
fax, document transfer to communicate with parties involved, transfer drawings
and numerical (text) data. Key data transferred to DisCo DMS for dispatching and
monitoring,

·        
With communication service quality requirements of Medium
availability and response; not a real-time process. Data must be timely and
accurate to facilitate interconnection studies and dispatch or monitoring of DR
by DisCo DMS.

·        
With security requirements of High confidentiality of DR vendor
and DR owner for competitive reasons. Certain key data such as base rating may
be published according to state and local policies.

·        
With data management requirements of a few databases updated
infrequently requiring conversion of DR device data from printed form to digital
form accurately and keeping current on devices whose characteristics change with
time with ambient conditions or human intervention.

·        
With constraints/concerns: obtaining sufficiently accurate system
data and descriptions of characteristics of DR devices suitable for studies and
dispatch and control of DR. Also, capturing present characteristics of devices
that can be reprogrammed remotely by changing firmware..

### 1.1.4                   DisCo Analyzes DR Interconnection to the Power System

The purpose of DISCO ANALYZES DR INTERCONNECTION TO THE
POWER SYSTEM function is to determine what changes, if any, must be made to the
operation of the distribution system to accommodate the DR and to determine the
protective equipment necessary and the settings for such equipment. directly
involving DisCo Planner, DisCo protection engineers, DisCo rates personnel,
DisCo Account representatives, consultants, DR Owner, DR Vendor, performing
analysis and simulation to verify protection performance and safety issues of
proposed DR installation as well as the value of the proposed site relative to
DisCo planning issues. with key interfaces: between

      - DR owner and DisCo account reps,

      - DisCo planners and protection engineers and
consultants,

      - DisCo planners and DisCo rates personnel,

      - DisCo protection engineers and DisCo account
reps,

This function has the following key requirements:

·        
With communication configuration requirements of e-mail, phone,
fax, document transfer to communicate with parties involved, transfer drawings,
numerical (text) data, and documents related to negotiations on rates and other
aspects of interconnection agreements,

·        
With communication service quality requirements of Medium
availability and response; not a real-time process. Data must be timely and
accurate to facilitate interconnection studies and negotiation of
interconnection agreement.

·        
With security requirements of High confidentiality of DR owner for
competitive reasons during performance of interconnection studies. After
successful negotiations, certain key data will become public.

·        
With data management requirements of a few databases, updated
infrequently containing several documents and non-integrated system models
derived from conversion of DR interconnection and proposed operations data from
drawings and other printed form to digital form for engineering models and,

·        
With constraints/concerns: obtaining sufficiently accurate system
data and descriptions of characteristics of DR devices suitable for technical
studies and economic impact studies on the proposed DR interconnection and
monitoring of compliance with the interconnection agreements..

### 1.1.5                   Energy Services Provider Installs and Tests DR and DR Interconnection

The purpose of ENERGY SERVICES PROVIDER INSTALLS AND
TESTS DR AND DR INTERCONNECTION function is to implement the DR installation and
verify that it is functioning according to specifications. directly involving
Disco account representative, DisCo service crew, DR owner, Electrical
contractor, Electrical inspectors, performing installation and testing of the DR
equipment and final electrical inspections. The DisCo makes final connection to
distribution system. with key interfaces: between

      - Disco and DR owner,

      - DR installer and DR owner for coordination and
scheduling of resources.

This function has the following key requirements:

·        
With communication configuration requirements of elements
sufficient to test communications equipment installed with the DR.

·        
With communication service quality requirements of High
reliability, Medium speed data communications between DR equipment and DisCo,

·        
With security requirements of High confidentiality of DR owner and
energy services provider for competitive reasons,

·        
With data management requirements of a few databases with
infrequent updating.

### 1.1.6                   RTO/ISO/DisCo Certifies DR Units

The purpose of RTO/ISO/DISCO CERTIFIES DR UNITS function
is to provide oversight of DR installations to maintain a high level of
reliability and to ensure the compliance of DR owners with interconnection
agreements. directly involving Disco account representative, DisCo protection
engineers, DisCo line maintenance personnel, DisCo DMS, DR owner, DR installer,
performing oversight and inspection of installation and testing, communication
testing for DisCo DMS (or SCADA). Also production of formal certification for
DR. with key interfaces: between

      - DR owner and DisCo account reps,

      - DR Installer and DisCo Acct Rep,

      - DR Installer and DisCo DMS,

      - DisCo Line maintenance personnel and DR owner,

This function has the following key requirements:

·        
With communication configuration requirements of e-mail, phone,
fax, document transfer for off line transactions. Communications agreed upon for
interconnection agreement between DisCo DMS and DR equipment.

·        
With communication service quality requirements of hi reliability,
high speed data communications between DR equipment and DisCo DMS.

·        
With security requirements of Low for certification since this
public knowledge. Connection to DisCo DMS would have security specified in
interconnection agreement,

·        
With data management requirements of a few databases with
infrequent updating.

### 1.1.7                   RTO/ISO/DisCo Coordinate Long Term Transmission and Generation Maintenance

The purpose of RTO/ISO/DISCO COORDINATE LONG TERM
TRANSMISSION AND GENERATION MAINTENANCE function is to maintain adequate
generation capacity during equipment outages. directly involving RTO/ISO
Dispatching, DisCo Operations, DR owner, DR Aggregator, performing coordination
between each entity for scheduling maintenance and outage of facilities, with
key interfaces: between

      - DisCo Operations and DR owner,

      - DR Aggregator and DR owner,

      - RTO/ISO Dispatch and DR Aggregator,

      - RTO/ISO Dispatch and DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of e-mail, phone,
fax, document transfer to communication maintenance plans and schedules to
selected DR owners. DisCo and/or DR aggregator have secure resource planning
data link,

·        
With communication service quality requirements of Medium for
email and telecom, but High reliability and High security for scheduling
interface,

·        
With security requirements of Medium High since this information
might be used to disable the power system. This information should be provided
only to larger, dispatchable DR facilities capable of controlling access to the
information.

·        
With data management requirements of a few databases with
daily/weekly/monthly updating and coordinated among the various parties.

### 1.1.8                   RTO/ISO/DisCo Register and Perform Credit Rating of DR Owners

The purpose of RTO/ISO/DISCO REGISTER AND PERFORM CREDIT
RATING OF DR OWNERS function is to ensure that the DR owner has the access to
cash to meet fiduciary responsibilities. directly involving Market participants,
performing credit scoring, with key interfaces: between Market participants,

This function has the following key requirements:

·        
With communication configuration requirements of interconnection
with credit agencies and DisCo customer databases through secure public channels
in most cases.

·        
With communication service quality requirements of medium
availability, medium response, because process is not real time.

·        
With security requirements of High confidentiality.

·        
With data management requirements of large database, infrequent
updating,

·        
With constraints/concerns: similar to market operations.

### 1.1.9                   RTO/ISO/DisCo Register DR Meters

The purpose of RTO/ISODISCO REGISTER DR METERS function
is to have metering used by DR certified and registered with the DisCo, RTO and
ISO, directly involving DisCo IT department, Disco account representative, DR
owners, DR aggregators, with key interfaces: between DisCo IT department and DR
owners,

Disco account rep and DR owners,

RTO/ISO/DisCo and DR aggregators,

This function has the following key requirements:

·        
With communication configuration requirements of custom AMR system
or secure internet connection to meters. (Meters will be read manually if not
automatically.),

·        
With communication service quality requirements of typically
monthly readings. Future requirements related to DR may require more rapid
reconciliation of accounts for better managing of energy costs. Real-time meter
reading will be used to verify output of DR for conformance and estimating
additional capabilities,

·        
With security requirements of High confidentiality. Only DisCo and
possibly aggregator should have access to the meters. Details of interconnection
agreement should be restricted to DisCo management and appropriate DR owner
personnel unless required to be public by regulatory agency,

·        
With data management requirements of large database, infrequent
updating, with confidentiality of metering agreements and data,

·        
With constraints/concerns: similar to market operations.

## 1.2           Real-time Interconnected DR Management (Micro EMS Concept)

### 1.2.1                   DR Operates in Local Power System Only, with Load Following

The purpose of DR OPERATES IN LOCAL POWER SYSTEM ONLY,
WITH LOAD FOLLOWING function is to Follow normal daily load changes, Analyze
load requirements, Forecast load requirements, Provide means for supplying
replacement power following loss of generation, Optimize system operation,
directly involving Dr Operator/Owner

DisCo Operator/Owner

RTO, performing System operation to maximize asset
utilization, Routine maintenance activities, Control functions for meeting load
demand, with key interfaces: between DR owner/operator and DisCo DR
owner/operator and RTO,

This function has the following key requirements:

·        
With communication configuration requirements of LAN for internal
DR system operation, WAN for DR to DisCo and DR to RTO communication,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High to allow for continuous
operation of local system,

·        
With data management requirements of Mainly associated with the
operation of the local system and related data recording and transferring
functions.

·        
With constraints/concerns: Accurate coordination with DisCo to
avoid synchronization problems if local system is to be connected to grid.

### 1.2.2                   DR Operator’s SCADA Monitors and Controls Aggregated DR Devices

The purpose of DR OPERATOR’S SCADA MONITORS AND CONTROLS
AGGREGATED DR DEVICES function is to Supervise DR generation Control DR
generation Perform data transfers Monitor power flows, directly involving DR
owner/operator DisCo RTO/ISO, performing Overall DR system supervision

·        
Data acquisition

·        
Data logging

·        
Control functions

·        
Alarm processing

with key interfaces: between DR system operator and DisCo
DR system operator and RTO,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for DR owner
/ operator to Disco and to RTO ; LAN for internal DR,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High, to assure reliable DR/grid
interconnection,

·        
With data management requirements of Associated with the
monitoring of the DR/grid interconnection power flows and DR generation control,

·        
With constraints/concerns: Equipment compatibility

.

· Continuous monitoring (mini SCADA)

· Periodic monitoring (download information periodically)

### 1.2.3                   Local Power System with DR Interconnects with Utility Power System

The purpose of LOCAL POWER SYSTEM WITH DR INTERCONNECTS
WITH UTILITY POWER SYSTEM function is to

·        
Provide/receive reactive power support

·        
Provide reactive power coordination

·        
Provide synchronizing control

·        
Implement voltage regulation

·        
Implement anti islanding protection

·        
Monitor power flow

·        
Coordinate protective functions

directly involving DR Owner/ Operator DisCo RTO,
performing DR/Grid Interface control and monitoring, with key interfaces:
between DR system operator / DisCo / RTO,

This function has the following key requirements:

·        
With communication configuration requirements of LAN within DR,
WAN for communication between DR and Disco and DR and RTO,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High to assure reliable DR/grid
interconnection,

·        
With data management requirements of Moderate – mainly associated
with the monitoring of the DR/grid interconnection,

·        
With constraints/concerns: Synchronization issues if DR/grid
interconnection opens to grid.

### 1.2.4                   DisCo’s SCADA System Monitors DR Devices

The purpose of DISCO’S SCADA SYSTEM MONITORS DR DEVICES
function is to Monitor DR device status, Alarm processing, Data logging, Power
flow forecasting, Monitor DR/grid interactions, Supervise generation, Perform
data validation, Perform data acquisition, and Handle communication failures

directly involving DisCo

·        
DR Operator

·        
TransCo

·        
RTO

performing Monitor and control functions to maximize
asset utilization, with key interfaces: between DR and DisCo SCADA

·        
DisCo SCADA and RTO

This function has the following key requirements:

·        
With communication configuration requirements of Disco’s SCADA
system to RTO and DR owner/operator over WAN,

·        
With communication service quality requirements of High
availability, high data accuracy, frequent updates,

·        
With security requirements of High to assure maintain overall
system integrity,

·        
With data management requirements of Data exchange between
organizations,

·        
With constraints/concerns: No specific constraints.

### 1.2.5                   DR Protection Devices React to System Conditions

The purpose of DR PROTECTION DEVICES REACT TO SYSTEM
CONDITIONS function is to provide fault detection and protection coordination,
Provide system reliability, Prevent islanding condition, directly involving DR
devices, DR operator, DisCo, RTO, performing System protection by implementing
protective functions, with key interfaces: between DR operator and individual DR
devices, DR operator and DisCo, Event recorders and DR archival center.

This function has the following key requirements:

·        
With communication configuration requirements of Interface between
protection equipment and DR control center and data archival facilities,

·        
With communication service quality requirements of High
availability, high accuracy,

·        
With security requirements of High, to assure reliable overall
system operation,

·        
With data management requirements of Infrequent data transfers,
Accurate data processing,

·        
With constraints/concerns: Failure to operate properly may lead to
equipment damage, with subsequent loss of revenue and system availability.

–       
Direct Transfer Tripping

–       
Disconnects local EPS from utility EPS without turning off DR –
intentional islanding

### 1.2.6                   DisCo Manages Microgrid with DR

The purpose of DISCO MANAGES MICROGRID WITH DR function
is to Optimize asset utilization, Monitor DR/grid interaction, Manage DR power
import/export, Provide voltage regulation, Manage DR dispatch, Allow for
seamless DR/grid resynchronization, Implement black start, Monitor power
quality, Power and ancillary services, Manage restoration protocol, Provide
supervisory control on power interchange, Schedule transmission, Monitor
reserves, Forecast and schedule resources, Schedule generation dispatch,
Reconfigure system, directly involving DisCo, GenCo, TransCo, RTO, ISO,
performing Overall system management including resource allocation and power
system analysis. with key interfaces: between DisCo SCADA system/control center
and other SCADA systems (GenCo, TransCo, RTO, ISO),

This function has the following key requirements:

·        
With communication configuration requirements of WAN - Requires
interconnection between microgrid control center and other control centers,

·        
With communication service quality requirements of High
availability, high volume, frequent updates,

·        
With security requirements of High to assure reliable overall
system operation,

·        
With data management requirements of Frequent data transfers,
frequent data logging,

·        
With constraints/concerns:

–       
DR/grid synchronization issues and effective handling of fault-on and
post-fault system conditions.

–       
Communication and coordinated control of microgrid components.

### 1.2.7                   All Systems Log Significant Events and Store Statistically Important Data

The purpose of ALL SYSTEMS LOG SIGNIFICANT EVENTS AND
STORE STATISTICALLY IMPORTANT DATA function is to

·        
Provide GPS time-stamped records of events

·        
Provide record of system variables

·        
Provide record of system settings

·        
Provide record of system topology

·        
Allow for data access to different organizations

·        
Message processing and management

·        
Data maintenance

directly involving DR owner/operator, DisCo, RTO,
performing Archival functions and data maintenance, with key interfaces: between

·        
DR archival center/data base and DR owner/operator

·        
 DR archival center/data base and DisCo

·        
 DR archival center / data base and RTO

This function has the following key requirements:

·        
With communication configuration requirements of Requires
communication between archival center and other control centers over WAN. DR
local data acquisition/processing over LAN,

·        
With communication service quality requirements of High
availability, fast accessibility, medium volume, frequent updates,

·        
With security requirements of High, to assure access to critical
data,

·        
With data management requirements of

–       
May require multiple data bases

–       
May require the storage of large amounts of data

·        
With constraints/concerns: Data storage software obsolescence and
resultant loss of data accessibility.

## 1.3           Advanced Distribution Automation (ADA) with DR Installed on Distribution System

### 1.3.1                   ADA System Updates Power System Model and Analyzes Distribution Operations

The purpose of ADA SYSTEM UPDATES POWER SYSTEM MODEL AND
ANALYZE DISTRIBUTION OPERATIONS function is to maintain the complete power
system model to assure that the automation system uses the appropriate system
parameters during operation, directly involving

·        
DR Operator/Owner

·        
DisCo Operator/Owner

·        
RTO/ISO, performing

·        
Topology maintenance

·        
Load model maintenance

·        
GIS maintenance

·        
Distribution sub model maintenance, with key interfaces: between

·        
DR owner/operator and DisCo

·        
DisCo and RTO/ISO

·        
DR owner/operator and RTO/ISO

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to RTO/ISO and LAN for internal DisCo communication. DR
owner/operator will communicate via WAN with all interfaces.

·        
With communication service quality requirements of power system
model update requires medium availability. Real-time operational conditions
require high availability, high volume, and frequent updates.

·        
With security requirements of  DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of model maintenance will
require update of many legacy and non-legacy data sources. Real-time DA data
will generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval.
Connection to legacy systems data and data structure incompatibility issues.

–       
Update topology model

–       
Update facilities model

–       
Update load model

–       
Update vicinity model

–       
Analyze real-time operation conditions using distribution power flow

### 1.3.2                   ADA System Performs Fault Location, Fault Isolation, and Power Restoration

The purpose of ADA SYSTEM PERFORMS FAULT LOCATION, FAULT
ISOLATION, AND POWER RESTORATION function is to identify distribution system
fault conditions and automatically restore power, directly involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, identify location of system fault and automatically take action to restore
power. DA may instruct DR device to disconnect or operate in isolation depending
on system conditions. with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner. LAN communication within DisCo to
coordinate power restoration.

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval
and data transfer speed. System must act very quickly against real-time data.

### 1.3.3                   Operators Restore Power Manually

The purpose of OPERATORS RESTORE POWER MANUALLY function
is to identify distribution system fault conditions and manually restore power,
directly involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, identify location of system fault and take action to restore power.
Operator may instruct DR device to disconnect or operate in isolation depending
on system conditions. with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner. LAN communication within DisCo to
coordinate power restoration.

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Fast, Manual retrieval of system data
to make appropriate decisions.

### 1.3.4                   ADA System Restores Power Using Automation

The purpose of ADA SYSTEM RESTORES POWER USING AUTOMATION
function is to Identify distribution system fault conditions and automatically
restore power, directly involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, take action to restore power. DA may instruct DR device to disconnect or
operate in isolation depending on system conditions. with key interfaces:
between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner. LAN communication within DisCo to
coordinate power restoration.

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval
and data transfer speed. System must act very quickly against real-time data..

### 1.3.5                   ADA System Reconfigures Feeders to Meet Differing Requirements

The purpose of ADA SYSTEM RECONFIGURES FEEDERS TO MEET
DIFFERING REQUIREMENTS function is to identify system conditions and reconfigure
distribution system optimally for the given the system conditions, directly
involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, identify alternative feeder configurations to optimally serve current and
forecasted load. with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner. LAN communication within DisCo to
coordinate system configuration.

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Fast retrieval of system data to make
appropriate decisions..

### 1.3.6                   ADA System Controls Volt/Var to Meet Criteria Optimally

The purpose of ADA SYSTEM CONTROLS VOLT/VAR TO MEET
CRITERIA OPTIMALLY function is to identify system conditions and reconfigure
distribution system optimally for the given the system conditions, directly
involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, identify alternative feeder configurations to optimally serve current and
forecasted load. with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner. LAN communication within DisCo to
coordinate system configuration.

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Fast retrieval of system data to make
appropriate decisions..

### 1.3.7                   ADA System Analyzes Planned Outage Requests

The purpose of ADA SYSTEM ANALYZES PLANNED OUTAGE
REQUESTS function is to identify the planned outages on the distribution system
and connected DR devices that are critical in serving loads, directly involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner,

performing Outage requests analysis initiated by the
DisCo and DR owner/operators, with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner. LAN communication between DisCo
Operations,

·        
With communication service quality requirements of Medium
availability and medium accessibility. Data will be filtered by Disco into the
DA system for analysis.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of DA outage data will generally
be stored in commercial data sources,

·        
With constraints/concerns: Integration of legacy outage data into
DA outage analysis software.

### 1.3.8                   ADA System Creates and Performs Switching Orders

The purpose of ADA SYSTEM CREATES AND PERFORMS SWITCHING
ORDERS function is to analyze system conditions and identify optimal switching
sequences, directly involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, identify optimal switching orders. with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner and LAN communication within DisCo,

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Fast retrieval and analysis of system
data to make appropriate decisions..

### 1.3.9                   ADA System Creates Islands Intentionally

The purpose of ADA SYSTEM CREATES ISLANDS INTENTIONALLY
function is to analyze system conditions and identify optimal switching
sequences to island the DR device, directly involving

·        
DR Owner/Operator

·        
DisCo Operator/Owner, performing

Using power system model information and real-time system
data, identify optimal switching orders. with key interfaces: between

·        
DR owner/operator and DisCo

·        
Internal DisCo Operations,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner, and LAN communication within DisCo,

·        
With communication service quality requirements of High
availability and fast accessibility.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Real-time DA data will
generally be stored in commercial data sources,

·        
With constraints/concerns: Fast retrieval and analysis of system
data to make appropriate decisions..

## 1.4           Post Operations

### 1.4.1                   Meter Data Management Agents (MDMAs) Retrieve DR Meter Data

The purpose of METER DATA MANAGEMENT AGENTS (MDMAS)
RETRIEVE DR METER DATA function is to Manage meter readings and usage profile,
Provide the means for sharing meter data, Maintain equipment, directly involving
DR owner/operator, DisCo, ESP, Customers, performing Data management functions
Data verification, with key interfaces: between

·        
ESP and DR operator

·        
ESP and recording equipment

This function has the following key requirements:

·        
With communication configuration requirements of Automatic reading
from remote sensors, "on-demand" readings from remote sensors over WAN,

·        
With communication service quality requirements of High
availability, fast accessibility, frequent updates,

·        
With security requirements of High security to prevent
unauthorized access to data,

·        
With data management requirements of Data base for fast data
storage and retrieval,

·        
With constraints/concerns: Communication equipment compatibility,
equipment obsolescence, Reliability under severe weather conditions.

### 1.4.2                   Statistical Data on Operational Conditions are Collected and Calculated

The purpose of STATISTICAL DATA ON OPERATIONAL CONDITIONS
ARE COLLECTED AND CALCULATED function is to Infer statistically significant
information such as end-user's load demand profile, directly involving DR
owner/operator, DisCo, ESP, Customers, performing Statistical computations, data
analyses, data collection, data verification, with key interfaces: between

·        
ESP and DR operator

·        
ESP and recording equipment

This function has the following key requirements:

·        
With communication configuration requirements of Automatic reading
from remote sensors, "on-demand" readings from remote sensors over WAN,

·        
With communication service quality requirements of High
availability, fast accessibility, frequent updates,

·        
With security requirements of High security to prevent
unauthorized access to data,

·        
With data management requirements of Data base for fast data
storage and retrieval,

·        
With constraints/concerns: Communication equipment compatibility,
equipment obsolescence, Reliability under severe weather conditions.

### 1.4.3                   Systems Create Reports

The purpose of SYSTEMS CREATE REPORTS function is to
Compile and generate reports, directly involving

·        
ESP and DR owner/operator

·        
ESP and DisCo

·        
ESP and Energy Service Provider

·        
ESP and end user, performing Data search and retrieval Data
compilation,

with key interfaces: between

·        
ESP and DR owner/operator

·        
ESP and DisCo

·        
ESP and end user

·        
ESP and GenCo,

This function has the following key requirements:

·        
With communication configuration requirements of Internet, phone,
dedicated communication channels,

·        
With communication service quality requirements of High
availability, fast accessibility, frequent updates,

·        
With security requirements of High security to prevent
unauthorized access to data,

·        
With data management requirements of Data base for fast data
retrieval,

·        
With constraints/concerns: Communication equipment compatibility,
equipment obsolescence, Reliability under severe weather conditions.

### 1.4.4                   Environmental System Collect Environmental and Pollution Statistics

The purpose of ENVIRONMENTAL SYSTEM COLLECT ENVIRONMENTAL
AND POLLUTION STATISTICS function is to Collect data that might have an adverse
impact on the environment, directly involving DR operator, performing Data
collection, with key interfaces: between DR operator / RTO /DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of DR operator and
data recording equipment,

·        
With communication service quality requirements of High
availability, moderate access rate,

·        
With security requirements of High security to prevent
unauthorized access to data,

·        
With data management requirements of Requires data base for
storage and retrieval of data.

## 1.5           DR Equipment Maintenance

### 1.5.1                   DR maintenance staff collect statistics on DR operations and all operating conditions

The purpose of DR MAINTENANCE STAFF COLLECT STATISTICS ON
DR OPERATIONS AND ALL OPERATING CONDITIONS function is to 1) Plan the
performance and down times of the DR's, and 2) Identify times during a period to
get optimal value of operating cost. directly involving DR Owner/Operator, RTO/
ISO, performing Optimization of operating cost and efficiency. with key
interfaces: between

·        
DR owner/operator and DisCo

·        
DisCo and RTO/ISO

·        
DR owner/operator and RTO/ISO,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner.

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of model maintenance will
require update of many legacy and non-legacy data sources. Real-time DA data
will generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval.
Connection to legacy systems data and data structure incompatibility issues.

### 1.5.2                   DR Maintenance Staff Maintain DR Equipment

The purpose of DR MAINTENANCE STAFF MAINTAIN DR EQUIPMENT
function is to 1. Reduce the number of un-scheduled outages, directly involving
DR Owner/Operator, performing Routine Maintenance, with key interfaces: between

·        
DR owner/operator and DisCo

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner.

·        
With communication service quality requirements of Medium
availability, medium volume.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements: May require multiple data bases
and may require the storage of large amounts of data

·        
With constraints/concerns: Data storage software obsolescence and
resultant loss of data accessibility.

### 1.5.3                   DR Maintenance Staff Test DR Equipment

The purpose of DR MAINTENANCE STAFF TEST DR EQUIPMENT
function is to 1. Validate ratings, capacity 2. Interconnecting infrastructure
to allow the DR's to participate in the market operations, directly involving DR
Owner/Operator, performing Equipment testing, with key interfaces: between

·        
DR owner/operator and DisCo

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner.

·        
With communication service quality requirements of Medium
availability, medium volume.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements: May require multiple data bases
and may require the storage of large amounts of data

·        
With constraints/concerns: Data storage software obsolescence and
resultant loss of data accessibility.

### 1.5.4                   RTO/ISO/DisCo SCADA System Monitors DR

The purpose of RTO/ISO/DISCO SCADA SYSTEM MONITORS DR
function is to Supervise DR generation, Control DR generation, Perform data
transfers, Monitor power flow, directly involving DR operator, DisCo, RTO,
performing Overall DR system supervision, Data acquisition, Data logging,
Control functions, Alarm processing

with key interfaces: between DR system operator and DisCo
DR system operator and RTO,

This function has the following key requirements:

·        
With communication configuration requirements of Disco’s SCADA
system to GenCos, RTO over WAN,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High, to assure reliable DR/grid
interconnection,

·        
With data management requirements of Moderate – mainly associated
with the monitoring of the DR/grid interconnection power flows and DR generation
control,

·        
With constraints/concerns: Synchronization issues if DR/grid
interconnection opens to grid and power flow reversal

## 1.6           Market Operations

### 1.6.1                   DR Owners Analyze Operational Conditions

The purpose of DR OWNERS ANALYZE OPERATIONAL CONDITIONS:
(e.g. load forecasts, weather conditions, energy prices, DR maintenance
requirements, DR capabilities and capacity, etc.) function is to evaluate energy
capture (wind systems) and availability, maximize productivity and anticipate
revenue potential from the resource, directly involving owners, operators,
SCADA, digital control systems, analog sensors, actuators and other automatic
and/or remote systems, performing monitoring of system performance and
measurement and collection of real-time data, with key interfaces: between
operators and SCADA and/or energy management systems,

This function has the following key requirements:

·        
With communication configuration requirements of "one-to-many",
SCADA systems, field devices,

·        
With communication service quality requirements of protected
electronics, well-maintained mechanical control systems, high availability,
rapid response, high data accuracy and throughput,

·        
With security requirements of information integrity,

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security, back-up power to
control systems.

### 1.6.2                   DR Owners Enter into Bilateral Energy Contracts with Other Market Participants

The purpose of DR OWNERS ENTER INTO BILATERAL ENERGY
CONTRACTS WITH OTHER MARKET PARTICIPANTS function is to establish bilateral
contracts ("long-term" or hourly) between generation and loads to negotiate the
price of energy, to agree on congestion rents between points-of-delivery and
points-of-receipt and to schedule transmission services, directly involving
market participants (generators, ancillary service providers, demand-side
resources, power exchanges, energy traders, load serving entities, energy
service companies, municipalities, cooperatives, industrials, commercials,
marketers, transmission rights traders, transmission owners, public interest
groups, distribution companies, regulators, auditors), performing financial
contracts for energy between market participants, with key interfaces: between
market participants,

This function has the following key requirements:

·        
With communication configuration requirements of internet,
telephone, satellite, radio, fax, e-mail, and other interfaces,

·        
With communication service quality requirements of high
availability, rapid response, high data accuracy and throughput for negotiating
energy contracts,

·        
With security requirements of high security (encryption, virus
protection, physical device protection, etc.),

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

### 1.6.3                   DR Owners Submit Day-Ahead Energy Schedules to RTO/ISO/DisCo

The purpose of DR OWNERS SUBMIT DAY-AHEAD ENERGY
SCHEDULES TO RTO/ISO/DISCO function is to provide settlement data [min. run
time, min. down time, daily availability, start-up notification time, start-up
cost curves, min. generation value ($/hr), incremental operating costs ($),
operating limits, unit status (fixed, on-dispatch, on-control)] for determining
LBMP for transmission pricing for the next day (24 hrs) so that market
participants may lock in their day-ahead buy-sell prices and avoid real-time
volatility, directly involving market participants (generators, ancillary
service providers, demand-side resources, power exchanges, energy traders, load
serving entities, energy service companies, municipalities, cooperatives,
industrials, commercials, marketers, transmission rights traders, transmission
owners, public interest groups, distribution companies, regulators, auditors),
performing accessing market information system(s) and supplying data, with key
interfaces: between system operator and market participants,

This function has the following key requirements:

·        
With communication configuration requirements of web-based market
information system(s), "Open Access Same-time Information System (OASIS",

·        
With communication service quality requirements of high
availability, rapid response, high data accuracy and throughput,

·        
With security requirements of high security (encryption, virus
protection, physical device protection, etc.),

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

### 1.6.4                   DR Owners Submit Day-Ahead Bids for Ancillary Services: Reserve, Regulation, Frequency Response, etc.

The purpose of DR OWNERS SUBMIT DAY-AHEAD BIDS FOR
ANCILLARY SERVICES: RESERVE, REGULATION, FREQUENCY RESPONSE, ETC. function is to
provide voltage support, system regulation (balance), reliable operation and to
lock in day-ahead buy-sell prices and avoid real-time volatility, directly
involving generation owners, transmission owners and system operator (and
control centers), performing accessing market information system(s) and
supplying data, with key interfaces: between system operator and market
participants,

This function has the following key requirements:

·        
With communication configuration requirements of web-based market
information system(s), "Open Access Same-time Information System (OASIS",

·        
With communication service quality requirements of high
availability, rapid response, high data accuracy and throughput,

·        
With security requirements of high security (encryption, virus
protection, physical device protection, etc.),

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

### 1.6.5                   DR Owners Submit Adjustments to Real-time Energy Schedules

The purpose of DR OWNERS SUBMIT ADJUSTMENTS TO REAL-TIME
ENERGY SCHEDULES function is to account for "current-day" changes and enable
real-time security constrained dispatch based on bid energy costs and improved
tracking of system security, directly involving generation owners, transmission
owners and system operator (and control centers), performing accessing market
information system(s) and supplying data, with key interfaces: between system
operator and market participants,

This function has the following key requirements:

·        
With communication configuration requirements of web-based market
information system(s), "Open Access Same-time Information System (OASIS",

·        
With communication service quality requirements of high
availability, rapid response, high data accuracy and throughput,

·        
With security requirements of high security (encryption, virus
protection, physical device protection, etc.),

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

### 1.6.6                   DR Owners Submit Real-time Bids for Ancillary Services

The purpose of DR OWNERS SUBMIT REAL-TIME BIDS FOR
ANCILLARY SERVICES function is to provide voltage support, system regulation
(balance), reliable operation, directly involving generation owners,
transmission owners and system operator (and control centers), performing
accessing market information system(s) and supplying data, with key interfaces:
between system operator and market participants,

This function has the following key requirements:

·        
With communication configuration requirements of web-based market
information system(s), "Open Access Same-time Information System (OASIS",

·        
With communication service quality requirements of high
availability, rapid response, high data accuracy and throughput,

·        
With security requirements of high security (encryption, virus
protection, physical device protection, etc.),

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

## 1.7           Wind-Related Issues/Functions/Applications

### 1.7.1                   Day Ahead Wind Prediction from Meteorological Sources

The purpose of DAY AHEAD WIND PREDICTION FROM
METEOROLOGICAL SOURCES function is to Plan wind turbine-generator output for the
Day Ahead Market, directly involving DR operator, DisCo, RTO, Meteorological
Services, performing System planning/operation to maximize asset utilization.
with key interfaces: between DR system operator and DisCo DR system operator and
RTO DR system operator and Meteorological Services,

This function has the following key requirements:

·        
With communication configuration requirements of Disco’s SCADA
system to GenCos, RTO over WAN, Meteorological Services over WWW or satellite
communications,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High, to assure confidential DR/grid
interconnection Low to Meteorological service,

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

### 1.7.2                   Real Time Wind Prediction from Meteorological Sources

The purpose of REAL TIME WIND PREDICTION FROM
METEOROLOGICAL SOURCES function is to Plan wind turbine-generator output for the
Hourly Market, directly involving DR operator, DisCo, RTO, Meteorological
Services, performing System planning/operation to maximize asset utilization.
with key interfaces: between DR system operator and DisCo DR system operator and
RTO DR system operator and Meteorological Services,

This function has the following key requirements:

·        
With communication configuration requirements of Disco’s SCADA
system to GenCos, RTO over WAN, Meteorological Services over WWW or satellite
communications,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High, to assure confidential DR/grid
interconnection Low to Meteorological service,

·        
With data management requirements of database systems requiring
timely access and frequent updates across organizational boundaries,

·        
With constraints/concerns: information security.

## 1.8           Dispersed Storage

### 1.8.1                   DR Owners Store Energy from the Power System

The purpose of DR OWNERS STORE ENERGY FROM THE POWER
SYSTEM function is to store energy when it is at its lowest cost and when it has
least possibility to be detrimental to the power system, directly involving DR
owners or aggregators and RTO/ISO/DisCo, performing capture (purchase) of
sufficient energy to meet projected demand at an appropriate time and economical
cost, with key interfaces: between DR owners or aggregators and RTO/ISO/DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of High
availability, medium speed in most cases although some may require high speed,

·        
With communication service quality requirements of High
reliability, Medium speed,

·        
With security requirements of Medium,

·        
With data management requirements of conventional demand interval
metering databases with real-time monitoring of available energy and projected
schedules,

·        
With constraints/concerns: ability to draw power without impacting
system performance. Automatic monitoring of electricity prices in unattended
installations (likely the norm)..

### 1.8.2                   DR Owners Discharge Stored Energy into the System

The purpose of DR OWNERS DISCHARGE STORED ENERGY INTO THE
SYSTEM function is to sell energy at a favorable price when capacity is needed
and to provide T&D grid support, directly involving DR owners or aggregators and
RTO/ISO/DisCo, performing managing real-time bids for energy and ancillary
services while meeting agreements regarding delivery of power to meet dispatched
demand and grid support requirements during emergency conditions, with key
interfaces: between DR owners or aggregators and RTO/ISO/DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of High
availability, medium speed in most cases although some may require high speed if
required to respond to sudden loss of capacity (some technologies can respond
within seconds),

·        
With communication service quality requirements of High
reliability, Medium speed,

·        
With security requirements of Medium,

·        
With data management requirements of conventional demand interval
metering databases with real-time monitoring of available energy remaining,

·        
With constraints/concerns: limited storage resource.

### 1.8.3                   RTO/ISO/DisCo Dispatches Storage to Meet Power Demand

The purpose of RTO/ISO/DISCO DISPATCHES STORAGE TO MEET
POWER DEMAND function is to reclaim stored energy to meet local or regional
power demand with competitively-priced energy and to support the distribution or
transmission system, directly involving DR owners or aggregators and
RTO/ISO/DisCo, performing determination of the need for additional power to meet
demand and monitoring ability of storage to make up projected deficits, with key
interfaces: between DR owners or aggregators and RTO/ISO/DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of High
availability, medium speed to DisCo control center,

·        
With communication service quality requirements of High
reliability, Medium speed,

·        
With security requirements of Medium,

·        
With data management requirements of conventional demand interval
metering databases with real-time monitoring of available energy and energy
remaining,

·        
With constraints/concerns: limited storage resource.

### 1.8.4                   RTO/ISO/DisCo Dispatches Storage to Support Intentional Islanding

The purpose of RTO/ISO/DISCO DISPATCHES STORAGE TO
SUPPORT INTENTIONAL ISLANDING function is to utilize stored energy in
combination with other DR to supply power to a group of end users separated from
bulk power supply (either intentionally as in the case of microgrids or
unintentionally due to equipment outage), directly involving DR owners or
aggregators and RTO/ISO/DisCo, DisCo operations, performing control of
restoration of the system to exploit the capability of storage to temporarily
supply an isolated part of the system, with key interfaces: between

      - DR owners or aggregators and RTO/ISO/DisCo

      - DR owners and DisCo operations,

This function has the following key requirements:

·        
With communication configuration requirements of High
availability, medium speed to DisCo control center with connections to other DR
for real-time control functions,

·        
With communication service quality requirements of High
reliability, Medium speed,

·        
With security requirements of Medium,

·        
With data management requirements of conventional demand interval
metering databases with real-time monitoring of available energy and energy
remaining,

·        
With constraints/concerns: limited storage resource and ability to
support an island, which may require that some other form of DR also be
operating.

### 1.8.5                   DR Owners Provide Fast Voltage Sag Correction

The purpose of DR OWNERS PROVIDE FAST VOLTAGE SAG
CORRECTION function is to utilize the stored energy to support the system
voltage during short to medium duration disturbances to enable critical
customers to continue operations. directly involving DR owners, DisCo,
Customers, performing ancillary support and energy supply functions, with key
interfaces: between DR owner and DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of telecom or
internet connection to transfer power quality monitor data post-event,

·        
With communication service quality requirements of Medium
availability and speed (not critical to operation, but desirable in a prompt
fashion),

·        
With security requirements of Medium, although many DisCos will
want to treat their power quality data as highly confidential. Performance base
rate information may eventually become public,

·        
With data management requirements of a power quality database
capable of storing various types of data and more conventional energy metering
database. Updating is infrequent, but can be voluminous after an event,
depending on contractual arrangement of performance-based rates,

·        
With constraints/concerns: many different types of power quality
monitors with diverse data representations and transfer capabilities.

## 1.9           Non-grid Connected Generation: Monitoring for Safety

### 1.9.1                   DR Owners Collect DR Operational Information

The purpose of DR OWNERS COLLECT DR OPERATIONAL
INFORMATION function is to follow normal daily load changes

·        
Analyze load requirements

·        
Forecast load requirements

·        
Provide means for supplying replacement power following loss of
generation

·        
Optimize system operation

directly involving

·        
DR Operator/Owner

·        
DisCo Operator/Owner, performing

·        
System operation to maximize asset utilization

·        
Routine maintenance activities

·        
Control functions for meeting load demand

·        
Monitoring operation of DR device, with key interfaces: between

·        
DR Owner/Operator and DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of WAN
communications with DisCo and LAN communication internal to DR owner/operator,

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of High to allow for continuous
operation of local system,

·        
With data management requirements of Moderate – mainly associated
with the operation of the local system and associated data recording and
transferring functions.

·        
With constraints/concerns: Synchronization issues if local system
is to be connected to grid.

## 1.10      DSM (Demand Side Management)

The purpose of (DEMAND SIDE MANAGEMENT) function is to 1.
Optimize asset utilization by pricing Industrial loads higher than normal during
peak hours in order to compensate for more expensive generation utilized at
those times.

2. Regulating consumer and industrial loads in greater
constrained regions to be able to transfer power more efficiently. directly
involving DR operator, DisCo, RTO, Special Customers, performing Optimization of
operating cost and efficiency. with key interfaces: between

·        
DR owner/operator and DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner.

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Model maintenance will
require update of many legacy and non-legacy data sources. Real-time DA data
will generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval.
Connection to legacy systems data and data structure incompatibility issues.

### 1.10.1               DR Owner Initiated DSM

The purpose of OWNER INITIATED function is to 1. Optimize
asset utilization by pricing Industrial loads higher than normal during peak
hours in order to compensate for more expensive generation utilized at those
times.

2. Regulating consumer and industrial loads in greater
constrained regions to be able to transfer power more efficiently. directly
involving DR operator, DisCo, RTO, Special Customers, performing Optimization of
operating cost and efficiency. DR owner may choose to purchase versus produce
power based upon cost analysis. with key interfaces: between

·        
DR owner/operator and DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner.

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Model maintenance will
require update of many legacy and non-legacy data sources. Real-time DA data
will generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval.
Connection to legacy systems data and data structure incompatibility issues.

### 1.10.2               Utility Initiated DSM

The purpose of LITY INITIATED function is to 1. Optimize
asset utilization by pricing Industrial loads higher than normal during peak
hours in order to compensate for more expensive generation utilized at those
times.

2. Regulating consumer and industrial loads in greater
constrained regions to be able to transfer power more efficiently. directly
involving DR operator, DisCo, RTO, Special Customers, performing Optimization of
operating cost and efficiency. Utility initiates DSM based upon real time
conditions to support load and/or ancillary services, with key interfaces:
between

·        
DR owner/operator and DisCo,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from DisCo to DR/Owner.

·        
With communication service quality requirements of High
availability, medium volume, frequent updates,

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Model maintenance will
require update of many legacy and non-legacy data sources. Real-time DA data
will generally be stored in commercial data sources,

·        
With constraints/concerns: Real-time data storage and retrieval.
Connection to legacy systems data and data structure incompatibility issues.

## 1.11      Residential Generation Devices

The purpose of RESIDENTIAL GENERATION DEVICES function is
to provide electrical power to residence while remaining in parallel with ESP,
directly involving Residential DR owner/operator, ESP, performing

·        
System operation to maximize asset utilization

·        
Routine maintenance activities

·        
Control functions for meeting load demand

·        
Monitoring operation of DR device,

with key interfaces: between

·        
DR owner/operator and ESP,

This function has the following key requirements:

·        
With communication configuration requirements of WAN for
communication from ESP to DR/Owner.

·        
With communication service quality requirements of High
availability, medium volume, frequent updates. On/off control by ESP.

·        
With security requirements of DA critical data requires very high
security. Breach of DA system can result in severe disruption,

·        
With data management requirements of Moderate – mainly associated
with the operation of the local system and associated data recording and
transferring functions.

·        
With constraints/concerns: Real-time data storage and retrieval.
Connection to legacy systems data and data structure incompatibility issues.
