# OPC Command

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_OPC_Command.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### OPC Command

**URL:**www.opcfoundation.org

This specification describes interfaces which are
implemented by any OPC Servers (e.g. Data Access, Alarm & Event, Batch) with a need for commands, and which provide the
mechanisms for OPC Clients to be notified of the occurrence of specified
command state and result information. These interfaces also provide services
that allow OPC Clients to determine the commands supported.

The basis for the execution of an OPC command is the
Finite State Machine (FSM). The FSM is an object that precisely describes the
behavior of the command in terms of states, transitions, transition conditions,
events, and actions. This provides the mechanism to convey information about
the method and sequence of the command’s execution. The FSM includes the
triggering stimulus and resulting actions related to each state transition
within the process as well as status and error data associated with resultant
states.

**Keywords:** Computational VP, Limited usage
