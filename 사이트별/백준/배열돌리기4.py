from itertools import permutations

n, m, k = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]
rotates = [list(map(int, input().split())) for _ in range(k)]
rotate_len = len(rotates)
orders = range(rotate_len)
answer = 1e9

def rotate(num_list, sr, sc, s):

    for ds in range(1, s + 1):
        nr, nc = sr - ds, sc - ds
        ori_sr, ori_sc = nr, nc
        first_tmp = num_list[nr][nc]

        for i in range(1, 2 * ds + 1):
            if 0 <= nr < n and 0 <= nc < m and 0 <= nr + 1 < n and 0 <= nc < m:
                num_list[nr][nc] = num_list[nr + 1][nc]
            nr += 1

        for i in range(1, 2 * ds + 1):
            if 0 <= nr < n and 0 <= nc < m and 0 <= nr < n and 0 <= nc + 1 < m:
                num_list[nr][nc] = num_list[nr][nc + 1]

            nc += 1
        for i in range(1, 2 * ds + 1):
            if 0 <= nr < n and 0 <= nc < m and 0 <= nr - 1 < n and 0 <= nc < m:
                num_list[nr][nc] = num_list[nr - 1][nc]

            nr -= 1
        for i in range(1, 2 * ds + 1):
            if 0 <= nr < n and 0 <= nc < m and 0 <= nr < n and 0 <= nc - 1 < m:
                if nr == ori_sr and nc - 1 == ori_sc:
                    num_list[nr][nc] = first_tmp
                    nc -= 1
                    break
                num_list[nr][nc] = num_list[nr][nc - 1]

            nc -= 1

    return num_list


ori_num_list = [x[:] for x in num_list]

for order in permutations(orders, rotate_len):
    num_list = [x[:] for x in ori_num_list]
    tmp_ans = 1e9

    order = list(order)
    for i in order:
        sr, sc, s = rotates[i]
        sr, sc = sr - 1, sc - 1
        num_list = rotate(num_list, sr, sc, s)

    for i in num_list:
        tmp_ans = min(tmp_ans, sum(i))

    answer = min(answer, tmp_ans)

print(answer)
