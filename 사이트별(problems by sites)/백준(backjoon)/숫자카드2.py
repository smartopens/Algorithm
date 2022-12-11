from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
card_dict = defaultdict(int)

for i in cards:
    card_dict[i] += 1

m = int(input())
cases = list(map(int, input().split()))
ans = []

for i in cases:
    ans.append(card_dict[i])

for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end = '')
        break
    print(ans[i], end = ' ')