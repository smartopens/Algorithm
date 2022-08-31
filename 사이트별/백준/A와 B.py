s = input()
t = input()
is_ok = True
idx = len(s)
ori_len_s = len(s)
ori_len_t = len(t)

for _ in range(ori_len_t -ori_len_s ):
    is_ok_tmp = False

    if t[idx] == "A":
        idx += 1
        s += "A"
        is_ok_tmp = True
    else:
        new_s = ""
        s_len = len(s)
        for i in range(s_len):
            new_s += s[s_len-i-1]
        s= new_s + "B"
        idx += 1

if s != t:
    print(0)
else:
    print(1)




