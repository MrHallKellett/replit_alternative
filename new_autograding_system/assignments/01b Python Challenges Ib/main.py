'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''




def leet_speak():
	## complete exercise 1 - L33t sp34k - here
	pass

def banner():
	## complete exercise 2 - Banner - here
	pass


def grid():
	## complete exercise 3 - Grid - here
	pass





### leave this code here


x = input("""Enter 1 to test L33T SP34K
Enter 2 to test BANNER
Enter 3 to test GRID""")
try:
        [leet_speak, banner, grid][int(x-1)]()
except:
        pass
