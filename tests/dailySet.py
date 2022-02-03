from datetime import date
from random import choice





today = date.today()
todayDate = today.strftime("%d/%m/%Y")

with open(".daily.txt", "r+") as g:
        if g.readline(0) == todayDate:
            g.close()
            print("Today's wordle has already been completed")
        elif g.readlines != todayDate:
            with open(".wordle.txt") as f:
                word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")

print("word")