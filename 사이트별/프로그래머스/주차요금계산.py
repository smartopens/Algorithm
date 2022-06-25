def strToInt(string):
    string = string.split(":")

    return int(string[0]) * 60 + int(string[1])


def solution(fees, records):
    answer = []
    cars = dict()
    carsTotal = dict()
    cost = []

    for re in records:
        re = re.split()

        if re[1] in carsTotal:
            carsTotal[re[1]].append([re[0], re[2]])
        else:
            carsTotal[re[1]] = [[re[0], re[2]]]

    carsTotal = sorted(carsTotal.items())

    for i in carsTotal:
        if i[0] not in cars:
            cars[i[0]] = i[1]

    for k, v in cars.items():
        if len(v) % 2 != 0:
            cars[k].append(["23:59", "OUT"])

    for k, v in cars.items():
        time = 0

        for i in range(0, len(v), 2):
            time += abs(strToInt(v[i][0]) - strToInt(v[i + 1][0]))

        cost.append(time)

    for time in cost:
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            time -= fees[0]
            if time // fees[2] != time / fees[2]:
                time = time // fees[2] + 1
            else:
                time = time // fees[2]
            answer.append(fees[1] + time * fees[3])

    return answer