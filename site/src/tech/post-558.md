---
date: '2009-07-19'
recovered_from: wayback
slug: post-558
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200907\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=558
title: The Anonymous Web
---


This is the flips side of what I usually work with: figuring out who really is at the other end of an HTTP request. What if some one doesn’t want to be known at all? It turns out to be as hard as proving you are who you say you are!


**Tor**. Re\-route your traffic through a few nodes donated by nice people until your point of origin is hard to trace. Free. Down side, performance is about 100 times slower than without Tor. And I measure that. It’s slower than a modem on a noisy line. The system is currently overrun by bittorrent traffic and there are no incentives to be an exit node: no money and the exit node owners get blamed for the IP laws broken while traversing them.


**Commercial Proxies**. I tried out Anonymizer. Performance is good, but you can’t directly sign up for email accounts when your IP is proxied. The email providers assume you are a spammer if you are trying to create an account while proxied.


**Java Applets, your browser, etc.**. All of these fancy client features leak information about who you are. Java applets can even get an honest answer about your unproxied IP address even when your browser is only reporting the proxied IP address! I think, for a nosy website to use this info, they’d have to have a special crafted java applet, AFAIK, an ordinary applet doesn’t leak information.


You’d think that with all this leaked info, we could use it to ID someone routinely, but IP tracing is hard detective work. You’d have to be doing something remarkable to make it worth someone’s effort to track you down by the crumbs you leave when surfing.


**Social Engineering Still Rules**. I imagine that if a user covered all their tracks, as soon as they accidentally say something online that ties them to a particular person in real life, the game is over.