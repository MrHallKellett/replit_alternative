### Due to the way the new replit Teams system handles unit tests...
### you cannot use input(prompt) ####################################
#####################################################################
### instead please use: #############################################
### print(prompt) ###################################################
### answer = input()  ###############################################
### on two separate lines. ##########################################
#####################################################################



# CONSTANTS
OPTIONS = '''Press 1 to set your secret number.
Press 2 to set your name.
Press 3 to set your age.
Press 4 to set your verification code.
Press 5 to set your username.
Press 6 to set your password.
Press 7 to set and confirm your password.
Press 8 to compare two strings.
Press 9 to quit.'''

# variables
usernames = ["powerRanger987", "avengers-fan-123", "xX_aViD_FroG_Collector_Xx"]

def task_1():

	pass

def task_2():
	
	pass

def task_3():

	pass

def task_4():

	pass

def task_5():

	pass

def task_6():

	pass

def task_7():

	pass

### EXTENSION

def task_8():

	pass

## you will need to complete task_9 in a separate repl / offline program.


##############################

def menu():
	option = "0"

	while option != "9":
		
		print(OPTIONS)
		option = input()
	
		if option == '1':
			secret_number = task_1()
		elif option == '2':
			name = task_2()
		elif option == '3':
			age = task_3()
		elif option == '4':
			verification_code = task_4()
		elif option == '5':
			usernames = task_5(usernames)
		elif option == '6':
			password = task_6()
		elif option == '7':
			task_7()
		elif option == '8':
			similarity_rating = task_8()
		elif option == "9":
			print("bye!")
		else:	
			print("Invalid choice.")


if __name__ == "__main__":

	menu()