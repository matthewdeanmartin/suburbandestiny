---
date: '2011-01-31'
recovered_from: wayback
slug: post-612
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201101\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=612
title: The standard advice on new opensource projects
---


**The Linux Advice**  

Work on a project alone until the project becomes so big, successful and large that other developers beat a path to your door.


This isn’t really very useful advice. It kind of implies some extreme assumptions– no one will help on a small project, and only really big, successful one man projects can attract community contributions.


**Code yard sales**I heard the phrase first on Hanselman. Here’s some junk code, have fun. Because the original commiter is so … uncommitted, the project isn’t likely to go far.


This model has it’s places, but it doesn’t help if you want a medium sized open source project to grow and have some modest success.


Face it, odds are low your project will become as successful as Linux and it’s unnecessarily lazy to give away your starting code base and abandon it.


**WordPress\-style Plug in Model**  

If the application is designed from the get\-go for extensibility in a variety of ways, from basic stuff like using abstract classes and interfaces, to using a full blown plug\-in architecture, then people can  contribute in an unco\-ordinated fashion, perhaps without even committing to the main trunk.


The core of the application is a component host. The lead developer first job is to provide the glue for the parts. The particular functions would be secondary. I think this is counterintuitive, but essential. If I have an idea for a great blog engine, if I write a blog engine first, I will have to retrofit it for plugins. If I write an application host first, albeit one optimized for plugins, then it will be a very different application.