import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Error: Include DNA database and sequence")
        sys.exit()

    # TODO: Read database file into a variable
    dna = []
    with open(sys.argv[1]) as f_dna:
        reader = csv.reader(f_dna)
        for row in reader:
            dna.append(row)

    # TODO: Read DNA sequence file into a variable

    with open(sys.argv[2]) as f_sequence:
        for line in f_sequence:
            sequence = (line)

    # TODO: Find longest match of each STR in DNA sequence

    str = dna[0]
    x = len(str)
    str_count = []
    str_index = 0

    # load str values in str count list

    for i in range(1, x):
        l_m = longest_match(sequence, str[i])
        str_count.append(l_m)
        str_index += 1

    # TODO: Check database for matching profiles
    # copy each index of dna into a variable "persona" excluding first element
    # compare str count with strs in persona

    y = 1
    dna_index = len(dna)
    while y < dna_index:
        persona = dna[y]
        compare_str(persona, str_count, str_index)
        y += 1
    print("No Match")

    return


def compare_str(persona, str_count, str_index):

    count = 0
    j = 0
    for j in range(str_index):
        if int(str_count[j]) == int(persona[j+1]):
            count += 1
    if count == len(str_count):
        print(f"{persona[0]}")
        exit()


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
