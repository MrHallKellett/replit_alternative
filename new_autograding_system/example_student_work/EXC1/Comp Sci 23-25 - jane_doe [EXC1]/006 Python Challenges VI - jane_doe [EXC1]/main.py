
def sports_recorder():
  sport_list = []
  for i in range(5):
    sport = input("Enter sport: \n")
    sport_list.append(sport)
  print(f"Your sports were: {sport_list}")
  pass

def my_zoo():
  animal = input("What animal? \n")
  three_letters = ["cat", "dog", "cow", "pig", "rat", "bat", "ewe"]
  while animal not in three_letters:
    print("Not one of mine.")
    animal = input("What animal? \n")
  print("Thats one of mine!")
  pass

def name_positions():
  names = ["Baz", "Beth", "Mik", "Dave", "Bill", "Chuck", "Olu", "Ted", "Dewan", "Anjel"]
  num = int(input("What number?\n"))
  while num < 1 or num > 10:
    print("Please enter between 1 and 10 only.")
    num = int(input("What number?\n"))
  index = num - 1
  wanted = names[index]
  print(f"{wanted.upper()} was found at number {num}")
  pass
  
def lengths_of_friends():
  name_list = []
  name = ""
  while name != "stop":
    length = len(name)
    name_list.append(length)
    name = input("What name?\n")
  print("OK - stopping. The names you entered had these lengths:")
  name_list.remove(0)
  print(name_list)
  pass

def word_analysis_table():
  ## Complete Exercise 5 - Word Analysis Table - here
  pass

        






#### leave this block of code - don't change it!
##########################################################################

print("""Enter 1 to test SPORTS RECORDER
Enter 2 to test MY ZOO
Enter 3 to test NAME POSITIONS
Enter 4 to test LENGTHS OF FRIENDS
Enter 5 to test WORD ANALYSIS TABLE""")
x = input()
subs = {"1":sports_recorder, "2":my_zoo, "3":name_positions, "4":lengths_of_friends, "5":word_analysis_table}
if x in subs:
  subs[x]()

##########################################################################
