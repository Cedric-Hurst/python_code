
from art import logo
from random import choice
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
  return choice(cards)


def add_score(hand):
  total = 0
  for num in hand:
    total += num
  return total


def bust(hand):
  ace = -1
  for num in hand:
    if num == 11:
      ace = hand.index(11)
  if add_score(hand) > 21:
    if ace != -1:
      hand[ace] = 1
      bust(hand)
    else:
      return True
  else:
    return False


def turn(hand):
  #ask player to draw card or end turn
  cont = input(
      "Type 'draw' to draw another card or Press ENTER to end your turn \n"
  ).lower()
  if cont == "draw":
    #add card to hand
    hand.append(draw_card())
    clear()
    print(logo)
    print(f"Player Hand: {hand}  ({add_score(hand)})")
    print(f"Dealer Hand: [{computer[0]}, *]")
    #return hand if bust else recursion turn(hand)
    if bust(hand):
      return hand
    elif add_score(hand) == 21:
      return hand
    else:
      turn(hand)
  else:
    return hand


def computer_turn(hand):
  sum = add_score(hand)
  if sum < 17:
    hand.append(draw_card())
    if bust(hand):
      return hand
    elif add_score(hand) == 21:
      return hand
    else:
      computer_turn(hand)
  else:
    return hand


def winner_check(player, dealer):
  player_total = add_score(player)
  dealer_total = add_score(dealer)
  if player_total > dealer_total:
    return "You Win"
  elif player_total == dealer_total:
    return "Draw"
  elif bust(dealer):
    return "Dealer Bust! You Win!"
  else:
    return "Dealer Wins"


game_running = True

while game_running:
  computer = [draw_card(), draw_card()]
  player = [draw_card(), draw_card()]

  print(logo)
  print(f"Player Hand: {player} ({add_score(player)})")
  print(f"Dealer Hand: [{computer[0]}, *]")

  turn(player)

  clear()
  print(logo)
  print(f"Player Hand: {player} ({add_score(player)})")

  if add_score(player) == 21:
    print("You got 21 you win!")
  elif bust(player):
    print("You bust! You lose!")
  else:
    computer_turn(computer)
    print(f"Dealer Hand: {computer} ({add_score(computer)})")
    print(winner_check(player, computer))
  replay = input(
      "Press ENTER to play again or type 'quit' to stop the game. \n").lower()
  if replay == "quit":
    game_running = False
  else:
    clear()
