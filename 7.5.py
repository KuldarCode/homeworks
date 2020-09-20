fibonacci = 1001
count = 1
while fibonacci >= 1001:
    count += count + count
    print(count)
    fibonacci = fibonacci - 1
