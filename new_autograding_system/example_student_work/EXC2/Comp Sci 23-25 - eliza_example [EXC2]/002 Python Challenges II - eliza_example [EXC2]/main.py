'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''


def old_enough_to_drive():
  age = int(input("How old are you then?"))
  if age >= 18:
    print("Old enough to drive!")
  else:
    print("Too young to drive.")
  pass


def grade_calculator():
  mark = int(input("Enter mark:\n"))
  if mark >= 87:
    print("That's a grade A*.")
  elif mark >= 77:
    print("That's a grade A.")
  elif mark >= 70:
    print("That's a grade B.")
  elif mark >= 63:
    print("That's a grade C.")
  elif mark >= 57:
    print("That's a grade D.")
  elif mark >= 50:
    print("That's a grade E.")
  pass


def leap_year():
  year = int(input("What year?\n"))
  if year % 400 == 0:
    print("That one's a leap year!")
  if year / 100 == 1 or year % 400 != 0:
    print("Not a leap year")
  else:
    print("Not a leap year")
  pass


def financial_adviser():
  cash = float(input("How much is in the bank? £\n"))
  if cash >= 1000000000:
    print("You're a billionaire!")
  elif cash >= 1000000:
    print("You're a millionaire!")
  elif cash >= 100:
    print("Living comfortably.")
  elif cash >= 0.70:
    print("Barely enough for a packet of crisps!")
  elif cash <= 0.70:
    print("No crisps for you!")
  pass


def name_length_comparison():
  fore = input("What's your forename?\n")
  sur = input("What's your surname?\n")
  lenf = len(fore)
  lens = len(sur)
  if lenf - lens == 1:
    print("Your forename is longer by 1 character.")
    if lens - lenf == 1:
      print("Your surname is longer by 1 character.")
  if lenf >= lens and lenf - lens != 1:
    dif = lenf - lens
    print(f"Your forename is longer by {dif} characters.")
  elif lens >= lenf and lens - lenf != 1:
    dif = lens - lenf
    print(f"Your surname is longer by {dif} characters.")
    pass


def username_validator():
  user = input("Enter username:\n")
  if user[0] == "X":
    if len(user) > 10 and len(user) < 18:
      if " " in user:
        print("Invalid. Try again")
      else:
        print("Valid. Username accepted")
    else:
      print("Invalid. Try again")
  else:
    print("Invalid. Try again")
  pass


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
  [
    old_enough_to_drive, grade_calculator, leap_year, financial_adviser,
    name_length_comparison, username_validator
  ][int(x) - 1]()
