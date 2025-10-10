import art

# TODO-1: Ask the user for input
print(art.logo)

new_bidder = True
all_bids = {}

while new_bidder:
    bidder = input("What is your name? ")
    bid = input("What is your bid? ")

    all_bids[bidder] = bid

    end_bids = input("Are there any bidders left? yes or no: ").lower()

    if end_bids == "no":
        new_bidder = False
    else:
        print("\n" * 100)

winning_bid = max(all_bids.values())
winning_name = ""
for key, value in all_bids.items():
    if value == winning_bid:
        winning_name = key

print(art.logo)
print(f"The winner is {winning_name} with a bid of ${winning_bid}.")
