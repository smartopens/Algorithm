import sys
sys.setrecursionlimit(10**5)

def count_answer(str_list):
    global answer
    stack = []

    for i in str_list:
        if i == "{":
            stack.append(i)
        else:
            if not stack:
                answer += 1
                stack.append("{")
            elif stack and stack[-1] == "{":
                stack.pop()

    if stack:
        answer += len(stack) // 2
    return


order = 1
while True:
    answer = 0
    input_string = input()
    if input_string[0] == "-":
        break

    string_list = list(input_string)
    string_len = len(string_list)
    count_answer(string_list)

    print("{}. {}".format(order,answer))
    order += 1