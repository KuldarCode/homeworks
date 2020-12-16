from random import randint

def roll_dice(number_times, number_sides):
    total = 0
    for i in range(0, number_times):
        dice = randint(1, number_sides)
        print(dice)
        total = total + dice
    return total

while True:
    dice_times = int(input("how many times you like to throw: "))
    if dice_times == 0:
        break
    dice_size = int(input("how many sides of dice: "))
    all = roll_dice(dice_times, dice_size)
    print(all)

print("round over!")