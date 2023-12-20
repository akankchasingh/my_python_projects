############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_card_sum = 0
computer_cards_sum = 0
should_continue = True
#to store the num of items
counter = 0

for deal in range(0,2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    user_card_sum += user_cards[deal]
    computer_cards_sum += computer_cards[deal]
    counter += 1

print(f"Your deck is {user_cards} and sum is {user_card_sum}")
print(f"Dealer's sum is {computer_cards_sum}")

while should_continue == True:
    if user_card_sum > 21:
        if 11 in user_cards:
            user_card_sum -= 10
        else:
            should_continue = False
            print(f"You lose the match, sum is greater than 21, Dealer's sum is {computer_cards_sum}")
    elif user_card_sum == 21:
        should_continue = False
        print(f"You win the match, Blackjack, Dealer's sum is {computer_cards_sum}")
    elif computer_cards_sum == 21:
        should_continue = False
        print(f"You lose the match, Blackjack, Dealer's sum is {computer_cards_sum}")
    elif computer_cards_sum > 21:
        if 11 in computer_cards:
            computer_cards_sum -= 10
        else:
            should_continue = False
            print(f"You win the match, Dealer sum is greater than 21, Dealer's sum is {computer_cards_sum}")
    elif user_card_sum < 21:
        user_input = input("Do you want to draw another card? Y or N? : ").lower()
        if user_input == "y":
            user_cards.append(random.choice(cards))
            user_card_sum += user_cards[counter]
            computer_cards.append(random.choice(cards))
            computer_cards_sum += computer_cards[counter]
            counter += 1
            print(f"Your deck is {user_cards} and sum is {user_card_sum}")
        else:
            if computer_cards_sum < 17:
                computer_cards.append(random.choice(cards))
                computer_cards_sum += computer_cards[counter]
                counter += 1
                print(f"The dealer's deck is {computer_cards} and the sum is {computer_cards_sum}")
            else:
                if user_card_sum > computer_cards_sum:
                    should_continue = False
                    print(f"You win the match, your score is {user_card_sum} and the dealer's score is {computer_cards_sum}")
                elif user_card_sum < computer_cards_sum:
                    should_continue = False
                    print(f"You lose the match, your score is {user_card_sum} and the dealer's score is {computer_cards_sum}")

                else:
                    should_continue = False
                    print(f"The match is draw, your score is {user_card_sum} and the dealer's score is {computer_cards_sum}")



