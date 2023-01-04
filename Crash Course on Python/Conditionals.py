# __COMPARING THINGS__

print(10>1) # Results in "True" - which is a boolean data type.
# Boolean - One of two possible states: either true or false.
print('cat' == 'dog')
print(1 != 2)
print(1 == '1')
# Logical operators
print("Yellow" > 'Cyan' and 'Brown' > 'Magenta') #To evaluate as true, 
# the 'and' operator would need bothe expressions to be true at the same time. 

print(25 > 50 or 1 != 2) # If we use the 'or' operator, the expression will be true if either of the 
# expressions are true and false only when both expressions are false. 

print(not 42 == "Answer") # The 'not' operator inverts the value of the 
# expression that's in front of it. 

# Note: Comparison Operators: In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False. To check if two values are the same, we can use the equality operator: == To check if two values are not the same, we can use the not equals operator: !=   We can also check if values are greater than or lesser than each other using > and <. If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError. We can make very complex comparisons by joining statements together using logical operators with our comparison operators. These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true. When using the or operator, if either side of the comparison is true, then the whole statement is true. Lastly, the not operator simply inverts the value of the statement immediately following it. So if a statement evaluates to True, and we put the not operator in front of it, it would become False.


# _Branching with 'if' statements_

#Branching is the ability of a program to alter its execution sequence. 

def hinit_username(username):
    if len(username)  < 3:
        print('Invalid username. Must be at least 3 characters long.')
# if Statements Recap - We can use the concept of branching to have our code alter its execution sequence depending on the values of variables. We can use an if statement to evaluate a comparison. We start with the if keyword, followed by our comparison. We end the line with a colon. The body of the if statement is then indented to the right. If the comparison is True, the code inside the if body is executed. If the comparison evaluates to False, then the code block is skipped and will not be run.

 
 
 # _Else statements_
 
def hinit_username(username):
    if len(username)  < 3:
        print('Invalid username. Must be at least 3 characters long.')
    else: 
        print('Valid username.')

def is_even(number):
    if number % 2 == 0:
        return True
    return False # When a return statement is executed, the function exits so that the code that follows doesn't get executed. 
# Else Statements and the Modulo Operator - We just covered the if statement, which executes code if an evaluation is true and skips the code if it’s false. But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement. The else statement follows an if block, and is composed of the keyword else followed by a colon. The body of the else statement is indented to the right, and will be expected if the above if statement doesn’t execute. We also touched on the modulo operator, which is represented by the percent sign: %. This operator performs integer division, but only returns the remainder of this division operation. If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%2 would return 0, as there is no remainder.



# _Elif Statements_

def hinit_username(username):
    if len(username)  < 3:
        print('Invalid username. Must be at least 3 characters long.')
    elif len(username) > 15:
        print('Invalid username. Must be at most 15 characters long.') # Restricts username to at most 15 characters.
    else: 
        print('Valid username.')
# More Complex Branching with elif Statements - Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!
# Conditionals Cheat Sheet - In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks. It’s a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance. 
# Comparison operators
#	a == b: a is equal to b
#	a != b: a is different than b
#	a < b: a is smaller than b
#	a <= b: a is smaller or equal to b
# 	a > b: a is bigger than b
#	a >= b: a is bigger or equal to b
# Logical operators
#	a and b: True if both a and b are True. False otherwise.
#	a or b: True if either a or b or both are True. False if both are False.
#	4not a: True if a is False, False if a is True.






# _QUIZ_

# Number 1
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# Number 2
def input(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)
input(12)
input(11)
input(10)

# Number 3
print("A dog" > "A mouse")
print(9999+8888 > 100*100)

# Number 4
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder == 0  or (partial_block_remainder >= 0 and full_blocks == 0):
        return 4096
    return 8192

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192





# _END OF MODULE QUIZ_
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


def exam_grade(score):
	if score == 100:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


def format_name(first_name, last_name):
	# code goes here
	if first_name == "" and last_name == "":
		return ""
	elif first_name == "":
		return "Name: " + last_name
	elif last_name == "":
		return "Name: " + first_name
	elif first_name == "" and last_name == "":
		return "wow"
	else:
		string = "Name: "  + last_name + ", "  + first_name
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))



def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if denominator != 0:
		lesserQuotient = (numerator % denominator)/denominator
		return lesserQuotient
	else:
		return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
