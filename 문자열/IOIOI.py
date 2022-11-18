n = int(input())
m = int(input())

problem = input()
p_len = 2*n+1
possible_list = []
pro_len = len(problem)
tmp = ""
is_ok = False
ans = 0

for i in range(len(problem)):
    if problem[i] == "I" and not is_ok:
        is_ok = True

    if (problem[i] == "I" and i+1 < pro_len and problem[i+1] == "I") or (i == len(problem)-1)\
            or (problem[i] == "O" and i+1 < pro_len and problem[i+1] == "O"):
        if problem[i] == "I":
            tmp += problem[i]
        if len(tmp) > 1:
            possible_list.append(tmp)
        is_ok = False
        tmp = ""
        continue

    if is_ok:
        tmp += problem[i]


for case in possible_list:
    if len(case) >= p_len:
        tmp =  (len(case)-p_len)//2 + 1
        ans += tmp

print(ans)

