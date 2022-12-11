from collections import deque

t = int(input())

for _ in range(t):
    order = input()
    Flag,error = True, False
    n = int(input())
    num_list = input()
    if len(num_list) == 2:
        nums = []
    else:
        nums = deque(list(map(int,num_list[1:-1].split(','))))

    for o in order:
        if o == "R":
            if Flag:
                Flag = False
            else:
                Flag = True
        else:
            if len(nums) > 0:
                if Flag:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                print("error")
                error = True
                break
    if error:
        continue
    nums = list(nums)
    if not Flag:
        nums.reverse()

    print("[", end= '')
    for i in range(len(nums)):
        if i == len(nums) -1:
            print(nums[i], end='')
            continue
        print(nums[i], end=',')
    print("]")

