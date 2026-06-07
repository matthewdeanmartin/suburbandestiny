---
date: '2016-05-06'
recovered_from: wayback
slug: post-833
source_file: C:\github\dead_blog\data\normalized\suburbandestiny.com\Tech\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=833
title: How to do postbuild tasks painlessly in Visual Studio
---


So, you’d think you’d need to write custom msbuild targets or even learn msbuild syntax. Wrong!


(okay, some of this can be done via the project properties, the “Build Events” tab. The “Build Events” tab hides the fact that you are writing msbuild code and now you have batch file code embedded into a visual property page instead a file that can be check into source control, diffed or run independently.)


You will have to edit your csproj file.


1\. Create a postbuild.bat file in the root of your project. Right click for properties and set to “always copy”. A copy of this will now always be put in the bin\\DEBUG or bin\\RELEASE folder after each build.


2\. Unload your csproj file (right click, “Unload project”), right click again to bring it up for edit.


3\. At the very end, find this:  

`<Target Name="AfterBuild">  

<Exec Command="CALL postbuild.bat $(OutputPath)" />  

</Target>`


The code passes the \\bin\\DEBUG or \\bin\\RELEASE path to the batch file. You could pass more msbuild specific variables if you need to.


Strangely, the build output window will always report an error regarding the first line of the batch file. It will report that SET or ECHO or DIR or whatever isn’t a recognized command. But the 2nd and subsequent lines of the batch file run just fine.


From here you can now call out to powershell, bash, or do what batch files do.