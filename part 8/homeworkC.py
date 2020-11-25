def closest_nr1():
    closest_nr = 1
    minimum = float("inf")
    the_list = [1, 2, 3, 1, 102, 312, 23, 431, 42, 12, 1, 432]
    your_pick = int(input("add a number: "))

    for number in the_list:
        if abs(
                number - your_pick) < minimum:
            minimum = abs(number - your_pick)

    print(closest_nr)


closest_nr1()
