# Day_8 project
# This is the code for implementing Caesar's Cipher
from art import logo
from alphabet import alphabet

print(logo)
print("Welcome to Caesar's Cipher")

def caesar (original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d message: {cipher_text}")


terminate = False
while not terminate:
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(original_text = text,shift_amount = shift, encode_or_decode = mode)
    restart = input("Type 'yes' to go again, otherwise type 'no'\n").lower()
    if restart == 'no':
        terminate = True
        print("Goodbye!")