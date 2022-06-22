import sys
from copy import deepcopy

sys.setrecursionlimit(10000000)
answer = 1


def canGo(s, prev, graph):
    nextNode = [x for x in prev if x != s]
    nextNode.extend(graph[s])

    return nextNode


def dfs(s, maxSheep, dist, prev, n, sheep, graph, info):
    global answer

    answer = max(answer, sheep)
    nextNode = canGo(s, prev, graph)

    if maxSheep == 0 or not nextNode or dist <= 0:
        return

    for e in nextNode:
        if info[e] == 0:
            dfs(e, maxSheep - 1, dist + 1, nextNode, n, sheep + 1, graph, info)
        else:
            dfs(e, maxSheep, dist - 1, nextNode, n, sheep, graph, info)

    return


def solution(info, edges):
    global answer
    maxSheep = info.count(0)
    n = len(info)
    graph = [[] for _ in range(n)]

    for edge in edges:
        x, y = edge
        graph[x].append(y)

    dfs(0, maxSheep, 1, [0], n, 1, graph, info)

    return answer