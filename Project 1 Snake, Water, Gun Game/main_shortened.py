import random

computer = random.choice([1, 0, -1])
user = input("Enter your choice (s, w, g): ")
yourDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}
reverseDict = {
    1 : "Snake",
    0 : "Gun",
    -1 : "Water"
}

if user not in yourDict:
    print("Invalid input! Please enter s, w, or g.")
else:
    you = yourDict[user]
    print(f"Your choice is {reverseDict[you]}")
    print(f"Computer choice is {reverseDict[computer]}")

    if(you == computer):
        print("Draw")
    else:
        '''
         if (you == 1 and computer == -1): computer - you = -2
            print("You Win! Because Snake drinks the water.")
        elif(you == -1 and computer == 0): computer - you = -1
            print("You Win! Because Water rusts the gun.")
        elif(you == 0 and computer == 1): computer - you = 1
            print("You Win! Because Gun shoots the snake.")
        elif(you == -1 and computer == 1): computer - you = 2
            print("Computer Win! Because Snake drinks the water.")
        elif(you == 0 and computer == -1): computer - you = -1
            print("Computer Win! Because Water rusts the gun.")
        elif(you == 1 and computer == 0): computer - you = -1
            print("Computer Win! Because Gun shoots the snake.")
        else:
            print("Something went wrong!")

        The below logic is on the base of computer - you values 
        ''' 
        if ((computer - you) == -1 or (computer - you) == 2):
            print("You Lose!")
        else:
            print("You Win!")