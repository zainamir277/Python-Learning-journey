# A Python Program: Game Function Using a File.
"""The game function in a program lets a user play a game and returns the score as an integer. 
You need to read a file Hi-score.txt which is either blank or contains the previous Hi-score. 
You need to write a program to update the high score whenever the game() function breaks the high score."""
def game():
    with open("game.txt") as f:
        data=f.read()
    if data=="":
        hiscore=0
    else:
        hiscore=int(data)
    score=int(input("Enter your score : "))
    if score>hiscore:
        print("Congrats! You created a new high-score, High-score:",(score))
        with open("game.txt", "w") as f:
            f.write(str(score))
    else:
        print("Your score is less then High-score, High-score:",(hiscore))