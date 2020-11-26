yourNum = int(input("add a number: "))
numbers = [1.3, 2, 3, 1, 102, 312, 23, 431, 42, 12, 1, 432]
for number in numbers:
    if number - yourNum < minimum:
        closest = number