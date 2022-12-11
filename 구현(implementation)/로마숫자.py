roma_num1 = input()
roma_num2 = input()

roma_limit_1 = ["V","L","D"]
roma_limit_2 = ["I","X","C","M"]
roma_limit_3 = ["IV","IX","XL","XC","CD","CM"]

roma_limit_3_vi = set()
roma_to_num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
               "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}

roma_order = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
ans_num = 0
ans_roma = ""
len_ans = 1e9
is_jump = False

for i in range(len(roma_num1)):
    if is_jump:
        is_jump = False
        continue

    if i == len(roma_num1)-1:
        ans_num += roma_to_num[roma_num1[i]]
        continue

    if roma_to_num[roma_num1[i]] >= roma_to_num[roma_num1[i + 1]]:
        ans_num += roma_to_num[roma_num1[i]]
    else:
        ans_num += (roma_to_num[roma_num1[i] + roma_num1[i + 1]])
        is_jump = True

is_jump = False
for i in range(len(roma_num2) - 1):
    if is_jump:
        is_jump = False
        continue

    if i == len(roma_num2)-1:
        ans_num += roma_to_num[roma_num2[i]]
        continue

    if roma_to_num[roma_num2[i]] >= roma_to_num[roma_num2[i + 1]]:
        ans_num += roma_to_num[roma_num2[i]]
    else:
        ans_num += (roma_to_num[roma_num2[i] + roma_num2[i + 1]])
        is_jump = True

def dfs(num,limit1,limit2,limit3,string):
    global ans_roma,len_ans
    if num <= 0:

        if len_ans > len(string):
            ans_roma = string
            len_ans = len(string)
        return
    is_done = False


    for i in range(13):
        is_ok = True

        if num >= roma_to_num[roma_order[i]]:
            now_num = roma_to_num[roma_order[i]]

            if len(string)>1 and string[-1] == roma_order[i]:
                if roma_order[i] in roma_limit_1:
                    is_ok = False

                if roma_order[i] in roma_limit_2:
                    limit2 += 1
                    if limit2 >= 4:
                        is_ok = False
                        limit2 = 0

            if not is_ok:
                continue

            if roma_order[i] not in roma_limit_3:
                dfs(num - roma_to_num[roma_order[i]],limit1,limit2,limit3,string + roma_order[i])
                break
            else:
                if roma_order[i] not in roma_limit_3_vi:
                    if string[i] == "IV" and roma_order[i] == "IX"\
                            or string[i] == "IX" and roma_order[i] == "IV":
                        is_ok = False
                    elif string[i] == "XL" and roma_order[i] == "XC"\
                            or string[i] == "XC" and roma_order[i] == "XL":
                        is_ok = False
                    elif string[i] == "CD" and roma_order[i] == "CM"\
                            or string[i] == "CM" and roma_order[i] == "CD":
                        is_ok = False
                    if is_ok:
                        continue
                    roma_limit_3_vi.add(roma_order[i])
                    dfs(num - roma_to_num[roma_order[i]],limit1,limit2,1,string + roma_order[i])
                    break

    return

dfs(235,0,0,0,"")
print(553)
print(ans_roma)
