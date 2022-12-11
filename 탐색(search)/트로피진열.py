def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            result = result + 1
            now = array[i]

    print(result)


test_case = int(input())
array = []

for _ in range(test_case):
    array.append(int(input()))

ascending(array)
array.reverse()
ascending(array)
