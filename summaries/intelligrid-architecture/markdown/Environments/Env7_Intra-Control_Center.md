# Env7 Intra-Control Center

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Environments/Env7_Intra-Control_Center.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Intra-Control Center Environment - #7

if !vml?![](Env7_Intra-Control_Center_files/image002.gif)endif?This
environment represents communications between modules of a single
control center, typically over a local area network within a single
physical building.

**Typical Applications:** Updating databases
and human-machine interfaces with data gathered from the “front-end
processors” within Energy Management Systems (EMSs) or Distribution
Management Systems (DMSs).

**Characteristics:**  Located in a very
secure and reliable physical environment, but with a huge amount of
data to manage and distribute between a variety of platforms and
database technologies.  Updates must happen in at least human response
times for some data.

**Similar Environments:** This environment
carries ALL the data brought in via High Security DAC or Low Security
DAC, but need not be transmitted in as reliable a format.  Carries
similar types of data as when the control center communicates with
other businesses (CC/ESP, CC/Customer Equipment, or CC/corporations). 
However, the real-time requirements are tighter, security is nowhere
near as important, and data formats tend to be proprietary for
performance reasons.

**Definition:**  This environment is defined
by the following requirements:

.

---

# Communication and Information Requirements that Define this Environment

## Configuration Requirements

* Support peer to peer interactions
* Support interactions within a contained environment (e.g. substation or control center)

## Quality of Service Requirements

* Support high availability of information flows of 99.9+ (~9 hours)
* Support time synchronization of data for age and time-skew information

## Security Requirements

* Provide Authorization Service for Access Control (resolving a policy-based access control decision to ensure authorized entities have appropriate access rights and authorized access is not denied)
* Provide Audit Service (responsible for producing records, which track security relevant events)
* Provide Security Policy Service (concerned with the management of security policies)
* Provide User Profile and User Management (combination of several other security services)

## Network and System Management Requirements

* Provide Network Management (management of media, transport, and communication nodes)
* Provide System Management (management of end devices and applications)

## Data Management Requirements

* Support the management of large volumes of data flows
* Support keeping the data up-to-date
* Support extensive data validation procedures
* Support keeping data consistent and synchronized across systems and/or databases
* Support timely access to data by multiple different users
* Support frequent changes in types of data exchanged
* Support management of data whose types can vary significantly in different implementations
* Support specific standardized or de facto object models of data
* Support the exchange of unstructured or special-format data (e.g. text, documents, oscillographic data)
* Provide discovery service (discovering available services and their characteristics)
* Provide conversion and protocol mapping

---

# Recommended Technologies

## Energy Industry-Specific Technologies

### Utility Field Device Related Data Exchange Technologies

- [IEC61850 Part 6 - Substation Configuration Language](../New_Technologies/Tech_IEC61850_Part_6_-_Substation_Configuration_Language.htm)
  - Network Management, Data Management

### Utility Control Center Related Data Management Technologies

- [IEC 60870-6 (ICCP)](../New_Technologies/Tech_IEC_60870-6_(ICCP).htm)
  - Configuration,
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

- [IEEE 802 MAC Addresses](../New_Technologies/Tech_IEEE_802_MAC_Addresses.htm)
  - Configuration,
- [Asynchronous Transfer Mode (ATM)](../New_Technologies/Tech_Asynchronous_Transfer_Mode_(ATM).htm)
  - Configuration,

### Wireless Technologies

- [Global Positioning System (GPS)](../New_Technologies/Tech_Global_Positioning_System_(GPS).htm)
  - Quality of Service, Data Management

### Computer Systems Related Technologies

- [CORBA and CORBA Services](../New_Technologies/Tech_CORBA_and_CORBA_Services.htm)
  - Data Management
- [Web Services](../New_Technologies/Tech_Web_Services_.htm) 
  - Data Management
- [Universal Description, Discovery, and Integration (UDDI)](../New_Technologies/Tech_Universal_Description,_Discovery,_and_Integration_(UDDI).htm)
  - Data Management
- [XML Protocol/Simple Object Access Protocol (SOAP)](../New_Technologies/Tech_XML_Protocol-Simple_Object_Access_Protocol_(SOAP).htm)
  - Data Management
- [Enterprise Java Beans (EJB)](../New_Technologies/Tech_Enterprise_Java_Beans_(EJB).htm)
  - Data Management
- [IEEE 1588 Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems](../New_Technologies/Tech_IEEE_1588_Standard_for_a_Precision_Clock_Synchronization_Pro.htm)
  - Quality of Service,
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
- [XSLT](../New_Technologies/Tech_XSLT.htm)
  - Data Management
- [XQuery](../New_Technologies/Tech_XQuery.htm)
  - Data Management
- [ANSI/ISO/IEC 9075 - Structured Query Language (SQL)](../New_Technologies/Tech_ANSI-ISO-IEC_9075_-_Structured_Query_Language_(SQL).htm)
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

- [Role-Based Access Control](../New_Technologies/Tech_Role-Based_Access_Control.htm)
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
- [AGA-12 Cryptographic Protection of SCADA Communications General Recommendations](../New_Technologies/Tech_AGA-12_Cryptographic_Protection_of_SCADA_Communications_Gene.htm)
  - Security,

### Transport Layer Security Technologies

- [Transport Layer Security (TLS)/Secure Sockets Layer (SSL)](../New_Technologies/Tech_Transport_Layer_Security_(TLS)-Secure_Sockets_Layer_(SSL).htm)
  - Security,

### Application Layer Security Technologies

- [SNMP Security](../New_Technologies/Tech_SNMP_Security.htm)
  - Security, Network Management,
- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
  - Quality of Service, Security, Data Management
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
- [Security Policies](../New_Technologies/Tech_Security_Policies.htm)
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

- [Distributed Data Management Service](../New_Technologies/Tech_Distributed_Data_Management_Service.htm)
  - Data Management
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
- [Network Time](../New_Technologies/Tech_Network_Time.htm)
  - Data Management
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
- [Checkpoint and Recovery](../New_Technologies/Tech_Checkpoint_and_Recovery.htm)
  - Network Management,
- [Workflow Service](../New_Technologies/Tech_Workflow_Service.htm)
  - Network Management,

---

# Recommended Best Practices

## Data Management Best Practices

### Data Management

- [Backup Data Sources](../New_Technologies/Tech_Backup_Data_Sources.htm)
  - Quality of Service,
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
- [Management of Data Consistency and Synchronization across Systems](../New_Technologies/Tech_Management_of_Data_Consistency_and_Synchronization_across_Sy.htm)
  - Data Management
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
- [Data Consistency across Multiple Systems](../New_Technologies/Tech_Data_Consistency_across_Multiple_Systems.htm)
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
  - Quality of Service, Data Management
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

### Application Layer Protocols

- [Microsoft COM+](../New_Technologies/Tech_Microsoft_COM+.htm)
  - Data Management

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

### Wireless Technologies

- [IEEE 802.11 Wireless Local Area Network (WLAN)](../New_Technologies/Tech_IEEE_802_11_Wireless_Local_Area_Network_(WLAN).htm)
  - Configuration,
- [IEEE 802.15 Wireless Personal Area Network (PAN)](../New_Technologies/Tech_IEEE_802_15_Wireless_Personal_Area_Network_(PAN).htm)
  - Configuration,
- [Bluetooth Special](../New_Technologies/Tech_Bluetooth_Special.htm)
  - Configuration,
- [Radio Frequency Identification (RFID)](../New_Technologies/Tech_Radio_Frequency_Identification_(RFID).htm)
  - Data Management

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

- [Backup Sites](../New_Technologies/Tech_Backup_Sites.htm)
  - Quality of Service,

## 

## 

### ISO/IEC Documents on Security Technologies

- [ISO/IEC 7816-9:2000 Identification cards -- Integrated circuit(s) cards with contacts -- Part 9: Additional](../New_Technologies/Tech_ISO-IEC_7816-9_2000_Identification_cards_--_Integrated_circu.htm) 
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

### IETF Internet Requests for Comments (RFCs) on Security Technologies

- [RFC 1305 Network Time Protocol (Version 3) Specification, Implementation](../New_Technologies/Tech_RFC_1305_Network_Time_Protocol_(Version_3)_Specification,_Im.htm)
  - Quality of Service,
- [RFC 1352 SNMP Security Protocols](../New_Technologies/Tech_RFC_1352_SNMP_Security_Protocols.htm)
  - Network Management,
- [RFC 1940 Source Demand Routing: Packet Format and Forwarding Specification (Version 1)](../New_Technologies/Tech_RFC_1940_Source_Demand_Routing__Packet_Format_and_Forwarding.htm)
  - Network Management,
- [RFC 2086 IMAP4 ACL extension](../New_Technologies/Tech_RFC_2086_IMAP4_ACL_extension.htm)
  - Security,
- [RFC 2093 Group Key Management Protocol (GKMP) Specification](../New_Technologies/Tech_RFC_2093_Group_Key_Management_Protocol_(GKMP)_Specification.htm)
  - Security,
- [RFC 2230 Key Exchange Delegation Record for the DNS](../New_Technologies/Tech_RFC_2230_Key_Exchange_Delegation_Record_for_the_DNS.htm)
  - Security,
- [RFC 2244 ACAP -- Application Configuration Access Protocol](../New_Technologies/Tech_RFC_2244_ACAP_--_Application_Configuration_Access_Protocol.htm)
  - Security,
- [RFC 2246 The TLS Protocol Version 1.0](../New_Technologies/Tech_RFC_2246_The_TLS_Protocol_Version_1_0.htm)
  - Security,
- [RFC 2547 BGP/MPLS VPNs](../New_Technologies/Tech_RFC_2547_BGP-MPLS_VPNs.htm)
  - Network Management,
- [RFC 2764 A Framework for IP Based Virtual Private Networks](../New_Technologies/Tech_RFC_2764_A_Framework_for_IP_Based_Virtual_Private_Networks.htm)
  - Network Management,
- [RFC 2753 A Framework for Policy-based Admission Control](../New_Technologies/Tech_RFC_2753_A_Framework_for_Policy-based_Admission_Control.htm)
  - Security,
- [RFC 2797 Certificate Management Messages over CMS](../New_Technologies/Tech_RFC_2797_Certificate_Management_Messages_over_CMS.htm)
  - Security,
- [RFC 2898 PKCS #5: Password-Based Cryptography Specification Version 2.0](../New_Technologies/Tech_RFC_2898_PKCS_5__Password-Based_Cryptography_Specification_V.htm)
  - Security,
- [RFC 2977 Mobile IP Authentication, Authorization, and Accounting Requirements](../New_Technologies/Tech_RFC_2977_Mobile_IP_Authentication,_Authorization,_and_Accoun.htm)
  - Security,
- [RFC 3053 IPv6 Tunnel Broker](../New_Technologies/Tech_RFC_3053_IPv6_Tunnel_Broker.htm)
  - Network Management,
- [RFC 3280 Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](../New_Technologies/Tech_RFC_3280_Algorithms_and_Identifiers_for_the_Internet_X_509_P.htm)
  - Security,
- [RFC 3414 User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3)](../New_Technologies/Tech_RFC_3414_User-based_Security_Model_(USM)_for_version_3_of_th.htm)
  - Network Management,
- [RFC 3647 Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework](../New_Technologies/Tech_RFC_3647_Internet_X_509_Public_Key_Infrastructure_Certificat.htm)
  - Security,

### Other Security Technolog

- [IEEE 802.11b Web Encryption Protocol](../New_Technologies/Tech_IEEE_802_11b_Web_Encryption_Protocol.htm)
  - Security,
- [IEEE 802.11i Security for Wireless Networks](../New_Technologies/Tech_IEEE_802_11i_Security_for_Wireless_Networks.htm)
  - Security,
- [RSA PKCS #12 Personal Information Exchange Syntax Standard, version 1.0.](../New_Technologies/Tech_RSA_PKCS_12_Personal_Information_Exchange_Syntax_Standard,_v.htm)
  - Security,
- [OASIS Documents on Security Technologies](../New_Technologies/Tech_OASIS_Documents_on_Security_Technologies.htm)
  - Security,
- [WC3 XML Key Management Specification (XKMS 2.0) Bindings](../New_Technologies/Tech_WC3_XML_Key_Management_Specification_(XKMS_2_0)_Bindings.htm)
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
