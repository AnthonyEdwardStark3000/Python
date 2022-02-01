print("**************** Caeser Cipher ****************")
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]

direction = input("Enter encode to encrypt and decode to decrypt:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Enter the number of shifts :"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        letter_position = alphabets.index(letter)
        new_position = letter_position + shift_amount
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(cipher_text)


def decrypt(plain_text, shift_amount):
    decrypted_text = ""
    for letter in plain_text:
        letter_position = alphabets.index(letter)
        new_position = letter_position - shift_amount
        new_letter = alphabets[new_position]
        decrypted_text += new_letter
    print(decrypted_text)


if direction == "encrypt" or direction == "encode":
    encrypt(text, shift)
elif direction == "decrypt" or direction == "decode":
    shifts = int(input("Enter the number of decrypt :"))
    message = input("Enter the message to decrypt: ")
    decrypt(plain_text=message, shift_amount=shifts)

# option = input("Enter yes to restart the program or no to quit:").lower()
# if option == "yes":
#     repeat_direction = input("Do you want to encrypt or decrypt ? :")
#     decrypt(plain_text=message, shift_amount=shifts)
