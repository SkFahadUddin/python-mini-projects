import random


WORDS = [
    "apple", "candy", "cabin", "caper", "cater", "cider", "cocoa",
    "crane", "dream", "drift", "eagle", "flame", "glide", "grape",
    "green", "hello", "latch", "lemon", "light", "mango", "magic",
    "night", "ocean", "pearl", "piano", "plant", "pride", "quick",
    "quiet", "river", "roast", "shine", "smile", "sound", "spice",
    "stare", "stone", "storm", "tiger", "trail", "water", "whale",
    "world", "write", "zebra",
]


def main():
    answer = random.choice(WORDS)
    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 tries.")

    for attempt in range(6):
        guess = input(f"Guess {attempt + 1}: ").lower()

        if len(guess) != 5:
            print("Please enter exactly 5 letters.")
            continue

        if guess == answer:
            print("You got it!")
            return

        hint = ""
        for i in range(5):
            if guess[i] == answer[i]:
                hint += guess[i]
            else:
                hint += "_"

        print("Correct positions:", hint)

    print("Out of guesses! The word was", answer)


if __name__ == "__main__":
    main()
