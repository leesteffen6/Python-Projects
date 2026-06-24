

import random




while True:
    user_response = input("Roll the dice? (y/n): ")
    if (user_response == "y"):
        print("(" + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ")")
        # pass
    elif (user_response == "n"):
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
