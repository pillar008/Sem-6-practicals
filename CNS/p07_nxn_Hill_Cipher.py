# P7-Implement n x n Hill Cipher

import numpy as np

# Function to preprocess the plaintext
def preprocess(text, n):
    # Convert the text to uppercase and remove spaces
    text = text.upper().replace(" ", "")
    # Pad the text with 'X' to make its length a multiple of n
    if len(text) % n != 0:
        text += 'X' * (n - len(text) % n)
    return text

# Function to generate the key matrix
def generate_key_matrix(key, n):
    key = key.upper().replace(" ", "")
    # Convert the key to uppercase and convert characters to numbers
    key_matrix = np.array([ord(char) - 65 for char in key])
    key_matrix = key_matrix.reshape(n, n)
    return key_matrix

# Function to encrypt plaintext using Hill cipher
def encrypt_hill(plaintext, key):
    n = int(len(key) ** 0.5)
    plaintext = preprocess(plaintext, n)
    key_matrix = generate_key_matrix(key, n)

    # Convert plaintext characters to numbers
    plaintext_numbers = np.array([ord(char) - 65 for char in plaintext])
    plaintext_numbers = plaintext_numbers.reshape(len(plaintext) // n, n)

    # Perform matrix multiplication and modulo 26 to get the ciphertext
    ciphertext = ""
    for block in plaintext_numbers:
        block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join([chr(num + 65) for num in block])
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (as a string of characters): ")

# Example usage:
ciphertext = encrypt_hill(plaintext, key)
print("Ciphertext:", ciphertext)
