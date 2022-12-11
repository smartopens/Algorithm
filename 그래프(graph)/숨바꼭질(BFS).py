from collections import deque

n, k = map(int, input().split(' '))
max = 100001
array = [0] * max

def bfs(v):
    q = deque([v])

    while q:
        now_pos = q.popleft()

        if now_pos == k:
            return array[now_pos]

        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < max and not (array[next_pos]):

                if next_pos == k:
                    return array[now_pos] + 1
                else:
                    array[next_pos] = array[now_pos] + 1
                    q.append(next_pos)

result_time = bfs(n)
print(result_time)