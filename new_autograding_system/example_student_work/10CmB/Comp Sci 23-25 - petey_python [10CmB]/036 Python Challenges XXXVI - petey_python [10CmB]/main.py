def Exercise1():
    colours = ["cloud", "slate", "concrete", "silver", "cement"]
    return colours

def Exercise2():
    house = [["navy", "ultramarine", "cobalt", "teal", "cyan"],["ruby", "magenta", "cardinal", "amaranth", "blood"], ["cloud", "slate", "concrete", "silver", "cement"]]
    return house

def Exercise3(house):
   print("The first colour of the third room is {}".format(house[2][0]))
   print("The last colour of the last room is {}".format(house[-1][-1]))
   print("The third letter of the second colour of the first room is {}".format(house[0][1][2])) 

def Exercise4(house):
    for room in house:
        for colour in room:
            print(colour.ljust(15), end=" ")
        print()

def Exercise5(house):
    for room in house:
        for colour in room:
            if len(colour) > 4:
                print(colour, end= ", ")
        print()
    print(list)

def Exercise6(house):      
    for i in range(0, 3):
        print(house[i][i])

class Business:
    def _init_(self):
        self.manager = "bob"
        self.industry = "coffee"
        self.years_active = 3
        self.annual_turnover = 100000.000
        self.is_private_company = True

def Exercise8():
    business1 = Business()
    business2 = Business()

    business1.manager = "Chuck Bloddington"
    business1.industry = "biomedical research indsutry"
    business1.years_active = 1
    business1.annual_turnover = 23200000
    business1.is_private_company = False

    business2.manager = "Pakpao Thaksin Mongkut Sukhon"
    business2.industry = "catering"
    business2.years_active = 10
    business2.annual_turnover = 10200000000
    business2.is_private_company = True

    return business1, business2


house = Exercise2()
Exercise1()
Exercise2()
Exercise3(house)
Exercise4(house)
Exercise5(house)
Exercise6(house)
