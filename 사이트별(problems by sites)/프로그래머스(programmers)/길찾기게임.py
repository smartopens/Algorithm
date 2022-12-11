from copy import deepcopy
import sys

sys.setrecursionlimit(10 ** 6)
pre_order = []
post_order = []


def pre_search(node):
    pre_order.append(node.index)

    if node.left:
        pre_search(node.left)

    if node.right:
        pre_search(node.right)


def post_search(node):
    if node.left:
        post_search(node.left)

    if node.right:
        post_search(node.right)

    post_order.append(node.index)


class Tree:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.left = None
        self.right = None


def solution(nodeinfo):
    nodeinfo_idx = [info + [idx + 1] for idx, info in enumerate(nodeinfo)]
    nodeinfo_idx.sort(key=lambda x: (x[1], x[0]), reverse=True)
    root_node = None

    for node in nodeinfo_idx:
        if not root_node:
            root_node = Tree(node[0], node[1], node[2])
        else:
            cur_node = root_node
            x = node[0]

            while True:
                if x < cur_node.x:
                    if cur_node.left:
                        cur_node = cur_node.left
                        continue
                    else:
                        cur_node.left = Tree(node[0], node[1], node[2])
                        break

                elif x > cur_node.x:
                    if cur_node.right:
                        cur_node = cur_node.right
                        continue
                    else:
                        cur_node.right = Tree(node[0], node[1], node[2])
                        break

    pre_search(root_node)
    post_search(root_node)
    answer = []
    answer.append(pre_order)
    answer.append(post_order)

    return answer