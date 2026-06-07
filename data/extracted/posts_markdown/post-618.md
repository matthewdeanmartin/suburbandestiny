---
date: '2011-05-31'
recovered_from: wayback
slug: post-618
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201105\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=618
title: Mercurial and .hgignore
---


The .hgignore file must exist before the /bin/ /obj/ etc files exist. If you edit the .hgignore file after the /bin files have been created, you have to tell tortoise to forget the files. In my case, it was easier to completely empty out the folder by moving all the files outside of the repository folder \& then re\-adding them– this time with the .hgignore file in place.


The file needs to be at the root of the repository. This is an unlikely cause of the problem. It isn’t clear if putting the .hgignore file in every @\#$@%^ folder helps.


There are about six ways to exclude /bin/,


glob:/bin  

glob:\*/bin/\*  

glob:bin/  

regex:\\/bin\\/  

glob:\\/bin\\/


And so on. God knows which one actually works, it isn’t clear if putting every @$!@% version in the .hgignore file will trigger an ignore.


Anyhow, I never had this problem with Ankh and Tortoise SVN. Tortoise SVN understood windows and Ankh understood .NET projects. The corresponding mercurial products don’t seem to understand either, and seem reluctant to ignore.


Personally, I’d rather a version control tool that was reluctant to ‘add’.