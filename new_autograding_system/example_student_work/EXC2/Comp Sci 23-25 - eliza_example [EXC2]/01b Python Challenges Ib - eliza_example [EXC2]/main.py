'''Below are several subroutine stubs
Your task is to write the correct code inside
each subroutine to create the program shown
in the task instructions (see 'instructions.md')

Test your code by pressing Run >'''




def leet_speak():
  ## complete exercise 1 - L33t sp34k - here
  speech = input("Say something:\n")
  speech = speech.replace("i", "!")
  speech = speech.replace("e", "3")
  speech = speech.replace("o", "0")
  speech = speech.replace("a", "4")
  speech = speech.replace("|<", "k")
  speech = speech.replace("|-|", "h")
  print(speech)
  
  pass

def banner():
  ## complete exercise 2 - Banner - here
  name = input("Who are you?").upper()
  length = len(name)
  print(("-" * length) + ("=" * (length + 2)) + ("-" * length))
  print(("-" * (length - 2)) 
  
  pass


def grid():
  ## complete exercise 3 - Grid - here
  pass



  # this instructs the program to execute each
  # of the subroutines, one after the other.
  # if you don't want them ALL to run, add a #
  # at the start of the line to comment it out.
  # to complete the built in Input/Output Tests
  # you will need them to execute in this order:
  
leet_speak()
banner()
grid()