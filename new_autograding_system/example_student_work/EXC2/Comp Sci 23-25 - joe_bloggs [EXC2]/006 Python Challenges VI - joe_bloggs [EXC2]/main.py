
def cheerleader():
  name = input("Name?\n")
  for letter in name:
    print(letter + "!")
  
  
  pass

def countdown_v2():
  num = int(input("Enter number to count down from: \n"))
  for i in range(num, -1, -1):
    print(i)
  print("GO!")
  
  pass

def sum_kinda_program():
  
  num = int(input("Enter Number: "))
  for ask in range(9):
    num = int(input("Enter Number: "))
  total = num 
  
  pass
  
def triangle():
  ## Complete Exercise 4 - Triangle - here
  pass

def mimicker():
  ## Complete Exercise 5 - Mimicker - here
  pass

def my_name_your_name():
  ## Complete Exercise 6 - My Name, Your Name - here
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