# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6358: Python for Business Analytics
#
# Linear Algebra in Python
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
#
# January 19, 2021
#
##################################################
"""



##################################################
# Import Modules.
##################################################

# Module os to interact with the operating system, 
# e.g. set the working directory. 
import os

# Module numpy for numerical methods in Python, 
# e.g. to use linear algebra.
import numpy as np



##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
# os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\QMB6358_Spring_2022\\GitRepo\\QMB6358S22\\demo_08_PP_Ch_06_Using_Modules')
os.chdir('C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\GitHub\\QMB6358S22\\demo_08_PP_Ch_06_Using_Modules')
# Check that the change was successful.
os.getcwd()



##################################################
# Examples Using Numpy.
##################################################

# Some programming languages are designed for matrix algebra. 
# For example, when you use the statistical programming language ```R```,
# the matrix multiplication operator is the symbol ```%*%```. 

# Python operates on vectors and matrices differently. 
# It thinks of them as parameters in a function, 
# such as the dot function in the numpy module. 

# Assign numbers to two numpy arrays.
A = np.array([[1., 2., 3.], [4., 5., 6.]])
x = np.array([[10., 11.], [20., 21.], [30., 31.]])

# Multiply these matrices together. 
b = A.dot(x)
print(b)

# These numpy arrays have their own type. 
type(A)

type(x)

type(b)


# To extract values from the array, you can extract elements
# just as you would for a list.

A[1]

A[1][2]

# Since these numpy arrays are 2-dimensional objects,
# you can also extract the elements by passing a 
# list of index numbers. 
A[1, 2]

# Now that we know how to perform matrix multiplication, 
# we can use it to solve for the unknown vector or matrix 
# x that produced the product b.


#--------------------------------------------------
# Solve a linear system with the inverse matrix
#--------------------------------------------------

# The conceptually simple--but computationally expensive--approach 
# is to calculate the inverse of the matrix ```A``` 
# and then multiply ```b``` to achieve the solution ```b```. 


# Assign numbers to two numpy arrays.
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 1.])


# Use the np.linalg.inv method to find the inverse.
A_inv = np.linalg.inv(A)
A_inv

# Verify that A_inv is the inverse of A.
A.dot(A_inv)

A_inv.dot(A)

# Since both of these products (approximately) equal the identity matrix, 
# A_inv is the inverse of A. 

# Notice that the off-diagonal elements are not exactly zero.
# Rounding errors occur when using numbers with finite precision. 

# Now use this inverse to find the solution by multiplying
# the vector b by the inverse of A.
x_soln = A_inv.dot(b)
print(x_soln)

# Verify the solution by calculating the multiplication with the solution:
A.dot(x_soln)
# which is the same as b.


#--------------------------------------------------
# Solve a linear system without the inverse
#--------------------------------------------------



# Use the solve method to find a solution x to the system
# of the form A*x = b
soln = np.linalg.solve(A, b)
soln

# Check the solution
A.dot(soln)
# equals b, so soln is truly the solution. 




#--------------------------------------------------
# Functions for creating arrays 
#--------------------------------------------------

# There exist several convenient functions 
# for generating matrices of a specific form. 

# Create an array of zeros.
a = np.zeros((2,2))   
print(a)

# Create an array of ones.
b = np.ones((1,2))
print(b)

# Create a constant array. 
c = np.full((2,2), 7)
print(c)

# Create a 2x2 identity matrix. 
d = np.eye(2)
print(d)

# Create an array filled with random values.
e = np.random.random((2,2))
print(e)

# These are often useful for solving algebra problems, 
# since the syntax matches the symbols often used 
# on the blackboard.


##################################################
# End.
##################################################
