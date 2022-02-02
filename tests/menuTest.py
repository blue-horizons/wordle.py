import pyperclip
from time import sleep
import random
from datetime import date
solvedOut = """
⬜️⬜️🟨⬜️⬜️
🟩⬜️⬜🟨🟨
🟩🟩⬜️⬜️🟨
🟩🟩🟩🟩🟩
"""

global variables
variables = {}


# Set Daily Word
def setDaily(todayDate,word):
    with open("daily.txt", "w") as g, open("wordle.txt","r") as f:
    
        if g.readline(0) == todayDate:
            close(g)
        elif g.readlines != todayDate:
            word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")

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
            word = random.choice(f.readlines())
            # DEBUG USE ONLY
            variables.append("word : {word}")
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            variables.append("gameState : ")
        elif choice[0].lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure[0].lower() == "y":
                print("Closing")
                print("\b")
                time.sleep(5)
                quit()
        elif choice[0].lower() == "d":
            print("Daily starting")
            with open("daily.txt","r") as f:
                lastPlayed = f.readline(0)
                word = f.readline(1)
            if lastPlayed == date.today():
                print("You've already played today's daily Wordle. \nPlease come back tomorrow.")
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            setDaily()

menu()

print()

