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
