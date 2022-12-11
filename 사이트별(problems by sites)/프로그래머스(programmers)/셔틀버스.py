from copy import deepcopy


def toStr(n):
    h = n // 60
    m = n % 60

    if h < 10:
        s = "0" + str(h) + ":"
    else:
        s = str(h) + ":"

    if m < 10:
        s += "0" + str(m)
    else:
        s += str(m)

    return s


def toInt(s):
    h, m = map(int, s.split(":"))

    return h * 60 + m


def solution(n, t, m, timetable):
    ct = 0
    ctMax = toInt("24:00")
    bs = toInt("09:00")
    timeDict = {}
    intAns = 0

    for ti in timetable:
        tn = toInt(ti)
        if tn not in timeDict:
            timeDict[tn] = ["crew"]
        else:
            timeDict[tn].append("crew")

    timeDict2 = deepcopy(timeDict)

    while ct < ctMax:
        bo = toInt("09:00")
        bs = toInt("09:00")
        timeDict3 = deepcopy(timeDict)
        if ct in timeDict3:
            timeDict3[tn].append("con")
        else:
            timeDict3[ct] = ["con"]

        timeDict2 = {}
        orderList = sorted(timeDict3.keys())
        for o in orderList:
            timeDict2[o] = timeDict3[o]

        conOk = False
        busSet = set()
        m2 = m

        for ni in range(n):
            bs = bo + ni * t

            for ti in timeDict2:
                if m2 == 0:
                    break

                if ti <= bs:
                    if timeDict2[ti]:
                        tmp = timeDict2[ti]

                        if tmp and tmp.pop(0) == "con":
                            conOk = True
                        timeDict2[ti] = tmp
                        m2 -= 1
        if conOk:
            intAns = max(intAns, ct)

        ct += 1
    print(toStr(intAns))
    ans = ''
    return ans
solution(2,1,2,["09:10", "09:09", "08:00"])