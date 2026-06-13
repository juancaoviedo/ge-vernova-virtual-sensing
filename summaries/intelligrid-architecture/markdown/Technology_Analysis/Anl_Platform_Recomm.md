# Platform Technologies

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/Technology_Analysis/Anl_Platform_Recomm.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

# Platform Technologies

 

Platform technologies are those that are
generally specified by horizontally oriented standards groups and vendors.  Platform technologies are used equally by all
industries.  Most of these technologies
are used to provide a development and run time “container” for interoperating
application components.  While
horizontally focused companies such as IBM,
Microsoft, Sun Microsystems, or Oracle generally handle the design and
implementation of these technologies, an understanding of how IntelliGrid Architecture
leverages and specializes these horizontal technologies is necessary to
understand the IntelliGrid Architecture.  This
section provides an overview of the platform technologies recommended for use
with IntelliGrid Architecture. The complete set of recommended IntelliGrid Architecture platform technologies are
described in detail in Appendix D of this volume. 

### Analysis of Platform Technologies

This section discusses two types of Platform
technologies: Operating System Platforms and Component Container Platforms.
Operating System (OS) Platforms include:

if !supportLists?·      
endif?Windows

if !supportLists?·      
endif?Unix/Linux

if !supportLists?·      
endif?Mainframe

For many years, software developers have
worked to integrate applications across OS platforms.  Complexity includes differences in
heterogeneous mechanisms and semantics concerning many horizontal services
required for interoperation.  These
horizontal services typically specified by the OS platform include but is not
limited to issues such as:

  

if !supportLists?·      
endif?Inter-process communication – What do
applications running on different machine communicate i.e. what is the common
mechanism.

if !supportLists?·      
endif?Representation of data – How is data
stored/retrieved and represented in a computers memory.

if !supportLists?·      
endif?Security – How can applications communicate
securely, share information about who are allowed to access data and then share
access information at run time.

More recently, consortia and vendors have
offered several solutions to this problem. 
Available solutions include:

if !supportLists?·      
endif?CORBA

if !supportLists?·      
endif?Java

if !supportLists?·      
endif?Proprietary Messaging Middleware

if !supportLists?·      
endif?Web Services

CORBA and Java were originally developed to
solve cross OS issues.  While both of
these technologies were supported by a wide variety of vendors, a solution
needs to be nearly universally used to be truly useful.  More recently the software industry has begun
to coalesce around the use of Web Services and even more recently Grid Services.   One could use CORBA or Java to link legacy
applications, but these technologies require a common security domain context,
function calling convention, binary data types, and way of locating and
activating remote applications. 
Additionally, CORBA and Java typically require that server applications
must be ready to service a request when the client wishes.  Thus CORBA and Java are better suited to
assembly of tightly coupled components. 
To use a post office analogy, no one waits at the front door for the
postman to arrive before mailing a package. Mailboxes provide a convenient
method for storing letters until a mail truck comes along to pick up the mail
and deposit the received mail.   One
could use email, but email has not been designed for efficient automation. 

Just as Hyper Text Markup Language (HTML) has
become the universal language of the Web, businesses have sought a similar
language for describing business data. XML has been adopted by the World-Wide
Web Consortium (W3C) and is rapidly becoming the preferred format for
exchanging complex businesses data internally as well as between E-Commerce
applications. Similar to HTML, XML allows the designer to create custom tags
and describe how they are used and thus provides the facilities to create
self-describing messages.  This capability
is independent of how transport mechanisms, calling conventions (the order in
which parameters are passed as well as how data is returned), and data
formats.  This significantly reduces the
size and complexity of legacy application wrappers.  XML- formatted business data offers standard
and extensible information formats or packages with which to exchange
information internally and with other businesses. 

Existing proprietary message-oriented
middleware products help link applications. 
In general, these software products include a message broker.  With message broker technology, a business
application can send business messages to a broker message queue for later
delivery.  The messages are then picked
up by the message broker and dispatched to other internal or external
applications. Message brokers facilitate location and technology independence
and have proven to be the best way to link loosely coupled legacy applications

In addition to message brokering, these
middleware products often include the ability to automate business processes
(data transformation and workflow).  In
doing so, they provide a single point of control for managing information flow
across multiple applications.  For
example, the generation of a bill can be automated by creating a script that
first collects meter and customer data, then sends the information to a billing
application and lastly routes the bill to an application for presentment to the
customer.  In between these steps,
message data may be manipulated so that it matches the internal data model of
these applications. 

While existing message based middleware
provides a universal solution, these products remain largely proprietary.  As a result, many companies have come
together to develop a new architecture for integration of loosely coupled
applications called “Web Services”.  Web
Services is an attempt to define a common set of communication and security
mechanism and semantic that appears to have universal support.  Web Services platforms provided by different
vendors should interoperate. 

Obviously, it is not possible to start this
effort by working with a clean slate. 
The fact needs to recognized up front that all of the existing RTOs have
working infrastructures that can’t be replaced wholesale simply because of a desire
to develop RTO data exchange standards. 
Therefore, this requires the development of a data exchange standards
implementation approach that seamlessly integrates with existing RTO
technological investments and allows for continued growth at a pace conducive
to any particular RTOs needs or desires. 
Not a trivial challenge, but one that is achievable through the use of
Web Services, coupled with an iterative implementation plan that is agreed to
by all the participating RTOs.  To
understand the method by which this goal can be accomplished, first the notion
of exactly what Web Services are, and can accomplish, needs to be elaborated
upon.

The IntelliGrid Architecture architects see Web Services as a
key common platform that must be supported by the architecture.  While it is unlikely that most utility
application will be based on a Web Services platform in the near term, given
the direction of the industry, IntelliGrid Architecture must be designed such that all the
horizontal capabilities of Web Services can be applied to the utility vertical
domain.
