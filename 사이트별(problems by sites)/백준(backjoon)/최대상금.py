T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def dfs(cnt,n):
    global ans
    is_done = False

    if cnt == 0:
        ans = max(ans, int(''.join(n)))
        is_done = True

    if not is_done:
        for i in range(n_len):
            for j in range(i+1, n_len):
                n[i], n[j] = n[j], n[i]
                tmp = ''.join(n)

                if visited.get((tmp,cnt),1):
                    visited[(tmp,cnt)] = 0
                    dfs(cnt-1)

                n[i], n[j] = n[j], n[i]



for test_case in range(1, T + 1):
    n, k = map(str, input().split())
    k = int(k)
    n = list(n)
    ans = 0
    n_len = len(n)
    if len(n) == 1:
        print("#", end = '')
        print(test_case, n[0])
        continue

    visited = {}
    dfs(k)

    print("#{} {}".format(test_case, ans))



