---
date: '2011-01-27'
recovered_from: wayback
slug: post-613
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201101\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=613
title: Validation Application Block Post Mortem
---


VAB seemed to work only for simple domain restrictions on a single property.  This is the least interesting, least value providing sort of validation.  At worst It is a 2 line if/then block of code! Replacing it with an attribute saves 1 line of code and creates some design rigidities.


If you had complex logic (and it didn’t have to be very complicated), one was tempted to write complex expressions in attributes. This is ugly programming.


If you had complex logic, you were supposed to write custom validators.  Contrary to this [blog post](http://blogs.microsoft.co.il/blogs/bursteg/archive/2007/07/26/CustomValidatorApplicationBlockSoftwareFactory.aspx), which says, “This is very easy to do”, this is not easier than writing a Validate() method– at the very least, it’s 100s of lines of extra code.


The custom validators tend to be a lot like  

List\<string\> Validate(MyObject someObject),  

which is the way things were before attribute driven programming.


The codebase began to evolve to use VAB less and less.


Today I’m removing the assembly.