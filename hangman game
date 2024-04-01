
from replit import clear
import random
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)
guess_word = []
lives = 6
for letter in chosen_word:
  guess_word.append("_")

def game_over():
  if guess_word == word_list:
    print("You Win!")
    return True
  elif lives == 0:
    print("You Lose!")
    return True
while not game_over():
  guess = input("Guess a letter: ").lower()
  clear()
  for x in range(len(chosen_word)):
    if chosen_word[x] == guess:
      guess_word[x] = chosen_word[x]
  if guess not in chosen_word:
    lives -= 1
  print(stages[lives])
  print(f"{' '.join(guess_word)}")

