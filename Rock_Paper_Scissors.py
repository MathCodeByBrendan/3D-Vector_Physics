import random

options = {
    'h': 'heads',
    't': 'tails'
}

def play():
    while True:
        comp_selection = options.random.choice()

        while True:
            user_choice = input("To play choose heads or tails. 't' for tails, 'h' for heads: ")
            if user_choice in options:
                user_selection = options.get(user_choice)
                break
            else:
                print("Enter t or h, JACKASS!!!")
                continue
        if comp_selection == user_selection:
            print("Correct!")
        else:
            print("False")
        
        play_again = input("Would you like to play again, press 'y' for yes, anything else for no: ").lower().strip()
        if play_again == 'y':
            continue
        else:
            break
play()