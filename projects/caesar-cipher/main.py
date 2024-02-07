alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(initial_text, shift_amount):
    cipher_text = ""
    for letter in initial_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift_amount) % len(alphabet)
            new_letter = alphabet[new_index]
            cipher_text += new_letter
    print(f"Encrypted text: {cipher_text}")


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift_amount) % len(alphabet)
            new_letter = alphabet[new_index]
            decrypted_text += new_letter
    print(f"Decrypted text: {decrypted_text}")


if direction == "encode":
    encrypt(initial_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_amount=shift)
