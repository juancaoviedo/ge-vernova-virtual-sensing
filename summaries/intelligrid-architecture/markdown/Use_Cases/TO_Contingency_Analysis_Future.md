# Contngcy Analys Future

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Contingency_Analysis_Future.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - Future Contingency Analysis Function

## Contents

* [Narrative](TO_Contingency_Analysis_Future.htm#Narrative)
* [Steps](TO_Contingency_Analysis_Future.htm#Steps)
* [Start a Second
  Sequence](TO_Contingency_Analysis_Future.htm#Start a Second Sequence)
* [Additional Information](TO_Contingency_Analysis_Future.htm#Additional Information)

## Narrative

### Overview

In layman's terms, Contingency
Analysis (CA) is a "what if" scenario simulator that evaluates,
provides and prioritizes the impacts on an electric power system when
problems occur. A contingency is the loss or failure of a small part
of the power system (e.g. a transmission line), or the loss/failure of
individual equipment such as a generator or transformer. This is also
called an unplanned "outage". Contingency analysis is a computer
application that uses a simulated model of the power system, to:

> ·       
> evaluate the
> effects, and
>
> ·       
> calculate any
> overloads,

resulting from each outage event.

Contingency Analysis is essentially a
"preview" analysis tool. It simulates and quantifies the results of
problems that could occur in the power system in the immediate future.

CA is used as a study tool for the
off-line analysis of contingency events, and as an on-line tool to
show operators what would be the effects of future outages. This
allows operators to be better prepared to react to outages by using
pre-planned recovery scenarios.

**Future CA**
as described in this use case template is an enhanced application that
takes advantage of the improved communications architecture being
defined by IntelliGrid Architecture for the future. It will use wide area data and other
data to improve its reliability, and to analyze power system security
(safe and stable operation) for a wide operating region. Future CA
will also incorporate intelligence features to resolve execution
problems by using its knowledge base of previous experience in solving
difficult situations.

### Introduction

Note: *This
narrative assumes that the reader has already reviewed the use case
template for Contingency Analysis – Baseline (current usage), and is
therefore familiar with the terminology and the functions of this
application for power system security analysis.*

Contingency
analysis (CA) is an Energy Management System (EMS) application that
analyzes the security (i.e. the safe and stable operation) of a power
system. It calculates, identifies and prioritizes the:

> ·       
> current and
> power flow overloads in equipment,
>
> ·       
> voltage
> violations at buses, and
>
> ·       
> some system
> stability problems

that would
occur if contingency events (i.e. equipment failures or outages)
happen in the future. Contingency analysis simulates the effects of
removing equipment, one by one, and calculates the results using a
model of the power system. CA is essentially a "what if" problem
identification tool that is used for off-line studies by system
planners and outage schedulers, and for on-line support by system
operators.

This narrative
describes an advanced contingency analysis application ("Future CA")
that can be achieved in the near future, possibly before 2010. This
application will have features and performance that together address
some of the CA shortcomings that are reviewed in the narrative for
today's CA of 2004. For details of these deficiencies, refer to the
use case template for Contingency Analysis – Baseline.

Some of these
CA shortcomings (and therefore its requirements) can be addressed with
an improved communications architecture, which will support the use of
more, more frequent, higher quality, and wider-area data. This will
enhance CA to form one of the tools necessary for the future
"self-healing grid" that IntelliGrid Architecture project is helping to define.

In the list
below, the CA shortcomings that are candidates for significant or
partial improvement due to an advanced communications architecture are
marked with an asterisk (\*).

Problems that
exist in many current implementations of Contingency Analysis include:

> (a)
> Lack of Reliability and Robustness in the CA solution
> "engine" (\* partial)
>
> (b)
> Usability – difficult to set up and use CA (\* partial)
>
> (c)
> Difficult for users to interpret the avalanche of numeric CA
> results
>
> (d)
> Restricted visibility - not always a "wide area" or regional
> solution, and does not always "see" accurate topology (\*)
>
> (e)
> Few or no remedial action suggestions for operators (\*
> partial)
>
> (f)
> Slow performance
>
> (g)
> No intelligence or learning from previous cases (\* partial)
>
> (h)
> Relatively isolated application, no links with Equipment
> Condition Monitoring or Phase Angle telemetry (\*)
>
> (i)
> Rarely coupled with the SystemOperator Training Simulator (\*
> partial)

This use case
template for Future CA will focus on the CA improvements that will
come from using a communications architecture that is being defined in
IntelliGrid Architecture project. This advanced architecture is a prerequisite for
building the integrated tools that are needed to achieve a
self-healing grid.

 

### Future CA improvements

#### Wide area CA and requirements

The Future CA
will be improved by the use of an advanced communications architecture
that supports the considerably increased acquisition, sharing and
exchange of information and data among utilities, ISOs, and RTOs. This
will allow the exchange of the extensive data needed for input to a
"wide area network model" which can essentially be common to all
participants.

Each utility
can then have a "view" of a wide area that extends beyond its service
area into a larger control area, or a complete operating region. The
contingency analysis will therefore be able to show and quantify the
effects of contingency events that may occur outside each utility's
immediate service area, but that can affect the local operating
conditions.

The size of
this network model, and the corresponding data and contingency events
requirements for wide area CA, will be typically 10 times those of the
current baseline CA. Targets include a model size of 20,000 buses,
supported by 50,000 data points, and screening 10,000 contingencies.

The
communications architecture must also provide very fast acquisition of
this extensive data from its many widespread sources (collection
target within 10 seconds) while ensuring the time coherency of the
data ("skew" target within 5 seconds). The referential integrity of
data with its source, quality, time and other attributes must be
preserved during its acquisition and possibly afterwards for storage.

Wide area CA
will require much higher performance than baseline CA so that
contingency analysis runs essentially in real time, even with the wide
area network model. The target will be to provide CA results for the
most severe contingencies every 20 seconds, which is necessary for its
effective on-line use by operators.

A wide area CA
will make possible (and essential) the coordination of regional
remedial actions by each utility, for mutual security benefits.
Studies can be performed on the most likely and most serious
contingencies over a wide area, to identify and test the best recovery
scenarios. Then remedial action "scripts" can be prepared and used in
a coordinated mode by each utility, based on the wide area simulation.
In some conditions coordinated remedial actions over a wide area may
be more effective than local actions, to maintain overall power system
security and stability.

Regional
authorities such as ISOs already employ a basic form of wide area CA.
The Midwest ISO (MISO) uses a very large network model (over 30,000
buses), based on wide area data (over 80,000 data points) obtained
through several Inter Control Center Protocol (ICCP) data links. This
MISO CA performs reasonably fast studies of wide area power system
security, for operations support. It executes less frequently than the
State Estimator, which typically runs every 5 minutes, according to
the Interim Report on the August 2003 Blackout. However it is a
significant step toward the wide area CA of the future, because it
allows the CA to "see" and evaluate contingency effects over a very
large operating region.

Wide area CA
will therefore require significant improvements in data gathering
capability from many sources, and in data exchange among all the
utilities in a region. Additional needs include fast performance,
tight time coherency and data integrity. These requirements can be met
with an advanced communications architecture.

Wide area CA
will be an improvement over the current baseline CA that has
restricted visibility of power system contingency effects throughout
an operating region. This is one of the operational problems described
in the Interim Report on the August 2003 Blackout.

 

#### CA with improved topology data ("deeper CA")

The CA
algorithm works best (i.e. does not have problems solving) when:

> ·       
> the network
> model is correct (i.e. the model represents the real
> connectivity or topology of power system equipment), and
>
> ·       
> it uses
> accurate base case data for that model (for a current "now"
> CA study, usually the State Estimator results are the most
> dependable).

Problems occur
when the network model is different from the real-world power system.
This can be caused by incorrect topology being reported (due to
transducer wiring errors, or incorrect status is manually entered or
reported by phone from the field) or being deduced from SCADA data. In
this case the network model and the initial base case data do not
match properly, and CA may encounter problems such as failing to
solve. Experts can usually fix the problem by adjusting the model or
its data, but this takes time - often many minutes, and sometimes
hours. Then CA loses its relevance as an on-line tool for operators.

But better
topology data is often available, which could be used by CA. In many
power utilities that use hierarchical control centers, the Energy
Management System (EMS) where the CA executes does not "see" all the
sub-transmission and distribution SCADA data that the regional or
distribution control centers have available from the substations and
field. Only a subset of the field data (from the higher voltage part
of the system) is sent to the EMS, either reported from its own RTUs,
or more typically sent using separate "EMS" scan maps within
multi-purpose RTUs. The majority of the field data is sent to other
lower level monitoring and control systems such as regional and
distribution SCADA.

However this
lower level field data contains valuable information that can be used
by the EMS to correctly deduce or confirm the connectivity and status
of substation and other field equipment, essentially by a "local
estimation" or by using a simple set of rules.

When more of
the sub-transmission and distribution SCADA data is available for use
in a topology estimator or connectivity validation tool, then the
"deeper" CA will benefit from using a valid network model, and will be
more reliable. An advanced communications architecture will provide
this additional data for improved topology. This addresses another of
the operational problems that are described in the Interim Report on
the August 2003 Blackout.

 

#### CA with access to alternate and wide area data

The CA
algorithm sometimes fails to solve, because of faulty or missing data,
or an incorrect network model. Typical problems include:

> ·       
> Use of
> manually-entered data (sometimes obtained by phone from a
> neighboring utility) that is incorrect or incorrectly
> entered,
>
> ·       
> Use of
> telemetered data that is inaccurate or invalid, or
>
> ·       
> Incorrect
> assumptions about the operating status of equipment (such as
> transmission lines or generators) at the boundary of a
> utility's service area.

The improved
communications architecture can be used to provide a wider range of
data from other utilities, which the Future CA will use to become more
robust and accurate. With a wider range of data available, some of it
being obtained from alternate sources outside the local operating
area, the CA application and user have access to the data that "best
fits" the situation under study. The CA user will choose the best data
for the situation, and can either select it or manually enter it for
use during the set up procedure.

With an
advanced communications architecture providing additional and
redundant "checkpoint" data to CA, the application can be enhanced to
automatically choose the correct data for dependable solutions (see
the next section for "intelligent CA").

The
availability of alternate and a wider range of data (from the boundary
of a utility and from other utilities in the region) will therefore
improve the ability of CA to work reliably, to provide solutions in
unusual cases.

 

#### CA using special data (condition monitoring and phase angle measurements)

Although
utilities are increasing their use of equipment condition monitoring
data for asset management and maintenance planning, this data is
rarely used in system operations or security assessment. Future CA
will use equipment condition data to:

> ·       
> Provide
> condition-based operating limits for major power system
> equipment (such as transformers, transmission lines, series
> compensators, and inductors);
>
> ·       
> Initiate
> contingency analysis studies as part of the equipment outage
> planning and scheduling process;
>
> ·       
> Integrate
> equipment condition data and contingency analysis in the
> reliability based maintenance process.

With improved
transducers and very tight time synchronization (approaching a few
milliseconds in current utility tests at Bonneville Power and SRP),
transmission line phase angle measurements within utilities and over
wide areas are starting to be used to show pending power system
stability problems. Future CA will use these phase angle measurements
to initiate contingency analysis in its on-line mode, so that
operators can see potential problems as they are developing.

When phase
angle indicators of potential problems (power angle "twist"
approaching stability limits) are combined with the Future CA
capabilities, remedial actions will be suggested for operators, or in
some cases they will be automatically executed, similar to load and
generation shedding schemes.

 

#### CA with remedial action

Future CA will
make use of the advanced communications architecture to become more of
a "closed loop" application. In addition to:

> ·       
> acquiring and
> using data from wider, deeper, alternate and special
> sources, and
>
> ·       
> providing
> warnings and alarms for potential problem situations for
> future contingency events,

it will provide
remedial action plans as part of the CA results. Operators will use
these to "move" the power system away from exposure to insecure (due
to overloads and violations) or unstable conditions, which the
contingency analysis shows for possible outages in the system.

SystemOperator
can perform these remedial actions, but in some cases they will be
executed automatically using the control capabilities of the data
acquisition and control (DAC) application. The advanced communications
architecture will provide access to the field equipment and control
devices; however in most situations remedial actions will be routed
through DAC to avoid conflicts.

For wide area
and regional operations, remedial actions will need to be coordinated
among the participating utilities and reliability organizations. With
proper coordination and planning, Future CA can send remedial action
control outputs directly to field equipment and automatic systems,
similar to the load shedding and generation dumping schemes used
currently.

 

#### Additional "intelligence" features for CA

The Future CA
can be enhanced with the ability to "look for the best source" data
that will allow it to resolve problem situations. The application can
use the communications architecture to interrogate alternate sources
and actively find better data from the wider range available, both
inside and outside the utility.

Future CA will
also be able to check a stored library of previous studies and
solutions, to identify similar situations to the current study being
performed. This "knowledge base" library will include previous "fixes"
applied by specialists for problem cases that did not solve without
adjustments.

Future CA will
use its knowledge base to assist the user (using prompts or
assumptions) with the set up procedures and definition of the input
data, network model adjustments, contingency lists and execution
parameters.

In case of
problems with the network model, or if the input data does not match
the model, Future CA can exercise its "intelligence" by:

> ·       
> finding and
> suggesting the best data to use from alternate sources, or
>
> ·       
> checking its
> knowledge base and suggesting changes to the model or input
> data.

These changes
or fixes can be quickly tried in a user-prompted or "self-healing"
mode, so that CA guides itself toward a solution while alerting the
user about the decisions it has made. An audit trail with the decision
logic and choices will be maintained as part of the solution
mechanism. As CA gains experience in resolving problem situations, it
will be able to provide to users a confidence factor for its
solutions. In this way raw data (from alternate sources and about the
guided solution process) is transformed into useful information, and
becomes part of the knowledge base.

These
"intelligent" features of CA - the ability to find better data, and to
learn from and use its previous solution experience - will improve its
reliability and usability as an on-line operations tool. The
intelligence features of Future CA form a significant enhancement to
current baseline CA, and make it a key component of the self-healing
grid of the future.

 

#### CA coupled with the SystemOperator Training Simulator

In most current
implementations, contingency analysis works separately (and often
remotely) from the SystemOperator Training Simulator. When operating
situations and contingency analysis cases/solutions are encountered
that would be useful as training scenarios for operators, there are
often no tools (or cumbersome tools) to transfer these cases to the
Training Simulator.

The advanced
communications architecture will include the capability for quick and
easy transfer of cases from Future CA to SystemOperator Training
Simulators. Tools for standardizing the case descriptions, data
formats and input requirements will be needed for "feeding" Training
Simulator applications from various suppliers.

Future CA will
therefore be a source of challenging cases to be used for improved
training for operators. This is another step toward the self-healing
grid.

 

#### Future CA – prerequisites and outstanding issues

There are
several prerequisites and issues that should be examined in more
detail and resolved for the successful implementation of Future CA,
considering its wide area capability and other improvements. These
include:

> ·       
> Apply and
> benefit from the experience with the basic wide area CA as
> already implemented at ISOs and RTOs in their function as
> area and regional reliability coordinators;
>
> ·       
> Significant
> work and tools will be needed to develop and support the
> wide area network model, its frequent changes, and its
> parameters;
>
> ·       
> Methods must
> be developed to collect the necessary data from many sources
> (participating utilities and regional authorities), and
> "feed" a wide area CA, fast enough (collection target within
> 10 seconds) to support its on-line use by operators;
>
> ·       
> Significant
> work and tools will be needed to acquire and exchange data
> in common formats, requiring data conversion and re-mapping
> among different Energy Management Systems, data sources and
> applications;
>
> ·       
> Uniform data
> access methods will be needed for all types of data, for
> ease of use;
>
> ·       
> High
> performance needs - wide area CA should execute fast enough
> (solution target every 20 seconds) to be used for on-line
> operations support as well as for off-line studies;
>
> ·       
> Performance
> may need to be enhanced by using a reduced wide area network
> model, that still contains enough detail to provide useful
> information;
>
> ·       
> Data coherence
> and time synchronization needs (time skew) – the wide area
> data should be time synchronized (target within 5 seconds)
> so that the network model uses coherent data;
>
> ·       
> Time
> synchronization needs for special data - phase angle
> measurements across an operating region must be very tightly
> synchronized (within a few milliseconds) to be useful;
>
> ·       
> Data integrity
> – the CA input data and its attributes (source, quality,
> time stamp, etc.) must be preserved throughout the process,
> and (perhaps) afterward for storage
>
> ·       
> Older RTU
> technology, field devices and communications technology
> currently used by utilities are limitations that will slow
> down data gathering to the "lowest common denominator" until
> they are upgraded;
>
> ·       
> Several types
> of data must be gathered and shared among utilities,
> including the network model and parameters, initial base
> case set up data, real-time measurements, State Estimator
> solutions, special data, manually entered data, and the
> Future CA results including remedial action plans;
>
> ·       
> Storage and
> archiving – the requirements for short-term storage and
> historical archiving of Future CA cases, including large
> data files, should be considered within the communications
> architecture;
>
> ·       
> Work will be
> needed to develop coordinated remedial action plans for the
> most serious contingencies, for joint execution by utilities
> in the region;
>
> ·       
> It may be
> possible to implement automatic triggering and automatic
> execution of remedial actions, similar to load shedding and
> generation shedding routines that are largely automatic
> today;
>
> ·       
> For technical
> support and data flow optimization, it may be more feasible
> for all participating utilities to use a single regional
> wide area CA running on a central server (i.e. an extension
> of the current ISO type of CA), with real-time access and
> displays provided to all utilities for executing individual
> studies and obtaining CA results;
>
> ·       
> For accuracy
> of its solutions, the Future CA should include in its
> network model the operations of Special Protection Systems
> (such as automatic load shedding and generation dumping), as
> well as the operating status of these systems;
>
> ·       
> Future CA
> could be extended to provide useful results if the power
> system breaks into islands, for use in system restoration;
>
> ·       
> Common
> training will be needed for users, including use of the
> operator training simulator for scenarios in the wide area
> context;
>
> ·       
> For effective
> use by multiple utilities in an operating region, Future CA
> will require a common and intuitive User Interface, user
> procedures, and maintenance tools;
>
> ·       
> Improved
> presentation methods (probably using graphics) will be
> needed to show the wide area CA results, to ensure easier
> and quicker understanding by all users, especially the busy
> power system operators;
>
> ·       
> There may be
> some restrictions on sharing of certain data among utilities
> due to deregulation (e.g. knowledge of planned outages by
> one utility might provide a "market power" advantage to
> another utility).

 

#### Future CA improvements summary

In summary, the
combination of the contingency analysis improvements reviewed above
will constitute a Future CA that takes advantage of an advanced
communications architecture to address many of the current CA
shortcomings. Future CA will feature:

> ·       
> Acquisition
> and use of data from wider, deeper, alternate and special
> sources
>
> ·       
> Improved
> reliability and robustness (i.e. solving without problems
> and the need for expert assistance) due to the use of wide
> area, deeper and alternate data
>
> ·       
> Improved
> usability (i.e. easier setup) with the uniform access to,
> and automatic use of, many sources of data
>
> ·       
> Improved
> usability with a standard and intuitive User Interface
>
> ·       
> Increased
> visibility of the interconnected power system, using the
> wide area data for regional solutions that are more valuable
> for on-line operations
>
> ·       
> Remedial
> action plans that CA provides to operators, or automatically
> executes in some situations using DAC or direct control
> outputs
>
> ·       
> Intelligence
> to learn from experience and guide itself toward correct
> solutions, for increased reliability in problem situations
>
> ·       
> Use of special
> data such as equipment condition monitoring and phase angle
> measurements
>
> ·       
> Easy transfer
> of unusual cases to the training simulator for building
> scenarios

These CA
improvements can be implemented using an advanced communications
architecture that is being defined by IntelliGrid Architecture project. Future
contingency analysis will provide increased value to system operators,
as a dependable on-line decision support tool. Actual implementation
of the Future CA by suppliers will likely be done in stages, and is
achievable by 2010, to form a major component of a self-healing grid.

 

### Future CA usage

Future CA will
be used for off-line studies as follows:

> ·       
> A request to
> evaluate a power system change or a planned equipment outage
> initiates the contingency analysis study
>
> ·       
> The CA user
> sets up the study, using input data from wide area and other
> sources, now available through the advanced communications
> architecture (and stored for use in "future" study cases)
>
> ·       
> The
> intelligence features of CA assist the user to define the
> study case, including the input data, network model
> adjustments, contingency lists, and the execution parameters
>
> ·       
> In case of
> execution problems, the intelligence features help to find a
> solution using alternate data or model adjustments, based on
> previous learned experience
>
> ·       
> CA presents
> its wide area results (severity-ranked lists of overloads
> and violations, for the utility and the operating region) to
> the CA user for evaluation (probably with graphic displays
> for easier interpretation of the results)
>
> ·       
> If necessary,
> the CA user easily transfers the study case and parameters
> to the Training Simulator for use in building operator
> training scenarios

Future CA will
be used for on-line operations support as follows:

> ·       
> Experts
> perform the set up of CA for on-line use, including the
> network model, definition of input data and the contingency
> list to be used, etc.
>
> ·       
> An execution
> control program in the EMS for the security analysis
> sequence initiates CA to execute continuously, typically
> every 20 seconds
>
> ·       
> CA uses for
> its solutions the wide area and other source data for the
> current operating conditions, continuously updated through
> the advanced communications architecture
>
> ·       
> In case of
> execution problems, the intelligence features automatically
> find a solution using alternate data or model adjustments,
> based on previous learned experience
>
> ·       
> CA presents
> its wide area results (severity-ranked lists of overloads
> and violations, plus warnings and alarms to notify of
> potential problems) to the system operators for decision
> support
>
> ·       
> CA also
> provides lists of remedial actions for each severe
> contingency, for manual implementation by operators, or for
> automatic execution using the DAC application and the
> advanced communications network
>
> ·       
> If necessary,
> the operators can easily transfer interesting CA cases and
> remedial action lists to the Training Simulator

As shown above,
to the casual observer Future CA will work in a similar way to current
baseline CA. However with its improvements the application will be
more reliable, the results will show the wide area effects of
contingencies, and operators will have an on-line tool that assists
with remedial actions.

 

### Future CA incremental data inputs and outputs

In addition to
the data inputs that already are used in current baseline contingency
analysis, Future CA will exploit the advanced communications
architecture to use the following "new" data:

> ·       
> Wide area data
> such as SCADA, network models and parameters, State
> Estimator solutions, telemetry and manual entries obtained
> from a large operating region, beyond each utility's
> boundaries
>
> ·       
> Deeper data
> and accurate topology information from SCADA, distribution
> systems, telemetry and manual entries within each utility
>
> ·       
> Alternate and
> substitute data, that Future CA actively seeks for use in
> solving execution problem situations
>
> ·       
> Special data
> such as equipment condition monitoring and phase angle
> measurements

In addition to
the results that already are provided by current baseline contingency
analysis, Future CA will use its improvements and exploit the advanced
communications architecture to provide the following "new" outputs:

> ·       
> Remedial
> action lists, for operators to implement, or for automatic
> execution
>
> ·       
> Control
> outputs (remedial action commands) to the DAC application,
> or in some cases directly to field devices and special
> protection systems
>
> ·       
> Storage of
> cases and model or data adjustments by experts, for use in
> the knowledge base library
>
> ·       
> Transfer of
> cases and associated parameters to the SystemOperator
> Training Simulator

These
incremental inputs and outputs will be supported by the advanced
communications architecture, to enhance the Future contingency
analysis application.

 

### Additional communications impacts for "central server" CA

If Future CA
were implemented in a central server, to serve many remote users at
utilities throughout an operating region, there would be
communications impacts due to:

> ·       
> Users sending
> requests and data for off-line contingency analysis studies
> to be executed at the central CA facility
>
> ·       
> The return of
> CA results and displays to regional users
>
> ·       
> The continuous
> "broadcast" of on-line CA results to operators and other
> users at participating utilities

In this use
case template, it is assumed that each participating utility will have
its own Future CA application working in its Energy Management System.
The analysis and communications impacts reflect this "individual
Future CA" model.

## Steps

### Future Contingency Analysis Off-line Study Mode Sequence = FCA-SM steps

| **#** | **Event** | **Name of Process** | **Description of   Process/Activity** | **Information Producer** | **Information   Receiver** | **Name of Info Exchanged** | **Additional Notes** | **IntelliGrid Architecture Environments** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Outage request  Or  Change study request  (can split these later into separate sequences if necessary, but each request initiates the same steps) | Initiate CA study | Initiates the Contingency Analysis study, by:  ·         a request for off-line analysis of an equipment outage request or  ·         a change (to the power system) request | Field Equipment Maintenance Mgmt System  Or  System Planner | Future CA User (SM)  (a generic user to represent the Equipment Outage Planner  and Scheduler, or the System Planner) | Outage request  Or  Change study request |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2 |  | Set up CA study | CA user sets up the CA study, by using CA displays to feed/input/acquire the necessary network model and data from the EMS databases, and by using manual entries.  Notes:  ·         the intelligent features of Future CA will prompt and assist the set up procedures;  ·         several elements of data are required to "set up" a CA study;  ·         these elements can be acquired from many wide area and other sources, however all necessary data is available through the EMS databases;  ·         this process becomes more complex for a future study case | EMS databases  External Computer System  Special systems  DAC | Future Contingency Analysis  application | Network model  Base case initial data | Communications issues: interfaces and data exchange and performance | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 3 |  | Adjust the network model | CA user adjusts the network model to represent the power system configuration to be studied. The user performs this by manually removing equipment from a base configuration, or possibly by adding equipment. |  | Future Contingency Analysis  application | CA study model | Communications issues: may need access to stored future data and historical data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 4 |  | Define contingency list to be used | CA user defines the list of contingency events to be used in the study. Includes making manual adjustments to stored lists retrieved from the EMS database.  This list could range from a few outages to be evaluated, to thousands of outages to be simulated. | EMS databases | Future Contingency Analysis  application | Contingency list |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 5 |  | Set CA execution parameters | CA user sets the CA execution control parameters, to define constraints and outputs. |  | Future Contingency Analysis  application | Execution parameters |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 6 | CA user starts contingency screening process ("start" button) | Screen for worst contingencies | CA application performs a quick check to screen (identify) the worst contingencies, and displays these to the user.  Note: users may choose to skip this step and instruct the application to proceed directly to the "complete analysis" step CA-SM.7. |  | Future CA User (SM) | Screened contingency list |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 6.1 | CA solution fails or has solution problems | Future CA resolves solution problems | Future CA alerts the CA user when it encounters solution problems; then will use its intelligent features and ability to find better or alternate data, to automatically resolve problems of incorrect models or mismatched data | Future Contingency Analysis  application | Future CA User (SM) | CA error messages | Communications issues: interfaces and data exchange and performance | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 7 | CA user starts complete analysis for the worst contingencies | Perform complete analysis of the worst contingencies | Future CA application performs a complete analysis of the worst contingencies, to calculate and display the branch overloads and voltage violations for each outage, for the wide area operating region. |  | Future CA User (SM) | CA results | Performance and visualization issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 8 |  | Reviews and interprets CA results | CA user reviews and interprets the CA results.  Typically results are presented in summary tabular displays, however Future CA will use graphic display techniques to assist interpretation of voluminous results. |  |  |  | Presentation and visualization issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 9 |  | Saves results | CA user initiates the printing and "save" of CA results in the EMS databases.  User may transfer the CA study model and results to the Training Simulator (an external system). |  | EMS databases  External Computer System | CA results | Communications issues: interfaces and data exchange | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 10 |  | Issues report | CA user issues report based on the CA results: an outage approval, or a report on the effects of the proposed change to the power system.  Report templates and forms are typically available from the CA application and EMS.  May also affect the annual maintenance and outage plan. |  | Field Equipment Maintenance Mgmt System  Or  System Planner | Outage approval  Change study report |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |

### 

## Start a Second Sequence

### Steps to implement Future Contingency Analysis On-line Operations Mode Sequence (OM)

Note: This mode of use of Future Contingency
Analysis is very similar to the off-line study mode, except that:

> ·       
> the users are the power system operators in
> the control center, outage coordinators who manage the
> planned withdrawal of equipment from the power system, and
> network engineers who provide advisory support to the
> operators
>
> ·       
> the application runs continuously in the
> background, providing its results (a preview of contingency
> effects) to operators with updates at every execution cycle
> (target every 20 seconds)
>
> ·       
> the application looks at contingencies
> starting with the current operating situation (not future
> situations), and uses the current power system data and
> State Estimator data from the wide area to initiate its
> network model for the operating region
>
> ·       
> operators typically do not interact with the
> application or initiate their own studies; it is more of a
> "look only" advisory tool
>
> ·       
> the on-line Future CA provides visual warnings
> and even audible alarms to operators, to notify them of
> overloads and violations that would occur if certain
> contingency events happen in future (i.e. a "what if"
> preview of the effects of future outages)
>
> ·       
> on-line Future CA provides lists of remedial
> action suggestions, which will be performed by operators to
> correct potential problems
>
> ·       
> on-line Future CA may send commands directly
> to DAC to perform remedial actions as automatic procedures,
> without operator assistance

### Future Contingency Analysis On-line Operations Mode Sequence = FCA-OM steps

| **#** | **Event** | **Name of Process/Activity** | **Description of   Process/Activity** | **Information Producer** | **Information   Receiver** | **Name of Info Exchanged** | **Additional Notes** | **IntelliGrid Architecture Environments** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FCA-OM.1 | Periodic "start CA" command from the execution control program | Initiate on-line Future CA execution | Initiates the Future Contingency Analysis in periodic cycles (target every 20 seconds) using the application execution control program (security analysis sequence). |  |  |  | Communications issues: gather wide area and other data fast enough to support on-line use of Future CA | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| FCA-OM.2 | CA results presented to users | Present on-line Future CA results | Presents the on-line Future CA results in displays for the users to consult and monitor; revised results are presented after every CA execution cycle, target every 20 seconds |  | Future CA User (OM) | CA results  CA warnings and alarms  Remedial action suggestions | Presentation and visualization issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| FCA-OM.3 | Future CA user action | Action by users of on-line CA | Future CA on-line users may react to the CA results and remedial action suggestions by:  ·         System Operator: Planning remedial actions, to be ready if a contingency event occurs  ·         Outage Coordinator and Network Engineer: Implementing or postponing a scheduled outage  ·         System Operator: Making remedial action changes to the power system to reduce exposure to problems in case of a contingency event |  | DAC  Field Equipment Maintenance Mgmt System | Remedial action commands | Communications issues: output commands to DAC and field devices | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| FCA-OM.4 | Future CA action | Future CA direct remedial action | Future CA may issue direct remedial action commands to DAC, to correct undesirable operating situations in the power system. |  | DAC | Remedial action commands | Communications issues: output commands to DAC and field devices | [Critical Operations DAC](../Environments/Env5_Critical_Operations_DAC.htm) |

## Additional Information

### Information exchanged

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| Outage request | Document form, electronic and paper  The outage request is a form submitted by field maintenance personnel to the equipment outage planner and Scheduler. It requests approval to take equipment out of service for a defined period of time, for a specific reason. |
| Outage approval | Document form, electronic and paper  Approval form issued by the outage planner and Scheduler, to approve the equipment outage and schedule it for a specified date/time/duration. Operations and maintenance personnel would then perform the equipment outage procedures. |
| Change study request (study of a power system modification) | Document drawing and description, electronic and paper  Notice of a planned change to the power system (e.g. the addition of a substation) to be studied. The system planner reviews this change using CA, to evaluate the impacts on the modified configuration in case of contingency events (equipment failures). |
| Change study report | Document drawing and description, electronic and paper  Report prepared by the system planner from the results of the CA study, which accepts, accepts with modifications, or requests further study about the planned change. |
| Annual maintenance and outage plan (or similar names) | Document, electronic and paper  Plan used to schedule the un-availabilities for power system equipment. Consulted to determine future planned configurations of the power system. Used for studies of new outage requests and for risk assessment by operations. Is refined into monthly and weekly outage schedules throughout the year, to reflect current operating conditions of the power system. |
| Network model (wide area) | Stored files on computer media  Static simulated model of the wide area power system, used by Future CA. This model uses the parameters and characteristics of the real-world power system and "behaves" like the real system for the purposes of studies. Can be a model of the current power system, or of a future configuration of the power system. |
| Base case initial data | Stored files on computer media + Manually entered data  Data that CA obtains from the EMS databases in order to set up the network model before executing the analysis. Includes data that is entered manually by users.  Sometimes the base case is for a study of a future operating condition of the power system, requiring a future "picture" of the network and its parameters.  Future CA will assist the definition of the base case initial data, with automated choices based on previous similar situations, and "prompts" to the user. |
| CA study model | Temporary or stored file  Network model that has been adjusted by the CA user, by removing or adding equipment until it represents the desired starting point for the CA study.  Future CA will assist the definition of the study model, with automated choices based on previous similar situations, and "prompts" to the user. |
| Contingency list | Document, electronic and paper and Temporary or stored file  List of contingency events (equipment outages) that is prepared by the CA user, and input to CA as the list of events to evaluate. Typically a base contingency list is retrieved from the EMS database and manually enabled and modified by the user (on displays) before it is ready for CA to use.  These lists can range from a few selected items of power system equipment, to thousands of elements of the power system. They are the "test scripts" for CA execution.  Future CA will assist the definition of the contingency list, with automated choices based on previous similar situations, and "prompts" to the user. |
| Execution parameters | Stored files on computer media + Manually entered data  Control parameters (enable or disable certain features of the application, and enter values) that the CA user selects from menus or enters manually, to set up the behavior and functionality of the application. |
| Screened contingency list | Document, electronic and paper and Temporary or stored file  List of the most serious equipment outages that are selected by the CA screening process (or manually selected by the CA user) to undergo a complete analysis to determine the severity of violations and overloads. |
| CA results | Document forms and graphic pictures, electronic and paper  Lists of bus voltage violations and branch overloads for the wide area operating region, shown in displays and on printouts. Typically these results consist of long lists of numbers sorted by priority – worst case violations/overloads are shown at the top of the list. Future CA will have improved visualization technology and incorporate graphic pictures for easier interpretation of results.  CA users also provide written reports to summarize these results for other departments. |
| Stored CA results | Data files  CA study results are stored in the EMS databases for review by system planning, outage scheduling, and operations personnel. They can also be accessed by or transferred to the Training Simulator, for use in building training scenarios for operations personnel. |
| CA error messages | Temporary or stored file  The CA application issues notification to the users of any problems with its execution, so that the user can adjust the model or provide additional data inputs to correct the problem.  Future CA will use its intelligence features to resolve solution problems based on previous experience and the use of better or alternate data. |
| CA warnings and alarms | Temporary or stored file  For on-line users Future CA will issue warning messages and even audible alarms, to notify operators about overloads or violations that WOULD occur IF certain contingency events happen in future. These are essentially "preview" warnings or alarms about the effects of possible future events. |
| Remedial action suggestions | Temporary or stored file  Future CA will provide suggestions for operators to correct potential overloads and violations. These would typically consist of suggestions to adjust or add generation, reduce load, adjust power system voltage levels, add reactive VAR resources, isolate a problem area, etc. |
| Remedial action commands | Temporary or stored files  Future CA may send commands directly to DAC to perform remedial actions as automatic procedures, without operator assistance.  Operators will also issue remedial action commands to DAC. |
| Saved cases for the knowledge base library | Data files  Future CA will save useful and unusual study cases (network models, base case data, and adjustments by experts to allow solutions) in its knowledge library. The intelligence features will use this library to assist in providing solutions when execution problems occur. |
| Saved cases for the System Operator Training Simulator | Data files  Future CA will transfer interesting study cases (network models, base case data and results) to the System Operator Training Simulator using easy procedures, if a CA user initiates this type of "saved case". |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Acquire and use extensive data | Future contingency analysis (CA) will use extensive data to be more robust, and to provide wide area analysis and visibility of the regional power system. |
| Use intelligent features to solve execution problems | Future CA will incorporate intelligent features to solve difficult cases, with minimal assistance needed from users and experts. |
| Identify the most serious contingencies for detailed analysis | CA performs a quick screening of the hundreds or even thousands of possible equipment outages (contingencies), and identifies the few (typically 10-50) that would have the worst effects on the power system. |
| Analyze the most serious contingencies and quantify the effects of each | CA performs a complete analysis of the most serious contingencies, to calculate the magnitude of branch overloads and voltage violations for individual elements of the power system. These "what if" simulations are the main tool for ensuring secure power system operation in case of equipment failures or planned equipment outages. |
| Organize the analysis results (by severity) and display them to users (both on-line and off-line use) | CA presents the overloads and violations in order of their severity, in tabular lists. These are displayed and can be stored for reference. Future CA will use graphic displays for presentation of wide area results.  For on-line use by operators, summary displays show highlights of the CA results, such as the names of contingency events that would result in severe overloads, and the number of these overloads. |
| Issue warnings and alarms to operators (on-line use) | CA issues warning and alarm messages to power system operators, to alert them about the effects of **future** contingency events (i.e. a preview) that would result in branch overloads and voltage violations. |
| Provide remedial actions (on-line use) | Future CA will provide remedial action suggestions for operators to perform, and will issue remedial action commands for automatic execution. |
| Save results and cases for reference, in the CA database and knowledge base | CA users can save results and the study cases (power system conditions), for future review. This includes Future CA saving in its knowledge base difficult cases and fixes applied by experts, for intelligent use in future situations.  Note: this "save case to knowledge base" activity is NOT included in the step-by-step analysis, because it is an internal (background) activity of Future CA, with no external communications impact. |
| Transfer study cases to the operator training simulator for use in training | Future CA users can easily transfer interesting study cases to the operator training simulator, for use in training scenarios. |

### Contracts/Regulations

| ***Contract/Regulation*** | ***Impact of Contract/Regulation on Function*** |
| --- | --- |
| Deregulation and competition (FERC Orders 888 and 889, etc,) | May restrict the sharing of power system data (especially equipment unavailabilities) among competing utilities (and related companies), which could limit the Contingency Analysis solutions to the "observable" network, instead of a wider area solution. |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ***Policy  if !supportLineBreakNewLine?  endif?*** | ***From Actor   if !supportLineBreakNewLine?  endif?*** | ***May*** | ***Shall Not*** | ***Shall*** | ***Description (verb)*** | ***To Actor*** |
| NERC Operating Policy 2.A – Transmission Operations | NERC |  |  | X | Operate the power system in a secure and reliable manner, using security analysis tools to recognize and avoid problem conditions.  "All control areas shall operate so that instability, uncontrolled separation, or cascading outages will not occur as a result of the most severe single contingency."  (voluntary reliability guidelines and standards for utilities) | System Planners and System Operator |

 

|  |  |  |  |
| --- | --- | --- | --- |
| ***Constraint*** | ***Type*** | ***Description*** | ***Applies to*** |
| Thermal limits of power system equipment | Engineering | Flow limits (maximum current and MW) to be respected in order to avoid damage to, or premature aging of, power system equipment (such as generators, transmission lines, transformers, breakers, etc.). Used by CA to calculate overloads. | Future Contingency Analysis application |
| Stability limits for transmission lines and corridors | Engineering | Flow limits (maximum MW and MVA) for transmission lines and corridors, to be respected in order to maintain power system stability. Used by CA to calculate overloads. | Future Contingency Analysis application |
| Voltage limits | Engineering | Voltage limits on buses (high and low) to be respected in order to maintain secure and stable operation of the power system. Used by CA to calculate violations. | Future Contingency Analysis application |
| Wide area and other data | Communications | Future CA will need an advanced communications architecture to provide wide area and other types of data for the calculations. | DAC |
| Need for fast solutions (a) | Performance of the application (computer resources) | For on-line use by power system operators (decision support), CA must provide fast solutions, within seconds of an event.  Current (2004) computer resources can already meet this constraint, so there is no problem for Future CA resources. | Energy Management System |
| Need for fast solutions (b) | Performance of the application (application design) | For on-line use by power system operators (decision support), CA must provide fast solutions, within seconds of an event.  Future CA will have improvements to meet this constraint, even for wide area solutions. | Future Contingency Analysis application |
| Need for robust application | Reliability of the application (application design and features) | For both off-line and on-line use, CA must be reliable – it must provide solutions even in difficult situations with limited input data.  Future CA will have intelligent features to assist with solutions. | Future Contingency Analysis application |
| Need for ease-of-use of the application | Usability of the application (application design and user interface) | In order to be useful for on-line analysis and decision support, the CA application must be easy to use, without requiring a programmer's skills. | Future Contingency Analysis application |
| Need for fast analysis of the results | Usability of the application (application design and results presentation) | The CA application must present its voluminous numeric results in a manner that can be quickly understood by users, especially for on-line use. This requires summary displays and graphical displays that are designed for easier interpretation. | Future Contingency Analysis application |

#
