---
date: '2012-11-02'
recovered_from: wayback
slug: post-691
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201211\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=691
title: So you want to run powershell scripts without admin rights
---


First logon as a limited, non admin user on windows 7\. Should be easy because large organizations are yanking admin rights and apps are running better without admin rights, so whining to the help desk isn’t as effective as it was.


Create an empty file, say test.ps1 


Try to run it using 


 .\\test.ps1


You can’t. **Execution of scripts has been disabled**. (You try modules and profile scripts, same issue) So you read up and try running


`set-executionpolicy remotesigned` 


And you get an error message about not being able to modify the registry because you are not admin on your machine you are a limited user. And then you think to your self…There’s a time when the operation of the machine becomes so odious, makes you so sick at heart, that you can’t take part! You can’t even passively take part! And you’ve got to put your bodies upon the gears and upon the wheels…upon the levers, upon all the apparatus, and you’ve got to make it stop! And you’ve got to indicate to the people who run it, to the people who own it, that unless you’re free, the machine will be prevented from working at all!


And with a rebel cry we jump to google. A non\-admin can still run a batch file as a limited user. So can we execute .ps1 equivallent as a .bat?


Yes! [Our friends from the CCCP know how.](http://dmitrysotnikov.wordpress.com/2008/06/27/powershell-script-in-a-bat-file/)


Wrap everything in your .ps1 file in a 


`$code={ #code goes here }`


Encode it


`[convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($code))`


Put it in a batch file like so, names test.bat


`powershell.exe -NoExit -EncodedCommand  

DQAKAAkAIwBpAHQAZQByAGEAdABlACAAbgB1  

AG0AYgBlAHIAcwAgADEAIAB0AGgAcgBvAHUAZwBoACAAMQ  

AwAA0ACgAJADEALgAuADEAMAAgAHwAIABmAG8AcgBlAGEA  

YwBoAC0AbwBiAGoAZQBjAHQAIAB7AA0ACgAJ  

ACMAIABqAHUAcwB0ACAAbwB1AHQAcAB1AHQAIAB0AGgAZQB  

tAA0ACgAJACIAQwB1AHIAcgBlAG4AdAAgAG  

8AdQB0AHAAdQB0ADoAIgANAAoACQAkAF8ADQAKAAkAfQANAAoA`


The code executes and is the moral equivallent of executing a .ps1 file. Except you have no clue what the source is by casual inspection. And it means all non\-admin users have to run their ps1 code through a build step.


Jeffrey Snover, tear down this wall! Thanks.