---
date: '2008-01-28'
recovered_from: wayback
slug: post-318
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200801\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=318
title: License Mixing from a CDDL standpoint
---


Wow I can’t believe how long this document got.  I just wanted to be able to get $25 bucks from ordinary people who use my software, but can afford to pay, to get code contributions from developers who want to use my software but don’t want to pay, and not give my code away to people so that they could sell it for $24\.50 and discourage anyone from buying from me.   And I don’t want anyone suing me for relying on my product and suffering some dread fate.


So far dual licensing with CDDL looks the best.


Contributing new code is okay under the CDDL license, just follow the relevant rules to hold harmless, etc.


But what if I find a cool library, API, code snippet, DLL, control, JAR, etc that someone has released for free on the web? Can it be used with the open source project I’m currently working on?


Often…no! 


Viral licenses, GPL, CDDL require careful consideration of what code you mix in with existing code.  In fact, a viral license may prevent change an existing code base from proprietary to open, depending on what licenses are already mixed in.  The FSF has a long list of [GPL incompatible licenses](http://www.fsf.org/licensing/licenses/).


For example, the Free Software Foundation says that CDDL and GPL are incompatible:



[Common Development and Distribution License (CDDL)](http://www.opensolaris.org/os/licensing/cddllicense.txt) 

This is a free software license. It has a copyleft with a scope that’s similar to the one in the Mozilla Public License, which makes it incompatible with the [GNU GPL](gpl.html). This means a module covered by the GPL and a module covered by the CDDL cannot legally be linked together. We urge you not to use the CDDL for this reason.


Also unfortunate in the CDDL is its use of the term [“intellectual property”](http://www.gnu.org/philosophy/not-ipr.xhtml).


\[Sigh.  The link to the essay on "intellectual property" is disheartening.  Mr. Stallman is trying to say that property rights between physical and intangible things are somehow different.  A more rigorous understanding of ownership of property demonstrates that ownership is a bundle of intangible rights, like the right to use, dispose, sell an object.  The property right is to the intangible ability\-\- the physical object is just a distraction.  Stallman has not earned the standing to make a statement like "Economics operates here, as it often does, as a vehicle for unexamined assumptions."  I might as well be saying nuclear physicists are a bunch of raving lunatics and whining ninnys, despite me not know squat about nuclear physics.]


Or maybe license incompatibility isn’t so bad!    

LAMP applications are often developed as a single unit, yet they use GPL, Apache, Hybrid and PHP licenses respective, which the FSF says are incompatible with each other.


Dual Licensing  

Make different versions that are released under different licenses.   So there might be a CDDL version and a GPL version.  Contributors would could contribute to the GPL branch and mix in GPL code.  Alternatively they could contribute to the CDDL version and take advantage of it’s superior terms.


Copyright and Dual Licensing  

The choice to do dual licensing can only be done by the original project’s copyright holder.  


Merging and Dual Licenses  

You can’t merge GPL improvments back into the dual licensed branch of code.  This is a strange restriction because when GPL is violated, the party that has standing is the copyright holder!  Unless the chosen opensource license gives users and contributors standing, I don’t see how they could stop a copyright holder from periodically merging the proprietary and opensource branches, unless the contributor retains rights to the contribution.  


If the contributor is retaining rights to the contribution, then he could take action against merging.  If the license says that contributions are automatically granted to the original copyright holder, then merging is OK.


If the contributor didn’t have the rights to his contribution in the first place, (say the contributor stole some proprietary code) then merging could pose a risk to the the original copyright holder trying to sell under a proprietary license.


Trade Marks and Dual Licenses  

You might want to give the open source and closed source product a different name, since a trademark is a signal to the market that one company has done something to enforce quality.  An open source product uses different means to create quality.


Forking and Dual Licensing  

Because only the orginal copyright holder can release a proprietary version, forks don’t normally pose a competitive risk


Purism and Dual Licensing  

Purism is a sign of obsessive compulsive personality disorder being projected onto software licensing.  Just because some GPL users are OCPD doesn’t mean non OCPD developers should strive for a perfect ‘all GPL’ world.


What about LGPL?  

LGPL specificly talks about allowing code mixing with dynamically link libraries, a specific technology for mixing code.  CDDL allows for code mixing on a file based level, which allows for mixing licenses that are statically or dynamically linked.  (This may be a red herring, since some LGPL licenses say “static or dynamic linking”)



Incentives LGPL and Dual Licensing  

If I am a commercial developer and want to sell some code, I will look for open source licenses that allow me to mix free code with my proprietary code.  If I take an LGPL licensed work and put a thin layer of my code over the top, I can start selling it.  This would compete with the original copyright holder’s commercial version.


On the other hand, if I am a commercial developer, I might use the open source version as a trial version, and then buy the commercial license if I didn’t want to deal with the viral features of GPL or CDDL.


Viral to the Modifications, Viral to the Derived Works



In CDDL, you only need to make your modifications to the CDDL work opensource.  If you compose the CDDL code, statically or dynamically (what ever that may mean), [the derived work doesn’t have to be made open source](http://weblogs.java.net/blog/evanx/archive/2006/06/mayhem_roundup.html).


Can you change your mind?  

You can change your mind with a proprietary license, but many open source licenses are forever.  Also, because the licenses are long lived and are based on licenses who’s official version might change!  So at the very least, you might want to pick a type of license that has something to say about versioning or that doesn’t refer back to the “latest greatest” license that some foundation has tweaked.


Blogged with [Flock](http://www.flock.com/blogged-with-flock "Flock")