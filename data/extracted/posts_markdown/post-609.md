---
date: '2011-01-25'
recovered_from: wayback
slug: post-609
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201101\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=609
title: Picking .NET tools when you want to collaborate
---


Something as simple as solution folders can stop you from collaborating with anyone except Visual Studio Professional.


**Strategies for the IDE**  

Target the largest crowd.  For example, everyone with VS2005\. A good percent of those people only have a licensed copy at where  work and won’t have time to dink around with an open source project, unless it happens to be solving a commercial problem for them.


Target multiple crowds.  Eg. distribute with \#ifdef statements for 1\.1,2\.0,4\.0, Mono and six different solution files and project files targeting VS.NET, VS2003, VS2005, VS2008, VS2010, and monodevelop. The extreme version of this strategy is crazy.


Target the poor. Visual Studio Express, Nant \+ notepad, csc.exe \+ notepad, WebMatrix, CodeRun, MonoDevelop. Ok, but some of these have really low productivity characteristics.


Hybrid strategies. Make sure the largest crowd can contribute and maybe one subset of the poor or different, such as the previous release of VS or Visual Studio Express.  This will require periodically opening the solution in the less expensive environment to make sure that you aren’t using a feature the other IDE doesn’t have.


**Strategies for the rest**  

git hub or CodePlex or what? Use one site for bug tracker, source control and everything or pick your favorite bug tracker, source control, etc.


**VS2010 Express \+ SVN/Git \+ Team City**You can create DLLs, WebForms, MVC, Silverlight widgets and WCF services. So it’s kind of like being in a ‘all\-you\-have\-is\-a\-hammer’ situation, so these are your hammers.


VS without Ankh is a bit trickier, you’ll probably just use tortoise. You will need to know on your own to not check in /obj/  .cache, .suo, maybe not /bin/


Codeplex has an SVN bridge. Cool.


Since you can create DLLs, you can create unit tests separate from code\-under\-test.  At the moment, all I can find the nUnit GUI test runner. I’m not seeing a way to add commands to the menu in VSExpress, but you can add post\-build steps that will call the nUnit GUI test runner. On the otherhand, you wouldn’t want that to run in the build server, because the build server would have it’s own unit test runner.  So again, it’s just a non\-integrated experience.