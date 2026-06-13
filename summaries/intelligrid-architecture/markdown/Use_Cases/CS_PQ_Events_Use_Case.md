# PQ Event Notifications

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/CS_PQ_Events_Use_Case.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Customer Services - Power Quality (PQ) Event Notifications Function

## Contents

* [Narrative](CS_PQ_Events_Use_Case.htm#Narrative)
* [Steps](CS_PQ_Events_Use_Case.htm#Steps)

## Narrative

The purpose of the power quality event
notifications enterprise activity is to enable a mechanism whereby
stakeholders are alerted as soon as possible to the location, time
and severity of power quality events that occur.

Power quality event capture instruments can be
installed anywhere on the electric power grid including transmission
substations all the way down to end-use customer facilities.  After an
event capture there are generally two methods employed to notify
stakeholders that an event has occurred.  The first method is an
“on-the-fly” approach, near real-time.  When an event is captured, if
it exceeds pre-set thresholds for notifications, then an email or page
is immediately sent to a list of recipients.  Generally, these emails
or pages will list the time, magnitude and severity.  In the case of
some instrument manufacturers, a link is given to go back and view the
event and in some cases, the event is embedded in the actual email
message.

The other form of event notification is
“after-the-fact” or post-processed.  In this method, the data is
collected and then processed by a central server or other type of
application that is looking for events that exceeded thresholds.  In
this case, the central server application then sends out emails or
pages to a list of recipients.  This method has time lag built in
because in some instances, data is downloaded only daily and messages
are sent after the data is post-processed.  Some instruments after and
event is captured, will call back to the central server to let the
server know, they should download data, reducing the time lag.

Key communication occurs between the instruments
to pager vendor and ISPs and from the instruments to the central
server and then similarly from the central server out to pager vendor
and ISPs or internal mail servers.

if !vml?![](CS_PQ_Events_Use_Case_files/image002.gif)endif?

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Event Capture | Event Capture | If voltage and/or current thresholds are exceeded, the power quality instrument records and event | Power Quality Instrument | Instrument | Voltage and current waveforms and other power quality data |  | [Inter-Field Equipment](../Environments/Env4_Inter-Field_Equipment.htm) |
| 1.2A.1 | Instrument Event Notification | Instrument Event Notification | If an event is triggered, the instrument sends out pages and/or emails to stakeholder recipients | Power Quality Instrument | Customer | PQ Event data and/or summary data including date, time, magnitude, duration, etc. | Basic telecommunication constraints such as modem and dial up telephone connection, but could also include internet TCP/IP connectivity or even cellular | [Intra-Customer Site](../Environments/Env16_Intra-Customer_Site.htm) |
| 1.2B.1 | Event Transmittal | Event Transmittal | After an event is triggered, the instrument calls back to the central server and the server downloads the data | Power Quality Instrument | Central Server | Voltage and current waveforms and data | Basic telecommunication constraints such as modem and dial up telephone connection, but could also include internet TCP/IP connectivity or even cellular | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |
| 1.2.B.2 | Server Event Notification | Server Event Notification | After the central server software processes the event data, pages and/or emails are sent out to stakeholders | Central Server | Customer | PQ Event data and/or summary data including date, time, magnitude, duration, etc. | Basic telecommunication constraints such as modem and dial up telephone connection, but could also include internet TCP/IP connectivity or even cellular | [ESP to Customer](../Environments/Env18_Customer_to_ESP.htm) |

if !supportEndnotes?  
 endif?
