#!/usr/bin/env python

'''Creates a PigLatin generator.'''

__author__ = 'nathanArnett'
__email__ = "nvarnett@ucsc.edu"
__credits__ = ["Breanna", "Karl"]

def pigLatin(w, d):
    """
	this function handles pigLatin for word w, for dialect d

    Args:
		w: a word
        d: a dialect (as a string)

    Returns:
        pigLatined: a PigLatin representation of word w

    Raises:
        Nothing

	"""
    
    ##Maybe not necessary, as it's overwritten, but initialize word vector
    pigLatined = w #not what you'll do, but it will allow us to run the test
    #d = ["way", "yay", "ay"]
    ##List the vowels; for each w, check for occurence & take lowest n
    vowels = "aeiou"
    vList = [w.find(x) for x in vowels if x in w]
    vPlace = min(vList)

    ##Check for traps (numbers, word final "e")
    if not w.isalpha():
     return w

    if w[0] in vowels and w[-1] in vowels:
     w = w[:-1]
     ## if v loc is non-empty, store the location; Else store -1
    if vPlace != []:
     ret = vPlace
    else:
     ret = -1

    ##Return w for V-initial w, else strip off initital C, append word-finally
    if vPlace == "-1":
        ret = w
    else:
        onset = w[:vPlace]
        ret = w[vPlace:] + onset

    if onset != "":
     ending = d[1:]
    else:
     ending = d
        
    
    pigLatined = ret + ending
      
    return pigLatined

if __name__ == "__main__":
    
    # all of the below code is used to TEST whether yours worked
    # a list of test word -> pg examples, as a dict
    wordsToPigLatin = {"artichoke": ("artichokyay", "yay"), 
                       "stipple": ("ipplestay", "way"),
                       "123re": ("123re", "ay"),
                       "soup": ("oupsay", "way")}
    
    # per word, get the pg, the expected answer, and print success
    for word in wordsToPigLatin:
        ans, dialect = wordsToPigLatin[word]
        pg = pigLatin(word, dialect)
        if pg == ans:
            result = "PASS"
        else:
            result = "FAIL"
        print word, pg, result