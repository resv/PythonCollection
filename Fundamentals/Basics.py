#ONLINE PYTHON COMPILER
https://www.programiz.com/python-programming/online-compiler/

#PRINT STATEMENT
print('hello')

To override the insertion of the new line character and replace it with a space, add end=" " as the last item in the print() parameters. 
This makes it possible to add the next print output to the same line, separated by a space. You might use this technique when a print() 
function is part of a for or while loop. Example syntax:  print(x+1, end=" ")

#PRINT ASSIGNMENT
x = 6
print(x)

#PRINT W/ VARIABLE CONDITION
x = 43
x = x + 1
print(x)

----------------------------------------------------------------------------------------------------------------------------------

#IF STATEMENT / CONDITIONAL STEPS
#indentation aka 4 spaces is important. Colons are necessary
#prints smaller then finis, "bigger" is skipped due to the 1st if being statisfied
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

----------------------------------------------------------------------------------------------------------------------------------

#WHILE LOOPS
#condition is true in a loop so it will print until we lower N to 0
n = 5
while n > 0 :
    print (n)
    n = n - 1
print('Blastoff!')

----------------------------------------------------------------------------------------------------------------------------------

#CONSTANTS
#string constants use single ' or double "

#Reserved words are special words that python are listening for them.
#Reserved words: False, None, True, and, as, assert, break, class, if, def, del, elif,
#Reserved words cont: else, except, return, for, from, global, try, import, in, is, lambda
#Reserved words cont: while, not, or, pass, raise, finally, continue, nonlocal, with, yield

----------------------------------------------------------------------------------------------------------------------------------

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

----------------------------------------------------------------------------------------------------------------------------------

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

----------------------------------------------------------------------------------------------------------------------------------

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

----------------------------------------------------------------------------------------------------------------------------------

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
----------------------------------------------------------------------------------------------------------------------------------

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
e.g. of break
def addition_table(given_number):
    iterated_number = 1
    my_sum = 1
    while iterated_number <= 5:
        my_sum = given_number + iterated_number
        if my_sum > 20:
            break
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
        iterated_number += 1
5 + 1 = 6
5 + 2 = 7
5 + 3 = 8
5 + 4 = 9
5 + 5 = 10
17 + 1 = 18
17 + 2 = 19
17 + 3 = 20

----------------------------------------------------------------------------------------------------------------------------------

** divisor is a number that divides into another without a remainder

# prime numbers - Integers that have only two factors, which are the number itself multiplied by 1. The lowest prime number is 2.
# prime factors - Prime numbers that are factors of an integer. For example, the prime numbers 2 and 5 are the prime factors of the number 10 
# (2x5=10). The prime factors of an integer will not produce a remainder when used to divide that integer. 

# divisor - A number (denominator) that is used to divide another number (numerator). For example, if the number 10 is divided by 5, the number 5 is the divisor.
# sum of all divisors of a number - The result of adding all of the divisors of a number together.  
# multiplication table - An integer multiplied by a series of numbers and their results formatted as a table or a list. For example:

----------------------------------------------------------------------------------------------------------------------------------

FOR LOOPS - start at 0
e.g.
for x in range(5)
    print(x)

Result:
0
1
2
3
4

e.g.2
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friends in friends:
    print("Hi " + friend)

e.g.3
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("total sum: " + str(sum) + " - Average: " + str(sum/length))

When to use:
For loops: -when theres a sequence of elements that you want to iterated number
           -loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence
While loops: -when you want to repeat an action until a condition changes
             -loops are used when a segment of code needs to execute repeatedly while a condition is true

RANGE FUNCTION:
The range() function can take up to three parameters:  range(start, stop, step) 
range(stop)
range(start, stop)
range(start, stop, step)

e.g. range(3) is 0 1 2 but if we add 3+1 to include 4, or you can write range(5)
for number in range(0,3+1):
    print(number*3)
----------------------------------------------------------------------------------------------------------------------------------
#RECURSION
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
-----
e.g.
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

----------------------------------------------------------------------------------------------------------------------------------
#STRING INDEXING AND SLICING
e.g.
fruit = "Mangosteen"
>>> fruit[1:4]
'ang'

#from X: to end
>>> fruit[5:]
'steen'

#From 0 to 5 + from 5to end
>>> fruit[:5] + fruit[5:]
'Mangosteen'

#index that contains the letter g using animals.index("g"), which will return the index 8
animals = "lions tigers and bears"
animals.index("g")
8

#substrings to locate the index where the substring begins. animals.index("bears") would return 17, since 
#that’s the start of the substring. If there’s more than one match for a substring, the index method will return the first match
animals = "lions tigers and bears"
animals.index("bears")
17
----------------------------------------------------------------------------------------------------------------------------------
#Check if string exists / BOOLEAN RESULT
animals = "lions tigers and bears"
"horses" in animals
False

animals = "lions tigers and bears"
"tigers" in animals
True
----------------------------------------------------------------------------------------------------------------------------------
# UPPER() & LOWER()
 "this is a string".upper(). T
 "THIS IS A STRING"
----------------------------------------------------------------------------------------------------------------------------------
# STRIP()
.strip("") move white spaces from both sides
.lstrip("") strips white space on left staticmethod
.rstrip("") strips white space on right side. 
----------------------------------------------------------------------------------------------------------------------------------
# COUNT()
Check to see how many chars or words appear in string

----------------------------------------------------------------------------------------------------------------------------------
# isnumeric()
check if string is only composed of numbers.
----------------------------------------------------------------------------------------------------------------------------------
# endswith() / BOOLEAN RESULT
checks if string ends with a substring you provide.
----------------------------------------------------------------------------------------------------------------------------------
# " ".join(["this","is","a","sentence"])
will input spaces between the array index
----------------------------------------------------------------------------------------------------------------------------------
# .split()
split a string into a list of strings, by default it splits on whitespace.
----------------------------------------------------------------------------------------------------------------------------------
#String operations
len(string) - Returns the length of the string
for character in string - Iterates over each character in the string
if substring in string - Checks whether the substring is part of the string
string[i] - Accesses the character at index i of the string, starting at zero
string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).
----------------------------------------------------------------------------------------------------------------------------------
#String methods
string.lower() - Returns a copy of the string with all lowercase characters
string.upper() - Returns a copy of the string with all uppercase characters
string.lstrip() - Returns a copy of the string with the left-side whitespace removed
string.rstrip() - Returns a copy of the string with the right-side whitespace removed
string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
string.count(substring) - Returns the number of times substring is present in the string
string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)
string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter
string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 
----------------------------------------------------------------------------------------------------------------------------------
#FORMAT
# "strings {}".format(variable) <- variable goes into the empty {}

name = "my name is {}, hi".format(Jason)
print(name)
"""Outputs:
my name is Jason, hi
"""
--------------------------
#If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).
first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""
--------------------------
"{var1} {var2}".format(var1=value1, var2=value2)
--------------------------
# {:d} integer value
'{:d}'.format(10.5) → '10'


#Formatting expressions
Expr       Meaning                                       Example
{:d}       integer value                                 '{:d}'.format(10.5) → '10'
{:.2f}     floating point with that many decimals        '{:.2f}'.format(0.5) → '0.50'
{:.2s}     string with that many characters              '{:.2s}'.format('Python') → 'Py'
{:<6s}     string aligned to the left that many spaces   '{:<6s}'.format('Py') → 'Py'
{:>6s}     string aligned to the right that many spaces  '{:>6s}'.format('Py') → '    Py'
{:^6s}     string centered in that many spaces           '{:^6s}'.format('Py') → '  Py  '
----------------------------------------------------------------------------------------------------------------------------------
#String Operations and Methods
.format() - String method that can be used to concatenate and format strings. 
{:.2f} - Within the .format() method, limits a floating point variable to 2 decimal places. The number of decimal places can be customized.
len(string) - String operation that returns the length of the string.
string[x] - String operation that accesses the character at index [x] of the string, where indexing starts at zero.
string[x:y] - String operation that accesses a substring starting at index [x] and ending at index [y-1]. If x is omitted, its value defaults to 0. 
            If y is omitted, the value will default to len(string).
string.replace(old, new) - String method that returns a new string where all occurrences of an old substring have been replaced by a new substring.
string.lower() - String method that returns a copy of the string with all lowercase characters.
----------------------------------------------------------------------------------------------------------------------------------
#TUPULES AND APPEND
The first value of the tuple is the index and the second value is the element itself.

#### for index, element in enumerate(sequence) - Iterates over both the indices and the elements in the sequence at the same time. ####

def skip_elements(elements):
	newElement = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			newElement.append(element)
	return newElement

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

Here is your output:
['a', 'c', 'e', 'g']
['Orange', 'Strawberry', 'Peach']

-------
# Another complex tuple
The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence 
"Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) 
should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. 
Fill in the gaps in this function to do that. 

def guest_list(guests):
	for ___:
		___
		print(___.format(___))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer

Answer:
def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}.".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])



----------------------------------------------------------------------------------------------------------------------------------
# List-specific operations and methods
# One major difference between lists and tuples is that lists are mutable (changeable) and tuples are immutable (not changeable). 

list[index] = x - Replaces the element at index [n] with x.
list.append(x) - Appends x to the end of the list.
list.insert(index, x) - Inserts x at index position [index].
list.pop(index) - Returns the element at [index] and removes it from the list. If [index] position is not in the list, the last element in the list is returned and removed.
list.remove(x) - Removes the first occurrence of x in the list.
list.sort() - Sorts the items in the list.
list.reverse() - Reverses the order of items of the list.
list.clear() - Deletes all items in the list.
list.copy() - Creates a copy of the list.
list.extend(other_list) - Appends all the elements of other_list at the end of list
----------------------------------------------------------------------------------------------------------------------------------
# List comprehension
[expression for variable in sequence] - Creates a new list based on the given sequence. Each element in the new list is the result of the given expression.
Example: my_list = [ x*2 for x in range(1,11) ]

[expression for variable in sequence if condition] - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true. 
Example: my_list = [ x for x in range(1,101) if x % 10 == 0 ]



def squares(start, end):
    return [n**2 for n in range(start,end+1) ]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

-----
### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines 
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)

results:
List comprehension result:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Long form code result:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

----------------------------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------