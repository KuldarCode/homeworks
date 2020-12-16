from random import randint
dice_times = 1

while dice_times > 0:
    dice_times = int(input("how many times you like to throw: "))
    dice_size = int(input("how many sides of dice: "))
    total = 0
    dice_times_counter = dice_times
    while dice_times_counter >= 1:
        dice = randint(1, dice_size)
        dice_times_counter = dice_times_counter - 1
        print(dice)
        total = total + dice
    print("your score is", total)
#print("round over!")
#print(dice)