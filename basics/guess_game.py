#Write a function game() number-guessing game,
# that takes 2 int parameters defining the range.
# Using some kind of random function to generate random int from the range.
# While user input isn't equal that number, print "Try again!". If user guess the number, congratulate him and exit.
import random
def game():
    while True:
        guess_range = input("Input range [int,int]: ")
        if isinstance(guess_range,tuple):
            comp_var = random.choice(guess_range)
            while True:
                human_guess = input("Input your guess number: ")
                if human_guess == comp_var:
                    print ("Congrats! You win.")
                    break
                else:
                    print ("Wrong. Try again!")
        else:
            print("Incorrect range")

game()

