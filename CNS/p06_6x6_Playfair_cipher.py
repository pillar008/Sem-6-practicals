# P6-Implement 6 x 6 Playfair cipher

import numpy as np

def preprocess(text):
    # Convert the text to uppercase and remove spaces
    text = text.upper().replace(" ", "")
    # Replace 'J' with 'I' in the text
    text = text.replace("J", "I")
    return text

def generate_key_square(key):
    # Convert the key to uppercase and remove duplicate letters
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))
    # Remove 'J' and add 'I' if it's not present
    key = key.replace("J", "")
    if 'I' not in key:
        key += 'I'
    # Create the key square matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = np.array(list(key + alphabet))
    key_square = np.unique(key_square.reshape(6, 6), axis=1)
    return key_square

def find_letter_positions(key_square, letter):
    row, col = np.where(key_square == letter)
    return row[0], col[0]

def encrypt_playfair(plaintext, key):
    plaintext = preprocess(plaintext)
    key_square = generate_key_square(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_letter_positions(key_square, char1)
        row2, col2 = find_letter_positions(key_square, char2)
        if row1 == row2:  # Same row
            ciphertext += key_square[row1, (col1 + 1) % 6]
            ciphertext += key_square[row2, (col2 + 1) % 6]
        elif col1 == col2:  # Same column
            ciphertext += key_square[(row1 + 1) % 6, col1]
            ciphertext += key_square[(row2 + 1) % 6, col2]
        else:  # Forming rectangle
            ciphertext += key_square[row1, col2]
            ciphertext += key_square[row2, col1]
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Example usage:
ciphertext = encrypt_playfair(plaintext, key)
print("Ciphertext:", ciphertext)
