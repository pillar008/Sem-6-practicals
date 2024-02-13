# P5-Implement the rail fence cipher with variable fence

def encrypt_rail_fence(plaintext, rails):
    fence = [''] * rails
    direction = -1  # Direction of the rail: -1 for downwards, 1 for upwards
    row = 0

    for char in plaintext:
        fence[row] += char
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction when reaching the top or bottom rail
        row += direction
    
    # Combine all rail strings into a single ciphertext
    ciphertext = ''.join(fence)
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
rails = int(input("Enter the number of rails: "))

# Example usage:
ciphertext = encrypt_rail_fence(plaintext, rails)
print("Ciphertext:", ciphertext)
