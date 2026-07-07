import random

number = random.randint(1, 10)

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it correctly.")
        break