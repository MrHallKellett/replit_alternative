import random

class player:

    def __init__(self):
        self.hp = 100
        self.name = ""
        self.team = ""



player1 = player()
player2 = player()
player3 = player()
player4 = player()

player1.name = "Cara"
player2.name = "aarav"
player3.name = "adele"

players = [player1, player2, player3]

enemies = []
for _ in range(10):
    enemies.append(player())

for player in players:
    print(player.name)


for player in players:
    player.hp -= random.randint(1,100)

print(player1.hp)
print(player2.hp)
print(player3.hp)


player4.hp = int(input("???"))
player4.name = input("???")
player4.team = input("???")
for attribute in player4:
    pass