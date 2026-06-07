---
date: '2008-02-22'
recovered_from: wayback
slug: post-325
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200802\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=325
title: Working with a Hostile Intranet Environment
---


Scenario  

Your favorite computers are all on a corporate network, which is surrounded by a firewall restricting inbound traffic, but not outbound traffic. However, in an effort to reduce productivity, Mordac, preventer of IT services, has installed additional firewalls that separate groups of machines on the inside of the outermost firewall.


Diagnostics aka Port Scanning  

You presumably control both machines that you want to talk to each other.  If you don’t then this is hacking.  If you do control both of them, then this is diagnostics. Portqry from Microsoft is one utility you will likely be able to use.


e.g.  

portqry \-n intranetserver \-e 433


Options  

Reconfigure the firewall.  Inside a firewall, additional firewalls on the intranet is security overkill.  It means you have untrusted machines on the network.  Moving those outside of the intranet and re\-opening the ports internally is the best option. However, not all network admins give a rats ass about your project or know how to configure the firewall they installed.  


Reconfigure to use what is open. Some ports can be expected to be open even on all machines, for example LDAP and Kerberos ports, without which machines can’t authenticate.  You can also expect VNC or RDP ports to be open, else Mordac would have to get off his fat ass and visit machines in person to work help desk tickets.  These ports still might not be open for the pair of computers you are interested in or the direction you are interested in.


VPN and other tunnels.   Hamachi and putty/ssh are examples.  Hamachi is easy to use, but requires a 3rd party on the internet to enable you traffic.  Putty doesn’t require a 3rd party, but is challenging to configure and use.


Remote desktop/VNC.  If that fails, depending on the scenario, you might just want to see if RDP or VNC are available.  If you can’t copy the file from there to here, maybe it is enough to read it through RDP.


Proxy.  Proxies are an edge case.  If you have three machines on a network, A, B, C, where A can’t talk to C, but A\-B and B\-C work, then you can set up a proxy for the traffic from A to C.