---
date: '2015-01-20'
recovered_from: wayback
slug: post-786
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201501\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=786
title: Things that went wrong trying to run pydoc
---


This is from the standpoint of a beginning python developer on windows. I assume you are like all other python developers and just stare at the machine to twiddle the electrons. These are my in progress notes on getting pydoc to run.


Install [python](https://www.python.org/downloads/windows/). Install it over and over because it is just like Java, and .NET, dozens of side by side installs.  

Install [pip](https://pip.pypa.io/en/latest/installing.html). It may or may not already be there.  

Install [pywin](https://github.com/davidmarble/pywin). I have no idea if it helps. My generators only generated for 3\.3\.  

Install virtual environment so you don’t junk up the global interpreter with packages. 


You will want to get c:\\python33\\c:\\python33\\scripts in the path. Set the path the old fashioned way. If using powershell, reload the environment over and over. (pywin is supposed to help for this)



> $env:Path \= \[System.Environment]::GetEnvironmentVariable(“Path”,”Machine”)


ref: https://stackoverflow.com/questions/17794507/reload\-the\-path\-in\-powershell


Okay, check it like this



> $env:Path.Split(“;”) \| Where {$\_.Contains(“yth”)}


The goal is to get all the sphinx cruft into a \\doc\\ folder. The whole mess will fight this every step of the way.


cd over to your source code folder (maybe) and run this. (I’m not sure about the best folder, initially I tried running from the c:\\python33\\source folder, which junks up the python directory. Which seems wrong.)



> sphinx\-quickstart


If it doesn’t run, your path is screwed up. This command creates a conf.py  

When answering, most of the time you answer the default, except for the API doc stuff, which appears to be “n” by default. It appears that people use pydoc not just for python api documentation, but for autobiographies and they cater to that scenario first.


You’ll need to edit that conf.py


Install [nano](http://www.nano-editor.org/). You could instead open it with word, or some other inappropriate application. At least nano doesn’t kick you out of the console and it isn’t vim.


If the conf file lives in the same directory as your source code, uncomment this:



> sys.path.insert(0, os.path.abspath(‘.’))


Or if the conf.py file is in a sub directory of your app’s directory, use two dots



> sys.path.insert(0, os.path.abspath(‘..’))


Pause. Go edit your python files and add this to anything that will execute code (and not just define functions and classes) so you don’t get side effects when generating documentation. And add some comments of the for “”"blah”"” to your functions. I think this is the [expected syntax for the doc comments](http://epydoc.sourceforge.net/manual-epytext.html).



> if \_\_name\_\_ \=\= ‘\_\_main\_\_’:  
> 
>  launch\_nuclear\_attack()


Create the rst files.



> sphinx\-apidoc \-o api .


(maybe – . . would work better?)  

I got modules.rst and foldername.rst. The modules.rst just has a reference to foldername.rst.


These .rst files are like editable “markdown” like things. They need further processing. Firstly, on my machine, when I run it, it adds the folder name as the package, and then I get a FolderName.filename package doesn’t exist error for each file on the make. So edit the .rst file and fix the package names.


Copy those .rst files into the root of your source control or where ever where ever conf.py is. I think. Put it in all the directories on the workstation if that doesn’t work. This is like working with java, nothing knows where anything is.


Run these, although I have no idea what they do:



> sphinx\-build \-b html . build



> .\\make html


And it spits out some html. Cd to the build/html folder and run this to launch chrome.



> Start\-Process “chrome.exe” “index.html”


I have no idea if this works, my source folder and python folders are littered with crap created all over the place. 


Official docs:  

http://sphinx\-doc.org/tutorial.html Quick start tutorial. If this works for you, then you are the sort of person that didn’t need docs in the first place. Sort of ironic.  

https://codeandchaos.wordpress.com/2012/07/30/sphinx\-autodoc\-tutorial\-for\-dummies/ This is the more useful one, but not in itself enough to generate.  

http://sphinx\-doc.org/man/sphinx\-apidoc.html You need this if you are using it for, I don’t know, python API documentation and not your autobiography.


TODO: Turn this into a .bat and .ps1 file.


Follow up Links  

PyCharm has a built in understanding of Sphinx.  

ref: [Overview](https://www.jetbrains.com/pycharm/webhelp/documenting-source-code-in-pycharm.html)  

ref: [Python Integrated Tools Dialog](https://www.jetbrains.com/pycharm/webhelp/python-integrated-tools.html).