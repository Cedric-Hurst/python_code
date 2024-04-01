from replit import clear
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_game = True
def caesar(text, shift, direction):
  end_text = []
  if direction == "decode":
    shift *= -1
  for letter in text:  
    if letter.isalpha():
      char_index = alphabet.index(letter)
      new_cipher_index = char_index + shift
      if(new_cipher_index > 25):
        end_text += alphabet[new_cipher_index-26]
      else:
        end_text += alphabet[new_cipher_index]
    else:
      end_text += letter
  print(f"The {direction}d Text is: {''.join(end_text)}")
while run_game:
  clear()
  input_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  input_text = input("Type your message:\n").lower()
  input_shift = int(input("Type the shift number:\n"))
  if input_shift > 26:
    input_shift = input_shift % 26
  if input_direction == "encode" or input_direction == "decode":
    caesar(text=input_text, shift=input_shift, direction=input_direction)
  else:
    print(f"invalid input {input_direction}")
  replay = input("To run again type 'yes'.\n")
  if replay.lower() != "yes":
    run_game = False
