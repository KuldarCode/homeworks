from random import randint
max_num = 10
list_of_randoms = [0] * max_num
num_times = 100000000
for i in range(1, num_times):
    number = randint(0, max_num - 1)
    #print(number)
    list_of_randoms[number] += 1
print(list_of_randoms)