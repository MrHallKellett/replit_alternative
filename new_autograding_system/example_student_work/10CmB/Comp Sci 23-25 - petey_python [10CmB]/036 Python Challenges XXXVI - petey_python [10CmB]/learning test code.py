from random import randint

class Player:
    #player contains properties
    def _init_(self):
        self.hp = 100
        self.name = ""
        self.guild = ""

player1 = Player()
player2 = Player()
player3 = Player()

player1.name = "adele"
player2.name = "yummy"
player3.name = "yum"

players = [player1, player2, player3]

#loop through the players and print out each players name
#then decrease the hp by a random amount
for player in players:
    print(player.name)
    player.hp -= randint(1,75)

#add a new player with all three properties input by the user
player4 = Player()
player4.hp = int(input())
player4.name = input()
player4.guild = input()

enemies = []
for _ in range(10):
    enemies.append(Player())