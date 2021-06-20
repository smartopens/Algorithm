from itertools import combinations

while True:

    n_list = list(map(int, input().split(' ')))
    f = n_list.pop(0)

    if f == 0:
        break

    result = []
    for loto in combinations(n_list, 6):
        result.append(list(loto))

    for i in result:
        for j in range(len(i)):
            if j == len(i) - 1:
                print(i[j], end='')
            else:
                print(i[j], end=' ')
        print()
    print()