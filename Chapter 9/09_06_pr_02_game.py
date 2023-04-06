def game ():
    return 644

score = game()
with open("highscore.txt") as f:
    highscoreStr = f.read()
 
if int(highscoreStr) < score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))