test = int(input())

for _ in range(test):
    data = input()
    d_size = len(data)
    stack = []
    idx = 0

    for i in data:
        if i == '<':
            if idx > 0:
                idx -= 1

        elif i == '>':
           if idx < len(stack):
                idx += 1

        elif i == '-':
            if idx > 0 and stack:
                stack.pop(idx-1)
                idx -= 1
        else:
            stack.insert(idx,i)
            idx += 1

    print(''.join(stack))
