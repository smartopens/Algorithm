a, b = map(str, input().split())
a_list = list(a)
b_list = list(b)
a_list.sort(reverse=True)
int_b = int(b)
a_len = len(a_list)
b_len = len(b_list)
a_vi = set()
idx = 0
is_small = False
new_num  = []

for i in range(b_len):
    if i > a_len -1:
        break

    for j in range(a_len):
        if not is_small and a_list[j] <= b_list[i] and j not in a_vi:
            a_tmp = a_list[j]
            if a_tmp == b_list[i]:
                new_num.append(str(a_tmp))
            else:
                is_small = True
                new_num.append(str(a_tmp))
            a_vi.add(j)
            break

        if is_small and j not in a_vi:
            new_num.append(str(a_list[j]))
            a_vi.add(j)
            break

answer = -1

if len(''.join(new_num)) == len(a_list) and int(''.join(new_num)) <= int_b:
    new_num_int =  int(''.join(new_num))
    ori_num = new_num[:]
    is_ok = False

    if new_num_int == int_b:
        possible_nums = []
        for j in range(len(new_num)-1,0,-1):
            for k in range(j-1,-1,-1):
                new_num[j],new_num[k] = new_num[k],new_num[j]
                new_num_tmp = int(''.join(new_num))

                if new_num_tmp < int_b:
                    possible_nums.append(new_num_tmp)

                new_num[j], new_num[k] = new_num[k], new_num[j]

        if possible_nums:
            answer = max(possible_nums)
        print(answer)

    else:
        answer = new_num_int
        print(answer)
else:
    print(answer)



