m, n = map(int, input().split())
m += 1
n += 1
k = int(input())
stores = [list(map(int, input().split())) for _ in range(k)]
c_a, c_d = map(int, input().split())

if c_a == 1:
    c_r = 0
    c_c = c_d
elif c_a == 2:
    c_r = n - 1
    c_c = c_d
elif c_a == 3:
    c_r = c_d
    c_c = 0
elif c_a == 4:
    c_r = c_d
    c_c = m - 1

ans = 0

for s in range(k):

    s_a, s_d = stores[s][0], stores[s][1]

    if s_a == 1:
        s_r = 0
        s_c = s_d
    elif s_a == 2:
        s_r = n - 1
        s_c = s_d

    elif s_a == 3:
        s_r = s_d
        s_c = 0

    elif s_a == 4:
        s_r = s_d
        s_c = m - 1

    while True:
        left_d = 0
        right_d = 0

        ori_r, ori_c = c_r, c_c
        is_left = False
        is_right = False

        if c_a == 1:

            while c_c != m - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c += 1
                left_d += 1

            while c_r != n - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r += 1
                left_d += 1

            while c_c != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c -= 1
                left_d += 1

            while c_r != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r -= 1
                left_d += 1

            c_r, c_c = ori_r, ori_c

            while c_c != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c -= 1
                right_d += 1

            while c_r != n - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r += 1
                right_d += 1
            while c_c != m - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c += 1
                right_d += 1
            while c_r != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r -= 1
                right_d += 1

            ans += min(left_d, right_d)
            c_r, c_c = ori_r, ori_c


        elif c_a == 2:
            while c_c != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c -= 1
                left_d += 1

            while c_r != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r -= 1
                left_d += 1

            while c_c != m - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c += 1
                left_d += 1
            while c_r != n - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r += 1
                left_d += 1

            c_r, c_c = ori_r, ori_c

            while c_c != m - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c += 1
                right_d += 1

            while c_r != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r -= 1
                right_d += 1
            while c_c != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c -= 1
                right_d += 1
            while c_r != n - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r += 1
                right_d += 1

            ans += min(left_d, right_d)
            c_r, c_c = ori_r, ori_c

        elif c_a == 3:

            while c_r != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r -= 1
                left_d += 1

            while c_c != m - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c += 1
                left_d += 1

            while c_r != n - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r += 1
                left_d += 1

            while c_c != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c -= 1
                left_d += 1

            c_r, c_c = ori_r, ori_c
            while c_r != n - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r += 1
                right_d += 1
            while c_c != m - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c += 1
                right_d += 1
            while c_r != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r -= 1
                right_d += 1
            while c_c != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c -= 1
                right_d += 1

            ans += min(left_d, right_d)
            c_r, c_c = ori_r, ori_c

        elif c_a == 4:
            while c_r != n - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r += 1
                left_d += 1
            while c_c != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c -= 1
                left_d += 1

            while c_r != 0 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_r -= 1
                left_d += 1

            while c_c != m - 1 and not is_left:
                if s_r == c_r and s_c == c_c:
                    is_left = True
                    break
                c_c += 1
                left_d += 1

            c_r, c_c = ori_r, ori_c

            while c_r != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r -= 1
                right_d += 1
            while c_c != 0 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c -= 1
                right_d += 1

            while c_r != n - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_r += 1
                right_d += 1
            while c_c != m - 1 and not is_right:
                if s_r == c_r and s_c == c_c:
                    is_right = True
                    break
                c_c += 1
                right_d += 1
            ans += min(left_d, right_d)
            c_r, c_c = ori_r, ori_c

        break

print(ans)
