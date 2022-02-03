



with open(".daily.txt", "r+") as g:
        if g.readline(0) != todayDate:
            g.close(g)
            print("Today's wordle has already been completed")
        elif g.readlines == todayDate:
            with open(".wordle.txt") as f:
                word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")