'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''



def old_enough_to_drive():
	## complete exercise 1 - Are You Old Enough To Drive? - here
	pass

def grade_calculator():
	## complete exercise 2 - Grade Calculator - here
	pass

def leap_year():
	## complete exercise 3 - Is It A Leap Year? - here
	pass

def financial_adviser():
	## complete exercise 4 - Financial Adviser - here
	pass

def name_length_comparison():
	## complete exercise 5 - Name Length Comparison - here
	pass

def username_validator():
	## complete exercise 6 - Username Validator - here
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
