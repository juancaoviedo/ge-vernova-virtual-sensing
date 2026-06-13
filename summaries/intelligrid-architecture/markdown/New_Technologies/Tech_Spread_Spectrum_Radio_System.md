# Spread Spectrum Radio System

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Spread_Spectrum_Radio_System.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Spread Spectrum Radio System

**URL:**http://www.conformity.com/0008emc1.html  
http://grouper.ieee.org/groups/802/11/main.html  
http://www.sss-mag.com/ss.html

To avoid having to operate with allocated frequencies
from the FCC, a different type of radio known as spread spectrum (SS) radio is
used in point to multipoint radio systems. The configuration of the master and
remote radios is exactly the same as that for the MAS. The only difference is
that FCC Part 15 Rules allow these radios to operate without the need for a
license in the 902-928MHz frequency band. To meet the FCC criteria, the radios
must operate at low power and must continually hop over a range of frequencies
(typically 64 or more), staying on one frequency only for a short fixed period
(typically 250 ms). Special processing built into the radio allows the radio to
recover data in its original format while continually changing frequencies.

Two spread spectrum modulation techniques are
commonly used to achieve spread spectrum. One technique uses the direct
sequence method in which the carrier is modulated by a digital code that runs
much faster than the modulation rate. With digital data, this means that each
bit of data can be spread over a wide frequency band, resulting in less power
and a more limited transmission range of typically 3 to 5 miles. The other
technique uses the frequency hopping method in which a digital code also moves
a carrier but it runs much slower than the modulation rate. Thus, frequency
hopping allows a block of data to be transmitted in the span of, say, 250
milliseconds on one frequency before it switches to another frequency.

When SS radio is used for MAS type application, the
coverage is often less because of the low power restriction. Line-of-sight is
still required for optimal coverage. However, the ability to operate with
unlicensed frequencies is very attractive to potential users because it allows
installation to be done quickly without licensing delay. For this reason, SS
radio is often used as last-mile connections to a main communication system
and, in such an application, the line-of-sight requirement is not as stringent
and reliable communication can be achieved even if trees, buildings or terrain
obstruct the path. However, each obstruction does reduce the RF (radio
frequency) strength. When operating in the unlicensed spread spectrum band,
interference is considered normal because there will be many users using the
same frequencies. The primary effect is somewhat lower communication
throughput. A number of remedies can be used to improve radio
performance.

**Main Features of Technology**

|  |  |
| --- | --- |
| Technology | Radio |
| Frequency | 900 MHz  range or 2.4 GHz  range |
| Bandwidth | 12.5kHz  for 900MHz,  20MHz  for 2.4GHz |
| Operation | In point-to-multipoint configuration, one master radio can poll multiple remote radios but can also operate point-to-point (last mile connection) |
| Capacity | Limited by data rate and system scan time (same as MAS) |
| Coverage | 5-8 km for direct sequence spread spectrum radio, 16-24 km for frequency hopping spread spectrum radio, can be extended by using repeaters |
| Data rate | Up to 19.2Kbps for 900MHz radio, T1/E1 (1.544Mbps/2.408Mbps) for 2.4GHz radio |
| No. of Channels | Typically 50 or more |
| Multiplexing/modulation method | Spreading of frequencies by direct sequence or frequency hopping techniques |
| Modulation | OQPSK (offset quadrature phase shift keying) |
| Power | low 0.1W  to 1W |
| Regulatory | No licensing required for frequencies but directional antenna gain, antenna height, number of hopping frequencies and max. dwell time on each frequency are regulated |

**Key Advantages**

|  |  |
| --- | --- |
| Capacity | In point-to-multipoint system, one master radio can poll multiple remote radios and capacity is limited only by data speed and system scan time |
| Coverage | 5-8 km or 16-24 km |
| Data rate | Up to 19.2Kbps for 900 MHz, T1 or E1 for 2.4GHz |
| Reliability | Increased by choosing unobstructed transmission path, using redundant hardware, loop-back diagnostics and forward error correction code |
| Interference | Designed to operate in environment where interference exists. Interference to others is limited by low power and frequent frequency changes |
| Security | Spread spectrum techniques provide significant security against eavesdropping, replay, spoofing, denial of service, and interception of information |
| Regulatory | No licensing required in USA |
| Cost | Relatively low |

**Key Disadvantages**

|  |  |
| --- | --- |
| Operation | Line-of-sight makes medium prone to obstruction but some obstruction can be tolerated |
| Coverage | More limited in distance when compared to MAS and microwave |

**Keywords:** wireless, LAN, frequency hopping, direct sequence,
