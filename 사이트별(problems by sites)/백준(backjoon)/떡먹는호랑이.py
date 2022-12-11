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

"""
a, b

d = 1: a,b
d = 2: b,a+b : a + 2b
d = 3: a+b, a+2b : 2a + 3b
d = 4: a+2b, 2a+3b : 3a + 5b
d = 5: 2a+3b, 3a+5b : 5a + 8b
d = 6: 3a+5b, 5a+8b : 8a + 13b = k
...

px + qy = k

y = (k - px)//q

"""