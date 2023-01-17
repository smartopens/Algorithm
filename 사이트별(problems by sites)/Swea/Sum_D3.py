
for _ in range(10):
    t = int(input())
    num_array = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    # 행 합 비교
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += num_array[r][c]
        if max_sum < row_sum:
            max_sum = row_sum
    # 열 합 비교
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += num_array[r][c]
        if max_sum < col_sum:
            max_sum = col_sum

    # 대각선1 비교
    tmp_sum1 = 0
    for i in range(100):
        tmp_sum1 += num_array[i][i]
    if max_sum < tmp_sum1:
        max_sum = tmp_sum1

    # 대각선2 비교
    tmp_sum2 = 0
    for i in range(100):
        tmp_sum2 += num_array[i][99-i]
    if max_sum < tmp_sum2:
        max_sum = tmp_sum2

    print("#{} {}".format(t, max_sum))