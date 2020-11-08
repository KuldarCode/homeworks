from random import randint
yourPick = int(input("isert a numbert, so my program can guess it: "))
computerP = randint(1,10)
while yourPick != computerP:
    computerP = randint(1,10)
    print(computerP)
    if yourPick == computerP:
        print(computerP)
