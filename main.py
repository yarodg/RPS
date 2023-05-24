import random
import os

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds = 5
user_name = input("Type your name: ")

while rounds != 0:
    print(f"Rounds left: {rounds}")

    while True:
        user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        os.system("cls")

        if user >= 3 or user < 0:
            print("Invalid number. Try again")
        else:
            print("You chose: ", choices[user])

            computer = random.randint(0, 2)

            print("Computer chose: ", choices[computer])
            break

    if user == computer:
        print("Its a draw.")
        rounds -= 1
    elif user == 0 and computer == 2:
        print("You win.")
        user_score += 1
        rounds -= 1
    elif computer == 0 and user == 2:
        print("You lose.")
        computer_score += 1
        rounds -= 1
    elif computer > user:
        print("You lose.")
        computer_score += 1
        rounds -= 1
    elif user > computer:
        user_score += 1
        rounds -= 1
        print("You win.")

print("\nFINAL SCORE:")

if user_score == computer_score:
    print(f"{user_name}: {user_score} | Computer: {computer_score}")
    print("It's a draw!")
elif user_score > computer_score:
    print(f"{user_name}: {user_score} | Computer: {computer_score}")
    print("You've won!")

else:
    print(f"{user_name}: {user_score} | Computer: {computer_score}")
    print("You've lost!")
