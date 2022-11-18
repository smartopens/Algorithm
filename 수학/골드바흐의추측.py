import math

def makePrimes(max_,isPrime):

    for i in range(2, int(math.sqrt(max_))+1):
        if isPrime[i] == False:

            for j in range(i+i, max_+1, i):
                isPrime[j] = True

    return isPrime

isPrime = [False]*500001
isPrime = makePrimes(500000, isPrime)


while True:
    n = int(input())

    if n == 0:
        break
    max_ = 0
    resA,resB = 0,0

    for num in range(2, n//2 +1):
        a = num
        if isPrime[a]:
            continue
        b = n - a

        if isPrime[b]:
            continue

        resA, resB = a,b
        break

    if resA == 0 and resB == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(n,"=",resA,"+",resB)

