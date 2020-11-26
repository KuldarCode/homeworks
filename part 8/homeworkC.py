def closest_nr1(your_pick, the_list):
    closest_nr = 1
    minimum = float("inf")

    for current_number in the_list:
        if abs(current_number - your_pick) < minimum:
            minimum = abs(current_number - your_pick)
            closest_nr = current_number

    return closest_nr


yourpick1 = float(input("add a number: "))
numbers = [1.3, 4123, 12, 246]
print(closest_nr1(yourpick1, numbers))