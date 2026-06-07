---
date: '2015-12-03'
recovered_from: wayback
slug: post-819
source_file: data\normalized\suburbandestiny.com\Tech\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=819
title: Mister SQL | The other half of MS SQL
---


**Features worth searching for:**  

Log\-by\-level. E.g. info, warn, verbose, error.  

Log\-by\-module/theme. E.g. MyClass, file1\.js, Data, UI, Validation, etc. Sometimes called “groups” or other things.  

Log\-errors. Info, warn, verbose are all the same data type, but the error is a complex data type and the work flow differs dramatically from the others.  

Log\-to\-different places, e.g. HTML, alert, console, Ajax/Server  

Log\-formatting. E.g. xml, json, CSV, etc.  

Log\-correlation. E.g. if you log to 2 places, say a client, server and web\-service and db, and a transactions passes through all four, can you correlate the log entries?  

Log\-analysis. E.g. if you generate \*a lot\* of log entries, something to search/summarize them would be nice.  

Semantic\-logging. E.g. logging (arbitrary) structured data as well as strings or a fixed set of fields.  

Analytics. Page hit counters. (I didn’t search for these)  

Feature Usage. Same, but for applications where feature !\= page  

Console. Sometimes as a place to spew log entries, sometimes as a place for interactive execution of code.


**Repository Queries:**  

[http://bower.io/search/?q\=logging](http://bower.io/search/?q=logging) 25 entries right now.  

[http://bower.io/search/?q\=log](http://bower.io/search/?q=log)  

[http://bower.io/search/?q\=console](http://bower.io/search/?q=console)


[https://www.nuget.org/packages?q\=javascript\+logging](https://www.nuget.org/packages?q=javascript+logging) Nuget JS logging libraries.


<https://nodejsmodules.org/tags/logging> – Nodejs Repository query


**Various Uncategorized Browser\-Centric Libraries**  

[https://github.com/enoex/Bragi\-Browser](https://github.com/enoex/Bragi-Browser) category logger (here they are called “groups”)  

[https://github.com/better\-js\-logging/console\-logger](https://github.com/better-js-logging/console-logger) category \& level logger.  

<https://github.com/latentflip/bows> colorful logging by category  

<https://oaxoa.github.io/Conzole/> Side console.  

[https://github.com/structured\-log/structured\-log](https://github.com/structured-log/structured-log) – Serilog/Structured Log  

<http://log4javascript.org/> Log4JavaScript – for people who like the log4x API. As of 2015, appears dated \& unmaintained.  

[http://www.softwarementors.com/log4js\-ext/](http://www.softwarementors.com/log4js-ext/) More upto date log4x library. Fancy on screen log.  

<https://github.com/stritti/log4js> A level\-logger. (Many features are IE only)  

<http://smalljs.org/logging/debug/> Console logger with module filters.  

<http://jsnlog.com/> Client side logger that sends events to popular server side logging libraries (more than just server side node)  

<http://www.songho.ca/misc/logger/logger.html> on screen (HTML) logging overlay  

[https://github.com/cerner/canadarm/](https://github.com/cerner/canadarm/ )   

[https://github.com/FacetsTechnologies/loghound](https://github.com/FacetsTechnologies/loghound )   

<http://jstracer.sourceforge.net/>  

<https://github.com/jbail/lumberjack> Monkeypatches the built\-in console object.


**Microlibraries for Browser**  

These might not be any smaller than other libraries.  

<https://github.com/bfattori/LogJS> – supports local storage logging.  

[https://github.com/kapilkaisare/sleeper\-agent](https://github.com/kapilkaisare/sleeper-agent) 4 level logging with an on/off switch at runtime.  

<https://github.com/mattkanwisher/driftwood.js> – 4 level logging with environment switches \& ajax  

<https://github.com/pimterry/loglevel>. 4 level logging Supports plugins.  

[https://github.com/cowboy/javascript\-debug/tree/v0\.4](https://github.com/cowboy/javascript-debug/tree/v0.4) console.log wrapper  

<http://js.jsnlog.com/> Same as JSN Log, but just the JS part, so it’s like a microlibrary.  

<https://github.com/gillesruppert/flog>  

[https://github.com/nhnb/console\-log](https://github.com/nhnb/console-log) – Polymer/web\-component style console logging  

<https://github.com/icodeforlove/Console.js> – Polyfill for pretty\-console display?  

<https://github.com/Couto/groundskeeper> – Build step to remove console.log entries before sending to production.


**Abandonware**  

[https://github.com/pockata/blackbird\-js](https://github.com/pockata/blackbird-js) \-Abandoned? Not sure what it does.  

NitobiBug \-Abandoned. If you look long enough you can find websites that serve up the file.


**Browser plug ins**  

<http://getfirebug.com/logging> – Firefox centric.


**Error Logging**  

Error logging is more than a print statement. Generally, at point of error you want to capture all the information that the runtime provides.  

<http://www.stacktracejs.com/> Stacktrace and more.  

[http://openmymind.net/2012/4/4/You\-Really\-Should\-Log\-Client\-Side\-Error/](http://openmymind.net/2012/4/4/You-Really-Should-Log-Client-Side-Error/) Roll your own


**Node Loggers (might work in Browser, not sure)**  

[https://github.com/enoex/Bragi\-Node](https://github.com/enoex/Bragi-Node) (Node Centric)  

<https://www.npmjs.com/package/winston> (Node Centric)  

<https://github.com/jstrace/jstrace> (Node centric)  

[https://nodejs.org/en/blog/module/service\-logging\-in\-json\-with\-bunyan/](https://nodejs.org/en/blog/module/service-logging-in-json-with-bunyan/) Bunyan


**Commercial Loggers**  

Often a opensource client that talks to a commercial server. No idea if these can work w/o the server component.


<https://www.loggly.com/docs/javascript/>  

[https://github.com/loggly/loggly\-jslogger](https://github.com/loggly/loggly-jslogger ) 


<https://logentries.com/>  

<https://github.com/logentries/le_js>


<https://trackjs.com/>  

<https://github.com/trackjs>


<http://jslogger.com/>