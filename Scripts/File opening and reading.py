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