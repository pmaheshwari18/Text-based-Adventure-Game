# Text-based Adventure Game

# Game Story
print("Welcome to the Text-based Adventure Game!")
print("You find yourself in a mysterious forest. Your goal is to find a way out.")

# Game Logic
inventory = []

def handle_player_progress(choice):
    # Implement logic for handling player progress
    if choice == "1":
        print("You find a key.")
        inventory.append("key")
    elif choice == "2":
        print("You discover a hidden path.")
    else:
        print("Invalid choice.")

def handle_game_end():
    # Implement logic for the game's ending
    if "key" in inventory:
        print("Congratulations! You have found the key and escaped the forest.")
    else:
        print("You couldn't find the key. You are still trapped in the forest.")

# User Interaction
def game_start():
    # Game setup
    print("You are in a forest. You can see a path to your left and a path to your right.")
    print("1. Go left")
    print("2. Go right")

def main_game_loop():
    # Main game loop
    while True:
        choice = input("Enter your choice: ")
        handle_player_progress(choice)
        if "key" in inventory or choice.lower() == "exit":
            break

def game_end():
    # Game ending
    handle_game_end()

# Game Execution
if __name__ == "__main__":
    game_start()
    main_game_loop()
    game_end()
