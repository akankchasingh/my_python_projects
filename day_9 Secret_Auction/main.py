import art

print("Welcome to the Secret Auction Club")
print(art.logo)
#initialisation
highest_bid = 0
bid_dictionary = {}
response = "yes"

while response == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: "))
    bid_dictionary[name] = bid
    print(bid_dictionary)
    if highest_bid < bid:
        highest_bid = bid
    response = input("Is there any other bidder? Yes or No ? : ").lower()

key_list = list(bid_dictionary.keys())
val_list = list(bid_dictionary.values())

position = val_list.index(highest_bid)

print(f"The highest bid of the auction is {val_list[position]} by {key_list[position]}")


