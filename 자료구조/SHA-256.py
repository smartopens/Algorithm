n_size = input()
n_set = set(map(int, input().split(' ')))
m_size = input()
m_list = list(map(int, input().split(' ')))

for i in m_list:
    if i in n_set:
        print('1')
    else:
        print('0')
