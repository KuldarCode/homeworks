from random import randint
randomNumber = randint(1, 3)
print(randomNumber)
number1 = 0
print("computer will generate random number from 1 to 1000, try to guess it!")
while number1 is not randomNumber:
    number1 = int(input("Number is:  "))
    if number1 > randomNumber:
        print("random number is smaller!")
    if number1 < randomNumber:
        print("random number is bigger!")
if number1 > randomNumber:
    print("random number is smaller!")
if number1 < randomNumber:
    print("random number is smaller!")
if number1 == randomNumber:
    print("well done!")