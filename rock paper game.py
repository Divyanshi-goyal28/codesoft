#Rock Paper and scissors
import random

#making  a list to select random move
moves = ["rock", "paper", "scissors"]

print("=========== ROCK PAPER SCISSORS ========== ")
print()
while True:
    
    #for taking random choice by the computer
    computer_choice = random.choice(moves)
    
    print("Press 1 for Rock ✊" )
    print("Press 2 for Paper 🖐" )
    print("Press 3 for Scissors ✌" )
    user_input=input("Enter your move ✊,🖐,✌ (1/2/3):")
    
    #conditions for wining and tie
    if (user_input=="1" and computer_choice =="scissors") or (user_input=="2" and computer_choice=="rock") or (user_input=="3" and computer_choice=="paper"):
        print("Congratulations!🎉 You Win The Game")
    elif(user_input=="2" and computer_choice =="scissors") or (user_input=="3" and computer_choice=="rock") or (user_input=="1" and computer_choice=="paper"):
        print("The computer wins the game")
    elif(user_input=="3" and computer_choice=="scissors") or (user_input=="1" and computer_choice=="rock") or (user_input=="2" and computer_choice=="paper"):
        print("There is a Tie")
    else:
        print("This is an Invalid Choice")
    print("The game over")

    #to continue the game
    ask=input("Do you want to play again? {yes/no or y/n or Yes/No} ")
    if ask not in ["yes","y","Yes"]:
        break