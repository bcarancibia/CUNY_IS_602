"""
Benjamin Arancibia
Week 5 Assignment
October 8th, 2014
"""

"""
Load in the .csv and then perform a linear regression using the least squares method
on the relationship of brain weight [br] to body weight [bo].
looking for a model in the form bo = X * br + Y.
Find values for X and Y and print out the entire model to the console.
"""

import csv
import re
values = []

with open('/Users/bcarancibia/CUNY_IS_602/brainandbody.csv', 'rb') as csv:
  reader = csv.reader(csv, delimiter=",")
  for row in reader:
    values.append(row)

values.pop(0) #remove header

for i in range(len(values)):
  values[i][1] = float(values[i][1])
  values[i][2] = float(values[i][2])

bodymean = 0
brainmean = 0

#means
for i in range(len(values)):
  bodymean += vals[i][1]
  brainmean += vals[i][2]
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

print "body = " + str(slope) + " * brain + " + str(constant)
