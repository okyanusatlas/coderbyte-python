"""
Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest
 word in the string. If there are two or more words that are the same length, return the first word from the string with
  that length. Ignore punctuation and assume sen will not be empty.
"""

def LongestWord(sen):
    sentence = sen.split()
    result = sentence[0]
    for word in sentence:
        if len(word) > len(result):
            result = word

    return result


print(LongestWord("I lo dogs"))