from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
p_arr = permutations(arr,n)

ans = 0

for p in p_arr:
    plus = 0

    for i in range(1,len(p)):
        plus += abs(p[i]- p[i-1])
    ans = max(ans, plus)

print(ans)
