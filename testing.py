def roundit( number ):
    roundedNr = round(float(number))
    print(roundedNr)
    if roundedNr % 2 == 0:
        print("True")
    else:
        print("False")
roundit(1.8)
roundit(1.1)
roundit(5.6)
roundit(17.6)