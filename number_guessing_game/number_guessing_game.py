

"""
Author: Lee Steffen
Date: 6/16/2026
"""

import random

gen_number = random.randint(1, 100)

while True:
    try: 
        user_guess = int(input("Guess the number between 1 and 100: "))
        
        if (user_guess > gen_number):
            print("Too high!")
        elif (user_guess < gen_number):
            print("Too low!")
        else:
            print("Congradulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")