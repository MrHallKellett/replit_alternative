'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''



def old_enough_to_drive():
	age = int(input("How old are you then?\n"))
	if age >= 18:
		print("Old enough to drive!")
	else:
		print("Too young to drive.")
	pass

def grade_calculator():
	mark = int(input("Enter mark:\n"))
	if mark >= 101:
		print("ERROR")
	elif mark >= 87:
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
	else:
		print("That's a grade F.")
	pass

def leap_year():
	year = int(input("What year?\n"))
	if year == 0:
		print("Invalid input year.")
	elif year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print("That one's a leap year!")
			else:
				print("Not a leap year")
		else:
			print("That one's a leap year!")
	else:
		print("Not a leap year")
	pass
  
def financial_adviser():
	money = float(input("How much is in the bank? £\n"))
	if money < 0.7:
		print("No crisps for you!")
	elif money < 100:
		print("Barely enough for a packet of crisps!")
	elif money >= 1000000000:
		print("You're a billionaire!")
	elif money >= 1000000:
		print("You're a millionaire!")
	elif money >= 100:
		print("Living comfortably.")
	pass

def name_length_comparison():
	forename = input("What's your forename?\n")
	surname = input("What's your surname?\n")
	forlen = len(forename)
	surlen = len(surname)
	if forlen - surlen == 1:
		print("Your forename is longer by 1 character.")
	elif surlen - forlen == 1:
		print("Your surname is longer by 1 character.")
	elif forlen > surlen:
		difference = forlen - surlen
		print(f"Your forename is longer by {difference} characters.")
	elif surlen > forlen:
		difference = surlen - forlen
		print(f"Your surname is longer by {difference} characters.")
	else:
		print("Both your names are of equal length.")
	pass

def username_validator():
	user = input("Enter username:\n")
	if user[0] == "X":
		if len(user) >= 10 and len(user) <= 18:
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
	[old_enough_to_drive,
	grade_calculator,
	leap_year,
	financial_adviser,
	name_length_comparison,
	username_validator][int(x)-1]()

