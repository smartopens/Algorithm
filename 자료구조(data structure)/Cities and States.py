from collections import defaultdict

n = int(input())
city_graph = dict()
answer = 0

for _ in range(n):
    x,y = map(str, input().split())
    x = x[:2]
    if x not in city_graph:
        city_graph[x] = defaultdict(int)
        city_graph[x][y] = 1
    else:
        if y not in city_graph[x]:
            city_graph[x][y] = 1
        else:
            city_graph[x][y] += 1

    if x == y:
        continue
    if y in city_graph:
        if x in city_graph[y]:
            answer += city_graph[y][x]

print(answer)