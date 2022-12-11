import sys
sys.setrecursionlimit(10**6)

problem = input()
ans = 0
flag = 0

def dfs(stack,idx,ans_tmp):
    global ans, flag

    if idx == len(problem):
        if stack:
            flag = 1
        else:
            flag = 0
        return

    if problem[idx] == "(":
        stack.append("(")
        dfs(stack,idx+1,ans_tmp*2)
    elif problem[idx] == "[":
        stack.append("[")
        dfs(stack,idx+1,ans_tmp*3)
    elif problem[idx] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            if problem[idx - 1] == "(":
                ans += ans_tmp
            dfs(stack,idx+1,ans_tmp//2)
        else:
            flag = 1
            return
    else:
        if stack and stack[-1] == "[":
            stack.pop()
            if problem[idx - 1] == "[":
                ans += ans_tmp
            dfs(stack,idx+1,ans_tmp//3)
        else:
            flag = 1
            return

dfs([],0,1)

if flag == 0:
    print(ans)
else:
    print(0)
