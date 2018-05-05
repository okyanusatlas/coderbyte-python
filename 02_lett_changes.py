"""
Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using
the following algorithm. Replace every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this
modified string.
"""

def LetterChanges(str):
    str = list(str)
    asciiList = []
    for letter in str:
        asciiList.append(ord(letter))

    for counter, ascii_code in enumerate(asciiList):
        if ascii_code > 64:
            if ascii_code == 122:
                asciiList[counter] = "a"
            else:
                ascii_code += 1
                if chr(ascii_code) in ('a', 'e', 'i', 'o', 'u'):
                    asciiList[counter] = chr(ascii_code).capitalize()
                else:
                    asciiList[counter] = chr(ascii_code)
        else:
            asciiList[counter] = chr(ascii_code)


    result = ''.join(asciiList)

    return result


print(LetterChanges("beautifulz^"))
