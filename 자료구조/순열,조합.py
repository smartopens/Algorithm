import time

def permutation1(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    per_list = []

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            per_list.append(chosen[:])
            return

        # 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return per_list

def permutations2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

def permutation3(array, r, prefix="nothing"):
    for i in range(len(array)):
        if array[i] == prefix: continue
        if r == 1:
            yield [array[i]]
        else:
            prefix = array[i]
            for next in permutation3(array, r-1, prefix):
                yield [array[i]] + next

# 조합
def combination1(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    com_list = []

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            com_list.append(chosen[:])
            return

    # 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

    return com_list

def combination2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combination2(array[i+1:], r-1):
                yield [array[i]] + next

# 방법1
print("재귀함수 permutations")
start_time = time.time()
for i in permutation1(range(500), 2): pass
end_time = time.time()
print(end_time - start_time)
print()

# 방법2
print("Generation permutations")
start_time = time.time()
for i in permutations2(list(range(500)), 2): pass
end_time = time.time()
print(end_time - start_time)
print()

# 방법3
print("Generation permutations2")
start_time = time.time()
for i in permutation3(list(range(500)), 2): pass
end_time = time.time()
print(end_time - start_time)
print()

# 조합

# 방법1
print("재귀함수 combinations")
start_time = time.time()
for i in combination1(range(500), 2): pass
end_time = time.time()
print(end_time - start_time)
print()

# 방법2
print("Generation combinations")
start_time = time.time()
for i in combination2(range(500), 2): pass
end_time = time.time()
print(end_time - start_time)
print()


def permutation_test(num_list, m_idx):
    for i in range(len(num_list)):
        if m_idx == 1:
            yield [num_list[i]]
        else:
            for next in permutation_test(num_list[:i] + num_list[i+1:], m_idx-1):
                yield [num_list[i]] + next

def combination_test(num_list, m_idx):
    for i in range(len(num_list)):
        if m_idx == 1:
            yield [num_list[i]]
        else:
            for next in combination_test(num_list[i+1:], m_idx-1):
                yield [num_list[i]] + next



orders = list(range(1,5))

per = permutation_test(orders,3)
com = combination_test(orders,3)
print(list(per))
print(list(com))
