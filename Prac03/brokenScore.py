"""

CP1404/CP5632 - Practical

Broken program to determine score status

"""


score = float(input("Enter score: "))

# Check if input is valid
if score < 0 or score > 100:

    print("Invalid score")

# If input is valid then test score
else:
    if score > 90:

        print("Excellent")

    elif score > 50:

        print("Passable")

    else:

        print("Bad")