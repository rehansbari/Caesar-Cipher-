import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(caesar_text, shift_amount, direction):
  caesar_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift_amount
        caesar_text += alphabet[new_position]
      elif direction == "decode":
        new_position = position - shift_amount
        caesar_text += alphabet[new_position]
    else:
      caesar_text += letter

  if direction == "encode":
    print(f"The encoded text is {caesar_text}")
  elif direction == "decode":
    print(f"The decoded text is {caesar_text}")

print(art.logo)

answer = True 
valid_shift = True

answer = True 
valid_shift = True

while answer != False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    valid_shift = False
  while valid_shift == False:
    shift = int(input("Please enter a valid shift number: "))
    if shift < 26: 
      valid_shift = True

  caesar(caesar_text=text, shift_amount=shift, direction=direction)
  user_continue = input("Would you like to go again? Y or N").lower()
  if user_continue == "y":
    answer = True
  elif user_continue == 'n':
    answer = False
    print("Goodbye")
  