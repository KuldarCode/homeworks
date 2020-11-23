def roundit( number ):
    roundedNr = round(float(number))
    print(roundedNr)
    if roundedNr % 2 == 0:
        answer = True
    else:
        answer = False
    print(answer)
roundit(1.1)
roundit(5.6)
roundit(17.6)
