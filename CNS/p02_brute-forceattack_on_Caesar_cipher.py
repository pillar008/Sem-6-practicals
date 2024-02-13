# P2-Implement the brute-force (exhaustive key search)attack on Caesar cipher

def caesar_cipher_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Get the character code of the letter (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar cipher shift
            shifted = (ord(char) - base - key) % 26 + base
            # Convert the shifted character code back to a character
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Keep non-alphabetic characters unchanged
    return decrypted_text

# Get the ciphertext from the user
ciphertext = input("Enter the ciphertext to decrypt: ")

# Brute-force attack: Try all possible keys (0 to 25)
for key in range(26):
    decrypted_text = caesar_cipher_decrypt(ciphertext, key)
    print(f"Key {key}: {decrypted_text}")
