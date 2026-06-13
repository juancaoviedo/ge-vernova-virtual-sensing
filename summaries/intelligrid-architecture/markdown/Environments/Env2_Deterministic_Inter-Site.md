# Env2 High Speed Inter-Subst

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Environments/Env2_Deterministic_Inter-Site.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Deterministic Rapid Response Inter-Site Environment - #2

if !vml?![](Env2_Deterministic_Inter-Site_files/image002.gif)endif?The
Deterministic Rapid Response Inter-Site environment represents a set
of requirements primarily concerned with the system-wide stability and
reliability of the power grid.   When implemented on general networks
rather than dedicated lines, it is even newer than its
Intra-Substation counterpart, with only a few pilot projects currently
underway.

**Typical Applications:** Sending
protection, samples, phasor measurements, and process control
information between sites in real-time enables applications that can
coordinate functions at a grid level and anticipate problems rather
than just reacting to them.  The simplest use of this environment may
be transmission line protection, while more complex applications might
involve real-time contingency analysis. These applications may be
coordinated between field equipment, between multiple substations, or
between substations and other sites such as control centers.

**Characteristics, and Similar Environments:**The Deterministic Rapid Response Inter-Site environment has higher
security requirements and lower timing requirements than Deterministic
Rapid Response Intra-Substation.  However, violations of its timing
requirements might still cause equipment damage, safety concerns, or
network instability issues. Volumes of this type of data exchange are
small so far but have the potential to be enormous if the quest for
grid stability causes data to be directly measured that previously was
only estimated.  This could make data management concerns for this
environment much greater than its Intra-Substation counterpart.

**Definition:**  This environment is defined
by the following requirements:

---

# Communication and Information Requirements that Define this Environment

## Configuration Requirements

* Support interactions across widely distributed sites

## Quality of Service Requirements

* Provide ultra high speed messaging (short latency) of less than 4 milliseconds
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
- [IEC61850 Parts 7-3 and 7-4 - Substation Object Modeling](../New_Technologies/Tech_IEC61850_Parts_7-3_and_7-4_-_Substation_Object_Modeling.htm)
  - Quality of Service, Data Management
- [IEC61850 Power Quality Object Models](../New_Technologies/Tech_IEC61850_Power_Quality_Object_Models.htm)
  - Quality of Service, Data Management
- [IEEE C37.94 - Standard for N x 64 kbps Optical Fiber Interfaces between](../New_Technologies/Tech_IEEE_C37_94_-_Standard_for_N_x_64_kbps_Optical_Fiber_Interfa.htm) 
  - Quality of Service,

## Communications Industry Technologies

### Link Layer and Physical Technologies

- [Ethernet](../New_Technologies/Tech_Ethernet.htm)
  - Quality of Service,
- [Bridges/Switches](../New_Technologies/Tech_Bridges-Switches.htm)
  - Configuration,
- [Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH)](../New_Technologies/Tech_Synchronous_Optical_Network_(SONET)_and_Synchronous_Digital_.htm)
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
  - Data Management

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

---

# Alternative Technologies

### Link Layer and Physical Technologies

- [Digital Signal (DSx), Time-division multiplexing, the T-carriers, T1, fractional T1](../New_Technologies/Tech_Digital_Signal_(DSx),_Time-division_multiplexing,_the_T-carr.htm)
  - Configuration,
- [Frame Relay](../New_Technologies/Tech_Frame_Relay.htm)
  - Configuration,

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

- [Alternate Communication Channels](../New_Technologies/Tech_Alternate_Communication_Channels.htm)
  - Configuration,
- [Backup Data Sources](../New_Technologies/Tech_Backup_Data_Sources.htm)
  - Configuration,

## 

## 

### IETF Internet Requests for Comments (RFCs) on Security Technologies

- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
  - Quality of Service,

## 

## 

## 

## 

## 

## 

## 

## 

## 

## 

##
