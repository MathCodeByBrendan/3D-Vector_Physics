import random

def roll():
    wins = 0
    losses = 0
    balance = 0

    while True:
        while True:
            try:
                guess = int(input("Guess the sum of your rolls for 10 dollars, only loose 1 dollar if wrong: "))
                if guess < 2 or guess > 12:
                    print("Enter a winnable number: must be between 2 - 12 to win!")
                    continue
            except ValueError:
                print("Enter a an integer.")
                continue
            break
        roll1, roll2 = random.randint(1, 6), random.randint(1, 6)
        sum = roll1 + roll2

        if guess == sum:
            wins += 1
            balance += 10
            result_message = "You won $10!"
        else:
            losses += 1
            balance -= 1

        play_again = input(f"You rolled {roll1}, and {roll2}. Your total is {sum}. You won {wins} times, and lost {losses} times. Your balance is {balance}. Would you like to roll again? Enter 'y' for yes, 'n' for no: ").lower().strip()

        if play_again == 'y':
            continue
        else:
            break

roll()
