t = int(input())

for _ in range(t):
    m,n,x,y = map(int, input().split())
    year = 1
    mul_x = x
    is_solve = False

    while True:
        if (mul_x - y)%n == 0:
            is_solve = True
            break

        if mul_x >= m*n:
            break

        mul_x += m

    if is_solve:
        print(mul_x)
    else:
        print(-1)