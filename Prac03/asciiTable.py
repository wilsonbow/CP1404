"""
This program is designed to teach students about ASCII.
"""

LOWER = 33      # minimum allowable ASCII code
UPPER = 127     # maximum allowable ASCII code

def main():
    # Prompt for character
    user_char_str = input("Enter a character: ")

    # Tell user ASCII code for entered character
    user_char_code_int = ord(user_char_str)
    print("The ASCII code for {} is {}".format(user_char_str, user_char_code_int))

    user_code_int = get_number(LOWER, UPPER)
    # Tell user character for ASCII code entered
    user_code_char = chr(user_code_int)
    print("The ASCII code for {} is {}".format(user_code_int, user_code_char))

    # Print out ASCII table
    for i in range(33,127):
        print("{:>3}: {}".format(i, chr(i)))

def get_number(lower, upper):
    # Prompt user for number between 33 and 127
    user_code_int = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    # Check input is between upper and lower bounds
    while user_code_int < lower or user_code_int > upper:
        user_code_int = int(input("Invalid input!\n" + \
            "Enter a number between {} and {}: ".format(LOWER, UPPER)))

    return user_code_int

main()