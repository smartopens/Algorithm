from collections import deque

one = deque(map(int, input().strip()))
two = deque(map(int, input().strip()))
three = deque(map(int, input().strip()))
four = deque(map(int, input().strip()))
arrs = [one, two, three, four]

t = int(input())
q = deque()

for _ in range(t):
    x, y = map(int, input().split())
    q.append((x-1, y))


def Cycle(q):
    q.appendleft(q.pop())
    return q


def CounterCycle(q):
    q.append(q.popleft())
    return q


while q:
    s = [0,0,0,0]
    n, c = q.popleft()
    oriC = c

    for i in range(n+1,4):
        if arrs[i-1][2] == arrs[i][6]:
            break
        s[i] = -c
        c = -c

    for i in range(n-1,-1,-1):
        if arrs[i+1][6] == arrs[i][2]:
            break
        s[i] = -oriC
        oriC = -oriC

    for i in range(4):
        if s[i] == 1:
            arrs[i] = Cycle(arrs[i])
        elif s[i] == -1:
            arrs[i] = CounterCycle(arrs[i])


ans = 0
ans = arrs[0][0] + 2*arrs[1][0] + 4*arrs[2][0] + 8*arrs[3][0]

print(ans)
