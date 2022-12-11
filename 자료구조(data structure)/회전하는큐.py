from collections import deque
import copy
ans = 0

n, m = map(int, input().split(' '))
orderList = list(map(int, input().split(' ')))
storage = deque(list(i for i in range(1,n+1)))


while m and orderList:
    left = 0
    right = 0

    # if orderList[0] == storage[0]:
    #     orderList.pop(0)
    #     storage.popleft()
    #     m -= 1

    tempStorageleft = deque(copy.deepcopy(storage))
    while orderList and orderList[0] != tempStorageleft[0]:
        tempStorageleft.append(tempStorageleft.popleft())
        left += 1

    tempStorageRight = deque(copy.deepcopy(storage))
    while orderList and orderList[0] != tempStorageRight[0]:
        tempStorageRight.appendleft(tempStorageRight.pop())
        right += 1

    if right >= left:
        storage = deque(copy.deepcopy(tempStorageleft))
        ans += left
        storage.popleft()
        if orderList:
            orderList.pop(0)
        m -= 1
    else:
        storage = deque(copy.deepcopy(tempStorageRight))
        ans += right
        storage.popleft()
        if orderList:
            orderList.pop(0)
        m -= 1

print(ans)