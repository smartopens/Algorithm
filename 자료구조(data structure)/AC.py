t = int(input())

for _ in range(t):
    opers = input()
    n = int(input())
    if n > 0:
        string = input()
        nums = list(map(int, string[1:-1].split(",")))
    else:
        nums = []
    rNum = 0
    isError = False

    for i in opers:
        if i == "R":
            rNum += 1
        else:
            if rNum % 2 == 1:
                if nums:
                    nums.pop()
                else:
                    isError = True
                    break
            else:
                if nums:
                    nums.pop(0)
                else:
                    isError = True
                    break
    if isError:
        print("error")
    else:
        if rNum % 2 == 1:
            nums.reverse()

        print("[", end = '')
        if nums:
            for i in nums:
                if i == nums[-1]:
                    print(str(i), end='')
                    continue
                print(str(i), end=',')
        print("]")