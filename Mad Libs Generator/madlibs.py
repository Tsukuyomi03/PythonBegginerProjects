def story_one():
    print("Story 1: The Adventure")
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    number = input("Enter a number: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    
    story = f"""
    Once upon a time, {name} was exploring a {adjective1} {noun1}.
    Suddenly, they {verb1} and discovered a {adjective2} {noun2}.
    Inside were {number} {color} {animal}s dancing around in circles.
    {name} couldn't believe their eyes and decided to join the party!
    """
    
    print("\n" + "="*50)
    print("YOUR MAD LIB STORY:")
    print("="*50)
    print(story)

def story_two():
    print("Story 2: The Restaurant")
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    food1 = input("Enter a food: ")
    verb1 = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")
    liquid = input("Enter a liquid: ")
    body_part = input("Enter a body part: ")
    adjective3 = input("Enter another adjective: ")
    food2 = input("Enter another food: ")
    
    story = f"""
    Yesterday, {name} went to a {adjective1} restaurant.
    They ordered {food1} and decided to {verb1} while waiting.
    The waiter was very {adjective2} and spilled {liquid} all over {name}'s {body_part}.
    The food was {adjective3} but tasted like {food2}.
    {name} will never forget this dining experience!
    """
    
    print("\n" + "="*50)
    print("YOUR MAD LIB STORY:")
    print("="*50)
    print(story)

def story_three():
    print("Story 3: The School Day")
    name = input("Enter a student's name: ")
    adjective1 = input("Enter an adjective: ")
    subject = input("Enter a school subject: ")
    verb1 = input("Enter a verb (past tense): ")
    noun1 = input("Enter a noun: ")
    teacher_name = input("Enter a teacher's name: ")
    adjective2 = input("Enter another adjective: ")
    number = input("Enter a number: ")
    object_plural = input("Enter objects (plural): ")
    
    story = f"""
    {name} had a {adjective1} day at school during {subject} class.
    They {verb1} their {noun1} and got in trouble with {teacher_name}.
    The teacher was {adjective2} and made {name} write {number} sentences about {object_plural}.
    From that day on, {name} always remembered to bring their homework!
    """
    
    print("\n" + "="*50)
    print("YOUR MAD LIB STORY:")
    print("="*50)
    print(story)

def story_four():
    print("Story 4: The Vacation")
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective1 = input("Enter an adjective: ")
    transportation = input("Enter a mode of transportation: ")
    activity = input("Enter an activity: ")
    adjective2 = input("Enter another adjective: ")
    weather = input("Enter a type of weather: ")
    emotion = input("Enter an emotion: ")
    souvenir = input("Enter an object: ")
    
    story = f"""
    Last summer, {name} went on vacation to {place}.
    The trip was {adjective1} and they traveled by {transportation}.
    {name} spent most of their time {activity} which was {adjective2}.
    Unfortunately, the weather was {weather} but {name} felt {emotion} anyway.
    They brought home a {souvenir} as a memory of their amazing trip!
    """
    
    print("\n" + "="*50)
    print("YOUR MAD LIB STORY:")
    print("="*50)
    print(story)

def main():
    print("Welcome to the Mad Libs Generator!")
    print("Choose a story to create:")
    print("1. The Adventure")
    print("2. The Restaurant")
    print("3. The School Day")
    print("4. The Vacation")
    
    while True:
        choice = input("\nEnter your choice (1-4) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            print("Thanks for playing Mad Libs! Goodbye!")
            break
        elif choice == '1':
            story_one()
        elif choice == '2':
            story_two()
        elif choice == '3':
            story_three()
        elif choice == '4':
            story_four()
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
        
        play_again = input("\nWould you like to create another story? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing Mad Libs! Goodbye!")
            break

if __name__ == "__main__":
    main()
