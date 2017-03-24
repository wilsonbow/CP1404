import random


finished = False
while not finished:
    try:
        num_games = int(input("How many quick picks: "))
        finished = True
    except:
        print("Please enter a valid int")

# Print specified number of games
for games in range(num_games):

    # Produce set of numbers (unsorted)
    game = []
    for numbers in range(6):
        drawn_number = random.randint(1,45)

        # Ensure number has not already been picked
        while drawn_number in game:
            drawn_number = random.randint(1,45)

        game.append(drawn_number)

    game.sort()

    for number in range(len(game)):
        print("{:3}".format(game[number]), end=' ')

    print()