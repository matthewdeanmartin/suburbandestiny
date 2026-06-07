---
date: '2014-06-07'
recovered_from: wayback
slug: post-738
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201406\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=738
title: Writing code for technical interviews, my opinions so far
---


I like the idea of asking a candidate to write code during an interview, usually I ask a really simple question like FizzBuzz and I tell them what the mod operator is. I doing give a hoot if a candidate knows the mod operator, you rarely use it in line of business applications. I what to know if they can combine a loop and an if block in a reasonable way. If they can, maybe they are incompetent. If they can’t, they are incompetent. This isn’t a silver bullet, the completion of any single programming exercise doesn’t say that much about how they will be able to cope with the technical and social dysfunctions of your organization, which can be more important than mere technical competencies.


**What people have asked me to do**  

Create a database, tables, a stored procedure for read and insert, and create a UI to do the insert and read. If I remember correctly, it was for a Personnel table. The trick was, this one one of about 4 programming exercises for a 2 hour exam. After doing it once, I realized, you could only do it in the time limits if you chose drag and drop techniques like SqlDataSource, and other techniques that leaned on Visual Studio’s code generation. Except all of those techniques (strongly typed XSDs, DataSet driven database development, SqlDataSource that binds to a UI Grid with no middle component) are out of fashion, deprecated and considered harmful for production code. And to do it in 30 minutes, you’d have to have practiced in advanced. If they wanted me to do a code Kata and for it to look as smooth as a on\-stage conference demo, I’d have to practice like conference presenters do. 


I didn’t get that job and the recruiter said the client rejected a whole batch of developers. 


Next job interview. I got a multiplechoice test, and then was told to create a db, create a table, populate it with sample data, write two views (or a stored procedure that used subqueries). I could use the internet. But only 1 instance of sql server out of 3 on the machine were running. They didn’t give me a connection string. I switch to Ms\-Access. But because of MS\-Office’s restrictions, the guest account could not load featuers that involved VBA, so no QueryDefs. I almost got a gridview and sqldatasouce up and running, but without a SQL Designer, I was writing SQL by hand. SSMS was also broken because the trial license had expired. I ran out of time to prove my SQL would work. 


(And there was malware on the machine that injected ads on all sites and then involuntarily redirected you away from a page after a few minutes, so visiting MSDN to check syntax, which they explicitly permitted, was borked until I disabled the malware add on in chrome. I notified them about it and they said it was a junker laptop and they didn’t care)


I was also told to write a REST ready WCF service. Speaking from experience, to set that up and prove it works takes a day. Anyone can right click and create a SCV file and add some attributes. But to demonstrate that it all works you need to:


\- Machine generate a ServiceModel section of web.config. Save it off to a separate file so as it evolves you can easily revert back to a working ServiceModel section.  

\- Create a console app for the host and client. Some bindings aren’t easily testible with a Cassinni or IIS hosted service.  

\- Create tests that separate failures of the underlying code from the service. Also make sure you have a way to test the basic binding so you can differentiate between misconfigured advanced bindings from other errors.  

\- Create a System.Diagnostics section to turn on and off the WCF trace.  

\- Since this is a rest API  

\- Create a template for the Jquery service call, which is about 50 lines of code (most of those lines are success, failure and options settings), but it’s the same for most service calls.  

\- Verify that the JSON serializes and deserializes the way you want it. You may need to pass the data as string and use JSON.stringfy/parse to deal with the JSON  

\- Configure IIS to respond to PUT and DELETE as as well as GET and POST.  

\- Verify that routing and URL are working and that a variety of plausible templates don’t route to the wrong place.  

\- If this was a real world application, a similar amount of effort, equal to the effort described so far will be spent trying to get your organization to punch holes in the firewalls, to get an exotic single sign on server to talk to your app and to figure out why the services work on machine a, b and c but not d, e, and f. 


Instead of conveying my knowledge of that, I was able to convey, with my stupid incomplete SVC file, that I was a rather dim witted developer who was probably faking it.


**Interview Zen**  

This was on the website http://www.interviewzen.com — Solve a programming problem with a screen recorder running, but do so in a browser text box without intellisense or unit test tools. This is sort of unfair. So I solved it in Visual Studio and commented out the dumb lines of code I wrote so they could see how it evolved. This was the most fair test so far, but since I wasn’t going to do this on billable hours, I had to wait until a quiet period on the weekend. Take home programming quizzes will select for people who are not currently working. But people who aren’t currently working and have lots of spare time are also signaling that they aren’t the best candidates! (Or it signals they have slack time at their current job, which is fine, or it signals they don’t give a hoot about productivity at their current job, which is not) So doing good on a take home quiz, is a mixed message.


**A Modest Proposal**  

If you want to ask something more advanced than FizzBuzz, then let them take the test home, let them use all available tools, let them use their. If you are worried they will just get answers from StackOverflow, make the test hard enough to require programming talent even if you were to post the questions on StackOverflow.