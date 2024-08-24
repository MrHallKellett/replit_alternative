def Exercise1():
    colours = ["red", "blue", "green", "yellow", "purple"]
    return colours

def Exercise2():
    house = [
        ["red", "blue", "green"]
        ["yellow", "orange", "purple"]
        ["pink", "brown", "gray"] 
         ]
    return house 
def Exercise3(house): 
    print("(a) The first colour of the third room., b) The last colour of the last room.(c) The third letter of the second colour of the first room.")

def Exercise4():
    house = Exercise2()
    for room in house:
        for color in room:
            print(.ljust(n))


def Exercise5(house):
    for room in house:
        for colour in room:
            if len(colour) > 4:
                print(colour, end=",")

def Exercise6():
    Exercise2()  

    colours = Exercise1()
    house = Exercise2()
    Exercise3()
    Exercise4()
    Exercise5()
    Exercise6()
    

Exercise8()
Business:
     def __init__(self, manager, industry, years_active, annual_turnover, is_private_company):
        self.manager = manager
        self.industry = industry
        self.years_active = years_active
        self.annual_turnover = annual_turnover
        self.is_private_company = is_private_company

HugePharmaLTD = 