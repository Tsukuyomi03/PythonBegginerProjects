import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        print("Invalid choice! Please try again.")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'quit' at any time to stop playing.\n")
    
    while True:
        player_choice = get_player_choice()
        
        if player_choice == "quit":
            break
            
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        print(f"Score - You: {player_score}, Computer: {computer_score}\n")
    
    print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
    
    if player_score > computer_score:
        print("Congratulations! You won overall!")
    elif computer_score > player_score:
        print("Computer won overall! Better luck next time!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    play_game()
