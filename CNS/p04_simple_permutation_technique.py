# P4-Implement simple permutation technique

def encrypt_permutation(plaintext, key):
    # Create a mapping of original positions to the positions after permutation
    permutation_map = {i: int(key[i]) - 1 for i in range(len(key))}
    
    # Apply the permutation to the plaintext
    ciphertext = ''.join(plaintext[i] for i in permutation_map)
    
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (a permutation of numbers): ")

# Check if the key is valid
def is_valid_key(key):
    # Check if the key contains only digits
    if not key.isdigit():
        return False
    
    # Check if each digit appears exactly once
    return len(set(key)) == len(key)

if not is_valid_key(key):
    print("Invalid key. The key should contain only unique digits.")
else:
    # Example usage:
    ciphertext = encrypt_permutation(plaintext, key)
    print("Ciphertext:", ciphertext)
