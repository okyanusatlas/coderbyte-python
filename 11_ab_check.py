"""
Using the Python language, have the function ABCheck(str) take the str parameter being passed and return the string true
if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed"
would result in true because there is exactly three characters between a and b). Otherwise return the string false.
"""

def ABCheck(str):

    array = list(str)
    for counter, letter in enumerate(array):
        if counter+4 < len(array):
            if letter == "a" and array[counter+4] == "b":
                return True
        else:
            return False

    return array


print(ABCheck("lane borrowed"))
