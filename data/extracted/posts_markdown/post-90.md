---
date: '2003-10-05'
recovered_from: wayback
slug: post-90
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200310\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=90
title: Using Jbuilder to Make a Swing GUI
---


Here are some random observations:


Applicable to All Java Forms


1. Rename your objects, not doing so makes the code unreadable and you will need to be able to read the code.
2. A typical pattern is to have an Border layout, with the title or button in the north, a status bar, instructions or buttons in the south and a nested panel in the center that holds the fields with labels.
3. Add borders to your components while designing
4. Start with absolute positioning and convert it to GridBag.
5. Keep a big reference manual handy for looking up specifics, like which events you need to hook to get a pop up to show.
6. Applets don’t resize, their size is set by the APPLET tag. Resizing is a key feature of a Java Swing form, it allows you to put the same form on monitors of different resolutions. Get around this limitation by creating a launch button in the applet, and on the click event handler, open a new frame. Put all the UI into that new frame.


Jbuilder Specific


1. You will have to edit the source code from time to time, JBuilder can’t always guess which panel you want a control to go to.
2. Sometimes, Jbuilder fails to add a panel to the UI, but leaves the code. You have to do a `panelX.add(myNestedPanel)` command to get it back on the designer.
3. For an applet I was working on I had to manually add my menu bar to the code with `this.setJMenuBar(myMenuBar)`