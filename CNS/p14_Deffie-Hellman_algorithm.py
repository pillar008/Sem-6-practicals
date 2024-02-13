# P14-Implement Deffie-Hellman algorithm for key exchange with small number

# Get prime number from the user
p = int(input("Enter the prime number (shared): "))
# Get primitive root from the user
g = int(input("Enter the primitive root (shared): "))

# Get Alice's private key from the user
private_key_alice = int(input("Enter Alice's private key: "))
# Get Bob's private key from the user
private_key_bob = int(input("Enter Bob's private key: "))

# Calculate Alice's public key
public_key_alice = (g ** private_key_alice) % p
# Calculate Bob's public key
public_key_bob = (g ** private_key_bob) % p

# Calculate the shared secret key using Bob's public key and Alice's private key
shared_secret_alice = (public_key_bob ** private_key_alice) % p
# Calculate the shared secret key using Alice's public key and Bob's private key
shared_secret_bob = (public_key_alice ** private_key_bob) % p

# Check if both shared secrets are equal (they should be)
assert shared_secret_alice == shared_secret_bob

print("Alice's public key:", public_key_alice)
print("Bob's public key:", public_key_bob)
print("Shared secret key:", shared_secret_alice)
