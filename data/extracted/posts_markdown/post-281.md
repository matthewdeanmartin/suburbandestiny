---
date: '2007-09-14'
recovered_from: wayback
slug: post-281
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200709\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=281
title: API’s I don’t Like
---


WMI. Relies on barely discoverable magic words (Namespace paths). Uses SQL as metaphor, but doesn’t actually have a proper database or relational structure behind it.



ADSI. Incomprehensible. Can’t easily play around with it as local authentication stores don’t act like active directory. And mere developers don’t usually have rights to Active Directory. Hence, no path to gaining competence.



Win32\. Not friendly to languages other than C\+\+. Incomprehensible.



Crypto API. Incomprehensible.



Javascript. Generally undiscoverable, but getting better with some IDE’s.



**API’s that are better**


COM, when early bound. Examples, ADO classic. Somewhat discoverable. When late bound relies on barely discoverable magic words (construction strings, method calls). Not friendly to languages that weren’t built specifically to be COM friendly.



WSDL Web Services. Not friendly unless you are using tools that ‘do it all for you’



**API’s I like**


REST. Plays very well with all programming languages that can make a GET request and receive an HTTP response.



.NET Framework. Highly discoverable, documentation strategy is build into the framework.



**Patterns**


* Discoverable metadata. APIs that could support intellisense if the IDE supported it are good. APIs that make it too hard for IDE’s to support intellisense are bad.
* Independent. APIs that have a fierce registration burden—I don’t like.
* Built in documentation. APIs should have javadoc type documentation features
* Aspect Orient Programming Features. API’s that automatically support Trace/Debug/Logging are good.