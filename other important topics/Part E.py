import random


def closest_nr1(search_list, target):
    closest_nr = None
    minimum = float("inf")

    for number in search_list:
        if abs(number - target) < minimum:
            minimum = abs(number - target)
            closest_nr = number
    return closest_nr


MAX_NUM = 100

num_items = 5  # FIXME: replace with function to ask the user how many items

def num_items(items_in_list):
    return items_in_list

user_list = random.sample(range(0, 100), num_items)  # FIXME: replace with function to ask for list

your_target = random.randint(0, MAX_NUM)  # FIXME: replace with function to ask for target pick

closest = closest_nr1(user_list, your_target)

print("Search list: [{}]".format(",".join(str(i) for i in user_list)))
print("Target Number: {}".format(your_target))
print("Closest Number: {}".format(closest))
print(num_items(5))