#!/usr/bin/env python

__author__ = 'nvarnett'
__email__ = "nvarnett@ucsc.edu"
__credits__ = ["Karl", "Breanna"]


###this file contains dictionary entries for the words in HW parts 5 & 6.
## The first half are the syntactico-semantic into; THe second, the phonemic reps

dictionary = {}
dictionary['python'] = {'def': 'A type of large constricting snake.',
                        'pos': "n",
                        'stressSlyb': '1',
                        'sylb': {}}
dictionary['when'] = {'def': 'At an earlier and less prosperous time.',
                      'pos': 'adv',
                      'stressSylb': '1',
                      'sylb': {}}
dictionary['i'] = {'def': ' first person singular subject personal pronoun',
                   'pos': 'd',
                   'stressSylb': '1',
                   'sylb': {}}
dictionary['was'] = {'def': 'First-person sing simple past tense indicative of be.',
                     'pos': 'v',
                     'stressSylb': '1',
                     'sylb': {}}
dictionary['little'] = {'def': 'Small in size.',
                        'pos': 'a',
                        'stressSylb': '1',
                        'sylb': {}}
dictionary['thought'] = {'def': 'simple past tense and past participle of think',
                         'pos': 'v',
                         'stressSylb': '1',
                         'sylb': {}}
dictionary['a'] = {'def': 'One; any indefinite ex of; used to denote a singular item of a group.',
                   'pos': 'd',
                   'stressSylb': '1',
                   'sylb': {}}
dictionary['snake'] = {'def': 'A legless reptile of the sub-order Serpentes with a long, thin body and a fork-shaped tongue. ',
                       'pos': 'n',
                       'stressSylb': '1',
                       'sylb': {}}
dictionary['now'] = {'def': 'At the present time.',
                     'pos': 'adv',
                     'stressSylb': '1',
                     'sylb': {}}
dictionary['know'] = {'def': 'To be certain or sure about.',
                      'pos': 'v',
                      'stressSylb': '1',
                      'sylb': {}}
dictionary['it'] = {'def': 'The third-person singular personal pronoun used to refer to an inanimate object, to an inanimate thing with no or unknown sex or gender.',
                    'pos': 'd',
                    'stressSylb': '1',
                    'sylb': {}}
dictionary['is'] = {'def': 'third-person singular simple present indicative form of be',
                    'pos': 'v',
                    'stressSylb': '1',
                    'sylb': {}}
dictionary['really'] = {'def': 'Actually; in fact; in reality.',
                        'pos': 'deg',
                        'stressSylb': '1',
                        'sylb': {}}
dictionary['monster'] = {'def': 'A terrifying and dangerous, wild or fictional creature.',
                         'pos': 'n',
                         'stressSylb': '1',
                         'sylb': {}}
dictionary['in'] = {'def': 'Contained by.',
                    'pos': 'p',
                    'stressSylb': '1',
                    'sylb': {}}
dictionary['disguise'] = {'def': "Attire (e.g. clothing, makeup) used to hide one's identity or assume another.",
                          'pos': 'n',
                          'stressSylb': '2',
                          'sylb': {}}
dictionary['but'] = {'def': 'Without, apart from, except.',
                     'pos': 'c',
                     'stressSylb': '1',
                     'sylb': {}}
dictionary['will'] = {'def': 'Used to express the future tense, formerly with some implication of volition when used in first person.',
                      'pos': 'm',
                      'stressSylb': '1',
                      'sylb': {}}
dictionary['prevail'] = {'def': 'To be superior in strength, dominance, influence or frequency; to have or gain the advantage over others; to have the upper hand; to outnumber others.',
                         'pos': 'v',
                         'stressSylb': '2',
                         'sylb': {}}
dictionary['over'] = {'def': 'Again; another time; once more; over again.',
                      'pos': 'p',
                      'stressSylb': '1',
                      'sylb': {}}
dictionary['this'] = {'def': 'The (thing) here',
                      'pos': 'd',
                      'stressSylb': '1',
                      'sylb': {}}
dictionary['hideous'] = {'def': 'Frightful; shocking; extremely ugly.',
                         'pos': 'a',
                         'stressSylb': '1',
                         'sylb': {}}
dictionary['beast'] = {'def': 'Any animal other than a human; usually only applied to land vertebrates, especially large or dangerous four-footed ones.',
                       'pos': 'n',
                       'stressSylb': '1',
                       'sylb': {}}

###PHONEMIC REPRESENTATIONS
dictionary['when']['sylb']['1'] = { 'phonList' : ["w", "ɛ", "n"],
                                    'nucIndex' : 1}
dictionary['I']['sylb']['1'] = { 'phonList' : ["aɪ"],
                                 'nucIndex' : 0}	
dictionary['was']['sylb']['1'] = { 'phonList' : ["w", "ʌ", "z"],
                                   'nucIndex' : 1}
dictionary['little']['sylb']['1'] = { 'phonList' : ["l", "ɪ"],
                                      'nucIndex' : 1}
dictionary['little']['sylb']['2'] = { 'phonList' : ["ɾ", "ə", "l"],
                                      'nucIndex' : 1}
dictionary['thought']['sylb']['1'] = { 'phonList' : ["θ", "ɔ", "t"],
                                       'nucIndex' : 1}
dictionary['a']['sylb']['1'] = { 'phonList' : ["eɪ"],
                                 'nucIndex' : 0}
dictionary['python']['sylb']['1'] = { 'phonList' : ["p", "aɪ"],
                                      'nucIndex' : 1}
dictionary['python']['sylb']['2'] = { 'phonList' : ["θ", "ɑ:", "n"],
                                      'nucIndex' : 1}
dictionary['snake']['sylb']['1'] = { 'phonList' : ["s", "n", "eɪ", "k"],
                                     'nucIndex' : 2}
dictionary['now']['sylb']['1'] = { 'phonList' : ["n", "aʊ"],
                                   'nucIndex' : 1}
dictionary['know']['sylb']['1'] = { 'phonList' : ["n", "oʊ"],
                                    'nucIndex' : 1}
dictionary['it']['sylb']['1'] = { 'phonList' : ["ɪ", "t"],
                                  'nucIndex' : 0}
dictionary['is']['sylb']['1'] = { 'phonList' : ["ɪ", "z"],
                                  'nucIndex' : 0}
dictionary['really']['sylb']['1'] = { 'phonList' : ["r", "ɪ"],
                                      'nucIndex' : 1}
dictionary['really']['sylb']['2'] = { 'phonList' : ["l", "i"],
                                      'nucIndex' : 1}
dictionary['a']['sylb']['1'] = { 'phonList' : ["ə"],
                                 'nucIndex' : 0}
dictionary['monster']['sylb']['1'] = { 'phonList' : ["m", "a", "n"],
                                       'nucIndex' : 1}
dictionary['monster']['sylb']['2'] = { 'phonList' : ["s", "t", "ə", "ɹ"],
                                       'nucIndex' : 2}
dictionary['in']['sylb']['1'] = { 'phonList' : ["ɪ", "n"],
                                  'nucIndex' : 0}
dictionary['disguise']['sylb']['1'] = { 'phonList' : ["d", "ɪ", "s"],
                                        'nucIndex' : 1}
dictionary['disguise']['sylb']['2'] = { 'phonList' : ["g", "aɪ", "z"],
                                        'nucIndex' : 1}
dictionary['but']['sylb']['1'] = { 'phonList' : ["b", "ʌ", "t"],
                                   'nucIndex' : 1}
dictionary['will']['sylb']['1'] = { 'phonList' : ["w", "ɪ", "l"],
                                    'nucIndex' : 1}
dictionary['prevail']['sylb']['1'] = { 'phonList' : ["p", "r", "ɪ"],
                                       'nucIndex' : 2}
dictionary['prevail']['sylb']['1'] = { 'phonList' : ["v", "eɪ", "l"],
                                       'nucIndex' : 1}
dictionary['over']['sylb']['1'] = { 'phonList' : ["oʊ"],
                                    'nucIndex' : 0}
dictionary['over']['sylb']['2'] = { 'phonList' : ["v", "ə", "r"],
                                    'nucIndex' : 1}
dictionary['this']['sylb']['1'] = { 'phonList' : ["ð", "ɪ", "s"],
                                    'nucIndex' : 1}
dictionary['hideous']['sylb']['1'] = { 'phonList' : ["h", "ɪ"],
                                       'nucIndex' : 1}
dictionary['hideous']['sylb']['2'] = { 'phonList' : ["d", "i"],
                                       'nucIndex' : 0}
dictionary['beast']['sylb']['1'] = { 'phonList' : ["b", "i", "s", "t"],
                                     'nucIndex' : 1}
dictionary['hideous']['sylb']['3'] = { 'phonList' : ["ə", "s"],
                                       'nucIndex' : 1}