#!/usr/bin/env python

'''Creates a phonemic PigLatin generator.'''

__author__ = 'nvarnett'
__email__ = "nvarnett@ucsc.edu"
__credits__ = ["Karl", "Brianna"]

def pigLatin(w):
 """
	this function handles pigLatin for word w

 Args:
		w: an orthographic word

 Returns:
 pigLatined: a PigLatin representation of word w

 Raises:
 Nothing

	"""
	    
 dictionary = {}
 dictionary['python'] = {'def': 'A type of large constricting snake.', 'pos': "n", 'stressSlyb' : '1', 'sylb' : {}}
 #We give our sylable keys nice names like '1' '2' and '3'. If we had more than 9 we would go '01' '02' '03'. This lets us sort our keys easier
 dictionary['python']['sylb']['1'] = { 'phonList' : ["p", "aI"], 'nucIndex' : 1}
 dictionary['python']['sylb']['2'] = { 'phonList' : ["θ","ɑː","n"], 'nucIndex' : 1}

 ###Grab the phonemic representation of a word
 ##We exploit the nice, orderable names of our keys to get a sorted list of syllables
 sylblist = dictionary[w]['sylb'].keys()
 sylblist.sort()
 
 ##IF the first phoneme of the first sylable is a vowel... 
 if dictionary[w]['sylb'][sylblist[0]]['nucIndex'] == 0:
 ##THEN flatten the word into a list of phonemes and add "ej" to the end.
     myword = []
     for i in sylblist:   
         myword.extend(dictionary[w]['sylb'][i]['phonList'])    
     myword.append("ej")    
 else: 
 ##Find the nucleus of the first syllable, initialize a word vector 
     firstnuc = dictionary[w]['sylb'][sylblist[0]]['nucIndex']
 
     firstSylbNoOns = []
     firstSylbNoOns.extend(dictionary[w]['sylb'][sylblist[0]]['phonList'][firstnuc:])
     myword = firstSylbNoOns

     ##Loop through each non-initial segment in the word, add to the word list
     for i in sylblist[1:]:   
         myword.extend(dictionary[w]['sylb'][i]['phonList'])    
            
         
     firstOns = dictionary[w]['sylb'][sylblist[0]]['phonList'][:firstnuc]

     ##Add the word-initial onset + "ej" to the end of the word
     myword.extend(firstOns)
     myword.append("ej")
 ##Join the re-ordered segments into a single string    
 pigLatined = "".join(myword)
            
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
 
 return " ".join([i[-1] in ".,':;!?()" and (pigLatin(i[:-1]) + i[-1]) or pigLatin(i) for i in text.split()])

if __name__ == "__main__":
 
 # all of the below code is used to TEST whether yours worked
 
 inputLine = "if you think, sadly, that he will actually visit, then I am fine."
 
 # I think this is right. Someone tell me if I'm wrong; there are
 # clearly some glide epentheses and ambisyllabicity issues
 # I'm avoiding here.
 
 key = "ɪfej uyej ɪŋkθej, ædlijsej, ætðej ihej ɪlwej æktʃəliej ɪzɪtvej, ɛnðej I æmej aɪnfej." 
 pg = pigLatinParts("python, python, python")
 if pg ==key:
     result = "PASS"
 else:
     result = "FAIL"
 print inputLine
 print pg
 print key
 print result
