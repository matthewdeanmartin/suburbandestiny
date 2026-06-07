---
date: '2008-11-06'
recovered_from: wayback
slug: post-479
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200811\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=479
title: Developers think other developers are retarded
---


These commenting patters are so common, it can only mean one thing, us developers think other developers are clinically brain dead.


Because we can’t read pascal or camel case, all method names have space expansion for comments. Which would be okay if that wasn’t the only comment.


//get value  

public void getValue(){  

}


Because we can’t read call signatures, why not repeat it?


//a public method returning no value taking one integer argument  

public void setValue(int x){  

}


Because you are too stupid to get it if you don’t read it twice


//getValue  

public int getValue(){  

}


And we figure you probably don’t know English either, because words like “get” and “value” are pretty obscure and technical.  

//retrieve a number  

public int getValue(){  

}


Because we don’t give a flying f\*ck about comments, might as well make them all the same


//sets the value  

public void getValue(){  

}  

//sets the value  

public void setValue(){  

}


Or empty but pretty.  

///////////////////  

//  

///////////////////  

public void setValue(){  

}


And why stop at method names?  

//declare integer variable and initialize to zero  

int i \= 0;


Trust me, if you don’t understand the code, you won’t understand the above comment either. Comments aren’t for teaching elementary programming. If you can’t read variable declarations, you have bigger problems to worry about. (On a serious note, using methods using recursion, call back methods, etc, maybe should provide a note and maybe a link to wikipedia on how the technique works)


All examples come from real code.