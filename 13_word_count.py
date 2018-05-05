"""
Using the Python language, have the function WordCount(str) take the str string parameter being passed and return the
number of words the string contains (e.g. "Never eat shredded wheat or cake" would return 6). Words will be separated by
 single spaces.
"""

def WordCount(str):

    return len(str.split())

print(WordCount("He Wo"))
print(WordCount("one 22 three"))