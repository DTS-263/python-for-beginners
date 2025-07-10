def playRockPaperScissor():
    choice = input("Rock, Paper or Scissor? (r/p/s)")
    if choice not in ['r', 'p', 's']:
        print("Please enter the correct choice from Rock, Paper or Scissor (r/p/s)")
        return
    else:
        import random
        computerChoice = random.randint(1,3)
        computerChoiceChar = 'r'
        if computerChoice == 2:
            computerChoiceChar = 'p'
        elif computerChoice == 3:
            computerChoiceChar = 's'
        winner = checkResult(choice, computerChoiceChar)
        print(f"Your choice {displayEmoji(choice)}")
        print(f"Computer's choice {displayEmoji(computerChoiceChar)}")
        if winner == 0:
            print("Its a draw")
        elif winner == 1:
            print("You lose")
        elif winner == -1:
            print("You win")
        
            
def checkResult(choice, computerChoiceChar):
    if choice == computerChoiceChar:
        return 0
    elif choice == 'r' and computerChoiceChar == 'p':
        return 1
    elif choice == 'r' and computerChoiceChar == 's':
        return -1
    elif choice == 'p' and computerChoiceChar == 'r':
        return -1
    elif choice == 's' and computerChoiceChar == 'r':
        return 1
    elif choice == 'p' and computerChoiceChar == 's':
        return 1
    elif choice == 's' and computerChoiceChar == 'p':
        return -1
        
def displayEmoji(choice):
    if choice == 'r':
        return '🪨'
    elif choice == 'p':
        return '📃'
    elif choice == 's':
        return '✂️'
    
while True:
    playGame = input("You want to play the Rock, Paper, Scissors game? (y/n)")
    if playGame == 'n':
        break
    else:
        playRockPaperScissor()