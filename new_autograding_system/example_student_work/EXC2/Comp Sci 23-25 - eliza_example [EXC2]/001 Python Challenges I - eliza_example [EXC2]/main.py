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
  print("Hello " + name + ", it's nice to meet you.")
  return name # leave this here!

def name_length(name):  # leave this here!
  length = str(len(name))
  print(f"Did you know you have {length} letters in your name?")
  pass

def number_adder():
  ## complete exercise 5 - Number Adder - here
  num1 = int(input("Tell me a number:\n"))
  num2 = int(input("And another:\n"))
  add = str(num1 + num2)
  print(f"I've added them together! The answer is: {add}")
  
  pass

def in_x_years_time():
  ## complete exercise 6 - "In X years' time..." - here
  who = input("Hello, who are you?\n")
  age = int(input("How old are you?\n"))
  fut = str(age+age)
  print(f"OK, {who}, you are {age} years old.")
  print(f"Did you know that in {age} years' time you will be {fut} years old?")
  
  pass

def name_repeater():
  ## complete exercise 7 - Name Repeater - here
  fname = input("What is your first name?\n")
  lname = input("What is your last name?\n")
  time = int(input("How many times?\n"))
  fulname = (fname + " " + lname + " ")
  print(fulname * time)
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