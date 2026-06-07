---
date: '2008-05-27'
recovered_from: wayback
slug: post-364
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200805\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=364
title: Stsadm for hard core users- Installing Templates with Powershell
---


There is an easy way to [install the WSS3\.0 templates](http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=1634704&SiteID=1) this posted on a forum. But I wanted to try to use powershell to do it. And then the errors started.


Real hard core users can tell if they are pasting ANSI or UNICODE parameters and can see if that is an em dash or an en dash or some other character.


While trying to install ApplicationTemplateCore.wsp, I kept getting “Command line error”, plus a books worth of useless command listing.


[This post gave me the clue that works](http://www.eggheadcafe.com/software/aspnet/29671724/command-line-error.aspx).


Instead of copy/pasting from the readme/MSDN page, retype by hand. I guess this ensures that whitespace and character encoding isn’t anything that Stsadm can’t deal with.


Fortunately, this isn’t a bug because most SharePoint admins have super vision and can see the electrons moving around in the computers memory so they can determine if


“stsadm \-o addsolution \-filename ApplicationTemplateCore.wsp”


is ANSI, Unicode or what have you.


Here is the script that eventually worked.



```
stsadm -o addsolution -filename e:\download_temp\ApplicationTemplateCore.wsp
stsadm -o deploysolution -name ApplicationTemplateCore.wsp -allowgacdeployment -local
stsadm -o copyappbincontent
```

Here is the powershell script to install all the templates.  





```

foreach ($i in get-childitem E:\download_temp\*.wsp) {
     if(!($i.Name -eq "ApplicationTemplateCore.wsp)){
    stsadm -o addsolution -filename $i
    if($i.Name -eq "InventoryTracking.wsp" -or
       $i.Name -eq "DocumentLibraryReview.wsp" -or
       $i.Name -eq "RoomEquipmentReservations.wsp" 
       ){
       stsadm -o deploysolution -name $i.Name -local -allowgacdeployment
    }
    else
    {
       stsadm -o deploysolution -name $i.Name -local
    }
      }
}

```