# _DEFINING FUNCTIONS_ 

def greeting(name):
    print('Welcome, ' + name)

greeting('Frenando')

def greet(name, clan):
    print('Respect, ' + name)
    print('Congrats on joining the ' + clan + ' Clan')

greet('Oscar', 'Wu-Tang')

#Defining Functions - We looked at a few examples of built-in
#functions in Python, but being able to define your own functions 
#is incredibly powerful. We start a function definition with the 
#def keyword, followed by the name we want to give our function. 
#After the name, we have the parameters, also called arguments, 
# for the function enclosed in parentheses. A function can have 
# no parameters, or it can have multiple parameters. Parameters 
# allow us to call a function and pass it data, with the data being 
# available inside the function as variables with the same name as 
# the parameters. Lastly, we put a colon at the end of the line. 
#After the colon, the function body starts. It’s important to note 
# that in Python the function body is delimited by indentation. 
# This means that all code indented to the right following a function 
# definition is part of the function body. The first line that’s no
# longer indented is the boundary of the function body. It’s up to 
# you how many spaces you use when indenting -- just make sure to be
# consistent. So if you choose to indent with four spaces, you need 
# to use four spaces everywhere in your code.


# _RETURNING VALUES_

def areaTriangle(base, height):
    return (base*height)/2

area_a = areaTriangle(2,4)
area_b = areaTriangle(9,9)
sum = area_a + area_b
print('The sum of both area is: ' + str(sum))


def convertSeconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    secondsLeft = seconds - hours*3600 - minutes*60
    return hours, minutes, secondsLeft 

hours, minutes, seconds = convertSeconds(10000)
print(hours, minutes, seconds)
# OR
final = convertSeconds(10000)
print(final)

# Also ---

def call(name):
    print('Welcome, ' + name)

result = call('David')
print(result)

#Note:- 'None' is a special data type in Python used to indicate
# that things are empty or that they returned nothing. 

#Returning Values Using Functions - Sometimes we don't want a 
# function to simply run and finish. We may want a function to 
# manipulate data we passed it and then return the result to us. 
# This is where the concept of return values comes in handy. 
# We use the return keyword in a function, which tells the function 
# to pass data back. When we call the function, we can store the 
# returned value in a variable. Return values allow our functions 
# to be more flexible and powerful, so they can be reused and called 
# multiple times.
#Functions can even return multiple values. Just don't forget to 
# store all returned values in variables! You could also have a 
# function return nothing, in which case the function simply exits.

# _QUIZ_

# Number 1
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result.
print("The round-trip in kilometers is " + str(2 * my_trip_km))

# Number 2

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger= order_numbers(100, 99)
print(smaller, bigger)

# Number 3

def lucky_number(name):
  number = len(name) * 9 # 'len()' is a length/numberOfCharacters function
  result = "Hello " + name + ". Your lucky number is " + str(number)
  return result
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
