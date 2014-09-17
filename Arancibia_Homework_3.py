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
class car_evaluation(object):
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
    root = Tkinter.tk()
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

#write files
def write_cars(cars, lines = None):
    if lines == None:
        car_results = cars
    if lines > 0:
        car_results = cars[0:lines]
    if lines < 0:
        car_results = cars[lines:len(cars)]
    for car in car_results:
        print "Price: %s, Maintenance Cost: %s, Doors: %s, Seats: %s, Cargo Space: %s, Safety Rating: %s, Value: %s." \
              % (car.buying, car.maint, car.doors, car.persons, car.lugboot, car.safety, car.carclass)

#save files using tkinter
def car_evaluation_save(text):
    root = Tkinter.tk()
    open_file = tkFileDialog.asksaveasfile()
    try:
        file_out = open(open_file, mode='w')
        for car in text:
            car_out = "%s, %s, %s, %s, %s, %s, %s\n" \
                      % (car.buying, car.maint, car.doors, car.persons, car.lugboot, car.safety, car.carclass)
            file_out.write(car_out)
        file_out.close()
    except IOError:
        print "No file selected to save to"
        qui()



#sort cars by order
#parameter cars is cars from file
#value is all listed in .self above
#order is ascending or descending
def sorted_cars_params(list_cars, value, sorted_type):
    if sorted_type == "asc":
        return sorted(list_cars, key=attregetter(value+'_sorted_type'))
    elif sorted_type == "desc":
        return sorted(list_cars, key=attrgetter(value+'_sorted_type'), reverse=True)




if __name__ == "__main__":
    list_cars = open_csv()

    #print top 10 rows data sorted by safety descending order
    sort_top_10_safety = sorted_cars_params(list_cars, 'Safety', 'desc')
    print "Top ten rows of cars sorted by safety, descending order:"
    write_cars(sort_top_10_safety, 10)
    print ""

    #print to the console bottom fifteen rows sorted by maint in ascending order
    sort_bottom_fifteen_maint = sorted_cars_params(list_cars, 'Maint', 'asc')
    print "Bottom fifteen rows of car by maint in ascending order"
    write_cars(sort_bottom_fifteen_maint, -15)
    print ""

    #search for cars that have price, maint, safety of high or vhigh
    regex_car_search =[]
    for car in list_cars:
        pattern = "r^v?high$"
        if re.search(pattern, car.buying) and re.search(pattern, car.maint) and re.search(pattern, car.safety):
            regex_car_search.append(car)
    regex_car_search = sorted_cars_params(regex_car_search, "doors", "asc")
    print "Cars by price, maint, and safety are high or vhigh, sorted in ascending order"
    write_cars(regex_car_search)
    print ""

    #Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more
    regex_car_search2 =[]
    for car in list_cars:
        if car.buying == "vhigh" and car.maint == "med" and car.doors == "4" and (car.persons =='4' or car.persons == 'more'):
            regex_car_search2.append(car)


    car_evaluation_save(regex_car_search2)

















