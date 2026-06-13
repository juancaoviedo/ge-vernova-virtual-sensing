# Permanent PQ

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_PQ_Perrmantent_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Permanent Power Quality (PQ) Function

## Contents

* [Narrative](CS_PQ_Perrmantent_Use_Case.htm#Narrative)
* [Steps](CS_PQ_Perrmantent_Use_Case.htm#Steps)

## Narrative

The purpose of the permanent power quality
measurement enterprise activity is to provide long-term and
continuous monitoring in order to provide reliability and
benchmarking statistics.

Many customers which can include utilities and
large consumers of electric power have a need for an installed
permanent power quality measurement system.  Historically, power
quality meters were portable and installed on a temporary basis in
order to capture, diagnose, and solve a specific problem that might be
occurring in the facility.  However, with increased demands for power
quality and reliability benchmarking, power quality contracts, billing
and energy use verification, predictive maintenance and others, the
need and demand for permanent power quality monitoring has increased
dramatically in recent years.

The following is a typical scenario.  An electric
utility realizes the need for a permanently installed power quality
measurement system.  The reason could be new standards from the state
PUC or competitive threats or even just to keep existing customers
happy.  In addition, the utility could be implementing power quality
contracts and needs a mechanism to verify performance.  A utility will
then generally procure and install monitors at various locations.  The
locations could be statistically selected or just placed at key
customer locations.  Once the instruments are installed, it will be
necessary to establish communication from a central location to the
instruments.  At the central server location, there will generally be
two types of applications.  The first is the downloading application
that uses the communication medium selected and is used to setup and
download the data from the instruments in the field.  This requires
communication from the central server location to the monitoring
instrument either by telephone, Internet, satellite or other. 
Typically this is done on a daily basis or after a significant event
occurs.  The instrument captures and stores event data in standard or
proprietary form inside instrument.  Optional gateway device downloads
event data from instrument, converts it to a standardized format (IEEE
1159.3 PQDIF), and stores until downloaded by enterprise system. 
Enterprise system downloads data from the instrument or gateway,
converts to standard format if necessary, and puts in standardized
file hierarchy (IEEE 1159.3 PQDIF Annex C) and/or a commercial power
quality database (e.g. PQView). The second application resides on the
central server and is usually a database application that is used to
characterize, store and report results from the data collection.  The
central server also typically acts as a web server and is used to
supply data over corporate intranets or the internet itself.

if !vml?![](CS_PQ_Perrmantent_Use_Case_files/image001.gif)endif?

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Site Selection and Installation | Site Selection and Installation | Customer selects sites for permanently installed power quality monitors and installs them | Customer | Customer | Site Selection |  | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.2 | Event Capture | Event Capture | If thresholds are exceeded the power quality instrument captures and records and event | Power Quality Instrument | Power Quality Instrument | Raw power quality event data |  | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 1.3 | Event Transmittal | Event Transmittal | If an event is triggered, the instrument calls back to the central server and the server downloads the data | Power Quality Instrument | Central Server | Raw power quality event data | Basic telecommunication constraints such as modem and dial up telephone connection, but could also include internet TCP/IP connectivity or even cellular | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.4 | Data Storage, Characterization and Reporting | Data Storage and Characterization | Based on events recorded, data is characterized and loaded into a database and reports are generated | Central Server | Customer | Data report that includes a sag score | Data management in terms of culling important information | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
