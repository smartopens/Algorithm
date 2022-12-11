from collections import deque
#import numpy as np
from copy import deepcopy
from sys import stdin
from itertools import combinations

input = stdin.readline

n,m = map(int,input().split())
original_map = [list(map(int,input().split())) for _ in range(n)]
virus=[]
target_num =0

#virus_locate
for i in range(n):
    for j in range(n):
        if(original_map[i][j]==2):
            virus.append((i,j,0))
        elif(original_map[i][j]==0):
            target_num+=1

#virus_combinations
c_virus = list(combinations(virus,m))

def check_map():
    global n,maps
    for i in range(n):
        for j in range(n):
            if(maps[i][j]==0):
                return False
    return True


def bfs(active_virus):
    global n,maps,ans
    visited =[[0]*n for _ in range(n)]
    queue=deque()
    queue.extend(active_virus)
    for i in queue:
        i_,j_,qq = i
        visited[i_][j_]=1

    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    cnt=0
    while(queue):
        ti,tj,tcnt = queue.popleft()
        for i in range(4):
            ni = ti+di[i]
            nj = tj+dj[i]
            if(ni>=0 and ni<n and nj<n and nj>=0):
                if(maps[ni][nj]!=1 and visited[ni][nj]==0):
                    visited[ni][nj]=1
                    if(maps[ni][nj]==0):
                        maps[ni][nj]=2
                        cnt = tcnt +1
                        if(cnt>ans):
                            break
                    queue.append((ni,nj,tcnt+1))

    return cnt


ans = 1e9
for i in c_virus:
    maps= deepcopy(original_map)
    res = bfs(i)
    if(check_map()):
        ans = min(res,ans)

print(ans if ans!=1e9 else -1)