# Bidding system creation
import os

print("************ Bidding System ************")
bidders = {}
total_bidders = []
continue_loop = True
highest_bid = 0
winner = ""
bidder_amount = {}
# clear = lambda: os.system('cls')
print(type(bidder_amount))
while continue_loop:
    User_name = input("Enter the name : ")
    User_price = int(input("Enter the bid price : "))
    bidders = {"name": User_name, "price": User_price}
    # total_bidders.append(bidders)
    users = input("Is there any other bidders ? :").lower()
    if users == "no":
        continue_loop = False
    else:
        os.system('cls')
# print(total_bidders)
for bidder in bidders:
    bid_amount = {bidders[bidder]}
    print(bid_amount)
    # if bid_amount > highest_bid:
    #     highest_bid = bid_amount
    #     winner = bidder

print(f"Highest bid amount is {highest_bid} and the winner is {winner}")
