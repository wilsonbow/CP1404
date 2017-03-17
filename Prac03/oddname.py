"""
Ask user for their name and print every second letter.
"""


def get_name():
    global user_name
    # Prompt user for name
    user_name = input("Enter name: ")
    # Ensure name is not blank
    while user_name == "":
        print("Please do not leave blank.")
        user_name = input("Enter name: ")

def print_name(frequency):
    global print_string
    print_string = user_name[0:len(user_name):frequency]  # every fth letter from first to last letter
    return print_string

f = 3

get_name()
print_string = print_name(f)
print(print_string)
