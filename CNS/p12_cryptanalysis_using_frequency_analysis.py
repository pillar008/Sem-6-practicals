# P12-Implement the cryptanalysis using frequency analysis

from collections import Counter

def frequency_analysis(ciphertext):
    # Count the occurrences of each character in the ciphertext
    frequencies = Counter(ciphertext)
    # Sort the frequencies in descending order
    sorted_frequencies = frequencies.most_common()
    return sorted_frequencies

# Get input from the user
ciphertext = input("Enter the ciphertext: ")

# Perform frequency analysis
analysis_result = frequency_analysis(ciphertext)
print("Frequency analysis result:")
for char, frequency in analysis_result:
    print(f"Character: {char}, Frequency: {frequency}")
