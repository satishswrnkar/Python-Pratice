import os
from random import randint

os.system('cls') # clearing output screen

print("\n\n")

print("_"*100)
print("_"*100)

print("\n\n")

while input("\n\n\t\tDo you want to play Guess Game ? write yes to play: ").strip().lower() == 'yes':

    comGuess = randint(1, 50)
    chances = 5

    while chances != 0:
        print("\n\n")
        print(f"You have Left {chances} to win this game.".center(100))
        userGuess = int(input("\nEnter your Guess (1-50): "))

        if userGuess < 1 or userGuess > 50:
            print("\n")
            print("Warning!! GUESS Between 1-50 Only!!".center(100))
            continue

        if userGuess == comGuess:
            print("\n")
            print("Whola You such a Master!!! You Have Won The Game".center(100))
            break

        elif userGuess > comGuess:
            print("\n")
            print("Hint: Be in Limit, Think Lower".center(100))

        else:
            print("\n")
            print("Hint: Be Big Think Big".center(100))

        chances = chances - 1

    else:
        print("\n")
        print(f"Shame on You!!! You Such a LOOSER!!! Computer Guess Was: {comGuess}".center(100))

print("\n\n")

print("_"*100)
print("_"*100)

print("\n\n")
