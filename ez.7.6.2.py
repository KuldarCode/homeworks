total = 0
biggest = float("-inf")
smallest = float("inf")
div3 = 0

for i in range(5):
    usernum = int(input("add a number"))
    if usernum % 3 == 0:
        div3 += 1
        print(div3)
    if usernum <= smallest:
        smallest = usernum
    if usernum >= biggest:
        biggest = usernum
    if usernum <= -1:
        break
    if usernum == 0:
        break
    total += usernum


print("total is {:} " .format(total))
print("smallest number is {:}".format(smallest))
print("divisible by 3 is {:}".format(div3))
print("Biggest number is {:}" .format(biggest))