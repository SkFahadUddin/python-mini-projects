#Quiz Game
print("Welcome to the Quiz Game!");
questions=("What is the capital of France?",
           "What is the largest planet in our solar system?",
           "What is the chemical symbol for gold?",
           "Who wrote 'Romeo and Juliet'?",
           "What is the tallest mammal?");
options=(("a. Paris", "b. London", "c. Berlin", "d. Madrid"),
         ("a. Mars", "b. Jupiter", "c. Saturn", "d. Uranus"),
         ("a. Ag", "b. Au", "c. Al", "d. Fe"),
         ("a. Charles Dickens", "b. William Shakespeare", "c. Jane Austen", "d. Mark Twain"),
         ("a. Elephant", "b. Giraffe", "c. Hippopotamus", "d. Blue Whale"));
answers=("a", "b", "b", "b", "b");
guesses=[];
score=0;
print("Type 'exit' to quit the game at any time.\n");
print("Let's start the quiz!\n");
for i in range(len(questions)):
    print(f"Question {i+1} : {questions[i]}");
    print(f"Options : {options[i]}");
    guess=input("Enter your answer (a/b/c/d) : ");
    if guess.lower() == "exit":
        print("Exiting the game. Thank you for playing!");
        break;
    elif guess.lower()<'a' or guess.lower()>'d':
        print("Invalid option. Please enter a valid answer (a/b/c/d).");
        continue;
    else:
        guesses.append(guess.lower());
    print();

for i in range(len(answers)):
    if guesses[i] == answers[i]:
        score += 1
print(f"\nYour final score is: {score}/{len(answers)}")

for i in range(len(answers)):
    print(f"The right answers were : {answers[i]}");