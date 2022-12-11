t = int(input())

for _ in range(t):
    i, string = map(str, (input().split(' ')))
    ans = ""
    for s in string:
        ans += s*int(i)
    print(ans)