prime_nums = [True]*(100001)
prime_nums[0],prime_nums[1] = False,False

for i in range(2,int(100000**(1/2)),1):
    if prime_nums[i]:
        for j in range(i+i,100001,i):
            prime_nums[j] = False

while True:
    string = input()
    string_len = len(string)
    len_max = min(5,string_len)

    if string == '0':
        break

    max_prime = 1

    for i in range(1,len_max+1,1):
        for j in range(string_len-i+1):
            num = int(string[j:j+i])
            if prime_nums[num] and max_prime < num:
                max_prime = num

    print(max_prime)



