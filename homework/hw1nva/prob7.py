#!/usr/bin/env python

'''Checks if two words rhyme.'''

__author__ = 'nvarnett'
__email__ = "nvarnett@ucsc.edu"
__credits__ = ["Karl", "Breanna"]

def doRhyme(w1, w2):
    """
    this function checks if two words rhyme by examining their IPA representations
    
    Args:
    w1: a word (string)
    w2: a word (string)
    
    Returns:
    a boolean, True if w1 and w2 rhyme, False if they do not

    Raises:
    Nothing

    """
    # put your dictionary here
    dictionary = {}
    dictionary['final'] = {'def': 'of or relating to the end or to boundaries.',
                           'pos': "n",
                           'stressSlyb': '1',
                           'sylb': {}}
    dictionary['file'] = {'def': 'A collection of papers collated/archived together.',
                          'pos': 'n',
                          'stressSylb': '1',
                          'sylb': {}}
    dictionary['laughed'] = {'def': 'simple past tense and past participle of laugh.',
                             'pos': 'v',
                             'stressSylb': '1',
                             'sylb': {}}
    dictionary['red'] = {'def': 'Having red as its color.',
                         'pos': 'a',
                         'stressSylb': '1',
                         'sylb': {}}
    dictionary['listen'] = {'def': 'To pay attention to a sound or speech.',
                            'pos': 'v',
                            'stressSylb': '1',
                            'sylb': {}}
    dictionary['vixen'] = {'def': 'A female fox.',
                           'pos': 'n',
                           'stressSylb': '1',
                           'sylb': {}}
    dictionary['table'] = {'def': 'An item of furniture with a flat top surface raised above the ground, usually on one or more legs.',
                           'pos': 'n',
                           'stressSylb': '1',
                           'sylb': {}}
    dictionary['label'] = {'def': 'A small ticket or sign giving information about something to which it is attached or intended to be attached.',
                           'pos': 'n',
                           'stressSylb': '1',
                           'sylb': {}}
    dictionary['through'] = {'def': 'From one side of an opening to the other.',
                             'pos': 'p',
                             'stressSylb': '1',
                             'sylb': {}}
    dictionary['rough'] = {'def': 'Having a texture that has much friction. Not smooth; uneven. ',
                           'pos': 'a',
                           'stressSylb': '1',
                           'sylb': {}}

    #We give our sylable keys nice names like '1' '2' and '3'.
    ##If we had more than 9 we would go '01' '02' '03'.
    ##This lets us sort our keys easier
    dictionary['final']['sylb']['1'] = { 'phonList' : ["f", "aɪ"],
                                         'nucIndex' : 1}
    dictionary['final']['sylb']['2'] = { 'phonList' : ["n", "ə", "l"],
                                         'nucIndex' : 1}
    dictionary['file']['sylb']['1'] = { 'phonList' : ["f", "aɪ", "l"],
                                        'nucIndex' : 1}
    dictionary['laughed']['sylb']['1'] = { 'phonList' : ["l", "æ", "f", "t"],
                                           'nucIndex' : 1}
    dictionary['red']['sylb']['1'] = { 'phonList' : ["ɹ", "ɛ", "d"], 'nucIndex' : 1}
    dictionary['listen']['sylb']['1'] = {'phonList' : ["l", "ɪ"], 'nucIndex' : 1}
    dictionary['listen']['sylb']['2'] = {'phonList' : ["s", "ə", "n"], 'nucIndex': 1}
    dictionary['vixen']['sylb']['1'] = { 'phonList' : ["v", "ɪ", "k"],
                                         'nucIndex' : 1}
    dictionary['vixen']['sylb']['2'] = { 'phonList' : ["s", "ɪ", "n"],
                                         'nucIndex' : 1}
    dictionary['table']['sylb']['1'] = { 'phonList' : ["t", "eɪ"],
                                         'nucIndex' : 1}
    dictionary['table']['sylb']['2'] = { 'phonList' : ["b", "ə", "l"],
                                         'nucIndex' : 1}
    dictionary['label']['sylb']['1'] = { 'phonList' : ["l", "eɪ"],
                                         'nucIndex' : 1}
    dictionary['label']['sylb']['2'] = { 'phonList' : ["b", "ə", "l"],
                                         'nucIndex' : 1}
    dictionary['through']['sylb']['1'] = { 'phonList' : ["θ", "r", "u"],
                                           'nucIndex' : 2}
    dictionary['rough']['sylb']['1'] = { 'phonList' : ["r", "ʌ", "f"],
                                         'nucIndex' : 1}
 # Look up the keys assosiated with the syllables of w1 and w2 in dict
    w1sylbs = dictionary[w1]['sylb'].keys()
    w2sylbs = dictionary[w2]['sylb'].keys() 
    print w1sylbs, w2sylbs

 # Since these keys have nice names '1', '2', '3' we can sort them and find the last sylable
    w1sylbs.sort()
    w2sylbs.sort()  
    w1lastSylb = w1sylbs[-1]
    w2lastSylb = w2sylbs[-1]
    print w1lastSylb, w2lastSylb
    
    
 #Look up the phonList and nucleus index of the last sylable from dict
    w1sylb = dictionary[w1]['sylb'][w1lastSylb]['phonList']
    w1nuc = dictionary[w1]['sylb'][w1lastSylb]['nucIndex']
    print w1sylb, w1nuc

    
    w2sylb = dictionary[w2]['sylb'][w2lastSylb]['phonList']
    w2nuc = dictionary[w2]['sylb'][w2lastSylb]['nucIndex']
    print w2sylb, w2nuc
    
#Last we compare them (literal equivalence)
    if w1sylb[w1nuc:] == w2sylb[w2nuc:]:
        return True 
    else: 
        return False

