def task_1():

  print("What did you eat for lunch? ")
  food = input()
  print("Yum! I love eating", food)

#########################################################

def task_2():
  
  name = input("What's your name? ")
  print("Hello", name)
  
#########################################################

def task_3():  
  
  print("Enter a name for the number 0208345242:")
  l0208345242 = input()
  print(f"Enter the date you last called {l0208345242}: ")
  lastcalled = input()
  print("So you called", l0208345242, "on", lastcalled, "?")
 
#########################################################
 
def task_4():
    
  name = input("What's your name? ")
  if name[0] == "B":
    print("Hello")
  elif name[0] == "G":
    print("Goodbye")
  else:
      print("Who are you?")
      
#########################################################
      
def task_5():
    
  print("So, where do you live? ")
  city = input()
  print("WOW! I'd love to live in {}!".format(city))

#########################################################

def task_6():
  money = input("How much pocket money do you get per week? £")
  weeks = input("How many weeks have you been saving? ")
  print("You've saved £{}!".format(int(money) * int(weeks)))
  
#########################################################
  
def task_7():
  for number in range(5):
    num = int(input("Enter an even number. "))
    if num % 2 == 0:
      print("Correct!")
    else:
      print("Incorrect!")


#########################################################

def task_8():

  """Get information about a person and summarise it"""
  print("Just to confirm it's this file i'll put this here")
  job = input("What's your job? ")
  live = input("Where do you live? ")
  hair = input("What's your hair colour? ")
  age = int(input("How old are you? "))
  
  print("{} years of {} hair being a {} in {}?".format(age, hair, job, live))

#######################################################################################################

def task_9():
  """Check if the email address is a valid email, containing an @ symbol"""

  email = input("Enter your email e.g. bob@mail.com: ")
  if len(email) > 0:
    if "@" in email:
      print("Your email is valid.")
    else:
      print("Not valid.")
  else:
    print("Please enter an email!")
    
#######################################################################################################

def task_10():
  """Calculate how many bags of crisps per person."""

  bags = 24
  ppl = int(input("How many people? "))
  each = bags // ppl
  left = bags % ppl
  print("Each person can have {} bags of sticky rice and there will be {} left over.".format(each, left))

#######################################################################################################

def task_11():
  """Ask the user to enter the names of their children"""

  child1 = input("What's the name of your first child? ")
  child2 = input("What's the name of your second child? ")
  child3 = input("What's the name of your third child? ")
  print(f"Your children: {child1}, {child2}, {child3}")
  
#######################################################################################################

def task_12():
  """Tell the user how old they will be in 5 years' time"""

  age = int(input("How old are you? "))
  in_five = age + 5
  print("In 5 years you will be", in_five)

#######################################################################################################

def task_13():
  """Tell the user their initials."""

  name = input("Enter your name in the format forename[space]surname: ")
  fore, sur = name.split(" ")
  initials = "{}.{}.".format(fore[0], sur[0])
  print("Your initials are: ", initials)
  
#######################################################################################################
  
def task_14():
  """Have a chat about the user's job"""

  print("What's your name? ")
  thing = input()
  print("What do you do for a living? ")
  x = input()
  print("Where abouts is that? ")
  where = input()
  print("With a name like", thing, "I'd expect you to work in", where+"!")

#######################################################################################################

def task_15():
  """Display information about the user's favourite number"""

  fave_num = int(input("What's your favourite number? "))
  print("I can see that your favourite number...")
  if fave_num > 0:
    print("is a positive number!")
  if 10 <= abs(fave_num) < 100:
    print("only has 2 digits!")
  elif fave_num < 10:
    print("only has a single digit!")
  if fave_num % 2 == 1:
    print("is an odd number!")
  if "0" in str(fave_num):
    print("contains the digit 0!")

#######################################################################################################

def task_16():
  """Evaluate a football game score..."""

  home = int(input("How many goals scored by the HOME team? "))
  away = int(input("How many goals scored by the AWAY team? "))
  if home > away:
    print("HOME team wins!")
  if away > home:
    print("AWAY team wins!")
  if home == away:
    print("It was a DRAW!")
  elif home == 0 or away == 0:
    print("At least one clean sheet! ")


def menu():
  """Displays a list of options and calls the correct
  function for the requested exercise"""

  choice = input("Enter task number e.g. 1, 2, 3 etc: ")
  if choice == "1":
    task_1()
  try:
    eval("task_{}()".format(choice))
  except NameError:
    print("I didn't understand '{}'".format(choice))


menu()
