import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not characters:
        return "Error: At least one character type must be selected"
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    
    return password

def get_user_preferences():
    print("Password Generator Configuration")
    print("-" * 30)
    
    try:
        length = int(input("Enter password length (default 12): ") or "12")
        if length < 1:
            length = 12
    except ValueError:
        length = 12
    
    uppercase = input("Include uppercase letters? (y/n, default y): ").lower()
    include_uppercase = uppercase != 'n'
    
    lowercase = input("Include lowercase letters? (y/n, default y): ").lower()
    include_lowercase = lowercase != 'n'
    
    digits = input("Include digits? (y/n, default y): ").lower()
    include_digits = digits != 'n'
    
    symbols = input("Include symbols? (y/n, default y): ").lower()
    include_symbols = symbols != 'n'
    
    return length, include_uppercase, include_lowercase, include_digits, include_symbols

def main():
    print("Welcome to Password Generator!")
    print("=" * 35)
    
    while True:
        print("\nOptions:")
        print("1. Generate password with custom settings")
        print("2. Generate quick strong password (12 chars, all types)")
        print("3. Generate multiple passwords")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            length, upper, lower, digits, symbols = get_user_preferences()
            password = generate_password(length, upper, lower, digits, symbols)
            print(f"\nGenerated Password: {password}")
            
        elif choice == "2":
            password = generate_password()
            print(f"\nGenerated Password: {password}")
            
        elif choice == "3":
            try:
                count = int(input("How many passwords to generate? "))
                length = int(input("Password length (default 12): ") or "12")
                print(f"\nGenerated {count} passwords:")
                print("-" * 30)
                for i in range(count):
                    password = generate_password(length)
                    print(f"{i+1}. {password}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                
        elif choice == "4":
            print("Thank you for using Password Generator!")
            break
            
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
