---
date: '2003-10-04'
recovered_from: wayback
slug: post-88
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200310\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=88
title: Getting MS Explorer to Swing
---


I want to write an application that uses the Swing library and runs on any MS Explorer machine, without the client installing extra software or changing evironment variables, or spending a day dowloanding.


Here is what I’ve learned:


1\) People complain about Swing, for being big \& slow, but it has more features \& better looks than VB forms. The other UI for java include: HTML, AWT, commercial \& free non\-Sun component libraries, \& command line. For my main goal right now (showing off), these other options don’t measure up.  

2\) Mozilla 1\.0 requires a manual file copy to get the Java plug\-in to work  

3\) MSIE can do Swing if you unjar the file swingall.jar, but loading it from local on a fast machine takes a while. Also, you get a lot of security access errors as the swing form tries to figure out what kind of machine it is one (for plugable look and feel)  

4\) JBuilder has to be set to build for all VMs to get an applet that MSIE can open.  

5\) MSIE doesn’t seem to be able to open a jar archive without special software, although for some reason creating a CLASSPATH environment variable pointing to the swingall.jar file seems to work. (So a jar is OK if it local, bad if you download it? I don’t understand.)  

6\) Using jarg on javaswing reduces it from 2\.2MB to 1\.6MB, which is not much of an improvement \& the applet gets a little broken in the shrinking process.  

7\) Putting java files into a jar is easier if you don’t use a manifest file \& just use : `jar cvf newjar.jar *`  

You execute this command in the root of all your classes \& packages that you want in the jar.  

8\) Packages and jars are headaches, don’t try to include them in your build process if you are still learning. The errors caused by package and jar problems look a lot like other problems (namely they all give Class not found errors)  

9\) MSIE (using VM5\) sometimes crashes the entire computer, I’m not sure if it was Swing related.  

10\) Command line programs should be run using lots of 1 line .bat files. Some applications have such complicated switch syntax it is like writting a mini program.  

11\) Downloading a .jar application and running it is fairly easy, two files often will suffice (the jar file \& a batch file with  

`ava -jar myapp.jar`  

12\)