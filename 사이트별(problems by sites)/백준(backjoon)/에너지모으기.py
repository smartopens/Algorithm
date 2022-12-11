n = int(input())
dolls = list(map(int, input().split()))
max_score = 0

def dfs(dolls,score):
    global max_score

    doll_len = len(dolls)
    if doll_len == 2:
        if score > max_score:
            max_score = score
        return
    
    for i in range(doll_len):
        if i == 0 or i == doll_len-1:
            continue
        plus = dolls[i-1] * dolls[i+1]
        tmp = dolls.pop(i)
        dfs(dolls,score + plus)
        dolls.insert(i,tmp)

    return

dfs(dolls,0)
print(max_score)