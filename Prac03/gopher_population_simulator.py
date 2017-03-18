"""
This program will simulate the population of gophers over a ten year period.
"""
import random

BIRTH_RATE_MIN = 10 # 10%
BIRTH_RATE_MAX = 20 # 20%
DEATH_RATE_MIN = 5  # 5%
DEATH_RATE_MAX = 25 # 25%
YEARS = 10

print("Welcome to the Gopher Population Simulator!")


# Calculate births and deaths
def gopher_births(population):
    """Calculates yearly gopher births."""
    birth_rate = random.randint(BIRTH_RATE_MIN, BIRTH_RATE_MAX) # Birth rate between min and max
    return int(population * birth_rate / 100) # Calculate and return births


def gopher_deaths(population):
    """Calculate yearly gopher deaths"""
    death_rate = random.randint(DEATH_RATE_MIN, DEATH_RATE_MAX) # Death rate between min and max
    return int(population * death_rate / 100) # Calculate and return deaths


population = 1000
print("Initial population is 1000")

# Simulate for YEARS years
for year in range(1, YEARS + 1):
    births = gopher_births(population)
    deaths = gopher_deaths(population)

    population = int(population + births - deaths)

    print("In year {:>2}, there were {:>3} births and {:>3} deaths. \
    The new population is: {:>4}.\n".format(year, births, deaths, population))