n = int(input())
guilty_scores = list(map(int, input().split()))
relation = [list(map(int, input().split())) for _ in range(n)]
death = [0]*n
mapia = int(input())
answer = 0

def dfs_mapia(death,cnt,guilty_scores):
    global answer
    death = death[:]
    guilty_scores = guilty_scores[:]

    for i in range(n):
        if i == mapia or death[i] == 1:
            continue

        death[i] = 1
        guilty_scores_ori = guilty_scores[:]
        guilty_scores[i] = 0
        death_num = 0
        for j in range(n):
            if j == mapia:
                continue
            if death[j] == 1:
                death_num += 1

        if death_num == len(death) -1:
            if answer < cnt:
                answer = cnt

            death[i] = 0
            guilty_scores = guilty_scores_ori[:]
            continue

        for j in range(n):
            if i == j or death[j] == 1:
                continue
            guilty_scores[j] += relation[i][j]

        max_guilty = max(guilty_scores)
        kill_idx = 0

        for j in range(n):
            if guilty_scores[j] == max_guilty:
                kill_idx = j
                break

        if kill_idx == mapia:
            if answer < cnt:
                answer = cnt

            death[i] = 0
            guilty_scores = guilty_scores_ori[:]
            continue
        elif death_num + 1 == len(death) - 1:
            if answer < cnt :
                answer = cnt

            death[i] = 0
            guilty_scores = guilty_scores_ori[:]
            continue


        death[kill_idx] = 1
        tmp2 = guilty_scores[kill_idx]
        guilty_scores[kill_idx] = 0
        dfs_mapia(death,cnt+1,guilty_scores)
        death[i] = 0
        death[kill_idx] = 0
        guilty_scores[kill_idx] = tmp2
        guilty_scores = guilty_scores_ori[:]

    return

def dfs_people(death,cnt,guilty_scores):
    global answer
    death = death[:]
    guilty_scores = guilty_scores[:]

    death_num = 0
    for j in range(n):
        if j == mapia:
            continue
        if death[j] == 1:
            death_num += 1

    if death_num == len(death) -1:
        if answer < cnt:
            answer = cnt
        return

    max_guilty = max(guilty_scores)
    kill_idx = 0
    for j in range(n):
        if guilty_scores[j] == max_guilty:
            kill_idx = j
            break

    if kill_idx == mapia:
        if answer < cnt:
            answer = cnt
        return
    elif death_num + 1 == len(death) - 1:
        if answer < cnt:
            answer = cnt
        return
    else:
        death_num += 1

    death[kill_idx] = 1
    tmp2 = guilty_scores[kill_idx]
    guilty_scores[kill_idx] = 0

    for i in range(n):
        if i == mapia or death[i] == 1:
            continue

        death[i] = 1
        guilty_scores_ori = guilty_scores[:]
        guilty_scores[i] = 0

        if death_num + 1 == len(death) -1:
            if answer < cnt:
                answer = cnt

            death[i] = 0
            guilty_scores = guilty_scores_ori[:]
            continue

        for j in range(n):
            if death[j] == 1:
                continue
            guilty_scores[j] += relation[i][j]

        dfs_people(death,cnt+1,guilty_scores)
        death[i] = 0
        death[kill_idx] = 0
        guilty_scores[kill_idx] = tmp2
        guilty_scores = guilty_scores_ori[:]

    return

if n % 2 == 0:
    dfs_mapia(death,1,guilty_scores)

elif n % 2 == 1:
    dfs_people(death,0,guilty_scores)

print(answer)