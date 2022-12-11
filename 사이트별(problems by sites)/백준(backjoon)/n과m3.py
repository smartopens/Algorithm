n, m = map(int, input().split())
nums = list(range(1,n+1))
answers = set()

def dfs(idx,answer_str):
    global answers,nums

    if idx == m:
        tmp = []
        answers.add(answer_str)
        return

    for i in range(n):
        dfs(idx+1,answer_str+str(nums[i]))


dfs(0,"")

answers = list(answers)
answers.sort()

for answer in answers:
    for i in range(len(answer)):
        if i == len(answer) - 1:
            print(int(answer[i]), end = '')
            continue
        print(int(answer[i]), end = ' ')
    print()
