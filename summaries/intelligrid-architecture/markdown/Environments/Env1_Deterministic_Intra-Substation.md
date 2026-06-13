# Env1 High Speed Intra-Subst

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Environments/Env1_Deterministic_Intra-Substation.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Deterministic Rapid Response Intra-Substation Environment - #1

if !vml?![](Env1_Deterministic_Intra-Substation_files/image001.gif)endif?The
two Deterministic Rapid Response environments carry data exchanges
that were previously considered too fast, too high volume, or too
deterministic to carry on a generalized network.  These data exchanges
traditionally took place either within a single device or on dedicated
lines.

**Typical
applications:** Advances in technology have now made it possible to
exchange data over LANs and WANs:

·        
Between protective relays to coordinate protection
schemes

·        
Between those devices sampling measurements  (e.g. smart
current or voltage transformers) and those processing the data

·        
Between multiple devices that are distributing other
real-time processes that previously took place on a single device,
e.g. process control.  Another name that has been used for
Deterministic Rapid Response Intra-Substation is “process bus”.

**Characteristics:** The Deterministic Rapid
Response environments require extremely high speed, high volume, or
both, with timing requirements measured in milliseconds or lower. 
Violation of these requirements might cause equipment damage or safety
issues.

**Similar Environments:** The Deterministic
Rapid Response Intra-Substation environment is limited within the
physical boundaries of the substation.  Its security requirements can
therefore be somewhat lower, and its timing requirements somewhat
stricter, than Deterministic Rapid Response Inter-Site.  Data
management is not a major concern because of its limited scope.

**Definition:**  This environment is defined
by the following requirements:

---

# Communication and Information Requirements that Define this Environment

## Configuration Requirements

* Provide point-to-point interactions between two entities
* Support interactions within a contained environment (e.g. substation or control center)

## Quality of Service Requirements

* Provide ultra high speed messaging (short latency) of less than 4 milliseconds
* Support extremely high availability of information flows of 99.999+ (~5 minutes)
* Support high precision of data (< 0.5 variance)
* Support time synchronization of data for age and time-skew information

## Security Requirements

* Provide Authorization Service for Access Control (resolving a policy-based access control decision to ensure authorized entities have appropriate access rights and authorized access is not denied)
* Provide Security Policy Service (concerned with the management of security policies)

## Data Management Requirements

* Support keeping data consistent and synchronized across systems and/or databases
* Support specific standardized or de facto object models of data

---

# Recommended Technologies

## Energy Industry-Specific Technologies

### Utility Field Device Related Data Exchange Technologies

- [IEC61850 Part 7-2 - GSE (GOOSE and GSSE](../New_Technologies/Tech_IEC61850_Part_7-2_-_GSE_(GOOSE_and_GSSE.htm)
  - Configuration, Quality of Service,
- [IEC61850 Part 7-2 - SMV (Sampled Measured Values)](../New_Technologies/Tech_IEC61850_Part_7-2_-_SMV_(Sampled_Measured_Values).htm)
  - Configuration,
- [IEC61850 Parts 7-3 and 7-4 - Substation Object Modeling](../New_Technologies/Tech_IEC61850_Parts_7-3_and_7-4_-_Substation_Object_Modeling.htm)
  - Quality of Service, Data Management
- [IEEE C37.94 - Standard for N x 64 kbps Optical Fiber Interfaces between](../New_Technologies/Tech_IEEE_C37_94_-_Standard_for_N_x_64_kbps_Optical_Fiber_Interfa.htm) 
  - Quality of Service,

## Communications Industry Technologies

### Link Layer and Physical Technologies

- [Ethernet](../New_Technologies/Tech_Ethernet.htm)
  - Quality of Service,
- [Bridges/Switches](../New_Technologies/Tech_Bridges-Switches.htm)
  - Configuration,
- [Asynchronous Transfer Mode (ATM)](../New_Technologies/Tech_Asynchronous_Transfer_Mode_(ATM).htm)
  - Configuration, Quality of Service,

### Wireless Technologies

- [Global Positioning System (GPS)](../New_Technologies/Tech_Global_Positioning_System_(GPS).htm)
  - Quality of Service, Data Management

## Security Technologies

### Policy and Framework Related Technologies

- [ISO/IEC 10164-8:1993 Security Audit Trail Function - Information technology - Open Systems Interconnection - Systems Management](../New_Technologies/Tech_ISO-IEC_10164-8_1993_Security_Audit_Trail_Function_-_Informa.htm)
  - Security,
- [ISO/IEC 10181-7:1996 Security Audit and Alarms Framework - Information technology - Open Systems Interconnection -- Security Frameworks for Open Systems](../New_Technologies/Tech_ISO-IEC_10181-7_1996_Security_Audit_and_Alarms_Framework_-_I.htm)
  - Security,
- [FIPS PUB 112 Password Usage](../New_Technologies/Tech_FIPS_PUB_112_Password_Usage.htm)
  - Security,

### General Security Technologies

- [Role-Based Access Control](../New_Technologies/Tech_Role-Based_Access_Control.htm)
  - Security,
- [Service Level Agreements (SLA)](../New_Technologies/Tech_Service_Level_Agreements_(SLA).htm)
  - Security,

### Application Layer Security Technologies

- [IEC 62351-6 Security for IEC 61850 GOOSE, GSSE, and SMV Profiles](../New_Technologies/Tech_IEC_62351-6_Security_for_IEC_61850_GOOSE,_GSSE,_and_SMV_Prof.htm)
  - Security,

## Network and Enterprise Management Technologies

### Network Management Technologies

- [IEC 62351-7 Objects for Network Management](../New_Technologies/Tech_IEC_62351-7_Objects_for_Network_Management.htm)
  - Quality of Service, Data Management

---

# Recommended Common Services

## Security Services

### Common Security Services

- [Authorization for Access Control](../New_Technologies/Tech_Authorization_for_Access_Control.htm)
  - Security,
- [Security Policies](../New_Technologies/Tech_Security_Policies.htm)
  - Security,

## Network and System Management Services

### Enterprise Management Services

- [System/Network Health-Check Analysis](../New_Technologies/Tech_System-Network_Health-Check_Analysis.htm)
  - Quality of Service,
- [System/Network Fault Diagnosis](../New_Technologies/Tech_System-Network_Fault_Diagnosis.htm)
  - Quality of Service,
- [System/Network Performance Analysis](../New_Technologies/Tech_System-Network_Performance_Analysis.htm)
  - Quality of Service,

## Data Management Common Services

### Data Management Common Services

- [Address and Naming Management](../New_Technologies/Tech_Address_and_Naming_Management.htm)
  - Data Management
- [Network Time](../New_Technologies/Tech_Network_Time.htm)
  - Data Management

## Common Platform Services

---

# Recommended Best Practices

## Data Management Best Practices

### Data Management

- [Alternate Communication Channels](../New_Technologies/Tech_Alternate_Communication_Channels.htm)
  - Quality of Service,
- [Backup Data Sources](../New_Technologies/Tech_Backup_Data_Sources.htm)
  - Quality of Service,
- [Object Modeling Techniques](../New_Technologies/Tech_Object_Modeling_Techniques.htm)
  - Data Management
- [Quality Flagging](../New_Technologies/Tech_Quality_Flagging.htm)
  - Quality of Service, Data Management
- [Time Stamping](../New_Technologies/Tech_Time_Stamping.htm)
  - Quality of Service, Data Management
- [Data Update Management](../New_Technologies/Tech_Data_Update_Management.htm)
  - Data Management
- [Management of Time-Sensitive Data Flows and Timely Access to Data by Multiple Different Users](../New_Technologies/Tech_Management_of_Time-Sensitive_Data_Flows_and_Timely_Access_to.htm)
  - Quality of Service, Data Management
- [Management of Data and Object Naming](../New_Technologies/Tech_Management_of_Data_and_Object_Naming.htm)
  - Data Management
- [Management of Data Formats in Data Exchanges](../New_Technologies/Tech_Management_of_Data_Formats_in_Data_Exchanges.htm)
  - Data Management
- [Management of Data Accuracy](../New_Technologies/Tech_Management_of_Data_Accuracy.htm)
  - Quality of Service,

## Security Best Practices

## Security Technology Documents

## 

## 

## 

## 

## 

## 

## 

## 

## 

---

# Alternative Best Practices

### Data Management

- [Data Backup and Logging](../New_Technologies/Tech_Data_Backup_and_Logging.htm)
  - Quality of Service,

## 

## 

### IETF Internet Requests for Comments (RFCs) on Security Technologies

- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
  - Quality of Service,

### Other Security Technolog

- [ANSI INCITS 359-2004 Role Based Access Control (RBAC)](../New_Technologies/Tech_ANSI_INCITS_359-2004_Role_Based_Access_Control_(RBAC).htm)
  - Security,
