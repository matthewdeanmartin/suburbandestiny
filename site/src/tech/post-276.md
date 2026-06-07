---
date: '2007-09-07'
recovered_from: wayback
slug: post-276
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200709\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=276
title: 'Visual Studio 2005: Installation Woes'
---


So I have a clean Windows XP VMWare virtual machine.



I try to install from Remote Desktop. VS2005 actively refuses.



**VS2005 from the c: drive.** I copy all the files from the CD’s to the virtual machine’s hard drive. Visual Studio fails to ask for the location of the next disk, and instead reports that it wants the files for disk 2 and 3 to be merged in with the files from disk 1\. That is, it wants me to re\-arrange the files of the three disks until they are as if they were on one disk. Somehow I manage to shuffle files around, the install finally hangs at 0 CPU for a very long time on the SQL Express install. I didn’t really want SQL Express, I use SQL2000 Developer Edition, so I kill the install. It looks like most of the bits made it on the disk.



**MSDN**. Same problem. The MSDN installer can’t deal with being installed from c:\\ and doesn’t prompt for the location of disk 2, 3, etc. The MDSN installer eventually blows up. I think screw it, google works better anyhow. Because of the broken search on MSDN since VS2005, I’ve been trained to go to google first whenever I have a question.



**Visual Studio 2005 Service Pack 1\.** VS2005 SP1 is a massive re\-install. I use the VMWare remote client to pass through. The install hung after a night.



**Advice**. Create and mount ISO files when installing VS2005 to a virtual machine. The VS2008 Beta 2 install went through effortlessly. Consider switching to VS2008 beta before the official Feb 2008 release date.