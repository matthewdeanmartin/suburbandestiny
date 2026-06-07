---
date: '2007-06-25'
recovered_from: wayback
slug: post-240
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=240
title: SSL, I just don’t get it
---


So I’m buying an SSL certificate. To prevent getting a MSIE7 error, it needs only be unexpired, match the URL and come from a ‘trusted authority’.


A trusted authority, like rapidssl.com will give an SSL certificate to anyone who “controls their domain”


Why don’t we just call a spade a spade and tell people that an SSL certificate is a means of encryption on the wire amongst unauthenticated parties?


I got a magazine subscription from an online company that did everything possible to hide their identity (anonymous domain, no physical address)– and they used SSL. I did get my magazine subscription, so it appears that I was buying from a company that want to stay anonymous, maybe for tax reasons. The transaction size was small and the website was plausible, so I wasn’t exactly sending a check to Nigeria. All I really need for this transaction is \*correlation\* I can now correlate my experience with the first time I interacted with this anonymous company with the second time I interact with them and form a sense of their reputation. In fact, if a reputation server was what stood behind the URL \& SSL cert instead of a picture of a guy with a bag over his head, ecommerce would be a lot safer.


I really don’t see the value in the expensive SSL certs either. To get the additional trust from that cert, users have to:


1\. Understand that you $1000 cert underwent a rigorous audit, unlike the vast majority of certs.


2\. Know how to click through to see the subject on the cert


3\. etc.


Imho, SSL is not authentication at all. It’s more like meeting a stranger on the street and agreeing to speak in Esperanto so that the other strangers on the street can’t understand you.


The URL is not an identity either. OpenId is proposing that if you control an URL, you are that URL. But URL’s lapse all the time. Even excluding the rather rare, but technically possible hijacking of DNS servers and domain names, if my URL lapses, someone could pick it up and pretend that they were Matthew Martin. They wouldn’t be as stylish and suave, but an average web browser would be hard pressed to know the difference.