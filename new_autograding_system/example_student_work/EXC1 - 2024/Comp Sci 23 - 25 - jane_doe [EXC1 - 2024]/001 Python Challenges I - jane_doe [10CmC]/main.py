'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''




def hello_world():
  ## complete exercise 1 - Hello World - here
  print("Hello World")
  pass
  


def hello_newline_world():
	## complete exercise 2 - Hello [newline] World - here
	print("Hello\nWorld")
	pass


def meet_and_greet():
	name = input("Hello, what's your name?\n")
	print(f"Hello {name}, it's nice to meet you.")
	return name # leave this here!


def name_length(name):  # leave this here!
	length = str(len(name))
	print(f"Did you know you have {length} letters in your name? ")
	pass


def number_adder():
	num1 = int(input("Tell me a number:\n"))
	num2 = int(input("And another:\n"))
	total = str(num1 + num2)
	print(f"I've added them together! The answer is: {total}")
	pass


def in_x_years_time():
	name = input("Hello, who are you?\n")
	age = int(input("How old are you?\n"))
	x_years = str(age + age)
	print(f"OK, {name}, you are {age} years old.")
	print(f"Did you know that in {age} years' time you will be {x_years} years old?")
	pass


def name_repeater():
	first_name = input("What is your first name?\n")
	last_name = input("What is your last name?\n")
	times = int(input("How many times?\n"))
	full_name = (first_name + " " + last_name + " ")
	print((full_name) * times) 
	pass





# this instructs the program to execute each
# of the subroutines, one after the other.
# if you don't want them ALL to run, add a #
# at the start of the line to comment it out.
# to complete the built in Input/Output Tests
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
