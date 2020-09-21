num1 = 0
num2 = 1
print( 1, end=" " )
while True:
    num3 = num1 + num2
    if num3 > 1000:
        break
    print( num3, end=" " )
    num1 = num2
    num2 = num3