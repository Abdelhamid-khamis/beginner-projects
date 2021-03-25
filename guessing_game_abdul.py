import random

# User guess the computer's random choice between 1 & upper bound num.
def user_guess(x):
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
            


# Computer guess the User's random choice between 1 & upper bound num.
def computer_guess():
    comp_guess = random.randint(1,10)
    
    feedback = ""
    while feedback != "c":
        print("""
Enter 
`c` for correct guess,
`l` for low guess,
`h` for high guess:
""")
        feedback = input(f"is {comp_guess} your number? ").lower()
        if feedback == "l":
            comp_guess += 1
        elif feedback == "h":
            comp_guess -= 1
    print(f"you guessed the number {comp_guess} correctly!!")


user_guess(10)
# computer_guess()    
        