def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def main():
    print("Palindrome Checker")
    print("-" * 17)
    
    while True:
        user_input = input("\nEnter a word or phrase (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()
