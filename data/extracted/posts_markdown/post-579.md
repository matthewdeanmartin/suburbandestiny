---
date: '2009-11-29'
recovered_from: wayback
slug: post-579
source_file: data\normalized\suburbandestiny.com\root\__query__\p\579\index.html
source_site: suburbandestiny-tech
source_url: http://www.suburbandestiny.com/?p=579
title: Language Pre-contruction
---


**NEW**.  I just created the [unofficial Na’vi language mailing list on yahoo]((word list here)  ... and Unofficial yahoo mailing list here).   Please consider joining if you have any interest in deciphering the Na’vi language.


I’m reading [the Wheel, the Horse and Languag](http://www.amazon.com/Horse-Wheel-Language-Bronze-Age-Eurasian/dp/0691058873)e, which is about PIE (and who doesn’t like PIE?)   and I realized that if we can re\-construct PIE, we should be able to pre\-construct Na’vi, the as of yet unreleased language.  We have about 10 words of Na’vi, or fewer words than were used to reconstruct Virginian Algonquian.  We don’t have any related language, although all attested human languages  are potential sources–any new language is likely to rehash something that’s already been done before.   Using the existing 10 words, we probably can construct an alphabet, we know that words are going to be 2 \-15 symbols long, will have a similar phonetic distribution to the samples, will follow the same internal phonetic rules, etc.


**What’s the alphabet?** Identification of the full alphabet might be the first challenge.  If the 10 sample words didn’t cover the whole alphabet, we’d could at best generate the odds that the language has more sounds by comparing it against other common human languages.  Human languages have between [11 and 112 phonemes](http://www.vistawide.com/languages/language_statistics.htm)–with a mid\-range of 61!  I’d be worried about calculating an average because an an average of the \# of phonemes in human languages today will be heavily biased by survivors and correlations between families (i.e. all romance languages will have similar number of phonemes).  Languages end up with phoneme distributions that maximize the distance between vowels (i.e., a language wouldn’t have only i, e, y because they all sound similar)  So if the sample attested language had clusters (too many frictives, too few stops) and few phonemes, we could infer that we were missing letters.


**Finding the Uniform Distributions and the contingent distributions.** I’ve been working on what a word generator would look like.  I figure it would follow some sort of chain process, like, the first letter will follow distribution, where each distribution would have the odds of a letter of the alphabet being the next letter, all odds summing to 1 of course.


1st Letter: a .05, b .03, c .02 … etc for each letter of the alphabet.


2nd Letter when 1st is a:  a: 0 , b .1,  c .2 … etc


3rd Letter when 1st is ab: a: .02, b:0, c:0 …. etc


For an alphabet of 20 letters and words 5 letters long, this distribution has 20^5 parameters (3\.2 million), although most of these are going to be zeros.  Hmm.  Maybe this needs to be constrained in advance.


So if we have say three categories of sounds, 2 kinds of consonants and vowels, we would have a distribution like:


1st letter : voiced consonant : 30%, unvoiced consonant : 65%, vowel 5%


2nd letter if 1st letter is voiced consonant: voiced consonant : 50%, unvoiced consonant : 5%, vowel 45%


The above distributions would have 3^5 \=243 parameters.


If distributions have a short memory–i.e. the odds of a letter appearing depend only on the last 2 letters and the distributions are re\-used on each syllable break, then we have only a few parameters. For example if the maximum syllable is 4 letters, after which any new letters have the same distribution as if a new word was starting, we’d only have 81 parameters to estimate.


I’ll leave as an exercise to the reader the search for additional constraints to get the number of parameters down to less than the number of data points.


**Speaking of data points, how many data points do we have with a word list of 10 words?** We have about 50 letters–not enough to even get the probability distribution for the alphabet.  If we had 20 unique letters, then we’d have 20 probabilities to estimate, or about 2 data points per parameter. The confidence intervals would be huge.  We probably could estimate the distribution of vowels vs consonants or fricatives vs sibilants better than the odds of each particular letter– so if we had 30% frictives, we’d divide 30% by the number of fricatives to get the odds of ‘f’.


**Another possible pattern.** The above phonetic model doesn’t take into consideration “inbetween\-ness”  So if I have a word generator that generates just the consonants, then there would be odds for vowels falling in between certain combinations. This likewise has lots of parameters.  If there are 20 consonants, 5 vowels, then there will be 20 pairs.  Thats 2000 probabilities, admittedly many of them are 0\.


**Illegal Combinations.** If the first letter is a, then the 2nd letter will follow distribution Y, and so on.  If certain probabilities fall below a threshold, round down to zero because it means it is an illegal phonetic combination–some sort of truncated distribution.  I’d say on account of data being short, we’d first assume that unobserved combinations were illegal.  The type and the parameters of the distributions could be estimated from available data using [jackknifing and bootstrapping](http://en.wikipedia.org/wiki/Resampling_(statistics)).  Or simulation.  I guess the series of probability distributions that was most likely to generate the sample data would be the probability distribution for generating new words.


**Stability.** The resulting set of words would then have to go through a stability test.  Certain sound changes in languages are universal, such as the loss of large consonant clusters and maybe things like [Grimm’s Law](http://en.wikipedia.org/wiki/Grimm's_law) (g–\>k–\>h–\>0\)  Words that repeatedly drop out from the vocabulary after simulated test of time would have to be discarded as too unstable.


**Root words**.  All of the attested words probably have root words in them or are compound words, but there won’t be an easy way to say what the root is. Still, out of 1000s of randomly generated words, the group that has chunks of the attested words will have a higher hit rate than the other words.  There of course has to be an upper limit to this– at most a few dozen words can be generated this way.


**Distance between words.** The other constraint would be distance between words.  Language end up with lots of minimal pairs, so minimal pairs are okay.  But beyond a certain threshold, I think the language would either prohibit word pairs or have to introduce stress and tone.  For example, if the generating distributions created an extremely narrow set of words, then we can infer the language is tonal.  Examples would be Chinese which has a small number of syllables, which are given tones to generate more words.


**Vowel and consonant harmony.** The tongue is lazy.  On my favorite podcast, PC Mag Radio, the announcers keep saying AppScout as if it were Abscout. I’m sure it has something to do with the distance the tongue has to move to get from ‘A’ to ‘P’ and back to ‘S’.  Interestingly, AppScout is a portmanteau created by the artificial constraint of someone needing an available domain name, so unsurprisingly it is an illegal English word that is so instable it has already changed a consonant in spoken speech in only a few years.