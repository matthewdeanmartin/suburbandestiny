---
date: '2016-04-29'
recovered_from: wayback
slug: post-831
source_file: data\normalized\suburbandestiny.com\Tech\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=831
title: What a Build Master should know or do as a Build Master.
---


An automated build is beautiful. It takes one click to run. The clicking on the run button is completely deskilled. It can be delegated to the cat.


Setting up and troubleshooting a build server on the other hand is unavoidably senior developer work, but I encourage everyone to start as soon as they can stomach the complexity.


Does it compile?


A good build pays close attention to the build options as a production release will have different options from your workstation build. If it builds on your machine, you may still have accidentally sabotages performance and security on the production server. Review all the compilation options.


In the case of C\#, the rest of the build script is a csproj file, which is msbuild code, which is executable xml. You don’t need to know about how it works until stuff breaks and then you need to know enough msbuild to fix it. Also, because the build server sometimes doesn’t or can’t have the IDE on it, the msbuild script might be the only way to modify how the build is done.


The TFS build profile is written in XAML, which again is executable XML. Sometimes it has to be edited, for example if you want to get TFS to support anything but ms\-test. Fear the day you need to.


Technologies to know: msbuild, IDEs (VS20XX), TFS GUI, maybe XAML, possibly JS and CSS compilers like TypeScript and SASS


Is it fetching source code correctly, can it compile immediately after check out to a clean folder?


When there are 50 manual steps to be done after checking code out before you can compile, the build master must fix all of these. Again, it builds on the workstation, but all that proves is that you have a possibly non\-repeatable build.


Maybe 90% of the headaches have to do with libraries, or nowadays, repo managers, like nuget, bower, npm, etc. A sloppy project makes no effort to put dependencies into source control and crappy tools means the build server or build script is unawares of the library managers.


Technologies to know: tfs, nuget, bower, npm, your IDE


What is “good” as far as a build goes?


A good build server is opinionated and doesn’t ship what ever successfully writes to a hard drive. Depending on the technology, there isn’t even such a thing as compilation. Those technologies have to be validated using lint, unit tests and so on. These post build steps can either be failing or non\-failing post\-build tasks. If they don’t fail the build, then often they are just ignored. Failing unit tests should fail a build. Other failing tasks, probably should fail a build, even if they aren’t production artifacts. I usually wish I could fail a build on lint problems, but depending on the linter and the specific problems, sometimes there just isn’t enough time to address (literally) 1,000,000 lint warnings.


Technologies to know: mstest, nunit, xunit, and other unit test frameworks for each technology in your stack.


Who fixes the failing tests? Who fixes the bugs?


The build master, depending on the organization and how dysfunctional it is, is either completely or partially responsible for fixing the build. There is no way to write a manual for how to do this. Essentially, as a build master, you have to dig into someone else’s code and demonstrate they broke the build and are obliged to fix it, or quietly fix it, or what ever the team culture allows you to do.


Technologies to know: nunit test, debugging, trace


We got a good build, now what? Process.


Not so fast! Depending on the larger organization policies with respect to command and control, you may need to get a long list of sign offs from people before you can deploy to the next environment. Sometimes you can have the build serve deploy directly to the relevant environment, sometimes it spits out a zipped package to be consumed by some sort of deployment script. Usually though, the build server can’t deploy directly to production due to air gaps or cultural barriers.


Technologies to know: Jira or what ever issue tracker is being used.  

Non\-technologies to know: your organizations official and informal laws, rules and customs regarding deployment.


The Grand Council of Release Poobahs and your boss said okay, now what?  

This step is often the most resistant to automation. It often has unknowable steps, like filling in the production password, production file paths and IP addresses.


MsBuild supports no less than two xml transformation syntaxes for changing xml config for each environment.


It may be advisable for environments you know about to do enviornment discovery. It’s either wonderful or an easy way to shoot yourself in the foot. When you know the target server is a Windows2008 Server and on such servers it must do X and on Win 7 workstations it must do Y, don’t forget to think about the Windows 10 machine that didn’t exist when you wrote your environment discovery code. Maybe it should blow up on an unknown machine, maybe it should


Technologies to know: batch, powershell, msdeploy, MS Word  

Non\-technologies to know: your organizations official and informal laws, rules and customs regarding deployment.


Optional Stuff


Build servers like TFS also have built into them bug trackers, requirements databases, SSRS, SSAS (Analysis Services), and build farm things. They are all optional and each one is a huge skill. SSAS alone requires the implanting of a supplemental brain so you can read and write MDX queries.


Also, optional, is learning how other build servers work. No single build server has won all organizations, so you will eventually come across TeamCity, Lunt Build, etc.