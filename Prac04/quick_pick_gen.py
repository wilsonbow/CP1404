import random


finished = False
while not finished:
    try:
        num_games = int(input("How many quick picks: "))
        finished = True
    except:
        print("Please enter a valid int")

for games in range(num_games):

    # Produce set of numbers (unsorted)
    game = []
    for numbers in range(6):
        game.append(random.randint(1,45))

    # Sort numbers
    game.sort()

    for number in range(len(game)):
        print("{:3}".format(game[number]), end=' ')

    print()