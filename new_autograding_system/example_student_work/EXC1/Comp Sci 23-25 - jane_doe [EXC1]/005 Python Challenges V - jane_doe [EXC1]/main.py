
def cheerleader():
	name = input("Name?\n")
	for letter in name:
		print(f"{letter}!")
	pass

def countdown_v2():
	num = int(input("Enter number to count down from: "))
	for i in range(num, -1, -1):
		print(i)
	print("GO!")
	pass

def sum_kinda_program():
	total = 0
	for i in range(10):
		num = int(input("Enter number: "))
		total += num
	print(f"That's enough. Total was: {total}")
	pass
	
def triangle():
	name = input("Who are you? ")
	times = int(input("How many times? "))
	for i in range(times):
		print(name * i)
	print(name * times)
	pass

def mimicker():
	go = True
	while go == True:
		sentence = input("Enter a sentence: ")
		if sentence == "stop it now this is getting silly":
			go = False
			print("OK.")
		else:
			for i in sentence:
				print(sentence)
	pass

def my_name_your_name():
	myName = input("My name: ")
	urName = input("Your name: ")
	if len(myName) == len(urName):
		num = 0
		for letter in myName:
			print(f"Letter {num}:")
			if myName[num] == urName[num]:
				print("SAME")
			else:
				print("DIFFERENT")
			num += 1
			
	pass

def secret_code():
	## Complete Exercise 7 - Secret Code - here
	pass







#### leave this block of code - don't change it!
##########################################################################

print("""Enter 1 to test CHEERLEADER
Enter 2 to test COUNTDOWN V2
Enter 3 to test SUM KINDA PROGRAM
Enter 4 to test TRIANGLE
Enter 5 to test MIMICKER
Enter 6 to test MY NAME, YOUR NAME
ENTER 7 to test SECRET CODE""")
x = input()
subs = {"1":cheerleader, "2":countdown_v2, "3":sum_kinda_program, "4":triangle, "5":mimicker, "6":my_name_your_name, "7":secret_code}
if x in subs:
	subs[x]()

##########################################################################