import random

money = 100

#Write your game of chance functions here
def pick_game():
    pass

def coin_flip():
    print("Welcome to coin flip!")
    print("In this game you will decide whether you want to bet heads or tails and how much money you are betting on.")
    print("If the coin flip results in your favor you will win back your bet.")
    print("If it does not, you will lose that money.")
    print("Here we go!")
    wager = bet()
    int_wager = int(wager)
    h_or_t = heads_or_tails()
    print("Time to flip the coin!")
    flip = random.randint(1, 2)
    if flip == 1:
        print("Heads!")
    elif flip == 2:
        print("Tails!")
    if h_or_t == flip:
        print("Congratulations! You won {0} dollars!".format(wager))
        return int_wager
    else:
        print("You lost {0} dollars. Better luck next time!".format(wager))
        return -int_wager
    

    #Helper function for coin_flip game.
def heads_or_tails():
    h_or_t = input("Call it: heads or tails?\n")
    if h_or_t == "heads":
        return 1
    elif h_or_t == "tails":
        return 2
    else:
        print("Let's try that again. Please enter 'heads' or 'tails'.\n")
        heads_or_tails()

    #Helper function to take user input on bet amount.
def bet():
    money = input("How much would you like to bet on the game?\n")
    return money

#Cho-Han game functions will be below.
def cho_han():
    print("Welcome to 'Cho Han'!")
    print("In this game we will be rolling two dice and adding the results together. ")
    print("If you can guess correctly if the number is even or odd then you win!")
    print("Let's begin!")
    wager = bet()
    int_wager = int(wager)
    e_or_o = input("Do you bet the result is going to be even or odd?")


def dice_roll():
    roll = random.randint(1, 6)
    return roll


#Call your game of chance functions here
coin_flip()

