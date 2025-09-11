def generate_acronym(phrase):
    if not phrase.strip():
        return ""
    
    words = phrase.strip().split()
    acronym = ""
    
    for word in words:
        if word and word[0].isalpha():
            acronym += word[0].upper()
    
    return acronym

def generate_acronym_with_options(phrase, include_articles=False):
    if not phrase.strip():
        return ""
    
    articles = ['a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']
    words = phrase.strip().split()
    acronym = ""
    
    for word in words:
        if word and word[0].isalpha():
            if include_articles or word.lower() not in articles:
                acronym += word[0].upper()
    
    return acronym

def main():
    print("Welcome to Acronym Generator!")
    print("Create acronyms from phrases")
    print("-" * 30)
    
    while True:
        phrase = input("\nEnter a phrase (or 'quit' to exit): ").strip()
        
        if phrase.lower() == 'quit':
            print("Thanks for using Acronym Generator!")
            break
        
        if not phrase:
            print("Error: Please enter a phrase.")
            continue
        
        basic_acronym = generate_acronym(phrase)
        filtered_acronym = generate_acronym_with_options(phrase, include_articles=False)
        
        print(f"\nPhrase: {phrase}")
        print(f"Basic Acronym: {basic_acronym}")
        
        if basic_acronym != filtered_acronym:
            print(f"Filtered Acronym (excluding common words): {filtered_acronym}")
        
        choice = input("\nWould you like to include common words? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            full_acronym = generate_acronym_with_options(phrase, include_articles=True)
            print(f"Full Acronym (including all words): {full_acronym}")
        
        print("\n" + "=" * 40)

if __name__ == "__main__":
    main()
