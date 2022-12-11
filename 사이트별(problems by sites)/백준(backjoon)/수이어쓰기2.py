n, k = map(int, input().split())
multi_1 = 10
sum_a = 0
a = 9
idx = 1
answer = 0
tmp_k = 0

while sum_a + a < k:
    sum_a += a
    a *= 10
    idx += 1

rest_k = k - sum_a
new_n = 10**(idx-1)-1
new_n_tmp = (rest_k // idx)
rest_k -= (rest_k // idx)*idx
last_idx = 0

while rest_k >0:
    rest_k -= 1
    last_idx += 1

last_num = new_n + new_n_tmp


if last_num <= n:
    if last_num == n and last_idx > 0:
        print(-1)
    else:
        if last_idx == 0:
            print(int(str(last_num)[-1]))
        else:
            print(int(str(last_num+1)[last_idx-1]))
else:
    print(-1)