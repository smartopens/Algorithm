from itertools import combinations

n = int(input())
skills = [list(map(int, input().split())) for _ in range(n)]
total_score = 0
answer = 1e9
total_set = set(list(range(n)))
set_vi = set()

for link in combinations(range(n),n//2):
    link_score = 0
    start_score = 0
    link = set(link)
    start_set = total_set - link

    for r in link:
        for c in link:
            if r == c:
                continue
            link_score += skills[r][c]

    for r in start_set:
        for c in start_set:
            if r == c:
                continue
            start_score += skills[r][c]

    tmp_score = abs(link_score-start_score)

    if answer > tmp_score:
        answer = tmp_score

print(answer)
