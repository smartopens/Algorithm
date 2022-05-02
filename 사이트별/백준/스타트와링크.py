import sys
from itertools import combinations
from itertools import permutations

n = int(input())
team = set(i for i in range(n))
score = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize


for start in combinations(team, n//2):
    link = team - set(start)
    sScore = 0
    lScore = 0

    for i, j in permutations(start, 2):
        sScore += score[i][j]

    for i, j in permutations(link, 2):
        lScore += score[i][j]

    ans = min(ans, abs(sScore - lScore))

print(ans)