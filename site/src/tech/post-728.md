---
date: '2014-03-23'
recovered_from: wayback
slug: post-728
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201403\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=728
title: Launching WinForms apps from a console
---


This is harder than it seemed like it should be.


I wanted to have a console app with trace. I like tracing to a console. But if I’m writing a console app, the trace is going to interleave with the UI. So I thought, I’ll create a win form class and then Applicatin.Run() it, then send text to a TextBox. And I’ll get pretty trace in a window other than the main Console. 


So I did that, and the application blocks on Application.Run(), meaning the form responded to clicks and key presses, but the console freezes and executes no code.


So I learned to do form.Show() plus Application.DoEvents(), which shows the form, allows the console code to run, and then lets the form UI update.


But things still seemed blocked… and they were. This time because Console.ReadKey() was blocking. So I change Console.ReadKey() to a while\-Thread.Sleep(250\) and I could then move both windows, and send output to both windows via my TraceListener and ordinary console commands.


Console is single threaded, so is is easy to get blocked, which blocks any Forms it might have spawned. Also, Forms really doesn’t like to be manipulated from a thread different from the thread that created the Form. So some kinds of cross window communication blew up.


So that was my experiment. I guess the alternative would be to write to a WPF window, which could potentially make very pretty trace, but I don’t know if it would be worth my time to learn WPF.