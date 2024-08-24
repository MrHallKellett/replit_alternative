from random import randint
from time import sleep, time
from os import system
try:
    from pynput.keyboard import Listener
    pynput_found = True
except:
    pynput_found = False

turns = 0


class Player: #each player's properties
    def __init__(self):
        self.name = ""
        self.square = 0
        self.turn = False

def dice_roll(): #picking a number between 1 and 6
  def on_press(*args):
      return False
  
  input("Ready to roll?\n")
  if pynput_found:
  
    listener = Listener(on_press= on_press)
    listener.start()
    dice_value = randint(1,6)
    while listener.isalive():
        dice_value = randint(1,6)
        print("\r" + str(dice_value), end="")
        sleep(0.01)
    print("You rolled a {}".format(dice_value))
  else:
    dice_value = randint(1,6)
    print("You rolled a {}".format(dice_value))
  return dice_value

def start_to_end(): #which squares lead to which
    
    snakes = {
      32: 10,
      36: 6,
      62: 18,
      88: 24,
      95: 56,
      97: 78
    }
  
    ladders = {
      8: 10,
      4: 14,
      1: 38,
      21: 42,
      28: 76,
      50: 67,
      71: 92,
      88: 99 
    }
    return snakes, ladders

def snake_ladder(dice, snakes, ladders, current_player):
    """check whose turn it is
    change that players square according to the die roll
    return the player
    """
    this_die = dice
    new_square = current_player.square + this_die
    if new_square in snakes:
        current_player.square = snakes.get(new_square)
    elif new_square in ladders:
        current_player.square = ladders.get(new_square)
    else:
        current_player.square = current_player.square + this_die
    score = current_player.square
    return score


    """that_player = check_turn(turns, player, computer)
    print(f"player has {that_player.square}")
    current_score = player.square
    new_score = current_score + dice_value

    if new_score in snakes:
        overall_score = snakes.get(new_score)
    elif new_score in ladders:
        overall_score = ladders.get(new_score)
    else:
        overall_score = that_player.square + dice_value
    that_player.square += dice_value
    print(f"player now has {that_player.square}")
    return overall_score, that_player"""

def check_turn(turns, player, computer): #check and display which player's turn it is
    if turns % 2 != 0:
        this_player = player
    else:
        this_player = computer
    return this_player

def snake_ladder_print(score, snakes, ladders):
    if score in snakes:
        print("Oh no! You hit a snake!")
    elif score in ladders:
        print("Woo! You hit a ladder!")
    else:
       print("You didn't hit anything...")

def intro_screen():
   strings = ["WELCOME TO SNAKES AND LADDERS!", "YOU WILL PLAY AGAINST STEVE.", "1. EACH PLAYER MUST ROLL THE DICE TO GET TO THE FINISH", "2. IF YOU LAND ON A LADDER, PREPARE TO GET A BOOST UP!", "3. IF YOU LAND ON A SNAKE, YOU WILL BE SLID DOWN! CAREFUL." ]
   for new_string in strings:
      dash_amount = (100 - len(new_string)) // 2
      print("-" * dash_amount + new_string + "-" * dash_amount)

def end_screen(winner):
   strings = ["GAME OVER!", "WINNER IS {winner}"]
   for new_string in strings:
      dash_amount = (100 - len(new_string)) // 2
      print("-" * dash_amount + new_string + "-" * dash_amount)


def main_game(player, computer):
    intro_screen()
    turns = 0
    overall_score = 0 
    while player.square <= 100 or computer.square <= 100:
        current_player = check_turn(turns, player, computer)
        print("It is now {}'s turn".format(current_player.name))
        if current_player == computer:
            dice = randint(1,6)
            print("Steve rolled a {}".format(dice))
            snakes, ladders = start_to_end()
            score = snake_ladder(dice, snakes, ladders, current_player)
            sleep(0.5)
            print("{}'s new score is {}".format(current_player.name, score))
            sleep(0.5)
        else: 
            dice = dice_roll()
            snakes, ladders = start_to_end()
            score = snake_ladder(dice, snakes, ladders, current_player)
            sleep(0.5)
            snake_ladder_print(score, snakes, ladders)
            sleep(0.5)
            print("{}'s new score is {}".format(current_player.name, score))
            sleep(0.5)
        turns += 1
    if player.square == 100:
        winner = player
    elif computer.square == 100:
        winner = player
    end_screen(winner)




player = Player()
computer = Player()
player.name = input("What would you liked to be called?\n")
computer.name = "Steve"

"""x = snake_ladder(?, ?, ?)
current_player = check_turn()asd
dice_roll() 
main_game(current_player, x)"""

main_game(player, computer)
          
