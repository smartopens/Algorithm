from itertools import permutations
import sys
from collections import defaultdict

n = int(sys.stdin.readline())

def consider_case(idx,string):

    if idx == word_len:
        print(string)
        return

    for k,v in visit_dict.items():
        if v > 0:
            visit_dict[k] -= 1
            consider_case(idx+1,string + k)
            visit_dict[k] += 1

for _ in range(n):
    word = sys.stdin.readline().strip()
    word_list = list(word)
    word_list.sort()
    word_len = len(word)
    answer_set = set()
    visit_dict = defaultdict(int)

    for i in word_list:
        visit_dict[i] += 1

    consider_case(0,"")