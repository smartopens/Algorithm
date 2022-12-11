n, l = map(int, input().split(' '))
area = [list(map(int, input().split(' '))) for _ in range(n)]
ans = 0

def canGo(road):
    idx = 0
    first = road[idx]
    w = 1

    while idx < n - 1:
        if first == road[idx+1]:
            w += 1
            idx += 1

        elif first == road[idx + 1] - 1:
            if w < l:
                return False
            else:
                first = road[idx + 1]
                idx += 1
                w = 1

        elif first == road[idx + 1] + 1:
            if idx + l > n-1:
                return False
            else:
                temp = road[idx+1]
                for t in range(l):
                    if road[idx+t+1] != temp:
                        return False
                first = road[idx + 1]
                idx += l
                w = 1
        else:
            return False

    return True


for i in range(n):
    if canGo(area[i]):
        ans += 1

    colRoad = [area[j][i] for j in range(n)]
    if canGo(colRoad):
        ans += 1

print(ans)