# Digital Signal (DSx), Time-division multiplexing, the T-carriers, T1, fractional T1

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Digital_Signal_(DSx),_Time-division_multiplexing,_the_T-carr.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Digital Signal (DSx), Time-division multiplexing, the T-carriers, T1, fractional T1

**URL:**http://www.itu.int  
http://www.itu.int

Digital signal X is based on the ANSI T1.107
guidelines. Digital Signal X is a term for the series of standard digital
transmission rates or levels based on DS0, a transmission rate of 64 Kbps, the
bandwidth normally used for one telephone voice channel. Both the North
American T-carrier system and the European E-carrier systems of transmission
operate using the DS series as a base multiple. The digital signal is what is
carried inside the carrier system, typically via time division multiplexing.
DS0 is the base for the digital signal X series. DS1, used as the signal in the
T-1 carrier, is 24 DS0 (64 Kbps) signals transmitted using pulse-code
modulation (PCM) and time-division multiplexing (TDM). DS2 is four DS1 signals
multiplexed together to produce a rate of 6.312 Mbps. DS3, the signal in the
T-3 carrier, carries a multiple of 28 DS1 signals or 672 DS0s or 44.736 Mbps.
Telecom companies have developed transmission services which are essentially a
T1 line with some of the channels turned off. This is to target towards the
niche of cost-sensitive customers. Typical speeds for fractional T1's are 256,
384, 512 and 768kbps.

**Main Features of Technology**

|  |  |
| --- | --- |
| Technology | Frame based transmission over high-speed T1 circuits. Equivalent to X.25 without network layer functions (node-to-node error checking) |
| Operation | Allows customers to select port speed and request permanent virtual circuit (PVC) with committed information rate (CIR) |
| Bandwidth | Amount of bandwidth is adjusted to meet application, but limited |
| Capacity | Up to capacity of T1 and multiple T1s |
| Coverage | Same as that provided by LECs (local exchange carriers) |
| Data rate | For each customer, port speed and CIR from  16Kbps to 256Kbps or higher, up to the limit of the T1 or fractional T1 installed |
| No. of channels | PVC , typically 64 channels per T1 |
| Regulatory | None |

**Key Advantages**

|  |  |
| --- | --- |
| Capacity | Multiple T1s can be provided rapidly by telecommunications providers |
| Coverage | Very broad coverage for most areas, as provided by LEC |
| Data rate | Committed information rate (CIR) |
| Access | Faster network access without latency resulting from node-to-node error checking (in X.25 network) |

**Key Disadvantages**

|  |  |
| --- | --- |
| Cost | Cost of local access circuit can be high if the location of the carrier’s POP (point-of-presence) is not in the same city |
| Access | End devices need to perform error checking and request for re-transmission should error be found. This may slow down overall data transmission  Network congestion may cause frames to be discarded and will require re-transmission. |

**Keywords:** time division multiplexing, digital signal hierarchy, transmission.
