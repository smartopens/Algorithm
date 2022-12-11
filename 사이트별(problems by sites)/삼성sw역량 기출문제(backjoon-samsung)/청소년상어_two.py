import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def food(array, x, y):
    positions = []
    direction = array[x][y][1]
    for _ in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


def move_fish(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        dir = array[x][y][1]

        for _ in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_x and ny == now_y):
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], array[x][y][1]
                    break
            dir = (dir + 1) % 8


def dfs(array, x, y, total):
    global answer
    array = copy.deepcopy(array)

    number = array[x][y][0]
    array[x][y][0] = -1

    move_fish(array, x, y)

    result = food(array, x, y)

    answer = max(answer, total + number)
    for next_x, next_y in result:
        dfs(array, next_x, next_y, total + number)


temp = [list(map(int, input().split())) for _ in range(4)]
array = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1]

answer = 0
dfs(array, 0, 0, 0)
print(answer)