def PrimeN():
    num = int(input("add a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number ")
                print(i, "times" , num//i, "is",num)
                break
        else:
            print(num, "is prime number")
    else:
        print(num, (" is not prime number"))
#PrimeN()
def fibo():
    num1 = 0
    num2 = 1
    count = 0
    total = 11
    print("Fibonacci sequence:")
    while count < total:
        print(num1)
        fib = num1 + num2
        num1 = num2
        num2 = fib
        count += 1
    if num1 >10:
        print("done!")

fibo()