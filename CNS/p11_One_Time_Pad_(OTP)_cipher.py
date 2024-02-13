# P11-Implement the One Time Pad (OTP) cipher

import os

def generate_random_key(length):
    # Generate a random key of the specified length
    return os.urandom(length)

def otp_encrypt(plaintext, key):
    # Ensure that the key is the same length as the plaintext
    if len(key) != len(plaintext):
        raise ValueError("Key length must be the same as plaintext length")

    ciphertext = ""
    for i in range(len(plaintext)):
        # Perform XOR operation between the ASCII values of the plaintext and key characters
        encrypted_char = chr(ord(plaintext[i]) ^ key[i])
        ciphertext += encrypted_char
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")

# Generate a random key of the same length as the plaintext
key = generate_random_key(len(plaintext))

# Encrypt the plaintext using the OTP cipher
ciphertext = otp_encrypt(plaintext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
