#################################################################

def settled_in():
	## All of your code for the first task goes here
	pass

#################################################################

def order_bot():
	## All of your code for the second task goes here
	pass

#################################################################

def string_game():
	## All of your code for the third task goes here
	pass

#################################################################

def name_rater():
	## All of your code for the fourth task goes here	
	pass










#### leave this block of code - don't change it!
##########################################################################

print("""Enter 1 to test SETTLED IN
Enter 2 to test ORDER BOT
Enter 3 to test STRING GAME
Enter 4 to test NAME RATER""")
x = input()
subs = {"1":settled_in, "2":order_bot, "3":string_game, "4":name_rater}
if x in subs:
	subs[x]()

##########################################################################