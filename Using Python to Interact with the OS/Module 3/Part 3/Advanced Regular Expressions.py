''' CAPTURING GROUPS '''

import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result) # <re.Match object; span=(0, 13), match='Lovelace, Ada'>
print(result.groups()) # ('Lovelace', 'Ada')
print(result[0]) # Lovelace, Ada
print(result[1]) # Lovelace
print(result[2]) # Ada
print("{} {}".format(result[2], result[1])) # 'Ada Lovelace'
print()


def rearrange_name(name):
   result = re.search(r"^(\w*), (\w*)$", name)
   if result is None:
           return name
   return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada") # 'Ada Lovelace'
rearrange_name("Ritchie, Dennis") # 'Dennis Ritchie'
rearrange_name("Hopper, Grace M.") # 'Hopper, Grace M.'
print()


def rearrange_name(name):
   result = re.search(r"^(\w*), (\w*) (\w\.)$", name)
   if result is None:
           return name
   return "{} {} {}".format(result[2], result[3], result[1])
...
rearrange_name("Hopper, Grace M.") # 'Grace M. Hopper'
print()




''' MORE ON REPITION QUALIFIERS '''

print(re.search(r"[a-zA-Z]{5}", "a ghost")) # <re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) # <re.Match object; span=(2, 7), match='scary'>
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # ['scary', 'ghost', 'appea']

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeard")) # ['scary', 'ghost']
print(re.findall(r"\w{5,10}", "I really like strawberries")) # ['really', 'strawberri']
print(re.findall(r"\w{5,}", "I really like strawberries")) # ['really', 'strawberries']
print(re.search(r"\w{,20}", "I really like strawberries")) # <re.Match object; span=(0, 1), match='I'>
print(re.search(r"s\w{,20}", "I really like strawberries")) # <re.Match object; span=(14, 26), match='strawberries'>


def long_words(text):
   pattern = r"\w{7,}"
   result = re.findall(pattern, text)
   return result
...
print(long_words("I like to drint coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []




''' EXRACTING A PID USING REGEXES IN PYTHON '''


def extract_pid(log_line):
   regex = r"\[(\d+)\]"
   result = re.search(regex, log_line)
   if result is None:
           return ""
   return result[1]
...
print(extract_pid("gg elephants in a [cape]"))

import re
def extract_pid(log_line):
   regex = r"\[(\d+)\]\: ([A-Z]*)"
   result = re.search(regex, log_line)
   if result is None:
       return None
   return "{} ({})".format(result[1], result[2])
...
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)



''' SPLITTING AND REPLACING '''

re.split(r"[.?!]", "One sentence. Another one? And the last one!")
['One sentence', ' Another one', ' And the last one', '']
re.split(r"([.?!])", "One sentence. Another one? And the last one!")
['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
'Received an email for [REDACTED]'

re.sub(r"^([\w.-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
'Ada Lovelace'
