---
date: '2010-09-10'
recovered_from: wayback
slug: post-805
source_file: data\normalized\suburbandestiny.com\root\__query__\p\805\index.html
source_site: suburbandestiny-tech
source_url: http://www.suburbandestiny.com/?p=805
title: A machine parseable context free grammar for toki pona
---


This is entirely based on jan Kipo’s work.  




[The free command line parser](http://www.agfl.cs.ru.nl/).


This generate the parser:  

**agfl.exe tokipona.gra** 


This executes the parser:  

**agfl\-run.exe tokipona.aob**


Should you run the parser, it will create a graph of the sentence. If it thinks the sentence isn’t grammatical, you get no feedback at all.  The first thing one notices is that a simple sentence usually can be parsed many, many different ways.


[PDF explaining the meta\-syntax](http://www.agfl.cs.ru.nl/papers/manual28.pdf).


The text below is 2 files, tokipona.gra and tokipona.dat


**\#Starting tokipona.gra**


 `#Version 0.01`


`GRAMMAR tokipona.`




```
GRAMMAR tokipona.

LEXICON tokipona
DEFINES
    OWORD.

ROOT Utterance.

Utterance:
  Sentence,[ "." ];
  Answer,[ "." ];
  Vocative,[ "!" ];
  Interjection,[ "!" ].

Interjection:
  I;
  NP;
  "a".

I:
  "a";
  "a a";
  "a a a";
  "o";
  "pakala".

Vocative:
  NP,"o".

Answer:
  NP;
  VP;
  PP.

Sentence:
  "taso", [ Cond ], [ Vocative ], NP_PLUS, VP, "[", "li", VP, "]";
  [ Cond ], [ Vocative ], NP_PLUS, VP, "[", "li", VP, "]";
  [ Vocative ], NP_PLUS, VP, "[", "li", VP, "]";
  NP_PLUS, VP, LI_PHRASE;
  NP_PLUS, VP.

LI_PHRASE:
  "li", VP;
  "li", VP, LI_PHRASE.

Cond:
  NP, "la";
  Sentence, "la".

# roughly subject
NP_PLUS:
  "o";
  "mi";
  "sina";
  OWORD, "li";
  NP_MINUS, "li".

#defined above in lexicon section
#Oword:
#  WORD.
#any word in tp except: li. la. e, o, pi, mi, sina, [en, anu, a, mu] (probably but status to be decided)  

WORD:
  OWORD;
  "mi",
  "sina".

NP:
  WORD;
  NP_MINUS.

NP_MINUS:
  NP, WORD;
  NP, "pi", NP_MINUS;
  NP, Conj, NP;
  NP, Num;
  NP, "pi", PP.

Conj:
  "en";
  "anu".

PP:
  XPrep, NP.

XPrep:
  Prep;
  XPrep, NP.

Prep:
#  P;
  "poka";
  "sama";
  "kepeken".

#kepeken (doesn't work in verb slot)  (surely there will be more)

Num:
  [ "nanpa" ], Dig;
  Dig, [ "nanpa" ].

Dig:
  "ala";
  "wan";
  "tu";
  "mute";
  "luka";
  "ale";
  "ali".

#(probably more, like the last, frowned on)  

#WORDs here should be same
VP:
  VC, "[", "e", NP, "]", WORD, [ PP ], WORD;
  VC, "e", NP;
  VC, WORD, [ PP ], WORD;
  VC, WORD;
  VC.

#Verb complements
VC:
  WORD;
  NP;
  PP;
  XM, VP.

#some sort of modifier
XM:
  M;
  XM, NP.

#assuming this is modifiers, including mi, sina
M:
  WORD.
  WORD, M.
```


`#assuming this is modifiers, including mi, sina  

M:  

WORD.  

WORD, M.`


**\#tokipona.dat**


`"a" OWORD  

"akesi" OWORD  

"ala" OWORD  

"ale" OWORD  

"ali" OWORD  

"anpa" OWORD  

"ante" OWORD  

#"anu"  

"awen" OWORD  

#"e"  

#"en"  

"esun" OWORD  

"ijo" OWORD  

"ike" OWORD  

"ilo" OWORD  

"insa" OWORD  

"jaki" OWORD  

"jan" OWORD  

"jelo" OWORD  

"jo" OWORD  

"kama" OWORD  

"kala" OWORD  

"kalama" OWORD  

"kama" OWORD  

"kasi" OWORD  

"kepeken" OWORD  

"kili" OWORD  

"kin" OWORD  

"kiwen" OWORD  

"ko" OWORD  

"kon" OWORD  

"kule" OWORD  

"kute" OWORD  

"kulupu" OWORD  

#"la"  

"lape" OWORD  

"laso" OWORD  

"lawa" OWORD  

"len" OWORD  

"lete" OWORD  

#"li"  

"lili" OWORD  

"linja" OWORD  

"lipu" OWORD  

"loje" OWORD  

"lon" OWORD  

"luka" OWORD  

"lukin" OWORD  

"lupa" OWORD  

"ma" OWORD  

"mama" OWORD  

"mani" OWORD  

"meli" OWORD  

"mi" OWORD  

"mije" OWORD  

"moku" OWORD  

"moli" OWORD  

"monsi" OWORD  

"mu" OWORD  

"mun" OWORD  

"musi" OWORD  

"mute" OWORD  

"nanpa" OWORD  

"nasa" OWORD  

"nasin" OWORD  

"nena" OWORD  

"ni" OWORD  

"nimi" OWORD  

"noka" OWORD  

#"o"  

"oko" OWORD  

"olin" OWORD  

"ona" OWORD  

"open" OWORD  

"pakala" OWORD  

"pali" OWORD  

"palisa" OWORD  

"pan" OWORD  

"pana" OWORD  

#"pi"  

"pilin" OWORD  

"pimeja" OWORD  

"pini" OWORD  

"pipi" OWORD  

"poka" OWORD  

"poki" OWORD  

"pona" OWORD  

"sama" OWORD  

"seli" OWORD  

"selo" OWORD  

"seme" OWORD  

"sewi" OWORD  

"sijelo" OWORD  

"sike" OWORD  

"sin" OWORD  

"sina" OWORD  

"sinpin" OWORD  

"sitelen" OWORD  

"sona" OWORD  

"kama" OWORD  

"soweli" OWORD  

"suli" OWORD  

"suno" OWORD  

"supa" OWORD  

"suwi" OWORD  

"tan" OWORD  

#"taso" OWORD  

"tawa" OWORD  

"telo" OWORD  

"tenpo" OWORD  

"tomo" OWORD  

"tu" OWORD  

"unpa" OWORD  

"uta" OWORD  

"utala" OWORD  

"walo" OWORD  

"wan" OWORD  

"waso" OWORD  

"wawa" OWORD  

"weka" OWORD  

"wile" OWORD`