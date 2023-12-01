----------------------------- Opening a file and reading ------------------------------------------------------------------------

file = open("spider.txt") #opens file

print(file.readline()) #reads single line of the file

print(file.readline()) #reads the next line of the file, as it updates to the next line

print(file.read()) #reads the rest of the file from where ever we are

file.close() #closes file that is opened


#"WITH" will automatically close file after read.
file.close() 
with open("spider.txt") as file:
          (print(file.readline())
           
----------------------------- Iterating through a file ------------------------------------------------------------------------

with open("spider.txt") as file:
    for line in file:
        print(line.upper())


# Most likely will have to use .strip() to remove linebreaks.
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

#Sorting contents by putting it into a list
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

----------------------------- Writing to a file ------------------------------------------------------------------------
with open("spider.txt", "w") as file:   # "w" means to write / "r" is default and no need to pass it / "a" is append / "r+" read and write
    file.write("Lets add another line")
#returns number of chars

----------------------------- DIRECTORIES ------------------------------------------------------------------------
#import os <--- must do to use across all operating systems

------------------------------ Remove FILE os.remove("x") ---------------------------------------------------------------
import os 
os.remove("novel.txt")

------------------------------ Rename FILE | os.rename("old","new") ---------------------------------------------------------------
os.rename("oldname.txt", "newname.txt")

------------------------------ Check if file exists | os.path.exists("X")---------------------------------------------------------------
os.path.exists("filename.txt")
True/False

------------------------------ Get File size | os.path.getsize("X") ---------------------------------------------------------------
os.path.getsize("sample.txt")
192 (bytes)

------------------------------ Check when File was last modified | os.path.getmtime("x") ---------------------------------------------------------------
os.path.getmtime("sample.txt")
21392819032103

------------------------------ Fix time above^^ ---------------------------------------------------------------
import datetime
timestamp = os.path.getmtime("sample.txt")
datetime.datetime.fromtimestamp(timestamp)
datetime.datetime(2020, 1, 6, 7, 2, 3 ,899999)

------------------------------ Get absolute path of a file | os.path.abspath("x")  ---------------------------------------------------------------
os.path.abspath("spider.txt")
'/home/user/spider/txt'
------------------------------ Get current directory | os.getcwd()  ---------------------------------------------------------------
print(os.getcwd())

------------------------------ Make new directory | os.mkdir("x")  ---------------------------------------------------------------
os.mkdir("newdir")

------------------------------ Change directory | os.chdir("x") ---------------------------------------------------------------
os.chdir("differentdir")

------------------------------ Change directory UP ONE LEVEL | os.chdir("x") ---------------------------------------------------------------
current_directory = os.getcwd()
    # Get the current working directory
parent_directory = os.path.dirname(current_directory)
    # Get the parent directory (go up one level)
os.chdir(parent_directory)
    # Change the current working directory to the parent directory
print("Current Directory:", os.getcwd())
    # Now the current working directory is the parent directory

------------------------------ ABS path or parent directory | os.path.join(os.getcwd(), "..") ---------------------------------------------------------------
import os

def parent_directory():
        # Create a relative path to the parent of the current working directory
    relative_parent = os.path.join(os.getcwd(), '..')
        # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)
print(parent_directory())

------------------------------ REMOVE directory | os.rmdir("x") ---------------------------------------------------------------
os.rmdir("directory")
#only works if you have an empty dir

------------------------------ Check in Directory | os.listdir("x") ---------------------------------------------------------------
os.listdir("directory")
['file1", "folder2", "music3"]
 #this may only list file names and we know that filenames do not actually tell the correct ext... so you can use the next code below to tell us what this is.

------------------------------ Check file type in directory | os.path.isdir("x") ---------------------------------------------------------------
os.listdir("directory")
['file1", "folder2", "music3"]
    dir = "directory"
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)
        if os.path.isdir(fullname):
            print("{} is a directory".format(fullname))
        else:
            print("{} is a file".format(fullname))
# results            
directory/file1 is a file
directory/folder2 is a directory
directory/music3 is a file

------------------  CSV FILES | CSV FILES | CSV FILES | CSV FILES | CSV FILES------------------
import csv # required import
------------------------------ CSV OPENING | variable = open("x.txt") <br> csv_"variable" = csv.reader(variable)  ---------------------------------------------------------------
# Open the CSV file for reading
with open("example.csv", "r") as file:
    csv_reader = csv.reader(file)

    # Process the CSV data
    for row in csv_reader:
        print(row)
------------------------------ CSV READING | csv.reader(".csv")  ---------------------------------------------------------------
# Open the CSV file for reading
with open("example.csv", "r") as file:
    csv_reader = csv.reader(file)

    # Process the CSV data
    for row in csv_reader:
        print(row)

------------------------------ CSV CLOSING | csv.reader(".csv")  ---------------------------------------------------------------
  "x.csv".close()

------------------------------ CSV Unpacking values (close files too) | *include "x".close() ---------------------------------------------------------------
# Open the CSV file for reading
with open("example.csv", "r") as file:
    csv_reader = csv.reader(file)

    # Process the CSV data
    for row in csv_reader:
        name, phone, role = row
        print("name: {}, Phone: {}, Role: {}".format(name, phone, role))
        file.close()
------------------------------ CSV WRITING | csv.writer("file.csv") writer.writerows(contentVariable)) contentVariable =  [["x"], ["y"], ["z"]] ---------------------------------------------------------------
contentVariable = [["x"], ["y"], ["z"]]
with open("file", "w") as file:
    writer = csv.writer(file)
    writer.writerows(contentVariable)
    
------------------------------ CSV READING with dictionaries | DictReader ---------------------------------------------------------------
with open("x.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

------------------------------ CSV WRITING with dictionaries | DictWriter  ---------------------------------------------------------------
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv. DictWriter(by_department, fieldnames=keys) 
    writer.writeheader()
    writer.writerows (users)
------------------------------ CSV ANOTHER EXAMPLE ---------------------------------------------------------------
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))
------------------------------ CSV SKIPPING FIRST ROW  ---------------------------------------------------------------
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for i, row in enumerate(rows):
      if i == 0:
        continue
      # Format the return string for data rows only
      name, color, type = row

      return_string += "a {} {} is {}\n".format(name, color, type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

------------------------------ REGEX | import re ---------------------------------------------------------------
#e.g. r = raw string
    test = re.search(r"aza", "plaza")
    print(test)
#Result
    <re.Match object: span=(2,5), match='aza'>

---------------------------- USING REGEX AS A FUNCTION ----------------------------------------------------
#e.g. r = raw string

import re
def check_aei (text):
  result = re.search(r"a.e.i.", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

---------------------------- IGNORE CASE | re.IGNORECASE ----------------------------------------------------
#e.g. r = raw string

import re
def check_aei (text):
  result = re.search(r"a.e.i", text, re.IGNORECASE)
  return result != None

------------------------------ Search Upper or lower | re.search(r"[Pp]ython", Python") ---------------------------------------------------------------
print(re.search(r"[Pp]ython", Python))

------------------------------ Search any LOWERCASE | re.search(r"[a-z]way", highway") ---------------------------------------------------------------
print(re.search(r"[a-z]way", highway"))
#result: re.Match object; span(3-7), match='hway'>

------------------------------ Search Starting with | re.search(r"^[a-z]way", highway")  ---------------------------------------------------------------
------------------------------ Search ENDING with | re.search(r"high[a-z]$", highway")  ---------------------------------------------------------------
------------------------------ Search START UPPER + ANY AMOUNT + SPACE + ENDING WITH CERTAIN PUNC | "^[A-Z][a-z\s]*[.!?]$" ---------------------------
------------------------------ Search any UPPERCASE | re.search(r"[A-Z]way", highway")  ---------------------------------------------------------------
------------------------------ Search any NUMBER | re.search(r"[0-9]way", highway")  ---------------------------------------------------------------
------------------------------ Search any COMBINED | re.search(r"[a-zA-Z0-9]way", highway")  ---------------------------------------------------------------
------------------------------ Search up to 5 indexes COMBINED | re.search(r"\d{5}", text)  ---------------------------------------------------------------
------------------------------ Search PUNCTUATION in any order | result = re.search(r"[.,:;?!]", text) -----------------------------------------------------
------------------------------ Search anything thats NOT a letter (uses ^ as an negative) | result = re.search(r"[^a-zA-Z]", text) -------------------------
------------------------------ Search anything thats NOT a letter AND NOT SPACE (uses space in bracket) | result = re.search(r"[^a-zA-Z ]", text) ----------
------------------------------ Search OR (first hit will always be result) | result = re.search(r"[cat|dog]", text) ----------------------------------------
------------------------------ Search ALL hits findall | result = re.findall(r"[cat|dog", text) -------------------------------------------------------------
------------------------------ Search WILD CARD .* (ignores space, keeps going until last "n")| re.search(r"py.*n", "text")---------------------------------------------------------------
------------------------------ Search WILD CARD .* (aware of spaces, stops at the first detection)| re.search(r"py[a-z]*n", "text") ---------------------------------------------------------------
------------------------------ Search Matching pattern of any amount of "o" next to any amount of "l" ------------------------------------------------------
print(re.search(r"o+l+", "goldfish")) 
<re.Match object; span=(1, 3), match='ol'> 
>>> print(re.search(r"o+l+", "woolly")) 
<re.Match object; span=(1, 5), match='ooll'> ---------------------------------------------------------------

 ------------------------------ Search optional ? | re.search(r"p?each", "each")  ---------------------------------------------------------------
only finds "each" but "peach will be positive"
------------------------------  ---------------------------------------------------------------

------------------------------ ESCAPING CHARS \ | re.search(r"\.com", google.com) ---------------------------------------------------------------
treats . as a char and not a modifier.
------------------------------ NEW LINE \n | ---------------------------------------------------------------
------------------------------ NEW TAB \t |---------------------------------------------------------------
------------------------------ MATCH ANY ALPHANUMERIC (Char, #, and _) \w* |---------------------------------------------------------------
------------------------------ MATCH DIGITS \d ---------------------------------------------------------------
------------------------------ MATCH SPACE \s ---------------------------------------------------------------
------------------------------ MATCH WORD BOUNDRIES \b | USED LIKE SPAN \b xxxx \b---------------------------------------------------------------
------------------------------ MATCH SLOTS {X}| r"\d{5}" | r"[azAZ]{5}" |  | ---------------------------------------------------------------
------------------------------                  re.findall(r"[azAZ]{5}", text) spits into array
------------------------------                  FULL WORDS r"\b[azAZ]{5}\b", text
------------------------------                  re.findall(r"\w{5,10}", text) words between 5-10 chars
------------------------------                  re.findall(r"\w{5,}", text) min of 5 char
------------------------------                  re.findall(r"s{,10}") words that start with s and 11 chars
------------------------------
------------------------------ CAPTURE GROUPS () | variable= re.search(r"^(\w*), (\w*)$", text))
 Result looks like Lovelace, ada ---------------------------------------------------------------
------------------------------ PRINT GROUPS | print(variable.groups()) ---------------------------------------------------------------------------------------------
('Lovelace', 'ada')
------------------------------ PRINT Entire INDEX GROUPS = 0 | print(result[0]---------------------------------------------------------------
 Lovelace, Ada       
------------------------------ PRINT 1ST INDEX OF GROUPS = 1 | print(result[1]---------------------------------------------------------------
 Lovelace  
------------------------------ PRINT 2ND INDEX GROUPS = 2 | print(result[2]---------------------------------------------------------------
 Ada  
------------------------------ Function example of Groups ---------------------------------------------------------------
>>> def rearrange_name(name):
        result = re.search(r"^(\w*), (\w*)$", name) 
        if result is None:
            return name
        return "{{}".format(result[2], result[1])
>>> rearrange_name("Lovelace, Ada") 
'Ada Lovelace'
>>> rearrange_name("Ritchie, Dennis") 
'Dennis Ritchie'
>>> rearrange_name("Hopper, Grace M.") 
'Hopper, Grace M.
------------------------------ Function example of groups to capture . and - for middle names. ---------------------------------------------------------------
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name) 
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

rearrange_name("Hopper, Grace M.")
'Grace M. Hopper'
------------------------------ NUMERIC REPETITION ---------------------------------------------------------------
------------------------------  ---------------------------------------------------------------
------------------------------  ---------------------------------------------------------------
------------------------------  ---------------------------------------------------------------
------------------------------  ---------------------------------------------------------------






------------------------------ GREP ---------------------------------------------------------------
#example
grep "fruit" /parent/child/

^ = beginning #e.g. grep ^fruit /parent/child #RESULT= fruit, fruit's, fruitcake, etc
$ = end  #e.g. grep fruit$ /parent/child #RESULT= dryfruit, bigfruit's, frozenfruit, etc
. = wildcard #e.g. grep -i "fruit" /parent/child/ #RESULT= FRUIT, FrUIT, fruit
-i = ignore case # e.g.  grep s.ing /usr/file.txt #result will find sting or sling
* = means "any number of this".
.* = therefore means an arbitrary string of arbitrary length.
+ = one or more of the preceding character. (This character is also a modifier, because it must be preceded by another character.)
? = zero or one of the preceding character. (This character is also a modifier, because it must be preceded by another character.)
[ ... ] = a single character that is in the enclosed group of characters; either a list of characters, like [abc], or a range of characters, like [0-9], or both [0-9 ABC w-z]
[^ ... ] = any character except those enclosed in the square brackets, like [^0-9]
| = acts as an OR operator, separating two regular expressions
(  ) = encloses sub-expressions (used for grouping and for the registers variable in the STRMATCH function)
? = meaning that it will stop as soon as it finds a matc
------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------

------------------------------  ---------------------------------------------------------------