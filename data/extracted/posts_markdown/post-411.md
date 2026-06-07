---
date: '2008-08-31'
recovered_from: wayback
slug: post-411
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200808\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=411
title: Catch/Rethrow
---


How often do you see this pattern (or variations on it)


try{  

…some code…  

}  

catch{  

throw;  

}


Sometimes it will be catch(Exception ex) or catch(SomeParticularException ex), and sometimes it will be throw; or throw ex;, there is no finalizer block, but the important thing is that NO OTHER ACTION IS TAKEN (no logging, no retry, nothing else in the catch block).


As far as I can tell, this is equivallent of wrapping code in NOP (no\-operation) commands.


Please don’t do this.