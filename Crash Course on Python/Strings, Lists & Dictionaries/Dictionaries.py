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
