import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}
    
    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)
    
    def add_contact(self, name, phone="", email="", address=""):
        if name.lower() in [contact.lower() for contact in self.contacts.keys()]:
            return False
        
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        self.save_contacts()
        return True
    
    def view_contact(self, name):
        for contact_name, details in self.contacts.items():
            if contact_name.lower() == name.lower():
                return contact_name, details
        return None, None
    
    def update_contact(self, name, phone=None, email=None, address=None):
        for contact_name in self.contacts.keys():
            if contact_name.lower() == name.lower():
                if phone is not None:
                    self.contacts[contact_name]["phone"] = phone
                if email is not None:
                    self.contacts[contact_name]["email"] = email
                if address is not None:
                    self.contacts[contact_name]["address"] = address
                self.save_contacts()
                return True
        return False
    
    def delete_contact(self, name):
        for contact_name in list(self.contacts.keys()):
            if contact_name.lower() == name.lower():
                del self.contacts[contact_name]
                self.save_contacts()
                return True
        return False
    
    def search_contacts(self, query):
        results = []
        query = query.lower()
        for name, details in self.contacts.items():
            if (query in name.lower() or 
                query in details["phone"] or 
                query in details["email"].lower() or 
                query in details["address"].lower()):
                results.append((name, details))
        return results
    
    def list_all_contacts(self):
        return sorted(self.contacts.items())
    
    def get_contact_count(self):
        return len(self.contacts)

def display_contact(name, details):
    print(f"\nName: {name}")
    print(f"Phone: {details['phone'] if details['phone'] else 'Not provided'}")
    print(f"Email: {details['email'] if details['email'] else 'Not provided'}")
    print(f"Address: {details['address'] if details['address'] else 'Not provided'}")

def main():
    contact_book = ContactBook()
    
    print("Welcome to Contact Book!")
    print("Manage your contacts easily")
    print("-" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Contact Statistics")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            name = input("Enter name: ").strip()
            if not name:
                print("Error: Name is required.")
                continue
            
            phone = input("Enter phone (optional): ").strip()
            email = input("Enter email (optional): ").strip()
            address = input("Enter address (optional): ").strip()
            
            if contact_book.add_contact(name, phone, email, address):
                print(f"Contact '{name}' added successfully!")
            else:
                print("Error: Contact already exists.")
        
        elif choice == '2':
            name = input("Enter name to view: ").strip()
            if not name:
                print("Error: Please enter a name.")
                continue
            
            contact_name, details = contact_book.view_contact(name)
            if details:
                display_contact(contact_name, details)
            else:
                print("Contact not found.")
        
        elif choice == '3':
            name = input("Enter name to update: ").strip()
            if not name:
                print("Error: Please enter a name.")
                continue
            
            contact_name, details = contact_book.view_contact(name)
            if not details:
                print("Contact not found.")
                continue
            
            print(f"\nCurrent details for {contact_name}:")
            display_contact(contact_name, details)
            
            print("\nEnter new details (press Enter to keep current value):")
            phone = input(f"Phone ({details['phone']}): ").strip()
            email = input(f"Email ({details['email']}): ").strip()
            address = input(f"Address ({details['address']}): ").strip()
            
            phone = phone if phone else None
            email = email if email else None
            address = address if address else None
            
            if contact_book.update_contact(name, phone, email, address):
                print("Contact updated successfully!")
            else:
                print("Error updating contact.")
        
        elif choice == '4':
            name = input("Enter name to delete: ").strip()
            if not name:
                print("Error: Please enter a name.")
                continue
            
            contact_name, details = contact_book.view_contact(name)
            if not details:
                print("Contact not found.")
                continue
            
            confirm = input(f"Are you sure you want to delete '{contact_name}'? (y/n): ").lower().strip()
            if confirm in ['y', 'yes']:
                if contact_book.delete_contact(name):
                    print("Contact deleted successfully!")
                else:
                    print("Error deleting contact.")
            else:
                print("Deletion cancelled.")
        
        elif choice == '5':
            query = input("Enter search term: ").strip()
            if not query:
                print("Error: Please enter a search term.")
                continue
            
            results = contact_book.search_contacts(query)
            if results:
                print(f"\nFound {len(results)} contact(s):")
                for i, (name, details) in enumerate(results, 1):
                    print(f"\n{i}.")
                    display_contact(name, details)
            else:
                print("No contacts found.")
        
        elif choice == '6':
            contacts = contact_book.list_all_contacts()
            if contacts:
                print(f"\nAll Contacts ({len(contacts)} total):")
                for i, (name, details) in enumerate(contacts, 1):
                    print(f"\n{i}.")
                    display_contact(name, details)
            else:
                print("No contacts found.")
        
        elif choice == '7':
            count = contact_book.get_contact_count()
            print(f"\nContact Statistics:")
            print(f"Total contacts: {count}")
            
            if count > 0:
                contacts_with_phone = sum(1 for _, details in contact_book.contacts.items() if details['phone'])
                contacts_with_email = sum(1 for _, details in contact_book.contacts.items() if details['email'])
                contacts_with_address = sum(1 for _, details in contact_book.contacts.items() if details['address'])
                
                print(f"Contacts with phone: {contacts_with_phone}")
                print(f"Contacts with email: {contacts_with_email}")
                print(f"Contacts with address: {contacts_with_address}")
        
        elif choice == '8':
            print("Thanks for using Contact Book!")
            break
        
        else:
            print("Error: Please enter a valid choice (1-8).")

if __name__ == "__main__":
    main()
