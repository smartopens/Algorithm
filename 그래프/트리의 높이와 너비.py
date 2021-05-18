N = int(input())


class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node


def mid_order(node, level):
    global depth_level, x

    depth_level = max(depth_level, level)

    if node.left_node != -1:
        mid_order(tree[node.left_node], level + 1)
    width_max[level] = max(width_max[level], x)
    width_min[level] = min(width_min[level], x)
    x += 1
    if node.right_node != -1:
        mid_order(tree[node.right_node], level + 1)


depth_level = 1
x = 1
level = 1
width_max = [0] * (N + 1)
width_min = [N] * (N + 1)

tree = {}

for i in range(1, N + 1):
    tree[i] = Node(i, -1, -1)

for i in range(1, N + 1):

    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node

    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

root = 0
for i in range(1, N + 1):
    if tree[i].parent == -1:
        root = i

mid_order(tree[root], 1)

result_width = width_max[1] - width_min[1] + 1
result_level = 1

for i in range(2, depth_level + 1):
    width = width_max[i] - width_min[i] + 1

    if result_width < width:
        result_width = width
        result_level = i

print(result_level, result_width)
