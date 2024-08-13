
def sports_recorder():
  ## Complete Exercise 1 - Sports Recorder - here
  sport_chosen = []
  for sport_number in range(1,6):
    sport = input("Enter sport: ")
    sport_chosen.append(sport)
  
  else:
    print("Your sports were: ")
    print(sport_chosen)
  pass

def my_zoo():
  ## Complete Exercise 2 - My Zoo - here

  valid_animal = False
  while valid_animal == False:
    animal = input("What animal? \n")
    
    if animal in ["cat", "dog", "cow", "pig", "rat", "bat", "ewe"]:
      print('Thats one of mine!')
      valid_animal = True
      
    else:
      print("Not one of mine.")
    pass

def name_positions():
  ## Complete Exercise 3 - Name Positions - here
  valid_number = False
  
  while valid_number == False:
    number = int(input("What number?"))

    if number > 10:
      print("Please enter between 1 and 10 only.")
  
  pass
  
def lengths_of_friends():
  ## Complete Exercise 4 - Lengths of Friends - here
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
