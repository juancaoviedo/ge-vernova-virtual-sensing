# Using Fluffy Search

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/FluffySearch/Using Fluffy Search.htm

---

![Fluffy Search](Using Fluffy Search_files/fs.gif)   
... [from the developers of
**Ignite**](http://www.ignite-it.co.uk/)
[![Ignite: Web graphics optimization with edge!](Using Fluffy Search.htm)](http://www.ignite-it.co.uk/cgi-bin/pa/fsearch)

[Home](http://www.fluffy.co.uk/fs/index.html)

[Documentation](http://www.fluffy.co.uk/fs/docs.html)

[Overview](http://www.fluffy.co.uk/fs/docusing.html)

[Requirements](http://www.fluffy.co.uk/fs/docrequire.html)

[Configuring](http://www.fluffy.co.uk/fs/docconfig.html)

[Searching
etc](http://www.fluffy.co.uk/fs/docinas.html)

# Using Fluffy Search

Fluffy Search has been designed to be able to search most web sites with
little or no modification to the existing pages. In fact, unless you use
multiple framesets, you will be unlikely to need to do anything.

Simply install the scripts on your server and edit the configuration file to
point it to the right files. Create a 'template' page which gives the header and
footer for the search form and search results. Finally, run the indexer, and
link the search form to your existing pages. And you now have a search
engine!

Every time you modify the site, you need to re-index the site. This can be
done from a web browser, using a password you specify in the configuration
file.

## Controlling what is indexed

You can control what is indexed on your site. If you include a file called
.fcs\_exclude in a directory, then all the files within that, and the
directories below it, are excluded from the index, and won't be found in a
search. (The .fcs\_exclude should be a zero length file. Fluffy Search
only looks for it's existence to exclude the directory, not the content.)

Within the configuration file, you can also specify rules on what files will
be indexed, so for example, you could index .htm and .shtml files, but not .html
files if you so wished.

You can even specify exceptions to the above rules, to, for example, exclude
files with particular names. You might want to do this to exclude files called
'toc.html' if these are tables of contents used to display navigation in
framesets.

Finally, you can enclose text in <fcs\_ni></fcs\_ni> tag
pairs to exclude parts of a page from the index. This might be useful to exclude
constant navigational elements from pages.

Following the UNIX convention for hiding files, directories with names
beginning with '.' are ignored. To avoid indexing the extra data FrontPage
extensions add into the document directories, directories with names beginning
with '\_' are also ignored.

## Framesets

If your site uses multiple framesets, for example, one for each section,
Fluffy Search can display found pages in the correct frameset when you click on
a link on the search results.

It does this by finding the frameset for that section, and building a new
frameset 'on the fly' to enclose the found page.

You need to tell Fluffy Search which pages go in which frameset, and the
frame within that frameset which is supposed to contain the content. You can
either do this by a general rule (for example, the frameset is always called
'index.html' in the directory above the page) or by a list of directories and
the location of the frameset for each.

Alternatively, you can use a combination of the two methods. The general rule
specifies the majority of the framesets, and the list gives the exceptions to
the rule.

There is a slight restriction. All pages within a directory must use the same
frameset. Reorganising your site to meet this requirement should be the only
modification you need make to your site.

## Password protected directories

A word of warning: The page highlighter script does not do any password
protection. If you index a password protected directory on your server but do
not apply the same password protection to the cgi-bin directory Fluffy Search is
in, then you will be able to use the search to retrieve the protected files
without a password.

Make sure the script directory has the same password protection as the pages
you're searching!

If there are some password protected areas on your site, and you want to
search them as well as the non-protected areas, you can either turn off
highlighting, in which case all files will be retrieved from the web server as
normal, or create two search scripts, one which searches the non-protected pages
only and the second which searches everything, and is also password
protected.

< [Contents](http://www.fluffy.co.uk/fs/docs.html)
| [Requirements](http://www.fluffy.co.uk/fs/docrequire.html)
>

---

[![Ignite](Using Fluffy Search_files/ign.gif)](http://www.ignite-it.co.uk/)
Need blazingly fast downloads? Existing tools a bit clumsy?
**[Use Ignite](http://www.ignite-it.co.uk/)** to create
better, faster, web graphics in less time.  
Download your free 30 day
trial now!

---

(c) Fluffy Clouds Ltd 1999 | [home page](http://www.fluffy.co.uk/index.html)
