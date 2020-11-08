data =  """ How much Wood would a woodchuck chuck If a woodchuck could chuck wood? He would WOOD chuck, he would, as much as he could, And chuck as much as a woodchuck would If a woodchuck could chuck wood."""

#print(tea)
#print(len(tea))
#for i in tea:
#    print(i)
#if len(tea) >= 7:
#    print(tea[7])
#print(tea[0:3])
print(data)
words = data.split(" ")
#print(words)
countWood = 0
for word in words:
    word = word.replace("?", "")
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.lower()
    if word == "wood":
        print("wood")
        countWood += 1
    print(word)
print(countWood)
#    print(len(word))
#print(len(data))
#print(len(words))
#print(",".join(words))