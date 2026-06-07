---
date: '2007-06-22'
recovered_from: wayback
slug: post-236
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=236
title: Custom Rule Code vs AzMan BizRules
---


**Application Rules** 



```
If MyApplicationLogic.CheckNonRoleInfo() then
            AzMan.CheckAcces(...)
end if
```

This above CheckNonRoleInfo() method has limited access to the AzMan algorithm, which searches the entire role data structure for evidence that so \& so is allowed to do something. It would also be plausible that something depends on role and non\-role information, so it’s possible CheckNonRoleInfo() might evolve into CheckNonRoleInfo(CurrentUser, UsersRoles(), TimeOfDate, OtherRelevantFactor). Now this method is probably implementing some of the same logic as AzMan.


**AzMan Rules**



```
AzMan.CheckAccess(..., MiniDBOfNonRoleInfo())
```

The hooks are in the CheckAccess engine, so it combines both Role \& NonRoleInfo in a check.


The BizRule pattern means the rule is *part of* the AzMan Algorithm, which searches the entire role data structure for evidence that so \& so is allowed to do something. I’m imagining that the AzMan role engine hold the roles as some sort of network or graph, which it traverses. Everytime it gets to a node with a Rule attached, it evaluates that rule in addition to normal role checking logic.