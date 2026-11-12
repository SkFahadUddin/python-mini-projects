#Rock paper scissors game
import random

options = ("rock", "paper", "scissors")
ai_choice = random.choice(options)
tries = 1
runb=True
while runb:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        if(ai_choice==choice):
                print(f"AI chose {ai_choice}. It's a tie!\nTotal Tries : {tries}");
                tries+=1;
        elif((ai_choice=="rock" and choice=="scissors") or (ai_choice=="paper" and choice=="rock") or (ai_choice=="scissors" and choice=="paper")):
                print(f"AI chose {ai_choice}. You lose!\nTotal Tries : {tries}");
                tries+=1;
        else:
                print(f"AI chose {ai_choice}. You win! \nTotal Tries : {tries}");
                break;