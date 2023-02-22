formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "If the weather will be nice",
    "Maybe we will go in a honeymoon twice",
    "You and me, and me and you",
    "You know I love you!"))
