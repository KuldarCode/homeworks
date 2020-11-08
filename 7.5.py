lastNum = 0
prevPrev = 1
prev = 1
print("1")
print("1")
while lastNum <= 1000:
    lastNum = prevPrev + prev
    prevPrev = prev
    prev = lastNum
    print(lastNum)
