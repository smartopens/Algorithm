import sys

dp = [1] + [0]*7
d = int(input())
answer = 0

def move(state):
    tmp = [0]*8

    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2]+ state[3]
    tmp[2] = state[0] + state[1]+ state[3]+ state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]

    for i in range(8):
        tmp[i] = tmp[i]%1000000007
    return tmp

for _ in range(d):
    dp = move(dp)

print(dp[0])