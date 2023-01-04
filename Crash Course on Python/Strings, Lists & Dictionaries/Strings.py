# STRINGS, LISTS & DICTIONARIES. 

# ___STRINGS___

# _What is a String?_ - A string is a data type in python that is used to represent a piece of text. 
name = 'sasha'
color = 'gold'
place = "Cambridge"
print('Name: '+ name + " Color: " + ' Place: ' + place) # Concatenating
print()

# _The parts of a String_
# String Indexing
name = 'Jaylen'
print(name[1])
print(name[0])
print(name[5])
print(name[-1]) # Outputs the last character (r).
print(name[-2]) # Outputs the second to the last character. 
print()
# String Slice 
# The portion of a string that can contain more than one character' also sometimes called a substring.
colour = 'Orange'
print(colour[1:4])
fruit = 'Pineapple'
print(fruit[:4])
print(fruit[4:])
print()
# String Indexing and Slicing - String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index [-1] would access the last character of the string, and the index [-2] would access the second-to-last character. You can also access a portion of a string, called a slice or a substring. This allows you to access multiple characters of a string. You can do this by creating a range, using a colon as a separator between the start and end of the range, like [2:5].  This range is similar to the range() function we saw previously. It includes the first number, but goes to one less than the last number. For example:
# >>> fruit = "Mangosteen"
# >>> fruit[1:4]
# 'ang'
# The slice includes the character at index 1, and excludes the character at index 4. You can also easily reference a substring at the start or end of the string by only specifying one end of the range. For example, only giving the end of the range:
# >>> fruit[:5]
# 'Mango'
# This gave us the characters from the start of the string through index 4, excluding index 5. On the other hand this example gives is the characters including index 5, through the end of the string:
# >>> fruit[5:]
# 'steen'
# You might have noticed that if you put both of those results together, you get the original string back!
#>>> fruit[:5] + fruit[5:]
# 'Mangosteen'
# Cool!

# _Creating New Strings_
# N.B: Strings in python are immmutabe, hence, we use concatenation.
message = 'A kong string with a silly typo'
new_message = message[0:2] + 'l' + message[3:-1]
print(new_message)
message = 'Never be meam'
print(message)
message = 'To be continued!'
print(message)
print()
# Method - A method is a function associated with a specific class. 
pets = 'Cats & Dogs'
position = pets.index('&')
print(position) # 5
position = pets.index('C')
print(position) # 0
position = pets.index('Dog')
print(position) # 7
position = pets.index('s')
print(position) # 3
print()
# >>>>
test = "Dragons" in pets
print(test)
test = 'Cats' in pets
print(test)

# Drill
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email
newEmailAddress = replace_domain('david@gmail.com', 'gmail.com', 'morgan.edu')
print(newEmailAddress)
print()

# Basic String Methods - In Python, strings are immutable. This means that they can't be modified. So if we wanted to fix a typo in a string, we can't simply modify the wrong character. We would have to create a new string with the typo corrected. We can also assign a new value to the variable holding our string. If we aren't sure what the index of our typo is, we can use the string method index to locate it and return the index. Let's imagine we have the string "lions tigers and bears" in the variable animals. We can locate the index that contains the letter g using animals.index("g"), which will return the index; in this case 8. We can also use substrings to locate the index where the substring begins. animals.index("bears") would return 17, since that’s the start of the substring. If there’s more than one match for a substring, the index method will return the first match. If we try to locate a substring that doesn't exist in the string, we’ll receive a ValueError explaining that the substring was not found. We can avoid a ValueError by first checking if the substring exists in the string. This can be done using the in keyword. We saw this keyword earlier when we covered for loops. In this case, it's a conditional that will be either True or False. If the substring is found in the string, it will be True. If the substring is not found in the string, it will be False. Using our previous variable animals, we can do "horses" in animals to check if the substring "horses" is found in our variable. In this case, it would evaluate to False, since horses aren’t included in our example string. If we did "tigers" in animals, we'd get True, since this substring is contained in our string.
capital = 'Mountains'.upper()
print(capital)
small = 'Mountains'.lower()
print(small)
print()
# >>>
answer = input('Tall?? Yes/NO: ')
if answer.lower() == 'yes':
    print("User said " + answer + " (^_^)")
elif answer.lower() == 'no':
    print("User said " + answer + " (^_^)")
else:
    print("'" + answer + "'" + ' is not a valid response.')
print()    
# >>>>>
remove = ' Yes '
print(remove)
print(remove.strip())   # Removes all white spaces.
print(remove.lstrip())  # Removes spaces on the left side of the string.
print(remove.rstrip())  # Removes spaces on the left side of the string.
print()
# >>>> 
sentence = 'I am a Systems Engineering Student at University of Lagos.'
print(sentence.count("e"))
print()
# >>>>
word = "Forest"
print(word.endswith('rest'))    # Returns whether a string ends with the passed in value.
print(word.isnumeric())     # Retuns whether a string is numeric
sum = int("12345") + int("54321") # Returns the sum of two numeric strings
print(sum) 
print()
# >>>>>
roll = " ".join(['This', 'is', 'my', 'son'])    # Joins the passed in list with the passed in joiner to give a whole string.
print(roll)
phrase = 'Wasted as trash'      # # Splits up the passed in list to give a whole string.
print(phrase.split())

# Advanced String Methods - We've covered a bunch of String class methods already, so let's keep building on those and run down some more advanced methods. The string method lower will return the string with all characters changed to lowercase. The inverse of this is the upper method, which will return the string all in uppercase. Just like with previous methods, we call these on a string using dot notation, like "this is a string".upper(). This would return the string "THIS IS A STRING". This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases. You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively. The method count can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph. If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.
# The isnumeric method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful! We took a look at string concatenation using the plus sign, earlier. We can also use the join method to concatenate strings. This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using the initial string. For example, " ".join(["This","is","a","sentence"]) would return the string "This is a sentence". The inverse of the join method is the split method. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.

# _Formatting Strings_
name = "Manny"
number = len(name) * 3
print('Hello {}, your lucky number is {}'.format(name, number))
print('Your lucky number is {number}, {name}'.format(name = 'David' , number = len(name)*3))
# >>>
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print('Base price: ${:.2f}, With Tax: ${:.2f}'.format(price, with_tax))
# >>>>>
def to_celsius(x):
    return (x - 32) * 5/9
for x in range(0, 101, 10):
    print('{:>3} F | {:>10.2f} C'.format(x, to_celsius(x)))

# String Formatting - You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us. If the curly brackets are empty, they’ll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables. You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.
# String Reference Cheat Sheet
# String Reference Cheat Sheet
# In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.
# String operations
# - len(string) Returns the length of the string
# - for character in string Iterates over each character in the string
# - if substring in string Checks whether the substring is part of the string
# - string[i] Accesses the character at index i of the string, starting at zero
# - string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.
# String methods
# - string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
# - string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
# - string.count(substring) Returns the number of times substring is present in the string
# - string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
# - string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
# - string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
# - string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
# - delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
# - Check out the official documentation for all available String methods.  



# _Practice Quiz_

# 1. The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for i in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if i != " ":
			new_string = new_string + i.lower()
			reverse_string = i + reverse_string.lower()
	# Compare the strings
	if new_string == reverse_string:
		return True 
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
print()

# 2. Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
print()

# 3. Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."
def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
print()

# 4. The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(old)
		new_sentence = sentence[:-i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"



