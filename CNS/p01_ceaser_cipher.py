# P1-Implement the Caesar cipher with variable key

def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Get the character code of the letter (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar cipher shift
            shifted = (ord(char) - base + key) % 26 + base
            # Convert the shifted character code back to a character
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged
    return encrypted_text

# Get input from the user
plaintext = input("Enter the text to encrypt: ")
key = int(input("Enter the key (an integer): "))

# Encrypt the input text using the Caesar cipher
encrypted_text = caesar_cipher(plaintext, key)
print("Encrypted text(Classical ceaser cipher):", encrypted_text)
print("\nNote : Classical ceaser cipher has key = 3 \nand same encryptions with differnet key value comes under \nshift cipher(ceaser cipher is a type of shift cipher only)")
