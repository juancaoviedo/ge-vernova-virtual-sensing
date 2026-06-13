# IEC61850 Parts 7-3 and 7-4 - Substation Object Modeling

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_IEC61850_Parts_7-3_and_7-4_-_Substation_Object_Modeling.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### IEC61850 Parts 7-3 and 7-4 - Substation Object Modeling

IEC61850 Parts 7-3 and 7-4 comprise the Substation
Object Models. These two Parts of the IEC 61850 specifications describe the
object models as abstract objects, and only the last parts of the standard
describes “Specific Communication Service Mapping” onto a particular set of
protocols.

Object Models (OM) are Nouns with pre-defined names
and pre-defined data structures. Objects are the data that is exchanged among
different devices and systems.

The figure below illustrates Object Models. The OM
rests on top of the SM services model and the CP communications protocols.

It should be noted that new object models are
continually being developed.  Specifically, work is under way to add a
suite of Power Quality object models to deal with sag, swell, harmonics,
snapshots, and a variety of averaged values.

The OM structure from the bottom up is described
below:

·      
Standard Data Types: common digital formats such as Boolean, integer,
and floating point.

·      
Common Attributes: predefined common attributes that can be reused by
many different objects, such as the Quality attribute. These common attributes
are defined in IEC61850-7-3 clause 6.

·      
Common Data Classes (CDCs): predefined groupings building on the
standard data types and predefined common attributes, such as the Single Point
Status (SPS), the Measured Value (MV), and the Controllable Double Point (DPC).
In essence, these CDCs are used to define the type or format of Data Objects.
These CDCs are defined in IEC61850-7-3 clause 7.

·      
Data Objects (DO): predefined names of objects associated with one or
more Logical Nodes. Their type or format is defined by one of the CDCs. They
are listed only within the Logical Nodes. An example of a DO is “Auto” defined
as CDC type SPS. It can be found in a number of Logical Nodes. Another example
of a DO is “RHz” defined as a SPC (controllable single point), which is found
only in the RSYN Logical Node.

·      
Logical Nodes (LN): predefined groupings of Data Objects that serve
specific functions and can be used as “bricks” to build the complete device.
Examples of LNs include MMXU, which provides all electrical measurements in
3-phase systems (voltage, current, watts, vars, power factor, etc.); PTUV for
the model of the voltage portion of under voltage protection; and XCBR for the
short circuit breaking capability of a circuit breaker. These LNs are described
in IEC61850-7-4 clause 5.

·      
Logical Devices (LD): the device model composed of the relevant Logical
Nodes. For instance, a circuit breaker could be composed of the Logical Nodes:
XCBR, XSWI, CPOW, CSWI, and SMIG. Logical Devices are not directly defined in
any of the documents, since different products and different implementations
can use different combinations of Logical Nodes for the same Logical Device.
However, many examples are given in IEC61850-5.

**Keywords:** Protocol, Substation Object Mapping, Object Modeling, Substation
Object Mapping, Common Data Classes, Basic communication structure, abstract
definitions, common attribute types, data attribute
