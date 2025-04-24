import random
import time

# Global variables (demonstrating scope)
GAME_TITLE = "Health tracking system in boxing game"
MAX_HEALTH = 100

class Boxer:
    def __init__(self, name, health=MAX_HEALTH):
        self.name = name
        self.health = health
        self.blocking = False  # Demonstrating instance variable scope

    # Fruitful function that returns damage value
    def calculate_damage(self, move_type):
        """Calculate damage based on move type (demonstrates strings and returns)"""
        if move_type == "jab":
            return random.randint(5, 10)
        elif move_type == "hook":
            return random.randint(10, 20)
        return 0  # Default return

    def is_knocked_out(self):
        return self.health <= 0

    # Function with string manipulation
    def get_status(self):
        health_bar = "█" * int((self.health / MAX_HEALTH) * 20)
        return f"{self.name}: {health_bar} {self.health} HP"

def print_fighters(player, opponent):
    """Demonstrates string formatting and scoped variables"""
    print("\n" + "="*30)
    print(player.get_status())
    print(opponent.get_status())
    print("="*30 + "\n")

def get_player_move():
    """Demonstrates break/continue in input validation"""
    while True:
        print("\nYour turn:")
        print("1. Jab (quick, less damage)")
        print("2. Hook (slow, more damage)")
        print("3. Block (reduce next damage)")
        print("4. Quit fight")
        
        choice = input("Choose your move (1-4): ").strip()
        
        if choice == "4":
            if confirm_quit():
                return "quit"
            else:
                continue  # Continue the loop if not confirmed
        elif choice in ("1", "2", "3"):
            return choice
        else:
            print("Invalid choice! Please enter 1-4.")
            continue  # Explicit continue statement

def confirm_quit():
    """Fruitful function that returns boolean"""
    response = input("Are you sure you want to quit? (yes/no): ").lower()
    return response.startswith('y')

def apply_effects(attacker, defender, move_type):
    """Demonstrates scoped variables and string operations"""
    if move_type == "1":
        damage = attacker.calculate_damage("jab")
        defender.health -= damage
        print(f"\n{attacker.name.upper()} lands a quick jab! (-{damage} HP)")
    elif move_type == "2":
        damage = attacker.calculate_damage("hook")
        defender.health -= damage
        print(f"\n{attacker.name.upper()} swings a powerful hook! (-{damage} HP)")
    elif move_type == "3":
        attacker.blocking = True
        print(f"\n{attacker.name.upper()} raises guard to block!")

def simple_boxing_game():
    print(GAME_TITLE)
    print("-" * len(GAME_TITLE))
    
    # Get player's name with string validation
    while True:
        player_name = input("Enter your boxer's name: ").strip()
        if player_name:
            break  # Break out of loop if valid name
        print("Name cannot be empty!")

    player = Boxer(player_name)
    opponent = Boxer("The Champion")

    print(f"\n{player.name} vs {opponent.name}!")
    print("Fight starts now!\n")

    while True:
        # Player's turn
        move = get_player_move()
        if move == "quit":
            print("\nYou retreat from the fight!")
            break  # Break out of game loop

        apply_effects(player, opponent, move)

        # Check if opponent is knocked out
        if opponent.is_knocked_out():
            print(f"\nKNOCKOUT! {player.name} wins!")
            break

        # Opponent's turn
        print("\nOpponent's turn...")
        time.sleep(1)

        if random.random() < 0.2:  # 20% chance to block
            opponent.blocking = True
            print(f"{opponent.name} is blocking!")
        else:
            opponent.blocking = False
            damage = random.randint(8, 15)
            
            if player.blocking:
                damage = max(1, damage // 2)
                print(f"{opponent.name} attacks but you block some damage! (-{damage} HP)")
                player.blocking = False  # Reset block after use
            else:
                print(f"{opponent.name} hits you! (-{damage} HP)")
            
            player.health -= damage

        # Check if player is knocked out
        if player.is_knocked_out():
            print(f"\nKNOCKOUT! {opponent.name} wins!")
            break

        # Show status
        print_fighters(player, opponent)
        time.sleep(1)

# Start the game
if __name__ == "__main__":
    simple_boxing_game()
