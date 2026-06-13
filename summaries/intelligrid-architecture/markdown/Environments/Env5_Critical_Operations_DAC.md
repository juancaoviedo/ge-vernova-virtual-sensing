# Env5 Critical DAC

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Environments/Env5_Critical_Operations_DAC.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Critical Operations DAC and SCADA Environment - #5

if !vml?![](Env5_Critical_Operations_DAC_files/image002.gif)endif?

Critical Operations-related Data Acquisition
and Control is the environment most resembling what has been
traditionally called Supervisory Control and Data Acquisition
(SCADA).  It represents those messages between a substation and
control center that are critical to legal, safe, and reliable power
system operations.

**Typical applications**:  Include
monitoring and control of substations, pole-top devices, generation
plants or distributed energy resources.  These are the functions
performed by operators in the daily operation or emergency recovery of
the power system.

**Characteristics:**  It is vital that these
message exchanges not be tampered, monitored, or interfered with by
unauthorized persons.  Quality of service requirements are based
around human reaction times.  Configuration of the network changes
often, and may vary widely.  Could also include transfer of data that
is high-volume and critical, such as configuration files or fault
recordings.

**Similar Environments:** Critical
Operations Data Acquisition and Control is very similar to Critical
Operations Intra-Substation except that these exchanges take place
between control centers and field equipment, rather than between
substations.

---

# Communication and Information Requirements that Define this Environment

## Configuration Requirements

* Support interactions between a few "clients" and many "servers"
* Support interactions across widely distributed sites
* Support compute-constrained and/or media constrained communications

## Quality of Service Requirements

* Provide high speed messaging of less than 1 second
* Support high availability of information flows of 99.9+ (~9 hours)
* Support time synchronization of data for age and time-skew information

## Security Requirements

* Provide Authorization Service for Access Control (resolving a policy-based access control decision to ensure authorized entities have appropriate access rights and authorized access is not denied)
* Provide Information Integrity Service (data has not been subject to unauthorized changes or these unauthorized changes are detected)
* Provide Audit Service (responsible for producing records, which track security relevant events)
* Provide Credential Renewal Service (notify users prior to expiration of their credentials)
* Provide Security Policy Service (concerned with the management of security policies)
* Provide Single Sign-On Service (relieve an entity having successfully completed the act of authentication once from the need to participate in re-authentications upon subsequent accesses to managed resources for some reasonable period of time)
* Provide User Profile and User Management (combination of several other security services)
* Provide Security Discovery (the ability to determine what security services are available for use)

## Network and System Management Requirements

* Provide Network Management (management of media, transport, and communication nodes)
* Provide System Management (management of end devices and applications)

## Data Management Requirements

* Support the management of large volumes of data flows
* Support keeping the data up-to-date
* Support extensive data validation procedures
* Support timely access to data by multiple different users
* Support management of data whose types can vary significantly in different implementations
* Support specific standardized or de facto object models of data
* Provide discovery service (discovering available services and their characteristics)
* Provide conversion and protocol mapping

---

# Recommended Technologies

## Energy Industry-Specific Technologies

### Utility Field Device Related Data Exchange Technologies

- [ISO 9506 MMS - Manufacturing Messaging Specification](../New_Technologies/Tech_ISO_9506_MMS_-_Manufacturing_Messaging_Specification.htm)
  - Configuration, Quality of Service,
- [IEC61850 Part 7-2 - Abstract Common Services Interface (ACSI)](../New_Technologies/Tech_IEC61850_Part_7-2_-_Abstract_Common_Services_Interface_(ACSI.htm)
  - Configuration, Quality of Service, Data Management
- [IEC61850 Parts 7-3 and 7-4 - Substation Object Modeling](../New_Technologies/Tech_IEC61850_Parts_7-3_and_7-4_-_Substation_Object_Modeling.htm)
  - Network Management, Data Management
- [IEC61850 Part 6 - Substation Configuration Language](../New_Technologies/Tech_IEC61850_Part_6_-_Substation_Configuration_Language.htm)
  - Network Management, Data Management
- [IEC61850 Power Quality Object Models](../New_Technologies/Tech_IEC61850_Power_Quality_Object_Models.htm)
  - Data Management
- [IEC62350 - Object Models for Distributed Energy Resources (DER)](../New_Technologies/Tech_IEC62350_-_Object_Models_for_Distributed_Energy_Resources_(D.htm)
  - Network Management, Data Management
- [IEC62349 - Hydro Power Plant Object Models](../New_Technologies/Tech_IEC62349_-_Hydro_Power_Plant_Object_Models.htm)
  - Network Management, Data Management
- [IEC61400-25 for Wind Power Object Models](../New_Technologies/Tech_IEC61400-25_for_Wind_Power_Object_Models.htm)
  - Network Management, Data Management

### Utility Control Center Related Data Management Technologies

- [IEC 61970 Part 3 - Common Information Model (CIM)](../New_Technologies/Tech_IEC_61970_Part_3_-_Common_Information_Model_(CIM).htm)
  - Data Management
- [CIM Extensions for Market Operations](../New_Technologies/Tech_CIM_Extensions_for_Market_Operations.htm)
  - Data Management

## Communications Industry Technologies

### Access Technologies

- [Private Intranet](../New_Technologies/Tech_Private_Intranet.htm)
  - Configuration,

### Networking Technologies

- [Internet Protocol Version V4 (IPV4)](../New_Technologies/Tech_Internet_Protocol_Version_V4_(IPV4).htm)
  - Configuration,

### IP-based Transport Protocols

- [Transmission Control Protocol (TCP)](../New_Technologies/Tech_Transmission_Control_Protocol_(TCP).htm)
  - Configuration,

### Application Layer Protocols

- [SNTP (Network Time Protocol)](../New_Technologies/Tech_SNTP_(Network_Time_Protocol).htm)
  - Quality of Service, Data Management

### Link Layer and Physical Technologies

- [LAN/MAN Technologies](../New_Technologies/Tech_LAN-MAN_Technologies.htm)
  - Configuration,
- [IEEE 802 MAC Addresses](../New_Technologies/Tech_IEEE_802_MAC_Addresses.htm)
  - Configuration,
- [Ethernet](../New_Technologies/Tech_Ethernet.htm)
  - Configuration,
- [Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH)](../New_Technologies/Tech_Synchronous_Optical_Network_(SONET)_and_Synchronous_Digital_.htm)
  - Configuration,
- [Asynchronous Transfer Mode (ATM)](../New_Technologies/Tech_Asynchronous_Transfer_Mode_(ATM).htm)
  - Configuration,

### Wireless Technologies

- [Global Positioning System (GPS)](../New_Technologies/Tech_Global_Positioning_System_(GPS).htm)
  - Quality of Service,

### Computer Systems Related Technologies

- [Universal Description, Discovery, and Integration (UDDI)](../New_Technologies/Tech_Universal_Description,_Discovery,_and_Integration_(UDDI).htm)
  - Data Management
- [XML Protocol/Simple Object Access Protocol (SOAP)](../New_Technologies/Tech_XML_Protocol-Simple_Object_Access_Protocol_(SOAP).htm)
  - Data Management
- [IEEE 1588 Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems](../New_Technologies/Tech_IEEE_1588_Standard_for_a_Precision_Clock_Synchronization_Pro.htm)
  - Quality of Service,

### General Internet and De Facto Data Management Technologies

- [XML Schema (xls)](../New_Technologies/Tech_XML_Schema_(xls).htm)
  - Data Management

## Security Technologies

### Policy and Framework Related Technologies

- [ISO/IEC 10164-8:1993 Security Audit Trail Function - Information technology - Open Systems Interconnection - Systems Management](../New_Technologies/Tech_ISO-IEC_10164-8_1993_Security_Audit_Trail_Function_-_Informa.htm)
  - Security,
- [ISO/IEC 18014-1:2002 Time-Stamping Services - Information technology - Security Techniques - Part 1: Framework](../New_Technologies/Tech_ISO-IEC_18014-1_2002_Time-Stamping_Services_-_Information_te.htm)
  - Quality of Service, Security, Data Management
- [ISO/IEC 10181-7:1996 Security Audit and Alarms Framework - Information technology - Open Systems Interconnection -- Security Frameworks for Open Systems](../New_Technologies/Tech_ISO-IEC_10181-7_1996_Security_Audit_and_Alarms_Framework_-_I.htm)
  - Security,
- [FIPS PUB 112 Password Usage](../New_Technologies/Tech_FIPS_PUB_112_Password_Usage.htm)
  - Security,
- [FIPS PUB 113 Computer Data Authentication](../New_Technologies/Tech_FIPS_PUB_113_Computer_Data_Authentication.htm)
  - Security,
- [RFC 2196 Site Security Handbook](../New_Technologies/Tech_RFC_2196_Site_Security_Handbook.htm)
  - Security,
- [RFC 2401 Security Architecture for the Internet Protocol](../New_Technologies/Tech_RFC_2401_Security_Architecture_for_the_Internet_Protocol.htm)
  - Security,
- [RFC 2527 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework](../New_Technologies/Tech_RFC_2527_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Security,

### General Security Technologies

- [FIPS 197 for Advanced Encryption Standard (AES)](../New_Technologies/Tech_FIPS_197_for_Advanced_Encryption_Standard_(AES).htm)
  - Security,
- [Role-Based Access Control](../New_Technologies/Tech_Role-Based_Access_Control.htm)
  - Security,
- [FIPS 186 Digital Signatures Standard (DSS)](../New_Technologies/Tech_FIPS_186_Digital_Signatures_Standard_(DSS).htm)
  - Security,
- [Intrusion Detection Technologies](../New_Technologies/Tech_Intrusion_Detection_Technologies.htm)
  - Security, Network Management,
- [Intrusion Prevention Systems (IPS)](../New_Technologies/Tech_Intrusion_Prevention_Systems_(IPS).htm)
  - Security, Network Management,
- [Service Level Agreements (SLA)](../New_Technologies/Tech_Service_Level_Agreements_(SLA).htm)
  - Security,

### Media and Network Layer Technologies

- [Secure IP Architecture (IPSec)](../New_Technologies/Tech_Secure_IP_Architecture_(IPSec).htm)
  - Security,
- [IEEE 802.11i Security for Wireless Networks](../New_Technologies/Tech_IEEE_802_11i_Security_for_Wireless_Networks.htm)
  - Security,
- [Remote Authentication Dial In User Service (RADIUS)](../New_Technologies/Tech_Remote_Authentication_Dial_In_User_Service_(RADIUS).htm)
  - Security,
- [ATM Security](../New_Technologies/Tech_ATM_Security.htm)
  - Security,
- [AGA-12 Cryptographic Protection of SCADA Communications General Recommendations](../New_Technologies/Tech_AGA-12_Cryptographic_Protection_of_SCADA_Communications_Gene.htm)
  - Security,

### Transport Layer Security Technologies

- [Transport Layer Security (TLS)/Secure Sockets Layer (SSL)](../New_Technologies/Tech_Transport_Layer_Security_(TLS)-Secure_Sockets_Layer_(SSL).htm)
  - Security,

### Application Layer Security Technologies

- [SNMP Security](../New_Technologies/Tech_SNMP_Security.htm)
  - Security, Network Management,
- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
  - Quality of Service, Security,
- [IEC 62351-3 Security for Profiles including TCP/IP](../New_Technologies/Tech_IEC_62351-3_Security_for_Profiles_including_TCP-IP.htm)
  - Security,
- [IEC 62351-4 Security for Profiles including MMS (ISO-9506)](../New_Technologies/Tech_IEC_62351-4_Security_for_Profiles_including_MMS_(ISO-9506).htm)
  - Security,
- [IEC 62351-5 Security for IEC 60870-5 and Derivatives](../New_Technologies/Tech_IEC_62351-5_Security_for_IEC_60870-5_and_Derivatives.htm)
  - Security,
- [IEC 62351-6 Security for IEC 61850 GOOSE, GSSE, and SMV Profiles](../New_Technologies/Tech_IEC_62351-6_Security_for_IEC_61850_GOOSE,_GSSE,_and_SMV_Prof.htm)
  - Security,

### XML Related Technologies

- [OASIS Security Assertion Markup Language (SAML)](../New_Technologies/Tech_OASIS_Security_Assertion_Markup_Language_(SAML).htm)
  - Security,
- [Secure XML](../New_Technologies/Tech_Secure_XML.htm)
  - Security,

## Network and Enterprise Management Technologies

### Network Management Technologies

- [Simple Network Management Protocol (SNMP)](../New_Technologies/Tech_Simple_Network_Management_Protocol_(SNMP).htm)
  - Network Management,
- [IEC 62351-7 Objects for Network Management](../New_Technologies/Tech_IEC_62351-7_Objects_for_Network_Management.htm)
  - Quality of Service, Network Management, Data Management

### Web-based Network Management

- [Web-based Enterprise Management (WBEM)](../New_Technologies/Tech_Web-based_Enterprise_Management_(WBEM).htm)
  - Network Management,

---

# Recommended Common Services

## Security Services

### Common Security Services

- [Audit Common Service](../New_Technologies/Tech_Audit_Common_Service.htm)
  - Security,
- [Authorization for Access Control](../New_Technologies/Tech_Authorization_for_Access_Control.htm)
  - Security,
- [Credential Renewal Service](../New_Technologies/Tech_Credential_Renewal_Service.htm)
  - Security,
- [Information Integrity Service](../New_Technologies/Tech_Information_Integrity_Service.htm)
  - Security,
- [Security Policies](../New_Technologies/Tech_Security_Policies.htm)
  - Security,
- [Security Service Availability Discovery Service](../New_Technologies/Tech_Security_Service_Availability_Discovery_Service.htm)
  - Security,
- [Single Sign On Service](../New_Technologies/Tech_Single_Sign_On_Service.htm)
  - Security,
- [User and Group Management](../New_Technologies/Tech_User_and_Group_Management.htm)
  - Security,

## Network and System Management Services

### Enterprise Management Services

- [Inventory Management](../New_Technologies/Tech_Inventory_Management.htm)
  - Network Management,
- [Communication System/Network Discovery](../New_Technologies/Tech_Communication_System-Network_Discovery.htm)
  - Network Management,
- [Routing Management](../New_Technologies/Tech_Routing_Management.htm)
  - Network Management,
- [Traffic Management](../New_Technologies/Tech_Traffic_Management.htm)
  - Network Management,
- [Traffic Engineering](../New_Technologies/Tech_Traffic_Engineering.htm)
  - Network Management,
- [System/Network Health-Check Analysis](../New_Technologies/Tech_System-Network_Health-Check_Analysis.htm)
  - Network Management,
- [System/Network Fault Diagnosis](../New_Technologies/Tech_System-Network_Fault_Diagnosis.htm)
  - Network Management,
- [System/Network Fault Correcting](../New_Technologies/Tech_System-Network_Fault_Correcting.htm)
  - Network Management,
- [Service Level Agreement (SLA) Determination and Maintenance](../New_Technologies/Tech_Service_Level_Agreement_(SLA)_Determination_and_Maintenance.htm)
  - Network Management,
- [System/Network Performance Analysis](../New_Technologies/Tech_System-Network_Performance_Analysis.htm)
  - Network Management,
- [System/Network Performance Diagnosis](../New_Technologies/Tech_System-Network_Performance_Diagnosis.htm)
  - Network Management,
- [Performance Tuning/Correction](../New_Technologies/Tech_Performance_Tuning-Correction.htm)
  - Network Management,
- [Accounting and/or Billing](../New_Technologies/Tech_Accounting_and-or_Billing.htm)
  - Network Management,

## Data Management Common Services

### Data Management Common Services

- [Object Management Service](../New_Technologies/Tech_Object_Management_Service.htm)
  - Data Management
- [Address and Naming Management](../New_Technologies/Tech_Address_and_Naming_Management.htm)
  - Network Management, Data Management
- [Generic Eventing And Subscription](../New_Technologies/Tech_Generic_Eventing_And_Subscription.htm)
  - Network Management, Data Management
- [Alarm Detection/Reporting](../New_Technologies/Tech_Alarm_Detection-Reporting.htm)
  - Network Management, Data Management
- [Instrumentation and Monitoring Service](../New_Technologies/Tech_Instrumentation_and_Monitoring_Service.htm)
  - Network Management, Data Management
- [Measurement Data Logging Service](../New_Technologies/Tech_Measurement_Data_Logging_Service.htm)
  - Security, Network Management,
- [Remote Control](../New_Technologies/Tech_Remote_Control.htm)
  - Network Management,

## Common Platform Services

### Common Platform Services

- [Component Registry Service](../New_Technologies/Tech_Component_Registry_Service.htm)
  - Data Management
- [Component Lookup Service](../New_Technologies/Tech_Component_Lookup_Service.htm)
  - Data Management
- [Component Discovery Service](../New_Technologies/Tech_Component_Discovery_Service.htm)
  - Data Management
- [Component Initialization and Termination](../New_Technologies/Tech_Component_Initialization_and_Termination.htm)
  - Network Management,
- [Resource Management](../New_Technologies/Tech_Resource_Management.htm)
  - Network Management,

---

# Recommended Best Practices

## Data Management Best Practices

### Data Management

- [Backup Databases](../New_Technologies/Tech_Backup_Databases.htm)
  - Quality of Service,
- [Metadata Files and Databases](../New_Technologies/Tech_Metadata_Files_and_Databases.htm)
  - Network Management, Data Management
- [Object Modeling Techniques](../New_Technologies/Tech_Object_Modeling_Techniques.htm)
  - Data Management
- [Quality Flagging](../New_Technologies/Tech_Quality_Flagging.htm)
  - Quality of Service, Network Management, Data Management
- [Time Stamping](../New_Technologies/Tech_Time_Stamping.htm)
  - Quality of Service, Security, Network Management, Data Management
- [Validation of Source Data and Data Exchanges](../New_Technologies/Tech_Validation_of_Source_Data_and_Data_Exchanges.htm)
  - Data Management
- [Data Update Management](../New_Technologies/Tech_Data_Update_Management.htm)
  - Data Management
- [Management of Time-Sensitive Data Flows and Timely Access to Data by Multiple Different Users](../New_Technologies/Tech_Management_of_Time-Sensitive_Data_Flows_and_Timely_Access_to.htm)
  - Quality of Service, Data Management
- [Management of Data and Object Naming](../New_Technologies/Tech_Management_of_Data_and_Object_Naming.htm)
  - Data Management
- [Management of Data Formats in Data Exchanges](../New_Technologies/Tech_Management_of_Data_Formats_in_Data_Exchanges.htm)
  - Data Management
- [Management of Data Accuracy](../New_Technologies/Tech_Management_of_Data_Accuracy.htm)
  - Data Management
- [Management of Data Acquisition](../New_Technologies/Tech_Management_of_Data_Acquisition.htm)
  - Data Management
- [Management of Manual Data Entry](../New_Technologies/Tech_Management_of_Manual_Data_Entry.htm)
  - Data Management
- [Data Storage and Access Management](../New_Technologies/Tech_Data_Storage_and_Access_Management.htm)
  - Data Management
- [Database Maintenance Management](../New_Technologies/Tech_Database_Maintenance_Management.htm)
  - Data Management
- [Data Backup and Logging](../New_Technologies/Tech_Data_Backup_and_Logging.htm)
  - Quality of Service, Security, Data Management
- [Application Management](../New_Technologies/Tech_Application_Management.htm)
  - Network Management,

## Security Best Practices

### Security Frameworks and Policy Documents

- [ISO/IEC Security Best Practices](../New_Technologies/Tech_ISO-IEC_Security_Best_Practices.htm)
  - Security,
- [ISO/IEC 10164-8:1993 Information technology -- Open Systems Interconnection -- Systems Management: Security audit trail function](../New_Technologies/Tech_ISO-IEC_10164-8_1993_Information_technology_--_Open_Systems_.htm)
  - Quality of Service,
- [ISO/IEC 18014-1:2002 Information technology -- Security techniques -- Time-stamping services -- Part 1: Framework](../New_Technologies/Tech_ISO-IEC_18014-1_2002_Information_technology_--_Security_tech.htm)
  - Quality of Service,
- [ISO/IEC 18014-2:2002 Information technology -- Security techniques -- Time-stamping services -- Part 2: Mechanisms producing independent tokens](../New_Technologies/Tech_ISO-IEC_18014-2_2002_Information_technology_--_Security_tech.htm)
  - Quality of Service,
- [ISO/IEC 18014-3:2004 Information technology -- Security techniques -- Time-stamping services -- Part 3: Mechanisms producing linked tokens](../New_Technologies/Tech_ISO-IEC_18014-3_2004_Information_technology_--_Security_tech.htm)
  - Security,
- [Federal Security Best Practices](../New_Technologies/Tech_Federal_Security_Best_Practices.htm)
  - Security,
- [CICSI 6731.01 Global Command and Control System Security Policy](../New_Technologies/Tech_CICSI_6731_01_Global_Command_and_Control_System_Security_Pol.htm)
  - Security,
- [FIPS PUB 112 Password Usage](../New_Technologies/Tech_FIPS_PUB_112_Password_Usage.htm)
  - Security,
- [IETF Security Best Practices Internet Requests for Comments (RFCs)](../New_Technologies/Tech_IETF_Security_Best_Practices_Internet_Requests_for_Comments_.htm)
  - Network Management,
- [RFC 1102 Policy routing in Internet protocols](../New_Technologies/Tech_RFC_1102_Policy_routing_in_Internet_protocols.htm)
  - Network Management,
- [RFC 1322 A Unified Approach to Inter-Domain Routing](../New_Technologies/Tech_RFC_1322_A_Unified_Approach_to_Inter-Domain_Routing.htm)
  - Network Management,
- [RFC 1351 SNMP Administrative Model](../New_Technologies/Tech_RFC_1351_SNMP_Administrative_Model.htm)
  - Network Management,
- [RFC 2008 Implications of Various Address Allocation Policies for Internet Routing](../New_Technologies/Tech_RFC_2008_Implications_of_Various_Address_Allocation_Policies.htm)
  - Network Management,
- [RFC 2196 Site Security Handbook](../New_Technologies/Tech_RFC_2196_Site_Security_Handbook.htm)
  - Network Management,
- [RFC 2276 Architectural Principles of Uniform Resource Name Resolution](../New_Technologies/Tech_RFC_2276_Architectural_Principles_of_Uniform_Resource_Name_R.htm)
  - Security,
- [RFC 2386 A Framework for QoS-based Routing in the Internet](../New_Technologies/Tech_RFC_2386_A_Framework_for_QoS-based_Routing_in_the_Internet.htm)
  - Network Management,
- [RFC 2505 Anti-Spam Recommendations for SMTP](../New_Technologies/Tech_RFC_2505_Anti-Spam_Recommendations_for_SMTP_.htm) 
  - Security,
- [RFC 2518 HTTP Extensions for Distributed Authoring - WEBDAV](../New_Technologies/Tech_RFC_2518_HTTP_Extensions_for_Distributed_Authoring_-_WEBDAV.htm)
  - Network Management,
- [RFC 2527 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework](../New_Technologies/Tech_RFC_2527_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Network Management,

## Security Technology Documents

## 

---

# Alternative Technologies

### Utility Field Device Related Data Exchange Technologies

- [IEC60870-5 Part 104 - Telecontrol Protocol over TCP/IP](../New_Technologies/Tech_IEC60870-5_Part_104_-_Telecontrol_Protocol_over_TCP-IP.htm)
  - Configuration, Quality of Service,
- [DNP3 Protocol over TCP/IP](../New_Technologies/Tech_DNP3_Protocol_over_TCP-IP.htm)
  - Configuration, Quality of Service,

### Utility Control Center Related Data Management Technologies

- [IEC 60870-6 (ICCP)](../New_Technologies/Tech_IEC_60870-6_(ICCP).htm)
  - Configuration,

## 

### Networking Technologies

- [Internet Protocol Version 6 (IPV6)](../New_Technologies/Tech_Internet_Protocol_Version_6_(IPV6).htm)
  - Configuration,
- [Open Shortest Path First (OSPF) Routing Protocol](../New_Technologies/Tech_Open_Shortest_Path_First_(OSPF)_Routing_Protocol.htm)
  - Configuration,
- [Border Gateway Protocol (BGP)](../New_Technologies/Tech_Border_Gateway_Protocol_(BGP).htm)
  - Configuration,
- [Internet Group Management Protocol (IGMP)](../New_Technologies/Tech_Internet_Group_Management_Protocol_(IGMP).htm)
  - Configuration,
- [Distance Vector Multicast Routing Protocol (DVMRP)](../New_Technologies/Tech_Distance_Vector_Multicast_Routing_Protocol_(DVMRP).htm)
  - Configuration,
- [Multicast Open Shortest Path (MOSPF) routing protocol](../New_Technologies/Tech_Multicast_Open_Shortest_Path_(MOSPF)_routing_protocol.htm)
  - Configuration,
- [Protocol Independent Multicast-Sparse Mode (PIM-SM)](../New_Technologies/Tech_Protocol_Independent_Multicast-Sparse_Mode_(PIM-SM).htm)
  - Configuration,
- [Core-Based Tree (CBT) multicast routing](../New_Technologies/Tech_Core-Based_Tree_(CBT)_multicast_routing.htm)
  - Configuration,

### Link Layer and Physical Technologies

- [IEEE 802.1d Spanning Tree Protocol (STP)](../New_Technologies/Tech_IEEE_802_1d_Spanning_Tree_Protocol_(STP).htm)
  - Network Management,
- [IEEE 802.1w Rapid Spanning Tree Protocol (RSTP)](../New_Technologies/Tech_IEEE_802_1w_Rapid_Spanning_Tree_Protocol_(RSTP).htm)
  - Network Management,
- [Hubs/Repeaters](../New_Technologies/Tech_Hubs-Repeaters.htm)
  - Configuration,
- [Bridges/Switches](../New_Technologies/Tech_Bridges-Switches.htm)
  - Configuration,
- [Routers](../New_Technologies/Tech_Routers.htm)
  - Configuration,
- [Digital Signal (DSx), Time-division multiplexing, the T-carriers, T1, fractional T1](../New_Technologies/Tech_Digital_Signal_(DSx),_Time-division_multiplexing,_the_T-carr.htm)
  - Configuration,
- [Frame Relay](../New_Technologies/Tech_Frame_Relay.htm)
  - Configuration,

### Wireless Technologies

- [IEEE 802.16 Broadband Wireless Access Standards](../New_Technologies/Tech_IEEE_802_16_Broadband_Wireless_Access_Standards.htm)
  - Configuration,
- [Multiple Address (MAS) Radio](../New_Technologies/Tech_Multiple_Address_(MAS)_Radio.htm)
  - Configuration,
- [Spread Spectrum Radio System](../New_Technologies/Tech_Spread_Spectrum_Radio_System.htm)
  - Configuration,
- [Radio Frequency Identification (RFID)](../New_Technologies/Tech_Radio_Frequency_Identification_(RFID).htm)
  - Data Management

### Virtual Private Networking Technologies

- [Layer 3 VPNs](../New_Technologies/Tech_Layer_3_VPNs.htm)
  - Security,
- [Layer 2 VPNs](../New_Technologies/Tech_Layer_2_VPNs.htm)
  - Security,
- [PPTP](../New_Technologies/Tech_PPTP.htm)
  - Security,

## 

## 

### Network Management Technologies

- [Remote Network Monitor (RMON)](../New_Technologies/Tech_Remote_Network_Monitor_(RMON).htm)
  - Network Management,
- [OSI Network Management Model](../New_Technologies/Tech_OSI_Network_Management_Model.htm)
  - Network Management,

### Web-based Network Management

- [Policy-based Management Technologies](../New_Technologies/Tech_Policy-based_Management_Technologies.htm)
  - Network Management,

## 

## 

## 

## 

## 

---

# Alternative Best Practices

### Data Management

- [Alternate Communication Channels](../New_Technologies/Tech_Alternate_Communication_Channels.htm)
  - Quality of Service,
- [Backup Data Sources](../New_Technologies/Tech_Backup_Data_Sources.htm)
  - Quality of Service,
- [Backup Sites](../New_Technologies/Tech_Backup_Sites.htm)
  - Quality of Service,

## 

## 

### ISO/IEC Documents on Security Technologies

- [ISO/IEC 7816-9:2000 Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional](../New_Technologies/Tech_ISO-IEC_7816-9_2000_Identification_cards_--_Integrated_circu.htm) 
  - Security,
- [ISO/IEC 9594-8:1998 Information technology -- Open Systems Interconnection -- The Directory: Authentication framework](../New_Technologies/Tech_ISO-IEC_9594-8_1998_Information_technology_--_Open_Systems_I.htm)
  - Security,
- [ISO 9735-5:2002 Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 5: Security rul](../New_Technologies/Tech_ISO_9735-5_2002_Electronic_data_interchange_for_administrati.htm)
  - Security,
- [ISO/IEC 10164-9:1995 Information technology -- Open Systems Interconnection -- Systems Management: Objects and attributes for access control](../New_Technologies/Tech_ISO-IEC_10164-9_1995_Information_technology_--_Open_Systems_.htm)
  - Security,
- [ISO/IEC 10181-1:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Overview](../New_Technologies/Tech_ISO-IEC_10181-1_1996_Information_technology_--_Open_Systems_.htm)
  - Security,
- [ISO/IEC 10181-3:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Access control framework](../New_Technologies/Tech_ISO-IEC_10181-3_1996_Information_technology_--_Open_Systems_.htm)
  - Security,
- [ISO/IEC TR 13335-1:1996 Information technology -- Guidelines for the management of IT Security -- Part 1: Concepts and models for IT Security](../New_Technologies/Tech_ISO-IEC_TR_13335-1_1996_Information_technology_--_Guidelines.htm)
  - Security,
- [ISO/IEC TR 13335-2:1997 Information technology -- Guidelines for the management of IT Security -- Part 2: Managing and planning IT Security](../New_Technologies/Tech_ISO-IEC_TR_13335-2_1997_Information_technology_--_Guidelines.htm)
  - Security,
- [ISO/IEC TR 13335-5 Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security](../New_Technologies/Tech_ISO-IEC_TR_13335-5_Information_technology_-_Guidelines_for_t.htm)
  - Security,
- [ISO/IEC 15408-1:1999 Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 1: Introduction and general mode](../New_Technologies/Tech_ISO-IEC_15408-1_1999_Information_technology_--_Security_tech.htm)
  - Security,
- [ISO/IEC 15408-2:1999 Information technology -- Security techniques -- Evaluation criteria for IT security -- Part 2: Security functional requirements](../New_Technologies/Tech_ISO-IEC_15408-2_1999_Information_technology_--_Security_tech.htm)
  - Security,
- [ISO/IEC 17799:2000 Information technology -- Code of practice for information security management](../New_Technologies/Tech_ISO-IEC_17799_2000_Information_technology_--_Code_of_practic.htm)
  - Security,

### Federal Documents on Security Technologies

- [FIPS 197 Federal Information Processing Standards Publication 197, Specification for the Advanced Encryption Standard (AES)](../New_Technologies/Tech_FIPS_197_Federal_Information_Processing_Standards_Publicatio.htm)
  - Security,

### IETF Internet Requests for Comments (RFCs) on Security Technologies

- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
  - Quality of Service,
- [RFC 1352 SNMP Security Protocols](../New_Technologies/Tech_RFC_1352_SNMP_Security_Protocols.htm)
  - Network Management,
- [RFC 1827 IP Encapsulating Security Payload (ESP)](../New_Technologies/Tech_RFC_1827_IP_Encapsulating_Security_Payload_(ESP).htm)
  - Security,
- [RFC 1940 Source Demand Routing: Packet Format and Forwarding Specification (Version 1)](../New_Technologies/Tech_RFC_1940_Source_Demand_Routing__Packet_Format_and_Forwarding.htm)
  - Network Management,
- [RFC 1968 The PPP Encryption Control Protocol (ECP)](../New_Technologies/Tech_RFC_1968_The_PPP_Encryption_Control_Protocol_(ECP).htm)
  - Security,
- [RFC 2040 The RC5, RC5-CBC, RC5-CBC-Pad, and RC5-CTS Algorithms](../New_Technologies/Tech_RFC_2040_The_RC5,_RC5-CBC,_RC5-CBC-Pad,_and_RC5-CTS_Algorith.htm)
  - Security,
- [RFC 2045 Multi-Purpose Internet Mail Extensions (MIME) and Secure/MIME](../New_Technologies/Tech_RFC_2045_Multi-Purpose_Internet_Mail_Extensions_(MIME)_and_S.htm)
  - Security,
- [RFC 2086 IMAP4 ACL extension](../New_Technologies/Tech_RFC_2086_IMAP4_ACL_extension.htm)
  - Security,
- [RFC 2093 Group Key Management Protocol (GKMP) Specification](../New_Technologies/Tech_RFC_2093_Group_Key_Management_Protocol_(GKMP)_Specification.htm)
  - Security,
- [RFC 2228 FTP Security Extensions](../New_Technologies/Tech_RFC_2228_FTP_Security_Extensions.htm)
  - Security,
- [RFC 2230 Key Exchange Delegation Record for the DNS](../New_Technologies/Tech_RFC_2230_Key_Exchange_Delegation_Record_for_the_DNS.htm)
  - Security,
- [RFC 2244 ACAP -- Application Configuration Access Protocol](../New_Technologies/Tech_RFC_2244_ACAP_--_Application_Configuration_Access_Protocol.htm)
  - Security,
- [RFC 2246 The TLS Protocol Version 1.0](../New_Technologies/Tech_RFC_2246_The_TLS_Protocol_Version_1_0.htm)
  - Security,
- [RFC 2313 PKCS #1: RSA Encryption Version 1.5](../New_Technologies/Tech_RFC_2313_PKCS_1__RSA_Encryption_Version_1_5.htm)
  - Security,
- [RFC 2315 PKCS #7: Cryptographic Message Syntax Version 1.5](../New_Technologies/Tech_RFC_2315_PKCS_7__Cryptographic_Message_Syntax_Version_1_5.htm)
  - Security,
- [RFC 2406 IP Encapsulating Security Payload (ESP)](../New_Technologies/Tech_RFC_2406_IP_Encapsulating_Security_Payload_(ESP).htm)
  - Security,
- [RFC 2437 PKCS #1: RSA Cryptography Specifications Version 2.0](../New_Technologies/Tech_RFC_2437_PKCS_1__RSA_Cryptography_Specifications_Version_2_0.htm)
  - Security,
- [RFC 2440 OpenPGP Message Format](../New_Technologies/Tech_RFC_2440_OpenPGP_Message_Format.htm)
  - Security,
- [RFC 2408 Internet Security Association and Key Management Protocol (ISAKMP)](../New_Technologies/Tech_RFC_2408_Internet_Security_Association_and_Key_Management_Pr.htm)
  - Security,
- [RFC 2409 The Internet Key Exchange (IKE)](../New_Technologies/Tech_RFC_2409_The_Internet_Key_Exchange_(IKE).htm)
  - Security,
- [RFC 2459 Internet X.509 Public Key Infrastructure Certificate and CRL Profile](../New_Technologies/Tech_RFC_2459_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Security,
- [RFC 2510 Internet X.509 Public Key Infrastructure Certificate Management Protocols](../New_Technologies/Tech_RFC_2510_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Security,
- [RFC 2511 Internet X.509 Certificate Request Message Format](../New_Technologies/Tech_RFC_2511_Internet_X_509_Certificate_Request_Message_Format.htm)
  - Security,
- [RFC 2527 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework](../New_Technologies/Tech_RFC_2527_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Security,
- [RFC 2547 BGP/MPLS VPNs](../New_Technologies/Tech_RFC_2547_BGP-MPLS_VPNs.htm)
  - Security, Network Management,
- [RFC 2560 X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP](../New_Technologies/Tech_RFC_2560_X_509_Internet_Public_Key_Infrastructure_Online_Cer.htm)
  - Security,
- [RFC 2764 A Framework for IP Based Virtual Private Networks](../New_Technologies/Tech_RFC_2764_A_Framework_for_IP_Based_Virtual_Private_Networks.htm)
  - Security, Network Management,
- [RFC 2753 A Framework for Policy-based Admission Control](../New_Technologies/Tech_RFC_2753_A_Framework_for_Policy-based_Admission_Control.htm)
  - Security,
- [RFC 2797 Certificate Management Messages over CMS](../New_Technologies/Tech_RFC_2797_Certificate_Management_Messages_over_CMS.htm)
  - Security,
- [RFC 2817 Upgrades to TLS within HTTP/1.1](../New_Technologies/Tech_RFC_2817_Upgrades_to_TLS_within_HTTP-1_1.htm)
  - Security,
- [RFC 2818 HTTP over TLS (HTTPS)](../New_Technologies/Tech_RFC_2818_HTTP_over_TLS_(HTTPS).htm)
  - Security,
- [RFC 2875](../New_Technologies/Tech_RFC_2875_.htm) 
  - Security,
- [RFC 2898 PKCS #5: Password-Based Cryptography Specification Version 2.0](../New_Technologies/Tech_RFC_2898_PKCS_5__Password-Based_Cryptography_Specification_V.htm)
  - Security,
- [RFC 2946 Telnet Data Encryption Option](../New_Technologies/Tech_RFC_2946_Telnet_Data_Encryption_Option.htm)
  - Security,
- [RFC 2977 Mobile IP Authentication, Authorization, and Accounting Requirements](../New_Technologies/Tech_RFC_2977_Mobile_IP_Authentication,_Authorization,_and_Accoun.htm)
  - Security,
- [RFC 2985 PKCS #9: Selected Object Classes and Attribute Types Version 2.0](../New_Technologies/Tech_RFC_2985_PKCS_9__Selected_Object_Classes_and_Attribute_Types.htm)
  - Security,
- [RFC 2986 PKCS #10: Certification Request Syntax Specification Version 1.7](../New_Technologies/Tech_RFC_2986_PKCS_10__Certification_Request_Syntax_Specification.htm)
  - Security,
- [RFC 3053 IPv6 Tunnel Broker](../New_Technologies/Tech_RFC_3053_IPv6_Tunnel_Broker.htm)
  - Network Management,
- [RFC 3268 Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS)](../New_Technologies/Tech_RFC_3268_Advanced_Encryption_Standard_(AES)_Ciphersuites_for.htm)
  - Security,
- [RFC 3280 Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](../New_Technologies/Tech_RFC_3280_Algorithms_and_Identifiers_for_the_Internet_X_509_P.htm)
  - Security,
- [RFC 3369 Cryptographic Message Syntax (CMS)](../New_Technologies/Tech_RFC_3369_Cryptographic_Message_Syntax_(CMS).htm)
  - Security,
- [RFC 3370 Cryptographic Message Syntax (CMS) Algorithms](../New_Technologies/Tech_RFC_3370_Cryptographic_Message_Syntax_(CMS)_Algorithms.htm)
  - Security,
- [RFC 3414 User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3)](../New_Technologies/Tech_RFC_3414_User-based_Security_Model_(USM)_for_version_3_of_th.htm)
  - Network Management,
- [RFC 3447 Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1](../New_Technologies/Tech_RFC_3447_Public-Key_Cryptography_Standards_(PKCS)_1__RSA_Cry.htm)
  - Security,
- [RFC 3647 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework](../New_Technologies/Tech_RFC_3647_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Security,

### Other Security Technolog

- [IEEE 802.11b Web Encryption Protocol](../New_Technologies/Tech_IEEE_802_11b_Web_Encryption_Protocol.htm)
  - Security,
- [IEEE 802.11i Security for Wireless Networks](../New_Technologies/Tech_IEEE_802_11i_Security_for_Wireless_Networks.htm)
  - Security,
- [RSA Documents on Security Technologies](../New_Technologies/Tech_RSA_Documents_on_Security_Technologies.htm)
  - Security,
- [RSA PKCS #8 Private-Key Information Syntax Standard](../New_Technologies/Tech_RSA_PKCS_8_Private-Key_Information_Syntax_Standard.htm)
  - Security,
- [RSA PKCS #12 Personal Information Exchange Syntax Standard, version 1.0.](../New_Technologies/Tech_RSA_PKCS_12_Personal_Information_Exchange_Syntax_Standard,_v.htm)
  - Security,
- [OASIS Documents on Security Technologies](../New_Technologies/Tech_OASIS_Documents_on_Security_Technologies.htm)
  - Security,
- [WC3 XML Key Management Specification (XKMS 2.0) Bindings](../New_Technologies/Tech_WC3_XML_Key_Management_Specification_(XKMS_2_0)_Bindings.htm)
  - Security,
- [AGA-12 Cryptographic Protection of SCADA Communications General Recommendations.](../New_Technologies/Tech_AGA-12_Cryptographic_Protection_of_SCADA_Communications_Gene.htm)
  - Security,
- [ANSI INCITS 359-2004 Role Based Access Control (RBAC)](../New_Technologies/Tech_ANSI_INCITS_359-2004_Role_Based_Access_Control_(RBAC).htm)
  - Security,
- [EPRI 1002596 ICCP TASE.2 Security Enhancements](../New_Technologies/Tech_EPRI_1002596_ICCP_TASE_2_Security_Enhancements.htm)
  - Security,
- [NERC Certificate Policy for the Energy Market Access and Reliability Certificate (e MARC) Program Version 2.4](../New_Technologies/Tech_NERC_Certificate_Policy_for_the_Energy_Market_Access_and_Rel.htm)
  - Security,
- [WebDAV Access Control Extensions to WebDAV](../New_Technologies/Tech_WebDAV_Access_Control_Extensions_to_WebDAV.htm)
  - Security,
- [WPA WI-FI Protected Access](../New_Technologies/Tech_WPA_WI-FI_Protected_Access.htm)
  - Security,
- [WPA2 WI-FI Protected Access Version 2](../New_Technologies/Tech_WPA2_WI-FI_Protected_Access_Version_2.htm)
  - Security,
- [TMN PKI - Digital certificates and certificate revocation lists profiles](../New_Technologies/Tech_TMN_PKI_-_Digital_certificates_and_certificate_revocation_li.htm)
  - Security,

## 

---

# Possible Technologies

### Utility Field Device Related Data Exchange Technologies

- [IEC60870-5 Part 101 - Serial Telecontrol Protocol](../New_Technologies/Tech_IEC60870-5_Part_101_-_Serial_Telecontrol_Protocol.htm)
  - Configuration,
- [DNP Serial Protocol](../New_Technologies/Tech_DNP_Serial_Protocol.htm)
  - Configuration,
- [Fieldbus](../New_Technologies/Tech_Fieldbus.htm)
  - Configuration, Quality of Service,
- [PROFIBUS](../New_Technologies/Tech_PROFIBUS.htm)
  - Configuration, Quality of Service,
- [ModBus](../New_Technologies/Tech_ModBus.htm)
  - Quality of Service,
- [ModBus TCP/IP](../New_Technologies/Tech_ModBus_TCP-IP.htm)
  - Configuration, Quality of Service,
- [ModBus Plus](../New_Technologies/Tech_ModBus_Plus.htm)
  - Configuration, Quality of Service,

## 

### Access Technologies

- [Data over Voice Lines](../New_Technologies/Tech_Data_over_Voice_Lines.htm)
  - Configuration,
- [Fiber in the Loop (FITL)](../New_Technologies/Tech_Fiber_in_the_Loop_(FITL).htm)
  - Configuration,
- [Hybrid Fiber Coax (HFC)](../New_Technologies/Tech_Hybrid_Fiber_Coax_(HFC).htm)
  - Configuration,

### Networking Technologies

- [Intermediate System to Intermediate System (ISIS) Routing Protocol](../New_Technologies/Tech_Intermediate_System_to_Intermediate_System_(ISIS)_Routing_Pr.htm)
  - Configuration,
- [Routing Information Protocol (RIP)](../New_Technologies/Tech_Routing_Information_Protocol_(RIP).htm)
  - Configuration,

### IP-based Transport Protocols

- [Datagram Congestion Control Protocol (DCCP)](../New_Technologies/Tech_Datagram_Congestion_Control_Protocol_(DCCP).htm)
  - Configuration,
- [Real-Time Transport Protocol (RTP)](../New_Technologies/Tech_Real-Time_Transport_Protocol_(RTP).htm)
  - Configuration,

### Wireless Technologies

- [Trunked Mobile Radio (TMR, TETRA, Project25)](../New_Technologies/Tech_Trunked_Mobile_Radio_(TMR,_TETRA,_Project25).htm)
  - Configuration,
- [Satellite Leased Channels and VSAT](../New_Technologies/Tech_Satellite_Leased_Channels_and_VSAT.htm)
  - Configuration,

## 

## 

## 

## 

## 

## 

## 

## 

##
