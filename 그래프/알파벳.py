r, c = map(int, input().split(' '))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global result

    q = set()
    q.add((x, y, array[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and array[nx][ny] not in step:
                q.add((nx, ny, step + array[nx][ny]))


array = []
result = 1

for _ in range(r):
    array.append(input())

bfs(0, 0)
print(result)
