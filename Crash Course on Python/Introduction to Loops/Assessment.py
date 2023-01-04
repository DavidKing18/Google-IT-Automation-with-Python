# __INTRODUCTION TO LOOPS__
# -- While loops, For loops and Recursion. 

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
