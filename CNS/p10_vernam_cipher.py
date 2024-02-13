# P10-Implement the vernam cipher

def vernam_encrypt(plaintext, key):
    # Ensure that the key is at least as long as the plaintext
    if len(key) < len(plaintext):
        raise ValueError("Key length must be at least as long as plaintext")

    ciphertext = ""
    for i in range(len(plaintext)):
        # Perform XOR operation between the ASCII values of the plaintext and key characters
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i]))
        ciphertext += encrypted_char
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (same length as plaintext): ")

# Check if the length of the key matches the length of the plaintext
if len(key) != len(plaintext):
    print("Error: Key length must be the same as the plaintext length")
else:
    # Encrypt the plaintext using the Vernam cipher
    ciphertext = vernam_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
