from itertools import combinations

l, c = map(int, input().split(' '))

essence = ['a', 'i', 'o', 'u', 'e']

string_in = input().split(' ')
string_in.sort()

for problem in combinations(string_in, l):
    count = 0

    for i in problem:
        if i in essence:
            count += 1

    if count >= 1 and count + 2 <= l:
        print(''.join(problem))