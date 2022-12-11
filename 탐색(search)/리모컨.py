n = int(input())
m = int(input())

if m >= 1:
    m_arr = list(map(str, input().split()))

count = 0

def check(n):
    num = list(str(n))
    for i in num:
        if i in m_arr:
            return False
    return True

count = abs(n - 100)

for i in range(500001):
    if check(i):
        count = min(count, len(str(i)) + abs(i - n))

print(count)