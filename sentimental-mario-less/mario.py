# TODO

from cs50 import get_int


def main():

    # Get user input & check for conditions
    # assign values for white spaces and hashes

    n = 0
    while n <= 0 or n >= 9:
        n = get_int("Height: ")
        x = n - (n - 1)
        y = n - 1
        i = 1

    while i <= n:
        hash(x, y)

        # tabulate white spaces and hash
        
        x = x + 1
        y = y - 1
        i = i + 1

# print mario pattern


def hash(x, y):
    a = ' '
    b = "#"

    # print whitespace and hash

    print(f"{a * y}{b * x}")


main()
