gameMap = {"0000": "D","0001": "C","0011": "B",
           "0111": "A","1111": "E"}
inputCases = []

for _ in range(3):
    tempStr = list(map(str,input().split(' ')))
    tempStr.sort()
    inputCases.append(''.join(tempStr))

for i in inputCases:
    print(gameMap[i])
    # inputCases