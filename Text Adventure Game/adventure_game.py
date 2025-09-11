import random
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.gold = 50
        self.location = "village"
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def has_item(self, item):
        return item in self.inventory
    
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
    
    def is_alive(self):
        return self.health > 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_text(text):
    print(text)

def display_status(player):
    print(f"\n--- {player.name}'s Status ---")
    print(f"Health: {player.health}/100")
    print(f"Gold: {player.gold}")
    print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")
    print(f"Location: {player.location.title()}")

def get_choice(options):
    while True:
        try:
            print("\nChoose an option:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            choice = int(input("\nEnter your choice: ")) - 1
            if 0 <= choice < len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def village_scene(player):
    clear_screen()
    print_text(f"{player.name}, you stand in the center of a peaceful village.")
    print_text("The sun shines brightly overhead, and villagers go about their daily tasks.")
    print_text("You see several paths leading away from the village square.")
    
    options = [
        "Visit the weapon shop",
        "Go to the forest",
        "Explore the caves",
        "Rest at the inn",
        "Check your status"
    ]
    
    choice = get_choice(options)
    
    if choice == 0:
        return weapon_shop_scene(player)
    elif choice == 1:
        return forest_scene(player)
    elif choice == 2:
        return cave_scene(player)
    elif choice == 3:
        return inn_scene(player)
    else:
        display_status(player)
        input("\nPress Enter to continue...")
        return village_scene(player)

def weapon_shop_scene(player):
    player.location = "weapon shop"
    clear_screen()
    print_text("You enter a dimly lit weapon shop.")
    print_text("The shopkeeper, an old dwarf, greets you with a smile.")
    print_text("'Welcome, adventurer! I have fine weapons for sale.'")
    
    options = [
        "Buy a sword (30 gold)",
        "Buy a shield (25 gold)",
        "Buy a healing potion (15 gold)",
        "Leave the shop"
    ]
    
    choice = get_choice(options)
    
    if choice == 0:
        if player.gold >= 30:
            player.gold -= 30
            player.add_item("sword")
            print_text("You purchased a sharp sword!")
        else:
            print_text("You don't have enough gold.")
        input("\nPress Enter to continue...")
    elif choice == 1:
        if player.gold >= 25:
            player.gold -= 25
            player.add_item("shield")
            print_text("You purchased a sturdy shield!")
        else:
            print_text("You don't have enough gold.")
        input("\nPress Enter to continue...")
    elif choice == 2:
        if player.gold >= 15:
            player.gold -= 15
            player.add_item("healing potion")
            print_text("You purchased a healing potion!")
        else:
            print_text("You don't have enough gold.")
        input("\nPress Enter to continue...")
    else:
        player.location = "village"
        return village_scene(player)
    
    return weapon_shop_scene(player)

def forest_scene(player):
    player.location = "forest"
    clear_screen()
    print_text("You venture into the dark forest.")
    print_text("Tall trees surround you, and you hear strange sounds in the distance.")
    
    encounter = random.choice(["goblin", "treasure", "nothing"])
    
    if encounter == "goblin":
        return goblin_fight(player)
    elif encounter == "treasure":
        return find_treasure(player)
    else:
        print_text("You walk through the forest peacefully.")
        print_text("After some time, you decide to head back.")
        input("\nPress Enter to continue...")
        player.location = "village"
        return village_scene(player)

def goblin_fight(player):
    print_text("Suddenly, a goblin jumps out from behind a tree!")
    print_text("The goblin snarls and prepares to attack!")
    
    goblin_health = 50
    
    while goblin_health > 0 and player.is_alive():
        options = ["Attack", "Use healing potion", "Try to run away"]
        choice = get_choice(options)
        
        if choice == 0:
            if player.has_item("sword"):
                damage = random.randint(20, 30)
                print_text(f"You slash the goblin with your sword for {damage} damage!")
            else:
                damage = random.randint(10, 15)
                print_text(f"You punch the goblin for {damage} damage!")
            
            goblin_health -= damage
            
            if goblin_health > 0:
                goblin_damage = random.randint(15, 25)
                if player.has_item("shield"):
                    goblin_damage = max(5, goblin_damage - 10)
                    print_text(f"The goblin attacks, but your shield blocks some damage! You take {goblin_damage} damage.")
                else:
                    print_text(f"The goblin claws you for {goblin_damage} damage!")
                player.take_damage(goblin_damage)
        
        elif choice == 1:
            if player.has_item("healing potion"):
                player.remove_item("healing potion")
                player.heal(30)
                print_text("You drink the healing potion and recover 30 health!")
            else:
                print_text("You don't have a healing potion!")
                continue
        
        else:
            if random.choice([True, False]):
                print_text("You successfully escape from the goblin!")
                player.location = "village"
                return village_scene(player)
            else:
                print_text("The goblin blocks your escape!")
        
        if goblin_health > 0 and choice != 0:
            goblin_damage = random.randint(10, 20)
            if player.has_item("shield"):
                goblin_damage = max(5, goblin_damage - 10)
            player.take_damage(goblin_damage)
            print_text(f"The goblin attacks you for {goblin_damage} damage!")
        
        if player.health <= 20:
            print_text(f"You're badly injured! Health: {player.health}")
    
    if not player.is_alive():
        return game_over(player)
    
    if goblin_health <= 0:
        gold_found = random.randint(10, 25)
        player.gold += gold_found
        print_text(f"You defeated the goblin and found {gold_found} gold!")
        input("\nPress Enter to continue...")
        player.location = "village"
        return village_scene(player)

def find_treasure(player):
    print_text("You discover a hidden treasure chest!")
    treasure_type = random.choice(["gold", "potion", "artifact"])
    
    if treasure_type == "gold":
        gold_amount = random.randint(20, 50)
        player.gold += gold_amount
        print_text(f"You found {gold_amount} gold coins!")
    elif treasure_type == "potion":
        player.add_item("healing potion")
        print_text("You found a healing potion!")
    else:
        player.add_item("magic amulet")
        print_text("You found a mysterious magic amulet!")
    
    input("\nPress Enter to continue...")
    player.location = "village"
    return village_scene(player)

def cave_scene(player):
    player.location = "caves"
    clear_screen()
    print_text("You enter a dark cave system.")
    print_text("Water drips from the ceiling, and your footsteps echo.")
    
    if not player.has_item("magic amulet"):
        print_text("You hear a deep growling sound...")
        print_text("A massive dragon appears from the depths!")
        print_text("Without magical protection, you quickly retreat!")
        input("\nPress Enter to continue...")
        player.location = "village"
        return village_scene(player)
    else:
        print_text("Your magic amulet glows brightly!")
        print_text("You discover an ancient treasure room!")
        player.gold += 100
        print_text("You found 100 gold and ancient artifacts!")
        print_text("Congratulations! You've completed the adventure!")
        return victory_scene(player)

def inn_scene(player):
    player.location = "inn"
    clear_screen()
    print_text("You enter the cozy village inn.")
    print_text("The innkeeper welcomes you warmly.")
    
    options = [
        "Rest and heal (10 gold)",
        "Buy a meal (5 gold)",
        "Listen to rumors",
        "Leave the inn"
    ]
    
    choice = get_choice(options)
    
    if choice == 0:
        if player.gold >= 10:
            player.gold -= 10
            player.heal(50)
            print_text("You rest peacefully and recover your strength!")
        else:
            print_text("You don't have enough gold for a room.")
        input("\nPress Enter to continue...")
    elif choice == 1:
        if player.gold >= 5:
            player.gold -= 5
            player.heal(15)
            print_text("You enjoy a delicious meal and feel refreshed!")
        else:
            print_text("You don't have enough gold for a meal.")
        input("\nPress Enter to continue...")
    elif choice == 2:
        rumors = [
            "I heard there's treasure hidden in the forest...",
            "The caves are dangerous, but they say there's great reward for the brave...",
            "A magic amulet might protect you from ancient evils...",
            "Goblins have been seen near the forest path lately..."
        ]
        print_text(f"Innkeeper: '{random.choice(rumors)}'")
        input("\nPress Enter to continue...")
    else:
        player.location = "village"
        return village_scene(player)
    
    return inn_scene(player)

def game_over(player):
    clear_screen()
    print_text(f"{'='*50}")
    print_text("GAME OVER")
    print_text(f"{'='*50}")
    print_text(f"Unfortunately, {player.name}, your adventure has come to an end.")
    print_text(f"Final gold: {player.gold}")
    print_text("Better luck next time!")
    return False

def victory_scene(player):
    clear_screen()
    print_text(f"{'='*50}")
    print_text("VICTORY!")
    print_text(f"{'='*50}")
    print_text(f"Congratulations, {player.name}!")
    print_text("You have successfully completed the adventure!")
    print_text(f"Final gold: {player.gold}")
    print_text(f"Final inventory: {', '.join(player.inventory)}")
    print_text("You are now a legendary adventurer!")
    return False

def main():
    print_text("Welcome to the Text Adventure Game!")
    print_text("=" * 40)
    
    name = input("Enter your character's name: ").strip()
    if not name:
        name = "Adventurer"
    
    player = Player(name)
    
    print_text(f"\nWelcome, {player.name}!")
    print_text("Your adventure begins now...")
    
    game_running = True
    while game_running and player.is_alive():
        if player.location == "village":
            game_running = village_scene(player)
        else:
            game_running = village_scene(player)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
