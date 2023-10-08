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

The comparison operators include: 
==    (equality) 
!=     (not equal to) 
>       (greater than)
<      (less than)
>=    (greater than or equal to)
<=    (less than or equal to)

print(10-4 != 10+4) # The != operator checks if the 2 values are
True                # NOT equal to each other. If true, Python              
                    # returns a True result. 

The comparison operators greater than > and less than < can be used to alphabetize words in Python. 
The letters of the alphabet have numeric codes in Unicode (also known as ASCII values). 
The uppercase letters A to Z are represented by the Unicode values 65 to 90. The lowercase letters 
a to z are represented by the Unicode values 97 to 122.     
(upper case is lower on ascii values)

 If the strings have the same first few letters, the comparison will 
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values
print("sunbathe" > "suntan")
False

var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)

Is "my computer" greater than or equal to "my chair"? Result:  True
Is "Spring" less than or equal to "Winter"? Result:  True
Is "pineapple" less than or equal to "pineapple"? Result:  True


OR output
Expression1 Expression2 Result
True        True        True
True        False       True
False       True        True
False       False       False

# False or False returns False

The not logical operator inverts the value of the comparison expression
This is a helpful tool when you want to execute a block of code as long as a certain condition is not present.
-If the conditional  expression is True, the not logical operator can be added to make the expression not True (False). 
-If the conditional  expression is False, the not logical operator can be added to make the expression not False (True).  

x = 2*3 > 6
print("The value of x is:")
print(x)
The value of x is:
False

print("The inverse value of x is:")
print(not x)
The inverse value of x is:
True

today = "Monday"
print(not today == "Tuesday") 
True

Conditions will only run if True
also we can start a non sub indented line to return something else. using it as an else itself without stating else.

def is_even(number:
    if number % 2 ==0:
        return True
    return False
^^^^^^ This code will check if there is a remainder (modulo operator) if number is divded by 2 and then return True if true 
or it will fall back and just return False

elif statements
An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false
If condition1 is True: Then perform action1 and exit if-elif-else block
If condition2 is True: Then perform action2 and exit if-elif-else block
If neither condition1 nor condition2 are True: Then perform action3 and exit if-elif-else block

Syntax of an if-elif-else block
if condition1:
    action1
elif condition2:
    action2
else:
    action3

Incrementation
# x += 1  is the same thing as x = x + 1


while Loops
A while loop executes the body of the loop while a specified condition remains True.

e.g.
multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")

result:
5
10
15
20
25
30
35
40
45
50
Done

Failure to initialize variables. Make sure all the variables used in the loop’s condition are initialized before the loop.

Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will
 eventually end for all possible values of the variables. You can often prevent an infinite loop by using the break keyword or by 
 adding end criteria to the condition part of the while loop.

# prime numbers - Integers that have only two factors, which are the number itself multiplied by 1. The lowest prime number is 2.
# prime factors - Prime numbers that are factors of an integer. For example, the prime numbers 2 and 5 are the prime factors of the number 10 
# (2x5=10). The prime factors of an integer will not produce a remainder when used to divide that integer. 

# divisor - A number (denominator) that is used to divide another number (numerator). For example, if the number 10 is divided by 5, the number 5 is the divisor.
# sum of all divisors of a number - The result of adding all of the divisors of a number together.  
# multiplication table - An integer multiplied by a series of numbers and their results formatted as a table or a list. For example: