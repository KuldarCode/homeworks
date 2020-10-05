div3 = 0
word1 = input("add first word: ")
word2 = input("add a second word: ")
common = ""
for letter in word1:
    if (letter in word2) and (letter not in common):
        common += letter

# I DONT UNDERSTAND ! xD
