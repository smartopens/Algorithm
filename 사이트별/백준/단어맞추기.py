t = int(input())
test = "aaaa"
test2 = "abba"

for _ in range(t):
    problem = input()
    len_p = len(problem)
    p_list = list(problem)
    is_ok = True
    idx = len_p - 2
    idx2 = len_p - 1

    while idx >= 0 and p_list[idx] >= p_list[idx+1]:
        idx -= 1

    if idx < 0:
        print(''.join(p_list))
        continue

    while p_list[idx] >= p_list[idx2]:
        idx2 -= 1

    p_list[idx], p_list[idx2] = p_list[idx2],p_list[idx]
    ans = p_list[:idx+1]
    ans += list(reversed(p_list[idx+1:]))
    print(''.join(ans))