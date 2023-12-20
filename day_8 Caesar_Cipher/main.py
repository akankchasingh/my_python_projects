import art
print(art.logo)

print("Welcome to Caesar Cipher code!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

alphabet2 = alphabet + alphabet
#print(alphabet2)

response = "yes"

while (response == "yes"):
    cipher_list = []
    cipher_text = ""
    decrypt_list = []
    decrypt_text = ""

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    text_list = []
    text_list[:0] = text

    if direction == "encode":
        for char in text_list:
            char_index = alphabet.index(char)
            cipher_list.append(alphabet2[(char_index + shift)])

        print(f"The cipher text is {(cipher_text.join(cipher_list))}")

    elif direction == "decode":
        for char in text_list:
            char_index = alphabet.index(char)
            decrypt_list.append(alphabet2[(char_index - shift)])

        print(f"The decrypted text is {(decrypt_text.join(decrypt_list))}")

    else:
        print("Wrong input")
        response = "no"

    response = input("Do you want to continue? Yes or No ? : ").lower()
