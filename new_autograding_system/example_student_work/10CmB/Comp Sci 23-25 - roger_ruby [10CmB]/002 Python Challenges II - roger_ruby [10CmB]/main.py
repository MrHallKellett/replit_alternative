'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''



def old_enough_to_drive():
  ## complete exercise 1 - Are You Old Enough To Drive? - here
  age = int(input("How old are you then?\n"))
  if age >= 18:
    print ("Old enough to drive!\n") 
  else:
    print("Too young to drive.\n")

def grade_calculator():
  ## complete exercise 2 - Grade Calculator - here
  grade_mark = int(input("Enter mark:\n"))
  if grade_mark > 100:
    print("ERROR")
  elif grade_mark >= 87:
    print ("That's a grade A*.")
  elif grade_mark >= 77 :
    print("That's a grade A.")
  elif grade_mark >= 70 :
    print("That's a grade B.")
  elif grade_mark >= 63:
    print("That's a grade C.")
  elif grade_mark>=57:
    print("That's a grade D.")
  elif grade_mark<50:
    print("That's a grade F.")
  else:
    print("That's a grade E.")

def leap_year():
  ## complete exercise 3 - Is It A Leap Year? - here
  year = int(input("What year?\n"))
  if year == 0:
    print("Invalid input year.")
  elif year % 4 == 0 and year % 100 != 0:
    print("That one's a leap year!")
  elif year % 400 == 0:
      print("That one's a leap year!")
  else: 
    print("Not a leap year")
  
def financial_adviser():
  ## complete exercise 4 - Financial Adviser - here
  bank_money = float(input("How much is in the bank? £\n"))
  if bank_money < 0.70:
    print ("No crisps for you!")
  elif 100 > bank_money >= 0.70:
    print("Barely enough for a packet of crisps!")
  elif  1000000 > bank_money >= 100:
    print("Living comfortably.")
  elif 1000000000> bank_money >= 1000000:
    print("You're a millionaire!")
  else:
    print("You're a billionaire!")

def name_length_comparison():
  ## complete exercise 5 - Name Length Comparison - here
  name_1 = str(input("What's your forename?\n"))
  name_2= str(input("What's your surname?\n"))
  longer_forename = str((len(name_1) - len(name_2)))
  longer_surname = str((len(name_2)- len(name_1)))
  if len(name_1) > len(name_2):
    if longer_forename != "1":
      print("Your forename is longer by " + longer_forename + " characters.")
    elif longer_forename == "1":
      print("Your forename is longer by " + longer_forename + " character.")
  elif len(name_2) > len(name_1):
    if longer_surname == "1":
      print("Your surname is longer by " + longer_surname + " character.")
    elif longer_surname != "1":
      print("Your surname is longer by " + longer_surname + " characters.")
  elif len(name_1) == len(name_2):
    print("Both your names are of equal length.")

def username_validator():
  ## complete exercise 6 - Username Validator - here
  username = str(input("Enter username: \n"))
  if (10 <= len(username) <= 18) and (username[0] == "X") and ((" " in username) == False):
    print("Valid. Username accepted")
  else:
    print("Invalid. Try again")
  


#####################################################################

# leave this block of code as it is!
  



print('''Enter 1 to test OLD ENOUGH TO DRIVE
Enter 2 to test GRADE CALCULATOR
Enter 3 to test LEAP YEAR
Enter 4 to test FINANCIAL ADVISER
Enter 5 to test NAME LENGTH COMPARISON
Enter 6 to test USERNAME VALIDATOR''')

x = input()
if x in "123456":
  [old_enough_to_drive,
  grade_calculator,
  leap_year,
  financial_adviser,
  name_length_comparison,
  username_validator][int(x)-1]()
