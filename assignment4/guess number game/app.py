import random
print("Guess the number between 1 to 100!")
#generate random number
number =  random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number:"))
    if guess < number:
        print("To low Number!")
    elif guess > number:
        print("To High Number!")
    else:
        print("Congratulation you Got it right!")
        break