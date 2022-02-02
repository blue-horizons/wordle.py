# Pretty sure this is redundant as its already implemented

import pyperclip
from time import sleep

solvedOut = """
⬜️⬜️🟨⬜️⬜️
🟩⬜️⬜🟨🟨
🟩🟩⬜️⬜️🟨
🟩🟩🟩🟩🟩
"""


def menu():
    menuState = False
    print("""Wordle:
    S - Share 
    N - New 
    Q - Quit""")
    while not menuState:
        choice = input(">> ")
        if choice[0].lower() == "s":
            print(solvedOut)
            clipboard = input("""Copy to clipboard?\ny/N""")
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
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
        elif choice[0].lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure[0].lower() == "y":
                print("Closing in ")
                print("\b")
                for x in range(4, 0):
                    print("\b{x}")
                    x -= 1

                quit()


menu()
