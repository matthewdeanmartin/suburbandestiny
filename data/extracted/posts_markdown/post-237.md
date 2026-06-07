---
date: '2007-06-22'
recovered_from: wayback
slug: post-237
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200706\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=237
title: OpenId vs CardSpace Smackdown
---


CardSpace means your site needs:



> \* to be running ssl, with a confirmed location and organization name to prevent warnings.
> 
> 
> \* to be running with an account that can access the ssl certifications (ASPNET account, NETWORK SERVICES, etc)
> 
> 
> \* to decipher the claims, you need to decrypt the certificate and the associated claims, hence the need for access to the machine’s ssl certs (It appears to be POST and rather hard)
> 
> 
> \* you have to use cobbled together controls from the internet
> 
> 
> \* Optionally a third party. The user can act as their own certificate issuer.
> 
> 
> \* The server can be any OS, but the client has to be XP2 or Vista


OpenId means your site needs


\* a third party website to process the passwords


\* ideally the users will want to get their own URL (so that their identity is as strong as the domain name sales process, woo hoo!)


\* The user claims are posted back in the URL (REST is easy)


\* you have to use cobbled together login controls from the internet


\* The server and the client can be anything


I have an OpenID logon almost working, I got close to a working CardSpace logon control, but ran into the SSL cert issues.