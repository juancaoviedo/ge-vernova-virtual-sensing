# Env20 Maintenance

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Environments/Env20_Field_Equipment_Maintenance.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Field Equipment Maintenance Environment - #20

This
environment represents all communications with field crews.

if !vml?![](Env20_Field_Equipment_Maintenance_files/image002.gif)endif?**Typical
Applications:**  Asset management, primary equipment monitoring and
maintenance, planned outages, statistics gathering, testing,
diagnostics, protection engineering, trouble call management, updating
of schematics and drawings, emergency (fire, earthquake, flood)
response.

**Characteristics:**  Extremely mobile
workforce and frequent configuration changes makes wireless
communications, ease of use and self-discovery a necessity.   Response
times in seconds are required due to human reaction times.  Data is
critical to safe and reliable operation of the grid, and must be keyed
to role-based access, i.e. only certain employees have access to
certain data.

**Similar Environments:**  Similar to both
Critical Operations DAC and Non-Critical Operations DAC, but with an
emphasis on mobile access.

**Definition:**  This environment is defined
by the following requirements:

---

# Communication and Information Requirements that Define this Environment

## Configuration Requirements

* Support interactions between a few "clients" and many "servers"
* Support interactions across widely distributed sites
* Support mandatory mobile communications

## Quality of Service Requirements

* Provide medium speed messaging on the order of 10 seconds
* Support medium availability of information flows of 99.0+ (~3.5 days)

## Security Requirements

* Provide Identity Establishment Service (you are who you say you are)
* Provide Authorization Service for Access Control (resolving a policy-based access control decision to ensure authorized entities have appropriate access rights and authorized access is not denied)
* Provide Information Integrity Service (data has not been subject to unauthorized changes or these unauthorized changes are detected)
* Provide Firewall Transversal
* Provide User Profile and User Management (combination of several other security services)
* Provide Security Discovery (the ability to determine what security services are available for use)

## Network and System Management Requirements

* Provide Network Management (management of media, transport, and communication nodes)
* Provide System Management (management of end devices and applications)

## Data Management Requirements

* Support extensive data validation procedures
* Support frequent changes in types of data exchanged
* Support management of data whose types can vary significantly in different implementations
* Support specific standardized or de facto object models of data
* Support the exchange of unstructured or special-format data (e.g. text, documents, oscillographic data)
* Support transaction integrity (consistency and rollback capability)
* Provide discovery service (discovering available services and their characteristics)
* Provide conversion and protocol mapping

---

# Recommended Technologies

## Energy Industry-Specific Technologies

### Utility Field Device Related Data Exchange Technologies

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
- [IEC 61970 Part 4 - Generic Interface Definition (GID)](../New_Technologies/Tech_IEC_61970_Part_4_-_Generic_Interface_Definition_(GID).htm)
  - Configuration, Quality of Service, Data Management
- [IEC61968 SIDM System Interfaces for Distribution Management](../New_Technologies/Tech_IEC61968_SIDM_System_Interfaces_for_Distribution_Management.htm)
  - Data Management
- [OPEN GIS](../New_Technologies/Tech_OPEN_GIS.htm)
  - Data Management

### Customer Interface Data Management Technologies

- [IEC62056 - Data Exchange for Meter Reading, Tariff, and Load Control](../New_Technologies/Tech_IEC62056_-_Data_Exchange_for_Meter_Reading,_Tariff,_and_Load.htm) 
  - Data Management
- [ANSI C12.19 (Meter Tables)](../New_Technologies/Tech_ANSI_C12_19_(Meter_Tables).htm)
  - Data Management
- [AEIC Guidelines](../New_Technologies/Tech_AEIC_Guidelines.htm)
  - Data Management

## Communications Industry Technologies

### Access Technologies

- [Public Internet](../New_Technologies/Tech_Public_Internet.htm)
  - Configuration,
- [Private Intranet](../New_Technologies/Tech_Private_Intranet.htm)
  - Configuration,

### Networking Technologies

- [Internet Protocol Version V4 (IPV4)](../New_Technologies/Tech_Internet_Protocol_Version_V4_(IPV4).htm)
  - Configuration,

### IP-based Transport Protocols

- [Transmission Control Protocol (TCP)](../New_Technologies/Tech_Transmission_Control_Protocol_(TCP).htm)
  - Configuration,

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

- [Global System for Mobile Communication (GSM)](../New_Technologies/Tech_Global_System_for_Mobile_Communication_(GSM).htm)
  - Configuration,

### Computer Systems Related Technologies

- [Web Services](../New_Technologies/Tech_Web_Services_.htm) 
  - Data Management
- [Universal Description, Discovery, and Integration (UDDI)](../New_Technologies/Tech_Universal_Description,_Discovery,_and_Integration_(UDDI).htm)
  - Data Management
- [XML Protocol/Simple Object Access Protocol (SOAP)](../New_Technologies/Tech_XML_Protocol-Simple_Object_Access_Protocol_(SOAP).htm)
  - Data Management
- [Enterprise Java Beans (EJB)](../New_Technologies/Tech_Enterprise_Java_Beans_(EJB).htm)
  - Data Management
- [GUID](../New_Technologies/Tech_GUID.htm)
  - Data Management

### General Internet and De Facto Data Management Technologies

- [ANSI/ISO/IEC 8632-1, 2, 3, 4 - Computer Graphics Metafile (CGM)](../New_Technologies/Tech_ANSI-ISO-IEC_8632-1,_2,_3,_4_-_Computer_Graphics_Metafile_(C.htm)
  - Data Management
- [ISO/IEC 11179 Parts 1 - 6 Metadata Registries](../New_Technologies/Tech_ISO-IEC_11179_Parts_1_-_6_Metadata_Registries.htm)
  - Data Management
- [Meta Object Facility (MOF)](../New_Technologies/Tech_Meta_Object_Facility_(MOF).htm)
  - Data Management
- [XML Metadata Interchange (XMI)](../New_Technologies/Tech_XML_Metadata_Interchange_(XMI).htm)
  - Data Management
- [eXtensible Markup Language (XML)](../New_Technologies/Tech_eXtensible_Markup_Language_(XML).htm)
  - Data Management
- [XML Schema (xls)](../New_Technologies/Tech_XML_Schema_(xls).htm)
  - Data Management
- [ANSI/ISO/IEC 9075 - Structured Query Language (SQL)](../New_Technologies/Tech_ANSI-ISO-IEC_9075_-_Structured_Query_Language_(SQL).htm)
  - Data Management

## Security Technologies

### Policy and Framework Related Technologies

- [ISO/IEC 10164-8:1993 Security Audit Trail Function - Information technology - Open Systems Interconnection - Systems Management](../New_Technologies/Tech_ISO-IEC_10164-8_1993_Security_Audit_Trail_Function_-_Informa.htm)
  - Security,
- [ISO/IEC 18014-1:2002 Time-Stamping Services - Information technology - Security Techniques - Part 1: Framework](../New_Technologies/Tech_ISO-IEC_18014-1_2002_Time-Stamping_Services_-_Information_te.htm)
  - Data Management
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
- [FIPS 186 Digital Signatures Standard (DSS)](../New_Technologies/Tech_FIPS_186_Digital_Signatures_Standard_(DSS).htm)
  - Security,
- [Intrusion Detection Technologies](../New_Technologies/Tech_Intrusion_Detection_Technologies.htm)
  - Network Management,
- [Intrusion Prevention Systems (IPS)](../New_Technologies/Tech_Intrusion_Prevention_Systems_(IPS).htm)
  - Network Management,

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

### Application Layer Security Technologies

- [RFC 2228 FTP Security Extensions](../New_Technologies/Tech_RFC_2228_FTP_Security_Extensions.htm)
  - Security,
- [Internet Mail Extensions](../New_Technologies/Tech_Internet_Mail_Extensions.htm)
  - Security,
- [RFC 2086 IMAP4 ACL extension](../New_Technologies/Tech_RFC_2086_IMAP4_ACL_extension.htm)
  - Security,
- [SNMP Security](../New_Technologies/Tech_SNMP_Security.htm)
  - Security, Network Management,
- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
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

- [Authorization for Access Control](../New_Technologies/Tech_Authorization_for_Access_Control.htm)
  - Security,
- [Firewall Traversal](../New_Technologies/Tech_Firewall_Traversal.htm)
  - Security,
- [Identity Establishment Service](../New_Technologies/Tech_Identity_Establishment_Service.htm)
  - Security,
- [Information Integrity Service](../New_Technologies/Tech_Information_Integrity_Service.htm)
  - Security,
- [Quality of Identity Service](../New_Technologies/Tech_Quality_of_Identity_Service.htm)
  - Security,
- [Security Service Availability Discovery Service](../New_Technologies/Tech_Security_Service_Availability_Discovery_Service.htm)
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
  - Network Management,
- [Alarm Detection/Reporting](../New_Technologies/Tech_Alarm_Detection-Reporting.htm)
  - Network Management, Data Management
- [Instrumentation and Monitoring Service](../New_Technologies/Tech_Instrumentation_and_Monitoring_Service.htm)
  - Network Management, Data Management
- [Measurement Data Logging Service](../New_Technologies/Tech_Measurement_Data_Logging_Service.htm)
  - Network Management,
- [Remote Control](../New_Technologies/Tech_Remote_Control.htm)
  - Network Management,
- [File Transfer](../New_Technologies/Tech_File_Transfer.htm)
  - Data Management

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
- [Transactions](../New_Technologies/Tech_Transactions.htm)
  - Data Management
- [Checkpoint and Recovery](../New_Technologies/Tech_Checkpoint_and_Recovery.htm)
  - Network Management, Data Management
- [Workflow Service](../New_Technologies/Tech_Workflow_Service.htm)
  - Network Management,

---

# Recommended Best Practices

## Data Management Best Practices

### Data Management

- [Metadata Files and Databases](../New_Technologies/Tech_Metadata_Files_and_Databases.htm)
  - Network Management, Data Management
- [Object Modeling Techniques](../New_Technologies/Tech_Object_Modeling_Techniques.htm)
  - Data Management
- [Quality Flagging](../New_Technologies/Tech_Quality_Flagging.htm)
  - Network Management, Data Management
- [Time Stamping](../New_Technologies/Tech_Time_Stamping.htm)
  - Network Management, Data Management
- [Validation of Source Data and Data Exchanges](../New_Technologies/Tech_Validation_of_Source_Data_and_Data_Exchanges.htm)
  - Data Management
- [Data Update Management](../New_Technologies/Tech_Data_Update_Management.htm)
  - Data Management
- [Management of Data and Object Naming](../New_Technologies/Tech_Management_of_Data_and_Object_Naming.htm)
  - Data Management
- [Management of Data Formats in Data Exchanges](../New_Technologies/Tech_Management_of_Data_Formats_in_Data_Exchanges.htm)
  - Data Management
- [Management of Transaction Integrity (backup and rollback capability)](../New_Technologies/Tech_Management_of_Transaction_Integrity_(backup_and_rollback_cap.htm)
  - Data Management
- [Management of Data Accuracy](../New_Technologies/Tech_Management_of_Data_Accuracy.htm)
  - Data Management
- [Management of Data Acquisition](../New_Technologies/Tech_Management_of_Data_Acquisition.htm)
  - Data Management
- [Management of Manual Data Entry](../New_Technologies/Tech_Management_of_Manual_Data_Entry.htm)
  - Data Management
- [Database Maintenance Management](../New_Technologies/Tech_Database_Maintenance_Management.htm)
  - Data Management
- [Data Backup and Logging](../New_Technologies/Tech_Data_Backup_and_Logging.htm)
  - Quality of Service, Data Management
- [Application Management](../New_Technologies/Tech_Application_Management.htm)
  - Network Management,

## Security Best Practices

### Security Frameworks and Policy Documents

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

- [C37.111-1999 IEEE COMTRADE Standard (Common Format for Transient Data Exchange) for Power Systems](../New_Technologies/Tech_C37_111-1999_IEEE_COMTRADE_Standard_(Common_Format_for_Trans.htm)
  - Data Management
- [IEEE 1159.3 - Power Quality Data Interchange Format (PQDIF)](../New_Technologies/Tech_IEEE_1159_3_-_Power_Quality_Data_Interchange_Format_(PQDIF).htm)
  - Data Management

### Utility Control Center Related Data Management Technologies

- [IEC 60870-6 (ICCP)](../New_Technologies/Tech_IEC_60870-6_(ICCP).htm)
  - Configuration,
- [MultiSpeak](../New_Technologies/Tech_MultiSpeak.htm)
  - Data Management

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

### IP-based Transport Protocols

- [Stream Control Transmission Protocol (SCTP)](../New_Technologies/Tech_Stream_Control_Transmission_Protocol_(SCTP).htm)
  - Configuration,
- [Datagram Congestion Control Protocol (DCCP)](../New_Technologies/Tech_Datagram_Congestion_Control_Protocol_(DCCP).htm)
  - Configuration,
- [Real-Time Transport Protocol (RTP)](../New_Technologies/Tech_Real-Time_Transport_Protocol_(RTP).htm)
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

- [3rd Generation Cellular Wireless](../New_Technologies/Tech_3rd_Generation_Cellular_Wireless.htm)
  - Configuration,
- [Universal Mobile Telecommunication System (UMTS)](../New_Technologies/Tech_Universal_Mobile_Telecommunication_System_(UMTS).htm)
  - Configuration,
- [Code-Division Multiple Access 2000 (CDMA-2000)](../New_Technologies/Tech_Code-Division_Multiple_Access_2000_(CDMA-2000).htm)
  - Configuration,
- [TDMA Cellular Wireless - IS-136](../New_Technologies/Tech_TDMA_Cellular_Wireless_-_IS-136.htm)
  - Configuration,
- [CDMA Cellular Wireless - IS-95](../New_Technologies/Tech_CDMA_Cellular_Wireless_-_IS-95.htm)
  - Configuration,
- [Cellular Digital Packet Data (CDPD)](../New_Technologies/Tech_Cellular_Digital_Packet_Data_(CDPD).htm)
  - Configuration,
- [Short Message Service (SMS)](../New_Technologies/Tech_Short_Message_Service_(SMS).htm)
  - Configuration,
- [Trunked Mobile Radio (TMR, TETRA, Project25)](../New_Technologies/Tech_Trunked_Mobile_Radio_(TMR,_TETRA,_Project25).htm)
  - Configuration,
- [IEEE 802.11 Wireless Local Area Network (WLAN)](../New_Technologies/Tech_IEEE_802_11_Wireless_Local_Area_Network_(WLAN).htm)
  - Configuration,
- [IEEE 802.15 Wireless Personal Area Network (PAN)](../New_Technologies/Tech_IEEE_802_15_Wireless_Personal_Area_Network_(PAN).htm)
  - Configuration,
- [Bluetooth Special](../New_Technologies/Tech_Bluetooth_Special.htm)
  - Configuration,
- [IEEE 802.16 Broadband Wireless Access Standards](../New_Technologies/Tech_IEEE_802_16_Broadband_Wireless_Access_Standards.htm)
  - Configuration,
- [Multiple Address (MAS) Radio](../New_Technologies/Tech_Multiple_Address_(MAS)_Radio.htm)
  - Configuration,
- [Spread Spectrum Radio System](../New_Technologies/Tech_Spread_Spectrum_Radio_System.htm)
  - Configuration,
- [Satellite Leased Channels and VSAT](../New_Technologies/Tech_Satellite_Leased_Channels_and_VSAT.htm)
  - Configuration,
- [Paging Systems](../New_Technologies/Tech_Paging_Systems.htm)
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

### Computer Systems Related Technologies

- [Web Services Description Language (WSDL)](../New_Technologies/Tech_Web_Services_Description_Language_(WSDL).htm)
  - Data Management

### General Internet and De Facto Data Management Technologies

- [Common Warehouse Model (CWM)](../New_Technologies/Tech_Common_Warehouse_Model_(CWM).htm)
  - Data Management
- [American Standard Code for Information Interchange (ASCII)](../New_Technologies/Tech_American_Standard_Code_for_Information_Interchange_(ASCII).htm)
  - Data Management
- [Hypertext Markup Language (HTML)](../New_Technologies/Tech_Hypertext_Markup_Language_(HTML).htm)
  - Data Management
- [RDF](../New_Technologies/Tech_RDF.htm)
  - Data Management

### eCommerce Related Data Management Technologies

- [EAN.UCC Identification Numbers](../New_Technologies/Tech_EAN_UCC_Identification_Numbers.htm)
  - Data Management
- [EAN.UCC Universal Bar Codes](../New_Technologies/Tech_EAN_UCC_Universal_Bar_Codes.htm)
  - Data Management
- [10303 Standard Exchange for Product Data (STEP)](../New_Technologies/Tech_10303_Standard_Exchange_for_Product_Data_(STEP).htm)
  - Data Management

## 

## 

### Network Management Technologies

- [Remote Network Monitor (RMON)](../New_Technologies/Tech_Remote_Network_Monitor_(RMON).htm)
  - Network Management,
- [OSI Network Management Model](../New_Technologies/Tech_OSI_Network_Management_Model.htm)
  - Network Management,
- [Telecommunications Management Network (TMN) - M series](../New_Technologies/Tech_Telecommunications_Management_Network_(TMN)_-_M_series.htm)
  - Network Management,
- [Transaction Language 1 (TL1)](../New_Technologies/Tech_Transaction_Language_1_(TL1).htm)
  - Network Management,

### Web-based Network Management

- [Policy-based Management Technologies](../New_Technologies/Tech_Policy-based_Management_Technologies.htm)
  - Network Management,

## 

## 

## 

## 

## 

## 

---

# Alternative Best Practices

### Security Frameworks and Policy Documents

- [ISO/IEC 10181-7:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Security audit and alarms framework](../New_Technologies/Tech_ISO-IEC_10181-7_1996_Information_technology_--_Open_Systems_.htm)
  - Security,

## 

### ISO/IEC Documents on Security Technologies

- [ISO/IEC 7816-1:1998 Identification cards -- Integrated circuit(s) cards with contacts -- Part 1: Physical characteristics](../New_Technologies/Tech_ISO-IEC_7816-1_1998_Identification_cards_--_Integrated_circu.htm)
  - Security,
- [ISO/IEC 7816-3:1997 Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 3: Electronic signals and transmission protocols](../New_Technologies/Tech_ISO-IEC_7816-3_1997_Information_technology_--_Identification.htm)
  - Security,
- [ISO/IEC 7816-3:1997/Amd 1:2002 Electrical characteristics and class indication for integrated circuit(s) cards operating at 5 V, 3 V and 1,8 V](../New_Technologies/Tech_ISO-IEC_7816-3_1997-Amd_1_2002_Electrical_characteristics_an.htm)
  - Security,
- [ISO/IEC 7816-4:1995 Information technology -- Identification cards -- Integrated circuit(s) cards with contacts -- Part 4: Inter-industry commands for interchange](../New_Technologies/Tech_ISO-IEC_7816-4_1995_Information_technology_--_Identification.htm)
  - Security,
- [ISO/IEC 7816-4:1995/Amd 1:1997 secure messaging on the structures of APDU messages](../New_Technologies/Tech_ISO-IEC_7816-4_1995-Amd_1_1997_secure_messaging_on_the_struc.htm)
  - Security,
- [ISO/IEC 7816-5:1994 Identification cards -- Integrated circuit(s) cards with contacts -- Part 5: Numbering system and registration procedure for application identifiers](../New_Technologies/Tech_ISO-IEC_7816-5_1994_Identification_cards_--_Integrated_circu.htm)
  - Security,
- [ISO/IEC 7816-7:1999 Identification cards -- Integrated circuit(s) cards with contacts -- Part 7:](../New_Technologies/Tech_ISO-IEC_7816-7_1999_Identification_cards_--_Integrated_circu.htm) 
  - Security,
- [ISO/IEC 7816-8:1999 Identification cards -- Integrated circuit(s) cards with contacts -- Part 8: Security related](../New_Technologies/Tech_ISO-IEC_7816-8_1999_Identification_cards_--_Integrated_circu.htm) 
  - Security,
- [ISO/IEC 7816-9:2000 Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional](../New_Technologies/Tech_ISO-IEC_7816-9_2000_Identification_cards_--_Integrated_circu.htm) 
  - Security,
- [ISO/IEC 7816-10:1999 Identification cards -- Integrated circuit(s) cards with contacts -- Part 10: Electronic signals and answer to reset for synchronous cards](../New_Technologies/Tech_ISO-IEC_7816-10_1999_Identification_cards_--_Integrated_circ.htm)
  - Security,
- [ISO/IEC 7816-11:2004 Identification cards -- Integrated circuit cards -- Part 11: Personal verification through biometric methods](../New_Technologies/Tech_ISO-IEC_7816-11_2004_Identification_cards_--_Integrated_circ.htm)
  - Security,
- [ISO/IEC 7816-15:2004 Identification cards -- Integrated circuit cards with contacts -- Part 15: Cryptographic information application](../New_Technologies/Tech_ISO-IEC_7816-15_2004_Identification_cards_--_Integrated_circ.htm)
  - Security,
- [ISO/IEC 9594-8:1998 Information technology -- Open Systems Interconnection -- The Directory: Authentication framework](../New_Technologies/Tech_ISO-IEC_9594-8_1998_Information_technology_--_Open_Systems_I.htm)
  - Security,
- [ISO 9735-5:2002 Electronic data interchange for administration, commerce and transport (EDIFACT) -- Application level syntax rules (Syntax version number: 4, Syntax release number: 1) -- Part 5: Security rul](../New_Technologies/Tech_ISO_9735-5_2002_Electronic_data_interchange_for_administrati.htm)
  - Security,
- [ISO/IEC 10164-9:1995 Information technology -- Open Systems Interconnection -- Systems Management: Objects and attributes for access control](../New_Technologies/Tech_ISO-IEC_10164-9_1995_Information_technology_--_Open_Systems_.htm)
  - Security,
- [ISO/IEC 10181-2:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Authentication framework](../New_Technologies/Tech_ISO-IEC_10181-2_1996_Information_technology_--_Open_Systems_.htm)
  - Security,
- [ISO/IEC 10181-3:1996 Information technology -- Open Systems Interconnection -- Security frameworks for open systems: Access control framework](../New_Technologies/Tech_ISO-IEC_10181-3_1996_Information_technology_--_Open_Systems_.htm)
  - Security,
- [ISO 10202-1:1991 Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 1: Card life cycle](../New_Technologies/Tech_ISO_10202-1_1991_Financial_transaction_cards_--_Security_arc.htm)
  - Security,
- [ISO 10202-7:1998 Financial transaction cards -- Security architecture of financial transaction systems using integrated circuit cards -- Part 7: Key management](../New_Technologies/Tech_ISO_10202-7_1998_Financial_transaction_cards_--_Security_arc.htm)
  - Security,
- [ISO 10202-8:1998 Financial transaction cards -- Security architecture of financial transaction systems](../New_Technologies/Tech_ISO_10202-8_1998_Financial_transaction_cards_--_Security_arc.htm)
  - Security,
- [ISO JTC1 SC37 1.37.19784.1 BioAPI - Biometric Application Programming Interface](../New_Technologies/Tech_ISO_JTC1_SC37_1_37_19784_1_BioAPI_-_Biometric_Application_Pr.htm)
  - Security,
- [ISO JTC1 SC37 1.37.19794 - Biometric Data Interchange Format](../New_Technologies/Tech_ISO_JTC1_SC37_1_37_19794_-_Biometric_Data_Interchange_Format.htm)
  - Security,
- [ISO JTC1 SC37 1.37.19794.3 Biometric Data Interchange Format - Part 3: Finger Pattern Spectral Data](../New_Technologies/Tech_ISO_JTC1_SC37_1_37_19794_3_Biometric_Data_Interchange_Format.htm)
  - Security,
- [ISO JTC1 SC37 1.37.19794.4 Biometric Data Interchange Format - Part 4: Finger Image Data](../New_Technologies/Tech_ISO_JTC1_SC37_1_37_19794_4_Biometric_Data_Interchange_Format.htm)
  - Security,
- [ISO JTC1 SC37 1.37.1974.5 Biometric Data Interchange Format - Part 5: Face Image Data](../New_Technologies/Tech_ISO_JTC1_SC37_1_37_1974_5_Biometric_Data_Interchange_Format_.htm)
  - Security,

### Federal Documents on Security Technologies

- - Security,
- [FIPS 197 Federal Information Processing Standards Publication 197, Specification for the Advanced Encryption Standard (AES)](../New_Technologies/Tech_FIPS_197_Federal_Information_Processing_Standards_Publicatio.htm)
  - Security,

### IETF Internet Requests for Comments (RFCs) on Security Technologies

- [RFC 1004 Distributed-protocol authentication scheme](../New_Technologies/Tech_RFC_1004_Distributed-protocol_authentication_scheme.htm)
  - Security,
- [RFC 1352 SNMP Security Protocols](../New_Technologies/Tech_RFC_1352_SNMP_Security_Protocols.htm)
  - Network Management,
- [RFC 1507 DASS - Distributed Authentication Security Service](../New_Technologies/Tech_RFC_1507_DASS_-_Distributed_Authentication_Security_Service.htm)
  - Security,
- [RFC 1579 Firewall-Friendly FTP](../New_Technologies/Tech_RFC_1579_Firewall-Friendly_FTP.htm)
  - Security,
- [RFC 1826 IP Authentication Header](../New_Technologies/Tech_RFC_1826_IP_Authentication_Header.htm)
  - Security,
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
- [RFC 2356 Sun's SKIP Firewall Traversal for Mobile IP](../New_Technologies/Tech_RFC_2356_Sun's_SKIP_Firewall_Traversal_for_Mobile_IP.htm)
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
- [RFC 2817 Upgrades to TLS within HTTP/1.1](../New_Technologies/Tech_RFC_2817_Upgrades_to_TLS_within_HTTP-1_1.htm)
  - Security,
- [RFC 2818 HTTP over TLS (HTTPS)](../New_Technologies/Tech_RFC_2818_HTTP_over_TLS_(HTTPS).htm)
  - Security,
- [RFC 2865 Remote Authentication Dial In User Service (RADIUS)](../New_Technologies/Tech_RFC_2865_Remote_Authentication_Dial_In_User_Service_(RADIUS).htm)
  - Security,
- [RFC 2869 RADIUS Extensions](../New_Technologies/Tech_RFC_2869_RADIUS_Extensions.htm)
  - Security,
- [RFC 2874 DNS Extensions to Support IPv6 Address Aggregation and Renumbering](../New_Technologies/Tech_RFC_2874_DNS_Extensions_to_Support_IPv6_Address_Aggregation_.htm)
  - Security,
- [RFC 2875](../New_Technologies/Tech_RFC_2875_.htm) 
  - Security,
- [RFC 2898 PKCS #5: Password-Based Cryptography Specification Version 2.0](../New_Technologies/Tech_RFC_2898_PKCS_5__Password-Based_Cryptography_Specification_V.htm)
  - Security,
- [RFC 2946 Telnet Data Encryption Option](../New_Technologies/Tech_RFC_2946_Telnet_Data_Encryption_Option.htm)
  - Security,
- [RFC 2977 Mobile IP Authentication, Authorization, and Accounting Requirements](../New_Technologies/Tech_RFC_2977_Mobile_IP_Authentication,_Authorization,_and_Accoun.htm)
  - Security,
- [RFC 2979 Behavior of and Requirements for Internet Firewalls](../New_Technologies/Tech_RFC_2979_Behavior_of_and_Requirements_for_Internet_Firewalls.htm)
  - Security,
- [RFC 2985 PKCS #9: Selected Object Classes and Attribute Types Version 2.0](../New_Technologies/Tech_RFC_2985_PKCS_9__Selected_Object_Classes_and_Attribute_Types.htm)
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
- [AGA-12 Cryptographic Protection of SCADA Communications General Recommendations.](../New_Technologies/Tech_AGA-12_Cryptographic_Protection_of_SCADA_Communications_Gene.htm)
  - Security,
- [ANSI INCITS 359-2004 Role Based Access Control (RBAC)](../New_Technologies/Tech_ANSI_INCITS_359-2004_Role_Based_Access_Control_(RBAC).htm)
  - Security,
- [EPRI 1002596 ICCP TASE.2 Security Enhancements](../New_Technologies/Tech_EPRI_1002596_ICCP_TASE_2_Security_Enhancements.htm)
  - Security,
- [NIST GSC-IS The NIST Interagency Report 6887 - 2003 edition (Government Smart Card-Interoperability Specification) Version 2.1](../New_Technologies/Tech_NIST_GSC-IS_The_NIST_Interagency_Report_6887_-_2003_edition_.htm)
  - Security,
- [NISTIR 6529 Common Biometric File Format (CBEFF)](../New_Technologies/Tech_NISTIR_6529_Common_Biometric_File_Format_(CBEFF).htm)
  - Security,
- [Smart Card Alliance Smart Card Primer](../New_Technologies/Tech_Smart_Card_Alliance_Smart_Card_Primer.htm)
  - Security,
- [Smart Card Alliance Privacy and Secure Identification Systems: The Role of Smart Cards as a Privacy-Enabling Technology](../New_Technologies/Tech_Smart_Card_Alliance_Privacy_and_Secure_Identification_System.htm)
  - Security,
- [Smart Card Alliance Government Smart Card Handbook](../New_Technologies/Tech_Smart_Card_Alliance_Government_Smart_Card_Handbook.htm)
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

## 

---

# Possible Technologies

### Networking Technologies

- [Intermediate System to Intermediate System (ISIS) Routing Protocol](../New_Technologies/Tech_Intermediate_System_to_Intermediate_System_(ISIS)_Routing_Pr.htm)
  - Configuration,
- [Routing Information Protocol (RIP)](../New_Technologies/Tech_Routing_Information_Protocol_(RIP).htm)
  - Configuration,

### Application Layer Protocols

- [CSV files](../New_Technologies/Tech_CSV_files.htm)
  - Data Management

## 

## 

## 

## 

## 

## 

## 

## 

##
