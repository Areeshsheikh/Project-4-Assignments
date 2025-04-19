import random
def guess_the_number():
    """project 2: Guess the number game by computer."""
    number = random.randint(1, 100)
    guess_left = 7
    print("Welcome to the Guess number game!")
    print("I am thinking a number between 1 to 100")

    while guess_left > 0:
        print(f"\nyou have {guess_left} guesses left. ")
        try:
            guess = int(input("Take a guess of another number. "))
        except ValueError:
            print("Invalid input. please enter a number. ")
            continue

        #guess the secret number
        if  guess < number:
            print("to low number . Tell another!")
        elif guess > number:
            print("Too  high number. Tell another!")
        else:
            print(f"Congratulation! you got the correct number in {7 - guess_left + 1} tries. ")
            return
        

        guess_left -= 1
        
    print(f"\nyou ran out of guess . The number was {number}.")


guess_the_number()



