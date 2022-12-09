import random 

moves = ("rock", "paper", "scissors")
computer = random.choice(moves)

player = input("Enter rock, paper or scissor: ")

if player == computer:
    print("It is a tie.")
elif player == "rock" and computer == "scissor":
    print("You win.")
elif player == "paper" and computer == "rock":
    print("You win.")
elif player == "scissor" and computer == "paper":
    print("You win.")
else:
    print("You lose.")
