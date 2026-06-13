# Data over Voice Lines

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Data_over_Voice_Lines.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Data over Voice Lines

**URL:**http://www2.rad.com/networks/1994/modems/modem.htm  
http://www.techtutorials.info/hdmodems.html  
http://www.rad.com/RADCnt/MediaServer/3656\_ldv-2.pdf  
http://www.vocal.com/data\_sheets/v925.html

Voice-grade telephone connections (standard 3 kHz
voice circuits) are made either by dialing by the user or by being wired in the
telephone company's central office and remain connected until the service is
discontinued. The latter kind is called a private line, leased line or
dedicated line. The user usually pays a fixed fee every month for this service.
The leased line is a point-to-point circuit, with both end points identified to
the telephone company. The user has no knowledge of where or how the circuit is
routed between the two end-points, unless the telephone company is specifically
requested to provide diversity for security and availability purposes.

Point-to-point circuits are cost effective for
high-speed communication between two devices, but are more expensive when
compared to dial-up applications where the circuit is connected and charged
only for the duration of the connection. Low speed point-to-point voice-grade
circuits are known in the industry as 3002 circuits. Voice-grade circuits can
carry uncompressed data from the slowest speed up to 19.2 kbps. Higher speeds
(up to 56 kbps) can be carried with data compression.

Digital circuits or Digital Data Services (DDS) can
carry data at 2.4, 4.8, 9.6, 19.2, 56, and 64Kbps. Digital circuits are not
technically voice-grade, but they can be used to carry either voice or data.
Slow speed leased lines have been used extensively by utilities to provide
quick connections to various facilities and devices that cannot otherwise be
reached in a structured network or telecommunications scheme.

**Main Features of Technology**

|  |  |
| --- | --- |
| Technology | 3 kHz bandwidth telephone voice circuit |
| Operation | Low speed, limited by bandwidth and circuit quality |
| Capacity | Usually dedicated to one modem per line for most applications, but multi-drop connections to multiple RTUs are common |
| Coverage | As far as phone company phones lines can reach |
| Data rate | Up to 64kbps with special line conditioning |
| Power | Terminal equipment to provide |
| Regulatory | None required |

**Key Advantages**

|  |  |
| --- | --- |
| Coverage | Telephone company circuits reach most locations within the United States and can be installed rapidly |
| Maintenance | Telephone company provides all maintenance |
| Interference | Phone company usually guarantees the performance of the line |
| Availability | Phone company usually guarantees the availability of the line along with time to repair |
| Security | Each line is dedicated and not shared with others, but eavesdropping is relatively easy |
| Cost | Phone company is responsible for the line, so no installation and maintenance costs |

**Key Disadvantages**

|  |  |
| --- | --- |
| Reliability/availability | User has no control over line reliability and availability. Situation has worsened since de-regulation because a single line may have multiple carriers, which makes it difficult to trouble-shoot problems and hold one carrier responsible |
| Data rate | Low data rates |
| Cost | Recurring charges, high installation cost if remote site does not have nearby phone facility |

**Keywords:** Physical layer

#### Digital Subscriber Line (DSL) Technologies

**URL:**http://www.dslforum.org/  
http://www.t1.org/t1e1/t1e1.htm

ADSL was first standardized in 1995 by the American
National Standards Institute as T1.413, and then by the ITU in 1999 as G.992.1.
ADSL can transmit data at speeds up to 8 megabits per second ("Mbps")
downstream and up to 640 Kbps upstream. In 1999, the ITU also standardized a
lower speed version of ADSL, known as G.Lite or G.992.2. G.Lite can transmit
data at speeds up to 1.5 Mbps downstream and up to 512 Kbps upstream without
using special filtering equipment required by full-rate ADSL.

In 2002, the ITU standardized a new family of ADSL
standards known as ADSL2 or G.992.3 and G.992.4. These standards provide
numerous improvements over previous ADSL standards, including line diagnostics,
power management, power cutback, reduced framing, and on-line reconfiguration.
In January 2003, the ITU standardized an extension of ADSL2 known as ADSL2+ or
G.992.5. ADSL2+ builds upon the ADSL2 standard by increasing achievable data
rates to speeds of up to 25 Mbps upstream on phone lines as long as 3,000 feet
(20 Mbps out to 5,000 feet). Reach-Extended ADSL2 (RE-ADSL2) - the new ADSL2
Annex L standard - was ratified by the ITU in October 2003. Annex L proposes
new power spectral density (PSD) masks that can result in a significant
increase in ADSL's reach.

The DSL Forum is a consortium of networking,
computing, and service provider companies that promote the development and
worldwide acceptance of the Digital Subscriber Line family of technologies.

Committee T1 is sponsored by the Alliance for
Telecommunications Industry Solutions (ATIS) and accredited by the American
National Standards Institute (ANSI) to create network interconnections and
interoperability standards for the United States. Within T1, T1E1 is concerned
with Interfaces, Power, and Protection of networks. The T1E1.4 working group
(DSL Transmission) addresses high-speed bi-directional digital transport via
metallic facilities. The work of this group focuses on the physical layer
transceiver functionality.
