"""
Using the Python language, have the function VowelCount(str) take the str string parameter being passed and return the
number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for
this challenge.
"""
def VowelCount(str):
    result = 0
    array = list(str)
    for letter in array:
        if letter in ("a","e","i","o","u"):
            result += 1
    return result

print(VowelCount("coderbyte"))
print(VowelCount("aaaaa"))
