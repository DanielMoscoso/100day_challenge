# import logo  # Use this when running as as program/scrypt.
from Day_8 import art  # Use this when running in an IDE.


def caesar_cipher(direction="", text="", shift=0):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = ""

    if direction == "encode":
        for char in text:
            if char in alphabet:
                # ---------------------- This is for encrypting: ----------------------
                original_index = alphabet.index(char)
                # original_index = alphabet.index("v")  # This is for debugging purposes.
                # original_index  # This is for debugging purposes.

                if (original_index + shift) > 25:
                    output += alphabet[(original_index + shift) - 26]
                else:
                    output += alphabet[original_index + shift]
                # ---------------------- This is for encrypting: ----------------------
            else:
                output += char
    elif direction == "decode":
        for char in text:
            if char in alphabet:
                # ---------------------- This is for decrypting: ----------------------
                original_index = alphabet.index(char)
                # original_index = alphabet.index("v")  # This is for debugging purposes.
                # original_index  # This is for debugging purposes.

                if (original_index - shift) < 0:
                    output += alphabet[(original_index - shift) + 26]
                else:
                    output += alphabet[original_index - shift]

                # ---------------------- This is for decrypting: ----------------------
            else:
                output += char
    else:
        print('I need to "Encrypt" or "Decrypt", try again.\n')

    return output


print(art.logo, "\n")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26  # This will make sure that the actual shift stays in the 26  letter-index-range boundary. No matter how high the number is.
# print(encrypt("hello", 5))  # This is for debugging purposes.
# print(encrypt("civilization", 5))  # This is for debugging purposes.
print(f"The final {direction}d text is: {caesar_cipher(direction, text, shift)}")


# %%
# Alternative:
# import logo  # Use this when running as as program/scrypt.
from Day_8 import art  # Use this when running in an IDE.


def caesar_cipher(direction="", text="", shift=0):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#               The "index()" method will return the first time a letter appears
#               in the list. So it does not matter how many times it is repeated.
    output = ""

    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)

            if direction == "encode":
                # -------------------- This is for encrypting: --------------------
                # original_index = alphabet.index("v")  # This is for debugging purposes.
                # original_index  # This is for debugging purposes.

                output += alphabet[original_index + shift]
                # -------------------- This is for encrypting: --------------------
            elif direction == "decode":
                # -------------------- This is for decrypting: --------------------
                # original_index = alphabet.index("v")  # This is for debugging purposes.
                # original_index  # This is for debugging purposes.

                output += alphabet[original_index + (shift * -1)]
            else:
                pass
                # -------------------- This is for decrypting: --------------------
        else:
            output += char

    return output


print(art.logo, "\n")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26  # This will make sure that the actual shift stays in the 26  letter-index-range boundary. No matter how high the number is.
# print(encrypt("hello", 5))  # This is for debugging purposes.
# print(encrypt("civilization", 5))  # This is for debugging purposes.

if direction == "encode" or direction == "decode":
    print(f"The final {direction}d text is: {caesar_cipher(direction, text, shift)}")
else:
    print('I need to "Encrypt" or "Decrypt", try again.\n')
