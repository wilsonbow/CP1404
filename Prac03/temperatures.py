"""
Celcius to Fahrenheit conversion

"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    # input fahrenheit, return celsius conversion
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def get_celsius():
    finished = False # finish flag for valid input
    while not finished:
        try:
            celsius = float(input("Celsius: "))
            finished = True
        except ValueError:
            print("Please enter a valid number.")
    return celsius


def get_fahrenheit():
    finished = False
    while not finished:
        try:
            fahrenheit = float(input("Fahrenheit: "))
            finished = True
        except ValueError:
            print("Please enter a valid number.")
    return fahrenheit


def main():
    # Display menu and get input
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()

    # Infinite while loop. Terminates when "Q" entered
    while choice != "Q":
        if choice == "C":

            celsius = get_celsius()
            fahrenheit = celsius_to_fahrenheit(celsius)

            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":

            fahrenheit = get_fahrenheit()
            celsius = fahrenheit_to_celsius(fahrenheit)

            print("Result: {:.2f} C".format(celsius))

        else:

            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    # Print when loop terminates (Quit)
    print("Thank you.")

main()