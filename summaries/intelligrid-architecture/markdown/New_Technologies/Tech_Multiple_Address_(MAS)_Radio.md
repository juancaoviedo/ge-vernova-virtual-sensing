# Multiple Address (MAS) Radio

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Multiple_Address_(MAS)_Radio.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Multiple Address (MAS) Radio

**URL:**http://www.micronetcom.com/mas.htm

MAS radio has gained
popularity in recent years due to its flexibility, reliability and compact
size. A basic MAS radio link consists of a master radio transmitter/receiver
unit and multiple remote radio transmitter/receiver units. A master unit can
access or poll multiple units via a pair of transmit/receive frequencies. The
master unit is set up always ready to transmit and receive in order to keep
delay due to transmitter keying to a minimum. Each remote unit is set up always
in the listening mode until it is polled and then ready to transmit. Each
remote unit has a unique address so no two units will try to answer the poll at
the same time. This eliminates any contention among the remotes to transmit to
the master. The frequency pair used by MAS requires to be licensed by the FCC
and the same pair can be re-used elsewhere in the system as long as it does not
cause any interference.

For performance reasons, there is a limit to the
number of remotes that can be polled by one master radio. This limit is
determined by the time delay in the poll and the handshaking required in the
response, the data transmission rate and the data collection time set by the
system. So, for a large service area, many master radios will need to be used
to cover groups of remote units each located in or near a utility owned
facility. For difficult-to-reach locations due to topography or limitation of
line-of-sight, the same MAS radio can be used as a repeater radio to allow
signal transmission over or around large obstructions.

Typically each master radio is located at a site
where there is an existing connection to the utility’s control center where
data is collected for the entire system. This can be a microwave site or fiber
optic network node in a network. MAS radio is the
preferred communication medium and has been used widely by utilities for SCADA
(supervisory control and data acquisition) systems and DA (distribution
automation) systems.

**Main Features of Technology**

|  |  |
| --- | --- |
| Technology | Radio |
| Frequency | 895 to 960 MHz transmit/receive frequency pair |
| Bandwidth | 25kHz for existing frequencies, 12.5kHz for new frequencies |
| Operation | Requires line-of-sight, point-to-multipoint for master and remote radios |
| Capacity | Can be expanded by using more master radios, but will be limited by how fast remotes can be polled and system scan period allowed |
| Coverage | Each link is typically 15km |
| Data rate | Up to 4.8kbps, can be increased to 9.6Kbps but coverage will be reduced |
| No. of channels | Minimum separation between adjacent channels is 25kHz for previous frequency allocations and 12.5KHz for new frequency allocations |
| Multiplexing/modulation method | Frequency shift keying (FSK) |
| Power | 5W master, 1W remote |
| Regulatory | Frequency licensing required |

**Key Advantages**

|  |  |
| --- | --- |
| Capacity | Capacity is limited by data speed and system scan time. Also, limited by the number of masters that can be physically installed in the system (location, topography, etc.) |
| Coverage | Can typically reach 15 km, can be extended by using repeaters |
| Data rate | Up to 9.6kbps (with reduced coverage) |
| Reliability | Can be improved with remote diagnostics, warm standby equipment and redundant architecture |
| Interference | Licensed frequencies provide some protection against interference by others |
| Cost | Relatively low |

**Key Disadvantages**

|  |  |
| --- | --- |
| Operation | Line-of-sight to remotes prone to obstruction |
| Regulatory | Licensing is time consuming and may not be possible due to lack of available frequencies |

**Keywords:** Wireless, LAN
