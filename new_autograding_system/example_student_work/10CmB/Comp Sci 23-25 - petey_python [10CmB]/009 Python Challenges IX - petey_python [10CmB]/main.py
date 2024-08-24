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
  
  ## fill out the code for this function here
  
  return capitals
  
## add the third and fourth functions here

### main menu loop
choice = ""
while choice != "5":
  
  word = input("What word to analyse? ")
  
  choice = input("""
What to do?
1. count vowels
2. count capitals""")   ## amend this with the new options

  if choice == "1":
    num = count_vowels(word)
    
  elif choice == "2":
    num = count_capitals(word)  ## make sure the new functions are called here.
  elif choice == "5":
    print("Bye!")
  else:
    print("What am I supposed to do with {}?".format(choice))
  
  print("I found {}.".format(num))
    
  
  