n = int(input())

def is_prime(num):
    m = int(num**0.5)
    if num == 2 or num == 3:
        return True

    if num % 2 == 0 or num < 2:
        return False

    for i in range(3,m+1,2):
        if num % i == 0:
            return False

    return True

def is_pallen(num):
    num_str = str(num)
    num_len = len(num_str)
    m = num_len // 2

    for i in range(m):
        if num_str[i] != num_str[num_len-1-i]:
            return False

    return True

while True:

    if not is_prime(n):
        n += 1
        continue

    if not is_pallen(n):
        n += 1
        continue

    print(n)
    break


