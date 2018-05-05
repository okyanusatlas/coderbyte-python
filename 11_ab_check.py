"""
Using the Python language, have the function ABCheck(str) take the str parameter being passed and return the string true
if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed"
would result in true because there is exactly three characters between a and b). Otherwise return the string false.
"""

def ABCheck(str):

    array = list(str)
    for counter, letter in enumerate(array):
            if letter == "a" and counter+4 < len(array) and array[counter+4] == "b":
                return True

    return False


print(ABCheck("lane borrowed"))
print(ABCheck("after badly"))
