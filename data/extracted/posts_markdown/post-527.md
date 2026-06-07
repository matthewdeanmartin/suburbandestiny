---
date: '2009-04-26'
recovered_from: wayback
slug: post-527
source_file: data\normalized\tech.wakayos.com\root\__query__\m\200904\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=527
title: Brave new world of Web Services
---


So I’m writing a programmer Kata (that is an exercie I expect to repeat several times, just because I want to improve my skills as a developer).  I’m writing a a better movie meetup application.  The first use case is a user adds an event.  But the user has to look up the movie theater location, time, place, either manually–and that is a lot to ask from a user,  or look it up in a table I maintain, and that is too much to ask from me.  But Movies.com, Fandango.com, Google.com/movies, Yahoo, imdb.com, Netflix.com  and more already have movie and/or theater and showtime information.


Movies.com and Fandango.com are both restrictive in their TOS. You can link to their home page, other wise, they want you to f\*\-off.  No API’s outside of RSS feeds anyhow.


Fortunately, other companies have API’s with liberal TOS, i.e. free, allow sufficietly large number of requests per day and allow commercial use, Google and Netflix the best of the TOSs.


Google.com has API’s, but google.com/movies has to be screen scraped. We got the technology, but I can’t tell if I have the right.


Yahoo has the API’s, but they will give you the location of the theater(s), but not showtimes.


Netflix.com has the API, but they only have movie review and description information.


All of these services could be cancelled at any moment, could change their business model, or change their interface.  So my application will still need to have all the code necessary to input theaters, movies, and showtimes manually.


All of a sudden, this is a lot of work to avoid duplicating the work of listing theaters, movies and showtimes available for going out to the movies with a group of friends!