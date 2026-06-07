---
date: '2007-07-19'
recovered_from: wayback
slug: post-259
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200707\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=259
title: Running a Ps1 File and PowerShell Signing
---


**Invoking a Powershell Script**


By default, powershell does not run any unsigned ps1 files. Also, to invoke a script, you need to prefix it with .\\


 .\\myScript.ps1  




The following will get a bemusing error message:


 myScript.ps1  




If you don’t sign it, you will get an error message about not trusting the code.


**Should we sign it?**


If you distribute the code, you might want to sign it. If you are paranoid about accidentally running malicious code, you might want to sign your code, maybe if you work at a bank or some other attractive target for hackers. [Signing PowerShell Scripts is a very challenging chore](http://www.hanselman.com/blog/SigningPowerShellScripts.aspx).


* If the script moves to another machine, you will need to bring the certification authority with it.
* If the script’s signature expires, you will need to resign the script (and this will probably be a different user, with different access to tools and documentation)
* If you don’t do self signatures, you will have to harass the system administrator who has access to the companies SSL cert, or worse spend money on a SSL cert.


Here is how to turn off signing and return to the security policies that govern .BAT files.


Set\-ExecutionPolicy Unrestricted


Set\-ExecutionPolicy RemoteSigned


Remote signed is not a hassle like the other two because it only applies to scripts that were sent to you, say by the Mafia.