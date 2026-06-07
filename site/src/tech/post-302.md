---
date: '2007-11-06'
recovered_from: wayback
slug: post-302
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200711\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=302
title: 'ASP.NET: Grid Layouts'
---


**Goal**: Recreate the world of Windows Forms in the browser and generally not use the flow layout engine of the browser.


**Options:** Embedded GUIs (Flash, Java, Silverlight), CSS absolute positioning, CSS Grid, Table Layout.


**Embedded GUIs** means picking an entirely different technology that happens to be able to run as a browser plug in. They require a completely differnt skill set (maybe different staff), more configuration on the client side, are less accessible, etc. I’ll skip discussing this option.


**CSS absolute positioning.** CSS absolute positioning means adding this to all elements:


style\=”position:absolute;top:248px;left: 536px;width: 105px;height: 8px;”


You can improve readability by moving it to a separate css file, but the result is the same, one CSS style per element, which defines size and location.


**CSS grid**. In the paper and ink design world, designers create various grids with various distances between columns, various distances between rows, (i.e. *not necessarily* a grid like green math class square grid graph paper). Design elements align to the grid and look better for it.


\[place holder, still looking for a site with grid layout tools or templates]


As far as I can tell, CSS grid techniques rely on floating lots of divs around a page in such a fashion that they necessarily line up correctly.


**Table grid.** Table layout works, but is inaccessible, hard to maintain, etc. etc. It is easier and MS Expressions Web provides a good tool for table layout.


**Tools.**MS Expression Web \= Visual Studio 2008 HTML designer, almost.


[VS2008Beta2 in many ways is worse than VS2005](http://blogs.msdn.com/mikhailarkhipov/archive/2007/02/26/what-is-not-in-the-vs-orcas-web-designer-compared-to-expression-web.aspx). Keep in mind I’m reviewing Beta 2, for all I know all this is fixed in RTM. For example you can’t select multiple items at one time, you can’t drop a new control onto a form and expect it to land where you click (it slides to the upper right hand corner). Also, selecting controls via remote desktop is painfully slow leading to many accidental resizings, mis\-draggings and setting properties on the wrong control. Using a visual desginer requires video game level responsiveness from the graphical environment and RDP prevents that (or VS2008Beta2 prevents it, I haven’t tested VS2008Beta2 on a local machine yet)


**Overlapping Boxes**. The text box heights that you see in the designer preview don’t match the heights you see in MSIE7 or Firefox (both browsers show the boxes as taller)


**Unaligned Boxes.** VS2005 has the Format/Align/Bottoms (and variations), which fix some of aligmnent woes.


**Mixing Flow and Absolutely postioned Elements.** Typcially you will have a flow layout for headers, sidebars and footers. Design your absolutely positioned layout in a separate page. When done, put in in two div like this:


\<div style\=”height:500px”\>  

\<div style\=”position:absolute;”\>  

(Your absolutely positioned elements go here)  

\</div\>\</div\>


**Pathalogical Sensitivity to Font Resizing**. VS2005 absolute position means elements are pinned at corners, so as fonts grow, screen elements begin to overlap. This means, imho, that layouts break sooner than they would if they were a flow layout.