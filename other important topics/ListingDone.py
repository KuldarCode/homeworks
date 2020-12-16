
def get_user_number(text, max):
    input_number = int(input(text))
    if input_number < 0 or input_number > max:
        result = 0
    else:
        result = input_number
    return result


def get_list(list_size):
    the_list = []
    while list_size > 0:
        the_list.insert(1, get_user_number("give number to list: ", MAX_NUM))
        list_size = list_size - 1
    return the_list


def closest_nr1(search_list, target):
    closest_nr = None
    minimum = float("inf")

    for number in search_list:
        if abs(number - target) < minimum:
            minimum = abs(number - target)
            closest_nr = number
    return closest_nr


MAX_NUM = 100

how_many_items = get_user_number("How many items you like to be inside the list: ", MAX_NUM) # FIXME: replace with function to ask the user how many items

user_list = get_list(how_many_items) # FIXME: replace with function to ask for list
print(user_list)

your_target = closest_nr1(user_list, get_user_number("your target: ", MAX_NUM))# FIXME: replace with function to ask for target pick
print(your_target)
