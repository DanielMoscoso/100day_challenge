def encrypt(direction="", text="", shift=0):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = ""
    for letter in text:
        # ---------------------- This is for encrypting: ----------------------
        original_index = alphabet.index(letter)
        # original_index = alphabet.index("v")  # This is for debugging purposes.
        # original_index  # This is for debugging purposes.

        if (original_index + shift) > 25:
            output += alphabet[(original_index + shift) - 26]
        else:
            output += alphabet[original_index + shift]
        # ---------------------- This is for encrypting: ----------------------

    return output


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# print(encrypt("hello", 5))  # This is for debugging purposes.
# print(encrypt("civilization", 5))  # This is for debugging purposes.
print(encrypt(direction, text, shift))
