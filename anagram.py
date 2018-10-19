from random import randint
from itertools import permutations
import json


'''
To solve for cases of duplicate letters
'''
def is_capitalized(word):
    return reduce(lambda x, y: x & y, map(lambda x : x.isupper(), word))
def anagram_1(string, dictionary):
    '''Create a table listing all the letters and form words that way'''
    alphabetical = ''.join(sorted(string))
    to_dict = [char for char in alphabetical]
    words = []
    '''Going off the base assumption that a word is 2 or more letters'''
    for i in range(2, len(string)):
        targets = map(lambda x : ''.join(x), set(permutations(''.join(to_dict),i)))
        words.extend(targets)
    return filter(lambda word : word in dictionary, words)

def anagram(string):
    with open('dictionary.json') as f:
        dictionary = json.load(f)
    return anagram_1(string,dictionary)

print(anagram("sort"))

