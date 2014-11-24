from operator import itemgetter, attrgetter
# 1. fill in this class
# it will need to provide for what happens below in the
# main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# a function called showEvaluation, and an attribute carCount
class CarEvaluation:
    'A simple class that represents a car evaluation'
    carCount = 0

    def __init__(self, Brand, Price, Safety_Rating):
        self.Brand = Brand
        self.Price = Price
        self.Safety_Rating = Safety_Rating
        CarEvaluation.carCount += 1

    def displaycarCount(self):
        return "Car Count = %d" % CarEvaluation.carCount

    def showEvaluation(self):
        print "The", self.Brand, "has a", self.Price, "and it's safety is rated a", self.Safety_Rating, "."

# 2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
# 	otherwise by descending price
#you fill in the rest

def sortbyprice(input, order):
    high = []
    med = []
    low = []
    for input in input:
        if input.Price == "High":
            high.append(input.Brand)
        elif input.Price == "Med":
            med.append(input.Brand)
        else:
            low.append(input.Brand)
    if order == "des":
        return high + med + low
    else:
        return low + med + high





#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
#   you fill in the rest
def searchforsafety(input, safeValue):
    for input in input:
        if(input.Safety_Rating == safeValue):
            return True
        else:
            return False


# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount  # Car Count = 3

    eval1.showEvaluation()  #The Ford has a High price and it's safety is rated a 2
    eval2.showEvaluation()  #The GMC has a Med price and it's safety is rated a 4
    eval3.showEvaluation()  #The Toyota has a Low price and it's safety is rated a 3

    L = [eval1, eval2, eval3]

    print sortbyprice(L, "asc");  #[Toyota, GMC, Ford]
    print sortbyprice(L, "des");  #[Ford, GMC, Toyota]
    print searchforsafety(L, 2);  #true
    print searchforsafety(L, 1);  #false