import random

money = 100

#Write your game of chance functions here
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
    


def heads_or_tails():
    h_or_t = input("Call it: heads or tails?\n")
    if h_or_t == "heads":
        return "heads"
    elif h_or_t == "tails":
        return "tails"
    else:
        print("Let's try that again. Please enter 'heads' or 'tails'.\n")
        heads_or_tails()

def bet():
    money = input("How much would you like to bet on the game?\n")
    return money



#Call your game of chance functions here
coin_flip()

