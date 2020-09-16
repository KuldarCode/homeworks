gradeX = float(input("write your grade: "))
if gradeX > 10:
    exit()
elif gradeX < 0:
    exit()
elif gradeX >= 8.5:
    print("You got 'A'")
elif gradeX >= 7.5:
    print("You got 'B'")
elif gradeX >= 6.5:
    print("You got 'C'")
elif gradeX >= 5.5:
    print("you got 'D'")
else:
    print("You got 'F'")
