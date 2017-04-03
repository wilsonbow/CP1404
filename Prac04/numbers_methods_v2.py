numbers = []


def get_valid_int(prompt):
    finished = False
    while not finished:
        try:
            number = int(input(prompt))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")

    return number


count = 1
number = get_valid_int("Number {}:".format(count))  # random positive number
while number >= 0:
    numbers.append(number)
    count += 1
    number = get_valid_int("Number {}:".format(count))

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))
