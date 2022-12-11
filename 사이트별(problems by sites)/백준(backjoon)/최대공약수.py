n = int(input())
a_dict = dict()
b_dict = dict()

def divide_num(num,s):
    ori_num = num
    if s == 0:
        while num != 1:
            is_done = False

            if num % 2 == 0:
                num //= 2
                if 2 not in a_dict:
                    a_dict[2] = 1
                else:
                    a_dict[2] += 1

            elif num % 3 == 0:
                num //= 3

                if 3 not in a_dict:
                    a_dict[3] = 1
                else:
                    a_dict[3] += 1
            else:
                first = False

                for i in range(5,int(pow(num,1/2))+1,2):
                    if num % i == 0:
                        first = True

                        if i not in a_dict:
                            a_dict[i] = 1
                        else:
                            a_dict[i] += 1
                        num //= i

                if first == False and num != 1:
                    if num not in a_dict:
                        a_dict[num] = 1
                    else:
                        a_dict[num] += 1

                    num = 1


    else:
        while num != 1:
            if num % 2 == 0:
                num //= 2
                if 2 not in b_dict:
                    b_dict[2] = 1
                else:
                    b_dict[2] += 1

            elif num % 3 == 0:
                num //= 3

                if 3 not in b_dict:
                    b_dict[3] = 1
                else:
                    b_dict[3] += 1
            else:
                first = False

                for i in range(5,int(pow(num,1/2))+1,2):
                    if num % i == 0:
                        first = True

                        if i not in b_dict:
                            b_dict[i] = 1
                        else:
                            b_dict[i] += 1
                        num //= i

                if not first and num != 1:

                    if num not in b_dict:
                        b_dict[num] = 1
                    else:
                        b_dict[num] += 1
                    num = 1


    return

a_nums = list(map(int,input().split()))
for i in a_nums:
    divide_num(i,0)

m = int(input())
b_nums = list(map(int,input().split()))
for i in b_nums:
    divide_num(i,1)

answer = 1
for k, v in a_dict.items():
    if k in b_dict:
        answer = answer*(k**min(v,b_dict[k]))

#print(a_dict)
#print(b_dict)
ans_str = str(answer)
if len(ans_str) > 9:
    print(ans_str[-9:])
else:
    print(ans_str)
