# Dice Rolling Simulator

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice (or type 'quit' to exit): ")
    print(f"You rolled a {roll_dice()}")
    if input("Roll again? (yes to continue, no to exit): ").lower() == "no":
        break
