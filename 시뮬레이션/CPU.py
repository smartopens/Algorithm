n = int(input())
res = []
opcode = {'ADD': '00000','ADDC': '00001','SUB': '00010', 'SUBC': '00011',
          'MOV': '00100', 'MOVC': '00101', 'AND': '00110', 'ANDC': '00111',
          'OR': '01000', 'ORC': '01001', 'NOT': '01010', 'MULT': '01100',
          'MULTC': '01101', 'LSFTL': '01110', 'LSFTLC': '01111', 'LSFTR': '10000',
          'LSFTRC': '10001', 'ASFTR': '10010','ASFTRC': '10011', 'RL': '10100',
          'RLC': '10101', 'RR': '10110', 'RRC': '10111'
          }

for _ in range(n):
    opc, rd, ra, rbc = input().split(' ')
    add = ''
    add += opcode[opc]
    add += '0'
    rd = bin(int(rd))
    rd = rd[2:]
    while len(rd) != 3:
        rd = '0' + rd
    add += rd

    ra = bin(int(ra))
    ra = ra[2:]
    while len(ra) != 3:
        ra = '0' + ra
    add += ra

    if add[4] == '0':
        rbc = bin(int(rbc))
        rbc = rbc[2:]
        while len(rbc) != 3:
            rbc = '0' + rbc
        rbc += '0'
        add += rbc
    else:
        rbc = bin(int(rbc))
        rbc = rbc[2:]
        while len(rbc) != 4:
            rbc = '0' + rbc
        add += rbc
    res.append(add)

for i in res:
    print(i)