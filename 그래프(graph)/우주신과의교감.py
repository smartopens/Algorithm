import math

n, m = map(int, input().split(' '))


def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]

    return math.sqrt(a ** 2 + b ** 2)


def get_parent(parent, n):
    if parent[n] == n:
        return parent[n]
    return get_parent(parent, parent[n])


def union(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a == b:
        return True
    else:
        return False


locations = []
parent = dict()
edges = []

for _ in range(n):
    x, y = map(int, input().split(' '))
    locations.append((x, y))

length = len(locations)

for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, length + 1):
    parent[i] = i

for _ in range(m):
    a, b = map(int, input().split(' '))
    union(parent, a, b)

edges.sort(key=lambda data: data[2])
result = 0

for edge in edges:
    a, b, dist = edge

    if not (find(parent, a, b)):
        result += dist
        union(parent, a, b)

print("%0.2f" % result)
