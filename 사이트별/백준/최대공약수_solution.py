n = int(input())
a_dict = dict()
b_dict = dict()
a,b = 1,1

def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a

a_nums = list(map(int,input().split()))
for i in a_nums:
    a *= i

m = int(input())
b_nums = list(map(int,input().split()))
for i in b_nums:
    b *= i
answer = gcd(a,b)
ans_str = str(answer)
if len(ans_str) > 9:
    print(ans_str[-9:])
else:
    print(ans_str)