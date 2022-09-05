n, k = map(int, input().split())
str_list = []

def dfs(str_tmp, num_sum):
    if num_sum == n:
        str_split = str_tmp.replace(',','+')[:-1]
        str_list.append(str_split)
        return

    elif num_sum > n:
        return

    dfs(str_tmp + str(1) + ",", num_sum + 1)
    dfs(str_tmp + str(2) + ",", num_sum + 2)
    dfs(str_tmp + str(3) + ",", num_sum + 3)
    return

dfs("",0)
str_list.sort()

if len(str_list) >= k:
    print(str_list[k-1])
else:
    print(-1)