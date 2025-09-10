import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(wrong_guesses):
    stages = [
        "",
        "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    return stages[wrong_guesses]

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_game():
    words = ["python", "hangman", "computer", "programming", "challenge", "keyboard", "monitor", "software", "hardware", "internet"]
    
    word = random.choice(words).lower()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 8
    
    while wrong_guesses < max_wrong:
        clear_screen()
        print(display_hangman(wrong_guesses))
        print()
        print("Word:", display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print()
        
        if set(word) <= guessed_letters:
            clear_screen()
            print(display_hangman(wrong_guesses))
            print()
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"The word was: {word.upper()}")
            print(f"You guessed it with {max_wrong - wrong_guesses} mistakes to spare!")
            return True
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
    
    clear_screen()
    print(display_hangman(wrong_guesses))
    print()
    print("💀 YOU LOSE! 💀")
    print(f"The word was: {word.upper()}")
    print("Better luck next time!")
    return False

def main():
    print("Welcome to Hangman!")
    print("Guess the word letter by letter.")
    print()
    
    while True:
        won = play_game()
        print()
        
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing Hangman! Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()
