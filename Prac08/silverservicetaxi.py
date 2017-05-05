from Prac08.taxi import SilverServiceTaxi


def main():
    testcar = SilverServiceTaxi("Hummer", 100, 2)
    print(testcar)
    testcar.drive(20)
    print(testcar)
    testcar.start_fare()
    print(testcar)
    testcar.drive(30)
    print(testcar)
    testcar.start_fare()
    print(testcar)
    testcar.drive(50)
    print(testcar)
    print("-" * 30)
    testcar.add_fuel(10)
    testcar.start_fare()
    print(testcar)
    testcar.drive(10)
    print("${:.2f}".format(testcar.get_fare()))

main()
