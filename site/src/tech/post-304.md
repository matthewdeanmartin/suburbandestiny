---
date: '2007-11-12'
recovered_from: wayback
slug: post-304
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200711\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=304
title: 'Webcast Notes: Top 5 Challenges Faced by Software Development Teams'
---


[http://www.microsoft.com/events/EventDetails.aspx?…](http://www.microsoft.com/events/EventDetails.aspx?...)


Recommended listening speed: 1\.25


Top five software challenges:


\-Invisible Progress  

\-Inefficient (manual tasks, expensive communication)  

\-Too many \*unintegrated\* projects (stovepipes?)  

\-No process (I’d add, wrong process, too much process, fake process, dysfunctional process)  

\-Not enough $$


What is invisible progress?


LOC failed to measure software. Metrics tricky to collect. Customers, managers become unhappy and unrealistic. Related to the \*estimation\* problem. If you can’t measure progress, you probably can’t estimate either. The shift away from code that can be measured with LOC makes it that much harder to measure progress


Test for invisible progress– How much progress? (Software measurement) How much more progress can we make with our current resources? (Software estimation)


What are Inefficiencies?


SDLC– The SDLC is what is inefficient. (primary, secondary activities, e.g. analysis, code, source control, build, etc. etc.) Bottle necks here are more technical, physical, e.g. it takes long time to build, slow debug process, etc.  

Social bottlenecks, eg. inter\-team communication, interperson communication, customer\-team communication


Communication tools\- In person, phone, IM, email, memos (word documents), PPT shows \<– unstructured communication.


What are disparate projects?


In particular, different tools, ie. as you move thorugh the SDLC, you have a lot of context switches, for example here is a SDLC with many tool context switches: IDE–\>Source Control (subversion)–\>Text Environment –\>Communication Env (Word/Email) –\>Reporting (ad hoc) –\>Work flow (white board)


What is a lack of discipline?


Missing, wrong or bad process.


Evidence of discipline:  

\- formally defined workflows  

\- formally defined responsibilites (specialists, not a collection of 1 man teams)  

\- accomodating different skills (i.e. explicit consideration of the fact that there is a singnificant learning curve, different skill levels, etc.) i.e. training \& progressive increase in duties  

\- someone collecitng metrics  

\- someone doing estimates, collectin data on estimates: metrics \+ predictions  

\- improvement feedback loop (formally identify problems \& solutions)


Problems lack of money causes:


Fewer people, fewer tools, less formal training, fewer outside experts. Can make existing problems worse.


However…some problems can’t be solved with more money, i.e. necessary but not sufficient resource


Challenges in curing this– organizations don’t spend money on IT because it is a task peripheral to the main organization’s mission (running government, selling stuff, etc.)


Generic Solutions  

Invisible progress: collect metrics! publicize it! Pay the cost of collecting metrics.  

Inefficiencies: Formalize improvement process! (identify \& solve, duh)  

Disparate tools: Pick integrated tools (prefer IDE plug ins over separate tools)  

Lack of discipline\- adopt some sort of softare process. Works best if there is a advocate for process on the team, preferably the project manager.  

Small budget\-Solve other problems first. (spend carefully, duh)


MS Solutions  

Visual Studio– plug ins, VSTS has metrics, formalized communication (bug tracker, feature tracker, tracker\=workflow, reports, even datawarehousing style reports)  

Editions encourage specialization (implies about 4 kinds of developers on a team)


PRICE OF TEAM SYSTEM  

MSDN \= 5 user license for team server \+ 1 dev environment, \~$2,500/yr (not clear about other 4 developers licenses, presumably dev env will need to be purchased separate for each)  

Team System Server — (not clear what price is, presumably $$ if more than 5 users \+ per user costs)Dev Env not targeting team system\- $0 – $800  

Dev Env targeting team system \= $5,500 \-\> $11,000 (!!) each!


Despite the sticker shock when comparing against say a MSDN subscription, this may be cheap when comparing against Rational or other IDEs meant for huge programming teams (50\+ developers)


Conclusion. Team System is for big companies. Everything up to VS200X Pro is for small teams. If you use VS200X Pro, you will still need affordable source control, collaboration, etc. Can use CodePlex if the project if opensource (which is essentially free Team System Hosting)