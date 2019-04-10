# Set the value of formatter to four seperate strings. 
formatter = "{} {} {} {}"
# print 1 2 3 4 
print(formatter.format(1,2,3,4))
# print one two three four
print(formatter.format("one", "two", "three", "four"))
# print True False False True
print(formatter.format(True, False, False, True))
# print the value of formatter as strings. This will print four times. 
print(formatter.format(formatter, formatter, formatter, formatter))
# print some string using the formmater 
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))
