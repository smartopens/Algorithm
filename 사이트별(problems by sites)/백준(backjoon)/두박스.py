y1,x1, y2,x2 = map(int, input().split())
x3, y3 = x1, y2
x4, y4 = x2, y1
b1,a1, b2,a2 = map(int, input().split())
a3, b3 = a1, b2
a4, b4 = a2, b1

print(x1,x2,x3,x4)
print(a1,a2,a3,a4)
print(y1,y2,y3,y4)
print(b1,b2,b3,b4)

if ((x3 == a4 and y3 == b4) or (x1 == a2 and y1 == b2) or (x2 == a1 and y2 == b1) or (x4 == a3 and y4 == b3)):
    print("POINT")
elif (y2 == b1 and x2 < b4 < x3) or (y2 == b1 and x2 < b1 < x3) or (x1 == a2 and y1 < b1 < y3) or (x1 == a2 and y1 < b2 < y3):
    print("LINE")
elif (y1 == b2 and x1 < a2 < x4) or (y1 == b2 and x1 < a3 < x4) or (a1 == x2 and y2 < b1 < y4) or (a1 == x2 and y2 < b3 < y4):
    print("LINE")
elif (y2 < b1) or (x1 < a2) or (b2 < y1) or(a1 < x2):
    print("NULL")
else:
    print("FACE")


"""
x1~x2 를 width_list에
y1~y2 를 height_list에 담는다.
Point: 양배열에 2가되는점이 2개 있을경우 ,
LINE: X1~X2의 상대거릿값 == width list 길이, y1~y2 == hieght len ,
NULL: 하나이상이 1로만 이루어졌을 경우
FACE: 그 욋값

"""