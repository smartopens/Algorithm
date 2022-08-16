s = input()
p = input()
len_p = len(p)
ans = 0
end = False

for i in range(len(s)):
    is_ok = True
    if end:
        break
    for j in range(len_p):
        if i+j >= len(s):
            is_ok = False
            end = True
            break
        if s[i+j] != p[j]:
            is_ok = False
            break

    if is_ok:
        ans = 1
        break

print(ans)