########################################
########################################
### DON'T TOUCH LINE 1 - LINE 45 !! ####
########################################
########################################

## always import libraries / functions first
import random

## then define global constants
SPACE = " "


## then come your function definitions
def make_abbreviated_name(name):
  """Function to abbreviate a name"""
  end = len(name) - 1
  mid = len(name) // 2
  
  first = name[0]
  second = " "
  third = " "
  while second == SPACE or third == SPACE:
    try:
      second, third = name[mid], name[end]
      abbr_name = "".join([first, second, third])
    except IndexError:
      abbr_name = "CANNOT BE ABBREVIATED"
      break
    mid += 1
    end -= 1
    
  return abbr_name

def make_silly_name(name):
  """Function to RaNDoM CAp a name"""
  silly_name = ""
  for letter in name:
    if random.randint(0, 1):
      silly_name += letter
    else:
      silly_name += letter.upper()
  
  return silly_name
  

def name_menu():
  pass


### write your solutions to the Tasks here.








