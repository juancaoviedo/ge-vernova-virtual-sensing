# Contngcy Analysis Base

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Use_Cases/TO_Contingency_Analysis_Baseline.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Transmission Operations - Contingency Analysis Baseline Function

## Contents

* [Narrative](TO_Contingency_Analysis_Baseline.htm#Narrative)
* [Steps](TO_Contingency_Analysis_Baseline.htm#Steps)
* [Start a Second
  Sequence](TO_Contingency_Analysis_Baseline.htm#Start a Second Sequence)
* [Additional Information](TO_Contingency_Analysis_Baseline.htm#Additional Information)

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

* evaluate the effects, and
* calculate any overloads,

resulting from each outage event.

Contingency Analysis is essentially a
"preview" analysis tool. It simulates and quantifies the results of
problems that could occur in the power system in the immediate future.

CA is used as a study tool for the
off-line analysis of contingency events, and as an on-line tool to
show operators what would be the effects of future outages. This
allows operators to be better prepared to react to outages by using
pre-planned recovery scenarios.

### Definitions

This narrative
is intended to provide an overview of the Contingency Analysis System,
including its major components, methodology, use, users, and a summary
of its data inputs and outputs. This narrative is not intended to be a
course in power engineering, and so will deal with everything at a
high level.

* The term
  "security" refers to the secure and stable operation of the electric
  power system in case of one or more equipment failures. It does not
  refer to the protection of digital information from computer "hackers"
  in the data communications world.
* An "element" of a
  power system usually refers to its electrical equipment (e.g.
  generator, transformer, transmission line, circuit breaker, etc.). An
  "outage" is the removal of equipment from service. It can be
  intentional and planned (i.e. for maintenance), or unplanned (i.e. due
  to failure). Element can also refer to the wider context of a group of
  devices that together constitute an outage, such as a busbar which
  effectively goes out of service if one or more breakers do not operate
  correctly.
* This narrative
  provides a high level and generic view of the Contingency Analysis
  software application. Each utility's use of this application will
  vary, ranging from off-line use in study and planning mode only, to
  its on-line use by system operators and network engineers for decision
  support.
* The fine points
  and variations of what exactly constitutes a "contingency" or failure
  of some part of the power system are not covered in this narrative.
* Related
  applications for security analysis of the power system, and supporting
  applications in SCADA and Energy Management Systems, are simply
  referenced, not described.
* A high level and
  generic explanation is provided of the power flow algorithm, which is
  the basis of the contingency analysis. More detailed coverage is not
  necessary to understand the functionality of CA.

### Overview of Contingency Analysis

Evaluation of
power system security is necessary in order to develop ways to
maintain system operation when one or more elements fail. A power
system is "secure" when it can withstand the loss of one or more
elements and still continue operation without major problems.

Contingency
Analysis (CA) is one of the "security analysis" applications in a
power utility control center that differentiates an Energy Management
System (EMS) from a less complex SCADA system. Its purpose is to
analyze the power system in order to identify the overloads and
problems that can occur due to a "contingency". A contingency is the
failure or loss of an element (e.g. generator, transformer,
transmission line, etc.), or a change of state of a device (e.g. the
unplanned opening of a circuit breaker in a transformer substation) in
the power system. Therefore contingency analysis is an application
that uses a computer simulation to evaluate the effects of removing
individual elements from a power system.

After a
contingency event, power system problems can range from:

* none - when the
  power system can be re-balanced after a contingency, without overloads
  to any element, to
* severe - when
  several elements such as lines and transformers become overloaded and
  risk damage, to
* critical - when
  the power system becomes unstable and will quickly collapse.

Current
electric utility operating policies (such as NERC's) require that each
utility's power system must be able to withstand and recover from any
"first contingency" or any single failure. Future policies may extend
this to withstanding a "second contingency" or any subsequent single
failure. Therefore contingency analysis is one of the tools used
primarily by power system planners and engineers to "test" the power
system (using a software model) for its strengths and weaknesses, and
for compliance with the operating policies. CA has always been an
important part of electric utility system planning and operations,
even before there were computers to assist the analysis, when manual
calculations were used.

By analyzing
the effects of contingency events in advance, problems and unstable
situations can be identified, critical configurations can be
recognized, operating constraints and limits can be applied, and
corrective actions can be planned.

In the planning
mode, apart from analysis of the complete power system for overall
security, CA is also used for scheduling the withdrawal of power
system equipment for periodic or restorative maintenance. The effects
of equipment outages are evaluated using future operating conditions
of the power system. The schedule for planned outages is arranged for
minimal risk of problems by using these CA studies, to avoid
scheduling concurrent outages of critical system elements.

CA is therefore
a primary tool used for preparation of the annual maintenance plan and
the corresponding outage schedule for the power system. This outage
schedule requires modification to reflect changes in the operating
conditions over time, and so CA is used repeatedly to refine the
schedule of planned outages, for long term and short term planning. If
there are no problems revealed by a final check using CA just before
an outage is scheduled to take place, the planned outage is approved
by the outage coordinator or network engineer, and it is implemented
by the system operator or dispatcher in the control center. Operators
perform the outage by using the DAC (data acquisition and control)
applications to open breakers and switches, to isolate equipment from
the power system.

 

### Methodology and the contingency analysis process

The CA
application is based on a detailed electrical model of the power
system, called the "network model". This is a simulated model of the
real power system that is prepared by each utility's system planners
and network engineer specialists. They translate the real world
equipment and connections of a power system (typically shown in a
schematic representation, called a one-line diagram) into a
mathematical model of the power network that is suitable for solution
by computer algorithms. This network model contains the connection
information (called the topology and connectivity), and the electrical
characteristics of the equipment (such as the impedance of
transmission lines). The algorithm in contingency analysis uses this
network information (often called network "parameters") and the
network model to simulate, and calculate the effects of, removing
equipment from the power system.

The network
model is usually the same model used in other security analysis
applications, so it must be accurate and must reflect the real world
power system in order to provide realistic and useful results. For
many utilities, in order to be accurate the size of the network model
will be several hundred or even a few thousand "buses" (connection
points for electrical components of the model) and "branches"
(connected components of the model, between the buses). The network
model may be reduced or simplified from its real world configuration,
containing fewer buses and fewer electrical components than are shown
on the detailed one-line diagram of the system. However network
engineers prepare the model with enough detail to provide a good
simulation of the operation of the real power system, with accurate
results.

The network
model is simply a static set of parameters and equations, but it
cannot be "solved" (i.e. used to calculate results) until it is
"initialized" by entering "starting" values for the simulated power
system. These starting values are the real world starting point for
the algorithm, so that it works with real data that reflects the
current operating conditions in the power system. Initialized values
are the real world reference for the network model.

Initialized
values include bus voltages, production levels for each generator,
loads, and power interchanges with neighboring utilities. Initial
values are sometimes taken from the current SCADA database
(measurements from field transducers) at the control center.
Preferably the initial values are taken from the State Estimator
database (if this application exists and is reliable), because these
values are estimated and are more accurate representations of the
actual state of the power system. Other parameters such as operating
and equipment limits, and generation participation factors are also
taken from the SCADA database to be used as references for calculating
overloads and violations.

The multiple
sets of limits that may be used for power system operations and for
security analysis is a complex subject that is beyond the scope of
this narrative about CA.

With an
initialized power network model, contingency analysis can now be
executed with a series of contingency events that is prepared by the
CA user. A "contingency list" contains each of the elements that will
be removed from the network model, one by one, to test the effects for
possible overloads of the remaining elements. The criteria for
selection of elements for the contingency events are further described
below.

In its basic
form, CA executes a "power flow" analysis for each potential problem
that is defined on a contingency list. The power flow (sometimes
called a load flow) is the name of the algorithm used by contingency
analysis to solve for the currents, voltages, and real and reactive
power flows (MW and MVA) in each part of the power system. A "network
solution" consists of these calculated results for every bus and
branch in the power network model.

The failure or
outage of each element in the contingency list (e.g. a loss of a
generator or a transmission line) is simulated in the network model by
removing that element. The resulting network model is solved (i.e.
computer programs solve the complex matrix equations that make up the
power flow algorithm) to calculate the resulting power flows,
voltages, and currents for the remaining elements of the model.

Results of each
contingency test – the network solution – are compared with the limits
for every element in the power system. For example, a transmission
line that was loaded at 85% of its MVA rating before the contingency
event, might now be loaded at 120% of its rating after the event.
Similarly a load bus voltage may fall to 90% of its nominal value, due
to the same contingency. If limit violations occur, these are arranged
in a tabular list according to how serious the overloads or violations
are. The list of violations is saved in the CA database. The CA
process continues - the network model is reset to its initial
operating conditions, and the next contingency (element outage) is
applied and analyzed. This process continues one after another, until
all the contingency events on the test list are examined. All the
violations resulting from each contingency, one list per contingency,
are saved in the CA database for review by users.

Typically the
power system model is tested for many hundreds of possible problems,
including the failure of each generator and line, as well as other
elements. These events are placed on the contingency list by
experienced planning and operations engineers because of their
importance - the severity of their effects, and their likelihood
(probability) of occurrence. Establishing the contingency lists is a
result of planning studies that use power flows to identify the
sensitive areas of a power network, under various loading conditions.
In practice these sensitivity studies can reduce the number of
contingencies that need to be evaluated by CA, to study only the most
serious and likely events.

Large computer
resources are needed to process a power flow solution for each
contingency in a large power system composed of many hundreds of
elements, especially when these studies are conducted for several
operating states and loading levels of the system. If voltage
violations and reactive power flows are of most concern in a
particular system or operating state, then a complete AC power flow is
required for each contingency.

Execution times
for testing hundreds of contingencies have of course been reduced
significantly over the past 30 years, and it is now possible to
execute the CA in a few seconds with current control center computers.
Other methods are used in practice to further improve CA execution
times, such as the use of simpler DC power flow analysis when
approximate MW power flows are more important than voltage limits on
buses. Therefore CA can be used not only as a system planning tool,
but is "fast enough" to be used as an on-line analysis tool by power
system dispatchers and network engineers, to support preventive and
corrective operator actions in case of problems.

### Results and use

The results of
the CA are compared against safe operating and stability limits for
each element of the power system being studied. Violations for each
overloaded element are shown in lists (e.g. "For contingency #1 outage
of generating unit G001, line L123 exceeds normal MVA limit by 50%").
The results of the contingency analysis are organized by ranking of
their severity –the most overloaded elements of the power system
appear at the top of the list. Lists can contain hundreds of entries,
but typically the most important violations are in the top 50, and
these indicate the major problem areas.

In practice
there can be more than one operating limit for many elements of the
power system, such as short-term and long-term thermal limits (e.g.
ambient temperature and the duration of an overload affect the safe
operating limits for transformers and transmission lines). There can
also be several stability limits for lines and interconnections,
depending on the configuration and the operating state of the power
system (light, medium, or heavy loading). All of these limits are
checked by CA, upon selection by the user.

In the real
power network, if limits are exceeded after the first contingency
event happens, protection equipment will react and remove overloaded
equipment from the power system. This can create further overloads,
resulting in cascading outages, which could eventually collapse the
power system in a complete blackout.

Therefore the
results of CA are used initially by system planners, to study the
effects of outages and to establish secure operating limits and
constraints for the power system under different conditions.
NetworkEngineers use CA as a study tool to develop corrective actions
in predefined "cookbooks" for system operators, to improve their
ability to resolve problems. In addition CA is used as an on-line
decision support tool to assist the operators' understanding and
correction of unusual situations, by looking at the effects of
possible outage events.

### Current CA implementation

In current
Energy Management Systems and planning departments, CA is no longer a
separate application, and is often an extension of the power flow or
optimal power flow applications. This allows the related applications
to work from common network models and base cases, and provides a
single point of editing and maintenance.

Since the
results of contingency analysis are used to define operating limits
and constraints for the power system, combined applications have
evolved such as Security Constrained Economic Dispatch, Security
Constrained Unit Commitment, and Security Constrained Optimal Power
Flow. These advanced applications use the CA results to directly
provide operating limits and constraints as part of their results, to
streamline the process instead of using separate applications to come
up with the same results.

### CA evolution, users and future

Contingency
analysis was originally (in the 1960s) such a computer intensive
application that its use was limited to power system planners, for
evaluating the design of the power system and to develop operating
constraints and corrective measures for the dispatchers. Analysis was
performed in off-line computers, often in large mainframes or
specialized engineering minicomputers. Results were typically
available only after many hours of computation, with huge stacks of
paper printouts (remember those?) needing days of line-by-line
analysis by power system experts.

Due to vastly
increased computer power and the use of special selection techniques
to minimize the contingency events that need to be examined, in 2004
the CA application has become very fast. Results are available in
seconds and graphical display tools allow quick visual analysis. CA
can therefore be used as an on-line operations support tool, by
dispatchers and network engineers.

However CA is
still a complex application, and like many of the security analysis
applications, its acceptance for on-line use by system dispatchers has
been limited. Procedures that are acceptable for backroom analysts are
not adequate for busy operations staff. The workload of executing
regular power dispatch and switching tasks, reacting to problem
situations, and entering data for reports, does not leave much time
for the dispatcher's use of advanced security analysis applications.
Relatively complex initialization, data entry requirements, and
infrequent use also mean a re-learning curve that further affects its
acceptance. Future improvements in the human interface and set up
procedures may increase the use of CA as an on-line tool.

CA is used in a
wider arena, for analyzing huge power pool and wide area networks for
operating regions such as the Midwest ISO (Independent System
Operator). Power marketing and trading entities, as well as the ISOs
and TSOs (Transmission System Operator), have driven some of these
requirements. For these very large network models, further
improvements in execution time, user tools and results presentation
will be needed in order for the application to be effective.

### Data Inputs and Outputs

The CA
application requires data inputs from many sources, including:

* equipment lists
  for the power systems to be studied
* contingency lists
  of the selected elements to be studied
* sets of limits
  for power system elements (lines, generators, transformers, etc.)
* base case
  "starting" data to initialize the network model (often this is the
  current network solution taken from the state estimator application)
* other base cases
  for studies of other power system operating states (saved cases from
  the study power flow application)
* power system
  loading models (these may be part of the base cases)
* "triggers" to
  start the application, such as automatic execution upon loss of a
  power system element, periodic execution as part of the security
  analysis sequence, or manual execution "on demand" by a user

In addition, CA
users enter or select data such as:

* definition and
  selection of contingencies (list of outages to be analyzed, activate
  or deactivate violation checking, etc.)
* selection of base
  cases (initial conditions for the power network model)
* execution control
  parameters (groups of contingencies, participation of units in
  generation loss, number of highest priority contingencies to be
  processed)
* enable automatic
  grouping of switching devices to define an element outage
* enable generation
  of warnings and alarms (usually for on-line users)
* severity ranking
  of contingencies (various factors can be used and weighted to rank and
  display the limit violations, such as branch current or MVA flow, bus
  voltage, reactive power generation, bus voltage shifts, reactive power
  shifts, etc.)
* adjustments to
  the weighting factors
* stop the CA
  execution at certain points in its sequence

The CA
application provides several outputs, such as:

* displays for
  users to set up and control the application
* execution status
  and problem displays, showing progress and non-convergence situations
* results – in the
  form of many types of contingency violation lists, according to
  severity, type of equipment, loss of generation or load, equipment
  affected by multiple contingencies, creation of islands, etc.
* results – in the
  form of many types of graphical displays, showing the overloads on
  one-line diagrams with color codes for severity, flags for types of
  problems, graphs, and even 3D representations of groups of analyses,
  etc.
* visible warnings
  and audible alarms for operations staff and dispatchers, and sometimes
  for study users, to alert them about potential problems if certain
  contingencies should occur in the future

### Shortcomings in Current Contingency Analysis

As mentioned
previously in section 1.4.5, the CA application has some shortcomings
in current practice. Some of these result in CA being more useful as
an off-line planning tool than as an on-line tool for operators. Other
shortcomings restrict its capability in identifying problems outside
the immediate control area that could impact the control area, or
limit the effective conversion of its voluminous numerical results
into meaningful information and intelligence for operations use.

Some of the CA
shortcomings could be addressed with an improved communications
architecture, which would support the use of more, more frequent,
higher quality, and wider-area data. This would enhance CA to form one
of the tools necessary for the future "self healing grid" that IntelliGrid Architecture project is helping to define. In the list below, the CA
shortcomings that are candidates for improvement with an advanced
communications architecture are marked with an asterisk (\*).

The list of CA shortcomings includes:

(a) Lack of Reliability and Robustness in the CA
solution "engine"

* "touchy"
* "sensitive"
* breaks easily
* sometimes needs
  assistance by a programmer-analyst and a network engineer to resolve
  problems

(b) Usability – difficult to set up and use CA

* Complex
  application
* Sometimes needs
  programmer-level entries in "code"
* Sometimes minimal
  use of dialogue boxes and menus for users
* Access to various
  data sources is not consistent
* Access to
  alternate and wider area data (to resolve situations of faulty,
  incomplete or missing data, needed for dependable solutions) is rarely
  provided (\*)
* Definition and
  selection of contingencies can be lengthy
* Poor user guides
* Poor or no
  scripts to follow
* Lack of default
  entries, "prompts" and "help" features

Summary - CA can be flexible and capable, but is
rarely an "elegant" application; it needs an intuitive interface and
better user features.

(c) Difficult for users to interpret the
avalanche of numeric CA results

* Summaries of
  overloads and violations are usually tabular displays, without being
  integrated in one-line diagrams for easier association with the power
  network
* Few or no graphic
  tools to assist interpretation of hundreds of numbers
* Comprehension of
  CA results can be relatively slow for new users

Summary - not an intuitive output style.

(d) Restricted visibility - not always a "wide
area" or regional solution (\*)

* May not show the
  problems at boundaries of the power system (\*)
* Without a large
  area model, CA can not show problems that start in remote locations,
  beyond the local control area (\*)
* Does not always
  "see" accurate topology, even in the local control area

(e) Few or no remedial action suggestions for
operators

* rarely provides
  operator "action lists", especially for unusual situations
* does not suggest
  remedial actions for wide area implementation, using coordinated
  multi-utility operations (\*)

(f) Slow performance

* Can sometimes be too slow for operators
  to use effectively for decision support, although modern computers can
  handle most requirements

(g)
No intelligence or learning from previous cases

CA can be initiated from previous base cases, but the
application is not equipped with intelligence to learn from previous
cases:

* How to assist the
  set up procedure, using self-start procedures
* How to resolve
  difficult situations (for example by trying or suggesting fixes to
  problems, such as interrogating and using alternate data sources) (\*)

(h) Relatively isolated application, no links
with Equipment Condition Monitoring (for revised limits and
integration with outage scheduling for maintenance) or Phase Angle
telemetry (operating conditions could trigger the CA analysis) (\*)

* CA shows its
  "study function" roots, since it is not usually linked with real-time
  triggers or telemetry
* Closer coupling
  with equipment condition and state measurement telemetry would enhance
  the value of CA (\*)

(i) Rarely coupled with the Training Simulator

* CA study cases
  should be easily transferable to the Training Simulator for use in
  building scenarios

These and other CA shortcomings combine to make
it less effective than its potential as a refined and usable decision
support and guidance tool for operations.

The interim report on the August 14, 2003
blackout ("U.S. – Canada Power System Outage Task Force, Interim
Report: Causes of the August 14th Blackout … November
2003") refers to some of these CA shortcomings, such as restricted
visibility of the regional power system, and the need for correct
topology data.

The "future" Contingency Analysis will be defined
(in another template) to improve many of these current shortcomings,
and to make CA a key component of the "self healing grid" of the
future.

## Steps

### Contingency Analysis Off-line Study Mode Sequence = CA-SM steps

 

| **#** | **Event** | **Name of Process/ Activity** | **Description of   Process/ Activity** | **Information Producer** | **Information   Receiver** | **Name of Info Exchanged** | **Additional Notes** | **IntelliGrid Architecture Environments** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Outage request  Or  Change study request  (can split these later into separate sequences if necessary, but each request initiates the same steps) | Initiate CA study | Initiates the Contingency Analysis study, by:  ·          a request for off-line analysis of an equipment outage request or  ·          a change (to the power system) request | Field Equipment Maintenance Mgmt System, System Planner | CA User (SM) | Outage request, Change study request | CA User (SM)  (a generic user to represent the Equipment Outage Planner  and Scheduler, or the System Planner) | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.2 |  | Set up CA study | CA user sets up the CA study, by using CA displays to feed/input/acquire the necessary network model and data from the EMS databases, and by using manual entries.  Notes:  ·          several elements of data are required to "set up" a CA study;  ·          these elements can be acquired from many sources, however all necessary data is available through the EMS databases;  ·          this process becomes more complex for a future study case | EMS Database, External Computer System, DAC | Contingency Analysis System | Network model, Base case initial data | Communications issues: interfaces and data exchange and performance | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.3 |  | Adjust the network model | CA user adjusts the network model to represent the power system configuration to be studied. The user performs this by manually removing equipment from a base configuration, or possibly by adding equipment. | CA User (SM) | Contingency Analysis System | CA study model | Communications issues: may need access to stored future data and historical data | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.4 |  | Define contingency list to be used | CA user defines the list of contingency events to be used in the study. Includes making manual adjustments to stored lists retrieved from the EMS database.  This list could range from a few outages to be evaluated, to thousands of outages to be simulated. | EMS Database | Contingency Analysis System | Contingency list |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.5 |  | Set CA execution parameters | CA user sets the CA execution control parameters, to define constraints and outputs. | CA User (SM) | Contingency Analysis System | Execution parameters |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.6 | CA user starts contingency screening process ("start" button) | Screen for worst contingencies | CA application performs a quick check to screen (identify) the worst contingencies, and displays these to the user.  Note: users may choose to skip this step and instruct the application to proceed directly to the "complete analysis" step 1.7. | Contingency Analysis System | CA User (SM) | Screened contingency list |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.7 | CA user starts complete analysis for the worst contingencies | Perform complete analysis of the worst contingencies | CA application performs a complete analysis of the worst contingencies, to calculate and display the branch overloads and voltage violations for each outage. | Contingency Analysis System | CA User (SM) | CA results | Performance and visualization issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.8 |  | Reviews and interprets CA results | CA user reviews and interprets the CA results.  Typically results are presented in summary tabular displays, however graphic display techniques can assist interpretation of voluminous results. |  |  |  | Presentation and visualization issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.9 |  | Saves results | CA user initiates the printing and "save" of CA results in the EMS databases.  User may transfer the CA study model and results to the Training Simulator (an external system). | CA User (SM) | EMS Database, External Computer System | CA results | Communications issues: interfaces and data exchange | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.10 |  | Issues report | CA user issues report based on the CA results: an outage approval, or a report on the effects of the proposed change to the power system.  Report templates and forms are typically available from the CA application and EMS.  May also affect the annual maintenance and outage plan. | CA User (SM) | Field Equipment Maintenance Mgmt System, System Planner | Outage approval, Change study report |  | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |

 

| # | Event | Name of Process/Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.7.1 | CA solution fails | Alerts user of failure to solve | CA display alerts the CA user when it cannot solve the network model, usually because of incomplete or faulty data. | Contingency Analysis System | CA User (SM) | CA error messages | Application robustness and problem diagnostic issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.7.2 |  | Adjust CA input data | CA user (with help from network model engineer and/or database support analyst) adjusts CA input data and/or the network model to fix the problem.  Usually involves manual entry of data corrections. | Power Network Model Engineer, Database Administrator | Contingency Analysis System | Base case initial data, CA study model | Application robustness and problem diagnostic issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 1.7.3 | Return to regular CA-SM sequence |  | After problems are resolved, the regular CA-SM sequence continues.  Go back to step 1.7 |  |  |  |  | NA |

## Start a Second Sequence

### Steps to implement Contingency Analysis On-line Operations Mode Sequence (OM)

Note: This mode of use of Contingency Analysis is
very similar to the off-line study mode, except that:

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
> (usually every few minutes)
>
> ·       
> the application looks at contingencies
> starting with the current operating situation (not future
> situations), and uses the current power system data and
> State Estimator data to initiate its network model
>
> ·       
> operators typically do not interact with the
> application or initiate their own studies; it is more of a
> "look only" advisory tool
>
> ·       
> the on-line CA provides visual warnings and
> even audible alarms to operators, to notify them of
> overloads and violations that would occur if certain
> contingency events happen in future (i.e. a "what if"
> preview of the effects of future outages)
>
> ·       
> Baseline CA does not usually extend to
> providing suggested lists of remedial actions, which could
> be performed by operators to correct potential problems.

### Contingency Analysis On-line Operations Mode Sequence = CA-OM steps

| # | Event | Name of Process/ Activity | Description of   Process/Activity | Information Producer | Information   Receiver | Name of Info Exchanged | Additional Notes | IntelliGrid Architecture Environments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 | Periodic "start CA" command from the execution control program | Initiate on-line CA execution | Initiates the Contingency Analysis in periodic cycles (typically every few minutes) using the application execution control program (security analysis sequence). |  |  |  | Communications issues: gather data fast enough to support on-line use of CA | NA |
| 2.2 | CA results presented to users | Present on-line CA results | Presents the on-line CA results in displays for the users to consult and monitor; revised results are presented after every CA execution cycle, typically every few minutes | Contingency Analysis System | CA User (OM) | CA results, CA warnings and alarms, Remedial action suggestions | Presentation and visualization issues | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |
| 2.3 | User action | Action by users of on-line CA | CA on-line users may react to the CA results and remedial action suggestions by:  ·         System Operator: Planning remedial actions, to be ready if a contingency event occurs  ·         Outage Coordinator and Network Engineer: Implementing or postponing a scheduled outage  ·         System Operator: Making remedial action changes to the power system to reduce exposure to problems in case of a contingency event | CA User (OM) | DAC, Field Equipment Maintenance Mgmt System |  | Communications issues: output commands to DAC and field devices | [Intra-Control Center](../Environments/Env7_Intra-Control_Center.htm) |

## Additional Information

### Actor (Stakeholder) Roles

|  |  |  |
| --- | --- | --- |
| ***Grouping (Community)*** | | ***Group Description*** |
| ***Actor Name*** | ***Actor Type (person, device, system etc.)*** | ***Actor Description*** |
| System Planner | Person | Prime actor and off-line CA user. Engineer who studies the power system to ensure overall system security, with the ability to withstand at least the first major contingency (failure event). Assists with planning and evaluating changes to the power system, such as the addition of substations and transmission lines. |
| Equipment Outage Planner  and Scheduler | Person | Prime actor and off-line CA user. Engineer who responds to outage requests from field maintenance personnel ("can I take this equipment out of service from XX to YY date?" by evaluating the impact on power system security if the equipment is withdrawn. Schedules equipment outages for minimum risk (to avoid same-time outages of key equipment), approves outage requests for execution by operators, and assists with the preparation of the annual maintenance schedule for the complete power system. |
| CA User (SM) | Person | Generic "stand-in" user actor for the SM = study mode, representing either of the main off-line CA users – the power system planner or the equipment outage planner/Scheduler.  For simplicity, this generic actor is used in the sequence steps for the CA off-line study mode. |
| Energy Management System | Computer system (single machine or distributed network based) | The computer system that supports computation through various applications (including Contingency Analysis), the user interface (displays), data input and output, communications (internal and external), storage in its databases, and other functions.  The Energy Management System  is an actor in the sense that it is responsible for the control and execution of these many functions, including CA. |
| EMS Database | Stored information in computer memory or on media | Main repository of the real-time and static information used by Contingency Analysis and its human actors, and by other EMS applications. Responsible for:  ·         finding, organizing, storing and providing the data requested by CA and other applications, and needed by the user displays, and  ·         storage of CA results.  The EMS databases provide the power system data (collected by the DAC application) including real-time information, and the State Estimator solutions for initializing CA studies that are based on the current operating conditions. |
| Contingency Analysis System | Computer program(s) and displays | The solution engine within the CA application that solves the network model for each contingency event, and calculates the CA results.  Also includes user interface (UI) displays provided by the EMS and the CA application for data input and information output. Displays are used to set up and control the application, enter and modify input data, view results, and save/transfer results. Typically these are tabular/character displays, but advanced graphical presentations are sometimes used to assist the interpretation of results. |
| System Planner | Person(s) | Note: This description is included for background information only; this secondary actor does not need to be "modeled".  Engineers and technicians who are responsible for power system planning. They provide change study requests to the power system planner (a CA user) in the form of planned modifications to the electric power system, using drawings and written specifications. These include changes such as system expansion and equipment upgrades due to load growth, reliability and security improvements, replacement of outdated equipment, and the addition of new transmission lines and generation facilities. |
| Field Equipment Maintenance Mgmt System | Person(s) | Note: This description is included for background information only; this secondary actor does not need to be "modeled".  Engineers and technicians who are responsible for power equipment maintenance (for generators, power lines, transformers, etc.) and preparation of the annual maintenance and outage plan. They request outage approvals from the outage planner and Scheduler (a CA user), in order to withdraw equipment from service for maintenance. These outages can range from a few hours to many months in duration. |
| Power Network Model Engineer | Person | Note: This description is included for background information only; this secondary actor does not need to be "modeled".  Network Engineer specialist, who maintains the model of the power system (used by CA and other control center applications) to keep it current, and consistent with the utility's and the neighboring utilities' configurations. Uses the future configurations of the power system (according to the annual maintenance plan) to define power network models for future studies. |
| Database Administrator | Person(s) | Note: This description is included for background information only; this secondary actor does not need to be "modeled".  Database analyst who performs changes to, and resolves problems with, the various databases in the EMS that CA uses. |
| External Computer System | Devices | Note: this may be a primary actor (grouped as a single actor for simplicity), and could be divided into systems that are within and outside the utility. However practically all external data is provided through the EMS databases.  Sources of other data used by CA for its solutions. These include:  ·         other computer systems within the utility (e.g. power equipment parameters are stored in a different computer system), and  ·         computer systems at other power utilities which provide necessary data about neighboring power systems, using data links and other communications methods. |
| DAC | Subsystem and application in the EMS or SCADA system | Collects most of the real-time and wide area data for the EMS databases.  Also, for on-line CA, DAC is the receiver and processor of control commands to field devices in the power system.  Operators can use DAC to perform remedial actions, if these suggestions are part of the CA results (i.e open breakers, increase generation, etc.). |
| System Operator | Person | Primary user of on-line CA. Also called a "Dispatcher". Person who "operates" the power system using the DAC (data acquisition and control) application in the EMS and/or SCADA system. Typical operations include monitoring power flows and voltage levels, switching equipment in and out of service (opening and closing breakers and switches by remote control), adding and adjusting generation sources (by remote control or using voice communications to field operators) to match the loads, and managing the operating conditions of the power system in real-time.  In many utilities operators use CA as a source of "preview" alarms (or warnings) to show the violations that **could occur** (or are imminent) as a result of a future equipment failure (contingency). CA runs periodically to "look ahead" at potential future problems.  An equipment failure event can also trigger CA to execute in a real-time advisory mode for operations support, to provide these "preview" alarms or warnings in case of a next contingency event.  A typical CA display is non-graphic and shows the operator a summary of violations with the name of each important contingency event. Details about specific violations and overloads are available in other tabular displays. In advanced Energy Management Systems, suggested remedial actions may be displayed as a list of procedures for operators to use to remedy overload situations. |
| Outage Coordinator | Person | User of on-line CA. The outage coordinator manages the short-term weekly and daily equipment outage schedule, approves each scheduled outage before it is implemented by operators, and advises operators during the equipment withdrawal procedures.  The outage coordinator may use CA as a "quick check" in the on-line mode using the current operating conditions, to make sure that a planned equipment outage will not create problems (violations and overloads). For this mode, easy setup and fast results (i.e. high performance) are necessary. |
| Network Engineer | Person | User of on-line CA. The network engineer is an expert in the power system who advises operators (usually upon request) before and during their execution of complex or unusual procedures. He also monitors the current operating conditions and the CA results.  The network engineer may use CA as a "quick check" in the on-line mode, to validate procedures and try "what if" scenarios. Again, easy setup and fast results (i.e. high performance) are necessary. |
| CA User (OM) | Person | Generic "stand-in" user actor for the OM = on-line mode, representing any of the main on-line CA users – the operator, outage coordinator, or network engineer.  For simplicity, this generic actor is used in the sequence steps for the CA on-line mode. |

### Information exchanged

| ***Information Object Name*** | ***Information Object Description*** |
| --- | --- |
| Outage request | Document form, electronic and paper  The outage request is a form submitted by field maintenance personnel to the equipment outage planner and Scheduler. It requests approval to take equipment out of service for a defined period of time, for a specific reason. Sometimes the outage request includes an estimated "return to service time" if it is a short outage on critical equipment that might be quickly needed back in service. |
| Outage approval | Document form, electronic and paper  Approval form issued by the outage planner and Scheduler, to approve the equipment outage and schedule it for a specified date/time/duration. Operations and maintenance personnel would then perform the equipment outage procedures. |
| Change study request (study of a power system modification) | Document drawing and description, electronic and paper  Notice of a planned change to the power system (e.g. the addition of a substation) to be studied. The system planner reviews this change using CA, to evaluate the impacts on the modified configuration in case of contingency events (equipment failures). |
| Change study report | Document drawing and description, electronic and paper  Report prepared by the system planner from the results of the CA study, which accepts, accepts with modifications, or requests further study about the planned change. |
| Annual maintenance and outage plan (or similar names) | Document, electronic and paper  Plan used to schedule the un-availabilities for power system equipment. Consulted to determine future planned configurations of the power system. Used for studies of new outage requests and for risk assessment by operations. Is refined into monthly and weekly outage schedules throughout the year, to reflect current operating conditions of the power system. |
| Network model | Stored files on computer media  Static simulated model of the power system, used by CA and other EMS applications such as the power flow analysis. This model uses the parameters and characteristics of the real-world power system and "behaves" like the real system for the purposes of studies. Can be a model of the current power system, or of a future configuration of the power system. |
| Base case initial data | Stored files on computer media + Manually entered data  Data that CA obtains from the EMS databases in order to set up the network model before executing the analysis. Includes data that is entered manually by users.  Sometimes the base case is for a study of a future operating condition of the power system, requiring a future "picture" of the network and its parameters. |
| CA study model | Temporary or stored file  Network model that has been adjusted by the CA user, by removing or adding equipment until it represents the desired starting point for the CA study. |
| Contingency list | Document, electronic and paper and Temporary or stored file  List of contingency events (equipment outages) that is prepared by the CA user, and input to CA as the list of events to evaluate. Typically a base contingency list is retrieved from the EMS database and manually enabled and modified by the user (on displays) before it is ready for CA to use.  These lists can range from a few selected items of power system equipment, to thousands of elements of the power system. They are the "test scripts" for CA execution. |
| Execution parameters | Stored files on computer media + Manually entered data  Control parameters (enable or disable certain features of the application, and enter values) that the CA user selects from menus or enters manually, to set up the behavior and functionality of the application. |
| Screened contingency list | Document, electronic and paper, and Temporary or stored file  List of the most serious equipment outages that are selected by the CA screening process (or manually selected by the CA user) to undergo a complete analysis to determine the severity of violations and overloads. |
| CA results | Document forms and graphic pictures, electronic and paper  Lists of bus voltage violations and branch overloads, shown in displays and on printouts. Typically these results consist of long lists of numbers sorted by priority – worst case violations/overloads are shown at the top of the list. New visualization technology incorporates graphic pictures for easier interpretation of results.  CA users also provide written reports to summarize these results for other departments. |
| Stored CA results | Data files  CA study results are stored in the EMS databases for review by system planning, outage scheduling, and operations personnel. They can also be accessed by or transferred to the Training Simulator, for use in building training scenarios for operations personnel. |
| CA error messages | Temporary or stored file  The CA application issues notification to the users of any problems with its execution, so that the user can adjust the model or provide additional data inputs to correct the problem. |
| CA warnings and alarms | Temporary or stored file  For on-line users the CA application can issue warning messages and even audible alarms, to notify operators about overloads or violations that WOULD occur IF certain contingency events happen in future. These are essentially "preview" warnings or alarms about the effects of possible future events. |
| Remedial action suggestions | Temporary or stored file  In some advanced implementations of baseline current Contingency Analysis, the application can provide suggestions for operators to correct potential overloads and violations. These would typically consist of suggestions to adjust or add generation, reduce load, adjust power system voltage levels, add reactive VAR resources, isolate a problem area, etc. |

### Activities/Services

| ***Activity/Service Name*** | ***Activities/Services Provided*** |
| --- | --- |
| Identify the most serious contingencies for detailed analysis | Contingency Analysis (CA) performs a quick screening of the hundreds or even thousands of possible equipment outages (contingencies), and identifies the few (typically 10-50) that would have the worst effects on the power system. |
| Analyze the most serious contingencies and quantify the effects of each | CA performs a complete analysis of the most serious contingencies, to calculate the magnitude of branch overloads and voltage violations for individual elements of the power system. These "what if" simulations are the main tool for ensuring secure power system operation in case of equipment failures or planned equipment outages. |
| Organize the analysis results (by severity) and display them to users (both on-line and off-line use) | CA presents the overloads and violations in order of their severity, in tabular lists. These are displayed and can be stored for reference.  For on-line use by operators, summary displays show highlights of the CA results, such as the names of contingency events that would result in severe overloads, and the number of these overloads. |
| Issue warnings and alarms to operators (on-line use) | CA issues warning and alarm messages to power system operators, to alert them about the effects of **future** contingency events (i.e. a preview) that would result in branch overloads and voltage violations. |
| Save results and cases for reference | CA users can save results and the study cases (power system conditions), for future review. |
| Transfer study cases to the operator training simulator for use in training | CA users can send interesting study cases to the operator training simulator, for use in training scenarios. |

### Contracts/Regulations

| ***Contract/Regulation*** | ***Impact of Contract/Regulation on Function*** |
| --- | --- |
| Deregulation and competition (FERC Orders 888 and 889, etc,) | May restrict the sharing of power system data (especially equipment unavailabilities) among competing utilities (and related companies), which could limit the Contingency Analysis solutions to the "observable" network, instead of a wider area solution. |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ***Policy  if !supportLineBreakNewLine?   endif?*** | ***From Actor   if !supportLineBreakNewLine?   endif?*** | ***May*** | ***Shall Not*** | ***Shall*** | ***Description (verb)*** | ***To Actor*** |
| NERC Operating Policy 2.A – Transmission Operations | NERC |  |  | X | Operate the power system in a secure and reliable manner, using security analysis tools to recognize and avoid problem conditions.  "All control areas shall operate so that instability, uncontrolled separation, or cascading outages will not occur as a result of the most severe single contingency."  (voluntary reliability guidelines and standards for utilities) | System Planners and System Operator |

 

|  |  |  |  |
| --- | --- | --- | --- |
| ***Constraint*** | ***Type*** | ***Description*** | ***Applies to*** |
| Thermal limits of power system equipment | Engineering | Flow limits (maximum current and MW) to be respected in order to avoid damage to, or premature aging of, power system equipment (such as generators, transmission lines, transformers, breakers, etc.). Used by CA to calculate overloads. | Contingency Analysis System |
| Stability limits for transmission lines and corridors | Engineering | Flow limits (maximum MW and MVA) for transmission lines and corridors, to be respected in order to maintain power system stability. Used by CA to calculate overloads. | Contingency Analysis System |
| Voltage limits | Engineering | Voltage limits on buses (high and low) to be respected in order to maintain secure and stable operation of the power system. Used by CA to calculate violations. | Contingency Analysis System |
| Need for fast solutions (a) | Performance of the application (computer resources) | For on-line use by power system operators (decision support), CA must provide fast solutions, within seconds of an event. Current (2004) computer resources can meet this constraint. | Energy Management System |
| Need for fast solutions (b) | Performance of the application (application design) | For on-line use by power system operators (decision support), CA must provide fast solutions, within seconds of an event. Current (2004) CA application barely meets this constraint. | Contingency Analysis System |
| Need for robust application | Reliability of the application (application design and features) | For both off-line and on-line use, CA must be reliable – it must provide solutions even in difficult situations with limited input data. | Contingency Analysis System |
| Need for ease-of-use of the application | Usability of the application (application design and user interface) | In order to be useful for on-line analysis and decision support, the CA application must be easy to use, without requiring a programmer's skills. | Contingency Analysis System |
| Need for fast analysis of the results | Usability of the application (application design and results presentation) | The CA application must present its voluminous numeric results in a manner that can be quickly understood by users, especially for on-line use. This requires summary displays and graphical displays that are designed for easier interpretation. | Contingency Analysis System |
