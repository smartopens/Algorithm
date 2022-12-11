import sys

n = int(input())
cranes = list(map(int, input().split(' ')))

m = int(input())
boxes = list(map(int, input().split(' ')))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

cranes.sort(reverse=True)
boxes.sort(reverse=True)

positions = [0] * (n)
checked = [False] * (m)

time = 0
count = 0

while True:

    if count == len(boxes):
        break

    for i in range(n):
        while positions[i] < len(boxes):

            if not (checked[positions[i]]) and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                count += 1
                positions[i] += 1
                break

            positions[i] += 1
    time += 1

print(time)