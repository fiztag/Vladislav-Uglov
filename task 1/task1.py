from itertools import cycle
n,m=int(input()),int(input())
a=[]
for i in range(1,n+1):
    a.append(i)
b=1
m1=m
for l in cycle(a):
    print(b)
    b=b+m-1
    if b>n:
        while b>n:
            b=b-n
    if b==1:
        break