import random

chances = 0

number = random.randint(1, 10)
print(number)

print("Guess a number between 1 and 10:")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("YOU'VE WON!")
        chances = 7
    elif guess > 10 or guess < 0:
        print("You're number is not in the proper range.")
    elif guess < number:
        print("Guess a number higher than " + str(guess))
        chances = chances + 1
    elif guess > number:
        print("Guess a number lower than " + str(guess))
        chances = chances + 1

if chances == 5:
    print("YOU RAN OUT OF ATTEMPTS, YOU'VE LOST!")
