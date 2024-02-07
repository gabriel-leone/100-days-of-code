alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if cipher_direction == "decode":
                new_index = (index - shift_amount) % len(alphabet)
            elif cipher_direction == "encode":
                new_index = (index + shift_amount) % len(alphabet)
            end_text += alphabet[new_index]
    print(f"The {cipher_direction}d text is: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
