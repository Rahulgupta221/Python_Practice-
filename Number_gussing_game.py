import random

num =random.randint(1, 100)
print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Guess the number bertween 1 to 100: "))
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {num} correctly!")
        break