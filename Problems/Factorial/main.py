n = int(input().strip())
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(factorial)
