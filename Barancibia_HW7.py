# Benjamin Arancibia
# 10/20/2014
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
import re
import numpy as np
from scipy.optimize import curve_fit


def scipy():
    values = []
    with open('/Users/bcarancibia/CUNY_IS_602/brainandbody.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            values.append(row)
    # Quick header remover:
    values.pop(0)
    # Converting strings to numbers:
    brain = []
    body = []
    for i in range(len(values)):
        body.append(float(values[i][1]))
        brain.append(float(values[i][2]))

    def slope_func(x, a, b):
        return a * x + b

    popt, pcov = curve_fit(slope_func, body, brain)
    print  "body = " + str(popt[0]) + " * brain + " + str(popt[1])


#HOMEWORK 5 CODE

def original():
    values = []
    with open('/Users/bcarancibia/CUNY_IS_602/brainandbody.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            values.append(row)
    values.pop(0) #remove header
    brain = []
    body = []
    for i in range(len(values)):
        values[i][1] = float(values[i][1])
        values[i][2] = float(values[i][2])
    bodymean = 0
    brainmean = 0

    #means
    for i in range(len(values)):
        bodymean += values[i][1]
        brainmean += values[i][2]
    bodymean = bodymean/float(len(values))
    brainmean = brainmean/float(len(values))

    meandistance = 0
    mse = 0

    #future reference how i got formulas: http://en.wikiversity.org/wiki/Least-Squares_Method
    for i in range(len(values)):
        meandistance += (values[i][1] - bodymean) * (values[i][2] - brainmean)
        mse += (values[i][1] - bodymean) * (values[i][1]-bodymean)
    slope = meandistance/mse
    constant = brainmean - (slope * bodymean)

    print "body = " + str(slope) + " x(brain) + " + str(constant)


if __name__ == "__main__":
    import timeit as ti
    print "5 iterations to test speed\n\n"
    print "Scipy: " + str(ti.timeit("scipy()", setup="from __main__ import scipy", number=5))
    print "Original: " + str(ti.timeit("original()", "from __main__ import original", number=5))