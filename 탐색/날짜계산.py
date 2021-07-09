e, s, m = map(int, input().split(' '))

result = 0

e_n = 0
s_n = 0
m_n = 0

while True:
    result += 1
    e_n += 1
    s_n += 1
    m_n += 1

    if e_n > 15:
        e_n = 1

    if s_n > 28:
        s_n = 1

    if m_n > 19:
        m_n = 1

    if (e_n == e and s_n == s and m_n == m):
        print(result)
        break
