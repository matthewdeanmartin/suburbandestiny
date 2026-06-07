---
date: '2007-08-12'
recovered_from: wayback
slug: post-267
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200708\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=267
title: 'Notes: Hosting Multiple ASP.NET Applications in one place'
---


I have a hosted account on a shared machine.  This means I have sub\-optimal access to IIS (a web\-app control panel that drives buggy and poorly documented asp scripts).


I have two applications I want to host in one place (I’m use the word place on purpose), because I don’t want to double my hosting fees just because I have a tiny application that isn’t thematically connected to my favorite application.  My favorite application is a movie club web site, the other site is a launch page for a [custom google search](http://google.com/coop/cse?cx=010530258174171504331%3Atrmsq7cfp8g).


I bought two domains and began working on pointing them at my site.  The finally found a separate control panel that let me pick the IP address for my site.  Since I have a static IP, I pointed my new domains at my static IP.  Now I get, “**ns5\.dnsserver8\.com** returned (SERVFAIL)”, which may just mean I need to wait two more days.  This could be a very slow bug to trouble shoot. In the meanwhile….


If I want the domains to resolve to different folders on my server, I have to double my hosting fees.  That isn’t good.  So I moved my applications into two folders and put a Default.aspx file at the root that inspects the requested domain name and forwards the browser to the correct subfolder.


This leads to web.config errors, because the redirection application and my two sub folders also have web.config files.


**Single application.**  I could put the everything into one visual studio project, with one web.config. I don’t like this solution because the ASP.NET 2\.0 application has only one Profile/Membership, etc. object and database per application.  


**Multiple applications.**  One in the root, two in subfolders.  The root application has a minimal web.config to minimize cascading.  


If an app in a subfolder is precompiled, it just serves the “This is a marker…” message and no compiled pages.  I even tried putting the PrecompiledApp.txt file in the folder and the parent folder, no joy.  I even tried moving the compiled files to the parent bin folder, still no joy.  I so I compiled the parent app, and got the error “The file default.aspx has not been compiled…” This normally means a reference is missing.  So I tried putting the compiled dll’s in the parent folder’s bin, still no joy.  A pre\-compiled application, it seems, must be entirely in it’s own IIS application.


**Creating IIS “Applications”.** I’m using WebHost4Life, so I use their “Total Control” control panel with command path of : “Site Admin: IIS Manager: Set .NET App: \[Go] (my domain) : (click on gear for child folder which hold asp.net apps)”


Finally, joy.  The parent project works, the child projects work and it doesn’t look like there is any significant web.config cascade problems.


Now solving the domain name problem, that will take longer….


\[Update!]


**Domain name problem solved.**  When you buy a domain name, two machines need configuration, the domain name servers of the company that sold the domain and the domain name servers of your web host company.  I initially tried to tell my domain name seller to use my static IP–no joy.  It wasn’t until the script that updates my web hosting companies two domain servers finally succeeded without error that the domain names started to work.  Afterwards, I had to set up an ASP.NET application for each folder for each domain name and voila! They all work.  I have no idea what the isolation is between one ASP.NET application and the next, but that is Okay.