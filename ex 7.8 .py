from random import randint, random
randomNumber = randint(1, 10)
intputNumber = int(input("Try to figure out what number computer got : "))
if randomNumber != intputNumber:
    print("Try again!")

else:
    print("YOu got it right")