# Jeu du juste prix:

import random

choice = random.choice(range(1,100))
running = True

while running:
    userchoice = int(input("guess the right number man:"))
    if (userchoice) == choice:
        print("You made it broooo!")
        running = False
    elif (userchoice) > choice:
        print("You're way to high! Welcome to the real world Jackass!!")
    elif(userchoice) < choice:
        print("You're like your penis: way to small !!! try again you bitch")

print("End of game, bitch")