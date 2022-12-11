T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    buildings = [0]*2 + list(map(int, input().split())) + [0]*2
    board = [[0]*1001 for _ in range(256)]
    answer = 0

    for i in range(2, n+2):
        if buildings[i-1] < buildings[i] and buildings[i-2] < buildings[i] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            answer += min(buildings[i] - buildings[i+1], buildings[i] - buildings[i+2],
                          buildings[i] - buildings[i - 1], buildings[i] - buildings[i-2])

    print("#",end='')
    print(test_case,answer)
