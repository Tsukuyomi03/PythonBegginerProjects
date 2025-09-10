import random

def roll_dice(num_dice=1):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def display_results(results):
    print(f"\nRolling {len(results)} dice:")
    print("Results:", " ".join(map(str, results)))
    print(f"Total: {sum(results)}")

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            print("\nOptions:")
            print("1. Roll dice")
            print("2. Exit")
            
            choice = input("\nEnter your choice (1-2): ").strip()
            
            if choice == "1":
                num_dice = int(input("How many dice do you want to roll? "))
                
                if num_dice <= 0:
                    print("Please enter a positive number!")
                    continue
                
                results = roll_dice(num_dice)
                display_results(results)
                
            elif choice == "2":
                print("Thanks for playing!")
                break
                
            else:
                print("Invalid choice! Please enter 1 or 2.")
                
        except ValueError:
            print("Please enter valid numbers only!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
