# __INTRODUCTION TO LOOPS__
# -- While loops, For loops and Recursion. 

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
