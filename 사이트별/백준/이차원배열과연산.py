from collections import deque
from copy import deepcopy

r,c,k = map(int, input().split( ))
r = r -1
c = c - 1
arr = [list(map(int, input().split( ))) for _ in range(3)]
sec = 0
ans = -1
tmpn = 0

while True:

    if 0<= r < len(arr) and 0 <= c < len(arr[0]) and arr[r][c] == k:
        ans = sec
        break

    if sec > 100:
        break

    if len(arr) >= len(arr[0]):
        arrList = []
        maxLen = 0
        arrParts = []
        newArr = []
        while arr:
            tmp = arr.pop(0)
            tmp.sort()
            first = tmp[0]
            cnt = 1
            nums = []
            total = []

            for i in range(1,len(tmp)):
                if tmp[i] == first:
                    cnt += 1
                else:
                    if first == 0:
                        first = tmp[i]
                        cnt = 1
                        continue
                    nums.append([first,cnt])
                    first = tmp[i]
                    cnt = 1
            if first != 0:
                nums.append([first,cnt])
                nums.sort(key = lambda  x: x[1])
            for n in nums:
                total.append(n[0])
                total.append(n[1])
            arrParts.append(total)
            if maxLen < len(total):
                maxLen = len(total)

        if maxLen > 100:
            maxLen = 100

        while arrParts:
            part = arrParts.pop(0)

            while len(part) < maxLen:
                part.append(0)
            if len(part) > maxLen:
                part = part[:maxLen]
            newArr.append(part)

        arr = deepcopy(newArr)

    else:
        convertArr = []
        for j in range(len(arr[0])):
            tmp = []
            for i in range(len(arr)):
                tmp.append(arr[i][j])
            convertArr.append(tmp)


        if 1 == 1:
            arrList = []
            maxLen = 0
            arrParts = []
            newArr = []

            while convertArr:
                tmp = convertArr.pop(0)
                tmp.sort()
                first = tmp[0]
                cnt = 1
                nums = []
                total = []
                for i in range(1, len(tmp)):
                    if tmp[i] == first:
                        cnt += 1
                    else:
                        if first == 0:
                            first = tmp[i]
                            cnt = 1
                            continue
                        nums.append([first, cnt])
                        first = tmp[i]
                        cnt = 1

                if first != 0:
                    nums.append([first, cnt])
                    nums.sort(key=lambda x: x[1])

                for n in nums:
                    total.append(n[0])
                    total.append(n[1])
                arrParts.append(total)

                if maxLen < len(total):
                    maxLen = len(total)

            if maxLen > 100:
                maxLen = 100

            while arrParts:
                part = arrParts.pop(0)

                while len(part) < maxLen:
                    part.append(0)

                if len(part) > maxLen:
                    part = part[:maxLen]

                newArr.append(part)

            arr = []
            for j in range(len(newArr[0])):
                tmp = []
                for i in range(len(newArr)):
                    tmp.append(newArr[i][j])
                arr.append(tmp)

    sec += 1

print(ans)