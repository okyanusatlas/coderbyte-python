"""
Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it
is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols
with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
So the string to the left would be false. The string will not be empty and will have at least one letter.

"""


def simple_symbols(word):
    words = list(word)
    plus_counter = 0
    for word in words:
        if word == "+":
            plus_counter += 1
        if 96 < ord(word) < 123:
            if plus_counter == 0:
                return False
            elif plus_counter >= 1:
                plus_counter = 0

    return plus_counter >= 1


print(simple_symbols("+a++"))
print(simple_symbols("++d+=3=+s"))

