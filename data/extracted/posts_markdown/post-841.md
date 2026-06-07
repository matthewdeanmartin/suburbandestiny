---
date: '2016-05-07'
recovered_from: wayback
slug: post-841
source_file: data\normalized\suburbandestiny.com\Tech\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=841
title: Adapting a template for a resume
---


For various reasons, I’ve become way to familiar with the technologies associated with creating resumes. For the record, the coolest are: [CV Maker](https://cvmkr.com/), [LaTeX resume templates](https://www.sharelatex.com/templates/cv-or-resume), [JsonResume](https://jsonresume.org/) and just about anyone’s HTML5 resume template. The HTML5 templates are written by people who actually have artistic taste, so they look beautiful. No way could I do the same in a short time, so I bought a template. (Never mind that the Template store’s UI let me buy the wrong template before I bought the right one, let’s focus on the happy parts of this experience.)


To use it for my self, I had to:


**Assemble the raw material for a resume.** StackOverflow Careers is my ground truth for resume data. From there I copy it to USAJobs and so on.


**Load it up in Intellij** Visual Studio with Resharper is not too bad, but if you just use Intellij, you get all the goodness that Resharper was giving you and more. 


**Disable the PHP mailer** A contact form is just a spam channel. Don’t ask me why spammers think they can make money sending mail to web admins (unless maybe it’s spear phishing). I considered not showing my email address, but the spam harvesters already have my email address and google already perfectly filters my spam.


**Strip out the boiler plate.** Every time you think to got it all, there is more references to John Doe.


**Fix the load image.** The load image was waiting for all assets to render before it would remove the annoying spinner and curtain. But the page did not have any elements that the user might interact with too early. The page didn’t have any flashes of unstyled content like you see with Angular. There weren’t any UI element suddenly snapping into place on the document ready event like a certain app I’ve worked on before.


**Deminimize the code.**  This should be easy, right? A template has to ship with the JavaScript source code. But the code was minimized. So I pointed the page to the non\-minimized version. The whole page broke. Finally I noticed the minimized file actually contained version 1\.2 and the non\-minimized shipped was 1\.0\. So I deminimized the code and could begin removing the extraneous load image.


**Upload to my hosted Virtual Machine** . Filezilla all of a sudden decides it can connect, but can’t do anything. Some minutes later, I figure out that TunnelBear, my VPN utility and Filezilla don’t play well together. So I added an exception for my wakayos.com domain.


**Write blog post.** I just wanted my resume to be a nice container. But as a developer, it sort of looks like maybe I wrote this from scratch. I certainly did not.