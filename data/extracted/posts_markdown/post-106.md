---
date: '2004-02-08'
recovered_from: wayback
slug: post-106
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200402\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=106
title: Stupid VB Control Tricks
---


1. **Visible connections** They clutter up the field
2. **Invisible text boxes**  

e.g. when you set the border to be invisible, they become invisible on the designer
3. **Zero width widgets**  

The designer should give everything a minimum width even if the widget will be zero width in runtime.
4. **Default trash text**  

Default names are ok. Default properties, like value \= “text1″ is a pain
5. **Absolute positioning**  

Who has time to bump around every single widget!
6. **Inconsistent property names**  

This control returns values with .value, that one with .text
7. **Non extendable controls**  

Give the using programmer’s a chance to fix the base controls defects. And give us at least 3 different ways to extend a control. (By adding new properties, overriding exiting behavior or properties, or making it easy to pass control through a subroutine each time before use for repair)
8. GUI only edits