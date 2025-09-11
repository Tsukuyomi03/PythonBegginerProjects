import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    return " " not in board

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return move
            else:
                print("Error: Please enter a number between 1 and 9. Try again.")
        except ValueError:
            print("Error: Please enter a valid number. Try again.")

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print()
    
    while True:
        board = [" "] * 9
        current_player = "X"
        
        while True:
            clear_screen()
            print_board(board)
            print()
            
            move = get_move(current_player)
            
            if board[move] != " ":
                print("That position is already taken. Try again.")
                continue
            
            board[move] = current_player
            
            winner = check_winner(board)
            if winner:
                clear_screen()
                print_board(board)
                print(f"Player {winner} wins the game!")
                break
            
            if is_board_full(board):
                clear_screen()
                print_board(board)
                print("It's a tie!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
