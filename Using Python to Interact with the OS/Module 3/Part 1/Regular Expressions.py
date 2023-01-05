''' Lesson 1 - Why use regular expression? '''

import re
log = "July 31 07:51:48 mycomputer bad-process[12345]: Error performing package upgrade. [419]"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


''' Lesson 2 - Basic Matching with grep. '''
# Linux
'''
grep thon "words.txt" - Interates through all the words(lines) in the text file and prints the word that have 'thon' in them.

grep -i thon "words.txt" - to remove case-sensitivity \

grep p.ck "words.txt" - Anchor character (.) represents any single character

grep ^cat "words.txt" - search for all words that start with cat.

grep cat$ "words.txt" - to search for all words that end with cat. 

'''

# Windows
'''
findstr thon "words.txt" - Interates through all the words(lines) in the text file and prints the word that have 'thon' in them.

findstr -i thon "words.txt" - to remove case-sensitivity \

findstr p.ck "words.txt" - Anchor character (.) represents any single character

findstr ^cat "words.txt" - search for all words that start with cat.

findsrt cat$ "words.txt" - to search for all words that end with cat. 

'''