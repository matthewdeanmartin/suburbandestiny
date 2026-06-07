---
date: '2007-10-31'
recovered_from: wayback
slug: post-298
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200710\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=298
title: 'SSIS: Dog Pile!'
---


Can’t stand people trying to stand in the way of a good dog pile.


Ayende made a bunch of good points about SSIS, Reed Me made an effort to rebutt.


[http://blogs.msdn.com/reedme/archive/2007/07/29/re…](http://blogs.msdn.com/reedme/archive/2007/07/29/re...)


Reed’s overall point was that with more product knowlege and effort, SSIS suddenly becomes a pleasant product to use.  If anything, this is a mark against SSIS compared to DTS because DTS was fairly easy to jump in and start using without a landmine map, I mean, best practices guide to keep users out of the broken corners. (I’m not defending classic DTS too much here, DTS also made it easy to jump in quick and shoot yourself in the foot)


Random Errors:  Reed said SSIS doesn’t yeild random errors and criticized Ayende for not posting them.  Here is one.


[![](https://suburbandestiny.com/tech/wp-content/uploads/2007/10/windowslivewriterssisdogpile-edcdimage0-thumb81.png)](https://suburbandestiny.com/tech/wp-content/uploads/2007/10/windowslivewriterssisdogpile-edcdimage0101.png)


Why long time user don’t see random errors. I’ve run into random errors in lots of applications, they go away after awhile regardless to patching. Reed appears to be a power user and power users have already been trained by the development environment to “stop doing that” because it leads to crashes.  How quickly we forget the initial pain, especially if we’ve been using it since Beta and have a plausible excuse for early instability.


Reed mentions several times that many problems are solved by following the Project Real.  Shouldn’t need a landmine map other than the product manual.  Actually shouldn’t need a product manual, ideally.


**UI Formating \+ Code.**  ASP.NET solved this problem using the codebehind model.  Just because many other MS products haven’t solved this problem doesn’t mean it can’t or shouldn’t be solved.


**Busy work.** Reed suggest that he code generates SSIS packages.  If SSIS was intended to be code generated, then why did it ship with BIDS instead of code generation tools and template editors?  No. SSIS was meant to be used in BIDS.  We consider code generation options in part out of frustration with BIDS.


Also, in response to the comment, “If you think you can make it better, please deposit your resume in [Careers @ Microsoft](http://www.microsoft.com/careers/).”  Well, there is also Jaspersoft ETL, plain old VB.NET, plain old stored procedures, many DTS look\-a\-likes.  In fact here is a huge discussion about [ETL products](http://datawarehouse.ittoolbox.com/groups/vendor-selection/dw-select/etl-tools-comparison-analysis-1180964?cv=expanded).