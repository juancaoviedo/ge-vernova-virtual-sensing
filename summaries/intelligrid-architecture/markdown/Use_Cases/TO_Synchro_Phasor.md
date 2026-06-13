# Synchro Phasor

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Synchro_Phasor.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - Synchro Phasor Function

## Contents

* [Narrative](TO_Synchro_Phasor.htm#Narrative)
* [Steps](TO_Synchro_Phasor.htm#Steps)

## Narrative

This system provides synchronized and
time-tagged voltage and current phasor measurements to any protection,
control, or monitoring function that requires measurements taken from
several locations, whose phase angles are measured against a common,
system wide reference. This is an extension of simple phasor
measurements, commonly made with respect to a local reference. Present
day implementation of many protection, control, or monitoring
functions are hobbled by not having access to the phase angles between
local and remote measurements. With system wide phase angle
information, they can be improved and extended. The essential concept
behind this system is the system wide synchronization of measurement
sampling clocks to a common time reference.

In addition to providing synchronized
measurements, the synchro-phasor system distributes the measurements.
Voltages and currents are measured at many nodes throughout the power
grid. Any protection, control, or monitoring function can access
measurements from several nodes, either by subscribing to continuous
streams of data, or requesting snapshots as needed. In principle, any
function could request measurements from any node, though in practice
most functions require data from only a few nodes.

The following is an example of how
synchro-phasors can be used to perform digital current differential
fault protection for a two terminal transmission line. There are two
intelligent electronic devices, one at each terminal, taking samples
of currents from all three phases. Physically, the two terminals might
be any distance at all apart, ranging from a few miles to a thousand
miles, for example. It is wished to provide fault protection for the
transmission line by summing the phasor values of currents to
determine differential current. In order to do that, the two
intelligent electronic devices need to measure the phasor values
against the same time reference, and exchange the data with each
other. This can be done with synchro-phasors.

Each intelligent device in this example is both
a client and a server of synchro-phasors. As a server, it provides
synchro-phasors to its partner. As a client, it requires
synchro-phasors from its partner. It is a completely symmetric
situation. We will examine the example mostly from the point of view
of one of the terminals, call it A.

Terminal A requires a steady stream of phasors
for three phase currents from terminal B. In this particular case, it
is decided to compute phasors every ½ cycle of the power system
frequency, and to transmit them once per ½ cycle. To simplify things,
it is decided not to perform frequency tracking, but rather to base
the sampling frequency on absolute time. For this particular case, it
is decided that synchronization between any pair of measurements must
be within 10 microseconds in steady state, even though there are other
applications that require tighter synchronization, such as to within 1
microsecond. Transiently, much larger synchronization errors are
permitted, but each terminal requires an estimate of the least upper
bound of the synchronization error if it exceeds 10 microseconds.

For correct transient tracking, it is decided
that the sampling windows must be aligned. That is, the set of
sampling times for each phasor window must be the same at each
terminal: overlapping is not allowed. It is understood that there may
be some latency involved in the exchange of information, but it should
not exceed 24 milliseconds, for example. It is also recognized that
some data might get lost or corrupted. A certain amount of lost data
is acceptable. The amount is somewhat arbitrary, but experience has
shown that 2.5% lost data can be tolerated. For this application, it
is not necessary to retransmit the lost data, since more, up-to-date
data will be arriving shortly anyway. However, it is necessary to
inform the protection application, so that it can move on to the next
time slot. It is also recognized that sometimes, communications might
be down altogether.

The possibility of corrupted data is a fact of
life in this arena. Without even considering abnormal events such as
electrical interference from faults, many types of communications are
considered to be operating normally with a low, but non-zero bit error
rate. Unless some steps are taken, it is possible for bit errors to
corrupt the data being exchanged. For this application, corrupted data
must be detected and ignored, since incorrect data could very well
cause a false de-energization of a transmission line, and move one
step closer to a black out. Bad data is worse than no data at all. To
that end, protection engineers would either want to see at 32 bit
cyclic redundancy code protecting against corrupted data, or have some
other assurances that under a credible worst scenario, it would not be
expected that a corrupted phasor would sneak through more often than
once every 300 years.

During installation of the differential
protection scheme, the two terminals are identified to each other, and
various parameters are selected, including those that impact the
exchange of synchro-phasors. There are GPS receivers at both
substations that can be used for sampling synchronization, so the
intelligent devices are configured to synchronize to the GPS clock.
(That is not always the case.) In this case, the GPS receivers are not
deemed reliable enough, so a backup strategy is required in which the
intelligent devices can synchronize to other clocks in the network
using the network time protocol. Also, the system engineers do not
completely trust digital communications, so they insist on two
physically independent communications channels between the pair of
terminals. That way, the system can continue to provide protection if
only one of the communications channels fails.

During commissioning, the two intelligent
devices are connected to their GPS clocks and checked out. Various
tests are run successfully off-line. The devices are then
re-initialized in an on-line mode.

During re-initialization of terminal A, the
synchro-phasor service synchronizes the local sampling clock to the
GPS clock, and turns on the calculation of synchronized phasors.
Terminal A then attempts to connect with terminal B, which in this
scenario, has not been initialized yet, so terminal A waits. Finally,
both terminals are ready, and begin to exchange synchro-phasor data,
and begin to provide digital current differential protection of the
transmission line.

Because of the communications latency, the
synchro-phasor also provides an alignment service. That is, it matches
local phasors with remote phasors that arise from the same time
window. This is a non-trivial task, because of the possibility of lost
data or data that arrives out of sequence under normal operation.

During normal operation, the synchro-phasor
exchange service attempts to exchange phasors redundantly. That is,
two copies of the data are transmitted over physically independent
paths. That way, if one path fails, data is likely available over the
other.

Occasionally the communications network may
switch the physical path between the two terminals, thereby changing
the latency. In the case of a switch to a shorter path, it is possible
to receive data out of order. In that case, it is permissible to throw
some data away, on the theory that more will be arriving shortly.

On rare occasions, the GPS clock at one or both
of the terminals may become unavailable. In that case, it is desired
to automatically throw over to the use of the communications network
to maintain the synchronization of the sampling clock(s), although the
protection function will need to be informed of the loss of the GPS
clock, and will need an estimate of the synchronization error. In the
case of loss of clock synchronization altogether, the protection
function also needs to be notified.

On resumption of clock synchronization
following a loss of synchronization, there are two options: a step
reset of the sampling clock, or a gradual ramping. As far as the
protection function is concerned, either approach is acceptable, but
protection is turned off until complete resynchronization is attained.

## Steps

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Phasor computation | Compute phasor | Local phasor measurements are handed off for publication. |  |  |  | NA |
| 1.2A.1 | Request for subscription | Request phasor subscription | Request that local phasor measurements be transmitted to a remote client | General phasor client | Communications interface |  | Intra-Control Center |
| 1.2A.2 | Cancellation of subscription | Cancel phasor subscription | Cancellation of a previous subscription request | Synchro-phasor subscriber | Communications interface |  | Intra-Control Center |
| 1.2B | Request for phasor | Request local phasor measurement | Request that a single local phasor measurement be transmitted to a local client | Synchro-phasor requestor | Communications interface |  | Intra-Control Center |
