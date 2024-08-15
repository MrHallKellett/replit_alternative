## NOTE: using a string any longer than 1 character is FORBIDDEN
## for this problem set!!!  #####################################
#################################################################



def task1():
	for i in range(1, 8):		
		for j in range(i):	
			print("*", end="")	
		print()
	pass

def task2():
	for i in range(11, 0, -1):		
		for j in range(i):	
			print("*", end="")	
		print()
	pass


def task3():
	for i in range(2, 11, 2):		
		for j in range(i):	
			print("*", end="")	
		print()
	pass


def task4():
	for i in range(10):		
		for j in range(10):	
			print(j, end="")	
		print("")
	pass


def task5():
	power = 1
	for i in range(6):		
		for j in range(2**i):	
			print("*", end="")	
		print()
	pass


def task6():
	for i in range(10, 0, -1):		
		for j in range(i):	
			print(j, end="")	
		print()
	pass


def task7():
	for i in range(10):
		for j in range(10):	
			print(str(i), end="")	
		print()
	pass


def task8():
	for i in range(11):		
		for j in range(i):	
			print(j, end="")	
		print()
	pass


def task9():
	for i in range(10, 0, -1):
		for j in range(10):
			print(" ", end="")
		for j in range(i):
			print(j, end="")
		print()
	pass


def task10():
  pass


print("""Enter number of task to test:""")
x = input()
if x.isdigit():
  eval(f"task{x}()")
else:
  print("Not a valid task.")