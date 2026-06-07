---
date: '2007-09-12'
recovered_from: wayback
slug: post-279
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200709\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=279
title: 'DTS: Unfriendly BIDS message'
---


And just what exactly am I supposed to do with this?


![](https://suburbandestiny.com/tech/wp-content/uploads/2007/09/091207-1347-dtsunfriend1.png)


“Unable to cast COM object of type ‘Microsoft.SqlServer.Dts.Runtime.Wrapper.PackageNeutralClass’ to interface type ‘Microsoft.SqlServer.Dts.Runtime.IObjectWithSite’. This operation failed because the QueryInterface call on the COM component for the interface with IID ‘{FC4801A3\-2BA9\-11CF\-A229\-00AA003D7352}’ failed due to the following error: The application called an interface that was marshalled for a different thread. (Exception from HRESULT: 0x8001010E (RPC\_E\_WRONG\_THREAD)). ”


This may have something to do with the DTS.dll COM component not being registered.  I haven’t followed up on that theory.