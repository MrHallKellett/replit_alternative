'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''

print("Running this one")


def hello_world():
	"""complete exercise 1 - Hello World - here"""
	print("Hello World")

def hello_newline_world():
	"""complete exercise 2 - Hello [newline] World - here"""
	print("Hello\nWorld")
def meet_and_greet():
	"""complete exercise 3 - Meet and Greet - here"""
	name = None
	print("Hello, what's your name?")
	name = input()
	print(f"Hello {name}, it's nice to meet you.")
	return name # leave this at the end!

def name_length(name):  # leave this here!
	"""complete exercise 4 - Name Length - here"""
	print(f"Did you know you have {len(name)} letters in your name?")

def number_adder():
	"""complete exercise 5 - Number Adder - here"""
	num1 = int(input("Tell me a number: "))
	num2 = int(input("And another: "))
	print(f"I've added them together! The answer is: {num1 + num2}")

def in_x_years_time():
	"""complete exercise 6 - "In X years' time..." - here"""
	print("Hello, who are you?")
	who = input()
	print("How old are you?")
	age = int(input())
	print(f"OK, {who}, you are {age} years old.")
	print(f"Did you know that in {age} years' time you will be {age+age} years old?")

def name_repeater():
	"""complete exercise 7 - Name Repeater - here"""
	forename = input("What is your first name?\n")
	lastname = input("What is your last name?\n")
	times = int(input("How many times?\n"))
	print((forename + " " + lastname + " ") * times)
	




	
hello_world()
hello_newline_world()
name = meet_and_greet() # *
name_length(name) # **
number_adder()
in_x_years_time()
name_repeater()


# * meet_and_greet() is a special type of subroutine called a FUNCTION. we will study these in more detail soon!
# ** the value from the meet_and_greet() function is returned and then passed into the name_length() procedure.

