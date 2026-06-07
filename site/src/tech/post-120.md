---
date: '2006-03-29'
recovered_from: wayback
slug: post-120
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200603\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=120
title: Component Designer in Visual 2005 kind of broke
---


The component designer allows you to graphically represent an object on the designer. This used to be on the same canvas as textboxes and labels, was moved to an onscreen tray in VS2003, and then moved to it’s own screen in VS2005\.


The components mostly generate code that goes into the InitializeComponent sub, which is executed on the Page\_Init event. Some properties are stored in resource files (.resx) The code also has some calls to ISupportInitialize.BeginInit and EditInit, which I think have something to do with letting the component know if they are in design time or runtime.


Conversion is causing me a lot of grief. The resource files changed layout. They used to be XML of one version, now they are XML of another version.


And sometimes the Page\_Init event seems to fail to fire on converted visual components. Check that the sub has the “Handles Me.Init” clause  

My solution has been to move the generated code out of the code generated sub and manually set up a Page\_Init.