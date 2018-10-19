from random import randint
from itertools import permutations
import json


'''
To solve for cases of duplicate letters
'''
wordlist =[]
with open('wordlist.txt') as contents:
    for line in contents:
        wordlist.append(line)
def anagram_1(string, dictionary, size_of_words):

    '''Create a table listing all the letters and form words that way'''
    alphabetical = ''.join(sorted(string))
    to_dict = [char for char in alphabetical]
    words = []
    if(size_of_words  < 2 or size_of_words > len(string)):
        raise("Error! Can't be this small")
    '''Going off the base assumption that a word is 2 or more letters'''
    for i in range(2, size_of_words+1):
        targets = map(lambda x : ''.join(x), set(permutations(''.join(to_dict),i)))
        words.extend(targets)
    return filter(lambda word : word in dictionary and wordlist, words)

def anagram(string):
    with open('dictionary.json') as f:
        dictionary = json.load(f).keys()
        dictionary = map(lambda char : char.encode('ascii', 'ignore').lower(), dictionary)
    return anagram_1(string,dictionary, 5)

print(anagram("knits"))

