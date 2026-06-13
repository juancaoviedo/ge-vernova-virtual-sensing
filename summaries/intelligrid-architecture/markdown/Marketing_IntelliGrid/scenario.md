# The IECSA Scenario

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Marketing_IntelliGrid/scenario.htm

---

![](../images/IntelliGridlogo.jpg)
 
[![](graphics/contact.gif)](http://www.e2i.org/resources/contact.html)
![](../images/EPRI-head01-alt.jpg)

![](graphics/ceids_art.jpg)

How the
IntelliGrid Architecture Comes into Play

In order to best understand the scope of the
problem and application domains that a comprehensive utility
communications, command, and control architecture must deal with,
here is a fictional but realistic future scenario of how a fully
deployed system might operate. This vision of the future of power
system operations served as a basis for describing the technical
approach to be used in defining the requirements for the IntelliGrid Architecture.

![](infrastructure3.jpg)

This scenario is designed to illustrate how use
of the IntelliGrid Architecture can improve the reliability and performance of the
overall system with communications and coordination all the way from
power generation to end user facilities. It is only one of many
scenarios where the IntelliGrid Architecture will support new
applications that were previously not possible. Overall, the
implementation can result in significantly improved reliability and
power quality while achieving more optimum operation of the system
at the same time.

#### The Scenario

This afternoon around 3:00 PM CDT near
Nashville, Tenn. heavy thunderstorms roll into the area. The
temperature is 99 degrees and the humidity is about the same - a new
peak load record will be set today. High winds, heavy downpours, and
significant lightning accompany the storms. At 15:12:10 CDT,
lightning strikes a tower on the Tennessee Valley Authority 500 kV
Roane-Wilson line - the major line serving Nashville from the east. This causes a flashover. This is reported in real time via
the National Lightning Detection Network and reported automatically
on the operator’s SCADA display. The flashover results in the
failure of one of the line insulator strings - a permanent fault.

The ensuing fault results in breakers opening
at the Roane and Wilson stations. Due to a protective device
configuration problem, the 1100 MW generating plant at Watts-Bar
trips off-line. At 15:12:40 after unsuccessful re-close attempts,
the breakers lockout due to the permanent fault. At 15:12:45 the
automatic generation control for the area starts responding to a
deficit of generation in the Nashville area because of the line
outage and generator trip. Signals are automatically sent to other
generators in the area using the newly implemented IntelliGrid Architecture system to
increase local generation. At 15:13:00 the Emergency Control System
(ECS) module of the IntelliGrid Architecture determines that there is not enough
generation or line capacity to meet the generation deficit. The ECS
evaluates the situation and decides that a combination of line
reconfiguration, power flow controller operation, load reduction and
dispatch of distributed generation resources in the area will make
up the deficit. The system updates prices for the next hour for
customers on hourly real-time pricing rate structures, sends
interrupt signals to selected interruptible rate customers in the
affected area, and initiates residential load control by sending
signals to shut down water heaters and other non-essential loads for
that time of day.

As generation starts to come on line and load
is reduced several FACTS controllers in the area have also been
commanded to divert power flow onto the TVA 161 kV lines to help
make up the deficit. On-line power flow, stability and security
analysis applications have re-calculated the optimum FACTS
configuration.

In an industrial park in the Nashville area, a
large, automated plastic bag manufacturing plant on a real-time rate
has received the next hour's prices, which are very high due to the
line and generator outage. Their energy management system has
decided to shut down the plant to save money. Nearby, a
semiconductor manufacturing firm has benefited from a temporary
reconfiguration of protective devices in the area. When the local
ECS determined that a storm was in the area (from the NLDN data) the
re-closers instantaneous trip setting were temporarily restrained on
selected feeders serving sensitive loads to minimize momentary
interruptions and multiple sags due to multiple re-close attempts. A
few more fuses would be sacrificed in residential areas to prevent
the storm disrupting critical industrial loads during the day.

An Internet service provider in the affected
area is on a feeder with distributed generation resources sufficient
to meet the entire load in that area. When the ECS dispatched the
generation, the local substation controller decided to temporarily
island itself from the main utility grid to eliminate the impact of
voltage sags from the transmission system.

By 15:15, the load/generation imbalance had
been fully satisfied and a new, stable system configuration has been
achieved. As the storm move through the area, small, local
configuration optimizations were performed.

The storm dissipates by 15:45 and as local ECS
controllers sense this through input from various distributed
measurement devices, they begin restoring protective device settings
back to normal. As work crews complete repairs on the transmission
line a few hours later and put it back in service and the Watts-Bar
generator comes back on-line, real-time prices are adjusted
accordingly, generation re-dispatched, line configurations and FACTS
controllers revert back to their normal, optimal configurations and
islanded systems are re-synched to the grid.

By the next morning, several applications with
access to the ECS database have automatically prepared reports on
how the system performed, the total cost of the storm including
incremental generation costs, repair costs, etc. Power quality and
reliability performance reports were prepared for engineering and
marketing personnel. Any system anomalies encountered during the
storm were automatically analyzed, a maintenance plan prepared and
e-mailed to appropriate personnel.

The IntelliGrid Architecture system has resulted in preventing a
wide area outage due to the generation deficit, has optimized the
configuration of local distribution systems to deal with the storm,
and has minimized disruptions that specific load centers are
sensitive to.

---

This page, and all contents of this web site, are © 2003-2004 by
EPRI. All rights reserved.
