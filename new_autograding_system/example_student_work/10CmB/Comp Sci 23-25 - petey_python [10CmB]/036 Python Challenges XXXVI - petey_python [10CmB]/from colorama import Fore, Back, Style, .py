from colorama import Fore, Back, Style, init
import random
import sys,time
from os import system
from time import sleep
win = False
filer = True
p1_hand_list = []
p2_hand_list = []
pile = []

def print_slow(time):
    for second in time:                     
        print(second, end='')
        sleep(0.05)
    print()
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
color_list = [Back.YELLOW+Fore.BLACK+"YELLOW", Fore.BLACK+Back.GREEN+"GREEN ", Fore.BLACK+Back.BLUE+"BLUE  ", Fore.BLACK+Back.RED+"RED   "]
random_num_p1 = random.choice(num_list)
random_color_p1 = random.choice(color_list)
p1_card = (random_color_p1 + " " + random_num_p1)
random_num = random.choice(num_list)
random_color = random.choice(color_list)
random_card = (random_color + " " + random_num)
wildcard = (Back.BLACK+"wildcard")
Green = Fore.BLACK+Back.GREEN+"Green"
Blue = Fore.BLACK+Back.BLUE+"Blue"
Red = Fore.BLACK+Back.RED+"Red"
Yellow = Fore.BLACK+Back.YELLOW+"Yellow"
draw_4 = (Back.BLACK+"draw 4")
draw_2 = (random_color+" "+"draw 2")
skip = (random_color + " " + "skip")
pile = []

def intro(): #will ask how many people there are and if isn't 2 than the game won't start
        print_slow("How many people are going to play? ")
        people_counter = int(input())
        sleep(0.25)
        while people_counter != 2: #will not allow numbers that aren't 2
                print ("That is not allowed a registered number for uno")
                sleep(0.5)
                print("You need 2 people, Input again")
                people_counter = int(input("How many people are going to play? "))   
        random_card_start() 

def random_card_start():
        print_slow("Player 1                                    Player 2")
        print_slow("--------                                    --------")
        for cards in range (0,8): #repeats 8 times
                random_num_p1 = random.choice(num_list)
                random_color_p1 = random.choice(color_list)
                random_num_p2 = random.choice(num_list)
                random_color_p2 = random.choice(color_list)

                p1_card = (random_color_p1 + "" + random_num_p1)
                p2_card = (random_color_p2 + "" + random_num_p2)
                player_tracker = True
                print(p1_card,Style.RESET_ALL,end=(""))
                sleep(0.5)
                print("                                   ",p2_card,Style.RESET_ALL)
                p1_hand_list.append(p1_card) #adds a random card into the player 1 list
                p2_hand_list.append(p2_card)  #adds a random card into the player 2 list
        moves()    

def moves():
              pile = [] #new list
              pile.append(random_card) #adds a random card to start the game
              player_name_tracker = ""
              counter=0
              win = False 
              hand_chooser = True
              opposite_player_list = [] #new list for the oppenants deck
              while win == False: #while loop will continue to run until there no cards in a players deck
                  if hand_chooser == True: #this will decide which player is playing and which list to use
                    current_player_list = p1_hand_list
                    opposite_player_list = p2_hand_list
                    player_name_tracker = "P1" #will show P1 in options like "P1 is choosing" or "P1 deck" to make it easier to see who is playing
                  elif hand_chooser == False: #this will decide which player is playing and which list to use
                    current_player_list = p2_hand_list
                    opposite_player_list = p1_hand_list
                    player_name_tracker = "P2" #will show P1 in options like "P1 is choosing" or "P1 deck" to make it easier to see who is playing
                  print("-"*60)
                  print(player_name_tracker,end=" ") #prints who is playing currently and with end="" will be on the same line as deck, example : P1 deck
                  sleep(0.5) #waits 0.5 seconds
                  print_slow("deck")#prints "deck"
                  if hand_chooser == True:
                    for card in p1_hand_list:
                      print(card,Style.RESET_ALL)
                  elif hand_chooser == False:
                    for card in p2_hand_list:
                      print(card,Style.RESET_ALL)
                  sleep(2)
                  print("-"*60)
                  print_slow("The top card is: ") 
                  print(pile[0],Style.RESET_ALL) #prints the top card or first element in pile and then resets the color 
                  print(player_name_tracker,end="") #
                  sleep(0.5)
                  print_slow(""", What would do?
hit, play, look at deck """)
                  first_move_input = input()
                  if first_move_input == "hit" or first_move_input == "Hit":
                      random_chance_calculator = random.randrange(0,100) #will choose a random number between 0 and 100
                      if random_chance_calculator <= 7: #if number is smaller than 7 then you will get a wildcard
                          current_player_list.append(wildcard)
                      elif random_chance_calculator <= 14: #if number is smaller than 14 then you will get a draw 4
                          current_player_list.append(draw_4)
                      elif random_chance_calculator <= 27: #if number is smaller than 27 then you will get a skip
                          current_player_list.append(skip)
                      elif random_chance_calculator <= 40: #if number is smaller than 40 then you will get a skip
                          current_player_list.append(draw_2)  
                      elif random_chance_calculator <= 100: #if number is smaller than 100 then you will get a normal card
                        current_player_list.append(random_card)
                      print(player_name_tracker,end=" ")
                      sleep(0.5)
                      print_slow("deck")
                      print("-"*16) 
                      if hand_chooser == True:
                          for card in p1_hand_list:
                            print(card,Style.RESET_ALL)
                      elif hand_chooser == False:
                          for card in p2_hand_list:
                            print(card,Style.RESET_ALL)
                      hand_chooser = not hand_chooser
                  if first_move_input == "Look at deck" or first_move_input == "look at deck":
                        print("-"*16) 
                        counter = 0
                        if hand_chooser == True:
                          for length in range(len(p1_hand_list)):
                            print(p1_hand_list[counter],Style.RESET_ALL) #will print P1 hand on seperate lines due to a for loop and a counter
                            counter = counter + 1
                        elif hand_chooser == False:
                          for length in range(len(p2_hand_list)):
                            print(p2_hand_list[counter],Style.RESET_ALL) #will print P2 hand on seperate lines due to a for loop and a counter
                            counter = counter + 1
                        print("-"*16)                          
                  if first_move_input == "play" or first_move_input == "Play":
                      print("-"*16) 
                      print(player_name_tracker,end="")
                      sleep(0.5)
                      print_slow(" choosing")
                      print_slow("The top card is :")
                      print(pile[0]) #will print the top card on the pile/first element
                      print(Style.RESET_ALL,"-"*16)
                      for index, item in enumerate(current_player_list): #for loop I use enumerate becuase it allows you to keep track of iterations in a loop
                        print(Style.RESET_ALL,index,Style.RESET_ALL, item,Style.RESET_ALL) #will print the player's deck but with numbers next to it
                        print("-"*16) 
                      first_move_play = int(input("Which card do you want to pick "))
                      first_move_replace = current_player_list[first_move_play] 
                      if "skip" in first_move_replace: #will check if skip is in first move replace
                        hand_chooser = not hand_chooser #will make the current player have another turn
                        print_slow("Opponent's turn is skipped.")
                      elif "draw 4" in first_move_replace:
                        for card in range(4): #for loop x4
                          opposite_player_list.append(random.choice(color_list) + " " + random.choice(num_list)) #will give a random card
                        hand_chooser = not hand_chooser
                      elif "draw 2" in first_move_replace and random_color in first_move_replace: 
                        for card in range(2):
                          opposite_player_list.append(random.choice(color_list) + " " + random.choice(num_list)) #will give a random card
                        hand_chooser = not hand_chooser
                      elif "wildcard" in first_move_replace:
                          choose_color = input("""Choose a colour
1. Yellow
2. Red
3. Blue
4. Green
""")
                          if choose_color.lower() == "yellow": #change color to yellow
                            pile[0] = Yellow #will put yellow as the top card
                            print("-"*16)
                            print_slow("The top card is:")
                            print_slow(pile[0])#prints yellow/top card/ first element
                          elif choose_color.lower() == "red": #change color red
                              pile[0] = Red #will put red as the top card
                              print("-"*16)
                              print_slow("The top card is:")
                              print_slow(pile[0])#prints red/top card/ first element
                          elif choose_color.lower() == "blue": #change blue
                              pile[0] = Blue #will put blue as the top card
                              print("-"*16)
                              print_slow("The top card is:")
                              print_slow(pile[0])#prints blue/top card/ first element
                          elif choose_color.lower() == "green": #change color green
                              pile[0] = Green #will put green as the top card
                              print("-"*16)
                              print_slow("The top card is:")
                              print_slow(pile[0])#prints green/top card/ first element
                          print(Style.RESET_ALL,"----------------",Style.RESET_ALL) 
                          current_player_list.remove(first_move_replace)
                          print(player_name_tracker,end=" ")
                          sleep(0.5)
                          print_slow("hand is now: \n")
                          if hand_chooser == True:
                            for card in p1_hand_list:
                              print(card,Style.RESET_ALL)
                          elif hand_chooser == False:
                            for card in p2_hand_list:
                              print(card,Style.RESET_ALL)
                          print("-"*16,Style.RESET_ALL) 
                          sleep(3)
                          print("-"*16,Style.RESET_ALL) 
                          hand_chooser = not hand_chooser
                      elif random_num in first_move_replace or random_color in first_move_replace: #will check if either the number or the color are the same
                        pile[0] = first_move_replace
                        current_player_list.remove(first_move_replace)
                        hand_chooser = not hand_chooser
                      else:
                        print_slow("That is not a valid color choice")
                  if len(current_player_list) == 0: #check if current player list is 0
                    win = True #stops the while loop
                    if hand_chooser == True:
                      player_name_tracker = "P1"
                    elif hand_chooser == False:
                      player_name_tracker = "P2"
                    print (hand_chooser + "Win") #prints win

intro()