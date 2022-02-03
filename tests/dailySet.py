from datetime import date
import random





today = date.today()
todayDate = today.strftime("%d/%m/%Y")

with open(".daily.txt", "r+") as g:
        if g.readline(0) == todayDate:
            g.close()
            print("Today's wordle has already been completed")
        elif g.readlines != todayDate:
            with open(".wordle.txt") as f:
                word = random.choice(f.readlines())
            g.seek(0)
            g.write(f"{todayDate}\n{word}")
            g.truncate()

print(word)