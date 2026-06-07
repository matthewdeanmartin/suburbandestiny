---
date: '2009-06-10'
recovered_from: wayback
slug: post-546
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200906\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=546
title: WCF + .NET 2.0
---


I’ve got an application that is stuck at .NET 2\.0 for a while. But I don’t do something to demonstrate WCF is useful, it will be stuck at 2\.0 for much longer.


**The Use Case: Unit Testing.**  

WCF opens your application up to more clients. If you think your application has only one client, your wrong, you application should have unit tests and the unit tests constitute a client, in addition to you web forms or windows forms application.


**WCF in one Assembly, Business Logic in the Other.**  

This works fine for the service class. The .svc file is a wrapper around some class that implements an interface with the relevant attributes. I haven’t figured out a way to do this without using a wrapper pattern. However, not so serious a problem because a service is probably going to be designed differently than the underlying business object– probably more stateless for one.


The complex data types used for the data transfer objects are more problematic. The WCF way is to put a \[DataContract] attribute on them. This means either putting a wrapper around your data types (i.e. your Customer object, the Order object, etc) or moving the WCF attributes into the business logic class’s assembly. Not possible if I want to leave the business logic tier at .NET 2\.0\. 


Fortunately, .NET 3\.5 SP1 supports POCO serialization, i.e. WCF will turn any plain old clr object into xml on the wire. That means you don’t need to put the DataContract attribute on your 2\.0 business objects, or wrap the business object in a 3\.5 wrapper.


**Choice of Host.**  

If your stuck with .NET 2\.0, you’re probably stuck with IIS 5/6 and Server 2000/2003\. That means no WAS. So hosting means web services wcf style over http. Unless you write your own host, probably using a windows service.