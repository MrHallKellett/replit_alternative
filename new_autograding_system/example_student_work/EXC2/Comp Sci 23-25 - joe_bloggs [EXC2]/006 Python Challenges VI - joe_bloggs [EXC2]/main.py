
def sports_recorder():
  ## Complete Exercise 1 - Sports Recorder - here
  sportslist = []
  for i in range(5):
    sport = input("Enter sport:\n")
    sportslist.append(sport)
  print(f"""Your sports were: {sportslist}""")
  pass

def my_zoo():
  ## Complete Exercise 2 - My Zoo - here
  animal = input("What animal? \n")
  animalslist = ["dog", "cat", "cow", "pig", "rat", "bat", "ewe"]
  while animal not in animalslist:
    print("Not one of mine.")
    animal = input("What animal?\n")
  print("That’s one of mine!")
  pass

def name_positions():
  ## Complete Exercise 3 - Name Positions - here
  number = int(input("What number?\n"))
  names = ["BAZ", "BETH", "MIK", "DAVE", "BILL", "CHUCK", "OLU", "TED", "DEWAN", "ANJEL"]
  while number > 10 or number < 1:
    print("Please enter between 1 and 10 only.")
    number = int(input("What number?\n"))
  print(f"{names[number - 1]} was found at number {str(number)}")
  pass
  
def lengths_of_friends():
  ## Complete Exercise 4 - Lengths of Friends - here
  namelengths = []
  name = input("What name?\n")
  namelengths.append(len(name))
  while name != "stop":
    name = input("What name?\n")
    namelengths.append(len(name))
  print("OK - stopping. The names you entered had these lengths:")
  namelengths.pop()
  print(namelengths)
  pass

def word_analysis_table():
  ## Complete Exercise 5 - Word Analysis Table - here
  num = int(input("How many words to analyse?\n"))
  words = []
  letters = []
  vowels = []
  repetitions = []
  vowel = 0
  repeats = 0
  maximum = 0
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if num > 0:
    print(f"OK - I will analyse {str(num)} words.")
  else:
    print("OK - I will analyse 1 word.")
  for i in range(1, num + 1):
    word = input(f"Enter word {str(i)}:  ")
    words.append(word.lower())
  words.append("WORD")
  for i in words:
    if len(i) > maximum:
      maximum = len(i)
  words.pop()
  print("WORD ANALYSIS")
  print(f"""WORD{(maximum + 1 - 4) * " "} LETTERS VOWELS REPETITIONS""")
  for i in range(num):
    letters.append(str(len((words[i].replace(" ", "")))))
    vowel = 0
    for letter in words[i]:
      if letter in "aeiou":
        vowel += 1
    vowels.append(str(vowel))
  for i in range(num):
    for letter in alphabet:
      theword = words[i]
      if letter in theword:
        theword.replace(letter, "")
      if letter in theword:
        repeats += 1
    repetitions.append(str(repeats))
    repeats = 0
  for i in range(num):
    print(words[i] + (((maximum - len(words[i]) + 2)) * " ") + letters[i] + ((8 - (len(letters[i]))) * " ") + vowels[i] + (6 * " ") + repetitions[i])
  
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
