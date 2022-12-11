msg = input()
key = input()
key_vi = set()
alpha_set = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'}

alpha_vi = set()
board = [[0] * 5 for _ in range(5)]
idx = 0

for r in range(5):
    if idx >= len(key): break
    for c in range(5):
        if key[idx] not in key_vi:
            board[r][c] = key[idx]
            key_vi.add(key[idx])
        else:
            while idx + 1 != len(key) and key[idx] in key_vi:
                idx += 1
            if key[idx] not in key_vi:
                board[r][c] = key[idx]
                key_vi.add(key[idx])
        idx += 1
        if idx >= len(key): break
plus = alpha_set - key_vi
plus = list(plus)
plus.sort()

idx = 0
for r in range(5):
    if idx >= len(plus): break
    for c in range(5):
        if board[r][c] == 0:
            board[r][c] = plus[idx]
            idx += 1
            if idx >= len(plus): break


idx = 0
new_msg = []

while idx < len(msg):
    if idx + 1 <= len(msg)-1 and msg[idx] == msg[idx + 1]:
        if msg[idx] == "X":
            new_msg.append(msg[idx] + "Q")
            idx += 1
        else:
            new_msg.append(msg[idx] + "X")
            idx += 1
    else:
        if idx + 1 != len(msg):
            new_msg.append(msg[idx] + msg[idx + 1])
            idx += 2
        else:
            new_msg.append(msg[idx] + "X")
            idx += 2

answer = ""

for msg in new_msg:
    tmp = []
    for r in board:
        cnt = 0
        for i in msg:
            if i in r:
                cnt += 1
        if cnt >= 2:
            tmp = r
            break
    if cnt == 2:
        for i in msg:
            for j in range(len(tmp)):
                if tmp[j] == i:
                    answer += tmp[(j+1)%5]
                    break

        continue

    is_done = False
    tmp = []
    cnt = 0
    for c in range(5):
        cnt = 0
        m_i = 0
        v_i = set()
        if is_done: break

        for r in range(5):
            for j in range(2):
                if j not in v_i and board[r][c] == msg[j]:
                    cnt += 1
                    v_i.add(j)

        if cnt == 2:
            is_done = True
            for k in range(5):
                tmp.append(board[k][c])
            break

    if tmp:
        for i in msg:
            for j in range(len(tmp)):
                if tmp[j] == i:
                    answer += tmp[(j+1)%5]
                    break
        continue

    tmp = []
    for i in msg:
        is_done = False
        for r in range(5):
            if is_done: break
            for c in range(5):
                if i == board[r][c]:
                    tmp.append((r,c))
                    is_done = True
                    break

    if len(tmp) >= 2:
        x1, y1, x2, y2 = tmp[0][0], tmp[0][1],tmp[1][0], tmp[1][1]
        answer += board[x1][y2]
        answer += board[x2][y1]

print(answer)
