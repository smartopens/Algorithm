from copy import deepcopy

fishDirect = dict()
space = [[0] * 4 for _ in range(4)]
direct = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
ans = 0

def food(array, x,y,dir):  # 상어가 먹을 수 있는 후보 위치 반환
    positions = []

    for i in range(1, 4):
        nx, ny = x + direct[dir][0], y + direct[dir][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions


def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j] == index:
                return (i, j)
    return None

def move_fish(array, now_x, now_y):  # 물고기 이동
    flag = False
    position = []
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        dir = fishDirect[array[x][y]] # 방향
        for j in range(8):
            nx, ny = x + direct[dir][0], y + direct[dir][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_x and ny == now_y) and array[nx][ny] != 17:  # 공간의 경계, 상어 있는 칸 확인
                    # 값 교체
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                    break
            dir = (dir + 1) % 8


def dfs(x, y, sdi, score,space):
    global ans
    space = deepcopy(space)
    sdi = fishDirect[space[x][y]]
    number = space[x][y]
    space[x][y] = 17

    move_fish(space,x,y)
    result = food(space, x,y,sdi)

    # 해당 먹이 먹는 모든 과정 탐색

    ans = max(ans, score + number)
    for next_x, next_y in result:
        dfs(next_x, next_y, sdi,score + number,space)



for i in range(4):
    info = input().split(' ')
    k = 0
    for j in range(0, len(info), 2):
        fishDirect[int(info[j])] = (int(info[j + 1]) - 1)
        space[i][k] = int(info[j])
        k += 1

print(fishDirect)
for s in space:
    print(s)
print()

dfs(0, 0, 0, 0,space)
print(ans)