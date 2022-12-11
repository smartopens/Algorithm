a,b,n = map(int, input().split())
times = [[] for _ in range(10**6)]
blue_present = []
red_present = []

idx = 1

for _ in range(n):
    st, c, cnt = map(str, input().split())
    st, cnt = int(st), int(cnt)

    for i in range(cnt):
        if c == "B":
            st += a*i
            times[st].append(("B"))
        else:
            st += b*i
            times[st].append(("R"))


for i in range(len(times)):
    if times[i]:
        times[i].sort()

for time in times:
    for i in time:
        if i == "B":
            blue_present.append(idx)
        else:
            red_present.append(idx)
        idx += 1

print(len(blue_present))
for i in range(len(blue_present)):
    if i == len(blue_present)-1:
        print(blue_present[i])
        break
    print(blue_present[i], end=' ')
print(len(red_present))

for i in range(len(red_present)):
    if i == len(red_present)-1:
        print(red_present[i])
        break
    print(red_present[i], end=' ')

