---
date: '2007-02-07'
recovered_from: wayback
slug: post-196
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200702\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=196
title: Integrated Security and Kiddie DOS Attacks
---


This morning my PC says my account is locked out.  Apparently, when I connect to my office by VPN, something on my computer was repeatedly trying to log into my computer using my name, Matthew Martin.  The password and domain were wrong, so Windows XP helpfully locked out my account, which I admit was the behavior I told to have.  I set a limit of something like 1000 failed logins before lockout.  On the “Welcome Screen”, there is no obvious way to log in as administrator.  Guess what feature I plan to start turning off on all the XP machines I come across?  That’s right.  Someday I’m going to need to tell someone in my family how to log on as administrator and they are going to be at a “Welcome Screen” without administrator on the list.  I managed to log on by using remote desktop.  I unlocked my account and found out that MYWORKDOMAIN\\Matthew Martin had been attempting to log on about every minute or so all night.


The failed logon continue.  Where could it be coming from?  If VPN is turned off, the logons stop.  Currently, I think the culprit is SQL Server Management Studio, which will send at ‘Are you alive’ connection attempt to every server on your list. It could also have been remote desktop or filesharing, I can’t really prove anything.


If the remote server is a WORKGROUP and not a domain machine and the user names are the same, then a polling app can easily lock out an account just by repeatedly attempting to log into a remote machine.  As long as the logon type \=3, there doesn’t appear to be any limits on the remote machine.