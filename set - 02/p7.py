#WAP to check whether entered input is character, digit or special symbol using ladder if-else

input_char = input("Enter a character: ")

if input_char.isalpha():
    print(f"The entered input '{input_char}' is a character.")
elif input_char.isdigit():
    print(f"The entered input '{input_char}' is a digit.")
else:
    print(f"The entered input '{input_char}' is a special symbol.")
