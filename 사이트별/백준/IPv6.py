ipv6_pressed = input()
first_back = []
second_back = []
ipv6_split = ipv6_pressed.split(":")
idx = 0
second_flag = False
tmp = 0
s_idx = 0
ip_len = len(ipv6_split)

for i in range(ip_len):
    i_len = len(ipv6_split[i])
    if i_len == 0:
        tmp += 1

        if not second_flag:
            s_idx = i
            second_flag = True

    elif i_len != 4:
        first_back.append("0" * (4 - i_len) + ipv6_split[i])

    else:
        first_back.append(ipv6_split[i])


if tmp > 0:
    zero_tmp = []
    for _ in range(8-ip_len+tmp):
        zero_tmp.append("0000")

    second_back = first_back[:s_idx] + zero_tmp + first_back[s_idx:]
else:
    second_back = first_back

answer = ""

for i in range(8):

    if i == 7:
        answer += second_back[i]
        break
    answer += second_back[i] +":"

print(answer)