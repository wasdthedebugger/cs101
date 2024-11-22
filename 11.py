import random

balance = 1000

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def play_game():
    global balance
    print("Your balance is", balance)
    bet_amount = int(input("Enter your bet amount: "))
    if bet_amount > balance:
        print("You don't have enough balance")
        exit()
        
    balance -= bet_amount
    dice = roll_dice()
    print("You rolled", dice)

    if dice == 7 or dice == 11:
        balance += bet_amount * 2
        print("You won! Your balance is now", balance)
        
    elif dice == 2 or dice == 3 or dice == 12:
        print("You lost! Your balance is now", balance)
        
    else:
        point = dice
        print("Point is", point)
        while True:
            input("Press Enter to roll the dice")
            dice = roll_dice()
            print("You rolled", dice)
            print("Point is", point)
            if dice == point:
                balance += bet_amount * 2
                print("You won! Your balance is now", balance)
                break
            elif dice == 7:
                print("You lost! Your balance is now", balance)
                break
    return balance

while True:
    play_game()
