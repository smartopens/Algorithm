import re

t = int(input())
answers = []

for _ in range(t):
    sign = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)

    if m: print("YES")
    else: print("NO")