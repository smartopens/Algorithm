t = int(input())
# Great 9 codes
for _ in range(t):
    t_idx = int(input())
    score_list = list(map(int, input().split()))
    num_list = [[0,i] for i in range(101)]
    for i in range(1000): num_list[score_list[i]][0] += 1
    num_list.sort(key = lambda x: (x[0],x[1]), reverse=True)
    print("#{} {}".format(t_idx, num_list[0][1]))