n = int(input())

a, b = 0, 1

while n > 0:
    result = a + b
    a, b = b, result
    n = n - 1

print(a)
