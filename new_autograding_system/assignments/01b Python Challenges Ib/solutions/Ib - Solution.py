'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''




def leet_speak():
	## complete exercise 1 - L33t sp34k - here
	p = list("this is how all the cool people on the internet talk".replace(" ", ""))

	c = "t,|-|,!,s,!,s,|-|,0,w,4,7,7,t,|-|,3,c,0,0,7,p,3,0,p,7,3,0,n,t,|-|,3,!,n,t,3,r,n,3,t,t,4,7,|<".split(',')

	convert = dict(zip(p, c))

	sentence = input("Say something:\n")

	for s in sentence:
		if s in convert:
			print(convert[s], end="")
		else:
			print(s, end="")
	print()

def banner():
	## complete exercise 2 - Banner - here
	n = input("Who are you?\n")

	x = len(n)

	print("-" * x, end="")
	print("=" * (x+4), end="")
	print("-" * x)
	print("-" * (x-2), end="")
	print("/ " * 2, end="")
	print(n.upper(), end="")
	print(" \\" * 2, end="")
	print("-" * (x-2))
	print("-" * x, end="")
	print("=" * (x+4), end="")
	print("-" * x)


def grid():
	## complete exercise 3 - Grid - here
	n = int(input("What size grid?\n"))
	for i in range((n//2)-1):
		s = ("*-" * n)
		print(s[:-1])
		s = ("| " * n)
		print(s.strip())
	s = ("*-" * n)
	print(s[:-1])



if __name__ == "__main__":
	# this instructs the program to execute each
	# of the subroutines, one after the other.
	# if you don't want them ALL to run, add a #
	# at the start of the line to comment it out.
	# to complete the built in Input/Output Tests
	# you will need them to execute in this order:
	
	leet_speak()
	banner()
	grid()
