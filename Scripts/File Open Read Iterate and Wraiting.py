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



