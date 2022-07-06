# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6358: Python for Business Analytics
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business 
# University of Central Florida
#
# February 22, 2021
# 
##################################################
#
# Demo for Chapter 10: 
# Part A: Reading and Writing Text Files
#
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory



##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\jo585802\\OneDrive - University of Central Florida\\Documents\\GitHub\\ECO5445\\'
os.chdir(git_path + '\\10-ReadWrite\\file_examples')
# Check that the change was successful.
os.getcwd()



##################################################
## Opening a File
##################################################


# First, let's create a simple file. 
# Create a folder called file_examples. 
# We created a file in a text editor with the following contents
# and save it as file_example.txt.


# First line of text.
# Second line of text.
# Third line of text.


# Now let's read this file. 


file = open('file_example.txt', 'r')
contents = file.read()
file.close()
print(contents)


# This code block makes a connection to the file file_example.txt
# and reads those contents in one string. 
# It closes the connection and prints those contents to screen. 


# First line of text.
# Second line of text.
# Third line of text.


#--------------------------------------------------
### The with Statement
#--------------------------------------------------

# The above method 
# file_1 = open('data/data1.txt', 'r') 
# works, most of the time, but when an error occurs, the program will not execute
# the file.close()command to release the file from memory. 
# If your program throws an error between the openand close
# statements, this file connection will remain in memory, 
# creating a drag on performance. 

# To avoid this problem, use the with statement. 


with open('file_example.txt', 'r') as file: 
    contents = file.read()

print(contents)


# This has the format of any other kind of indented code block, 
# in which the relevant statements are indented beyond the withkeyword. 
# With this approach, if an error occurs, the block terminates and
# the file connection will automatically be released from memory.


##################################################
## Techniques for Reading Files
##################################################

# Once you have made a connection to a file, 
# there are a number of ways to read the contents. 

#--------------------------------------------------
### The read Technique
#--------------------------------------------------

# With the read technique, 
# you read the entire contents of the file into a single string. 

# We used this method above with 


with open('file_example.txt', 'r') as file:
    contents = file.read()

print(contents)


# Clearly, for very large files, this can consume a lot of memory. 
# It is often better to read the contents in smaller chunks. 
# If an integer is passed to read, 
# it will read that specified number of characters. 


with open('file_example.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()

print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)



#--------------------------------------------------
### The readlines Technique
#--------------------------------------------------

# Instead of reading by the character, 
# which may not be a convenient unit to work with, 
# since you might not even know how many characters you need at a time, 
# you can get the contents of the file organized 
# into separate lines with the readlines function.


with open('file_example.txt', 'r') as example_file:
    lines = example_file.readlines()

print(lines)

lines[0]


# It gives a list of strings, each one containing a newline (\n) escape sequence. 

# Now consider the file planets.txt that contains the following text. 


# Mercury
# Venus
# Earth
# Mars

# This code block reads the file, 
# prints the contents in a list and then loops through that list 
# in reverse order using the built-in function reversed. 


with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
planets



for planet in reversed(planets):
    print(planet.strip())



for planet in reversed(planets):
    print(planet)



# You can perform other operations on this list, 
# such as sorting the lines first. 

with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
planets



for planet in sorted(planets):
    print(planet.strip())



#--------------------------------------------------
### The for line in file Technique
#--------------------------------------------------

# Often, it is useful to process the contents of a file
# one line at a time. The for line in filetechnique
# lets you read a file with the functionality of a forloop
# and the efficiency of working with the contents one line at a time. 


with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line))




# This allows you to perform arbitrary calculations using each line in sequence. 
# You can combine any other commands, potentially stripping away whitespace first. 


with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line.strip()))



#--------------------------------------------------
### The readline Technique
#--------------------------------------------------

# Sometimes you want to perform different operations 
# depending on the characteristics of the file. 
# You could use a series of if and elif statements. 
# Instead, you can instruct the python interpreter to 
# read a single line of the file, without following a pattern, 
# using the readline technique. 

# For example, consider the following dataset, contained in
# the file hopedale.txt. 


# Coloured fox fur production, HOPEDALE, Labrador, 1834-1842
# #Source: C. Elton (1942) "Voles, Mice and Lemmings", Oxford Univ. Press
# #Table 17, p.265--266
#       22   
#       29   
#        2   
#       16   
#       12   
#       35   
#        8   
#       83   
#      166   


# Notice that the first line is a description:
# it is a record of the number of fur pelts harvested 
# in a region of Canada over a period of several years during the 1800's. 
# The next two are preceded by a # character
# and the data begin on the fourth line.
# The following code block reads in the data,
# skips over the description in the header, 
# and calculates the total number of fur pelts. 


with open('hopedale.txt', 'r') as hopedale_file:

    # Read and skip the description line.
    hopedale_file.readline()

    # Keep reading and skipping comment lines until we read the first piece
    # of data.
    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()
        # Do nothing because these lines do not have data.

    # Now we have the first piece of data.  
    # Accumulate the total number of pelts.
    # Convert the string to an integer for the first value in the sum.
    total_pelts = int(data)

    # Read the rest of the data.
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())

print("Total number of pelts:", total_pelts)








# We could perform any other calculations with the lines of data, as follows.


with open('hopedale.txt', 'r') as hopedale_file:

    # Read and skip the description line.
    hopedale_file.readline()

    # Keep reading and skipping comment lines until we read the first piece
    # of data.
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()

    # Now we have the first piece of data.
    print(data)

    # Read the rest of the data.
    for data in hopedale_file:
        print(data.rstrip())




# Notice the numbers are aligned
# because we stripped the whitespace only on the right side, 
# using the rstrip() function. 


##################################################
## Files Over the Internet
##################################################

# The above examples assume the file is located on our computer system. 
# You can read file located on any computer that is available on the Internet.

# The urllibmodule has tools for reading files with a given URL.
# Note that the file can be encoded in one of several formats. 
# This example shows how to read a file encoded in a format called UTF-8. 
# This uses a function called decodeto decode the file content 
# in the form of bytes to obtain legible characters using UTF-8 encoding. 



import urllib.request
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)





##################################################
## Writing Files
##################################################

# The with statement can also be used for writing files. 
# Let's move to another directory for writing. 

# git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\QMB6358_Spring_2022\\GitRepo\\QMB6358S22\\'

os.chdir(git_path + '\\10-ReadWrite\\file_examples')
# Check that the change was successful.
os.getcwd()



with open('topics.txt', 'w') as output_file:
    output_file.write('Computer Science')
    


# In the above example, the file topics.txt need not exist:
# this file will be created if it does not exist
# and it will be overwritten if it does exist. 
# The distinction from reading files is shown by the second argument. 
# The 'w' denotes *writing*, while, in the earlier examples, 
# the argument 'r' indicated that the existing file
# would be open for *reading*. 

# If the file already exists and you want to write additional content, 
# you can pass the argument 'a' to *append*. 


with open('topics.txt', 'a') as output_file:
    output_file.write('Software Engineering')



# After running this, look at the contents of the new file:
# You should see

# Computer ScienceSoftware Engineering


# Note that a new line was not automatically added;
# you have to include it manually using \n. 


with open('topics.txt', 'a') as output_file:
    output_file.write('\nSoftware Engineering')

##################################################
# End
##################################################
