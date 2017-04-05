"""
This program will estimate the electricity bill based on
tariff, daily usage, and number of days in billing period

Version 2 adds functionality to prompt for a tariff
    rather than a charge rate
"""

# Create tariff dictionary
TARIFFS = {'11': 0.244618, '31': 0.136928, '69': 0.1, '22': 0.567, '25': 0.456}


def tariff_select(TARIFFS):
    """Creates prompt which lists all available tariffs"""
    print("Please select a tariff:")
    for tariff in TARIFFS:
        print("{}".format(tariff), end=', ')
    tariff_str = input("\n>>> ")

    return tariff_str


# Get valid tariff input
tariff_str = tariff_select(TARIFFS)
while not (tariff_str in TARIFFS):
    print("Please enter a valid tariff.")
    tariff_str = tariff_select(TARIFFS)

daily_use_float = float(input("Enter daily use in kWh: "))
days_billing_period_int = int(input("Enter number of billing days: "))

# Calculate the bill
total_bill_float = TARIFFS[tariff_str] * daily_use_float * days_billing_period_int

# Output the result to user
print("Estimated bill: $", format(total_bill_float, '.2f'), sep='')
