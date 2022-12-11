n, k = map(int, input().split())
ans = 0
is_ok = True

while True:
    n_bin = bin(n)

    if n_bin[2:].count("1") <= k:
        break

    n += 1
    ans += 1

print(ans)

