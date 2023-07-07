# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
import re
def check_aei(text):
    """ Returns bol for presence of aei"""
    result = re.search(r"a.e.i", text, re.IGNORECASE)
    return result != None

print(check_aei("academia")) # True
print(check_aei('aerial')) # False
print(check_aei('paramedic')) # True
print()


# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

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


# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 

def repeating_letter_a(text):
   result = re.search(r"[Aa]+.*a+", text)
   return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
print()


# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

import re
def check_character_groups(text):
  result = re.search(r"\d.*", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
print()



# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-zA-Z ]*[\.\?\!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
print()

