def closest_nr1(your_pick, the_list):
    closest_nr = 1
    minimum = float("inf")

    for current_number in the_list:
        if abs(current_number - your_pick) < minimum:
            minimum = abs(current_number - your_pick)
            closest_nr = current_number

    return closest_nr
def getnumber(asknumber):
    ants = float(input("add a another number: "))
    return ants

#def getlist(size):

    #list =


numbers = getlist(8)

print(getlist(3))

yourpick1 =  getnumber(1)
print(closest_nr1(yourpick1, numbers))

yourpick1 =  getnumber(1)
print(closest_nr1(yourpick1, numbers))
