from collections import deque
from copy import deepcopy


def bfs(cases, info, n):
    total = 0
    q = deque([[0, 0, n, cases]])
    Lion = []

    while q:
        idx, score, m, case = q.popleft()

        if idx >= 11 or m <= 0:
            lion, apeech = 0, 0
            for i in range(11):
                if case[i] > info[i]:
                    lion += (10 - i)
                else:
                    if info[i] > 0:
                        apeech += (10 - i)
            dist = lion - apeech

            if dist > 0 and total < dist:
                Lion = case
                total = dist
            elif lion > apeech and total == dist:
                for i in range(10, -1, -1):
                    if case[i] != Lion[i]:
                        if case[i] > Lion[i]:
                            Lion = case
                        break

            continue
        case2 = deepcopy(case)

        if m - (info[idx] + 1) >= 0:
            tmp = deepcopy(case)
            tmp[idx] = info[idx] + 1
            q.append([idx + 1, score + (10 - idx), m - (info[idx] + 1), tmp])
        elif idx == 10 and 0 < m < (info[idx] + 1):
            tmp = deepcopy(case)
            tmp[idx] = m
            q.append([idx + 1, score, 0, tmp])

        q.append([idx + 1, score, m, case2])

    return Lion


def solution(n, info):
    cases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Lion = bfs(cases, info, n)

    if Lion:
        answer = Lion
    else:
        answer = [-1]

    return answer