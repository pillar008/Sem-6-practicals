#WAP to check whether entered character is vowel or consonant. 

# Get input character from user
char = input("Enter a character: ")


if len(char) == 1:
    
    char = char.lower()
    
    if char.isalpha():
        if char in 'aeiou':
            print(f"The character {char} is a vowel.")
        else:
            print(f"The character {char} is a consonant.")
    else:
        print("Please enter an alphabet character.")
else:
    print("Please enter only a single character.")
