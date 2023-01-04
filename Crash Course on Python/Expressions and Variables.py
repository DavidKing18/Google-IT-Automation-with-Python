# -DATA TYPES-

# Data types include: Strings, Integer, Float e.t.c

print(7+5)

print("Hello " + "world!")

# print(7 + "8") is invalid because of varying data types

print(type('a'))
print(type(2))
print(type(2.5))

# In Python, text in between quotes -- either single or double
# quotes -- is a string data type. An integer is a whole number, 
# without a fraction, while a float is a real number that can 
# contain a fractional part. For example, 1, 7, 342 are all integers,
# while 5.3, 3.14159 and 6.0 are all floats. When attempting to mix
# incompatible data types, you may encounter a TypeError. 
# You can always check the data type of something using the type() function.


# -VARIABLES-

# Variables are containers for data. For example;

length = 17
width = 12
area = length * width 
print(area)

# Variables are very important in programming because they let
#perform operations on data that may change

# Variable Naming Restrictions - 
#(i.) Don't use keywords or functions that Python reserves for its own.      
#(ii.) Don't use spaces
#(iii.) Must start with a letter or an underscore(_).   
#(iv.) They can only be made up of numbers and underscores.


# EXPRESSIONS, NUMBERS, AND TYPE CONVERSIONS

#Types of conversions - Implicit and Explicit. 

#ImplicitConversion
print(7 + 8.5)

#ExplicitConversion
base = 7
height = 16
areaOfTriangle = (base * height)/2
print ('The area of the triangle is ' + str(areaOfTriangle))

#As we saw earlier in the video, some data types can be mixed and matched 
#due to implicit conversion. Implicit conversion is where the interpreter
#helps us out and automatically converts one data type into another, 
#without having to explicitly tell it to do so. By contrast, explicit 
#conversion is where we manually convert from one data type to another
#by calling the relevant function for the data type we want to convert to. 
#We used this in our video example when we wanted to print a number 
#alongside some text. Before we could do that, we needed to call the str() 
#function to convert the number into a string. Once the number was explicitly
#converted to a string, we could join it with the rest of our textual string and print the result.