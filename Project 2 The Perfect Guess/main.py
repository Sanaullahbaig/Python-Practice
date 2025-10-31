from random import randint

number = randint(1, 500)
user = -1
guesses = 0
# print(number)

while number != user:
    guesses += 1
    user = int(input("Guess the number: "))

    if (user > number):
        print("Lower Number Please!")
    else:
        print("Higher number please!")

print(f"You guess the correct number is {number} in {guesses} attempts.")