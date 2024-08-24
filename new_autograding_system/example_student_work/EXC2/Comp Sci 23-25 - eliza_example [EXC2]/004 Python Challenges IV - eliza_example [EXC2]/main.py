'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''



def credentials():
  user = input("Enter username:\n")
  passw = input("Enter password:\n")

  while user != "TheresaMay123" and passw != "abcdef":
    print("INCORRECT CREDENTIALS.")
    user = input("Enter username:\n")
    passw = input("Enter password:\n")

  print("CORRECT CREDENTIALS.\nWelcome to the system.")

  pass

def enough():

  enough = input("Have you had enough?\n")
  no = 0

  while enough != "ENOUGH" and no < 4:
    no += 1
    enough = input("Have you had enough?\n")

  print("You've had enough.")
  
	
  
  pass

def countdown():

  num = int(input("Enter number:\n"))
  orig = 100

  while orig > num:
    
    orig -= num
    print(orig)
  
  print("FINISHED")
  pass

def confirmation_attempts():
	## complete exercise 4 - Confirmation Attempts - here
	pass

def guess_my_number():
	## complete exercise 5 - Guess My Number - here
	pass








#### leave this block of code - don't change it!
##########################################################################

print("""Enter 1 to test CREDENTIALS
Enter 2 to test ENOUGH
Enter 3 to test COUNTDOWN
Enter 4 to test CONFIRMATION ATTEMPTS
Enter 5 to test GUESS MY NUMBER""")
x = input()
subs = {"1":credentials, "2":enough, "3":countdown, "4":confirmation_attempts, "5":guess_my_number}
if x in subs:
	subs[x]()

##########################################################################