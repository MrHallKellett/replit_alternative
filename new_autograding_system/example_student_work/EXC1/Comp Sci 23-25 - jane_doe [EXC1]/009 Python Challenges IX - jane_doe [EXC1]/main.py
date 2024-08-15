def count_vowels(word: str) -> int:
  vowels = 0                        ## start counting from zero
  print("Gonna be countin' vowels...")
  
  for character in word.lower():    ## loop through each character
    if character in "aeiou":        ## check if char is a vowel
      vowels += 1                   ## if it is, count it!
  
  return vowels                     ## 'give back' the number to the main menu


def count_capitals(word: str) -> int:
  capitals = 0
  print("Gonna be countin' capitals...")
  
  for character in word:
    if character.isupper():
      capitals += 1
  
  return capitals                   ## add the third and fourth functions here
   

def count_consonants(word: str) -> int:
  consonants = 0
  print("Gonna be countin' consonants...")

  for character in word.lower():
    if character not in "aeiou":
      consonants += 1

  return consonants
  

def count_spaces(word: str) -> int:
  spaces = 0
  print("Gonna be countin' consonants...")

  for character in word:
    if character == " ":
      spaces += 1

  return spaces


### main menu loop
choice = ""
while choice != "5":
  
  word = input("What word to analyse? ")
  
  print("""
What to do?
1. count vowels
2. count capitals
3. count consonants
4. count spaces
5. quit""")                         ## amend this with the new options
  
  choice = input(" > ")

  if choice == "1":
    num = count_vowels(word)        ## make sure the new functions are called here.
    print("I found {}.".format(num))  
  elif choice == "2":
    num = count_capitals(word)
    print("I found {}.".format(num))
  elif choice == "3":
    num = count_consonants(word)
    print("I found {}.".format(num)) 
  elif choice == "4":
    num = count_spaces(word)
    print("I found {}.".format(num))
  elif choice == "5":
    print("Bye!")
  else:
    print("What am I supposed to do with {}?".format(choice))
