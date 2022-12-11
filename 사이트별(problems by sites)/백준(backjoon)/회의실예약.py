n, m = map(int, input().split())
meeting_dict = dict()

for _ in range(n):
    meeting_dict[input()] = list()

for _ in range(m):
    room, s_time, e_time = map(str, input().split())
    s_time, e_time = int(s_time), int(e_time)
    meeting_dict[room].append((s_time, e_time))

meeting_dict = sorted(meeting_dict.items(), key = lambda x:x[0])

meeting_dict_sorted = dict()
for meeting in meeting_dict:
    meeting_dict_sorted[meeting[0]] = meeting[1]

for k,v in meeting_dict_sorted.items():
    v.sort(key = lambda x:x[0])


m_len = len(meeting_dict_sorted)
idx = 0

for k,v in meeting_dict_sorted.items():
    s,e = 9,0

    print("Room {}:".format(k))
    vi = [0]*10
    first_flag = False
    for s_t,e_t in v:
        for i in range(s_t,e_t):
            vi[i-9] = 1
    vi[9] = 1
    tmp = []
    if sum(vi) == 10:
        print("Not available")
    else:
        s,e = 0,0
        flag = False
        cnt = 0

        for i in range(len(vi)):
            if vi[i] == 0 and not flag:
                flag = True
                s = i
                e = i
                continue
            if vi[i] == 0 and flag:
                e = i
            elif vi[i] == 1 and flag:
                tmp.append((s,e+1))
                flag = False

        if flag:
            tmp.append((s,e))

        num = len(tmp)
        print(str(num),"available:")
        for i,j in tmp:
            i,j = i+9,j+9
            if i == 9:
                i = "09"

            i, j = str(i), str(j)

            print("{}-{}".format(i,j))


    idx += 1

    if idx == m_len:
        continue

    print("-----")
