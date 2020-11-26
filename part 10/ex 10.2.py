text = """And sending tinted postcards of places they don 't
realise they haven 't even visited to 'All at nu[m]ber 22, weather
w[on]derful, our room is marked with an 'X '. Wish you were here.
Food very greasy but we 've fo[tere]und a charming li[t]tle local place
hidden awa[y ]in the back streets where they serve Watney 's Red
Barrel and cheese and onion cris[p123124]s and the accordionist pla[y]s
"Maybe i[t] 's because I 'm a Londoner" ' and spending four days on
the tarmac at Luton airport on a five-day package tour wit[h]
n[o]thing to eat but dried Watney 's sa[n]dwiches..."""

while True:
    firstBrack = text.find("[")
    if firstBrack == -1:
        break
    firstBrack += 1
    secondBrack = text.find("]")
    print(text[firstBrack:secondBrack])
    #print(firstBrack)
    #print(secondBrack)
    #print(text[secondBrack + 1:])
    text = text[secondBrack + 1:]
