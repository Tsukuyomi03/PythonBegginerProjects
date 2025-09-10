import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("-" * 40)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed it correctly!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempt(s) to win!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempt(s) left.")
            
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1
            
    else:
        print(f"\nGame Over! You've used all {max_attempts} attempts.")
        print(f"The number I was thinking of was {secret_number}")
    
    play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
    if play_again in ['yes', 'y', 'yeah', 'yep']:
        print("\n" + "="*50)
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    number_guessing_game()
