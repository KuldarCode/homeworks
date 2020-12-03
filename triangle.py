def area_of_triangle(base, height):
    calculation = base * height / 2
    return calculation
#print(area_of_triangle(3,4))

def format_message(message, make_uppercase):
    if make_uppercase == True:
        message = message.upper()
    return message
#print(format_message("hello world", False))



def is_in_range(num, max):
    if num >= 0:
        if num < max:
            result = True
        else:
            result = False
    else:

        result = False

    return result

def is_in_range2(num, max):
    if num >= 0 and num < max:
        result = True
    else:
        result = False
    return result


def get_user_number (text, max):
    if text >= 0 and text < max:
        result = text
    else:
        result = 0
    return result

def list_of_numbers(input):


    listing = int(input("add numbers for list: "))

print(get_user_number(int(input("Add a number: ")), 30))
#print(is_in_range(33,10))