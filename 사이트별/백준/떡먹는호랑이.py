d, k = map(int, input().split())
p = 0
q = 1

for i in range(d-2):
    p,q = q, p+q

x = 0

while True:
    x += 1

    if (k - p*x)%q == 0:
        print(x)
        print((k - p*x)//q)
        break

