"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac07.car import Car


def main():
    """Demo test code to show how to use car class."""
    bus = Car(180)
    bus.drive(30)
    bus.name = "Bus 1"
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))

    limo = Car(100)
    limo.add_fuel(20)
    limo.name = "Limo 1"
    print("Limo fuel: {}".format(limo.fuel))
    limo.drive(115)
    print("Limo odo: {}".format(limo.odometer))



main()