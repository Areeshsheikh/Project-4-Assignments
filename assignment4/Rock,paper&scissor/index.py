import random

#game choices
choices =["rock","paper","scissor"]

#player choices
player_choice = input("Enter rock , paper , or scissor: ").lower()


#computer choices
computer_choice = random.choice(choices)

#winner decision
if player_choice == computer_choice:
    print(f"Both choices {player_choice} . Its tie!")
elif player_choice == "rock" and computer_choice == "scissor":
    print(f"player wins! {player_choice} beats {computer_choice}.")  

elif player_choice == "paper" and computer_choice == "rock":
    print(f"player wins! {player_choice} beats {computer_choice}.")

elif player_choice == "scissor" and computer_choice == "paper":
    print(f"player wins! {player_choice} beats {computer_choice}.")

else:
    print(f"computer win! {computer_choice} beats {player_choice}.")    
