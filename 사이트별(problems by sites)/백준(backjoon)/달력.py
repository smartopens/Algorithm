n = int(input())
times = []
for _ in range(n):
    x,y = map(int, input().split())
    times.append([x,y])

times = sorted(times,key = lambda x:(x[0],-x[1]))
print(times)