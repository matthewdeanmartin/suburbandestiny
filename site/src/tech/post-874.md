---
date: '2020-01-16'
recovered_from: wayback
slug: post-874
source_file: data\normalized\suburbandestiny.com\Tech\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=874
title: Is working with Python Environments a barrier to Python use?
---


**Vanilla Installs**  

easy!  

What is everyone complaining about?  

I only need one python ever!


Oh I got app 1 installing dependencies over app 2 because I’m installing everything to the system python and I have to run as admin or sudo pip install everything!


**Virtual envs**  

python \-m venv venv  

Pycharm’s venv creator  

venv wrapper  

activating with activate.bat and dot sourcing  

looking at PATH to figure out why nothing works  

adding PYTHONPATH for things that for some reason can’t be in the venv


**Oh, but I will never need another python.**  

Yeah right, python 2 and 3 everywhere, 2 often unavoidable.  

Pypy can solve perf problems  

You probably don’t want to migrate to 3\.n to 3\.n\+1 because libraries take a while to catch up so you’re switching back and forth  

Oh, you’re going to stick with 3\.1 forever? Pip just installed the latest version of a lib that doesn’t support 3\.1, do you know how to pin your dependencies?  

Oh you found a bug that is fixed, but now you need to move away from 3\.1, etc.  

So now you need pyenv, pywin and or tox. Tox does cross python testing, pyenv/pywin do interpreter switching


**Ah, my versions are pinned, I have no more problems**  

Dependency A depends on B 2\.1 and Dependency C depends on B 2\.3\. Pip out of box provides no clues why everything is broken  

Thanks okay, I’ll use pipenv. Now I can get a graph to see where the transitive problems are and get warnings when they happen. Also, I can separate out development dependencies so that the dependency graph for a production release is simpler.


**No more problems, yes sir.**  

“Can’t find FORTRAN compiler” – Yes, some common data science library have FORTAN dependencies.  

Oh, easy, I just won’t do datascience, just Postgres. “Can’t find C\+\+ compiler. Can’t find Python.h. Can’t find libfoo.so”…. Oh, I guess I need to install tool chains. Or learn to install wheels. Or realize that if you have a lot of native dependencies, maybe you should use conda.


**No more problems? Everyone on the team did the exact same thing, identically. All easy now?**  

Well actually they didn’t, all of the above are slightly different for each OS.  

But lets imagine everyone did have the same workstation  

The build environment runs in docker, often in a linux distro with most dependencies.This is so reliable, why didn’t we just use docker all the time? It is very, very slow if you’re writing to it all the time.  

The production environment runs in docker often a small distribution like alpine, except many ordinary packages lack the corresponding apk to do installs  

VMs and Vagrant are often too slow.  

And finally, you generally need a bunch of bash scripts to make this run in production. To get them to work on windows, you’ll need gitbash, or mingw64, or cygwin, all of which behave differently  

But what about Ubuntu on Windows (WSL?) – Until WSL2 is release, performance is really bad for anything involving IO, but some people can put up with it. Also not supported by free Pycharm, AFAIK.