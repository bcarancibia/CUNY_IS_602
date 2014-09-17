# Benjamin Arancibia
# 9/17/2014
#Homework 3

#Load data from cars.data.csv and then run following operations
#print top ten rows of the data sorted by safety descending order
#print to the console bottom fifteen rows sorted by maint in ascending order
#print console all rows are high or vhigh in fields 'buying', 'buying', 'maint', 'safety', sorted by 'doors' asc order
#user regular expressions.
#save to a file all rows

#import packages and modules
import re
from Tkinter import *
import tkFileDialog
from operator import attregetter
import csv
import os



#define simple class that represents car evaluation
class car_evaluation(object)
    def __init__(self, Buying, Maint, Doors, Persons, LugBoot, Safety, CarClass):
        #added a in front of self args because got confused with try beneath the self...
        aBuying = {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3}
        aMaint = {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3}
        aDoors = {'2': 0, '3': 1, '4': 2, '5more': 3}
        aPersons = {'2': 0, '4': 1, 'more': 2}
        aLugBoot = {'small': 0, 'med': 1, 'big': 2}
        aSafety = {'low': 0, 'med': 1, 'high': 3}
        aCarClass = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
        self.buying = Buying
        self.maint = Maint
        self.doors = Doors
        self.persons = Persons
        self.lugboot = LugBoot
        self.safety = Safety
        self.carclass = CarClass
        try:
            self.buying_ord = aBuying[Buying]
            self.maint_ord = aMaint[Maint]
            self.doors_ord = aDoors[Doors]
            self.persons_ord = aPersons[Persons]
            self.lugboot_ord = aLugBoot[LugBoot]
            self.safety_ord = aSafety[Safety]
            self.carclass_ord = aCarClass[CarClass]
        except:
            self.buying_ord = None
            self.maint_ord = None
            self.doors_ord = None
            self.persons_ord = None
            self.lugboot_ord = None
            self.safety_ord = None
            self.carclass_ord = None
            print 'The line %s, %s, %s, %s, %s, %s, %s contains errors' % (price, maint, doors, seats, cargo, safety, value)
            pass


#import dialogue box from tkinter

def open_csv():
    root = Tk()
    open_file = tkFileDialog.askopenfile(mode='r')
    try:
        list_cars = []
        for line in open_file:
            car_data = line.strip("\n").split(",")
            c = car_evaluation(*car_data)
            list_cars.append(c)
    except IOError:
        print "This file does not exist or cannot be imported, please try again."
    except TypeError:
        print "This file has errors, please try again"
    return list_cars

#sort cars by order
#parameter cars is cars from file
#value is all listed in .self above
#order is ascending or descending
def sorted_cars_by_parameters(list_cars, value, sorted_type):
    if sorted_type == "asc":
        return sorted(list_cars, key=attregetter(value+'_sorted_type'))
    else
        return sorted(list_cars, key=attrgetter(value+'_sorted_type'), reverse=True)

if __name__ == "__main__":
    list_cars = open_csv()

#print top 10 rows data sorted by safety descending order





