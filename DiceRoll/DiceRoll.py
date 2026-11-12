#Dice rolling program
import random
print(f"Welcome to the dice roller");
die_art={
    1: "┌─────┐\n│     │\n│  ●  │\n│     │\n└─────┘",
    2: "┌─────┐\n│ ●   │\n│     │\n│   ● │\n└─────┘",
    3: "┌─────┐\n│ ●   │\n│  ●  │\n│   ● │\n└─────┘",
    4: "┌─────┐\n│ ● ● │\n│     │\n│ ● ● │\n└─────┘",
    5: "┌─────┐\n│ ● ● │\n│  ●  │\n│ ● ● │\n└─────┘",
    6: "┌─────┐\n│ ● ● │\n│ ● ● │\n│ ● ● │\n└─────┘",
}

num=int(input(f"How many dice to roll ? : "))
dice=[]
total=0;
for roll in range(num):
    dice.append(random.randint(1,6))
    total+=dice[roll]

for row in zip(*(die_art[value].splitlines() for value in dice)):
    print("  ".join(row))
