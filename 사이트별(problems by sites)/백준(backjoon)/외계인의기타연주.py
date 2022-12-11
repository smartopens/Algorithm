import heapq

melody_h_dict = dict()
n, p_num = map(int, input().split())
ans = 0

for _ in range(n):
    h, p = map(int, input().split())

    if h not in melody_h_dict:
        melody_h_dict[h] = [p]
        ans += 1
    else:
        now_melody = melody_h_dict[h]
        if now_melody[-1] < p:
            melody_h_dict[h].append(p)
            ans += 1
        elif now_melody[-1] == p:
            continue
        else:
            while melody_h_dict[h] and melody_h_dict[h][-1] > p:
                melody_h_dict[h].pop()
                ans += 1
            if melody_h_dict[h] and melody_h_dict[h][-1] < p:
                melody_h_dict[h].append(p)
                ans += 1
            elif not melody_h_dict[h]:
                melody_h_dict[h] = [p]
                ans += 1

print(ans)

