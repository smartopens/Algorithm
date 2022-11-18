string = input()
opers = []
nums = []
ans = 0
total = ["+"]

for i in string:
    if i == "-":
        opers.append("-")
    elif i == "+":
        opers.append("+")

first = string.split("+")

for f in first:
    second = f.split("-")
    for s in second:
        nums.append(int(s))

while nums:
    total.append(nums.pop(0))
    if opers:
        total.append(opers.pop(0))


while total:
    oper = total.pop(0)

    if total:
        if oper == "-":
            while total and total[0] != "-":
                if total[0] == "+":
                    total.pop(0)
                    continue

                ans -= total.pop(0)
        else:
            ans += total.pop(0)

print(ans)
