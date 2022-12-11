n = int(input())
sold_book = dict()

for _ in range(n):
    book = input()

    if book not in sold_book:
        sold_book[book] = 1
    else:
        sold_book[book] += 1

target = max(sold_book.values())
array = []

for key, value in sold_book.items():
    if value == target:
        array.append(key)

array.sort()

print(array[0])
