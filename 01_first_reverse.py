"""
Using the Python language, have the function FirstReverse(str) take the str parameter being passed and return the string
in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the
string sredoC dna dlroW olleH.
"""
def FirstReverse(str):
    #split  - reverse - join
    array =  list(reversed(list(str)))
    result = ''.join(array)


    return result


print (FirstReverse("123456789"))