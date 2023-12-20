import random
print("Welcome to the International Rock, Paper, and Scissors Game")
choices = ["rock", "paper", "scissors"]
user_input = int(input("Enter 0 for rock, 1 for Paper, 2 for Scissors:  "))
print(f"Your choice is {choices[user_input]}")

comp_choice = random.randint(0,3)
print(f"Computer's choice is {choices[comp_choice]}")
if (user_input == comp_choice):
    print("It's a tie! ")
elif(user_input==0 and comp_choice==2):
    print("You won, Hurrah")
elif(user_input==2 and comp_choice==0):
    print("You lose the match")
elif(user_input > comp_choice):
    print("Hurrah! You won the match!")
else:
    print("Sorry, You lost the game!")

