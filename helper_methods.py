
def balance(money):
    print("You have {0} dollars.".format(money))

def bet():
    money = input("How much would you like to bet on the game?\n")
    return money

def dice_roll():
    roll = random.randint(1, 6)
    return roll

def heads_or_tails():
    h_or_t = input("Call it: heads or tails?\n")
    if h_or_t == "heads":
        return 1
    elif h_or_t == "tails":
        return 2
    else:
        print("Let's try that again. Please enter 'heads' or 'tails'.\n")
        heads_or_tails()

def try_again(game):
    y_or_n = print("Would you like to try again? Enter 'y' or 'n'")
    if y_or_n == "y":
        game()
    elif y_or_n == "n":
        print("Thank you for playing!")
        new_game = input("Would you like to play another game? Enter 'y' or 'n'.")
        if new_game == "y":
            pick_game()
        elif new_game == "n":
            return (print "See you next time!")
        else:
            print("Whoops. Please enter 'y' or 'n'.")
            try_again(game)
