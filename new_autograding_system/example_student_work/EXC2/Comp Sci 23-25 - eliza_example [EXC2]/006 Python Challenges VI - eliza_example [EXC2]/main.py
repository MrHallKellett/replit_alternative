
def sports_recorder():
  sport = []
  for sport_no in range(5):
    sport_2 = input("Enter sport:\n")
    sport.append(sport_2)
  print(f"Your sports were: {sport}")
  pass

def my_zoo():
  animal = input("What animal?\n")

  while len(animal) != 3:
    print("Not one of mine.")
    animal = input("What animal?\n")

  print("That’s one of mine!")
  pass

def name_positions():
  names = ["BAZ", "BETH", "MIK", "DAVE", "BILL", "CHUCK", "OLU", "TED", "DEWAN", "ANJEL"]

  number = int(input("What number?\n"))
  

  while number < 1 or number > 10:
    print("Please enter between 1 and 10 only.")
    number = int(input("What number?\n"))

  print(str(names[number - 1]) + " was found at number " + str(number) )
  pass
  
def lengths_of_friends():
  name = []


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
