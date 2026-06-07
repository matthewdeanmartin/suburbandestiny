---
date: '2007-09-20'
recovered_from: wayback
slug: post-282
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200709\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=282
title: 'Installing Oracle Drivers: A Heuristic Approach'
---


**Oracle**, n. Database named after people who spent all their time sucking fumes and spouting nonsense.



**Installation Phase.** Download Oracle Express, Oracle ODBC, Oracle JDBC, and anything else that might have a functioning installer. You must be initiated into the brotherhood of those who receive spam from the Oracle. It’s kind of like hearing the voices of the gods in your head, but it’s comes by email.



**Sacrifice.** Sacrifice a lackey to the Oracle. The Oracle is an angry god and must be appeased. The version number indicates how many the Oracle demands.



**File Search Phase.** Find the listener.ora, tnsnames.ora, sqlnet.ora. There may be many, you will never know which one an active driver may be using.



**Ritual.** Reboot the server, your workstation, stop and start all services, kill all tasks and restart them as well. Sacrifice an intern as well. The Oracle demands blood.



**Network Test Phase.** Tnsping proves that an application can move electricity from here to there and get electricity back. Given the dim hope of actually getting data back, researchers are working on ways to harness the returning electricity to power office lights and pencil sharpeners.



**Test Phase**. Sqlplus may or may not end up on your machine. Sqlplus is the preferred way to deal with the Oracle as the tippity tappity of keys strokes on a command line are pleasing to the ears of the Oracle. If sqlplus is not on your machine after installing drivers, return the Oracle and keep downloading random crap until sqlplus appears on your machine.



**Trace Phase.** When trouble shooting a linked oracle server on SQL2000, to get better error messages, you need to run “DBCC Traceon(7300\)”



**Alternate technologies.** It is possible that the oracle driver works, or has better error messages when you use other technologies. Write a series of applications using ODBC, JDBC, OLE\-DB that define a connection string, attempt to connect, and either display the error message or a success message. If possible, use the “tnsnames.ora”\-free connection string. If you get a “tnsnames.ora”\-free connection string to work, you can use that to update the tnsnames.ora file. This is was the technique I used to finally get a successful connection.



**Shock.** I can’t believe Oracle drivers are this crappy.



**Denial.** I must be doing something wrong. This isn’t happening to me.



**Bargaining.** I give you a chocolate bar if you can fix this tnsnames file for me?



**Guilt.** I’m a talentless hack. I’ll never connect to the Oracle. This is the end of my career.



**Anger.** Damn it, I’m going to go over to Larry Ellisons house and make him configure this damn driver!



**Depression.** Screw it. I the project is going to fail as soon as the dev team finds out the drivers are impossible to install. Sigh.



**Acceptance.** Oracle sucks. Data in oracle is inaccessible.



**Hope.** And least there are a lot of other relational databases in the world that do have drivers that just work. Even companies as big as Oracle sometimes go out of business, never to be heard from again. Ah, it feels good to dream.