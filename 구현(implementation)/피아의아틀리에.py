from itertools import permutations

n = int(input())
ingredients = dict()

def rotation(arr):
    n = 4
    newArr = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            newArr[c][n-1-r] = arr[r][c]

    return newArr

for i in range(n):
    arr = list()
    arr2 = list()
    for j in range(2):
        for _ in range(4):
            if j == 0:
                temp = list(map(int,input().split()))
                arr.append(temp)
            else:
                temp = list(map(str,input().split()))
                arr2.append(temp)

    for k in range(4):
        for l in range(4):
            arr[k][l] = str(arr[k][l]) + arr2[k][l]

        ingredients[i] = arr

newIngredients = dict()

for i in range(n):
    newIngredients[i] = []

for i in range(n):
    origin = ingredients[i]
    newIngredients[i].append(origin)
    for _ in range(3):
        origin = rotation(origin)
        newIngredients[i].append(origin)

sequenceList = []
result = 0
start = [(0,0),(0,1),(1,0),(1,1)]

print(newIngredients)

for per in permutations(list(range(n)),3):
    #위치
    for i in range(4):
        for j in range(4):
            for k in range(4):
                #회전
                for l in range(4):
                    for m in range(4):
                        for n in range(4):
                            basket = [["0W"] * 5 for _ in range(5)]
                            score = 0
                            color = ""
                            first = newIngredients[per[0]][l]
                            second = newIngredients[per[1]][m]
                            third = newIngredients[per[2]][n]

                            firstStart = start[i]
                            secondStart = start[j]
                            thirdStart = start[k]

                            for r in range(4):
                                for c in range(4):
                                    score = int(basket[firstStart[0]+r][firstStart[1]+c][0])\
                                            + int(first[r][c][:-1])

                                    if score < 0:
                                        score = 0
                                    elif score > 9:
                                        score = 9

                                    color = first[r][c][-1]
                                    basket[firstStart[0]+r][firstStart[1]+c] = str(score) + color

                                    #if firstStart == (0,0):
                                        #print(score)
                                        #print(color)
                                        #print(basket[firstStart[0]+r][firstStart[1]+c])
                            for r in range(4):
                                for c in range(4):
                                    score = int(basket[secondStart[0]+r][secondStart[1]+c][0])\
                                            + int(second[r][c][:-1])

                                    if score < 0:
                                        score = 0
                                    elif score > 9:
                                        score = 9

                                    color = second[r][c][-1]
                                    basket[secondStart[0]+r][secondStart[1]+c] = str(score) + color

                            for r in range(4):
                                for c in range(4):
                                    score = int(basket[thirdStart[0]+r][thirdStart[1]+c][0])\
                                            + int(third[r][c][:-1])

                                    if score < 0:
                                        score = 0
                                    elif score > 9:
                                        score = 9

                                    color = third[r][c][-1]
                                    basket[thirdStart[0]+r][thirdStart[1]+c] = str(score) + color

                            tempRes = 0
                            for r in range(5):
                                for c in range(5):
                                    if basket[r][c][-1] == "R":
                                        tempRes += int(basket[r][c][:-1])*7
                                    elif basket[r][c][-1] == "B":
                                        tempRes += int(basket[r][c][:-1])*5
                                    elif basket[r][c][-1] == "G":
                                        tempRes += int(basket[r][c][:-1])*3
                                    elif basket[r][c][-1] == "Y":
                                        tempRes += int(basket[r][c][:-1])*2

                            result = max(result, tempRes)

    print(basket)
    print(per)

print(result)





