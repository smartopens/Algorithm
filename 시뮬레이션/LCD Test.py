s, n = map(str, input().split(' '))
s = int(s)
len_ = len(n)

temp = ''
idx = 0
for num in n:
    if num == '0':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '1':
        for _ in range(s+3):
            temp += ' '

    elif num == '2':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '3':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '4':
        for _ in range(s+3):
            temp += ' '
    elif num == '5':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '6':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '7':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '8':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '9':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    if idx == len_ - 1:
        temp = temp[:-1]
    idx += 1
print(temp)

temp = ''
idx = 0
for num in n:
    if num == "1" or num == "2" or num == "3" or num == "7":
        for _ in range(s+1):
            temp += ' '
        temp += '|'
        temp += ' '
    elif num == "4" or num == "8" or num == "9" or num == "0":
        temp += '|'
        for _ in range(s):
            temp += ' '
        temp += '| '

    elif num == "5" or num == "6":
        temp += '|'
        for _ in range(s+2):
            temp += ' '

    if idx == len_ - 1:
        temp = temp[:-1]
    idx += 1

for _ in range(s):
    print(temp)

temp = ''
idx = 0
for num in n:
    if num == '0':
        temp += ' '
        for _ in range(s):
            temp += ' '
        temp += '  '
    elif num == '1':
        for _ in range(s+3):
            temp += ' '

    elif num == '2':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    elif num == '3':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    elif num == '4':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    elif num == '5':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    elif num == '6':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    elif num == '7':
        temp += ' '
        for _ in range(s):
            temp += ' '
        temp += '  '

    elif num == '8':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    elif num == '9':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    if idx == len_ - 1:
        temp = temp[:-1]
    idx += 1
print(temp)

temp = ''
idx = 0
for num in n:
    if num == "1" or num == "3" or num == "5" or num == "4" or num == "7" or num == "9":
        for _ in range(s + 1):
            temp += ' '
        temp += '|'
        temp += ' '
    elif num == "6" or num == "8" or num == "0":
        temp += '|'
        for _ in range(s):
            temp += ' '
        temp += '| '

    elif num == "2":
        temp += '|'
        for _ in range(s + 2):
            temp += ' '
    if idx == len_ - 1:
        temp = temp[:-1]
    idx += 1

for _ in range(s):
    print(temp)

temp = ''
idx = 0
for num in n:
    if num == '0':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '1':
        for _ in range(s+3):
            temp += ' '

    elif num == '2':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '3':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '4':
        for _ in range(s+3):
            temp += ' '
    elif num == '5':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '6':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '7':
        temp += ' '
        for _ in range(s):
            temp += ' '
        temp += '  '
    elif num == '8':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '
    elif num == '9':
        temp += ' '
        for _ in range(s):
            temp += '-'
        temp += '  '

    if idx == len_ - 1:
        temp = temp[:-1]
    idx += 1
print(temp)
