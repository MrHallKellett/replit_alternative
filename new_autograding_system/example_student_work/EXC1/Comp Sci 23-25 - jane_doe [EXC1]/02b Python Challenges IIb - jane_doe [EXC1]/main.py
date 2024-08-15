'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''




def age_rater():
	print("Age Rater\n")
	age = int(input("How old are you then\n"))
	if age >= 100:
		print("Centenarian!")
	if age >= 40:
		print("Over the hill!")
	if age >= 25:
		print("A quarter century!")
	if age > 16:
		print("Old enough to drive!")
	if age > 1:
		print("First word!")
	
	pass

def even_or_odd():
	print("")
	print("Even or Odd\n")
	number = int(input("What's your number?\n"))
	if number % 2 == 0:
		print("EVEN!")
	else:
		print("ODD!")
	
	pass


def word_soup():
	print("")
	print("Word Soup\n")
	word = input("Say your word:\n")
	if len(word) != 5:
		print(word)
	elif word[0].lower() in ["a", "e", "i", "o", "u"]:
		print(word[::-1])
	elif word[0].lower() in ["f", "h", "k", "l", "m", "n", "t", "v", "w", "x", "y"]:
		print((word[0] + word[2] + word[4]) * 3)
	else:
		print(word[0:3])
	
	pass


def numberama():
	print("")
	print("Numberama\n")
	num = input("ENTER YOUR NUMBERAMA:\n")
	n1 = int(num[0])
	n2 = int(num[1])
	n3 = int(num[2])
	valid = True
	if n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2:
		print("GIANT IN THE MIDST!")
		valid = False
	if n2 == 0:
		if n1 == 1 and n3 == 1:
			print("HOLE IN ONES!")
		else:
			print("HOLE IN ONE!")
		valid = False
	if n1 == n2 or n1 == n3 or n2 == n3:
		if n1 == n2 == n3:
			print("TRIPLETS!")
		else:
			print("CORNERED!")
		valid = False
	if n1 + n2 + n3 > 15:
		print("A HAPPY MEDIUM!")
		valid = False
	if valid == True:
		print("NO COMMENT.")
	
	pass



# this instructs the program to execute each
# of the subroutines, one after the other.
# if you don't want them ALL to run, add a #
# at the start of the line to comment it out.
# to complete the built in Input/Output Tests
# you will need them to execute in this order:

age_rater()
even_or_odd()
word_soup()
numberama()