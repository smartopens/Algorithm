stringMap = []
maxCol = 0

for _ in range(5):
    temp = input()
    stringMap.append(list(temp))
    maxCol = max(maxCol, len(temp))

result = [""]*maxCol

for string in stringMap:
    idx = 0
    while string:
        str_ = string.pop(0)
        result[idx]+= str_
        idx += 1

ans = ""

for i in result:
    ans += i

print(ans)
# ans = ""
# for i in result:
#     ans += ''.join(i)
