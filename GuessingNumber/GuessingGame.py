# Number guessing game
import random

number = random.randint(1, 100)
max_attempts = 10

print("Welcome to the number guessing game!")
print("Try to guess the number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess the correct number.")

for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if not 1 <= guess <= 100:
        print("Invalid guess. Please enter a number between 1 and 100.")
        continue

    if guess == number:
        print(f"Congratulations! You guessed the correct number {number} in {attempt} attempts.")
        break

    difference = abs(guess - number)
    if difference <= 5:
        print("Very close! Try again.")
    elif difference <= 10:
        print("Close! Try again.")
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    print(f"Sorry, you have used all your attempts. The correct number was {number}. Better luck next time!")
