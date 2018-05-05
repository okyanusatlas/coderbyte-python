"""
Using the Python language, have the function ExOh(str) take the str parameter being passed and return the string true if
there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered in
the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false because
there are 6 x's and 5 o's.
"""


def ExOh(str):

    counter = 0
    array = list(str)
    for letter in array:
        if letter == "x":
            counter += 1
        if letter == "o":
            counter -= 1

    return counter == 0

print(ExOh("xooxxoxo"))