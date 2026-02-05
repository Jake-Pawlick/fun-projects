# A simple Rock-Paper-Scissor game played against the computer (random integer generator)
import random
wins = 0
compwins = 0
def introchoose():
    userchoice = input("enter your choice (rock, paper, or scissors): ")
    if userchoice == "rock":
        return 1
    elif userchoice == "paper":
        return 2
    elif userchoice == "scissors":
        return 3
    else:
        print("invalid choice, please try again.")
        return introchoose()
    
def computerchoose():
    computerchoice = random.randint(1,3)
    if computerchoice == 1:
            print("computer chose rock")
            return 1
    elif computerchoice == 2:
            print("computer chose paper")
            return 2
    elif computerchoice == 3:
            print("computer chose scissors")
            return 3
    
def determin_winner(user, computer):
    if user == computer:
        print ("\nIt's a tie!\n")
    elif user == 1 and computer == 2 or user == 2 and computer == 3 or user == 3 and computer == 1:
        print ("\ncomputer won\n")
        return 0
    elif user == 1 and computer == 3 or user == 2 and computer == 1 or user == 3 and computer == 2:
        print ("\nyou won!\n")
        return 1

def round():
    rounds = input("How many rounds do you want to play? ")
    if rounds.isdigit():
        return int(rounds)
    else:
        print("invalid input, please try again.")
        return round()
    
print("Welcome to Rock, Paper, Scissors!")
rounds = round()
for i in range(rounds):
        user = introchoose()
        computer = computerchoose()
        result = determin_winner(user, computer)
        if result == 1:
            wins += 1
        elif result == 0:
            compwins += 1
if wins > compwins:
    print(f"YOU BEAT THAT DIRTY CLANKER! You won {wins} rounds and the computer won {compwins} rounds.")
elif compwins > wins:
    print(f"broooooooo! You let that clanker beat you??!! The computer won {compwins} rounds and you won {wins} rounds :(")
elif compwins == wins:
    print(f"wow, you tied with the computer... You both won {wins} rounds.")