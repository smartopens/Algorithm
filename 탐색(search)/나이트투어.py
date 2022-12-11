pathes = [input() for _ in range(36)]
int_pathes = []

row_c_dict = {"6": 0, "5": 1, "4": 2, "3": 3, "2": 4, "1": 5}
col_c_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
s_r,s_c = row_c_dict[pathes[0][1]], col_c_dict[pathes[0][0]]

for path in pathes:
    r, c = path[1], path[0]
    int_pathes.append((row_c_dict[r], col_c_dict[c]))

int_pathes.append((s_r,s_c))

is_valid = False
vi = [[0] * 6 for _ in range(6)]
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, -2, -1, 1, 2]

def dfs(idx):
    global is_valid

    r, c = int_pathes[idx]
    vi[r][c] = 1

    if idx == 36:
        if r == s_r and c == s_c:
            is_valid = True
        return

    if idx == 0:
        vi[r][c] = 0

    tr, tc = int_pathes[idx+1]

    for i in range(8):
        nr,nc = r + dr[i], c + dc[i]

        if 0 <= nr < 6 and 0 <= nc < 6:
            if not vi[nr][nc] and nr == tr and nc == tc:
                dfs(idx+1)


dfs(0)

if is_valid:
    print("Valid")
else:
    print("Invalid")