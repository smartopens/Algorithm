from collections import deque

n = int(input())
tops = list(map(int, input().split()))
dp = [0] * n
records = deque([])
max_h = 0
ans = []
stack = []

for i in range(n):

    if i != 0:
        while stack and stack[-1][1] < tops[i]:
            stack.pop()

        if not stack:
            stack.append([i + 1, tops[i]])
            ans.append(0)
        else:
            stack.append([i + 1, tops[i]])
            ans.append(stack[-2][0])
    else:
        stack.append([i+1,tops[0]])
        ans.append(0)


for i in range(n):
    if i == n-1:
        print(ans[i], end='')
        break

    print(ans[i], end = ' ')

