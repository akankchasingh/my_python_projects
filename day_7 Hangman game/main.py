import hangman_art
import hangman_words
import random


print(hangman_art.logo)
print("Welcome to the Hangman  Game !")

hang_count = 0
words = hangman_words.word_list
hang_art = hangman_art.stages
chosen_word = random.choice(words)
#store the correct characters guessed
correct_guess = []

len_word = len(chosen_word)

for l in range(0, len_word):
    correct_guess.append("_")

#convert the random word to a list
chosen_word_list = []
chosen_word_list[:0] = chosen_word
print(chosen_word)
output = ""

is_won = False
#main process
while(hang_count < 6 and is_won == False):
    user_input = input("Enter a letter that might be in the word: ").lower()
    count = 0
    output=""

    for char in range(0,len_word):
        if (user_input == chosen_word_list[char]):
            correct_guess[char] = chosen_word_list[char]
            count += 1

    print(f"The word is: {output.join(correct_guess)}")
    if (count == 0):
        hang_count += 1
        print(f"{hang_art[6-hang_count]}")

    if ("_" not in correct_guess):
        is_won = True

if is_won == True:
    print("Hurrah, we won the game")
else:
    print("Sorry, you exhausted the chances!\nPlease try again! ")
