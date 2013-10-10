#!/usr/bin/env python

'''Creates a PigLatin generator.'''

__author__ = 'nathanArnett'
__email__ = "nvarnett@ucsc.edu"
__credits__ = ["Breanna", "Karl"]

def pigLatin(w):
    """
	this function handles pigLatin for word w

    Args:
		w: a word

    Returns:
        pigLatined: a PigLatin representation of word w

    Raises:
        Nothing

	"""
    ##Maybe not necessary, as it's overwritten, but initialize word vector
    pigLatined = w #not what you'll do, but it will allow us to run the test

    ##Check for traps: single charater words are simply passed + "ay"
    if len(w) == 1:
     return w + "ay"
    
    ##List the vowels; for each w, check for occurence & take lowest n
    vowels = "aeiou"
    vList = [w.find(x) for x in vowels if x in w]
    vPlace = min(vList)
    
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
    pigLatined = ret + "ay"
      
    return pigLatined

def pigLatinParts(text):
    """
	this function handles pigLatin for all words in string S. It also remembers the punctuation as at the last Goedel number.

    Args:
		text: a string

    Returns:
        pigLatined: what people can download and use (a program)
        
    Raises:
        Nothing

	"""

    # my suggestion: break this into a few parts:
    # 1) break up the text into tokens
    # 2) run a for loop over each token where you get the pigLatined version of that
    #      for (2), you'll need to call pigLatin on that token
    # 3) put it all together to make one piece of text
    #      for that, you can use another for loop and + (just keep adding to the string you are going to return
    #      OR you can use a function called join []; see the note below 

    ##Split the string into tokens
    strings = text.split()
    punct = ".,:;'?!"
    ##For each token, call pigLatin() & return result
    # text = []
    # for i in strings:
    #  if i[-1] in punct:
    #   x = pigLatin(i[:-1]) + i[-1]
    #   text.append(x)
    #  else:
    #   x = pigLatin(i)
    #   text.append(x)
    strings = [i[-1] in punct and (pigLatin(i[:-1]) + i[-1]) or pigLatin(i) for i in strings]
     
    ##Flatten the word bag back into a string
    ##For each word, append to newString
    

    
    return " ".join(strings) #not what you want to do here, but this in the business of running.

if __name__ == "__main__":
    
    # all of the below code is used to TEST whether yours worked
    
    inputLine = "if you think, sadly, that he will actually visit, then I am fine."
    key = "ifway ouyay inkthay, adlysay, atthay ehay illway actuallyay isitvay, enthay I amay inefay." 
    pg = pigLatinParts(inputLine)
    if pg ==key:
        result = "PASS"
    else:
        result = "FAIL"
    print inputLine
    print pg
    print result