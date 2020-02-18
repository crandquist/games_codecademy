import random

money = 100

#Write your game of chance functions here
def pick_game():
    pass

def balance():
    print("You have {0} dollars.".format(money))

def try_again(game):
    y_or_n = input("Would you like to try again? Enter 'y' or 'n'")
    if y_or_n == "y":
        game()
    elif y_or_n == "n":
        print("Thank you for playing!")
        new_game = input("Would you like to play another game? Enter 'y' or 'n'.")
        if new_game == "y":
            pick_game()
        elif new_game == "n":
            return print ("See you next time!")
        else:
            print("Whoops. Please enter 'y' or 'n'.")
            try_again(game)


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

    


def dice_roll():
    roll = random.randint(1, 6)
    return roll


#Call your game of chance functions here
coin_flip()

