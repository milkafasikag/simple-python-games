import random

def roll_dice(num_dice, num_sides):
    print(f"Rolling {num_dice} dice with {num_sides} sides each...")
    print("Results:")

    for _ in range(num_dice):
        result = random.randint(1, num_sides)
        print(result)

def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        if num_dice <= 0 or num_sides <= 0:
            print("Invalid input. Number of dice and number of sides must be positive.")
            continue

        roll_dice(num_dice, num_sides)

        play_again = input("Do you want to roll the dice again? (yes/no): ")

        if play_again.lower() != "yes":
            break

dice_rolling_simulator()