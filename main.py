import random
from typing import  List

def init():
    name = str(input("Enter your name: "))
    print(f"Hello there, {name}. This is the most extreme guessing game!")
    ChooseNumber(name)

def ChooseNumber(name):
    x = int(input("Choose Min Number: "))
    y = int(input("Choose Max Number: "))
    randNumber = RandomNumber(x, y)

    userGuess = int(input(f"What's your guess {name}? "))
    CheckGuess(randNumber, userGuess, name)

def RandomNumber(x, y):
    randomNumber = random.randint(x, y)

    return randomNumber

def CheckGuess(answer, guess, name):
    if guess == answer:
        print(f"Congratulations, You guessed the number correctly {name}")
    else:
        print("Oops, the number was incorrect. Better luck next time!")

    continueGame = str(input("Want to continue playing?\nType yes to continue: "))


    ContinueGame(continueGame, name)

def ContinueGame(contgame: str, name: List[int]):
        if contgame.lower() == "yes":
            ChooseNumber(name)
        else:
            print(f"See you soon {name}")


init()
