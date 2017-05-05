
from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

TOP_MENU = "q)uit c)hoose taxi d)rive\n>>> "


def print_available_taxis(taxis):
    for this_taxi in range(0, len(taxis)):
        print("{} - ".format(this_taxi), taxis[this_taxi])


def print_bill(bill_value):
    print("Bill to date ${:.2f}".format(bill_value))


my_taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
            SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")

total_bill = 0.00
menu_selection = ''
user_taxi = ''
while menu_selection != 'q':

    if menu_selection == 'c':
        print_available_taxis(my_taxis)
        taxi_selection = int(input("Choose taxi: "))
        user_taxi = my_taxis[taxi_selection]
        print_bill(total_bill)

    elif menu_selection == 'd':
        if user_taxi == '':
            print("Please select a taxi first")
            menu_selection = ''
            continue

        drive_distance = int(input("Drive how far? "))
        user_taxi.drive(drive_distance)
        print("Your {} trip cost you ${:.2f}".format(user_taxi.name, user_taxi.get_fare()))
        total_bill += user_taxi.get_fare()
        print(total_bill)

    print(TOP_MENU)
    menu_selection = input("").lower()

print("Total trip cost: ${:.2f}".format(total_bill))
print("Taxis are now:")
print_available_taxis(my_taxis)
