import random

secret_number = random.randint(1, 100)
max_attempts = 10

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 10 attempts to guess the number.")

for attempt in range(1, max_attempts + 1):

    guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You won!")
        print(f"You guessed the number in {attempt} attempts.")
        break

    elif guess < secret_number:
        print("The secret number is higher!")

    else:
        print("The secret number is lower!")

else:
    print("\nGame Over! You lost.")
    print(f"The correct number was: {secret_number}")
