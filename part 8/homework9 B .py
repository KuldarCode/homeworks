def factorial(number):
    f = 1
    while number > 0:
        f = number * f
        number -= 1
    return f

print(factorial(7)/factorial(3))