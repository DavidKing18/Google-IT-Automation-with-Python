# __INTRODUCTION TO LOOPS__
# -- While loops, For loops and Recursion. 


# _While Loops_
# While loops instruct your computer to continuously execute your code based on the value of a condition. 

x = 0   # Initializing - To give an intial value to a variable. 
while x < 5:
  print('Not there yet, x = ' + str(x))
  x += 1
print('x = ' + str(x))
# Anatomy of a While Loop - A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.  
print()
# _More while Loops_
def attempts(n):
  x = 1 # Note - Always initialize your variables. 
  while x<= n:
    print('Attempt ' + str(x))
    x += 1
  print('Done')
  
attempts(5)
# Whenever you're writing a loop, check that you're initializing all the variables you want to use before you use them. 
# Common Pitfalls With Variable Initialization - You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable without first initializing it, you'll run into a NameError. This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it. Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to initialize your variables before using them!

# _Infinite Loops & Breaking them_
# Infinite loop Example
  #     while x % 2 == 0:
  #         x = x/2

if x != 0:
  while x % 2 == 0:
    x = x/2
# OR
while x % 2 == 0 and x != 0:
  x /= 2
  
# _Breaking loops
  # while True:
  #     do_something_cool()
  #      if user_requested_to_stop():
  #        break

# Infinite loops and Code Blocks - Another easy mistake that can happen when using loops is introducing an infinite loop. An infinite loop means the code block in the loop will continue to execute and never stop. This can happen when the condition being evaluated in a while loop doesn't change. Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero. In the Coursera code blocks, you may see an error message that reads "Evaluation took more than 5 seconds to complete." This means that the code encountered an infinite loop, and it timed out after 5 seconds. You should take a closer look at the code and variables to spot where the infinite loop is.


# _Practice Quiz_

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number /=  factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

print()

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

print()

def sum_divisors(number):
    sum = 0
    factor = 1
    
    while factor < number:
        if factor == 0:
            break
        if number % factor == 0:
            sum += factor
        factor += 1
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

print()


def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number*multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15



# _FOR LOOPS_

# A for loop iterates over a sequence of values.
# E.get
for x in range(5):
  print(x)
print()
# Iterating over stringgs - 
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
  print('Hi ' + friend)
print()
# Iterating Over Strings
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
  sum += value
  length += 1
print('Total sum : ' + str(sum) + ' - Average: ' + str(sum/length))
# For Loops Recap - For loops allow you to iterate over a sequence of values. Let's take the example from the beginning of the video:
# for x in range(5):
#  print(x)
# Similar to if statements and while loops, for loops begin with the keyword for with a colon at the end of the line. Just like in function definitions, while loops and if statements, the body of the for loop begins on the next line and is indented to the right. But what about the stuff in between the for keyword and the colon? In our example, we’re using the range() function to create a sequence of numbers that our for loop can iterate over. In this case, our variable x points to the current element in the sequence as the for loop iterates over the sequence of numbers. Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value. So range(5) will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.
# Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4. Our for loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable x and the code within our loop body will execute for each iteration through the sequence. So for the first loop, x will contain 0, the next loop, 1, and so on until it reaches 4. Once the end of the sequence comes up, the loop will exit and the code will continue.
# The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use for loops to iterate over a list of strings, such as usernames or lines in a file.
# Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. A for loop works well when you want to iterate over a sequence of elements.  
print()
# More for loop Examples
product = 1 
for n in range(1, 10):
  product = product * n
print(product) 
# Script calculates the product of all numbers from one to 10.
print()

def to_celcius(x):
  return (x-32)*5/9
for x in range (0, 101, 10):
  print(x, to_celcius(x))
# Script converts from fahranheit to degree celcius from 0 to 100, in intervals of 10.
print()
# A Closer Look at the Range() Function - Previously we had used the range() function by passing it a single parameter, and it generated a sequence of numbers from 0 to one less than we specified. But the range() function can do much more than that. We can pass in two parameters: the first specifying our starting point, the second specifying the end point. Don't forget that the sequence generated won't contain the last element; it will stop one before the parameter specified. The range() function can take a third parameter, too. This third parameter lets you  alter the size of each step. So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by 5. To quickly recap the range() function when passing one, two, or three parameters:
# One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
# - Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
# - Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.

# _Nested For Loops_

for left in range(7):
  for right in range(left, 7):
    print('[' + str(left) + '|' + str(right) + ']', end = "")
  print()
# Creates a Dominos set
print()

teams = [ 'Chelsea', 'Liverpool', 'Manchester', 'Man-City']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + ' vs ' + away_team)
# Pairs teams for matches without pairing the same team together. 
print()

# Loops Cheat Sheet - Loops Cheat Sheet. Check out below for a run down of the syntax for while loops and for loops.
# While Loops - A while loop executes the body of the loop while the condition remains True.
# Things to watch out for!
# - Failure to initialize variables. Make sure all the variables used in the loop’s condition  are initialized before the loop.
# - Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables.
# Typical use: While loops are mostly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.
# For Loops - A for loop iterates over a sequence of elements, executing the body of the loop for each element in the sequence.
# The range() function: range() generates a sequence of integer numbers. It can take one, two, or three parameters:
# - range(n): 0, 1, 2, ... n-1
# - range(x,y): x, x+1, x+2, ... y-1
# - range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)
# Common pitfalls:
# - Forgetting that the upper limit of a range() isn’t included.
# - Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by letter, but that might not be what you want.
# Typical use: For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.
# Break & Continue
# You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a cycle due to a separate condition.
# You can use the continue keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence aren’t relevant.
# If you want to learn more, check out this wiki page on for loops.


# _Practice_
# In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24. The code below makes the factorial function return the right number.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * (i)
    return result
print(factorial(4)) # should return 24
print(factorial(5)) # should return 
print()

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n**2
    return sum
print(sum_squares(10)) # Should be 285
# Sript calculates the sum of the squares of numbers from 0 to 9.
print()


for i in range(3, 7):
  print(i)
# Outputs numbers from 3, 4, 5, 6. 
print()


friends = 'David'
for friend in friends:
  print(friend)
# Iterates over each character
print() 
 
def validate_users(users):
  for user in users:
    if len(user) >= 3:
      print(user + " is valid")
    else:
      print(user + " is invalid")
validate_users(['purplecat'])
# The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3 characters long.
print()


# _Practice Quiz

def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result
for n in range(0,10):
    print(n, factorial(n+1))
# Outputs a number and its factorial. 
print()

for num in range(1,11):
  print(num**3)
# Outputs the cube of a number. 
print()

def multiple(num):
    for i in range(0,100):
        if i % num == 0:
            print(i)
multiple(7)
# Outputs the 'less than 100' multiples of a number.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    return True
  return is_power_of(number/base, base) 

    # Recursive case: keep dividing number by base.
print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False




# __Recursion__

# Recursion is the repeated application of the same procedure to a smaller problem.
# In programming, recursion is a way of doing a repetitive task by having a function call itself. 
# Example:-
def factorial(n):
  print('Factorial called with ' + str(n))
  if n < 2:
    print('Returning 1')
    return 1
  result = n * factorial(n-1)
  print('Returning ' + str(result) + ' for factorial of ' + str(n))
  return result
# lol -- I don't know how to explicitly define the function of this script. 
# Additional Recursion Sources - In the past, we visited the basic concepts of recursive functions.
# A recursive function must include a recursive case and base case. The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.


# _Practice Quiz_

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    if number == 1:
      return True
    else:
      return False

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
# Script returns whether the number is a power of the base. 
print()


def sum_positive_numbers(n):
  if n > 1:
    return n + sum_positive_numbers(n-1)
  return n
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
# Script returns the sum of all positive numbers between the number n received and 1.

# __MY ASSESSMENT__

# 1. Write a script that prints out numbers 1 through 7. 
number = 1
while number <= 7:
	print(number, end=" ")
	number += 1
print()

# 2.  Write a script that prints out each letter of a word on a separate line
def show_letters(word):
	for each in word:
		print(each)

show_letters("Hello")
# Should print one line per letter
print()

# 3. Write a script that returns how many digits a number has.
def digits(n):
  count = 0
  if n == 0:
	  return 1 
  while n > 0:
    count += 1
    n = n // 10
  return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
print()

# 4. Write a script that prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column)
def multiplication_table(start, stop):
	for x in range(1, start+stop):
		for y in range(1, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
print()

# 5. Write a script (function) that  counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x = x - 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x+1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
print()

# 6. Write a script (function) that returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”.
def even_numbers(maximum):
	return_string = ""
	for x in range(1, maximum + 1):
		if x % 2 == 0:
			return_string += str(x) + " "
	return return_string
print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
print()

# 7. What is the value of x at the end of the following code?
for x in range(1, 10, 3):
    print(x)
# ANS:- 9
print()

# 8. What is the value of y at the end of the following code?
for x in range(10):
    for y in range(x):
        print(y)
# ANS:- 8
print()

