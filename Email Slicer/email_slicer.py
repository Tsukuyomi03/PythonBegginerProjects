def slice_email(email):
    if '@' not in email:
        return None, None
    
    parts = email.split('@')
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return None, None
    
    username = parts[0]
    domain = parts[1]
    
    return username, domain

def validate_email(email):
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
    
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True

def main():
    print("Welcome to Email Slicer!")
    print("Extract username and domain from email addresses")
    print("-" * 45)
    
    while True:
        email = input("\nEnter an email address (or 'quit' to exit): ").strip()
        
        if email.lower() == 'quit':
            print("Thanks for using Email Slicer!")
            break
        
        if not email:
            print("Error: Please enter an email address.")
            continue
        
        if not validate_email(email):
            print("Error: Please enter a valid email address.")
            continue
        
        username, domain = slice_email(email)
        
        if username and domain:
            print(f"\nEmail: {email}")
            print(f"Username: {username}")
            print(f"Domain: {domain}")
            
            domain_parts = domain.split('.')
            if len(domain_parts) >= 2:
                print(f"Domain Name: {'.'.join(domain_parts[:-1])}")
                print(f"Top Level Domain: {domain_parts[-1]}")
        else:
            print("Error: Could not extract username and domain from the email.")

if __name__ == "__main__":
    main()
