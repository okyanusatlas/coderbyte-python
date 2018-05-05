"""
Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize the
first letter of each word. Words will be separated by only one space.
"""

def LetterCapitalize(str):
    words = str.split(" ")
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)

print(LetterCapitalize("i ran there"))