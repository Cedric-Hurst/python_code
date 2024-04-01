import random

from replit import clear
from art import logo, vs
from game_data import data

game_running = True
high_score = 0
score = 0
first_fact = random.choice(data)


def print_fact(fact):
  print(fact["name"])
  print(fact["description"])
  print(fact["country"])


def show_count(fact):
  print_fact(fact)
  print(fact["follower_count"])


def compare(guess, fact1, fact2):
  count1 = fact1["follower_count"]
  count2 = fact2["follower_count"]
  return (count2 >= count1 and guess == "higher") or (count2 <= count1
                                                     and guess == "lower")


def print_game():
  print(f"High Score: {high_score}")
  print(f"Current Score: {score}")
  print(logo)
  show_count(first_fact)
  print(vs)


while game_running:
  second_fact = random.choice(data)
  print_game()
  print_fact(second_fact)
  # ask user to input if random fact is higher or lower follower count then other random fact
  guess = input(
      f'Is {second_fact["name"]} higher or lower than {first_fact["name"]}? \n'
  ).lower()
  # if correct then move on using last fact with a new fact to compare for next part of game
  if compare(guess, first_fact, second_fact):
    clear()
    score += 1
    first_fact = second_fact
  #end game, show score, and ask to play again
  else:
    game_running = False
    clear()
    print_game()
    show_count(second_fact)
    print("\nGame Over!")
    print(f"Your score was: {score}")
    play_again = input("To play again type 'y' or 'n' to stop \n").lower()
    if play_again == 'y':
      if score > high_score:
        high_score = score
      clear()
      game_running = True
      score = 0
      first_fact = second_fact
