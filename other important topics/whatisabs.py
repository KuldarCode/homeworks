
def get_user_number(text, max):
    input_number = int(input(text))
    if input_number < 0 or input_number > max:
        result = 0
    else:
        result = input_number
    return result


def num_items(list_size):
    the_list = []
    while list_size > 0:
        the_list.insert(1, list_size)
        list_size = list_size - 1
    return the_list


size = int(input("list size: "))
print(size)
print(num_items(size))


