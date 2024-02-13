# P3-Implement simple transposition technique

def encrypt_transposition(plaintext, key):
    # Remove spaces from the plaintext
    plaintext = plaintext.replace(" " , "")
    
    # Calculate the number of columns based on the key
    num_columns = len(key)
    
    # Calculate the number of rows required
    num_rows = -(-len(plaintext) // num_columns)  # Ceiling division
    
    # Pad the plaintext to make it fit evenly into the grid
    plaintext += '*' * (num_rows * num_columns - len(plaintext))
    
    # Create the grid
    grid = [[''] * num_columns for _ in range(num_rows)]
    
    # Fill the grid with the plaintext characters
    for i, char in enumerate(plaintext):
        row = i // num_columns
        col = i % num_columns
        grid[row][col] = char
    
    # Generate the ciphertext by reading the grid column-wise based on the key
    ciphertext = ''
    for col_index in key:
        col_index = int(col_index) - 1  # Adjust for 1-based indexing
        for row_index in range(num_rows):
            ciphertext += grid[row_index][col_index]
    
    return ciphertext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (a permutation of numbers): ")

# Example usage:
ciphertext = encrypt_transposition(plaintext, key)
print("Ciphertext:", ciphertext)
