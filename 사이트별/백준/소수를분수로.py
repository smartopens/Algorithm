t = int(input())

def gcd(num,base):
    max_n = base

    if base == 0:
        return num

    return gcd(base,num%base)

for _ in range(t):
    num = input()[2:]
    isRe = False
    idx = 0

    for i in num:
        if i == "(":
            isRe = True
            break

        idx += 1

    if not isRe:
        num_len = len(num)
        base = "1" + "0" * num_len
        num,base = int(num), int(base)
        gcd_num = gcd(num,base)
        print("{}/{}".format(num//gcd_num,base//gcd_num))
    else:
        re_num = num[idx+1:-1]
        base = ""
        if idx > 0:
            p_num = num[:idx]
            num = p_num + re_num
            base = "9"*len(re_num) + "0"*len(p_num)
            num = int(num)
            num -= int(p_num)
            base = int(base)
        else:
            num = re_num
            base = "9" * len(re_num)
            num = int(num)
            base = int(base)
        gcd_num = gcd(num,base)
        print("{}/{}".format(num//gcd_num, base//gcd_num))


