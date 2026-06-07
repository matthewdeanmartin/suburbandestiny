---
date: '2009-05-09'
recovered_from: wayback
slug: post-530
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200905\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=530
title: 'When to and when not to use #Region in C# and VB.NET'
---


Regions are not classes. Regions are not shelves in your closet. Regions are not folders on your obsessively compulsively clean desk. Regions are not to be alphabetized like the cans of food in your cupboards. Regions are not the rug for sweeping your buggy code under. 


Remember, regions by default are collapsed and invisible without special action.


Regions are a code smell. Regions are obfuscation. Regions are evil. Except in the following 3 cases.


DO. License headers. You got to have them on every file for certain licenses. If these collapse by default, that is okay.


DO. Stupid ass headers your boss makes you put in your code that add no value. \#Region will make them invisible most of the time.


DO. Commented out dead code you can’t delete because you don’t expect your colleagues to find it in the source control.


And to clarify:


DON’T. Groups of related methods. This is a code smell. If you have more than 100 lines of code and have the urge to use a region, you probably have discovered the need for a new class.


DON’T. Arbitrary categories of members, e.g. Properties, private methods, methods that return strings, methods starting with the letter “r”


DON’T. Code Generated regions. Use partial classes.