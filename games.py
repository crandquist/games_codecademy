import random
import helper_methods

#money = 100

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
        #money += int_wager
        #balance()

    else:
        print("You lost {0} dollars. Better luck next time!".format(wager))
        #money -= int_wager
        print("You have {0} dollars!".format(money))

#Cho-Han game functions will be below.
def cho_han():
    print("Welcome to 'Cho Han'!")
    print("In this game we will be rolling two dice and adding the results together. ")
    print("If you can guess correctly if the number is even or odd then you win!")
    print("Let's begin!")
    
    wager = bet()
    int_wager = int(wager)
    e_or_o = input("Do you bet the result is going to be even or odd?")
    
    dice_1 = dice_roll()
    print("The first dice roll was {0}".format(dice_1))
    dice_2 = dice_roll()
    print("The second dice roll was {0}".format(dice_2))
    total_roll = dice_1 + dice_2
    even = None
    
    if total_roll % 2 is 0:
        even = True
    else:
        even = False
    if (even and e_or_o == "even") or (not even and e_or_o == "odd"):
        print("Congratulations! You won {0} dollars!".format(int_wager))
    else:
        print("You lost {0} dollars. Better luck next time!".format(int_wager))

money = 100

#Call your game of chance functions here
coin_flip()

