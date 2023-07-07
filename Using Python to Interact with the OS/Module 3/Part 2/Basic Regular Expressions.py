''' SIMPLE MATCHING IN PYTHON'''

import re
result = re.search('aza', 'plaza')
print(result)
print()

print(re.search(r"^x", "xenon"))
print()

print(re.search(r"p.ng", "PingPong", re.IGNORECASE))
print()


'''WILDCARDS AND CHARACTER CLASSES'''


print(re.search(r"[Pp]ython", "Python")) # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"[a-z]way", "highway")) # <re.Match object; span=(3, 7), match='hway'>
print(re.search(r"[a-z]way", "what a way")) # None
print(re.search("cloud[a-zA-Z0-9]", "cloudy")) # <re.Match object; span=(0, 6), match='cloudy'>
print(re.search("cloud[a-zA-Z0-9]", "cloudy")) # <re.Match object; span=(0, 6), match='cloudy'>


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



''' ESCAPING CHARACTERS '''

import re
print(re.search(r".com", "welcome")) # <re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com", "welcome")) # None
print(re.search(r"\.com", "mydomain.com")) # <re.Match object; span=(8, 12), match='.com'>
print(re.search(r"\w*", "This is an example")) # <re.Match object; span=(0, 4), match='This'>
print(re.search(r"\w*", "And_this_is_another.")) # <re.Match object; span=(0, 19), match='And_this_is_another'>
print(re.search(r"\d", "Phone: 08023234002")) # <re.Match object; span=(7, 8), match='0'>
print(re.search(r"\d*", "Phone: 8023234002")) # <re.Match object; span=(0, 0), match=''>
print(re.search(r"\d\d\d\d\d\d\d\d\d", "Phone: 8023234002")) # <re.Match object; span=(7, 16), match='802323400'>
print(re.search(r"\d\d\d\d\d\d\d\d\d\d", "Phone: 8023234002")) # <re.Match object; span=(7, 17), match='8023234002'>
print(re.search(r"\s", "Phone: 8023234002")) # <re.Match object; span=(6, 7), match=' '>
print(re.search(r"\d.*", "Phone:8023234002")) # <re.Match object; span=(6, 16), match='8023234002'>
print((re.search(r"\d.*", "Phone:8023234002"))[0]) # 8023234002
print((re.search(r"\s.*", "Phone:    8023234002"))) # <re.Match object; span=(6, 18), match='\t 8023234002'>
print((re.search(r"\b.*", "Phone:    8023234002"))) # <re.Match object; span=(0, 18), match='Phone:\t 8023234002'>
print((re.search(r"\b.*", "Test this"))) # <re.Match object; span=(0, 9), match='Test this'>
print()




''' REGULAR EXPRESSIONS IN ACTION '''

print(re.search(r"A.*a", "Argentina")) # <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"A.*a", "Azerbaija")) # <re.Match object; span=(0, 9), match='Azerbaija'>
print(re.search(r"A.*a", "Azerbaijan")) # <re.Match object; span=(0, 9), match='Azerbaija'>
print(re.search(r"A.*a$", "Azerbaijan")) # None
print(re.search(r"A.*a$", "Australia")) # <re.Match object; span=(0, 9), match='Australia'>
print()

pattern = r"^[A-Za-z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name")) # <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
print(re.search(pattern, "this isn't a valid variable name")) # None
print(re.search(pattern, "vaiable1")) # <re.Match object; span=(0, 8), match='vaiable1'>
print()