# TODO

from cs50 import get_string


def main():

    # Get text from user

    text = get_string("Text:")

    # Calculate letters

    letters = numberofletters(text)

    # Calculate word

    words = numberofwords(text)

    # Calculate sentences

    sentences = numberofsentences(text)

    # Calculate Index

    index = calculateindex(letters, words, sentences)

    # Check range of index

    if index < 1:
        print("Before Grade 1")
    elif index >= 1 and index <= 16:
        print(f"Grade {round(index)}")
    elif index > 16:
        print("Grade 16+")


def numberofletters(text):

    letters = 0

    # check for no of letters

    for i in text:
        if (i.isalpha()):
            letters += 1
    return letters


def numberofwords(text):

    words = 0

    # check for spaces to calculate no of words

    for i in text:
        if (i.isspace()):
            words += 1
    words += 1

    return words


def numberofsentences(text):

    sentences = 0

    # Check for . , ! & ? to calculate the end of sentences

    for i in text:
        if i == '.' or i == '!' or i == '?':
            sentences += 1

    return sentences


def calculateindex(letters, words, sentences):

    # Calculate s & l & index

    l = (letters / words) * 100
    s = (sentences / words) * 100
    index = (0.0588 * l) - (0.296 * s) - 15.8

    return index


main()

