---
date: '2014-04-01'
recovered_from: wayback
slug: post-701
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201404\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=701
title: Javascript Intellisense, Pretending to Compile JS
---


So Visual Studio 2010 is reporting everything has the same methods, the methods of the JavaScript Object.


**Getting Intellisense to work**  

1\) Maybe the Telerik ScriptManager stomped it. The ScriptManager has to be an Asp:ScriptManager and nothing else. (As of VS2010\)  

2\) Maybe VS wants a Ctrl\-Shift\-J (manually force a JS intellisense update)  

3\) Maybe there is a “compile” error.  

– Check the Error List tab and look at the yellow warnings.  

– Check the General output window, especially after doing a Ctrl\-Shift\-J  

– Try to reformat the code. If it doesn’t reformat, Visual Studio probably can’t “compile” and doesn’t know what to do  

– Look for green squiggles  

4\) Maybe the JS wants to be in its own file. I’ve seen broken intellisense start working after the code was moved from an aspx to a .js file  

5\) Maybe the the annotations (the fake reference at the top of a JS page) are in the wrong order. For example, if you are working with Telerik, the Ajax reference should be first, Telerik stuff next, your own code later and it should be in order of dependency.  

6\) Maybe you haven’t added enough annotations (especially the fake “references”, but also summary, param, returns annotations)  

7\) Maybe you used a golden nugget i.e. \<%\= Foo() %\> and put it in a JS block (on an ascx or aspx page of course.) The VS Javascript parser see this as JS and tries to treat it as malformed JS. When you can cheaply quote it, quote it.  

\- e.g. var foo \=”\<%\= Foo() %\>“; // Just a string.  

\- e.g. var bar \=parseInt(“\<%\= Bar() %\>“,10\); //Convert to int  

\- e.g. var bar \=”\<%\= TrueOrFalse().ToLower() %\>“\=\=\=”true”; //Convert to bool  

\- but maybe/maybe not e.g. eval(“\<%\= GenerateJS() %\>“); //This isn’t a nice solution because you are doing an unnecessary, expensive, logic changing eval just to keep intellisense from breaking.  

8\) Watch this space, I still haven’t gotten page method intellisense to show up reliably.  

9\) ScriptMode appears to affect intellisense. ScriptMode\=”DEBUG” has better intellisense, but literally 1000x worse performance for browser execution, especially on IE.


**And an mistake to avoid especially for ASP.NET developers**  

\<%\= Foo() %\> syntax does not work in a .js file. .js files are static and not processed by the ASP.NET templating engine.  

JS values written to the screen are initial values. Once they are written, they might as well be static. The JS is code generated on the server, but executed on the client.  

var now \= ‘\<%\= DateTime.Now.ToString() %\>‘ ; // This isn’t going to change.  

If you call page methods, they return immediately, the call back happens a few seconds later.  

If you page methods blow up, Global Asax will not get an error event, so you have to use try/catch in your Page Method.  

If a page method blows up, it may start erroneously reporting “Authentication Failed” errors. I think this is some version of a WCF style logic, where a client can go into a “faulted” state and just refuse to behave there\-after. Still a theory.  

On a single page application (SPA), var \=\=\= Session. In a multi\-page ASP.NET application, you constantly store state in Session because values don’t live past the life of a page. In a single page application, your user doesn’t change pages. So a page variable is Session. It never times out.  

All parameters of your page methods are user input. In server side programming, you might grab a value from the database, store it in Session and use it later to save a record. In the SPA scenario, that value is handed over to the user and they can change it before it is submitted back to the page method. The level of difficulty is not especially high. So as values pass from server to JS page and back, they will have to be re\-validated. Even if you try to keep the values on the server alone, eventually the user will be given a choice of values, and on the page method, you’d want to validate that these values were on the list.