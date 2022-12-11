ans = 1

n, target = map(int, input().split(' '))
countryRank = dict()
countryMedals = list()

for _ in range(n):
    countryMedals.append(list(map(int, input().split(' '))))

countryMedals = sorted(countryMedals, key = lambda x:x[1], reverse=False)
while countryMedals:
    goldMax = countryMedals[0][1]
    goldTemp = list()

    while countryMedals and goldMax == countryMedals[0][1]:
        goldTemp.append(countryMedals.pop(0))

    goldTemp = sorted(goldTemp, key=lambda x: x[2], reverse=False)
    silverTemp = list()

    while goldTemp:
        silverMax = goldTemp[0][2]
        silverTemp = list()

        while goldTemp and silverMax == goldTemp[0][2]:
            silverTemp.append(goldTemp.pop(0))

        silverTemp = sorted(silverTemp, key=lambda x: x[3], reverse=False)

        while silverTemp:
            bronzeMax = silverTemp[0][3]
            bronzeTemp = list()
            firstAns = ans

            while silverTemp and bronzeMax == silverTemp[0][3]:
                countryRank[silverTemp.pop(0)[0]] = firstAns
                ans += 1

            if silverTemp and bronzeMax > silverTemp[0][3]:
                bronzeMax = silverTemp[0][3]
                countryRank[silverTemp.pop(0)[0]] = ans
                ans += 1

        if goldTemp and bronzeMax > goldTemp[0][2]:
            silverMax = goldTemp[0][2]
            countryRank[goldTemp.pop(0)[0]] = ans
            ans += 1

    if countryMedals and goldMax > countryMedals[0][1]:
        goldMax = countryMedals[0][1]
        countryRank[countryMedals.pop(0)[0]] = ans
        ans += 1

print(countryRank[target])


