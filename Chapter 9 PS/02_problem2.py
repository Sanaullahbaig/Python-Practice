import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 100)
    

    # fetch the high score 
    with open("Hi_score.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else: 
            highscore = 0

    print(f"Your score is: {score}")    
    if (score > highscore):
        # write the high score to the file
        with open("Hi_score.txt", "w") as f:
            f.write(str(score))  
        print(f"New high score is: {score}")
    else:
        print("No new high score.")
    return score

game()
    
