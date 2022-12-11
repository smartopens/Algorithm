n = int(input())
arr = [list(map(str, input().rstrip())) for _ in range(n)]
fList = []

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def Union(parent, a,b):
    global number

    a = find(parent,a)
    b = find(parent,b)

    if a != b:
        parent[b] = a
        number[a] += number[b]

for i in range(n):
    for j in range(n):
        if arr[i][j] == "Y" and [j,i] not in fList:
            fList.append([i,j])

print(fList)
parent = dict()
number = dict()

for x,y in fList:
    if x not in parent:
        parent[x] = x
        number[x] = 1

    if y not in parent:
        parent[y] = y
        number[y] = 1

    Union(parent,x,y)

if not fList:
    number = [0]

print(max(number))
