#Benjamin Arancibia
#10/20/2014
#Homework Week 7

'''
Take what you did on homework 5 as a starting point (using any of the provided datasets).  
Replace the regression calculation using least squares with a curve fitting approach (examples in the reading).  
To start, just fit a linear equation.  Output the equation to the console.  
You don't need to graph anything (we'll look at that in a couple more weeks).

Homework 5 instructions:

#Load in the .csv and then perform a linear regression using the least squares method
#on the relationship of brain weight [br] to body weight [bo].
#looking for a model in the form bo = X * br + Y.
#Find values for X and Y and print out the entire model to the console.

'''

import csv
from timeit import timeit
import numpy as np
from scipy.optimize import curve_fit

def scipys():
	values = []
	with open('/Users/bcarancibia/CUNY_IS_602/brainandbody.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		for row in reader:
    		values.append(row)
    
    values.pop(0) #remove header