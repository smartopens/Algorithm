T = int(input())

for t_c in range(T):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    min_l = min(len(a_list), len(b_list))
    max_l = max(len(a_list), len(b_list))

    a_long = False
    if len(b_list) == min_l:
        a_long = True

    max_sum = 0

    for i in range(max_l-min_l+1):
        tmp_sum = 0

        for j in range(min_l):
            if a_long:
                tmp_sum += b_list[j]*a_list[i+j]
            else:
                tmp_sum += a_list[j]*b_list[i+j]
        if max_sum < tmp_sum:
            max_sum = tmp_sum

    print("#{0} {1}".format(t_c+1,max_sum))


