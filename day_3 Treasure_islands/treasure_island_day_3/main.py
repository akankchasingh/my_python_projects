print('''                                     _     _                 _ 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
inp_1 = input("left or right? : ").lower()

if(inp_1 == "left"):
    inp_2 = input("swim or wait? : ").lower()
    if(inp_2 == "wait"):
        inp_3 = input("Which door: red or blue?: ").lower()
        if(inp_3 == "red"):
            print("Congratulations!! You won the game !")
        else:
            print("Sorry, you lost the game, Game Over!")
    else:
        print("Sorry, you lost the game, Game Over!")
else:
    print("Sorry, you lost the game, Game Over!")
print("Thank you for playing the game!")


