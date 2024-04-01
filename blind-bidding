from replit import clear
from art import logo

active_bidding = True
bids = {}
print(logo)
print("Welcome to the secret auction program.\n")
while active_bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  clear()
  bids[name] = bid
  if others == "yes":
    continue
  elif others == "no":
    active_bidding = False;
  else:
    print("You typed an invaild respose. Bidding as ended")
    active_bidding = False;

highest_bid = 0
winner = ""
for key in bids.keys():
  if bids[key] > highest_bid:
    highest_bid = bids[key]
    winner = f"The Winner is {key} who bid ${bids[key]}"
  else:
    continue

print(winner)
