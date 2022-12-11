test_case = int(input())

for _ in range(test_case):
    n = int(input())
    result = ""

    while (n):
        if n % 2 == 0:
            i = n // 2
            result += "1" * i
            n = 0
        else:
            n = n - 3
            result += "7"

    print(int(result))
