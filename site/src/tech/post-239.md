---
date: '2007-06-25'
recovered_from: wayback
slug: post-239
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=239
title: Solved! YUI Menu Bar “Pop” problem
---


I have a YUI menu bar. It is entirely javascript driven and inserted into a DIV. That means, it is rendered last. In MSIE 7, that causes the entire page to draw, then pop about 20px down to make space for the menu bar. Here is my solution:


\<**div**  

id\=”mymenubarhere”  

style\=”position:absolute;right:0px;left:0px;”\>  




\</**div**\>\<**div**  

style\=”height:20px”\>\</**div**\>  




The absolute positioned element lets everything else slide beneath it. The following div props up the rest of the page. If you put the height directly on the div where javascript will insert the menu, the height will add padding, border or something to create a tiny gap between the menu bar and the drop down menus, making it impossible to mouse over from the bar to the menu.