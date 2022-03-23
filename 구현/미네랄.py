def dfs():

    return

n, m = map(int, input().split())
mineralMap = []
for _ in range(n):
    mineralMap.append(list(input()))

#print(mineralMap)

k = int(input())
rows = list(map(int, input()))

isLeft = True
for _ in range(k):
    row = rows.pop(0)
    if isLeft:
        for c in range(m):
            if mineralMap[row][c] == "x":
                mineralMap[row][c] = "."
                break
            dfs(mineralMap)
            isLeft = False

    else:
        for c in range(m-1,0,-1):
            if mineralMap[row][c] == "x":
                mineralMap[row][c] = "."
                break
            dfs(mineralMap)
            isLeft = True

