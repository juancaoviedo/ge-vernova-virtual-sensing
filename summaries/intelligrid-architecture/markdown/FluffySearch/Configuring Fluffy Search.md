# Configuring Fluffy Search

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/FluffySearch/Configuring Fluffy Search.htm

---

![Fluffy Search](Configuring Fluffy Search_files/fs.gif)   
... [from the developers of
**Ignite**](http://www.ignite-it.co.uk/)
[![Ignite: Web graphics optimization with edge!](Configuring Fluffy Search.htm)](http://www.ignite-it.co.uk/cgi-bin/pa/fsearch)

[Home](http://www.fluffy.co.uk/fs/index.html)

[Documentation](http://www.fluffy.co.uk/fs/docs.html)

[Overview](http://www.fluffy.co.uk/fs/docusing.html)

[Requirements](http://www.fluffy.co.uk/fs/docrequire.html)

[Configuring](http://www.fluffy.co.uk/fs/docconfig.html)

[Searching
etc](http://www.fluffy.co.uk/fs/docinas.html)

# Configuring Fluffy Search

Fluffy Search must be configured for your own web site. This is quite simple.
You only need to edit two files.

## The .config file

After you have unpacked the Fluffy Search archive into a directory of it's
own, you need to alter the .config file. The archive contains two starting
points, fluffysearch.config.unix and fluffysearch.config.nt,
for UNIX and NT based systems respectively. Choose the correct one for your web
server, rename it fluffysearch.config and delete the other.

Load fluffysearch.config into your text editor. This is a perl
script, but don't let that worry you. It's really quite simple.

Each configurable option is defined as a perl variable. These are always in
the form:

$*name* = '*value*';

where *name* is the name of the config option, and *value* is what
you want to set it to. (Some options are set in slightly different ways, but
we'll discuss them as we come to them. And as an exception, if you set an option
to a number, you don't need the quotes, shown in red above.)

Note that all directory names **do not** have ending '/' or '\'s. If you
put them in, things may not work.

We'll now go through each option in turn.

### docroot\_disc

Set this to the full directory name of the directory on the disc in which
your documents start. This is the directory that you FTP your documents too.

However, what you see when you FTP in might be misleading, since the average
web server doesn't place you in the root directory of the server when you log
in, but instead in your 'home directory'.

So, for example, you might see your document root as public\_html but
in fact it's really /home/user/public\_html on a UNIX system. You need
to use this fully qualified path, which starts with '/'. Typing pwd at
an FTP prompt might give you the answer you need, but if you're not sure, ask
your system administrator.

On an NT based server, it's a little different. You might have a root which
looks like c:/inetpub/wwwroot. (NT usually uses '\' as a directory
separator, but you can use '/' instead in the config file. It helps to avoid
confusion, since the web based paths must use '/' whatever platform the scripts
are running on). Again, ask your administrator if you're not sure.

### docroot\_web

Set this to the name of the above directory, as seen on the web server. For
example, if it's seen as http://www.example.com/subsite/ set this
option to /subsite. If it's just http://www.example.com/ set
it to nothing (ie just have $docroot\_web = '';).

### Using the docroot configuation options

docroot\_disc and docroot\_web are the most important
options, as they specify where the indexer can find the documents, and where the
documents appear on the web server respectively. If they aren't set correctly,
then it simply won't work, either because references to documents won't work, or
no files will be found to index.

If you are searching your entire web site -- you want to seach all document
from http://www.example.com/ -- then you should set
docroot\_disc to the directory you upload files to for the root of the
web server, and set docroot\_web to nothing ('').

However, if you're searching in and below a subdirectory, let's say that you
only want to search a product catalogue which is located at
http://www.example.com/products/ and below, then you need to set
docroot\_disc to the location of the products directory on the
web server (the directory you FTP files to). You **must** then set
docroot\_web to /products (note there's not final /)
otherwise Fluffy Search will think that the files it's searching are located at
http://www.example.com/, which will obviously cause problems.

### index\_loc

The directory to store the index files in. Make sure you have permissions to
write files inside it, and that it's not inside the document root.
**Warning** All other files within this directory will be deleted by the
indexer, so don't use a directory with other files in it!

### search\_script

The URL of the search script as seem from a web browser, ie what you'd type
in after the server name to retrieve the page. For example, if the URL of the
script is

http://www.example.com/cgi-bin/fcs/fluffysearch.pl

you need to enter /cgi-bin/fcs/fluffysearch.pl for this option.

### page\_script

Similarly for the fcp.pl script. For example, the script might
be

http://www.example.com/cgi-bin/fcs/fcp.pl

and you will need to enter /cgi-bin/fcs/fcp.pl.

### link\_target

Used to set the target for the links. If you're not using frames, leave this
blank. Otherwise, set it to

' target="\_top"'

(note there's a space before the word target) replacing
\_top with the name of the frame whose contents you want replace with
the generated frameset.

### frames\_framename

If you're using frames, set this to the name of the frame that contains the
content in your framesets. If you're not using frames, set it to nothing to
disable this feature.

### frames\_frameset

The generic rule which tells Fluffy Search how to locate the file containing
the appropriate frameset, given a HTML file. Set this to the href you'd use if
you were linking to it from the HTML files using a relative link. For example,
to specify the file index.html in the directory above, use
../index.html

### frames\_exceptions

You can specify exceptions to the rules specified by the above two options
using this option. You can also use it to specify **all** the locations of
every frameset if you require -- but in this case, make sure
frames\_framename is set to something other than nothing.

This option is specified slightly differently to the others. You place the
entries, one per line, between $frames\_exceptions =
<<\_\_ENDEXCEPTIONS;> and \_\_ENDEXCEPTIONS. They are
formatted as

source\_directory\_name frameset\_name frame\_name

where *source\_directory\_name* is the name of the directory we're
specifying the frameset for, *frameset\_name* is the filename of the file
containing the frameset, and *frame\_name* is the name of the frame
containing the content. For example:

/shopping/socialcare /shopping/socialcare/index.html main

All directory and filenames are relative to the search root. You can have as
many entries as you need.

### index\_include

This is specified in a similar way to the frames exceptions, with one *perl
pattern* per line. You don't have to worry about the way things are specified
if you don't understand perl patterns. The files come set up to index .htm,
.html and .shtml files. If you need to change this, delete the entries you don't
need, and add extra ones for extra file types. To include a new file type, add
an entry like:

\.**ext**\Z

where **ext** is the extension you want to index.

### index\_exclude

Using this option, you can specify exceptions to the above rule. For example,
use \Atoc\.html\Z to exclude all files called toc.html.

### shtmlroot\_disc

When a page is returned with highlighting, the web server won't expand SHTML
includes for security reasons, so the page script needs to perform this
operation. You need to set this option to the root directory for shtml includes.
This will probably be the same as docroot\_disc if you are indexing from the root
level of your web server.

### webindex\_pass

The password to start indexing from a web browser.

### disable\_noindex

If you aren't using the <fcs\_ni> tags to stop the indexing of
certain areas of the pages, set this to 1 for slightly faster indexing.

### high\_start and high\_end

Highlighting simply inserts HTML tags at the beginning and end of the text to
be indexed. These two options specify what is inserted to create the highlighted
text. You can use anything you want here.

### res\_per\_page

How many results to return in each page of found pages.

### indexer\_cmd

The command to run the indexer using the fluffyindex.pl script from
a web browser. You may not need to change this, but it is the system command
used to run the script fluffymkindex.pl. It may be that on a UNIX
system you might need to specify the full path to this script, or use something
like ./fluffymkindex.pl depending on how you system is set up.

Under NT, you might need to use
<full-path-to-perl.exe> <full-path-to-fluffymkindex.pl>
to get this to run. If you are running IIS 4, you may need to make some
configuration alterations. See [this info on
using perl to run external commands](http://www.whitecrow.demon.co.uk/steve/perlfaq/io.html#io) for details. If you're running IIS 3, [this'll be
more help.](http://www.whitecrow.demon.co.uk/steve/perlfaq/iis3.html#io)

### index\_grains

If you site is especially large, increase this number to 4, 8 or 13 to create
a more granular index, that is increase the number of files written. This should
speed up searching on larger sites. Only change if you think there is a
performance problem.

A word is located in the index by looking at its first and second letters.
Taken together, they indicate which file within the index directory the
references to the keyword are found in, giving a filename like a.3.
This configuration parameter determines how many different sections (the
granularity of the index) the second letters are split up into -- the higher the
value the more files are created, and the less data stored in each. This means
that the search script has to search through less data to find the keyword it
needs, and so the search becomes faster. Increasing this parameter on small
sites may decrease performance, due to the relative inefficiency of storing lots
of small files in one directory.

### meta\_weight

For ranking the pages, if a word is found in the meta keywords tag, it counts
this number of times more than if it was found in normal text.

## The fluffysearch.html file

This file defines the header and footer for the search page. Within it,
##### is replaced by the search form and/or results. All references to
files (for images and links etc) must be absolute (that is, start with '/' to
refer to the root of the web server).

If you need to change the look for the form itself, look at the bottom of
fluffysearch.pl -- but be careful what you change.

## #!/usr/bin/perl

At the top of all the .pl files, there is a line which reads
#!/usr/bin/perl. This specifies the location of perl on UNIX machines
(and some Windows machines running Apache). It must be set correctly for the
scripts to run.

If the scripts won't run at all (maybe getting a 500 Internal Configuration
Error) these lines may need altering -- although on most UNIX systems this
default is correct, and NT IIS servers ignore it. Change the line to
#![location of perl interpreter]

## Having problems?

Fluffy Search is unsupported. However, if you email [fluffysearch@fluffy.co.uk](mailto:fluffysearch@fluffy.co.uk) we'll try
and help you out, although we can't promise an immediate response. You
**must** include a copy of your .config file in any request for
help. Emails without this will be ignored, as it is difficult to diagnose
problems without seeing this file.

< [Requirements](http://www.fluffy.co.uk/fs/docrequire.html) | [Indexing and searching](http://www.fluffy.co.uk/fs/docinas.html)
>

---

[![Ignite](Configuring Fluffy Search_files/ign.gif)](http://www.ignite-it.co.uk/)
Need blazingly fast downloads? Existing tools a bit clumsy?
**[Use Ignite](http://www.ignite-it.co.uk/)** to create
better, faster, web graphics in less time.  
Download your free 30 day
trial now!

---

(c) Fluffy Clouds Ltd 1999 | [home page](http://www.fluffy.co.uk/index.html)
