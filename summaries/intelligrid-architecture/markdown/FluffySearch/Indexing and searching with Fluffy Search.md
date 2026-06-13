# Indexing and searching with Fluffy Search

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/FluffySearch/Indexing and searching with Fluffy Search.htm

---

![Fluffy Search](Indexing and searching with Fluffy Search_files/fs.gif)
  
... [from the developers of
**Ignite**](http://www.ignite-it.co.uk/)
[![Ignite: Web graphics optimization with edge!](Indexing and searching with Fluffy Search.htm)](http://www.ignite-it.co.uk/cgi-bin/pa/fsearch)

[Home](http://www.fluffy.co.uk/fs/index.html)

[Documentation](http://www.fluffy.co.uk/fs/docs.html)

[Overview](http://www.fluffy.co.uk/fs/docusing.html)

[Requirements](http://www.fluffy.co.uk/fs/docrequire.html)

[Configuring](http://www.fluffy.co.uk/fs/docconfig.html)

[Searching
etc](http://www.fluffy.co.uk/fs/docinas.html)

# Indexing

When you install Fluffy Search, and every time you make a change to the web
site, you need to index the site.

To do this, go to the fluffyindex.pl script with you web browser. For
example,

http://www.example.com/cgi-bin/fluffyindex.pl

Enter the password you have specified in the config file, and click 'Index'.
The site will then be indexed. This may take some time. However, at no point in
the process is the index in such as state as a search will fail, so this is a
safe operation to do at a time when the search is being used.

You can run the index from a command line using a command like (on UNIX)

/home/user/scripts/fluffymkindex.pl index

That is, run the fluffymkindex.pl with index as its first
parameter. You can use this to, for example, update the index on a site which
changes regularly at midnight by running it as a cron job.

# Searching

To run a search, link to, for example

/cgi-bin/fluffysearch.pl

on your web page. This will display the form and allow the user to search
your site.

For efficiency, you could save the source of this first page, upload it to
your site and link to that instead. This will make it unnecessary to run the
script to show the initial search form.

# Creating a quick search form

If you want to create a 'quick search' form, which contains just a field to
enter words and a search button, on any other web page, just insert code like
this

```
<form method=GET action="/cgi-bin/fluffysearch.pl">
<input type=text name="words"> <input type=submit value="Search">
</form>
```

Forms should use the GET method.

< [Configuring](http://www.fluffy.co.uk/fs/docconfig.html) | [Contents](http://www.fluffy.co.uk/fs/docs.html) >

---

[![Ignite](Indexing and searching with Fluffy Search_files/ign.gif)](http://www.ignite-it.co.uk/)
Need blazingly fast downloads? Existing tools a bit clumsy?
**[Use Ignite](http://www.ignite-it.co.uk/)** to create
better, faster, web graphics in less time.  
Download your free 30 day
trial now!

---

(c) Fluffy Clouds Ltd 1999 | [home page](http://www.fluffy.co.uk/index.html)
