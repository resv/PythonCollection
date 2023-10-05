#ONLINE PYTHON COMPILER
https://www.programiz.com/python-programming/online-compiler/

#PRINT STATEMENT
print('hello')

#PRINT ASSIGNMENT
x = 6
print(x)

#PRINT W/ VARIABLE CONDITION
x = 43
x = x + 1
print(x)

#IF STATEMENT / CONDITIONAL STEPS
#indentation aka 4 spaces is important. Colons are necessary
#prints smaller then finis, "bigger" is skipped due to the 1st if being statisfied
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

#WHILE LOOPS
#condition is true in a loop so it will print until we lower N to 0
n = 5
while n > 0 :
    print (n)
    n = n - 1
print('Blastoff!')

#CONSTANTS
#string constants use single ' or double "

#Reserved words are special words that python are listening for them.
#Reserved words: False, None, True, and, as, assert, break, class, if, def, del, elif,
#Reserved words cont: else, except, return, for, from, global, try, import, in, is, lambda
#Reserved words cont: while, not, or, pass, raise, finally, continue, nonlocal, with, yield

#NAMING CONVENTION
#Py must start with a letter or underscore_ and case sensitive

#MNEMONIC = MEMORY AID
#Choosing a variable name that helps us remember what we intend to store.

#KEYWORDS
#Values: True, False, None
#Conditions: if, elif, else
#Logical operators: and, or, not
#Loops: for, in, while, break, continue
#Functions: def, return  

#Arithmetic operators
# x + y            Addition + operator returns the sum of x plus y
# x - y             Subtraction - operator returns the difference of x minus y
# x * y            Multiplication * operator returns the product of x times y
# x / y             Division / operator returns the quotient of x divided by y
# x**e            Exponent ** operator returns the result of raising x to the power of e 
# x**2            Square expression returns x squared
# x**3            Cube expression returns x cubed
# x**(1/2)    Square root (½) or (0.5) fractional exponent operator returns the square root of x
# x // y           Floor division operator returns the integer part of the integer division of x by y
# x % y          Modulo operator returns the remainder part of the integer division of x by y


#Order of operations
#The order of operations are to be calculated from left to right in the following order
#Parentheses ( ), { }, [ ]
#Exponents xe   (x**e)
#Multiplication * and Division /  
#Addition + and Subtraction -    
#You might find the PEMDAS mnemonic device to be helpful in remembering the order.   

#find out data type 
# print(type("a"))
   #<class 'str'>
# print(type("2"))
   #<class 'int'>
# print(type(2.5))
   #<class 'float'>
 

# Terms
# expression - a combination of numbers, symbols, or other values that produce a result when evaluated
# data types - classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)
# variable - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type
# implicit conversion - when the Python interpreter automatically converts one data type to another
# explicit conversion - when code is written to manually convert one data type to another using a data type conversion function:
# str() - converts a value (often numeric) to a string data type
# int() - converts a value (usually a float) to an integer data type
# float() - converts a value (usually an integer) to a float data type?

Function basic
# def greeting(name, department):
#    print("welcome, " + name)
#    print("You are part of " + department)
# >>> greeting("blake", "IT Support")
#Welcome, Blake
#You are part of IT Support

Function return
#def area_triangle(base, height):
#    return base*height/2
#area_a = area_triangle(5,4)
#area_b = area_triangle(7,3)
#sum = area_a + area_b
#print("the sum of both triangles is : " + str(sum))
#the sum of both triangles is: 20.5

Terms
#return value - the value or variable returned as the end result of a function
#parameter (argument) -  a value passed into a function for use within the function
#refactoring code - a process to restructure code without changing functionality

Knowledge
#The purpose of the def() keyword is to define a new function. 
#Best practices for writing code that is readable and reusable:
#Create a reusable function - Replace duplicate code with one reusable function to make the code easier to read and repurpose.
#Refactor code - Update code so that it is self-documenting and the intent of the code is clear.
#Add comments - Adding comments is part of creating self-documenting code. Using comments allows you to leave notes to yourself and/or other programmers to make the purpose of the code clear.