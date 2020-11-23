firstLook = input("What do you love most?: ")
words = firstLook.split(" ")
print(words)
noCaps = firstLook[1:]
yesCaps = firstLook[0]
names = words.find(0,1)

print(noCaps)


for letter in yesCaps:
    yesCaps = letter.upper()
    print(yesCaps)
    for letters in noCaps:
        words = letters.lower()
        print(words)














#for word in words:

    #print(word)
