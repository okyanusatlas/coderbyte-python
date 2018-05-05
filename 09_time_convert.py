"""
Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the number
of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of
hours and minutes with a colon.
"""

def TimeConvert(num):
    hour = 0
    while num > 60:
        num -= 60
        hour += 1
    return str(hour) + ":" + str(num)


print(TimeConvert(126))
