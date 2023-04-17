# TODO

from cs50 import get_float
import math


def main():

    dollar_owed = get_dollar()

    quarters = calculate_quarters(dollar_owed)
    dollar_owed = dollar_owed - (quarters * 0.25)

    # Optimising for remaining dollar after calc quarters

    dimes = calculate_dimes(dollar_owed)
    dollar_owed = dollar_owed - (dimes * 0.10)

    # Optimising for remaining dollar after calc dimes

    nickels = calculate_nickels(dollar_owed)
    dollar_owed = dollar_owed - (nickels * 0.05)

    # Optimising for remaining dollar after calc quarters

    pennies = calculate_pennies(dollar_owed)
    dollar_owed = dollar_owed - pennies

    # Calculating no of coins
    
    coins = quarters + dimes + nickels + pennies

    print(coins)

# Promt user for dollar


def get_dollar():

    while True:
        dollar = get_float("Change owed: ")
        if dollar > 0:
            return dollar

# Calculate no of quarters


def calculate_quarters(dollar_owed):

    quarters = math.floor(dollar_owed / 0.25)
    return (quarters)

# calculate no of dimes


def calculate_dimes(dollar_owed):

    dimes = dollar_owed / 0.10
    dimes = math.floor(dimes)
    return dimes

# calculate no of nickels


def calculate_nickels(dollar_owed):

    nickels = math.floor(dollar_owed / 0.05)
    return nickels

# calculate no of pennies


def calculate_pennies(dollar_owed):

    pennies = dollar_owed / 0.01

    # Check for integer overflow
    if pennies > 0 and pennies < 1:
        return 1
    elif pennies > 1 or pennies == 1:
        pennies = math.floor(pennies)
        return pennies
    else:
        return 0


main()
