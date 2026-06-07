---
date: '2011-09-06'
recovered_from: wayback
slug: post-626
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201109\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=626
title: Custom Exception Antipatterns
---



> try{ } catch(SomeException)  
> 
> { throw MyCustomException(“Error in middle tier, method foobar()”);}


The above is wrong for multiple reasons. The text only tell you some stack trace information. Unless you know for sure that your error logging infrastructure or error reporting discards the stack trace and you can’t fix it, then don’t put stack trace information in your error. The default yellow screen and Elmah both capture stack trace.


The next reason the above is wrong, it overwrote the error. The error used to be something specific, e.g. SecurityException because you had the wrong NTFS permissions, for FormatingException, because you had two decimal points. But now the error is overwritten with “something bad happened”



> try{ } catch(SomeException e)  
> 
> { throw MyCustomException(“You need to run batch file foo.bat”,e);}


The above pattern wraps the exception. But error loggers don’t always display the internal errors, especially if there are multiple internal errors. Don’t wrap errors unless they are providing something remarkably valuable or unless you are \*actually\* writing code to specifically trap this sort of error on the next tier. (planning or thinking you might in five years doesn’t count)


**In ASP.NET don’t catch unless you feel pain from not catching.** 


In winforms, you have to catch, else the application exits. But in ASP.NET, only the page request ends. From the user’s standpoint, the application is still running because the next request can still succeed.