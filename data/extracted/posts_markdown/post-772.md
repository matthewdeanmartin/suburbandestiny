---
date: '2014-10-23'
recovered_from: wayback
slug: post-772
source_file: data\normalized\tech.wakayos.com\root\__query__\p\772\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=772
title: REST Levels above 4
---


There is the [Richardson Model](http://martinfowler.com/articles/richardsonMaturityModel.html) of REST says REST APIs can be ranked like so:


1\- Plain old XML. You serve up data in a data exchange format at HTTP endpoint. Ignores as much as possible about how HTTP was intended to work.  

2\- Resources have their own URL  

3\- Resources can be manipulated with GET, PUT, POST, DELETE  

4\- Resources return hypermedia, which contains links to other valid actions \& acts as the state of the application.


I’ll add these:  

5\- Metadata. The API supports HEAD, OPTIONS, and some sort of meta data document like HAL  

6\- Server Side Asynch – There is support for HTTP 202 \& an endpoint for checking the status of queued requests. This is not to be confused with client side asych. Server side asynch allows the server to close an HTTP connection and keep working on the request. Client side asych has to do with not blocking the browser’s UI while waiting for a response from the server.  

7\- Streaming – There is support for the ranges header for returning a resource in chunks of bytes. It is more like resumeable download, and not related to the chunk size when you write bytes to the Response. With ranges, the HTTP request comes to a complete end after each chunk is sent.


\#5 is universally useful, but there isn’t AFAIK, a real standard.  

\#6 \& \#7 are really only needed when a request is long running or the message size is so large it needs to support resuming.


Clients should have a similar support Level system.  

1 – Can use all verbs (Chrome can’t, not without JavaScript!)  

2 – Client Side Caches  

3 – Supports chunking \& maybe automatically chunks after checking the HEAD  

4 – Supports streaming with byte ranges