from collections import deque

n, k = map(int, input().split())
bottom = deque(list(map(int, input().split())))
fish_home = [[0] * n for _ in range(n)]
ans = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(len(bottom)):
    fish_home[n - 1][i] = bottom[i]

while True:
    max_num = max(bottom)
    min_num = min(bottom)
    if max_num - min_num <= k:
        break

    print(bottom)
    for i in range(n-10,n):
        for r in range(len(bottom)):
            print(fish_home[i][r], end = ' ')
        print()
    print()

    for i in range(len(bottom)):
        if bottom[i] == min_num:
            bottom[i] += 1

    fish_home[n - 2][0] = fish_home[n - 1][0]
    for i in range(len(bottom)):
        fish_home[n - 1][i] = bottom[i]

    fish_home[n - 1][-1] = 0
    bottom.popleft()
    clear_done = False
    print(bottom)
    for i in range(n-10,n):
        for r in range(len(bottom)):
            print(fish_home[i][r], end = ' ')
        print()
    print()

    while True:
        if clear_done:
            break
        rotate_stack = []
        rotate_num = 0

        for c in range(n):
            tmp = [fish_home[n-1][c]]
            idx = 1
            while fish_home[n-1-idx][c] != 0:
                tmp.append(fish_home[idx][c])
                idx += 1

            if len(tmp) > 1:
                rotate_stack.append(tmp)
            else:
                break
            rotate_num += 1

        for _ in range(rotate_num):
            bottom.popleft()

        if rotate_stack and len(rotate_stack[-1]) > len(bottom):
            break

        for i in range(len(bottom)):
            fish_home[n - 1][i] = bottom[i]

        for i in range(rotate_num):
            fish_home[n - 1][len(bottom) + i] = 0

        s_idx = 1
        for i in range(len(rotate_stack) - 1, -1, -1):
            for j in range(len(rotate_stack[i])):
                fish_home[n - 1 - s_idx][j] = rotate_stack[i][j]
            s_idx += 1

        print(bottom)
        for i in range(n-10,n):
            for r in range(len(bottom)):
                print(fish_home[i][r], end = ' ')
            print()
        print()

    change_num = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if fish_home[r][c] > 0:

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < n and 0 <= nc < n:
                        if fish_home[r][c] - fish_home[nr][nc] > 0:
                            tmp = (fish_home[r][c] - fish_home[nr][nc]) % 5
                            if tmp > 0:
                                change_num[r][c] -= tmp
                                change_num[nr][nc] += tmp

    for r in range(n):
        for c in range(n):
            if change_num[r][c] != 0:
                fish_home[r][c] += change_num[r][c]

    rotate_stack = []
    s_idx = 0
    for c in range(n):
        tmp = []
        idx = 0
        while fish_home[idx][c] != 0:
            tmp.append(fish_home[idx][c])
            idx += 1

        if len(tmp) > 1:
            rotate_stack.append(tmp)
        else:
            break
        s_idx += 1

    new_bottom = deque([])
    for i in rotate_stack:
        for j in i:
            new_bottom.append(j)

    bottom = list(new_bottom + bottom)
    rotate_stack1 = [deque(reversed(bottom[:len(bottom) // 2])), bottom[len(bottom) // 2:]]
    rotate_stack2 = [deque(reversed(rotate_stack1[-2][:len(rotate_stack1[-2])])),
                     deque(reversed(rotate_stack1[-2][:len(rotate_stack1[-2])])),
                     rotate_stack1[-2][len(rotate_stack1[-2]):], rotate_stack1[-1][len(rotate_stack1[-1]):]]


    bottom = deque([])
    s_idx = 0
    for c in range(len(rotate_stack2[0])):
        for i in range(3,-1,-1):
            bottom.append(rotate_stack2[i][c])


    fish_home = [[0] * n for _ in range(n)]
    for i in range(len(bottom)):
        fish_home[n - 1][i] = bottom[i]
    ans += 1

print(ans)
