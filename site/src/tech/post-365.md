---
date: '2008-05-30'
recovered_from: wayback
slug: post-365
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200805\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=365
title: Failure to upgrade Reporting Services 2005 to SP2
---


Don’t even bother to troubleshoot if this is a new installation. My defective install was SQL2005 Standard RTM where I applied SP2 after a few reboots (so I think Windows Update may have been modifying things). 


Install a new instance (you only need a new SQL instance and a new RS instance)  

Immediately run SP2, but only on the new SQL and RS instance.  

Run the “Reporting Service Configuration” Tool.  

Read this [KB article](http://support.microsoft.com/kb/934164). to deal with configuring IIS7\.


My new install was SQL 2005 Developers Edition. All of this was on Windows Server 2008 running as a workstation (i.e. not a member of a domain)


Afterwards, permanently turn off the old RS instance. You may not be able to uninstall it.


Reporting Services, of all the SQL components has given me the most trouble in all editions for all time since I ever started using it. The highly technical explanation for the problem is that Installation/Uninstallation/Update code for SSRS is crap.


Just in case anyone was curious here was my error message:


MSI (s) (3C:34\) \[12:55:51:479]: Product: Microsoft SQL Server 2005 Reporting Services – Update ‘Service Pack 2 for SQL Server Reporting Services 2005 ENU (KB921896\)’ installed successfully.


MSI (s) (3C:34\) \[12:55:51:480]: Windows Installer installed an update. Product Name: Microsoft SQL Server 2005 Reporting Services. Product Version: 9\.2\.3042\.00\. Product Language: 1033\. Update Name: Service Pack 2 for SQL Server Reporting Services 2005 ENU (KB921896\). Installation success or error status: 0\.


MSI (s) (3C:34\) \[12:55:51:481]: Note: 1: 1728  

MSI (s) (3C:34\) \[12:55:51:482]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:482]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:498]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:502]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:502]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:503]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:503]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:503]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:503]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:504]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:504]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:520]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:524]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:524]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:525]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:525]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:525]: Transforming table Error.


MSI (s) (3C:34\) \[12:55:51:525]: Note: 1: 2262 2: Error 3: \-2147287038  

MSI (s) (3C:34\) \[12:55:51:525]: Product: Microsoft SQL Server 2005 Reporting Services — Configuration completed successfully.