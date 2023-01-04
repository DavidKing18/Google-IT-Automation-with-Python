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
    print('{:>3} F | {:>6.2f} C'.format(x, to_celsius(x)))

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












# ___LISTS___


# _What is a list?_
x = ['Now', 'we', 'are', 'cooking']
print(type(x))
print(x)
print(len(x))
check = 'are' in x
print(check, x[0], x[3], x[1:3])
print()

# _In-class Practice_
# Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
print()
# Lists Defined >>
# Lists in Python are defined using square brackets, with the elements stored in the list separated by commas: list = ["This", "is", "a", "list"]. You can use the len() function to return the number of elements in a list: len(list) would return 4. You can also use the in keyword to check if a list contains a certain element. If the element is present, it will return a True boolean. If the element is not found in the list, it will return False. For example, "This" in list would return True in our example. Similar to strings, lists can also use indexing to access specific elements in a list based on their position. You can access the first element in a list by doing list[0], which would allow you to access the string "This".
# In Python, lists and strings are quite similar. They’re both examples of sequences of data. Sequences have similar properties, like (1) being able to iterate over them using for loops; (2) support indexing; (3) using the len function to find the length of the sequence; (4) using the plus operator + in order to concatenate; and (5) using the in keyword to check if the sequence contains a value. Understanding these concepts allows you to apply them to other sequence types as well.



# _Modifying the Contents of a List_

fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append('Kiwl')
print(fruits)

fruits.insert(0, 'Orange')
print(fruits)

fruits.insert(25, 'Peach')
print(fruits)

fruits.remove('Melon')
print(fruits)

fruits.pop(3)
print(fruits) 

fruits[2] = 'Strawberry'
print(fruits)

# In-class Practice
# The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that, using the for loop to iterate through the input list.
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0
 
	# Iterate through the list
	for element in elements:
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(element)
		# Increment i
		i += 1
	return new_list
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# Modifying Lists
# While lists and strings are both sequences, a big difference between them is that lists are mutable. This means that the contents of the list can be changed, unlike strings, which are immutable. You can add, remove, or modify elements in a list. You can add elements to the end of a list using the append method. You call this method on a list using dot notation, and pass in the element to be added as a parameter. For example, list.append("New data") would add the string "New data" to the end of the list called list. If you want to add an element to a list in a specific position, you can use the method insert. The method takes two parameters: the first specifies the index in the list, and the second is the element to be added to the list. So list.insert(0, "New data") would add the string "New data" to the front of the list. This wouldn't overwrite the existing element at the start of the list. It would just shift all the other elements by one. If you specify an index that’s larger than the length of the list, the element will simply be added to the end of the list.
# You can remove elements from the list using the remove method. This method takes an element as a parameter, and removes the first occurrence of the element. If the element isn’t found in the list, you’ll get a ValueError error explaining that the element was not found in the list.
# You can also remove elements from a list using the pop method. This method differs from the remove method in that it takes an index as a parameter, and returns the element that was removed. This can be useful if you don't know what the value is, but you know where it’s located. This can also be useful when you need to access the data and also want to remove it from the list. Finally, you can change an element in a list by using indexing to overwrite the value stored at the specified index. For example, you can enter list[0] = "Old data" to overwrite the first element in a list with the new string "Old data".



# _Lists & Tuples
# NB: Strings are sequences of characters, and are immutable.
#     Lists are sequences of elements of any type that are mutable. 
#     Tuples are sequences of elements of any type that are immutable. 

fullname = ('Grace', 'M', 'Hopper') # Positions inside tuples have meaning.
print(fullname)
firstname, initial, lastname = fullname # Unpacking
print(firstname, initial, lastname)

# In-class Practice 
# Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 
def file_size(file_info):
	Name, Type, Size= file_info
	return("{:.2f}".format(Size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
print()
# Tuples - As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses instead of square brackets.
# You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.


 
# _Iterating over Lists and Tuples_
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
  chars += len(animal)

print('Total characters: {}, Aveerage length: {}'.format(chars, chars/len(animals))) # Should be 'Total characters: 22, Average length: 5.5
# Enumerate Function >>
winners = ['Ashley', 'Dylan', 'Reese']
for index, name in enumerate(winners):
  print('{} - {}'.format(index + 1, name))

# In-class Practice
# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.
def skip_elements(elements):
	# code goes here
	list = []
	for index, character in enumerate(elements):
		if index % 2 == 0:
			list.append(character)
	return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print()
# Further example >>

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result

print(full_emails([('alex@example.com', 'Alex Diego'), ('shay@example.com', 'Shay Brandt')])) 
# Iterating Over Lists Using Enumerate -
# When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the enumerate() function. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.



# List Comprehensions
multiples = []
for x in range(1, 11):
  multiples.append(x*7)
  
print(multiples)
# List comprehensions lets us create new lists based on sequences or ranges
multiples = [x*7  for x in range(1, 11)] 
print(multiples)
#  >>>
languages = ['Python', 'Pearl', 'Ruby', 'Go', 'Java', 'C']
lengths = [len(lengths) for lengths in languages]
print(lengths)
# >>>
multiples3 = [x for x in range(0, 101) if x%3 == 0]
print(multiples3)

# In-class Practice
# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
def odd_numbers(n):
	return [x for x in range(1, n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
print()
# List Comprehensions - You can create lists from sequences using a for loop, but there’s a more streamlined way to do this: list comprehension. List comprehensions allow you to create a new list from a sequence or a range in a single line. For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. This would iterate over the range 1 to 10, and multiply each element in the range by 2. This would result in a list of the multiples of 2, from 2 to 20.
# You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the comprehension. For example, [ x for x in range(1,101) if x % 10 == 0 ] would generate a list containing all the integers divisible by 10 from 1 to 100. The if statement we added here evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, it gets added to the list. List comprehensions can be really powerful, but they can also be super complex, resulting in code that’s hard to read. Be careful when using them, since it might make it more difficult for someone else looking at your code to easily understand what the code is doing.

# NOTE
# Lists and Tuples Operations Cheat Sheet
# Lists and Tuples Operations Cheat Sheet - Lists and tuples are both sequences, so they share a number of sequence operations. But, because lists are mutable, there are also a number of methods specific just to lists. This cheat sheet gives you a run down of the common operations first, and the list-specific operations second.
# Common sequence operations
# len(sequence) Returns the length of the sequence
# for element in sequence Iterates over each element in the sequence
#if element in sequence Checks whether the element is part of the sequence
# Sequence[i] Accesses the element at index i of the sequence, starting at zero
# sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
# for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time
# Check out the official documentation for sequence operations.

# List-specific operations and methods
# list[i] = x Replaces the element at index i with x
# list.append(x) Inserts x at the end of the list
# list.insert(i, x) Inserts x at index i
# list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
# list.remove(x) Removes the first occurrence of x in the list
# list.sort() Sorts the items in the list
# list.reverse() Reverses the order of items of the list
# list.clear() Removes all the items of the list
# list.copy() Creates a copy of the list
# list.extend(other_list) Appends all the elements of other_list at the end of list
# Most of these methods come from the fact that lists are mutable sequences. For more info, see the official documentation for mutable sequences and the list specific documentation.

# List comprehension
# [expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.
# [expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true. 

# _PRACTICE QUIZ_

# 1.) 
# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [] 
for name in filenames:
    if name.endswith('hpp'):
        new = name[:-3] + 'h'
        newfilenames.append(new)
    else:
        newfilenames.append(name)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
print()

# 2.) 
# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
  say = ""
  List = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say = word[1:] + word[0] + 'ay'
    List.append(say)
    # Turn the list back into a phrase
  return " ".join(List)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
print()

# 3.) 
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. For example: 
# 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
# 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
# Fill in the blanks to make the code convert a permission in octal format into a string format.
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += '-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
print()


# 4.) 
# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
  members = group + ': ' + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print()


# 5.)0
# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 
def guest_list(guests):
	for name, age, profession in guests:
         if profession[0].lower() == 'a' or profession[0].lower() == 'e' or profession[0].lower() == 'i' or profession[0].lower() == 'o' or profession[0].lower() =='u':
            print('{} is {} years old and works as an {}'.format(name, age, profession))
         else:
            print('{} is {} years old and works as a {}'.format(name, age, profession))
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as an Engineer
"""















# __DICTIONARIES__



# _What is a dictionary?_
# The data inside dictinoaries take the form of pairs of keys and values. 

x = {}
print(type(x))
# >>>>
file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
print(file_counts)
print(file_counts['txt'])
print('jpg' in file_counts)

file_counts['cfg'] = 8
print(file_counts)
   
file_counts['csv'] = 17
print(file_counts)                                                                                       

del file_counts['cfg']
print(file_counts)
print()

# In-class Practice
# The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	1) Add an entry for Epilogue on page 39. 	2) Change the page number for Chapter 3 to 24. 	3) Display the new dictionary contents. 	4) Display True if there is Chapter 5, False if there isn't.
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc['Epilogue'] = 39 # Epilogue starts on page 39
toc['Chapter 3'] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
check = 'Chapter 5' in toc
print(check) # Is there a Chapter 5?
print()
# Dictionaries Defined - Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections. However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples. When creating a dictionary, you use curly brackets: {}. When storing values in a dictionary, the key is specified first, followed by the corresponding value, separated by a colon. For example, animals = { "bears":10, "lions":1, "tigers":2 } creates a dictionary with three key value pairs, stored in the variable animals. The key "bears" points to the integer value 10, while the key "lions" points to the integer value 1, and "tigers" points to the integer 2. You can access the values by referencing the key, like this: animals["bears"]. This would return the integer 10, since that’s the corresponding value for this key.
# You can also check if a key is contained in a dictionary using the in keyword. Just like other uses of this keyword, it will return True if the key is found in the dictionary; otherwise it will return False. Dictionaries are mutable, meaning they can be modified by adding, removing, and replacing elements in a dictionary, similar to lists. You can add a new key value pair to a dictionary by assigning a value to the key, like this: animals["zebras"] = 2. This creates the new key in the animal dictionary called zebras, and stores the value 2. You can modify the value of an existing key by doing the same thing. So animals["bears"] = 11 would change the value stored in the bears key from 10 to 11. Lastly, you can remove elements from a dictionary by using the del keyword. By doing del animals["lions"] you would remove the key value pair from the animals dictionary.


# _Iterating over the Contents of a Dictionary_

file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
for extensions in file_counts:
    print(extensions)
for ext, amount in file_counts.items():
    print('There are {} files with the .{} extenxion'.format(amount, ext))

print(file_counts.keys())

print(file_counts.values())

for value in file_counts.values():
    print(value)

# In-class Practice 
# Now, it's your turn! Have a go at iterating over a dictionary!
# Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, feature in cool_beasts.items():
    print("{} have {}".format(animal, feature))
print()
# >>>

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1 
    return result

print(count_letters('aaaa'))
print(count_letters('tenant'))
print(count_letters('a long string of letters'))
print()
# Iterating Over Dictionaries - You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. This will iterate over the sequence of keys in the dictionary. If you want to access the corresponding values associated with the keys, you could use the keys as indexes. Or you can use the items method on the dictionary, like dictionary.items(). This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and the second is the value.
# If you only wanted to access the keys in a dictionary, you could use the keys() method on the dictionary: dictionary.keys(). If you only wanted the values, you could use the values() method: dictionary.values().



# _Dictinoaries Vs. Lists_
# You want to use dictionaries when you plan on searching for a specific element. 

# In-class Practice
# In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth, colors in wardrobe.items():
	for i in colors:
		print("{} {}".format(i, cloth))
print()
# >>>
# Set
# A set is a data type used when you want to store a bunch of elements and be certain that they're only present once.
# Elemens of a set are immutable. 


# Dictionary Methods Cheat Sheet
# Dictionary Methods Cheat Sheet
# Definition
# x = {key1:value1, key2:value2} 
# Operations
# len(dictionary) - Returns the number of items in the dictionary
# for key in dictionary - Iterates over each key in the dictionary
# for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
# if key in dictionary - Checks whether the key is in the dictionary
# dictionary[key] - Accesses the item with key key of the dictionary
# dictionary[key] = value - Sets the value associated with key
# del dictionary[key] - Removes the item with key key from the dictionary

# Methods
# dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
# dict.keys() - Returns a sequence containing the keys in the dictionary
# dict.values() - Returns a sequence containing the values in the dictionary
# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
# dict.clear() - Removes all the items of the dictionary
# Check out the official documentation for dictionary operations and methods.  

# _PRACTICE QUIZ_

# 1.) 
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+'@'+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
print()


# 2.) 
# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users :
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary	
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
print()


# 3.) 
# The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe) # Should be - " 'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}"
print()


# 4.)
# The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for key, value in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
