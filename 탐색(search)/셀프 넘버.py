selfNums = set()

def makeSelf(num):
    res = num

    strNum = str(num)
    for s in strNum:
        res += int(s)

    return res

for n in range(1,10000):
    num = n

    while makeSelf(num) < 10000:
        if makeSelf(num) in selfNums:
            break
        num = makeSelf(num)
        selfNums.add(num)

for i in range(1, 10000):
    if i not in selfNums:
        print(i)