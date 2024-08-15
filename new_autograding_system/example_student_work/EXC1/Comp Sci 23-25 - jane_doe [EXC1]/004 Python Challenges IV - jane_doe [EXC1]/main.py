'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''



def credentials():
	username = ""
	password = ""
  
	while username != "TheresaMay123" or password != "abcdef":
		username = input("Enter username:\n")
		password = input("Enter password:\n")
		if username != "TheresaMay123" or password != "abcdef":
			print("INCORRECT CREDENTIALS.")
		
	print("CORRECT CREDENTIALS.")
	print("Welcome to the system.")
	pass

def enough():
	enough = "no"
	count = 5
	while enough != "enough" and count > 0:
		enough = input("Have you had enough?\n").lower()
		count -= 1
	print("You've had enough.")
	pass

def countdown():
	num = 100
	takeaway = int(input("Enter number:\n"))
	print("100")
	while num > takeaway:
		num -= takeaway
		print(num)
	print("FINISHED")
	pass

def confirmation_attempts():
	password = ""
	password2 = "1"
	attempts = 4
	valid = False
	
	while password != password2 and attempts != 0:
		password = input("Enter password:\n")
		password2 = input("Enter password again:\n")
		if password != password2 and attempts != 0:
			if attempts > 1:
				print("Password match not found.")
			attempts -= 1
			if attempts > 1:
				print(f"You have {attempts} attempts remaining. ")
			elif attempts == 1:
				print(f"You have {attempts} attempt remaining. ")
		else:
			print("ACCOUNT CREATED")
			
	if attempts == 0:
		print("ACCOUNT LOCKED")
	pass

def guess_my_number():
	num = ""
	magic_num = 66
	guesses = 10
	valid = False
	while valid == False and guesses > 0:
		checkpoints = [10, 7, 4]
		if guesses in checkpoints:
			print(f"You have {guesses} guesses remaining.")
		elif guesses == 1:
			print(f"You have 1 guess remaining.")
		num = int(input("What's my magic number?\n"))
		if num > 60 and num < 72 and num != 66:
			print("really close!")
			guesses -= 1
		if num > 66:
			print("LOWER!")
			guesses -= 1
		if num < 66:
			print("HIGHER!")
			guesses -= 1
		if num == 66:
			print("You guessed it!")
			valid = True
	print("You lose.")
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