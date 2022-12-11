n = int(input())
answers = []

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    for i in range(3, int(pow(num, 1 / 2)) + 1, 2):
        if num % i == 0:
            return False

    return True

def dfs(idx,string_num):
    global answers
    if idx == n+1:
        answers.append(int(string_num))
        return

    for i in range(10):
        if idx == 1:
            string_tmp = i
        else:
            string_tmp = int(string_num)*10 + i
        if is_prime(string_tmp):
            dfs(idx+1, str(string_tmp))
    return

dfs(1,"")
answers_num = list(map(int, answers))
answers_num = sorted(answers_num)
for i in answers_num:
    print(i)

