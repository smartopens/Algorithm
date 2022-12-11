from collections import deque

paper = [list(map(int, input().split())) for _ in range(10)]
n = len(paper[0])
color_papers_attached = [5]*5
ans_num = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
is_ok = True

def bfs():
    global color_papers_attached

    vi = [[0] * n for _ in range(n)]
    new_attachs = []
    q = deque([(deque([]))])
    max_cnt = 0

    for _ in range(1):
        for r in range(n):
            for c in range(n):
                if paper[r][c] == 1 and vi[r][c] == 0:
                    vi[r][c] = 1
                    new_tmp = []
                    p_size1 = 1

                    while p_size1 < 6:
                        is_done = False

                        for idx in range(p_size1):
                            if r+ idx >= n or c + idx >= n:
                                is_done = True
                                break
                            if paper[r+idx][c+idx] == 0:
                                is_done = True
                                break
                        if is_done:
                            break
                        p_size1 += 1
                        if p_size1 >= 6:
                            p_size1 = 5

                    right_size = p_size1
                    print(right_size,p_size1,r,c)
                    for i in range(right_size):
                        for j in range(right_size):
                            new_tmp.append((i+r,j+c))

                    if new_tmp:
                        new_attachs.append(new_tmp)

    new_attachs = sorted(new_attachs, key=lambda x: len(x))
    print(new_attachs)
    for i in range(len(new_attachs)-1,-1,-1):
        if color_papers_attached[int(pow(len(new_attachs[i]),1/2))-1] > 0:
            color_papers_attached[int(pow(len(new_attachs[i]), 1 / 2)) - 1] -= 1
            return new_attachs[i]
            break


while True:

    attach_check = 0

    for i in paper:
        attach_check += sum(i)

    if attach_check == 0 or sum(color_papers_attached) == 0:
        break

    attach_paper = bfs()
    print(attach_paper)
    if not attach_paper:
        is_ok = False
        break

    for r,c in attach_paper:
        paper[r][c] = 0

    for p in paper:
        print(p)
    print()
    ans_num += 1

if is_ok:
    print(ans_num)
else:
    print(-1)

