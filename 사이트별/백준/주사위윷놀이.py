from copy import  deepcopy

nums = list(map(int, input().split()))

road1 = [0] + [i for i in range(2,41,2)] + [0]
road2 = [0] + [13,16,19,25,30,35,40] + [0]
road3 = [0] + [22,24,25,30,35,40] + [0]
road4 = [0] + [28,27,26,25,30,35,40] + [0]
answer = 0
places = [0,0,0,0]
states = [[1,0,0,0,0] for _ in range(4)]
doll = 0

def dfs(doll,places,states,case,score):
    global answer
    cango = [1,1,1,1]

    if case == 10:
        answer = max(answer, score)
        return

    for i in range(4):
        if cango[i] == 1 and states[i][4] == 0:
            if i == 0:
                notOk = False
                now = places[i]
                scoreTmp = score
                stateTmp = deepcopy(states)

                if states[i][0] == 1 and places[i] == 5:
                    stateTmp[i][0] = 0
                    stateTmp[i][1] = 1
                    next = nums[case]
                    places[i] = next
                    score += road2[next]

                elif states[i][0] == 1 and places[i] == 10:
                    stateTmp[i][0] = 0
                    stateTmp[i][2] = 1
                    next = nums[case]
                    places[i] = next
                    score += road3[next]

                elif states[i][0] == 1 and places[i] == 15:
                    stateTmp[i][0] = 0
                    stateTmp[i][3] = 1
                    next = nums[case]
                    places[i] = next
                    score += road4[next]
                else:
                    ori = now

                    for j in range(4):
                        if states[i][j] == 1:
                            state = j

                    next = now + nums[case]

                    if state == 0:
                        if next > 20:
                            next = 21
                            stateTmp[i][4] = 1
                        else:
                            score += road1[now]
                    if state == 1 and next > 7:
                        if next > 7:
                            next = 8
                            stateTmp[i][4] = 1
                        else:
                            score += road2[next]
                    if state == 2:
                        if next > 6:
                            next = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road3[next]
                    if state == 3:
                        if next > 7:
                            next = 8
                            stateTmp[i][4] = 1
                        else:
                            score += road4[next]

                    places[i] = next

                notOk = False

                for j in range(4):
                    if states[doll][j] == 1:
                        state = j

                for j in range(4):
                    if j == i:
                        continue

                    if states[j][state] == 1 and places[j] == next:
                        notOk = True
                        break

                if notOk:
                    places[i] = now
                    score = tmp
                    continue

                dfs(i, places, stateTmp, case+1, score)
                places[i] = now
                score = tmp

            elif i == 1:
                if states[i][0] == 1 and places[i] == 5:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][1] = 1
                    place = places[i]
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 5
                        states[i][1] = 0
                        states[i][0] = 1
                        continue
                    dfs(i, places, states, case + 1, score + road2[nums[case]])
                    places[i] = 5
                    states[i][1] = 0
                    states[i][0] = 1

                elif states[i][0] == 1 and places[i] == 10:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][2] = 1
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 10
                        states[i][0] = 1
                        states[i][2] = 0
                        continue
                    dfs(i, places, states, case + 1, score + road3[nums[case]])
                    places[i] = 10
                    states[i][0] = 1
                    states[i][2] = 0
                elif states[i][0] == 1 and places[i] == 15:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][3] = 1
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 5
                        states[i][0] = 1
                        states[i][3] = 0
                        continue
                    dfs(i, places, states, case + 1, score + road4[nums[case]])
                    places[i] = 5
                    states[i][0] = 1
                    states[i][3] = 0
                else:
                    now = places[i]
                    ori = now
                    for j in range(4):
                        if states[i][j] == 1:
                            state = j

                    stateTmp = deepcopy(states)
                    now += nums[case]
                    tmp = score

                    if state == 0:
                        if now > 20:
                            now = 20
                            stateTmp[i][4] = 1
                        else:
                            score += road1[now]
                    if state == 1 and now > 7:
                        if now > 7:
                            now = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road2[now]
                    if state == 2:
                        if now > 6:
                            now = 6
                            stateTmp[i][4] = 1
                        else:
                            score += road3[now]
                    if state == 3:
                        if now > 7:
                            now = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road4[now]

                    places[i] = now
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = ori
                        score = tmp
                        continue
                    dfs(i, places, stateTmp, case + 1, score)
                    places[i] = ori
                    score = tmp

            elif i == 2:
                if states[i][0] == 1 and places[i] == 5:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][1] = 1
                    place = places[i]
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 5
                        states[i][1] = 0
                        states[i][0] = 1
                        continue
                    dfs(i, places, states, case + 1, score + road2[nums[case]])
                    places[i] = 5
                    states[i][1] = 0
                    states[i][0] = 1

                elif states[i][0] == 1 and places[i] == 10:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][2] = 1
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 10
                        states[i][0] = 1
                        states[i][2] = 0
                        continue
                    dfs(i, places, states, case + 1, score + road3[nums[case]])
                    places[i] = 10
                    states[i][0] = 1
                    states[i][2] = 0
                elif states[i][0] == 1 and places[i] == 15:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][3] = 1
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 5
                        states[i][0] = 1
                        states[i][3] = 0
                        continue
                    dfs(i, places, states, case + 1, score + road4[nums[case]])
                    places[i] = 5
                    states[i][0] = 1
                    states[i][3] = 0
                else:
                    now = places[i]
                    ori = now
                    for j in range(4):
                        if states[i][j] == 1:
                            state = j

                    stateTmp = deepcopy(states)
                    now += nums[case]
                    tmp = score

                    if state == 0:
                        if now > 20:
                            now = 20
                            stateTmp[i][4] = 1
                        else:
                            score += road1[now]
                    if state == 1 and now > 7:
                        if now > 7:
                            now = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road2[now]
                    if state == 2:
                        if now > 6:
                            now = 6
                            stateTmp[i][4] = 1
                        else:
                            score += road3[now]
                    if state == 3:
                        if now > 7:
                            now = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road4[now]

                    places[i] = now
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = ori
                        score = tmp
                        continue
                    dfs(i, places, stateTmp, case + 1, score)
                    places[i] = ori
                    score = tmp
            else:
                if states[i][0] == 1 and places[i] == 5:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][1] = 1
                    place = places[i]
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 5
                        states[i][1] = 0
                        states[i][0] = 1
                        continue
                    dfs(i, places, states, case + 1, score + road2[nums[case]])
                    places[i] = 5
                    states[i][1] = 0
                    states[i][0] = 1

                elif states[i][0] == 1 and places[i] == 10:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][2] = 1
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 10
                        states[i][0] = 1
                        states[i][2] = 0
                        continue
                    dfs(i, places, states, case + 1, score + road3[nums[case]])
                    places[i] = 10
                    states[i][0] = 1
                    states[i][2] = 0
                elif states[i][0] == 1 and places[i] == 15:
                    now = places[i]
                    states[i][0] = 0
                    places[i] = nums[case]
                    states[i][3] = 1
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = 5
                        states[i][0] = 1
                        states[i][3] = 0
                        continue
                    dfs(i, places, states, case + 1, score + road4[nums[case]])
                    places[i] = 5
                    states[i][0] = 1
                    states[i][3] = 0
                else:
                    now = places[i]
                    ori = now
                    for j in range(4):
                        if states[i][j] == 1:
                            state = j

                    stateTmp = deepcopy(states)
                    now += nums[case]
                    tmp = score

                    if state == 0:
                        if now > 20:
                            now = 20
                            stateTmp[i][4] = 1
                        else:
                            score += road1[now]
                    if state == 1 and now > 7:
                        if now > 7:
                            now = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road2[now]
                    if state == 2:
                        if now > 6:
                            now = 6
                            stateTmp[i][4] = 1
                        else:
                            score += road3[now]
                    if state == 3:
                        if now > 7:
                            now = 7
                            stateTmp[i][4] = 1
                        else:
                            score += road4[now]

                    places[i] = now
                    notOk = False

                    for j in range(4):
                        if states[doll][j] == 1:
                            state = j

                    for j in range(4):
                        if j == i:
                            continue

                        if states[j][state] == 1 and places[j] == place:
                            notOk = True
                            break
                    if notOk:
                        places[i] = ori
                        score = tmp
                        continue
                    dfs(i, places, stateTmp, case + 1, score)
                    places[i] = ori
                    score = tmp

    return

dfs(doll,places,states,0,0)
print(answer)