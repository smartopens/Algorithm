test = int(input())

for _ in range(test):
    n = int(input())
    bit = []

    while n > 0:
        bit.append(n%2)
        n //= 2
    len_ = len(bit)

    for i in range(len_):
        if bit[i] == 1:
            print(i, end =" ")

