# Test for the menu() Mechanic


import random
import pyperclip
from os import name, system
from time import sleep
from datetime import date

solvedOut = """
⬜️⬜️🟨⬜️⬜️
🟩⬜️⬜🟨🟨
🟩🟩⬜️⬜️🟨
🟩🟩🟩🟩🟩
"""
global word
global gameState
gameState = True
global todayDate
todayDate = date.today()


global variables
variables = []


# Set Daily Word
def setDaily(todayDate):
    with open(".daily.txt", "w") as g, open(".wordle.txt", "r") as f:

        if g.readline(0) == todayDate:
            g.close(g)
            print("Today's wordle has already been completed")
        elif g.readlines != todayDate:
            word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")
    return word


def newWord():
    with open(".wordle.txt", "r") as f:
        word = random.choice(f.readlines())
    return word


def menu():
    menuState = False
    print("""Wordle:
    S - Share 
    N - New 
    D - Play Daily
    Q - Quit""")
    while not menuState:
        choice = input(">> ")
        if choice[0].lower() == "s":
            print(solvedOut)
            clipboard = input("""Copy to clipboard?\ny/N\n >> """)
            if clipboard[0].lower() == "y":
                pyperclip.copy(solvedOut)
                print("copied to clipboard")
                continue
            elif clipboard[0].lower == "n":
                print("Not Copied")
                continue
        elif choice[0].lower() == "n":
            print("New game starting")
            newWord()

            # DEBUG USE ONLY
            variables.append("word : {word}")
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            menuState = True
            variables.append("gameState : ")
        elif choice[0].lower() == "d":
            print("Daily game starting")
            with open(".daily.txt") as f:
                word = f.readline(2)

            # DEBUG USE ONLY
            variables.append("word : {word}")
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            menuState = True
            variables.append("gameState : ")
        elif choice[0].lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure[0].lower() == "y":
                print("Closing")
                print("\b")
                for x in range(4, 0):
                    print("\b{x}")
                    x -= 1

                quit()


menu()

if not gameState:
    print("Game started\n")
