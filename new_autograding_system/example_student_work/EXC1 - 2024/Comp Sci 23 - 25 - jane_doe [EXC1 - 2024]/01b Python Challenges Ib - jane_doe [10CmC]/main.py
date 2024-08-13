'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''




def leet_speak():
	speech = input("Say something:\n")
	speech = speech.replace("i", "!")
	speech = speech.replace("e", "3")
	speech = speech.replace("o", "0")
	speech = speech.replace("a", "4")
	speech = speech.replace("k", "|<")
	speech = speech.replace("h", "|-|")
	speech = speech.replace("...", ".........")
	speech = speech.replace("?", "???")
	print(speech)
	pass

def banner():
	name = input("Who are you?\n").upper()
	times = int(len(name))
	print(("-" * times) + ("=" * (times + 4)) + ("-" * times))
	print(("-" * (times-2)) + "/ / " + name + " \ \\" + ("-" * (times-2)))
	print(("-" * times) + ("=" * (times + 4)) + ("-" * times))			
	pass


def grid():
	size = int(input("What size grid?\n"))
	rows1 = size/2
	rows2 = (size/2) - 1
	line1 = ((("*-") * (size - 1)) + "*")
	line2 = ("| " * (size - 1) + "|")
	while rows1 > 1:
		print(line1)
		print(line2)
		rows1 -= 1
		rows2 -= 1
	print(line1)
	pass




# this instructs the program to execute each
# of the subroutines, one after the other.
# if you don't want them ALL to run, add a #
# at the start of the line to comment it out.
# to complete the built in Input/Output Tests
# you will need them to execute in this order:

leet_speak()
banner()
grid()