import random

def guessing_game(x):
    rand_int_number = random.randint(1,x)

    guess = 0
    while guess != rand_int_number:
        guess = int(input(f"Guess a number between 1 & {x}: "))

        if guess < rand_int_number:
            print("Sorry, guess agin. Too Low!")
        elif guess > rand_int_number:
            print("Sorry, guess agin. Too High!")
        else:
            print(f"Yay, Congrats. you have guessed the number\
 {rand_int_number} correctly!!")
            
guessing_game(10)