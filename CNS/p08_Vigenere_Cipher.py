# P8-Implement Vigenere Cipher

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Convert the character to uppercase
            char = char.upper()
            # Determine the shift value for the current character in the key
            shift = ord(key[key_index].upper()) - ord('A')
            # Encrypt the current character using the Vigenère cipher
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            # Move to the next character in the key
            key_index = (key_index + 1) % len(key)
        else:
            # If the character is not alphabetic, leave it unchanged
            ciphertext += char
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encrypt the plaintext using the Vigenère cipher
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
