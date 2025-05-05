#Brandon Malave
#05/03/2025
#P5HW
#Program allows for the user to create two characters, display attributes 
#and simulate an attack sequence using loops, and functions

import random

def display_character(character):
    print(f"\nCharacter: {character['name']}")
    print(f"Health: {character['health']}")
    print(f"Strength: {character['strength']}\n")

def calculate_damage(strength):
    return random.randint(1, strength)

def attack(attacker, defender):
    damage = calculate_damage(attacker['strength'])
    defender['health'] -= damage
    print(f"\n{attacker['name']} attacks {defender['name']} for {damage} damage!")

    if defender ['health'] <= 0:
          print(f"{defender['name']} has been defeated!\n")
    else:
         print(f"{defender['name']}'s health is now {defender['health']}.\n")


def create_character():
    name = input("Enter your character name: ")

    while True:
        try:
            health = int(input("Enter health (e.g. how much pain can they take): "))
            strength = int(input("Enter strength (e.g. how much pain can they dish out before taking a nap): "))
            return {
                'name': name,
                'health': health,
                'strength': strength
            }
        except ValueError:
            print("Invalid input. Please enter numbers for health and strength.")


def main():
    print("=== Welcome to the Combat Game: Pain & Punchlines Edition ===")
    print("Where resilience is tested, strength is flexed, and someone always ends up taking a nap.")

    player1 = None
    player2 = None

    while True:
        print("\nMENU OF MAYHEM")
        print("1. Create Player 1")
        print("2. Create Player 2")
        print("3. Display Players")
        print("4. Let 'Em Fight")
        print("5. Exit the Arena")

        choice = input("Choose your destiny (1-5): ")

        if choice == '1':
            player1 = create_character()
            print(f"{player1['name']} has entered the ring. Let's hope they last longer than my last situationship.")
        elif choice == '2':
            player2 = create_character()
            print(f"{player2['name']} has arrived — probably late, but fashionably so.")
        elif choice == '3':
            if player1:
                print("\nPlayer 1:")
                display_character(player1)
            else:
                print("Player 1 is MIA. Create them first.")
            if player2:
                print("\nPlayer 2:")
                display_character(player2)
            else:
                print("Player 2 is still manifesting.")
        elif choice == '4':
            if player1 and player2:
                attack(player1, player2)
            else:
                print("Nice try, but both players need to exist before you unleash carnage.")
        elif choice == '5':
            print("Exiting the game. May your code be bug-free and your hits always crit.")
            break
        else:
            print("Nah. That's not a valid option. Try 1 through 5 like the legends do.")
main()










