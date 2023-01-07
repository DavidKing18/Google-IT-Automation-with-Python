''' SIMPLE MATCHING IN PYTHON'''

import re
result = re.search('aza', 'plaza')
print(result)
print()

print(re.search(r"^x", "xenon"))
print()

print(re.search(r"p.ng", "PingPong", re.IGNORECASE))
print()

def check_aei(text):
    """ Returns bol for presence of aei"""
    result = re.search(r"a.e.i", text, re.IGNORECASE)
    return result != None

print(check_aei("academia")) # True
print(check_aei('aerial')) # False
print(check_aei('paramedic')) # True
print("\n\n")



'''WILDCARDS AND CHARACTER CLASSES'''


print(re.search(r"[Pp]ython", "Python")) # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"[a-z]way", "highway")) # <re.Match object; span=(3, 7), match='hway'>
print(re.search(r"[a-z]way", "what a way")) # None
print(re.search("cloud[a-zA-Z0-9]", "cloudy")) # <re.Match object; span=(0, 6), match='cloudy'>
print(re.search("cloud[a-zA-Z0-9]", "cloudy")) # <re.Match object; span=(0, 6), match='cloudy'>


def check_punctuation(text):
    """ Returns bol for presence of punctuation"""
    result = re.search(r"[,.?']", text)
    return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence that ends with a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
print()

print(re.search(r"[a-zA-Z]", "This is a sentence with spaces.")) # <re.Match object; span=(0, 1), match='T'>
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) # <re.Match object; span=(4, 5), match=' '>
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) # <re.Match object; span=(30, 31), match='.'>
print()

print(re.search(r"cat|dog", "I like cats.")) # <re.Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I like dogs.")) # <re.Match object; span=(7, 10), match='dog'>
print(re.search(r"cat|dog", "I like both dogs and cats.")) # <re.Match object; span=(12, 15), match='dog'>
print(re.findall(r"cat|dog", "I like both dogs and cats.")) # ['dog', 'cat']
print("\n\n")



''' REPTITION QUALIFIERS '''
print(re.search(r"Py.*n", "Pygnamlion")) # <re.Match object; span=(0, 10), match='Pygnamlion'>
print(re.search(r"Py.*n", "Pygamlion")) # <re.Match object; span=(0, 9), match='Pygamlion'>
print(re.search(r"Py.*n", "Python Programming")) # <re.Match object; span=(0, 17), match='Python Programmin'>
print(re.search(r"Py[a-z]*n", "Python Programming")) # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"Py[a-z]*n", "Pyn")) # <re.Match object; span=(0, 3), match='Pyn'>
print()

print(re.search(r"o+l+", "cold")) # <re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly")) # <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", "boil")) # None
print(re.search(r"p?each", "To each their own.")) # <re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "I like peaches")) # <re.Match object; span=(7, 12), match='peach'>
print(re.search(r"[Pp]each", "I like peaches")) # <re.Match object; span=(7, 12), match='peach'>
print(re.search(r"[Pp]each", "To each their own")) # None
print()


def repeating_letter_a(text):
   result = re.search(r"[Aa]+.*a+", text)
   return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False

print(repeating_letter_a("Animal Kingdom")) # True

print(repeating_letter_a("A is for apple")) # True


