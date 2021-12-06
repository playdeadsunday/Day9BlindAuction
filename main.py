import blind_auction_art
import os
clear = lambda: os.system('cls')

print(blind_auction_art.logo)
print("Welcome to the secret auction program.")

auctioneers = {}
condition = "yes"
while condition == "yes":
    key = input("Please enter your name.\n")
    value = int(input("Please enter your bdding amount.\n$"))
    auctioneers[key] = value

    condition = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()

name = ""
highest = 0
for key in auctioneers:
    if auctioneers[key] > highest:
        name = key
        highest = auctioneers[key]
    else:
        pass
print(f"The winner is {name} with a bid of ${highest}")
