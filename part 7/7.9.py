from random import randint
maxNr = 1000
minNr = 0
yourPick = int(input("isert a numbert, so my program can guess it: "))
#computerP = int(maxNr/2)
computerP = randint(0, maxNr)
while yourPick != computerP:
    print(computerP)
    computerAsk = input("is number Higher (H) or Lower (L) ? ")
    if computerAsk == "H":
        minNr = computerP
    else:
        maxNr = computerP
    computerP = randint(minNr + 1, maxNr - 1)
    #computerP = int ((maxNr - minNr) / 2 + minNr)
    #print(computerP)
if yourPick == computerP:
    print(computerP)