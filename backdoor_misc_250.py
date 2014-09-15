import itertools
import string
 
hex_chars = '0123456789abcdef'
 
wordlist = open('wordlist', 'a')
 
for words in itertools.product(hex_chars, repeat=5):
    wordlist.write(''.join(words) + '007' + '\n'
