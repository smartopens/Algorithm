def make_prime_list(num):
    for i in range(2, 1001):
        if prime_list[i]:
            for j in range(i + i, 1000001, i):
                prime_list[j] = False


prime_list = [True]*1000001
make_prime_list(1000000)

while True:
    n = int(input())
    find = False

    if n == 0:
        break

    for first in range(3, n//2+1,2):
        if prime_list[first]:
            second = n - first

            if prime_list[second]:
                print(n,"=",first,"+",second)
                find = True
                break

    if not find:
        print("Goldbach's conjecture is wrong.")