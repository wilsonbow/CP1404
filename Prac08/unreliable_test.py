from Prac08.taxi import UnreliableCar


def main():
    testcar = UnreliableCar("Lemon", 100, 50)
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

main()
