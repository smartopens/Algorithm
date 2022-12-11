from itertools import permutations

n = int(input())
nArr = [x for x in range(1,n + 1)]

for p in permutations(nArr, n):
    for pi in p:
        print(pi, end = ' ')
    print()