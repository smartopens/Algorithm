from itertools import combinations


def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    combi = []

    for i in range(1, col + 1):
        for com in combinations(range(col), i):
            combi.append(com)

    keys = []
    for i in combi:
        tmp = [tuple(items[key] for key in i) for items in relation]
        tmpSet = set(tmp)

        if len(tmpSet) == row:
            put = True

            for k in keys:
                if set(k).issubset(set(i)):
                    put = False
                    break

            if put:
                keys.append(i)
    answer = len(keys)
    return answer