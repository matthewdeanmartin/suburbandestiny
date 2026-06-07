---
date: '2010-04-09'
recovered_from: wayback
slug: post-730
source_file: data\normalized\suburbandestiny.com\root\__query__\p\730\index.html
source_site: suburbandestiny-tech
source_url: http://www.suburbandestiny.com/?p=730
title: Creating Skype Chatrooms
---


To run a moderated chatroom on skype, you need to know these commands. The pre 4\.0 interface provided a GUI for these commands. the post 4\.0 interface seems to have fewer working commands and no GUI.  It does support group conference phone calls and both kick (temporary removal) and kickban (permanent remove) and well as a lurker mode for the world in general.


–Initial setup  

/set options \+JOINING\_ENABLED  

/set options \+JOINERS\_BECOME\_APPLICANTS  

/set options \+TOPIC\_AND\_PIC\_LOCKED\_FOR\_USERS  

/get uri


Public URI needs to be updated should a chatroom lapse.


– Can people join?  

/get options  

/set guidelines Joiners must be approved before chatting.


– Add a user  

/add foobar  

/setrole foobar USER  

/whois foobar


– Deal with bad behavior  

/kick badguy  

/kickban realbadguy


– What’s going on  

/info  

/get guidelines  

/get options