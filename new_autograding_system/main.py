
def sports_recorder():
  ## Complete Exercise 1 - Sports Recorder - here
  x = []
  for i in range(5):
    x.append(input("Enter sport: "))
  print("Your sports were:", x)

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

  n = "Baz, Beth, Mik, Dave, Bill, Chuck, Olu, Ted, Dewan, Anjel".split(", ")
  
  while valid_number == False:
    number = int(input("What number?"))

    if number > 10 or number < 1:
      print("Please enter between 1 and 10 only.")
    else:
      valid_number = True

  print(n[number-1].upper(), "was found at number", number)
  
  pass
  
def lengths_of_friends():
  ## Complete Exercise 4 - Lengths of Friends - here
  n = ""
  names = []
  while n != "stop":

    print("What name?")
    n = input()
    if n != "stop":
      names.append(n)
  print("OK - stopping. The names you entered had these lengths:")
  print(list(map(len, names)))


def word_analysis_table():
  ## Complete Exercise 5 - Word Analysis Table - here
  words = []
  w = int(input("How many words to analyse?\n"))
  print(f"OK - I will analyse {w} words.")
  for i in range(1, w+1):
    words.append(input(f"Enter word {i}: "))
  
  max_width = max([5, len(max(words, key=len)) + 1])
  print("WORD ANALYSIS")

  print("WORD ".ljust(max_width), end="")
  for w in "LETTERS,VOWELS,REPETITIONS".split(","):
    print(w.ljust(len(w)+1), end="")
  print()
  for word in words:
    print(word.ljust(max_width), end="")
    print(str(len(word)).ljust(len("LETTERS")+1), end="")
    print(str(sum(1 for i in word if i in "aeiou")).ljust(len("VOWELS")+1), end="")
    print(str(sum(1 for i in set(word) if word.count(i) > 1)).ljust(len("REPETITIONS")+1))




        






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
