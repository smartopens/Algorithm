import sys
from collections import deque
sys.setrecursionlimit(10**7)

n = int(input())
parent_dict = {}
child_dict = {}
graph = [[] for _ in range(n+1)]
is_win = False

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q= deque([1])
vi = [0]*(n+1)
vi[1] = 1
while q:
    v = q.popleft()
    for e in graph[v]:
        if vi[e] == 0:
            parent_dict[e] = v
            if v not in child_dict:
                child_dict[v] = [e]
            else:
                child_dict[v].append(e)
            vi[e] = 1
            q.append(e)

game_doll = [0]*(n+1)
q= deque([1])
vi = [0]*(n+1)
vi[1] = 1
while q:
    v = q.popleft()
    for e in graph[v]:
        if vi[e] == 0:
            if e in child_dict and child_dict[e]:
                vi[e] = 1
                q.append(e)
            else:
                game_doll[e] += 1

game_sum = sum(game_doll)
now_node = []

for i in range(len(game_doll)):
    if game_doll[i] > 0:
        now_node.append(i)

def dfs(game_doll,game_n,game_sum,now_node):
    global is_win
    if game_sum <= 0:
        if game_n % 2 == 0:
            is_win = True
        return

    copy_node = now_node[:]
    for i in now_node:
        if game_doll[i] > 0 and parent_dict[i]:
            if parent_dict[i] == 1:
                game_doll[i] -= 1
                copy_node.remove(i)
                dfs(game_doll,game_n+1,game_sum-1,copy_node)
                copy_node.append(i)
                game_doll[i] += 1
                continue
            game_doll[parent_dict[i]] += 1
            game_doll[i] -= 1
            copy_node.append(parent_dict[i])
            copy_node.remove(i)
            dfs(game_doll,game_n+1,game_sum-1,copy_node)
            copy_node.remove(parent_dict[i])
            copy_node.append(i)
            game_doll[parent_dict[i]] -= 1
            game_doll[i] += 1

    return

dfs(game_doll,1,game_sum,now_node)

if is_win:
    print("Yes")
else:
    print("No")
