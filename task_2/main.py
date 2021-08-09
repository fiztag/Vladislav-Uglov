from math import sqrt
F1=open('кординаты.txt')
str = F1.readline().split()
x1,y1 = float(str[0]) ,float(str[1])
str = F1.readline().split()
r=float(str[0])
F1.close()
F1=open('точки.txt')
for i in range(0,100):
    str = F1.readline().split()
    if not str:
        break
    x2,y2=float(str[0]),float(str[1])
    x2=x2-x1
    y2=y2-y1
    h=sqrt(x2**2+y2**2)
    if h==r:
        print('0')
    elif h>r:
        print('2')
    else :
        print('1')
F1.close()