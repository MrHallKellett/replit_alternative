'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''


def hello_world():
	"""complete exercise 1 - Hello World - here"""

def hello_newline_world():
	"""complete exercise 2 - Hello [newline] World - here"""

def meet_and_greet():
	"""complete exercise 3 - Meet and Greet - here"""
	name = ""
	# your code here
	return name # leave this at the end!

def name_length(name):  # leave this here!
	"""complete exercise 4 - Name Length - here"""	

def number_adder():
	"""complete exercise 5 - Number Adder - here"""	

def in_x_years_time():
	"""complete exercise 6 - "In X years' time..." - here"""	

def name_repeater():
	"""complete exercise 7 - Name Repeater - here"""
	




# this instructs the program to execute each
# of the subroutines, one after the other.
# if you don't want them ALL to run, add a #
# at the start of the line to comment it out.
# however, to pass the autograding tests,
# you will need them to execute in this order:

hello_world()
hello_newline_world()
name = meet_and_greet() # *
name_length(name) # **
number_adder()
in_x_years_time()
name_repeater()


# * meet_and_greet() is a special type of subroutine called a FUNCTION. we will study these in more detail soon!
# ** the value from the meet_and_greet() function is returned and then passed into the name_length() procedure.

