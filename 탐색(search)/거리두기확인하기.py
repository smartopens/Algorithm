from collections import deque

def bfs(start, place):
    global answer
    x, y = start
    canGo = [(x - 1, y), (x - 2, y), (x + 1, y), (x + 2, y), (x, y - 1), (x, y - 2), (x, y + 1), (x, y + 2),
             (x - 1, y + 1),
             (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([start])
    visited = [[False] * 5 for _ in range(5)]

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != 'X' and (nx, ny) in canGo:

                if place[nx][ny] == 'P':
                    return False
                q.append((nx, ny))
    return True


def solution(places):
    global answer
    answerList = []

    for place in places:
        answer = 1
        q = deque([])
        isRight = True

        for row in range(5):
            for col in range(5):
                if place[row][col] == "P":
                    q.append(((row, col)))

        for start in q:
            isRight = bfs(start, place)
            if not isRight:
                answer = 0
                break

        answerList.append(answer)

    return answerList