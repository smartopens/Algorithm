from collections import deque

t = int(input())

for _ in range(t):
    order = input()
    left,error = True, False
    n = int(input())
    num_tmp = input()
    if len(num_tmp) == 2:
        nums = []
    else:
        nums = deque(list(map(int,num_tmp[1:-1].split(','))))

    for o in order:
        if o == "R":
            if left:
                left = False
            else:
                left = True
        else:
            if len(nums) > 0:
                if left:
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
    if not left:
        nums.reverse()

    print(nums)

